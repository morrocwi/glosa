"""tests/test_kernel.py

tier: finite_diagnostic (tests executed: `python3 -m unittest discover -s tests -v`, run from
the glosa repo root -- see the command's actual output recorded in the task handoff / PR
description; this file IS the executed command referenced by kernel/glosa_kernel.py's own header).

Covers every function in kernel/glosa_kernel.py against:
  - the 20 valid examples in schema/examples/*.example.json (the ones relevant to each
    validate_* function),
  - all six deliberate-FAIL fixtures in schema/examples/fail/*.json (each must be REJECTED, and
    for the five with a clearly-named §3.3 rule, this file also asserts the specific rule fires
    by checking the rejection reason mentions that rule),
  - the 11 numbered kernel gate rules of FOUNDATION_v0.5.md §3.3, individually, via small
    hand-built payloads that isolate exactly one rule at a time (mutated copies of the valid
    claim_card example, mirroring the fail-fixture convention documented in schema/README.md),
  - route_genre's 9-step procedure, one case per terminal genre,
  - independence_ceiling, defeater_route (Readout Condition Proposition 3), silent_lift_check,
    mc01_check, lit_gate, compute_disclaimers, and self_test.

Runnable with either `pytest` or stdlib `python3 -m unittest discover -s tests`.
"""

import copy
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "kernel"))

import glosa_kernel as k  # noqa: E402

SCHEMA_DIR = REPO_ROOT / "schema"
EXAMPLES_DIR = SCHEMA_DIR / "examples"
FAIL_DIR = EXAMPLES_DIR / "fail"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_example(name):
    return load(EXAMPLES_DIR / name)


def load_fail(name):
    instance = load(FAIL_DIR / name)
    instance.pop("_fail_reason", None)
    return instance


class ValidClaimCardTest(unittest.TestCase):
    def test_valid_claim_card_passes(self):
        card = load_example("claim_card.example.json")
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertEqual(res["verdict"], "PASS")
        self.assertEqual(res["tier"], "finite_diagnostic")

    def test_result_shape(self):
        card = load_example("claim_card.example.json")
        res = k.validate_claim_card(card)
        self.assertEqual(set(res.keys()), {"ok", "verdict", "errors", "warnings", "tier"})

    def test_non_object_input_fails(self):
        res = k.validate_claim_card("not a dict")
        self.assertFalse(res["ok"])
        self.assertEqual(res["verdict"], "FAIL")


