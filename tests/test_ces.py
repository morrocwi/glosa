"""tests/test_ces.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers methodology/P20_core_epistemic_structure.md's enforcement (founder ruling 2026-09-07,
Blackbox Log BBL-2026-09-07-216/217/218): `kernel.glosa_kernel.ces_check_text` (Markdown/LaTeX
prose), `kernel.glosa_kernel.validate_core_epistemic_structure` (a parsed
`core_epistemic_structure` object, `schema/core_epistemic_structure.schema.json`),
`kernel.glosa_kernel.ces_check_path` (file dispatch), `kernel.glosa_kernel.gate_release`'s hard
fail on a manifest missing/failing `core_epistemic_structure`, and
`scripts/check_core_epistemic_structure.py`'s `check_paths()` (the same function `cli/glosa`'s
`ces check` subcommand calls).
"""

import copy
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "kernel"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import glosa_kernel as k  # noqa: E402
import check_core_epistemic_structure as ces_script  # noqa: E402

EXAMPLES_DIR = REPO_ROOT / "schema" / "examples"


def load_example(name):
    return json.loads((EXAMPLES_DIR / name).read_text(encoding="utf-8"))


VALID_MD_BLOCK = """\
**Core Epistemic Structure**

**Core Respondent / Experience-Based Expert:** Jane Doe -- lived experience: ten years running the practice this claim comes from
**Interactional Expert:** None
**AI Model(s) Used:** AI assistant -- drafting and mechanical schema/gate wiring

Non-collapse rule: Experience-Based Expertise ≠ Interactional Expertise ≠ AI Model
"""

VALID_LATEX_BLOCK = r"""
\section{Core Epistemic Structure}
\begin{description}[style=nextline]
  \item[Core Respondent / Experience-Based Expert:] Jane Doe --- lived experience: ten years in the field
  \item[Interactional Expert:] None
  \item[AI Model(s) Used:] AI assistant --- drafting
\end{description}
Non-collapse rule: Experience-Based Expertise $\neq$ Interactional Expertise $\neq$ AI Model.
"""


class CesCheckTextPassTest(unittest.TestCase):
    def test_markdown_block_passes(self):
        res = k.ces_check_text(VALID_MD_BLOCK)
        self.assertTrue(res["ok"], res["errors"])

    def test_latex_block_passes(self):
        res = k.ces_check_text(VALID_LATEX_BLOCK)
        self.assertTrue(res["ok"], res["errors"])

    def test_shipped_template_passes(self):
        text = (REPO_ROOT / "templates" / "core_epistemic_structure.md").read_text(encoding="utf-8")
        res = k.ces_check_text(text)
        self.assertTrue(res["ok"], res["errors"])

    def test_shipped_paper_templates_pass(self):
        for rel in ("templates/paper/arxiv-onecol/main.tex", "templates/paper/arxiv-twocol/main.tex"):
            text = (REPO_ROOT / rel).read_text(encoding="utf-8")
            res = k.ces_check_text(text)
            self.assertTrue(res["ok"], f"{rel}: {res['errors']}")

    def test_interactional_expert_none_is_legal(self):
        # VALID_MD_BLOCK already sets Interactional Expert to None -- must not itself be a finding.
        res = k.ces_check_text(VALID_MD_BLOCK)
        self.assertFalse(any("Interactional Expert" in e for e in res["errors"]), res["errors"])


class CesCheckTextMissingBlockTest(unittest.TestCase):
    def test_missing_block_entirely_fails(self):
        res = k.ces_check_text("# Some paper\n\nJust prose, no CES block at all.\n")
        self.assertFalse(res["ok"])
        self.assertTrue(any("Core Respondent" in e for e in res["errors"]), res["errors"])
        self.assertTrue(any("Interactional Expert" in e for e in res["errors"]), res["errors"])
        self.assertTrue(any("AI Model" in e for e in res["errors"]), res["errors"])
        self.assertTrue(any("non-collapse" in e for e in res["errors"]), res["errors"])

    def test_respondent_without_basis_fails(self):
        text = VALID_MD_BLOCK.replace(
            "**Core Respondent / Experience-Based Expert:** Jane Doe -- lived experience: ten years running the practice this claim comes from",
            "**Core Respondent / Experience-Based Expert:** Jane Doe",
        )
        res = k.ces_check_text(text)
        self.assertFalse(res["ok"])
        self.assertTrue(any("no basis" in e for e in res["errors"]), res["errors"])

    def test_empty_interactional_line_fails(self):
        text = VALID_MD_BLOCK.replace("**Interactional Expert:** None", "**Interactional Expert:**")
        res = k.ces_check_text(text)
        self.assertFalse(res["ok"])
        self.assertTrue(any("Interactional Expert is empty" in e for e in res["errors"]), res["errors"])


