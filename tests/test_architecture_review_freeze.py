"""Regression for the L6 freeze/rebuild drop of architecture_review (cross-vendor review finding
on PR #9, design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md §8 R3): `glosa lit manifest` rebuilds
litreview_manifest.yaml from scratch on every call via scaffold_litreview_manifest(), which never
carries the optional architecture_review block forward -- a run that used the architecture-first
comparative review companion mode lost its OPEN-node disclosure (node_status, n_open_nodes) the
moment the manifest was rebuilt or frozen. tier: finite_diagnostic."""
import copy
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSA = str(ROOT / "cli/glosa")


def _manifest_path(td, slug, hyp):
    lit = Path(td) / "records" / "lit" / slug / hyp.lower()
    for ext in (".yaml", ".yml", ".json"):
        p = lit / f"litreview_manifest{ext}"
        if p.is_file():
            return p
    raise AssertionError(f"no litreview_manifest under {lit}")


def _load(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


def _dump(path, data):
    if path.suffix in (".yaml", ".yml"):
        import yaml
        path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    else:
        path.write_text(json.dumps(data), encoding="utf-8")


class ArchitectureReviewFreezeRoundTripTest(unittest.TestCase):
    def _new_run(self, td, slug="arch-freeze-slug", hyp="H1"):
        env = dict(os.environ, GLOSA_RECORDS_ROOT=td)
        r = subprocess.run([sys.executable, GLOSA, "lit", "new", slug, hyp, "--search-mode", "SCOPING_SEARCH"],
                            cwd=td, env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        r = subprocess.run([sys.executable, GLOSA, "lit", "manifest", slug, hyp, "--human-owner", "founder"],
                            cwd=td, env=env, capture_output=True, text=True)
        return env, slug, hyp

    def test_freeze_preserves_architecture_review_and_recomputes_count(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env, slug, hyp = self._new_run(td)
            mpath = _manifest_path(td, slug, hyp)
            data = _load(mpath)
            data["architecture_review"] = {
                "used": True,
                "architecture_map_ref": "records/lit/%s/%s/architecture_map.md" % (slug, hyp.lower()),
                "architecture_dialogue_table_ref": "records/lit/%s/%s/architecture_dialogue_table.md" % (slug, hyp.lower()),
                "node_status": [
                    {"node_id": "N1", "status": "OPEN", "reason": "unanswered CHALLENGES row"},
                    {"node_id": "N2", "status": "CLOSED", "reason": None},
                ],
                # deliberately wrong count -- freeze must recompute this, not trust it
                "n_open_nodes": 99,
            }
            _dump(mpath, data)

            r = subprocess.run([sys.executable, GLOSA, "lit", "manifest", slug, hyp, "--human-owner", "founder", "--freeze"],
                                cwd=td, env=env, capture_output=True, text=True)
            self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)  # gate may FAIL (no citations); write still happens

            frozen = _load(mpath)
            self.assertEqual(frozen["status"], "FROZEN")
            arch = frozen.get("architecture_review")
            self.assertIsNotNone(arch, "architecture_review block was dropped by freeze/rebuild")
            self.assertTrue(arch.get("used"))
            self.assertEqual(len(arch.get("node_status") or []), 2)
            self.assertEqual(arch["n_open_nodes"], 1, "n_open_nodes must be recomputed from node_status, not trusted")

    def test_freeze_refuses_on_duplicate_node_ids(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env, slug, hyp = self._new_run(td)
            mpath = _manifest_path(td, slug, hyp)
            data = _load(mpath)
            data["architecture_review"] = {
                "used": True,
                "architecture_map_ref": "x",
                "architecture_dialogue_table_ref": "y",
                "node_status": [
                    {"node_id": "N1", "status": "OPEN", "reason": "r"},
                    {"node_id": "N1", "status": "CLOSED", "reason": None},
                ],
                "n_open_nodes": 1,
            }
            _dump(mpath, data)
            before = _load(mpath)

            r = subprocess.run([sys.executable, GLOSA, "lit", "manifest", slug, hyp, "--human-owner", "founder", "--freeze"],
                                cwd=td, env=env, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0, r.stdout)
            self.assertIn("duplicate", (r.stdout + r.stderr).lower())
            # refused -- the on-disk manifest must not have been silently rewritten without the block
            after = _load(mpath)
            self.assertEqual(before.get("architecture_review"), after.get("architecture_review"))

    def test_freeze_refuses_on_open_node_missing_reason(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env, slug, hyp = self._new_run(td)
            mpath = _manifest_path(td, slug, hyp)
            data = _load(mpath)
            data["architecture_review"] = {
                "used": True,
                "architecture_map_ref": "x",
                "architecture_dialogue_table_ref": "y",
                "node_status": [{"node_id": "N1", "status": "OPEN", "reason": None}],
                "n_open_nodes": 1,
            }
            _dump(mpath, data)

            r = subprocess.run([sys.executable, GLOSA, "lit", "manifest", slug, hyp, "--human-owner", "founder", "--freeze"],
                                cwd=td, env=env, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0, r.stdout)
            self.assertIn("no reason", (r.stdout + r.stderr).lower())


if __name__ == "__main__":
    unittest.main()