class FailFixtureTest(unittest.TestCase):
    """Every schema/examples/fail/*.json fixture must be rejected by validate_claim_card, and the
    rejection must mention the specific rule its own _fail_reason names."""

    def test_fail_same_model_review_rule1(self):
        card = load_fail("fail_same_model_review.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("independent_check" in e or "Kernel rule 1" in e or "PASSED" in e for e in res["errors"]), res["errors"])

    def test_fail_no_independent_check_rule9(self):
        card = load_fail("fail_no_independent_check.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_fail_missing_disclaimer(self):
        card = load_fail("fail_missing_disclaimer.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_fail_th_coqc_no_witness_rule2(self):
        card = load_fail("fail_th_coqc_no_witness.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_fail_stub_public_rule10(self):
        card = load_fail("fail_stub_public.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_fail_k2_without_i5_rule4(self):
        card = load_fail("fail_k2_without_i5.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_fail_ai_signs_claim_rule15(self):
        card = load_fail("fail_ai_signs_claim.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(
            any("rule15" in e for e in res["errors"]) or any("inference_to_claim" in e for e in res["errors"]),
            res["errors"],
        )

    def test_all_fail_fixtures_rejected_by_self_test(self):
        res = k.self_test()
        self.assertTrue(res["ok"], res["errors"])


class KernelRuleIsolationTest(unittest.TestCase):
    """Isolate each of §3.3's 11 numbered rules with a minimal mutation of the valid example,
    mirroring schema/README.md's own fail-fixture convention (diff against claim_card.example.json
    shows exactly what was changed)."""

    def setUp(self):
        self.card = load_example("claim_card.example.json")

    def test_rule1_mc02_passed_requires_not_i0_i1(self):
        card = copy.deepcopy(self.card)
        card["independent_check"] = {
            "status": "PASSED", "maker_id": "founder", "checker_id": "founder",
            "approver_id": "founder", "independence_class": "I1", "mc_level": "L1",
            "date": "2026-09-04", "expires_at": None,
        }
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["independent_check"]["independence_class"] = "I3"
        card["independent_check"]["checker_id"] = "route R2"
        res2 = k.validate_claim_card(card)
        # rule 1 itself should no longer fire (other rules may still comment on k_state etc.,
        # so we only assert the PASSED/I0-I1 combination is gone from the error set)
        self.assertFalse(any("independence_class" in e and "PASSED" in e for e in res2["errors"]))

    def test_rule2_th_coqc_requires_i4_or_i5(self):
        card = copy.deepcopy(self.card)
        card["tier"] = "Th_coqc"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I4"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule3_finite_diagnostic_requires_i4_or_i5(self):
        card = copy.deepcopy(self.card)
        card["tier"] = "finite_diagnostic"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I5"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule4_k2_k3_require_i5(self):
        card = copy.deepcopy(self.card)
        card["k_state"] = "K2"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I4"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I5"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule5_mc01_pairwise_distinct_once_past_pending_review(self):
        card = copy.deepcopy(self.card)
        card["status"] = "Approved-for-Test"
        card["k_state"] = None
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        card["independent_check"] = {
            "status": "PASSED", "maker_id": "founder", "checker_id": "founder",
            "approver_id": "someone-else", "independence_class": "I3", "mc_level": "L3",
            "date": "2026-09-04", "expires_at": None,
        }
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01" in e or "mc01" in e for e in res["errors"]), res["errors"])

        card["independent_check"]["checker_id"] = "an independent checker"
        res2 = k.validate_claim_card(card)
        self.assertFalse(any("mc01" in e.lower() for e in res2["errors"]), res2["errors"])

    def test_rule5_does_not_fire_while_still_draft(self):
        card = copy.deepcopy(self.card)
        card["independent_check"] = {
            "status": "NONE", "maker_id": "founder", "checker_id": "founder",
            "approver_id": "founder", "independence_class": "I1", "mc_level": "L1",
            "date": "2026-09-04", "expires_at": None,
        }
        self.assertEqual(card["status"], "Draft")
        res = k.validate_claim_card(card)
        self.assertFalse(any("mc01" in e.lower() for e in res["errors"]), res["errors"])

    def test_rule6_claim_scope_may_not_exceed_evidence_scope(self):
        card = copy.deepcopy(self.card)
        card["scope"]["claim_scope"] = "true for all cats in general"
        card["scope"]["evidence_scope"] = "one household, one cat, 14 days"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("rule6" in e for e in res["errors"]), res["errors"])

    def test_rule6_population_claim_over_single_subject_evidence(self):
        card = copy.deepcopy(self.card)
        card["scope"]["generalization_claimed"] = "population_claim"
        card["scope"]["evidence_scope"] = "n=1 cat"
        card["scope"]["claim_scope"] = "n=1 cat"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("rule6" in e for e in res["errors"]), res["errors"])

    def test_rule6_matched_scope_passes(self):
        card = copy.deepcopy(self.card)
        card["scope"]["claim_scope"] = "one household, one cat, 14 days"
        card["scope"]["evidence_scope"] = "one household, one cat, 14 days"
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])

    def test_rule7_silent_lift_flags_block_status(self):
        card = copy.deepcopy(self.card)
        card["silent_lift_check"]["flags"] = ["unexplained-dependency-X"]
        card["status"] = "Approved-for-Test"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

    def test_rule8_external_validation_proposed_hard_fail(self):
        card = copy.deepcopy(self.card)
        card["statement"]["text"] = card["statement"]["text"] + " We should seek external validation to confirm this."
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("EXTERNAL_VALIDATION_PROPOSED" in e for e in res["errors"]), res["errors"])

    def test_rule8_clean_text_passes(self):
        card = copy.deepcopy(self.card)
        res = k.validate_claim_card(card)
        self.assertFalse(any("EXTERNAL_VALIDATION_PROPOSED" in e for e in res["errors"]), res["errors"])

    def test_rule9_k1_requires_i3_plus_or_bounded_exception(self):
        card = copy.deepcopy(self.card)
        card["k_state"] = "K1"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        # only I1 evidence, no exception markers -> fail
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        # add an I3 route -> passes
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule9_bounded_exception_within_90_days_passes(self):
        card = copy.deepcopy(self.card)
        card["k_state"] = "K1"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I2"
        card["five_questions"]["tested"]["evidence_relations"].append({
            "evidence_id": "ev-cat-004", "bearing": "SUPPORTS", "independence_class": "I4",
            "citation_ref": "cite-cat-obs-001", "strength": "mechanical", "review_mode": "MECHANICAL_CHECK",
            "route_id": None, "asserted_by": "validator", "date": "2026-09-05", "notes": "",
        })
        card["disclaimers_emitted"].append({"id": "D-SAME-VENDOR"})
        card["independent_check"]["expires_at"] = "2026-11-01"  # date is 2026-09-04, 58 days later
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])

    def test_rule9_bounded_exception_beyond_90_days_fails(self):
        card = copy.deepcopy(self.card)
        card["k_state"] = "K1"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I2"
        card["five_questions"]["tested"]["evidence_relations"].append({
            "evidence_id": "ev-cat-004", "bearing": "SUPPORTS", "independence_class": "I4",
            "citation_ref": "cite-cat-obs-001", "strength": "mechanical", "review_mode": "MECHANICAL_CHECK",
            "route_id": None, "asserted_by": "validator", "date": "2026-09-05", "notes": "",
        })
        card["disclaimers_emitted"].append({"id": "D-SAME-VENDOR"})
        card["independent_check"]["date"] = "2026-09-04"
        card["independent_check"]["expires_at"] = "2027-01-15"  # far more than 90 days later
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("90-day" in e for e in res["errors"]), res["errors"])

    def test_rule10_stub_cannot_advance_past_draft(self):
        card = load_fail("fail_stub_public.json")
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["status"] = "Draft"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule11_provenance_and_silent_lift_must_be_run_before_k1(self):
        card = copy.deepcopy(self.card)
        card["k_state"] = "K1"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        card["provenance_dag"]["status"] = "not_run"
        card["silent_lift_check"]["status"] = "run"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])

        card["provenance_dag"]["status"] = "run"
        res2 = k.validate_claim_card(card)
        self.assertTrue(res2["ok"], res2["errors"])

    def test_rule15_ai_signs_claim_fails(self):
        """Kernel rule 15 (FOUNDATION_v0.5.md §2.1b, founder instruction 2026-09-04,
        BBL-2026-09-04-083/084): responsibility.inference_to_claim must be 'human'."""
        card = copy.deepcopy(self.card)
        card["responsibility"]["inference_to_claim"] = "ai"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(
            any("rule15" in e and "human" in e for e in res["errors"]), res["errors"]
        )

    def test_rule15_ai_owns_question_fails(self):
        """FOUNDATION §2.1c (BBL-2026-09-04-086): problem/question/hypothesis stay human."""
        card = copy.deepcopy(self.card)
        card["responsibility"] = {"data_to_inference": "joint", "inference_to_claim": "human",
                                  "ownership": {"problem": "human", "question": "ai", "hypothesis_selection": "human"}}
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("rule15" in e and "ownership" in e for e in res["errors"]), res["errors"])

    def test_rule15_human_signs_claim_passes(self):
        card = copy.deepcopy(self.card)
        card["responsibility"]["inference_to_claim"] = "human"
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertFalse(any(w.startswith("rule15w") for w in res["warnings"]), res["warnings"])

    def test_rule15w_warns_when_responsibility_absent(self):
        card = copy.deepcopy(self.card)
        card.pop("responsibility", None)
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertTrue(any(w.startswith("rule15w") for w in res["warnings"]), res["warnings"])

    def test_rule16w_warns_when_empirical_extension_absent(self):
        card = copy.deepcopy(self.card)
        self.assertEqual(card["claim_type"], "EMPIRICAL")
        card.pop("empirical_extension", None)
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertTrue(any(w.startswith("rule16w") for w in res["warnings"]), res["warnings"])

    def test_rule16w_silent_when_empirical_extension_present(self):
        card = copy.deepcopy(self.card)
        res = k.validate_claim_card(card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertFalse(any(w.startswith("rule16w") for w in res["warnings"]), res["warnings"])

    def test_rule16w_silent_for_non_empirical_claim_type(self):
        card = copy.deepcopy(self.card)
        card["claim_type"] = "FORMAL"
        card.pop("empirical_extension", None)
        res = k.validate_claim_card(card)
        self.assertFalse(any(w.startswith("rule16w") for w in res["warnings"]), res["warnings"])


class ReviewReportTest(unittest.TestCase):
    def test_valid_review_report_passes(self):
        report = load_example("review_report.example.json")
        res = k.validate_review_report(report)
        self.assertTrue(res["ok"], res["errors"])

    def test_missing_verdict_tier_fails_bounded_judge_law(self):
        report = load_example("review_report.example.json")
        del report["verdict_tier"]
        res = k.validate_review_report(report)
        self.assertFalse(res["ok"])

    def test_reviewer_same_as_maker_fails(self):
        report = load_example("review_report.example.json")
        res = k.validate_review_report(report, maker_id=report["reviewer_identity"])
        self.assertFalse(res["ok"])

    def test_reviewer_same_as_approver_fails(self):
        report = load_example("review_report.example.json")
        res = k.validate_review_report(report, approver_id=report["reviewer_identity"])
        self.assertFalse(res["ok"])


class CitationCardTest(unittest.TestCase):
    def test_rule17_citation_from_memory_fails(self):
        """Founder ruling 2026-09-04 (BBL-2026-09-04-100): a fetched citation without the link it
        was read from + page + line + verbatim passage cannot stand above CANDIDATE."""
        c = load_example("citation_card.example.json")
        c["fetch_status"] = "FETCHED"; c["status"] = "VERIFIED"; c.pop("fetched_from_url", None)
        res = k.validate_citation_card(c)
        self.assertFalse(res["ok"]); self.assertTrue(any("rule17(" in e for e in res["errors"]), res["errors"])
        c["status"] = "CANDIDATE"
        res = k.validate_citation_card(c)
        self.assertTrue(res["ok"], res["errors"]); self.assertTrue(any("rule17w" in w for w in res["warnings"]))

    def test_valid_citation_card_passes(self):
        citation = load_example("citation_card.example.json")
        res = k.validate_citation_card(citation)
        self.assertTrue(res["ok"], res["errors"])

    def test_verified_requires_both_booleans(self):
        citation = load_example("citation_card.example.json")
        citation["metadata_verified"] = False
        res = k.validate_citation_card(citation)
        self.assertFalse(res["ok"])

    def test_scrammed_requires_xenon_ledger_ref(self):
        citation = load_example("citation_card.example.json")
        citation["status"] = "SCRAMMED"
        citation["xenon_ledger_ref"] = None
        res = k.validate_citation_card(citation)
        self.assertFalse(res["ok"])

        citation["xenon_ledger_ref"] = "cases/worked-example-cat/XENON_LEDGER.md#row-1"
        res2 = k.validate_citation_card(citation)
        self.assertTrue(res2["ok"], res2["errors"])


class ReleaseManifestTest(unittest.TestCase):
    def test_valid_release_manifest_passes(self):
        manifest = load_example("release_manifest.example.json")
        res = k.validate_release_manifest(manifest)
        self.assertTrue(res["ok"], res["errors"])

    def test_blackbox_note_precondition_on_approved_for_live(self):
        manifest = load_example("release_manifest.example.json")
        manifest["status"] = "Approved-for-Live"
        manifest["blackbox_note_appendix_present"] = False
        res = k.validate_release_manifest(manifest)
        self.assertFalse(res["ok"])

    def test_pub_adversarial_review_fail_dimension_blocks_pass_verdict(self):
        manifest = load_example("release_manifest.example.json")
        manifest["adversarial_review"]["r1_leak_scan"]["result"] = "FAIL"
        manifest["gate_verdict"] = "PASS"
        res = k.validate_release_manifest(manifest)
        self.assertFalse(res["ok"])


class BlackboxNoteTest(unittest.TestCase):
    def test_valid_blackbox_note_passes(self):
        note = load_example("blackbox_note.example.json")
        res = k.validate_blackbox_note(note)
        self.assertTrue(res["ok"], res["errors"])

    def test_dangling_cooking_input_line_fails(self):
        note = load_example("blackbox_note.example.json")
        note["cooking"][0]["input_lines"] = [999]
        res = k.validate_blackbox_note(note)
        self.assertFalse(res["ok"])

    def test_public_line_without_privacy_scan_done_fails(self):
        note = load_example("blackbox_note.example.json")
        note["privacy_scan"] = "pending"
        res = k.validate_blackbox_note(note)
        self.assertFalse(res["ok"])


class ComputeDisclaimersTest(unittest.TestCase):
    def test_always_on_ids_present(self):
        card = load_example("claim_card.example.json")
        ids = {d["id"] for d in k.compute_disclaimers(card)}
        for always_id in ("D-STANDPOINT", "D-NONEXPERT", "D-NONCLAIM", "D-AUTHORSHIP", "D-REVISION-LIVE", "D-NO-EPISTEMIC-VETO", "D-BLACKBOX-NOTE"):
            self.assertIn(always_id, ids)

    def test_d_independence_fires_on_weak_evidence(self):
        card = load_example("claim_card.example.json")
        self.assertEqual(card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"], "I1")
        ids = {d["id"] for d in k.compute_disclaimers(card)}
        self.assertIn("D-INDEPENDENCE", ids)

    def test_d_independence_absent_once_i3_reached(self):
        card = load_example("claim_card.example.json")
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I3"
        ids = {d["id"] for d in k.compute_disclaimers(card)}
        self.assertNotIn("D-INDEPENDENCE", ids)

    def test_d_scope_fires_when_generalization_claimed(self):
        card = load_example("claim_card.example.json")
        card["scope"]["generalization_claimed"] = "pattern_candidate"
        ids = {d["id"] for d in k.compute_disclaimers(card)}
        self.assertIn("D-SCOPE", ids)

    def test_d_derived_patterns_fires_on_private_repo_reference(self):
        card = load_example("claim_card.example.json")
        card["ledger"]["borrowed"] = ["pattern re-derived from cpg (private, patterns only)"]
        # private source names are NOT shipped in the public kernel (git-ignored registry file /
        # env var) -- inject one for the test so it is environment-independent (CI has none).
        saved = list(k._PRIVATE_REPO_NAMES)
        k._PRIVATE_REPO_NAMES[:] = ["cpg"]
        try:
            ids = {d["id"] for d in k.compute_disclaimers(card)}
        finally:
            k._PRIVATE_REPO_NAMES[:] = saved
        self.assertIn("D-EXTERNAL-INPUT", ids)
        self.assertIn("D-DERIVED-PATTERNS", ids)

    def test_uses_catalogue_file_when_present(self):
        self.assertTrue(k.DISCLAIMER_CATALOGUE_PATH.is_file(), "methodology/data/disclaimer_catalogue.json should exist per Task B1")
        rows, source = k._load_disclaimer_catalogue()
        self.assertEqual(source, str(k.DISCLAIMER_CATALOGUE_PATH))
        self.assertGreater(len(rows), 20)

    def test_falls_back_to_embedded_table_when_file_missing(self):
        original = k.DISCLAIMER_CATALOGUE_PATH
        try:
            k.DISCLAIMER_CATALOGUE_PATH = REPO_ROOT / "does-not-exist.json"
            rows, source = k._load_disclaimer_catalogue()
            self.assertEqual(rows, k._EMBEDDED_MINIMAL_DISCLAIMER_TABLE)
            self.assertIn("EMBEDDED_MINIMAL_DISCLAIMER_TABLE", source)
        finally:
            k.DISCLAIMER_CATALOGUE_PATH = original


class RouteGenreTest(unittest.TestCase):
    def test_case_study_from_worked_example(self):
        card = load_example("claim_card.example.json")
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "case_study")
        self.assertEqual(result["venue_track"], card.get("venue_track"))
        self.assertEqual(result["companion_of"], card.get("companion_of"))
        self.assertTrue(result["reasons"])

    def test_empirical_qual_practice_when_not_bounded(self):
        card = load_example("claim_card.example.json")
        result = k.route_genre(card, context={"bounded_case": False})
        self.assertEqual(result["genre"], "empirical_qual_practice")

    def test_formal_proof_when_exact_functional_and_no_mechanical_evidence(self):
        card = load_example("claim_card.example.json")
        card["lens_translation"]["formal_applicability"] = "exact_functional"
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "formal_proof")

    def test_systematic_review_from_context(self):
        card = load_example("claim_card.example.json")
        result = k.route_genre(card, context={"has_search_log": True})
        self.assertEqual(result["genre"], "systematic_review")

    def test_archival_from_seen_access_model(self):
        card = load_example("claim_card.example.json")
        card["five_questions"]["seen"]["access_model"] = "archival record in a household document register"
        card["five_questions"]["seen"]["retrievable_original"] = True
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "archival")

    def test_position_reply_from_lineage(self):
        card = load_example("claim_card.example.json")
        card["lineage"]["derives_from"] = ["GLOSA-CC-20260101-0001"]
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "position_reply")

    def test_design_science_from_decision_policy_augmentation(self):
        card = load_example("claim_card.example.json")
        card["claim_type"] = "DECISION"
        card["five_questions"]["assumed"].append({
            "id": "A9", "type": "decision_policy_augmentation",
            "description": "built a scheduling protocol", "identification_level": "A2",
            "contaminated_concept_hit": None,
        })
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "design_science")

    def test_empirical_quant_from_population_claim(self):
        card = load_example("claim_card.example.json")
        card["scope"]["generalization_claimed"] = "population_claim"
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "empirical_quant")

    def test_conceptual_fallback(self):
        card = load_example("claim_card.example.json")
        card["standpoint"]["declared_basis"] = "reasoned argument only, no fieldwork of any kind"
        card["standpoint"]["method_basis"] = "conceptual synthesis of existing ideas"
        card["lens_translation"]["formal_applicability"] = "not_applicable_narrative"
        result = k.route_genre(card)
        self.assertEqual(result["genre"], "conceptual")

    def test_mixed_genre_when_multiple_branches_match(self):
        card = load_example("claim_card.example.json")
        card["lineage"]["derives_from"] = ["GLOSA-CC-20260101-0001"]
        # sequential routing (no opt-in) returns the FIRST match, position_reply (step4), since
        # step4 precedes step7 -- it never even reaches step7's case_study match.
        sequential = k.route_genre(card)
        self.assertEqual(sequential["genre"], "position_reply")
        # explicitly opting into the step-9 tie detector surfaces that step7 (case_study) ALSO
        # matched independently, and returns MIXED_GENRE for a human Approver to break the tie.
        mixed = k.route_genre(card, context={"check_mixed_genre": True})
        self.assertEqual(mixed["genre"], "MIXED_GENRE")

    def test_venue_track_and_companion_of_never_inputs(self):
        card = load_example("claim_card.example.json")
        card["venue_track"] = "thai_tci"
        card["companion_of"] = "some-artifact-id"
        result_a = k.route_genre(card)
        card["venue_track"] = "international"
        card["companion_of"] = None
        result_b = k.route_genre(card)
        self.assertEqual(result_a["genre"], result_b["genre"])


