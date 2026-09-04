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
