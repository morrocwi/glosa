"""tests/test_ret_check.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers RET-Check v0.3 (`scripts/ret_check.py`; `cases/ret/PREREGISTRATION_v0_1.md`;
`methodology/P21_ret_check.md`): each pre-registered scenario A-E and the self-application case
asserts the EXACT output declared in the preregistration before the code existed, plus a
JSON-input test, a CSV-input test, an invalid-input (exit 2) test, and a standard-library-only /
no-network guard (this module must never import anything beyond the Python standard library, and
must never open a socket).

v0.3 additions (`design/RESISTANCE_LADDER_v0_1.md` sec 4, founder ruling `BBL-2026-09-07-229`):
`TestReproductionCardConverter` exercises `ret_check.reproduction_card_to_row()` directly against
representative Reproduction Card shapes (published_value / independent_implementation /
public_dataset / human_review / coq_kernel / unrecognized) -- this is a converter unit test, never
a re-tuning of the RET RISK formula, which every class above this one still exercises unchanged.
`TestScenarioF` runs the pre-registered scenario F case (`cases/ret/F_reproduction_card.json`:
scenario A's Mirror rows plus one `world_record` row emitted from the converter) and asserts the
exact preregistered delta over scenario A: N_P +1, N_P^ind +1, an external interruption now
present, RET RISK LOW via rule 2.
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
        # N_P (2026-09-08 correction): the founder's own Mirror example is 1 shared root S1 ->
        # N_P = 1, not 0 -- a raw root count is not the same claim as an independence count.
        self.assertEqual(c["n_p"], 1)
        self.assertEqual(c["n_p_ind"], 0, "the single shared root is NOT declared independent")
        self.assertNotEqual(c["n_a"], 5 and c["n_p_ind"] == 5, "must not report evidence == 5")
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
        self.assertEqual(c["n_p_ind"], 5, "all 5 roots are declared independent here")
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
        # N_P (raw root count) = 2: the shared internal root plus the world-record's own root.
        self.assertEqual(c["n_p"], 2)
        self.assertEqual(c["n_p_ind"], 1, "only the world-record's root is declared independent")
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
        self.assertEqual(c["n_a"], 3)
        self.assertEqual(c["n_p"], 1, "the one shared H-original-framing root, counted")
        self.assertEqual(c["n_p_ind"], 0, "that root is not declared independent")
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

        # N_P (raw root count) differs by exactly the interruption's own root; N_P^ind isolates
        # the independence variable precisely.
        self.assertEqual(with_int["n_p"], 2)
        self.assertEqual(with_int["n_p_ind"], 1)
        self.assertEqual(without_int["n_p"], 1)
        self.assertEqual(without_int["n_p_ind"], 0)

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
        # N_P (2026-09-08 correction): the single shared internal-programme root counts as 1,
        # matching the founder's own Mirror correction -- independence is the separate N_P^ind.
        self.assertEqual(c["n_p"], 1)
        self.assertEqual(c["n_p_ind"], 0, "the internal-programme root is not declared independent")
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


class TestReproductionCardConverter(unittest.TestCase):
    """v0.3: `ret_check.reproduction_card_to_row()` (design/RESISTANCE_LADDER_v0_1.md sec 4's
    mapping table). Fixture cards here mirror the shape `methodology/P22_reproduction_ledger.md`
    / `schema/reproduction_card.schema.json` (stream S1) will declare -- these are converter-unit
    fixtures, not stream S4's own filed cards under `cases/repro/`."""

    PDG_CARD = {
        "id": "REPRO-2026-09-08-0001-TESTFIXTURE",
        "toledo_codes": ["EQ-068"],
        "claim": "the fit Lambda_RD->GeV = 246/v_native predicts a Higgs boson mass of 218.005 GeV",
        "preregistered_prediction": {
            "statement": "the fit Lambda_RD->GeV = 246/v_native predicts a Higgs boson mass of 218.005 GeV",
            "tolerance": "±5% of the PDG Review of Particle Physics value for the Higgs boson mass",
            "declared_at": "2026-09-08T00:00:00Z",
        },
        "oracle": {
            "kind": "published_value",
            "source": "Particle Data Group, Review of Particle Physics",
            "doi_or_url": None,
            "version": None,
        },
        "environment": {"python": "3.x", "packages": {}},
        "run": {
            "command": "python3 scripts/repro_check.py cases/repro/EQ-068_higgs_pdg.json",
            "input_hash": None, "output_hash": None, "ai_at_runtime": 0, "date": None,
        },
        "result": {"status": "PENDING", "observed": None, "deviation": None},
        "lineage": {"run_by": "S4-test-fixture", "ces": None},
        "notes": "Test fixture only (S2, tests/test_ret_check.py); not the authoritative S4 card.",
    }

    def test_published_value_becomes_world_record_row(self):
        row = ret_check.reproduction_card_to_row(self.PDG_CARD, claim="f-reproduction-claim")
        self.assertEqual(row["claim"], "f-reproduction-claim")
        self.assertEqual(row["agent"], "REPRO-2026-09-08-0001-TESTFIXTURE")
        self.assertEqual(row["parent"], "-")
        self.assertEqual(row["source_root"], "Particle Data Group, Review of Particle Physics")
        self.assertTrue(row["root_independent"], "an external-oracle kind is independent unconditionally (sec 4)")
        self.assertEqual(row["record_type"], "world_record")

    def test_independent_implementation_and_public_dataset_also_become_world_record(self):
        for kind in ("independent_implementation", "public_dataset"):
            card = json.loads(json.dumps(self.PDG_CARD))  # deep copy
            card["oracle"]["kind"] = kind
            row = ret_check.reproduction_card_to_row(card, claim="c")
            self.assertEqual(row["record_type"], "world_record")
            self.assertTrue(row["root_independent"])

    def test_source_root_includes_pinned_version(self):
        card = json.loads(json.dumps(self.PDG_CARD))
        card["oracle"]["version"] = "2024"
        row = ret_check.reproduction_card_to_row(card, claim="c")
        self.assertEqual(row["source_root"], "Particle Data Group, Review of Particle Physics v2024")

    def test_external_oracle_missing_source_refused(self):
        card = json.loads(json.dumps(self.PDG_CARD))
        card["oracle"]["source"] = None
        with self.assertRaises(ret_check.RetCheckConversionError):
            ret_check.reproduction_card_to_row(card, claim="c")

    def test_human_review_with_i2_becomes_review_row(self):
        card = {
            "id": "REPRO-TEST-HR-1",
            "oracle": {"kind": "human_review", "source": "reviewer read", "doi_or_url": None, "version": None},
            "lineage": {"run_by": "reviewer-jane", "ces": None},
        }
        row = ret_check.reproduction_card_to_row(card, claim="c", independence_class="I2")
        self.assertEqual(row["record_type"], "review")
        self.assertEqual(row["agent"], "reviewer-jane")
        self.assertEqual(row["source_root"], "reviewer-jane")
        self.assertTrue(row["root_independent"])

    def test_human_review_i3_i4_i5_also_pass(self):
        card = {
            "id": "REPRO-TEST-HR-2",
            "oracle": {"kind": "human_review", "source": "x", "doi_or_url": None, "version": None},
            "lineage": {"run_by": "reviewer-x", "ces": None},
        }
        for cls in ("I3", "I4", "I5"):
            row = ret_check.reproduction_card_to_row(card, claim="c", independence_class=cls)
            self.assertTrue(row["root_independent"])

    def test_human_review_below_i2_refused(self):
        card = {
            "id": "REPRO-TEST-HR-3",
            "oracle": {"kind": "human_review", "source": "x", "doi_or_url": None, "version": None},
            "lineage": {"run_by": "reviewer-y", "ces": None},
        }
        for cls in (None, "I0", "I1", "not-a-real-class"):
            with self.assertRaises(
                ret_check.RetCheckConversionError,
                msg=f"independence_class={cls!r} must be refused, never silently marked independent",
            ):
                ret_check.reproduction_card_to_row(card, claim="c", independence_class=cls)

    def test_human_review_reviewer_identity_override(self):
        card = {
            "id": "REPRO-TEST-HR-4",
            "oracle": {"kind": "human_review", "source": "x", "doi_or_url": None, "version": None},
            "lineage": {"run_by": "reviewer-z", "ces": None},
        }
        row = ret_check.reproduction_card_to_row(
            card, claim="c", independence_class="I2", reviewer_identity="external-reviewer-override"
        )
        self.assertEqual(row["agent"], "external-reviewer-override")
        self.assertEqual(row["source_root"], "external-reviewer-override")

    def test_coq_kernel_always_refused_with_exact_message(self):
        card = {"id": "REPRO-TEST-COQ", "oracle": {"kind": "coq_kernel", "source": "coqc", "doi_or_url": None, "version": None}}
        with self.assertRaises(ret_check.RetCheckConversionError) as ctx:
            ret_check.reproduction_card_to_row(card, claim="c")
        self.assertEqual(str(ctx.exception), ret_check.COQ_KERNEL_REFUSAL_MESSAGE)

    def test_coq_kernel_never_produces_a_row_regardless_of_other_fields(self):
        # Even a coq_kernel card that also happens to carry a plausible external-oracle-shaped
        # lineage must still be refused -- sec 4's rule has no override.
        card = {
            "id": "REPRO-TEST-COQ-2",
            "oracle": {"kind": "coq_kernel", "source": "Particle Data Group", "doi_or_url": None, "version": "2024"},
            "lineage": {"run_by": "someone", "ces": None},
        }
        with self.assertRaises(ret_check.RetCheckConversionError):
            ret_check.reproduction_card_to_row(card, claim="c", independence_class="I5")

    def test_unrecognized_oracle_kind_refused(self):
        card = {"id": "REPRO-TEST-BAD", "oracle": {"kind": "not-a-real-kind", "source": "x", "doi_or_url": None, "version": None}}
        with self.assertRaises(ret_check.RetCheckConversionError):
            ret_check.reproduction_card_to_row(card, claim="c")

    def test_converted_row_matches_f_scenario_fixture_row(self):
        """The 7th row of cases/ret/F_reproduction_card.json is the same converter output this
        test class exercises directly -- one computation, cited in two places, never duplicated
        logic (P19/P0 one-fact-one-home)."""
        row = ret_check.reproduction_card_to_row(self.PDG_CARD, claim="f-reproduction-claim")
        f_rows = json.loads((CASES_DIR / "F_reproduction_card.json").read_text(encoding="utf-8"))
        world_record_rows = [r for r in f_rows if r["record_type"] == "world_record"]
        self.assertEqual(len(world_record_rows), 1)
        filed = world_record_rows[0]
        for key in ("claim", "agent", "parent", "source_root", "root_independent", "record_type"):
            self.assertEqual(row[key], filed[key], key)