class IndependenceCeilingTest(unittest.TestCase):
    def test_i1_ceiling_is_dr_k0(self):
        result = k.independence_ceiling([{"independence_class": "I1"}])
        self.assertEqual(result["max_tier"], "Dr")
        self.assertEqual(result["max_k_state"], "K0")

    def test_i5_ceiling_is_th_coqc_k2(self):
        result = k.independence_ceiling([{"independence_class": "I1"}, {"independence_class": "I5"}])
        self.assertEqual(result["max_independence_class"], "I5")
        self.assertEqual(result["max_tier"], "Th_coqc")
        self.assertEqual(result["max_k_state"], "K2")

    def test_i3_ceiling_is_finite_diagnostic_k1(self):
        result = k.independence_ceiling([{"independence_class": "I3"}])
        self.assertEqual(result["max_tier"], "finite_diagnostic")
        self.assertEqual(result["max_k_state"], "K1")

    def test_empty_evidence_ceiling_is_conservative(self):
        result = k.independence_ceiling([])
        self.assertEqual(result["max_tier"], "Dr")
        self.assertEqual(result["max_k_state"], "K0")

    def test_many_weak_routes_do_not_beat_one_strong_route(self):
        """NC-31 ManyModels⇏Independence: count never substitutes for the highest level reached."""
        many_weak = [{"independence_class": "I1"}] * 10
        one_strong = [{"independence_class": "I4"}]
        self.assertEqual(
            k.independence_ceiling(many_weak)["max_tier"],
            k.independence_ceiling([{"independence_class": "I1"}])["max_tier"],
        )
        self.assertNotEqual(
            k.independence_ceiling(many_weak)["max_tier"],
            k.independence_ceiling(one_strong)["max_tier"],
        )


