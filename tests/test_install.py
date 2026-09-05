"""Install regression tests (founder ruling 2026-09-04, BBL-2026-09-04-092/093):
an ordinary person must be able to install glosa; the 2026-09-04 failure (plugin manifest forced
an ssh clone; host without a GitHub host key) must never recur. tier: finite_diagnostic."""
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class MarketplaceManifestTest(unittest.TestCase):
    def setUp(self):
        self.mk = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))

    def test_plugin_source_is_in_repo_relative_path(self):
        for pl in self.mk["plugins"]:
            src = pl["source"]
            self.assertIsInstance(src, str, "source must be a relative path string, not a remote-clone object")
            self.assertTrue(src.startswith("./"), src)
            self.assertTrue((ROOT / src).is_dir(), src)
            self.assertTrue((ROOT / src / ".claude-plugin/plugin.json").exists(), src)

    def test_no_ssh_anywhere_in_install_surface(self):
        for rel in (".claude-plugin/marketplace.json", "install.sh", "INSTALL.md", "README.md", "TOOLCHAIN.md"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotRegex(text, r"git@github\.com:|ssh://git", rel)  # an ssh URL actually used as a source

    def test_plugin_json_name_matches_marketplace(self):
        pj = json.loads((ROOT / "plugins/glosa/.claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(pj["name"], self.mk["plugins"][0]["name"])

    def test_every_skill_has_skill_md(self):
        for d in (ROOT / "plugins/glosa/skills").iterdir():
            if d.is_dir():
                self.assertTrue((d / "SKILL.md").exists(), d.name)


class InstallScriptTest(unittest.TestCase):
    def test_install_sh_parses(self):
        subprocess.run(["bash", "-n", str(ROOT / "install.sh")], check=True)

    def test_install_sh_uses_https_only(self):
        text = (ROOT / "install.sh").read_text(encoding="utf-8")
        self.assertIn("https://github.com/morrocwi/glosa", text)
        self.assertNotRegex(text, r"git@github\.com:|ssh://git")
        self.assertIn("doctor", text)

    def test_doctor_passes_in_repo(self):
        r = subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "doctor"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("glosa doctor: PASS", r.stdout)

    @unittest.skipUnless(os.environ.get("GLOSA_INSTALL_E2E") == "1", "set GLOSA_INSTALL_E2E=1 to run the fresh-dir install")
    def test_fresh_install_from_local_source_into_tempdir(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env = dict(os.environ, GLOSA_DIR=os.path.join(td, "glosa"), GLOSA_SOURCE=str(ROOT), GLOSA_NO_PIP="1", HOME=td)
            r = subprocess.run(["bash", str(ROOT / "install.sh")], env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("glosa doctor: PASS", r.stdout)
            self.assertTrue(Path(td, ".local/bin/glosa").exists())


if __name__ == "__main__":
    unittest.main()


class LitManifestFailClosedTest(unittest.TestCase):
    """Regression from the 2026-09-04 self-application run: a citation card written in the wrong
    shape must make `glosa lit manifest` report accuracy_gate FAIL, never pass silently."""

    def test_nonconformant_card_fails_manifest(self):
        import shutil
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            slug, hyp = "t-slug", "H9"
            lit = Path(td) / "records" / "lit" / slug / hyp.lower()
            (lit / "citations").mkdir(parents=True)
            (lit / "citations" / "cite-bad-001.yaml").write_text("citation_card_id: cite-bad-001\nidentifier_kind: DOI\nstatus: METADATA_OK\n", encoding="utf-8")
            env = dict(os.environ, GLOSA_RECORDS_ROOT=td)
            r = subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "lit", "new", slug, hyp, "--search-mode", "SCOPING_SEARCH"], cwd=td, env=env, capture_output=True, text=True)
            r = subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "lit", "manifest", slug, hyp, "--human-owner", "founder"], cwd=td, env=env, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0, r.stdout)
            self.assertIn("INVALID_SCHEMA", r.stdout + r.stderr)


class ClaimValidateCitationCardsFlagTest(unittest.TestCase):
    """`glosa claim validate --citation-cards <glob or paths...>` (this task): without the flag,
    rule 28 (INFLATED-BEARING) and D-LENS-UNCITED cannot resolve any citation_ref and are left
    "not checked"; with it, the CLI loads the named citation_card files (glob patterns and/or
    literal paths, yaml/json, *.i3.json/*.i5.json sidecars skipped) and passes them through to
    `kernel.validate_claim_card(citation_cards=[...])`. tier: finite_diagnostic."""

    def test_citation_cards_flag_loads_and_is_reported(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "cli/glosa"), "claim", "validate",
             str(ROOT / "schema/examples/claim_card.example.json"),
             "--citation-cards", str(ROOT / "schema/examples/citation_card.example.json")],
            capture_output=True, text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["citation_cards_checked"], 1, r.stdout)
        self.assertEqual(out["result"]["verdict"], "PASS", r.stdout)

    def test_without_citation_cards_flag_key_is_absent(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "cli/glosa"), "claim", "validate",
             str(ROOT / "schema/examples/claim_card.example.json")],
            capture_output=True, text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = json.loads(r.stdout)
        self.assertNotIn("citation_cards_checked", out, r.stdout)

    def test_citation_cards_glob_matches_and_skips_i3_sidecars(self):
        # a glob against schema/examples/*.example.json would sweep in non-citation schemas too --
        # use a glob that only ever matches the one real citation card plus a planted i3.json
        # sidecar, and assert the sidecar was skipped (count stays 1, not 2).
        import shutil
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            cards_dir = Path(td) / "citations"
            cards_dir.mkdir()
            shutil.copy(ROOT / "schema/examples/citation_card.example.json", cards_dir / "cite-cat-obs-001.json")
            (cards_dir / "cite-cat-obs-001.i3.json").write_text("{}", encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(ROOT / "cli/glosa"), "claim", "validate",
                 str(ROOT / "schema/examples/claim_card.example.json"),
                 "--citation-cards", str(cards_dir / "*.json")],
                capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            out = json.loads(r.stdout)
            self.assertEqual(out["citation_cards_checked"], 1, r.stdout)


