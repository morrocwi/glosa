"""tests/test_ret_check.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers RET-Check v0.1 (`scripts/ret_check.py`; `cases/ret/PREREGISTRATION_v0_1.md`;
`methodology/P21_ret_check.md`): each pre-registered scenario A-E and the self-application case
asserts the EXACT output declared in the preregistration before the code existed, plus a
JSON-input test, a CSV-input test, an invalid-input (exit 2) test, and a standard-library-only /
no-network guard (this module must never import anything beyond the Python standard library, and
must never open a socket).
"""

import csv
import io
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = REPO_ROOT / "cases" / "ret"
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import ret_check  # noqa: E402


def _claim(result, claim_id):
    for c in result["claims"]:
        if c["claim"] == claim_id:
            return c
    raise AssertionError(f"claim {claim_id!r} not found in result: {[c['claim'] for c in result['claims']]}")


class TestScenarioA(unittest.TestCase):
    """A -- Mirror: 5 agents, 1 (non-independent) root -- must NOT report evidence = 5; RET RISK
    HIGH (preregistration scenario A)."""

    def test_a_mirror_high(self):
        result = ret_check.run(CASES_DIR / "A_mirror.json")
        c = _claim(result, "a-mirror-claim")
        self.assertEqual(c["n_a"], 5)
        self.assertEqual(c["n_p"], 0)
        self.assertNotEqual(c["n_a"], 5 and c["n_p"] == 5, "must not report evidence == 5")
        self.assertTrue(c["cycle_detected"])
        self.assertFalse(c["external_interruption_present"])
        self.assertEqual(c["risk"], "HIGH")


class TestScenarioB(unittest.TestCase):
    """B -- Independent convergence: 5 agents, 5 independent roots -- must NOT be flagged like A;
    RET RISK LOW (preregistration scenario B)."""

    def test_b_independent_low(self):
        result = ret_check.run(CASES_DIR / "B_independent.json")
        c = _claim(result, "b-independent-claim")
        self.assertEqual(c["n_a"], 5)
        self.assertEqual(c["n_p"], 5)
        self.assertFalse(c["cycle_detected"])
        self.assertEqual(c["risk"], "LOW")
        self.assertNotEqual(c["risk"], "HIGH")


class TestScenarioC(unittest.TestCase):
    """C -- Evidence-driven convergence: effective alternatives decrease but an independent world
    record is added -- must NOT be called a tunnel; RET RISK LOW/MEDIUM with a reason
    (preregistration scenario C: pre-registered exact outcome is LOW, regime
    evidence_driven_convergence, never tunnel_contraction_risk)."""

    def test_c_evidence_driven_not_a_tunnel(self):
        result = ret_check.run(CASES_DIR / "C_evidence_driven.json")
        c = _claim(result, "c-evidence-driven-claim")
        self.assertEqual(c["n_a"], 3)
        self.assertEqual(c["n_p"], 1)
        self.assertTrue(c["external_interruption_present"])
        self.assertEqual(c["effective_alternatives_delta"], -2)
        self.assertEqual(c["regime"], "evidence_driven_convergence")
        self.assertNotEqual(c["regime"], "tunnel_contraction_risk")
        self.assertIn(c["risk"], ("LOW", "MEDIUM"))
        self.assertEqual(c["risk"], "LOW")  # exact pre-registered outcome


class TestScenarioD(unittest.TestCase):
    """D -- Recursive return: H -> AI1 -> AI2 -> H cycle detected (preregistration scenario D)."""

    def test_d_recursive_return_cycle(self):
        result = ret_check.run(CASES_DIR / "D_recursive_return.json")
        c = _claim(result, "d-recursive-return-claim")
        self.assertTrue(c["cycle_detected"])
        self.assertTrue(c["return_to_origin"])
        self.assertIn("H", c["cycle_path"])
        self.assertIn("AI1", c["cycle_path"])
        self.assertIn("AI2", c["cycle_path"])
        self.assertEqual(c["risk"], "HIGH")


class TestScenarioE(unittest.TestCase):
    """E -- External interruption present/absent: same structure, isolates the interruption
    variable (preregistration scenario E)."""

    def test_e_interruption_present_vs_absent(self):
        result = ret_check.run(CASES_DIR / "E_interruption.json")
        with_int = _claim(result, "e-with-interruption")
        without_int = _claim(result, "e-without-interruption")

        # Same endorsement structure and cycle on both claims.
        self.assertEqual(with_int["n_a"], without_int["n_a"])
        self.assertTrue(with_int["cycle_detected"])
        self.assertTrue(without_int["cycle_detected"])

        self.assertTrue(with_int["external_interruption_present"])
        self.assertFalse(without_int["external_interruption_present"])

        self.assertEqual(with_int["risk"], "LOW")
        self.assertEqual(without_int["risk"], "HIGH")
        self.assertNotEqual(with_int["risk"], without_int["risk"])