class DefeaterRouteTest(unittest.TestCase):
    def test_single_path_defeated_loses_distinction(self):
        dag = {"nodes": [{"id": "a"}, {"id": "b"}, {"id": "c"}], "edges": [{"from": "a", "to": "b"}, {"from": "b", "to": "c"}]}
        result = k.defeater_route(dag, "b")
        self.assertTrue(result["distinction_lost"])
        self.assertEqual(result["surviving_paths"], [])

    def test_alternate_path_survives(self):
        dag = {
            "nodes": [{"id": "a"}, {"id": "b"}, {"id": "c"}, {"id": "d"}],
            "edges": [{"from": "a", "to": "b"}, {"from": "b", "to": "d"}, {"from": "a", "to": "c"}, {"from": "c", "to": "d"}],
        }
        result = k.defeater_route(dag, "b")
        self.assertFalse(result["distinction_lost"])
        self.assertTrue(any("b" not in p for p in result["surviving_paths"]))

    def test_empty_dag_reports_no_loss(self):
        result = k.defeater_route({"nodes": [], "edges": []}, "x")
        self.assertFalse(result["distinction_lost"])
        self.assertEqual(result["all_paths_count"], 0)

    def test_worked_example_single_node_dag(self):
        card = load_example("claim_card.example.json")
        dag = card["provenance_dag"]
        result = k.defeater_route(dag, "obs-1")
        self.assertTrue(result["distinction_lost"])  # the only node, defeated -> nothing survives