class FindingsCompleteTest(unittest.TestCase):
    """Gate rule 10 (founder BBL-2026-09-05-121): no finding is ever dropped between ledgers."""

    def test_checker_detects_a_dropped_id(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            up = Path(td, "up.json"); up.write_text(json.dumps([{"id": "X-1"}, {"id": "X-2"}]), encoding="utf-8")
            down = Path(td, "down.md"); down.write_text("carried X-1 only", encoding="utf-8")
            r = subprocess.run([sys.executable, str(ROOT / "scripts/check_findings_complete.py"), str(up), str(down)], capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0); self.assertIn("X-2", r.stdout)
            down.write_text("X-1 carried; X-2 closed: duplicate of X-1", encoding="utf-8")
            r = subprocess.run([sys.executable, str(ROOT / "scripts/check_findings_complete.py"), str(up), str(down)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout)


class SessionOpenCloseTest(unittest.TestCase):
    """`glosa session open|close` (SA-1, SESSION_ARCH_v0.4_SPEC.md §2.1/§2.2/§8, build_now): the
    session-boundary + AI-reset fact lives on a Blackbox Note. `close` is fail-closed -- it must
    refuse without a non-empty, human-authored --retention-note (the field is never AI-filled)."""

    def _open(self, td, session_id="S-TEST-001"):
        r = subprocess.run(
            [sys.executable, str(ROOT / "cli/glosa"), "session", "open",
             "--session-id", session_id, "--project", "t-proj", "--human-owner", "founder",
             "--out-dir", str(Path(td) / "sess")],
            capture_output=True, text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = json.loads(r.stdout)
        self.assertTrue(out["self_check"]["ok"], r.stdout)
        self.assertEqual(out["ai_state_at_boundary"], "reset")
        return out, Path(out["written"]["path"])

    def test_open_scaffolds_a_valid_note_with_open_session_block(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            out, note_path = self._open(td)
            self.assertTrue(note_path.exists())
            data = json.loads(note_path.read_text(encoding="utf-8")) if note_path.suffix == ".json" else None
            if data is None:
                import yaml
                data = yaml.safe_load(note_path.read_text(encoding="utf-8"))
            self.assertEqual(data["session_id"], "S-TEST-001")
            self.assertIsNone(data["session_boundary"]["closed_at"])
            self.assertIsNone(data["retention_note"])
            self.assertEqual(data["session_boundary"]["ai_state_at_boundary"], "reset")

    def test_close_refuses_without_retention_note(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            _, note_path = self._open(td)
            r = subprocess.run(
                [sys.executable, str(ROOT / "cli/glosa"), "session", "close",
                 "--path", str(note_path), "--retention-note", ""],
                capture_output=True, text=True,
            )
            self.assertNotEqual(r.returncode, 0, r.stdout)
            self.assertIn("REFUSED", r.stdout)

    def test_close_with_retention_note_writes_closed_at_and_reset(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            _, note_path = self._open(td)
            r = subprocess.run(
                [sys.executable, str(ROOT / "cli/glosa"), "session", "close",
                 "--path", str(note_path), "--retention-note", "human kept the resistance-route decision"],
                capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            out = json.loads(r.stdout)
            self.assertTrue(out["self_check"]["ok"], r.stdout)
            self.assertIsNotNone(out["closed_at"])
            # closing again must refuse (already closed), never silently re-close
            r2 = subprocess.run(
                [sys.executable, str(ROOT / "cli/glosa"), "session", "close",
                 "--path", str(note_path), "--retention-note", "x"],
                capture_output=True, text=True,
            )
            self.assertNotEqual(r2.returncode, 0, r2.stdout)

    def test_note_produced_by_session_open_is_actually_seen_by_kernel_check(self):
        """MUST fix (ARCH_REVIEW_v0.7.json spec-code-fidelity/one-fact-one-home/fail-closed-and-
        controls/founder-invariants): a note scaffolded by `glosa session open` must be seen (not
        silently skipped) by kernel/glosa_kernel.py's `check_session_boundary_reset` -- this is the
        SA-1 cross-file acceptance mechanism the design docs name, exercised end-to-end here against
        the CLI's real output, not a hand-built flat fixture. Two notes sharing a session_id, one
        with a forced/corrupted `ai_state_at_boundary`, must actually trip the check."""
        sys.path.insert(0, str(ROOT / "kernel"))
        import glosa_kernel as k  # noqa: E402

        import tempfile
        with tempfile.TemporaryDirectory() as td:
            out1, note_path1 = self._open(td, session_id="S-ROUNDTRIP-001")
            data1 = json.loads(note_path1.read_text(encoding="utf-8")) if note_path1.suffix == ".json" else None
            if data1 is None:
                import yaml
                data1 = yaml.safe_load(note_path1.read_text(encoding="utf-8"))
            self.assertEqual(data1["session_id"], "S-ROUNDTRIP-001")

            # A well-formed pair sharing session_id, both literal 'reset' -- must NOT fire.
            data2_ok = json.loads(json.dumps(data1))
            res_ok = k.check_session_boundary_reset([data1, data2_ok])
            self.assertTrue(res_ok["ok"], res_ok["errors"])

            # Corrupt the second note's ai_state_at_boundary -- must fire, and must reference the
            # real, shared session_id (proving the check actually read the CLI's own field
            # location, not a hand-built fixture shape).
            data2_bad = json.loads(json.dumps(data1))
            data2_bad["session_boundary"]["ai_state_at_boundary"] = "carried"
            res_bad = k.check_session_boundary_reset([data1, data2_bad])
            self.assertFalse(res_bad["ok"])
            self.assertTrue(
                any("S-ROUNDTRIP-001" in e for e in res_bad["errors"]), res_bad["errors"]
            )


class DialogueTableDefeaterColumnsTest(unittest.TestCase):
    """`lrs.dialogue-table-claim-type-column` (build_now): dialogue_table.md and `glosa lit table`
    gain `defeater_class` + `legitimate_defeater` (deliberately NOT `claim_type`, which already
    routes rule16w on claim_card.yaml -- see SESSION_ARCH_v0.4_SPEC.md §9.3/§10.1). A row with a
    real stance (YES/NO) and no defeater_class/legitimate_defeater must render flagged INCOMPLETE."""

    def test_template_has_new_columns_not_claim_type(self):
        text = (ROOT / "templates/knowledge/dialogue_table.md").read_text(encoding="utf-8")
        self.assertIn("defeater_class", text)
        self.assertIn("legitimate_defeater", text)
        header_line = next(l for l in text.splitlines() if l.startswith("| source"))
        self.assertNotIn("claim_type", header_line)

    def test_lit_table_flags_incomplete_and_accepts_complete_row(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env = dict(os.environ, GLOSA_RECORDS_ROOT=td)
            slug, hyp = "t-defeater", "h1"
            subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "lit", "new", slug, hyp], cwd=td, env=env, capture_output=True, text=True)
            rows_dir = Path(td) / "records" / "lit" / slug / hyp / "rows"
            rows_dir.mkdir(parents=True, exist_ok=True)
            (rows_dir / "incomplete.json").write_text(json.dumps({
                "hypothesis_ref": hyp, "source_label": "Source A", "stance": "YES",
                "citation_card": "cc-1", "verified": {"metadata_verified": True, "claim_match_verified": True},
            }), encoding="utf-8")
            (rows_dir / "complete.json").write_text(json.dumps({
                "hypothesis_ref": hyp, "source_label": "Source B", "stance": "NO",
                "citation_card": "cc-2", "verified": {"metadata_verified": True, "claim_match_verified": True},
                "defeater_class": "empirical", "legitimate_defeater": "a documented failed replication",
            }), encoding="utf-8")
            r = subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "lit", "table", slug, hyp], cwd=td, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            out = json.loads(r.stdout)
            self.assertEqual(out["rows_incomplete_defeater"], ["Source A"], r.stdout)
            table_text = (Path(td) / "records" / "lit" / slug / hyp / "dialogue_table.md").read_text(encoding="utf-8")
            self.assertIn("INCOMPLETE", table_text)
            self.assertIn("empirical", table_text)


class HypothesisSelectionSessionIdTest(unittest.TestCase):
    """`schema.retention-direction-field`/SA-2 (build_now): hypothesis_selection.yaml gains a
    session-grouping key plus a `retained_direction` field defaulted `unknown` (NC-77 -- retention
    is never direction-evidence on its own)."""

    def test_lit_select_writes_session_id_and_default_retained_direction(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env = dict(os.environ, GLOSA_RECORDS_ROOT=td)
            slug, hyp = "t-hsel", "h1"
            subprocess.run([sys.executable, str(ROOT / "cli/glosa"), "lit", "new", slug, hyp], cwd=td, env=env, capture_output=True, text=True)
            manifest_dir = Path(td) / "records" / "lit" / slug / hyp
            (manifest_dir / "litreview_manifest.json").write_text(json.dumps({
                "id": "litrev-t-001", "hypothesis_ref": hyp, "status": "FROZEN",
                "gate": {"accuracy_gate": "PASS", "diversity_gate": "PASS", "overall": "PASS"},
            }), encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(ROOT / "cli/glosa"), "lit", "select", slug,
                 "--decided-by", "founder", "--reason", "best fit", "--chosen", "all",
                 "--session-id", "S-TEST-001"],
                cwd=td, env=env, capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            out = json.loads(r.stdout)
            hsel_path = Path(out["written"]["path"])
            data = json.loads(hsel_path.read_text(encoding="utf-8")) if hsel_path.suffix == ".json" else None
            if data is None:
                import yaml
                data = yaml.safe_load(hsel_path.read_text(encoding="utf-8"))
            self.assertEqual(data["session_id"], "S-TEST-001")
            self.assertEqual(data["retained_direction"], "unknown")