class TestScenarioF(unittest.TestCase):
    """F -- Reproduction interruption (`design/RESISTANCE_LADDER_v0_1.md` sec 4; preregistration
    v0.3 addendum): scenario A's Mirror rows plus one `world_record` row emitted from a
    Reproduction Card via `reproduction_card_to_row()`. Expected delta over scenario A: N_P rises
    by exactly one root, N_P^ind rises by exactly one (the card's oracle is independent by
    construction), an external interruption is now present, and RET RISK flips HIGH -> LOW via
    rule 2 -- the same pattern scenario C/E already exercise, now reached through the v0.3
    converter path instead of a hand-authored row."""

    def test_f_reproduction_card_flips_risk_to_low(self):
        mirror = ret_check.run(CASES_DIR / "A_mirror.json")
        a = _claim(mirror, "a-mirror-claim")

        result = ret_check.run(CASES_DIR / "F_reproduction_card.json")
        f = _claim(result, "f-reproduction-claim")

        # Same endorsement structure and cycle as scenario A (rows 1-6 are A's rows, claim renamed).
        self.assertEqual(f["n_a"], a["n_a"])
        self.assertEqual(f["n_a"], 5)
        self.assertTrue(f["cycle_detected"])
        self.assertEqual(f["cycle_detected"], a["cycle_detected"])

        # The one converter-emitted row adds exactly one root, and that root is independent.
        self.assertEqual(f["n_p"], a["n_p"] + 1)
        self.assertEqual(f["n_p"], 2)
        self.assertEqual(f["n_p_ind"], a["n_p_ind"] + 1)
        self.assertEqual(f["n_p_ind"], 1)

        # A had no external interruption; F does, from the converted row alone.
        self.assertFalse(a["external_interruption_present"])
        self.assertTrue(f["external_interruption_present"])
        self.assertEqual(len(f["external_interruption_rows"]), 1)
        self.assertEqual(f["external_interruption_rows"][0]["record_type"], "world_record")

        # A is HIGH (rule 3); F flips to LOW via rule 2 -- same mechanism as C/E, new input path.
        self.assertEqual(a["risk"], "HIGH")
        self.assertEqual(f["risk"], "LOW")
        self.assertIn("rule 2", f["risk_reason"])

    def test_f_row_is_reproducible_from_the_converter(self):
        """Re-derive the case file's own converted row from the fixture card and require an
        EXACT match -- the filed row is not a hand-typed guess at what the converter would emit."""
        card = TestReproductionCardConverter.PDG_CARD
        recomputed = ret_check.reproduction_card_to_row(card, claim="f-reproduction-claim")
        filed_rows = json.loads((CASES_DIR / "F_reproduction_card.json").read_text(encoding="utf-8"))
        filed = [r for r in filed_rows if r["record_type"] == "world_record"][0]
        self.assertEqual(recomputed["agent"], filed["agent"])
        self.assertEqual(recomputed["source_root"], filed["source_root"])
        self.assertEqual(recomputed["root_independent"], filed["root_independent"])
        self.assertEqual(recomputed["record_type"], filed["record_type"])
        self.assertEqual(recomputed["parent"], filed["parent"])


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