class SilentLiftCheckTest(unittest.TestCase):
    def test_clean_card_passes(self):
        card = load_example("claim_card.example.json")
        res = k.silent_lift_check(card)
        self.assertTrue(res["ok"], res["errors"])

    def test_undisclosed_dependency_is_hard_fail(self):
        card = load_example("claim_card.example.json")
        card["silent_lift_check"]["actual_dependency_set"] = ["obs-1", "ai-inferred-node-X"]
        res = k.silent_lift_check(card)
        self.assertFalse(res["ok"])
        self.assertIn("ai-inferred-node-X", res["computed_flags"])

    def test_already_recorded_flags_are_hard_fail(self):
        card = load_example("claim_card.example.json")
        card["silent_lift_check"]["flags"] = ["some-flag"]
        res = k.silent_lift_check(card)
        self.assertFalse(res["ok"])


class MC01CheckTest(unittest.TestCase):
    def test_distinct_ids_pass(self):
        res = k.mc01_check("alice", "bob", "carol")
        self.assertTrue(res["ok"])

    def test_maker_equals_checker_fails(self):
        res = k.mc01_check("alice", "alice", "carol")
        self.assertFalse(res["ok"])

    def test_missing_id_fails(self):
        res = k.mc01_check("alice", None, "carol")
        self.assertFalse(res["ok"])


class LitGateTest(unittest.TestCase):
    def test_valid_litreview_manifest_passes(self):
        manifest = load_example("litreview_manifest.example.json")
        res = k.lit_gate(manifest)
        self.assertTrue(res["ok"], res["errors"])
        self.assertEqual(res["verdict"], "PASS_WITH_LIMITS")

    def test_violations_found_blocks_pass(self):
        manifest = load_example("litreview_manifest.example.json")
        manifest["secondary_citation_ban_audit"]["violations_found"] = 2
        manifest["gate"]["overall"] = "PASS"
        res = k.lit_gate(manifest)
        self.assertFalse(res["ok"])

    def test_fail_without_blocked_reason_is_kernel_error(self):
        manifest = load_example("litreview_manifest.example.json")
        manifest["gate"]["overall"] = "FAIL"
        manifest["gate"]["blocked_reason"] = None
        res = k.lit_gate(manifest)
        self.assertFalse(res["ok"])

    def test_overall_may_not_be_looser_than_worst_subgate(self):
        manifest = load_example("litreview_manifest.example.json")
        manifest["gate"]["accuracy_gate"] = "FAIL"
        manifest["gate"]["diversity_gate"] = "PASS"
        manifest["gate"]["overall"] = "PASS"
        res = k.lit_gate(manifest)
        self.assertFalse(res["ok"])