class CesCheckTextAiWasUsedTest(unittest.TestCase):
    def test_ai_was_used_alone_fails(self):
        text = VALID_MD_BLOCK.replace(
            "**AI Model(s) Used:** AI assistant -- drafting and mechanical schema/gate wiring",
            "**AI Model(s) Used:** AI was used",
        )
        res = k.ces_check_text(text)
        self.assertFalse(res["ok"])
        self.assertTrue(any("AI was used" in e for e in res["errors"]), res["errors"])

    def test_ai_was_used_with_period_still_fails(self):
        text = VALID_MD_BLOCK.replace(
            "**AI Model(s) Used:** AI assistant -- drafting and mechanical schema/gate wiring",
            "**AI Model(s) Used:** AI was used.",
        )
        res = k.ces_check_text(text)
        self.assertFalse(res["ok"])

    def test_ai_models_none_is_legal(self):
        text = VALID_MD_BLOCK.replace(
            "**AI Model(s) Used:** AI assistant -- drafting and mechanical schema/gate wiring",
            "**AI Model(s) Used:** None",
        )
        res = k.ces_check_text(text)
        self.assertTrue(res["ok"], res["errors"])

    def test_ai_model_entry_with_no_dash_fails(self):
        text = VALID_MD_BLOCK.replace(
            "**AI Model(s) Used:** AI assistant -- drafting and mechanical schema/gate wiring",
            "**AI Model(s) Used:** AI assistant",
        )
        res = k.ces_check_text(text)
        self.assertFalse(res["ok"])
        self.assertTrue(any("no 'Model -- role' entry" in e for e in res["errors"]), res["errors"])


class ValidateCoreEpistemicStructureTest(unittest.TestCase):
    def setUp(self):
        self.obj = load_example("core_epistemic_structure.example.json")

    def test_shipped_example_passes(self):
        res = k.validate_core_epistemic_structure(self.obj)
        self.assertTrue(res["ok"], res["errors"])

    def test_interactional_none_passes(self):
        obj = copy.deepcopy(self.obj)
        obj["interactional"] = "None"
        res = k.validate_core_epistemic_structure(obj)
        self.assertTrue(res["ok"], res["errors"])

    def test_interactional_empty_fails(self):
        obj = copy.deepcopy(self.obj)
        obj["interactional"] = ""
        res = k.validate_core_epistemic_structure(obj)
        self.assertFalse(res["ok"])

    def test_ai_models_string_ai_was_used_fails(self):
        obj = copy.deepcopy(self.obj)
        obj["ai_models"] = "AI was used"
        res = k.validate_core_epistemic_structure(obj)
        self.assertFalse(res["ok"])
        self.assertTrue(any("not a role disclosure" in e for e in res["errors"]), res["errors"])

    def test_ai_models_string_none_passes(self):
        obj = copy.deepcopy(self.obj)
        obj["ai_models"] = "None"
        res = k.validate_core_epistemic_structure(obj)
        self.assertTrue(res["ok"], res["errors"])

    def test_ai_models_empty_list_fails(self):
        obj = copy.deepcopy(self.obj)
        obj["ai_models"] = []
        res = k.validate_core_epistemic_structure(obj)
        self.assertFalse(res["ok"])

    def test_ai_model_entry_missing_role_fails(self):
        obj = copy.deepcopy(self.obj)
        obj["ai_models"] = [{"model": "AI assistant"}]
        res = k.validate_core_epistemic_structure(obj)
        self.assertFalse(res["ok"])

    def test_respondent_object_form_with_basis(self):
        obj = copy.deepcopy(self.obj)
        obj["respondent"] = {"name": "Jane Doe", "basis": "lived experience of the practice"}
        res = k.validate_core_epistemic_structure(obj)
        self.assertTrue(res["ok"], res["errors"])

    def test_respondent_string_without_dash_fails(self):
        obj = copy.deepcopy(self.obj)
        obj["respondent"] = "Jane Doe"
        res = k.validate_core_epistemic_structure(obj)
        self.assertFalse(res["ok"])


