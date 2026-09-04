#!/usr/bin/env python3
"""
tests/test_registry.py — drift test for tools/registry.py's state-machine invariants (MUST-10).

Tier: finite_diagnostic (each test asserts on the real return code / stderr of the real
cmd_* functions, run against an isolated tmp registry — not a description of intended behavior).

Runs the module's own functions directly (no subprocess), with REPO_ROOT / REGISTRY_YAML /
REGISTRY_JSON / LIBRARY_MD / RELEASE_APPROVAL_TXT monkeypatched onto the loaded module to point
at a fresh tmp directory per test, so this never reads or writes the real
registry/RESEARCH_REGISTRY.yaml.
"""
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PY = REPO_ROOT / "tools" / "registry.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("registry_under_test", REGISTRY_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class RegistryStateMachineTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        tmp_root = Path(self._tmp.name)
        (tmp_root / "registry").mkdir()

        self.reg = _load_module()
        self.reg.REPO_ROOT = tmp_root
        self.reg.REGISTRY_YAML = tmp_root / "registry" / "RESEARCH_REGISTRY.yaml"
        self.reg.REGISTRY_JSON = tmp_root / "registry" / "RESEARCH_REGISTRY.json"
        self.reg.LIBRARY_MD = tmp_root / "RESEARCH_LIBRARY.md"
        self.reg.RELEASE_APPROVAL_TXT = tmp_root / "registry" / "RELEASE_APPROVAL.txt"

    # -- helpers --------------------------------------------------------

    def _run(self, fn, ns):
        out, err = io.StringIO(), io.StringIO()
        code = 0
        try:
            with redirect_stdout(out), redirect_stderr(err):
                fn(ns)
        except SystemExit as e:
            code = e.code or 0
        return code, out.getvalue(), err.getvalue()

    def _new(self, title="t"):
        code, out, err = self._run(
            self.reg.cmd_new, SimpleNamespace(title_th=title, title_en=title)
        )
        self.assertEqual(code, 0, err)
        entries = self.reg.load_registry()["entries"]
        return entries[-1]["id"]

    def _advance(self, entry_id, stage, by="ai", stub=False, ref=None):
        return self._run(
            self.reg.cmd_advance,
            SimpleNamespace(id=entry_id, stage=stage, by=by, stub=stub, litreview_manifest_ref=ref),
        )

    def _check(self):
        return self._run(self.reg.cmd_check, SimpleNamespace())

    def _entry(self, entry_id):
        return self.reg.find_entry(self.reg.load_registry()["entries"], entry_id)

    # -- new() starts at problem -----------------------------------------

    def test_new_entry_starts_at_problem_with_single_history_row(self):
        eid = self._new()
        entry = self._entry(eid)
        self.assertEqual(entry["spine_stage"], "problem")
        self.assertEqual(len(entry["history"]), 1)
        self.assertEqual(entry["history"][0]["stage"], "problem")

    # -- allowed (one-step-forward) transitions --------------------------

    def test_sequential_single_step_advances_succeed(self):
        eid = self._new()
        for stage in ("blackbox", "lens_in", "analysis", "lens_out"):
            code, out, err = self._advance(eid, stage)
            self.assertEqual(code, 0, err)
        entry = self._entry(eid)
        self.assertEqual(entry["spine_stage"], "lens_out")
        self.assertEqual([h["stage"] for h in entry["history"]],
                          ["problem", "blackbox", "lens_in", "analysis", "lens_out"])

    # -- forbidden: skipping stages ---------------------------------------

    def test_advance_refuses_a_skip(self):
        eid = self._new()
        code, out, err = self._advance(eid, "analysis")  # skips blackbox, lens_in
        self.assertNotEqual(code, 0)
        self.assertIn("only allows one step at a time", err)
        # entry must be unchanged
        self.assertEqual(self._entry(eid)["spine_stage"], "problem")

    def test_advance_refuses_going_backward(self):
        eid = self._new()
        self._advance(eid, "blackbox")
        code, out, err = self._advance(eid, "problem")
        self.assertNotEqual(code, 0)

    def test_advance_refuses_unknown_stage(self):
        eid = self._new()
        code, out, err = self._advance(eid, "not_a_real_stage")
        self.assertNotEqual(code, 0)
        self.assertIn("unknown stage", err)

    def test_advance_refuses_unknown_id(self):
        code, out, err = self._advance("GLS-2026-999", "blackbox")
        self.assertNotEqual(code, 0)
        self.assertIn("no such id", err)

    # -- litreview gate starting at lrs -----------------------------------

    def _to_lens_out(self, eid):
        for stage in ("blackbox", "lens_in", "analysis", "lens_out"):
            self._advance(eid, stage)

    def test_lrs_refuses_without_ref_or_stub(self):
        eid = self._new()
        self._to_lens_out(eid)
        code, out, err = self._advance(eid, "lrs")
        self.assertNotEqual(code, 0)
        self.assertIn("litreview_manifest_ref", err)
        self.assertEqual(self._entry(eid)["spine_stage"], "lens_out")

    def test_lrs_stub_succeeds_and_is_logged(self):
        eid = self._new()
        self._to_lens_out(eid)
        code, out, err = self._advance(eid, "lrs", stub=True)
        self.assertEqual(code, 0, err)
        entry = self._entry(eid)
        self.assertEqual(entry["spine_stage"], "lrs")
        self.assertTrue(entry["history"][-1].get("stub"))

    def test_lrs_with_real_ref_succeeds_and_is_not_logged_as_stub(self):
        eid = self._new()
        self._to_lens_out(eid)
        code, out, err = self._advance(eid, "lrs", ref="litreview_manifest.yaml#L1")
        self.assertEqual(code, 0, err)
        entry = self._entry(eid)
        self.assertEqual(entry["litreview_manifest_ref"], "litreview_manifest.yaml#L1")
        self.assertNotIn("stub", entry["history"][-1])

    # -- stub ceiling at genre_routed ---------------------------------------

    def _to_genre_routed_via_stub(self, eid):
        self._to_lens_out(eid)
        self._advance(eid, "lrs", stub=True)
        self._advance(eid, "hypothesis_selected", stub=True)
        self._advance(eid, "genre_routed", stub=True)

    def test_stub_allowed_through_genre_routed(self):
        eid = self._new()
        self._to_genre_routed_via_stub(eid)
        entry = self._entry(eid)
        self.assertEqual(entry["spine_stage"], "genre_routed")
        for row in entry["history"][5:]:  # lrs, hypothesis_selected, genre_routed
            self.assertTrue(row.get("stub"))

    def test_stub_refused_past_genre_routed(self):
        eid = self._new()
        self._to_genre_routed_via_stub(eid)
        code, out, err = self._advance(eid, "method", stub=True)
        self.assertNotEqual(code, 0)
        self.assertIn("only a valid escape through", err)
        self.assertEqual(self._entry(eid)["spine_stage"], "genre_routed")

    def test_method_requires_real_ref_even_after_prior_stub_stages(self):
        eid = self._new()
        self._to_genre_routed_via_stub(eid)
        # no real ref was ever supplied (all three gated stages used --stub)
        code, out, err = self._advance(eid, "method")
        self.assertNotEqual(code, 0)
        self.assertIn("litreview_manifest_ref", err)

    def test_method_succeeds_once_a_real_ref_is_supplied(self):
        eid = self._new()
        self._to_genre_routed_via_stub(eid)
        code, out, err = self._advance(eid, "method", ref="litreview_manifest.yaml#L1")
        self.assertEqual(code, 0, err)
        self.assertEqual(self._entry(eid)["spine_stage"], "method")

    # -- released requires doi_version + RELEASE_APPROVAL.txt ---------------

    def _to_review_with_real_ref(self, eid):
        self._to_lens_out(eid)
        self._advance(eid, "lrs", ref="litreview_manifest.yaml#L1")
        self._advance(eid, "hypothesis_selected")
        self._advance(eid, "genre_routed")
        self._advance(eid, "method")
        self._advance(eid, "paper_draft")
        self._advance(eid, "review")

    def test_released_refuses_without_doi_version(self):
        eid = self._new()
        self._to_review_with_real_ref(eid)
        code, out, err = self._advance(eid, "released")
        self.assertNotEqual(code, 0)
        self.assertIn("doi_version", err)

    def _set_doi(self, eid, doi):
        data = self.reg.load_registry()
        self.reg.find_entry(data["entries"], eid)["doi_version"] = doi
        self.reg.save_registry(data)

    def test_released_refuses_without_approval_file(self):
        eid = self._new()
        self._to_review_with_real_ref(eid)
        self._set_doi(eid, "10.5281/zenodo.99999999")
        code, out, err = self._advance(eid, "released")
        self.assertNotEqual(code, 0)
        self.assertIn("RELEASE_APPROVAL.txt", err)

    def test_released_succeeds_with_doi_and_approved_file(self):
        eid = self._new()
        self._to_review_with_real_ref(eid)
        self._set_doi(eid, "10.5281/zenodo.99999999")
        self.reg.RELEASE_APPROVAL_TXT.write_text("APPROVED 2026-09-04 Test Founder\n")
        code, out, err = self._advance(eid, "released")
        self.assertEqual(code, 0, err)
        self.assertEqual(self._entry(eid)["spine_stage"], "released")


class RegistryCheckCommandTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        tmp_root = Path(self._tmp.name)
        (tmp_root / "registry").mkdir()

        self.reg = _load_module()
        self.reg.REPO_ROOT = tmp_root
        self.reg.REGISTRY_YAML = tmp_root / "registry" / "RESEARCH_REGISTRY.yaml"
        self.reg.REGISTRY_JSON = tmp_root / "registry" / "RESEARCH_REGISTRY.json"
        self.reg.LIBRARY_MD = tmp_root / "RESEARCH_LIBRARY.md"
        self.reg.RELEASE_APPROVAL_TXT = tmp_root / "registry" / "RELEASE_APPROVAL.txt"

    def _run(self, fn, ns):
        out, err = io.StringIO(), io.StringIO()
        code = 0
        try:
            with redirect_stdout(out), redirect_stderr(err):
                fn(ns)
        except SystemExit as e:
            code = e.code or 0
        return code, out.getvalue(), err.getvalue()

    def _check(self):
        return self._run(self.reg.cmd_check, SimpleNamespace())

    def test_check_passes_on_empty_registry(self):
        code, out, err = self._check()
        self.assertEqual(code, 0, out + err)
        self.assertIn("0 violations", out)

    def test_check_passes_on_a_clean_stubbed_entry(self):
        data = {
            "entries": [
                {
                    "id": "GLS-2026-100",
                    "spine_stage": "genre_routed",
                    "litreview_manifest_ref": None,
                    "doi_version": None,
                    "history": [
                        {"date": "2026-09-04", "stage": "problem", "by": "joint"},
                        {"date": "2026-09-04", "stage": "blackbox", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_in", "by": "joint"},
                        {"date": "2026-09-04", "stage": "analysis", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_out", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lrs", "by": "joint", "stub": True},
                        {"date": "2026-09-04", "stage": "hypothesis_selected", "by": "joint", "stub": True},
                        {"date": "2026-09-04", "stage": "genre_routed", "by": "joint", "stub": True},
                    ],
                }
            ]
        }
        self.reg.save_registry(data)
        code, out, err = self._check()
        self.assertEqual(code, 0, out + err)

    def test_check_flags_a_hand_edited_skip_with_no_ref_or_stub(self):
        # exactly the shape reviews/ARCH_lifecycle.md F3 found: a single history row that lands
        # directly on a gated stage, no litreview_manifest_ref, no stub:true.
        data = {
            "entries": [
                {
                    "id": "GLS-2026-001",
                    "spine_stage": "paper_draft",
                    "litreview_manifest_ref": None,
                    "doi_version": "10.5281/zenodo.22301060",
                    "history": [
                        {"date": "2026-09-04", "stage": "paper_draft", "by": "joint"},
                    ],
                }
            ]
        }
        self.reg.save_registry(data)
        code, out, err = self._check()
        self.assertNotEqual(code, 0)
        self.assertIn("GLS-2026-001", out)
        self.assertIn("does not start at 'problem'", out)

    def test_check_flags_stub_placed_past_the_ceiling(self):
        data = {
            "entries": [
                {
                    "id": "GLS-2026-101",
                    "spine_stage": "method",
                    "litreview_manifest_ref": None,
                    "doi_version": None,
                    "history": [
                        {"date": "2026-09-04", "stage": "problem", "by": "joint"},
                        {"date": "2026-09-04", "stage": "blackbox", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_in", "by": "joint"},
                        {"date": "2026-09-04", "stage": "analysis", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_out", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lrs", "by": "joint", "stub": True},
                        {"date": "2026-09-04", "stage": "hypothesis_selected", "by": "joint", "stub": True},
                        {"date": "2026-09-04", "stage": "genre_routed", "by": "joint", "stub": True},
                        {"date": "2026-09-04", "stage": "method", "by": "joint", "stub": True},
                    ],
                }
            ]
        }
        self.reg.save_registry(data)
        code, out, err = self._check()
        self.assertNotEqual(code, 0)
        self.assertIn("past the stub ceiling", out)

    def test_check_flags_released_without_approval(self):
        data = {
            "entries": [
                {
                    "id": "GLS-2026-102",
                    "spine_stage": "released",
                    "litreview_manifest_ref": "litreview_manifest.yaml#L1",
                    "doi_version": "10.5281/zenodo.99999999",
                    "history": [
                        {"date": "2026-09-04", "stage": "problem", "by": "joint"},
                        {"date": "2026-09-04", "stage": "blackbox", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_in", "by": "joint"},
                        {"date": "2026-09-04", "stage": "analysis", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lens_out", "by": "joint"},
                        {"date": "2026-09-04", "stage": "lrs", "by": "joint"},
                        {"date": "2026-09-04", "stage": "hypothesis_selected", "by": "joint"},
                        {"date": "2026-09-04", "stage": "genre_routed", "by": "joint"},
                        {"date": "2026-09-04", "stage": "method", "by": "joint"},
                        {"date": "2026-09-04", "stage": "paper_draft", "by": "joint"},
                        {"date": "2026-09-04", "stage": "review", "by": "joint"},
                        {"date": "2026-09-04", "stage": "released", "by": "joint"},
                    ],
                }
            ]
        }
        self.reg.save_registry(data)
        code, out, err = self._check()
        self.assertNotEqual(code, 0)
        self.assertIn("no APPROVED", out)

    def test_check_on_real_repo_registry_file_passes(self):
        """Guard against the exact bug this drift test exists for: the real committed
        registry/RESEARCH_REGISTRY.yaml must itself pass `registry.py check`."""
        real = _load_module()  # loaded with the module's real (unpatched) REPO_ROOT paths
        code, out, err = self._run(real.cmd_check, SimpleNamespace())
        self.assertEqual(code, 0, out + err)


if __name__ == "__main__":
    unittest.main()