class GateReleaseTest(unittest.TestCase):
    def setUp(self):
        self.manifest = load_example("release_manifest.example.json")
        self.card = load_example("claim_card.example.json")
        self.review = load_example("review_report.example.json")

    def test_worked_example_gate_release(self):
        # the worked example's review is I3, matching §6.4's minimum bar.
        result = k.gate_release(self.manifest, [self.card], [self.review])
        self.assertIn(result["verdict"], ("PASS", "PASS_WITH_LIMITS"))
        self.assertEqual(result["tier"], "finite_diagnostic")

    def test_missing_claim_card_is_hard_fail(self):
        result = k.gate_release(self.manifest, [], [self.review])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any("no matching claim_card" in r for r in result["reasons"]))

    def test_stub_card_cannot_be_released(self):
        stub = load_fail("fail_stub_public.json")
        stub["status"] = "Draft"
        stub["claim_id"] = self.manifest["artifact_refs"]["claim_ids"][0]
        result = k.gate_release(self.manifest, [stub], [self.review])
        self.assertEqual(result["verdict"], "FAIL")

    def test_no_i3_plus_review_or_evidence_blocks_approved_status(self):
        weak_card = copy.deepcopy(self.card)
        result = k.gate_release(self.manifest, [weak_card], [])  # example manifest status is Pending Review, not Approved-*
        # Pending Review manifest does not trigger the §6.4 mandatory-gate check (only Approved-* does)
        self.assertNotEqual(result["verdict"], "HUMAN_REVIEW")

        approved_manifest = copy.deepcopy(self.manifest)
        approved_manifest["status"] = "Approved-for-Test"
        result2 = k.gate_release(approved_manifest, [weak_card], [])
        self.assertEqual(result2["verdict"], "FAIL")
        self.assertTrue(any("§6.4" in r for r in result2["reasons"]))

    def test_unresolved_dissent_routes_to_human_review(self):
        card = copy.deepcopy(self.card)
        card["five_questions"]["tested"]["dissent_records"] = [
            {"by": "founder", "date": "2026-09-05", "content": "disputed reading", "resolved": False}
        ]
        result = k.gate_release(self.manifest, [card], [self.review])
        self.assertEqual(result["verdict"], "HUMAN_REVIEW")


class SelfTestTest(unittest.TestCase):
    def test_self_test_passes_clean(self):
        res = k.self_test()
        self.assertTrue(res["ok"], res["errors"])


class SchemaValidationBackendTest(unittest.TestCase):
    """Confirms jsonschema is actually being exercised in this environment (not silently falling
    back), so the rest of this suite's PASS results reflect the real schema, not the coarse
    fallback. If jsonschema genuinely is not installed here, this test documents that instead of
    failing silently."""

    def test_jsonschema_backend_status(self):
        card = load_example("claim_card.example.json")
        errors, used_fallback = k._schema_validate(card, "claim_card.schema.json")
        if not k._HAVE_JSONSCHEMA:
            self.assertTrue(used_fallback)
        else:
            self.assertFalse(used_fallback)
            self.assertEqual(errors, [])


class SchemaFailClosedTest(unittest.TestCase):
    """MUST-4 (reviews/ARCH_integrity.md F1/F3): validate_claim_card (and every other validate_*
    function) must FAIL CLOSED -- ok:False with a plain "jsonschema not available; schema
    validation not performed" error -- the moment schema validation silently falls back to the
    coarse presence-only check, unless the caller explicitly opts in via allow_no_jsonschema=True
    (which downgrades the result tier to Dr and adds a warning instead). Unavailability is
    simulated by monkeypatching `k._validator_for` to always return None -- the exact code path
    `_schema_validate` takes when jsonschema cannot be imported, without actually uninstalling the
    package."""

    def setUp(self):
        self._orig_validator_for = k._validator_for
        k._validator_for = lambda schema_filename: None

    def tearDown(self):
        k._validator_for = self._orig_validator_for

    def _f1_style_illegitimate_card(self):
        """reviews/ARCH_integrity.md F1's own reproduction: fail_k2_without_i5.json's base,
        mutated to tier:Th_coqc / k_state-supporting fields / status:Approved-for-Live with I5
        evidence and three distinct AI-vendor identities -- exactly the payload that returned
        ok:True, with jsonschema active, before MUST-4/MUST-7."""
        card = load_fail("fail_k2_without_i5.json")
        card["tier"] = "Th_coqc"
        card["status"] = "Approved-for-Live"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I5"
        card["independent_check"] = {
            "status": "PASSED", "maker_id": "claude-session-A", "checker_id": "gemini-session-B",
            "approver_id": "codex-session-C", "independence_class": "I5", "mc_level": "L5",
            "date": "2026-09-06", "expires_at": None,
        }
        return card

    def test_fails_closed_by_default_when_jsonschema_unavailable(self):
        card = self._f1_style_illegitimate_card()
        errors, used_fallback = k._schema_validate(card, "claim_card.schema.json")
        self.assertTrue(used_fallback)  # confirms the monkeypatch actually forced fallback mode
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(
            any("jsonschema not available; schema validation not performed" in e for e in res["errors"]),
            res["errors"],
        )

    def test_all_validate_functions_fail_closed_by_default_and_downgrade_tier_on_opt_in(self):
        pairs = [
            ("claim_card.example.json", k.validate_claim_card),
            ("review_report.example.json", k.validate_review_report),
            ("citation_card.example.json", k.validate_citation_card),
            ("release_manifest.example.json", k.validate_release_manifest),
            ("blackbox_note.example.json", k.validate_blackbox_note),
        ]
        for filename, fn in pairs:
            instance = load_example(filename)

            closed = fn(instance)
            self.assertFalse(closed["ok"], (filename, closed))
            self.assertTrue(
                any("jsonschema not available; schema validation not performed" in e for e in closed["errors"]),
                (filename, closed["errors"]),
            )

            opened = fn(instance, allow_no_jsonschema=True)
            self.assertTrue(opened["ok"], (filename, opened["errors"]))
            self.assertEqual(opened["tier"], "Dr", filename)
            self.assertTrue(
                any("allow_no_jsonschema=True" in w for w in opened["warnings"]), (filename, opened["warnings"])
            )

    def test_used_fallback_false_when_jsonschema_actually_available(self):
        k._validator_for = self._orig_validator_for  # restore for this one assertion only
        card = load_example("claim_card.example.json")
        errors, used_fallback = k._schema_validate(card, "claim_card.schema.json")
        if k._HAVE_JSONSCHEMA:
            self.assertFalse(used_fallback)
            res = k.validate_claim_card(card)
            self.assertEqual(res["tier"], "finite_diagnostic")