class TestSelfApplication(unittest.TestCase):
    """Self-application (founder order item 4): the RET manuscript's own Core Epistemic
    Registration modeled as a 2-agent recursive dialogue over one shared, non-independent root,
    with no independent human review or AOWC record. Expected: RET RISK HIGH and the exact
    sentence. If the program instead reports this case as safe, THIS TEST DOCUMENTS THAT FAILURE
    HONESTLY rather than loosening the rule to pass it (per the preregistration's own binding
    instruction)."""

    def test_self_ret_reports_high_and_the_sentence(self):
        result = ret_check.run(CASES_DIR / "self_ret_v2_0.json")
        c = _claim(result, "ret-manuscript-self-audit")
        self.assertTrue(c["self_application"])
        self.assertEqual(c["n_a"], 2)
        self.assertEqual(c["n_p"], 0)
        self.assertTrue(c["cycle_detected"])
        self.assertFalse(c["external_interruption_present"])
        self.assertEqual(
            c["risk"], "HIGH",
            "Preregistration (cases/ret/PREREGISTRATION_v0_1.md): if the program reports the "
            "RET manuscript's own self-application case as safe, the artifact FAILS by the "
            "preregistration -- this assertion must not be loosened to make it pass.",
        )
        report = ret_check.render_report(c)
        self.assertIn(ret_check.SELF_APPLICATION_SENTENCE, report)


class TestInputFormats(unittest.TestCase):
    def test_csv_input(self):
        csv_path = REPO_ROOT / "cases" / "ret" / "_test_scratch_b_independent.csv"
        rows = json.loads((CASES_DIR / "B_independent.json").read_text(encoding="utf-8"))
        fieldnames = [
            "claim", "agent", "parent", "source_root", "root_independent", "record_type",
            "evidence_ref",
        ]
        try:
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for r in rows:
                    writer.writerow({k: r.get(k, "") for k in fieldnames})
            result = ret_check.run(csv_path)
            c = _claim(result, "b-independent-claim")
            self.assertEqual(c["n_a"], 5)
            self.assertEqual(c["n_p"], 5)
            self.assertEqual(c["risk"], "LOW")
        finally:
            csv_path.unlink(missing_ok=True)

    def test_json_object_with_rows_key(self):
        rows = json.loads((CASES_DIR / "A_mirror.json").read_text(encoding="utf-8"))
        # Exercise the {"rows": [...]} JSON shape directly via a temp file.
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump({"rows": rows}, f)
            path = f.name
        try:
            result = ret_check.run(path)
            c = _claim(result, "a-mirror-claim")
            self.assertEqual(c["n_a"], 5)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_invalid_input_missing_field_raises(self):
        import tempfile
        bad_rows = [{"claim": "x", "agent": "a1", "parent": "-"}]  # missing required fields
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(bad_rows, f)
            path = f.name
        try:
            with self.assertRaises(ret_check.RetCheckInputError):
                ret_check.run(path)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_invalid_input_bad_record_type_raises(self):
        import tempfile
        bad_rows = [{
            "claim": "x", "agent": "a1", "parent": "-", "source_root": "r1",
            "root_independent": False, "record_type": "not-a-real-type",
        }]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(bad_rows, f)
            path = f.name
        try:
            with self.assertRaises(ret_check.RetCheckInputError):
                ret_check.run(path)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_cli_main_exit_code_2_on_invalid_input(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            f.write("[]")
            path = f.name
        try:
            exit_code = ret_check.main([path])
            self.assertEqual(exit_code, 2)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_cli_main_exit_code_0_on_valid_input(self):
        exit_code = ret_check.main([str(CASES_DIR / "B_independent.json")])
        self.assertEqual(exit_code, 0)


class TestNoNetworkNoThirdParty(unittest.TestCase):
    """AI = 0 at runtime, standard library only (founder order BBL-2026-09-07-223)."""

    def test_module_imports_only_stdlib(self):
        stdlib_top_level = set(sys.stdlib_module_names) if hasattr(sys, "stdlib_module_names") else None
        source = (SCRIPTS_DIR / "ret_check.py").read_text(encoding="utf-8")
        import ast
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    imported.add(node.module.split(".")[0])
        non_stdlib = {m for m in imported if m not in ("__future__",)}
        if stdlib_top_level is not None:
            non_stdlib = {m for m in non_stdlib if m not in stdlib_top_level}
        self.assertEqual(
            non_stdlib, set(),
            f"ret_check.py must import only the Python standard library; found: {non_stdlib}",
        )

    def test_no_socket_module_used(self):
        source = (SCRIPTS_DIR / "ret_check.py").read_text(encoding="utf-8")
        for forbidden in ("socket", "urllib.request", "http.client", "requests"):
            self.assertNotIn(forbidden, source, f"ret_check.py must never reference {forbidden!r}")


if __name__ == "__main__":
    unittest.main()