class CesCheckPathTest(unittest.TestCase):
    def test_json_example_file_passes(self):
        res = k.ces_check_path(EXAMPLES_DIR / "core_epistemic_structure.example.json")
        self.assertTrue(res["ok"], res["errors"])

    def test_release_manifest_json_nested_passes(self):
        res = k.ces_check_path(EXAMPLES_DIR / "release_manifest.example.json")
        self.assertTrue(res["ok"], res["errors"])

    def test_missing_file_fails(self):
        res = k.ces_check_path(REPO_ROOT / "tests" / "does_not_exist_ces.json")
        self.assertFalse(res["ok"])

    def test_yaml_suffix_refused_by_kernel_dispatcher(self):
        # kernel.ces_check_path is stdlib-only (module docstring) and deliberately refuses to
        # parse YAML itself -- the CLI/script layer (which does import PyYAML) handles that
        # suffix instead, via validate_core_epistemic_structure directly.
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as fh:
            fh.write(b"respondent: Jane -- basis\ninteractional: None\nai_models: None\n")
            tmp_path = fh.name
        try:
            res = k.ces_check_path(tmp_path)
            self.assertFalse(res["ok"])
            self.assertTrue(any("does not parse YAML" in e for e in res["errors"]), res["errors"])
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    def test_md_path_works_through_kernel(self):
        res = k.ces_check_path(REPO_ROOT / "templates" / "core_epistemic_structure.md")
        self.assertTrue(res["ok"], res["errors"])


class CesScriptCheckPathsTest(unittest.TestCase):
    def test_check_paths_all_pass(self):
        exit_code, results = ces_script.check_paths([
            str(REPO_ROOT / "templates" / "core_epistemic_structure.md"),
            str(EXAMPLES_DIR / "core_epistemic_structure.example.json"),
        ])
        self.assertEqual(exit_code, 0)
        self.assertTrue(all(r["ok"] for r in results), results)

    def test_check_paths_one_failure_is_nonzero_exit(self):
        exit_code, results = ces_script.check_paths([
            str(REPO_ROOT / "templates" / "core_epistemic_structure.md"),
            str(REPO_ROOT / "tests" / "does_not_exist_ces.json"),
        ])
        self.assertEqual(exit_code, 1)
        self.assertTrue(results[0]["ok"])
        self.assertFalse(results[1]["ok"])


class GateReleaseCesTest(unittest.TestCase):
    def setUp(self):
        self.manifest = load_example("release_manifest.example.json")
        self.card = load_example("claim_card.example.json")
        self.review = load_example("review_report.example.json")

    def test_shipped_manifest_has_valid_ces_and_passes(self):
        result = k.gate_release(self.manifest, [self.card], [self.review])
        self.assertIn(result["verdict"], ("PASS", "PASS_WITH_LIMITS"))

    def test_missing_core_epistemic_structure_is_hard_fail(self):
        manifest = copy.deepcopy(self.manifest)
        del manifest["core_epistemic_structure"]
        result = k.gate_release(manifest, [self.card], [self.review])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any("core_epistemic_structure is missing" in r for r in result["reasons"]), result["reasons"])

    def test_invalid_core_epistemic_structure_is_hard_fail(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["core_epistemic_structure"]["ai_models"] = "AI was used"
        result = k.gate_release(manifest, [self.card], [self.review])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any("core_epistemic_structure:" in r for r in result["reasons"]), result["reasons"])

    def test_interactional_none_manifest_still_passes(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["core_epistemic_structure"]["interactional"] = "None"
        result = k.gate_release(manifest, [self.card], [self.review])
        self.assertIn(result["verdict"], ("PASS", "PASS_WITH_LIMITS"))


if __name__ == "__main__":
    unittest.main()