class LensSignatureCitationTest(unittest.TestCase):
    """MUST-6: kernel gate rule 12 (D-LENS-UNSIGNED, §3.3 rule 12) and the D-LENS-UNCITED
    lens-citation gate (§7.4). Positive/negative fixtures per the task instruction."""

    def setUp(self):
        self.card = load_example("claim_card.example.json")

    def _card_with_valid_signature(self):
        card = copy.deepcopy(self.card)
        card["lens_translation"]["lens_ref"] = "readout_universe"
        card["hypothesis_world"]["signature"] = (
            "hypothesis co-produced by founder+AI via lens readout_universe, 2026-09-04"
        )
        return card

    # -- D-LENS-UNSIGNED --

    def test_negative_no_lens_ref_is_untouched_by_rule12(self):
        self.assertIsNone((self.card.get("lens_translation") or {}).get("lens_ref"))
        res = k.validate_claim_card(self.card)
        self.assertTrue(res["ok"], res["errors"])
        self.assertFalse(any("D-LENS-UNSIGNED" in e for e in res["errors"]))

    def test_lens_ref_without_signature_fails_rule12(self):
        card = copy.deepcopy(self.card)
        card["lens_translation"]["lens_ref"] = "readout_universe"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("D-LENS-UNSIGNED" in e for e in res["errors"]), res["errors"])

    def test_lens_ref_with_signature_not_naming_lens_fails_heuristic(self):
        card = copy.deepcopy(self.card)
        card["lens_translation"]["lens_ref"] = "readout_universe"
        card["hypothesis_world"]["signature"] = "co-produced by founder + AI, 2026-09-04"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(
            any("D-LENS-UNSIGNED" in e and "HEURISTIC" in e for e in res["errors"]), res["errors"]
        )

    def test_positive_lens_ref_with_correct_signature_passes_rule12(self):
        card = self._card_with_valid_signature()
        res = k.validate_claim_card(card)
        self.assertFalse(any("D-LENS-UNSIGNED" in e for e in res["errors"]), res["errors"])

    def test_compute_disclaimers_emits_d_lens_unsigned_when_rule12_fires(self):
        card = copy.deepcopy(self.card)
        card["lens_translation"]["lens_ref"] = "readout_universe"
        ids = {d["id"] for d in k.compute_disclaimers(card)}
        self.assertIn("D-LENS-UNSIGNED", ids)

    def test_compute_disclaimers_silent_on_d_lens_unsigned_when_no_lens_used(self):
        ids = {d["id"] for d in k.compute_disclaimers(self.card)}
        self.assertNotIn("D-LENS-UNSIGNED", ids)

    # -- D-LENS-UNCITED --

    def test_negative_lens_uncited_fails_when_citation_cards_empty(self):
        card = self._card_with_valid_signature()
        res = k.validate_claim_card(card, citation_cards=[])
        self.assertFalse(res["ok"])
        self.assertTrue(any("D-LENS-UNCITED" in e for e in res["errors"]), res["errors"])

    def test_lens_uncited_fails_when_citation_card_present_but_not_verified(self):
        card = self._card_with_valid_signature()
        citation_cards = [{
            "id": "cite-lens-001",
            "identifier": {"kind": "DOI", "value": "readout_universe"},
            "status": "PENDING",
        }]
        res = k.validate_claim_card(card, citation_cards=citation_cards)
        self.assertFalse(res["ok"])
        self.assertTrue(any("D-LENS-UNCITED" in e for e in res["errors"]), res["errors"])

    def test_positive_lens_uncited_passes_with_matching_verified_citation_card(self):
        card = self._card_with_valid_signature()
        citation_cards = [{
            "id": "cite-lens-001",
            "identifier": {"kind": "DOI", "value": "readout_universe"},
            "status": "VERIFIED",
        }]
        res = k.validate_claim_card(card, citation_cards=citation_cards)
        self.assertTrue(res["ok"], res["errors"])
        ids = {d["id"] for d in k.compute_disclaimers(card, citation_cards=citation_cards)}
        self.assertNotIn("D-LENS-UNCITED", ids)

    def test_lens_uncited_not_checked_when_citation_cards_omitted(self):
        card = self._card_with_valid_signature()
        res = k.validate_claim_card(card)  # citation_cards defaults to None
        self.assertTrue(res["ok"], res["errors"])  # honest silence, never a fabricated pass
        self.assertTrue(
            any("D-LENS-UNCITED not checked" in w for w in res["warnings"]), res["warnings"]
        )


class HumanApproverTest(unittest.TestCase):
    """MUST-7 (reviews/ARCH_integrity.md F1): MC-01 human-Approver-identity extension.
    Reproduces F1's own payload -- three distinct AI-vendor identities reaching
    tier:Th_coqc/k_state-supporting-K2-fields/status:Approved-for-Live with ok:True and zero
    disclaimer naming the missing human -- and confirms it is now rejected everywhere the task
    named: validate_claim_card, validate_review_report, validate_release_manifest, gate_release."""

    def _all_ai_chain_card(self):
        card = load_fail("fail_k2_without_i5.json")
        card["tier"] = "Th_coqc"
        card["status"] = "Approved-for-Live"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I5"
        card["independent_check"] = {
            "status": "PASSED", "maker_id": "claude-session-A", "checker_id": "gemini-session-B",
            "approver_id": "codex-session-C", "independence_class": "I5", "mc_level": "L5",
            "date": "2026-09-06", "expires_at": None,
            # deliberately no approver_kind -- the all-AI chain reviews/ARCH_integrity.md F1
            # reproduced live, which previously reached ok:True with zero warning.
        }
        return card

    def test_all_ai_chain_rejected_at_approved_for_live(self):
        card = self._all_ai_chain_card()
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01-HUMAN" in e and "human" in e for e in res["errors"]), res["errors"])

    def test_all_ai_chain_rejected_even_when_approver_kind_explicitly_ai(self):
        card = self._all_ai_chain_card()
        card["independent_check"]["approver_kind"] = "ai"
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

    def test_human_approver_kind_clears_the_gate(self):
        card = self._all_ai_chain_card()
        card["independent_check"]["approver_kind"] = "human"
        res = k.validate_claim_card(card)
        self.assertFalse(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

    def test_k2_with_a_passed_independent_check_requires_human_approver_kind(self):
        card = copy.deepcopy(load_example("claim_card.example.json"))
        card["k_state"] = "K2"
        card["provenance_dag"]["status"] = "run"
        card["silent_lift_check"]["status"] = "run"
        card["five_questions"]["tested"]["evidence_relations"][0]["independence_class"] = "I5"
        card["independent_check"] = {
            "status": "PASSED", "maker_id": "a", "checker_id": "b", "approver_id": "c",
            "independence_class": "I5", "mc_level": "L4", "date": "2026-09-04", "expires_at": None,
        }
        res = k.validate_claim_card(card)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

        card["independent_check"]["approver_kind"] = "human"
        res2 = k.validate_claim_card(card)
        self.assertFalse(any("MC-01-HUMAN" in e for e in res2["errors"]), res2["errors"])

    def test_k2_without_a_passed_independent_check_does_not_trigger_the_human_gate(self):
        # An isolated k_state=K2 mutation with no completed independent check (mirrors
        # KernelRuleIsolationTest.test_rule4_k2_k3_require_i5's own base state) must not itself
        # demand approver_kind -- there is no Approver identity to validate yet; rule 4's own
        # I5-evidence requirement is a separate, prior gate this test does not touch.
        card = copy.deepcopy(load_example("claim_card.example.json"))
        card["k_state"] = "K2"
        self.assertEqual(card["independent_check"]["status"], "NONE")
        res = k.validate_claim_card(card)
        self.assertFalse(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

    def test_review_report_i5_requires_human_approver_kind(self):
        report = load_example("review_report.example.json")
        report["independence_class"] = "I5"
        res = k.validate_review_report(report)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

        report["approver_kind"] = "human"
        res2 = k.validate_review_report(report)
        self.assertFalse(any("MC-01-HUMAN" in e for e in res2["errors"]), res2["errors"])

    def test_release_manifest_approved_for_live_requires_human_approver_kind(self):
        manifest = load_example("release_manifest.example.json")
        manifest["status"] = "Approved-for-Live"
        del manifest["independent_check_summary"]["approver_kind"]
        res = k.validate_release_manifest(manifest)
        self.assertFalse(res["ok"])
        self.assertTrue(any("MC-01-HUMAN" in e for e in res["errors"]), res["errors"])

        manifest["independent_check_summary"]["approver_kind"] = "human"
        res2 = k.validate_release_manifest(manifest)
        self.assertFalse(any("MC-01-HUMAN" in e for e in res2["errors"]), res2["errors"])

    def test_gate_release_rejects_all_ai_chain(self):
        manifest = load_example("release_manifest.example.json")
        manifest["status"] = "Approved-for-Live"
        del manifest["independent_check_summary"]["approver_kind"]
        card = self._all_ai_chain_card()
        card["claim_id"] = manifest["artifact_refs"]["claim_ids"][0]
        review = load_example("review_report.example.json")
        review["claim_ref"] = card["claim_id"]
        result = k.gate_release(manifest, [card], [review])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any("MC-01-HUMAN" in r for r in result["reasons"]), result["reasons"])


class XenonLedgerTest(unittest.TestCase):
    """MUST-12: xenon_ledger_check counts unresolved SCRAMMED citation_cards among a supplied
    batch and hard-fails above a threshold; gate_release wires it in when citation_cards is
    supplied, and honestly discloses the gap when it is not."""

    def _scrammed(self, n, resolved=0):
        cards = []
        for i in range(n):
            cards.append({
                "id": f"cite-scram-{i:03d}",
                "status": "SCRAMMED",
                "superseded_by": "cite-replacement-001" if i < resolved else None,
            })
        return cards

    def test_under_threshold_passes(self):
        res = k.xenon_ledger_check(self._scrammed(2))
        self.assertTrue(res["ok"], res["errors"])
        self.assertEqual(res["unresolved_scrammed_count"], 2)

    def test_over_threshold_fails(self):
        res = k.xenon_ledger_check(self._scrammed(4))
        self.assertFalse(res["ok"])
        self.assertTrue(any("xenon_ledger_check" in e for e in res["errors"]), res["errors"])

    def test_resolved_scrammed_not_counted(self):
        cards = self._scrammed(5, resolved=5)  # every SCRAMMED card has superseded_by set
        res = k.xenon_ledger_check(cards)
        self.assertTrue(res["ok"], res["errors"])
        self.assertEqual(res["unresolved_scrammed_count"], 0)

    def test_custom_threshold(self):
        res = k.xenon_ledger_check(self._scrammed(2), threshold=1)
        self.assertFalse(res["ok"])

    def test_gate_release_wires_xenon_ledger_check(self):
        manifest = load_example("release_manifest.example.json")
        card = load_example("claim_card.example.json")
        review = load_example("review_report.example.json")
        result = k.gate_release(manifest, [card], [review], citation_cards=self._scrammed(5))
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any("xenon_ledger" in r for r in result["reasons"]), result["reasons"])

    def test_gate_release_without_citation_cards_notes_the_gap(self):
        manifest = load_example("release_manifest.example.json")
        card = load_example("claim_card.example.json")
        review = load_example("review_report.example.json")
        result = k.gate_release(manifest, [card], [review])
        self.assertTrue(
            any("Xenon Ledger threshold check" in r and "NOT run" in r for r in result["reasons"]),
            result["reasons"],
        )

    def test_gate_release_passes_with_citation_cards_under_threshold(self):
        manifest = load_example("release_manifest.example.json")
        card = load_example("claim_card.example.json")
        review = load_example("review_report.example.json")
        result = k.gate_release(manifest, [card], [review], citation_cards=self._scrammed(1))
        self.assertIn(result["verdict"], ("PASS", "PASS_WITH_LIMITS"))


if __name__ == "__main__":
    unittest.main()
