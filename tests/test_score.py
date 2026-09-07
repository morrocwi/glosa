"""tests/test_score.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers the Resistance Ladder (P23): `cli/glosa score <artifact>` end-to-end (subprocess, isolated
tmp directory with synthetic `cases/repro/*.json` cards, `reviews/routes/**/review_report.*`
files, and a fake Toledo `registry/CANONICAL.json` -- never against this repo's own real
`cases/repro/` or the real Toledo checkout). Asserts the per-rung `{held, evidence, reason}` shape
(design principle: never a single number) and that a disclosed `FAIL` still holds R3/R4/R6.
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = REPO_ROOT / "cli" / "glosa"


def run_cli(args, cwd):
    proc = subprocess.run(
        [sys.executable, str(CLI_PATH)] + args, cwd=str(cwd), capture_output=True, text=True,
    )
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        payload = {"_raw_stdout": proc.stdout, "_raw_stderr": proc.stderr}
    return proc.returncode, payload


def base_card(**overrides):
    card = {
        "$schema": "reproduction_card.schema.json",
        "id": "REPRO-SCORE-0001",
        "toledo_codes": ["EQ-999/H.01.v1"],
        "claim": "score-test-claim",
        "preregistered_prediction": {
            "statement": "observed equals 12",
            "tolerance": "exact integer match, 0 discrepancy",
            "declared_at": "2026-09-08T09:00:00+00:00",
        },
        "oracle": {
            "kind": "independent_implementation",
            "source": "stdlib arithmetic",
            "doi_or_url": "n/a",
            "version": "1.0",
        },
        "environment": {"python": "3.11.0", "packages": {}},
        "run": {
            "command": 'python3 -c "print(12)"',
            "input_hash": None,
            "output_hash": None,
            "ai_at_runtime": 0,
            "date": "2026-09-08T09:05:00+00:00",
        },
        "result": {"status": "PASS", "observed": "12", "deviation": 0},
        "lineage": {
            "run_by": "tester",
            "ces": {"respondent": "tester", "interactional": "None", "ai_models": "None"},
        },
        "notes": "",
    }
    card.update(overrides)
    return card


class TestScoreRungs(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.cwd = Path(self._tmp.name)
        (self.cwd / "cards").mkdir()
        (self.cwd / "reviews_dir").mkdir()

    def _write_card(self, name, card):
        (self.cwd / "cards" / name).write_text(json.dumps(card), encoding="utf-8")

    def _score(self, artifact, **extra_flags):
        args = ["score", artifact, "--repro-dir", "cards", "--reviews-dir", "reviews_dir"]
        for flag, value in extra_flags.items():
            args += [flag, value]
        return run_cli(args, self.cwd)

    def test_r0_false_for_a_code_absent_from_every_registry(self):
        """Bug found live, 2026-09-08: R0 used to hold `True` unconditionally for ANY string
        (`glosa score NONEXISTENT-CODE-999` reported R0 held:true with 'evidence' merely echoing
        the CLI's own input argument back -- no file was ever checked). Fixed: R0 requires a real
        registry entry with a non-empty statement, exactly like every other rung."""
        code, payload = self._score("NONEXISTENT-CODE-999", **{"--toledo-registry": str(self.cwd / "does-not-exist.json")})
        self.assertEqual(code, 0)
        self.assertFalse(payload["rungs"]["R0"]["held"], payload["rungs"]["R0"])
        self.assertIn("reason", payload["rungs"]["R0"])

    def test_r0_held_when_registry_entry_has_a_statement(self):
        registry_dir = self.cwd / "toledo_registry_r0"
        registry_dir.mkdir()
        registry_path = registry_dir / "CANONICAL.json"
        registry_path.write_text(json.dumps([
            {"code": "EQ-999/H.01.v1", "statement": {"latest": "a real statement"}, "coq": {"coq_status": "closed"}},
        ]), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R0"]["held"], payload["rungs"]["R0"])
        self.assertEqual(payload["rungs"]["R0"]["evidence"][0]["code"], "EQ-999/H.01.v1")

    def test_r0_false_when_registry_entry_has_no_statement(self):
        registry_dir = self.cwd / "toledo_registry_r0_empty"
        registry_dir.mkdir()
        registry_path = registry_dir / "CANONICAL.json"
        registry_path.write_text(json.dumps([
            {"code": "EQ-999/H.01.v1", "coq": {"coq_status": "closed"}},
        ]), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0, payload)
        self.assertFalse(payload["rungs"]["R0"]["held"], payload["rungs"]["R0"])
        self.assertIn("statement field is empty", payload["rungs"]["R0"]["reason"])

    def test_r0_r2_resolve_a_layer0_root_code_from_genesis_root_json(self):
        """Integration fix, 2026-09-08: Layer-0 root codes (e.g. `EQ-068`) live only in Toledo's
        `registry/genesis_root.json`, never in `CANONICAL.json` -- both must be checked."""
        registry_dir = self.cwd / "toledo_registry_root"
        registry_dir.mkdir()
        canonical_path = registry_dir / "CANONICAL.json"
        canonical_path.write_text(json.dumps({"canonical": []}), encoding="utf-8")
        genesis_path = registry_dir / "genesis_root.json"
        genesis_path.write_text(json.dumps({"root_equations": [
            {"code": "EQ-068", "statement": "a root statement"},
        ]}), encoding="utf-8")
        code, payload = self._score(
            "EQ-068", **{"--toledo-registry": str(canonical_path), "--toledo-genesis-root": str(genesis_path)}
        )
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R0"]["held"], payload["rungs"]["R0"])
        self.assertEqual(payload["rungs"]["R0"]["evidence"][0]["path"], str(genesis_path))
        # coq_status is absent on the root row -> R2 correctly reads not-held, but via a real
        # lookup that actually found the code (never "not found").
        self.assertFalse(payload["rungs"]["R2"]["held"])
        self.assertNotIn("not found", payload["rungs"]["R2"]["reason"])

    def test_no_scalar_score_flag_exists(self):
        """P23's own design principle: the command is built to refuse collapsing the table --
        there is no --score flag at all (argparse rejects it, exit code 2)."""
        proc = subprocess.run(
            [sys.executable, str(CLI_PATH), "score", "EQ-999/H.01.v1", "--score", "7"],
            cwd=str(self.cwd), capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 2)

    def test_r1_r3_r4_r6_held_with_matching_passing_card(self):
        self._write_card("c1.json", base_card())
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0, payload)
        rungs = payload["rungs"]
        self.assertTrue(rungs["R1"]["held"], rungs["R1"])
        self.assertTrue(rungs["R3"]["held"], rungs["R3"])
        self.assertTrue(rungs["R4"]["held"], rungs["R4"])
        self.assertTrue(rungs["R6"]["held"], rungs["R6"])

    def test_r3_r4_still_held_on_disclosed_fail(self):
        """P0/P23 §0: a disclosed FAIL is exactly as strong evidence of R3/R4 as a PASS -- never
        hidden, never downgraded to 'not held'."""
        card = base_card(result={"status": "FAIL", "observed": "13", "deviation": 1})
        self._write_card("c1.json", card)
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0)
        rungs = payload["rungs"]
        self.assertTrue(rungs["R3"]["held"])
        self.assertTrue(rungs["R4"]["held"], "R4 must hold on a disclosed FAIL too")
        self.assertEqual(rungs["R4"]["evidence"][0]["result_status"], "FAIL")

    def test_r4_not_held_on_pending_or_error(self):
        for status in ("PENDING", "ERROR"):
            with self.subTest(status=status):
                card = base_card(
                    run=None if status == "PENDING" else base_card()["run"],
                    result={"status": status, "observed": None, "deviation": None},
                )
                self._write_card("c1.json", card)
                code, payload = self._score("EQ-999/H.01.v1")
                self.assertEqual(code, 0)
                self.assertFalse(payload["rungs"]["R4"]["held"], status)

    def test_r6_not_held_for_coq_kernel_oracle(self):
        card = base_card(oracle={"kind": "coq_kernel", "source": "Coq kernel", "doi_or_url": None, "version": None})
        self._write_card("c1.json", card)
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0)
        rungs = payload["rungs"]
        self.assertFalse(rungs["R4"]["held"], "coq_kernel is not an external oracle -- R4 must not hold")
        self.assertFalse(rungs["R6"]["held"])
        self.assertIn("R4 not held", rungs["R6"]["reason"])

    def test_r6_not_held_when_tolerance_is_vacuous(self):
        card = base_card()
        card["preregistered_prediction"]["tolerance"] = "any value always passes, no tolerance"
        self._write_card("c1.json", card)
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0)
        rungs = payload["rungs"]
        self.assertTrue(rungs["R4"]["held"], "R4 does not depend on the tolerance's own non-vacuity")
        self.assertFalse(rungs["R6"]["held"], "R6 must refuse a vacuous, always-pass tolerance")

    def test_no_matching_card_leaves_every_rung_but_r0_unheld(self):
        registry_dir = self.cwd / "toledo_registry"
        registry_dir.mkdir()
        registry_path = registry_dir / "CANONICAL.json"
        registry_path.write_text(json.dumps([
            {"code": "EQ-999/H.01.v1", "statement": {"latest": "a real statement"}},
        ]), encoding="utf-8")
        self._write_card("unrelated.json", base_card(toledo_codes=["EQ-000/H.01.v1"], claim="unrelated-claim"))
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0)
        rungs = payload["rungs"]
        self.assertTrue(rungs["R0"]["held"])
        for rung in ("R1", "R3", "R4", "R5", "R6"):
            self.assertFalse(rungs[rung]["held"], rung)
            self.assertIn("reason", rungs[rung])

    def test_r3_r4_r6_not_held_when_a_linked_repro_verify_review_records_a_hash_mismatch(self):
        """Review journal wf_3208069c-1c1, "R3/R4/R6 ignore verify mismatch": a card whose latest
        `glosa repro verify` outcome (its own repro-verify review_report) disclosed a hash
        MISMATCH must not count toward R3 (and therefore not R4/R6), even though the maker's own
        `run{}` looks complete -- this is the EQ-068 false-positive the review journal names."""
        card = base_card()
        self._write_card("c1.json", card)
        review_dir = self.cwd / "reviews_dir" / "repro-verify-REPRO-SCORE-0001"
        review_dir.mkdir(parents=True)
        review = {
            "$schema": "review_report.schema.json",
            "claim_ref": "score-test-claim",
            "route_id": f"repro-verify-{card['id']}",
            "reviewer_identity": "checker1",
            "independence_class": "I1",
            "role": "SourceAuditor",
            "verdict": "hash match on re-execution: input_hash MATCH ('a' vs 'a'), "
                       "output_hash MISMATCH ('b' vs 'c').",
            "verdict_tier": "Dr",
            "date": "2026-09-08",
        }
        (review_dir / "review_report.json").write_text(json.dumps(review), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0, payload)
        rungs = payload["rungs"]
        self.assertFalse(rungs["R3"]["held"], rungs["R3"])
        self.assertIn("MISMATCH", rungs["R3"]["reason"])
        self.assertFalse(rungs["R4"]["held"], "R4 must not hold once its own R3-holding card is withdrawn")
        self.assertFalse(rungs["R6"]["held"], "R6 must not hold once R4 is withdrawn")

    def test_r3_still_held_when_the_linked_verify_review_matches(self):
        """Companion to the mismatch regression above: a MATCHING repro-verify review must not
        accidentally withdraw R3 -- only a disclosed MISMATCH does."""
        card = base_card()
        self._write_card("c1.json", card)
        review_dir = self.cwd / "reviews_dir" / "repro-verify-REPRO-SCORE-0001"
        review_dir.mkdir(parents=True)
        review = {
            "$schema": "review_report.schema.json",
            "claim_ref": "score-test-claim",
            "route_id": f"repro-verify-{card['id']}",
            "reviewer_identity": "checker1",
            "independence_class": "I1",
            "role": "SourceAuditor",
            "verdict": "hash match on re-execution: input_hash MATCH ('a' vs 'a'), "
                       "output_hash MATCH ('b' vs 'b').",
            "verdict_tier": "finite_diagnostic",
            "date": "2026-09-08",
        }
        (review_dir / "review_report.json").write_text(json.dumps(review), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0, payload)
        rungs = payload["rungs"]
        self.assertTrue(rungs["R3"]["held"], rungs["R3"])
        self.assertTrue(rungs["R4"]["held"], rungs["R4"])
        self.assertTrue(rungs["R6"]["held"], rungs["R6"])

    def test_r5_not_fabricated_by_a_default_independence_class_repro_verify_review(self):
        """Review journal wf_3208069c-1c1, "R5 fabricated via repro verify default": a
        repro-verify review_report scaffolded with the tool's own (pre-fix) default
        independence_class must not, by itself, hold R5 -- R5 requires I2+, and a mechanical
        re-execution under a different identity STRING alone (I1, the fixed default) is not
        that. This exercises `glosa score`'s own R5 rung directly against such a review."""
        self._write_card("c1.json", base_card())
        review_dir = self.cwd / "reviews_dir" / "repro-verify-REPRO-SCORE-0001"
        review_dir.mkdir(parents=True)
        review = {
            "$schema": "review_report.schema.json",
            "claim_ref": "score-test-claim",
            "route_id": "repro-verify-REPRO-SCORE-0001",
            "reviewer_identity": "checker1",
            "independence_class": "I1",
            "role": "SourceAuditor",
            "verdict": "hash match on re-execution: input_hash MATCH, output_hash MATCH.",
            "verdict_tier": "finite_diagnostic",
            "date": "2026-09-08",
        }
        (review_dir / "review_report.json").write_text(json.dumps(review), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0, payload)
        self.assertFalse(payload["rungs"]["R5"]["held"], payload["rungs"]["R5"])

    def test_r5_held_with_independent_review(self):
        self._write_card("c1.json", base_card())
        review_dir = self.cwd / "reviews_dir" / "route1"
        review_dir.mkdir(parents=True)
        review = {
            "$schema": "review_report.schema.json",
            "claim_ref": "score-test-claim",
            "route_id": "R1",
            "reviewer_identity": "checker1",
            "independence_class": "I3",
            "role": "SourceAuditor",
            "verdict": "hashes match",
            "verdict_tier": "finite_diagnostic",
            "date": "2026-09-08",
        }
        (review_dir / "review_report.json").write_text(json.dumps(review), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R5"]["held"], payload["rungs"]["R5"])

    def test_r5_not_held_below_i2(self):
        self._write_card("c1.json", base_card())
        review_dir = self.cwd / "reviews_dir" / "route1"
        review_dir.mkdir(parents=True)
        review = {
            "$schema": "review_report.schema.json",
            "claim_ref": "score-test-claim",
            "route_id": "R1",
            "reviewer_identity": "checker1",
            "independence_class": "I1",
            "role": "SourceAuditor",
            "verdict": "self-check only",
            "verdict_tier": "Dr",
            "date": "2026-09-08",
        }
        (review_dir / "review_report.json").write_text(json.dumps(review), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1")
        self.assertEqual(code, 0)
        self.assertFalse(payload["rungs"]["R5"]["held"])

    def test_r2_via_fake_toledo_registry(self):
        registry_dir = self.cwd / "toledo_registry"
        registry_dir.mkdir()
        registry_path = registry_dir / "CANONICAL.json"
        registry_path.write_text(json.dumps([
            {"code": "EQ-999/H.01.v1", "coq": {"coq_status": "closed"}},
            {"code": "EQ-999/H.02.v1", "coq": {"coq_status": "wrapped_related"}},
        ]), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R2"]["held"], payload["rungs"]["R2"])

        code, payload = self._score("EQ-999/H.02.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0)
        self.assertFalse(payload["rungs"]["R2"]["held"])
        self.assertIn("wrapped_related", payload["rungs"]["R2"]["reason"])

    def test_r2_via_real_toledo_registry_shape(self):
        """The real toledo/registry/CANONICAL.json (registry/SCHEMA.md) is NOT a bare list at the
        top level -- it is {"schema_version", "generated_from_commit", "canonical": [...],
        "raw_to_canonical": {...}, "counts": {...}}. A registry fixture shaped like the actual
        schema must resolve R2 exactly like the bare-list fixture above (integration regression:
        a previous `data.get("entries") or list(data.values())` fallback silently iterated the
        top-level dict's OWN values instead of the nested "canonical" list, so R2 could never be
        held true against a real registry file no matter what code was asked for)."""
        registry_dir = self.cwd / "toledo_registry_real_shape"
        registry_dir.mkdir()
        registry_path = registry_dir / "CANONICAL.json"
        registry_path.write_text(json.dumps({
            "schema_version": "1.0.0",
            "generated_from_commit": "deadbeef",
            "canonical": [
                {"code": "EQ-999/H.01.v1", "coq": {"coq_status": "closed"}},
                {"code": "EQ-999/H.02.v1", "coq": {"coq_status": "wrapped_related"}},
            ],
            "raw_to_canonical": {},
            "counts": {"current": 2},
        }), encoding="utf-8")
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R2"]["held"], payload["rungs"]["R2"])

        code, payload = self._score("EQ-999/H.02.v1", **{"--toledo-registry": str(registry_path)})
        self.assertEqual(code, 0)
        self.assertFalse(payload["rungs"]["R2"]["held"])
        self.assertIn("wrapped_related", payload["rungs"]["R2"]["reason"])

    def test_r2_reports_missing_registry_honestly(self):
        code, payload = self._score("EQ-999/H.01.v1", **{"--toledo-registry": str(self.cwd / "does-not-exist.json")})
        self.assertEqual(code, 0)
        self.assertFalse(payload["rungs"]["R2"]["held"])
        self.assertIn("not found", payload["rungs"]["R2"]["reason"])

    def test_claim_card_kind_r1_via_falsifier(self):
        claim_card = {
            "$schema": "claim_card.schema.json",
            "claim_id": "CC-SCORE-1",
            "shape": "stub",
            "statement": {"language": "en", "text": "x", "is_verbatim_quote": False},
            "standpoint": {"declared_basis": "b", "disciplines_not_claimed": [], "method_basis": ""},
            "claim_type": "EMPIRICAL",
            "produced_by": "human",
            "responsible": "human",
            "origin_blackbox_ref": None,
            "five_questions": {
                "tested": {"evidence_relations": [], "falsifier": "a controlled trial finding no effect would defeat this claim", "dissent_records": []},
                "ai_filled": {"used": False, "note": ""},
            },
            "non_claims": ["not a claim about anything else"],
            "human_owner": "tester",
            "tier": "Dr",
            "status": "Draft",
        }
        (self.cwd / "claim.json").write_text(json.dumps(claim_card), encoding="utf-8")
        code, payload = self._score("claim.json", **{"--kind": "claim_card"})
        self.assertEqual(code, 0, payload)
        self.assertTrue(payload["rungs"]["R1"]["held"], payload["rungs"]["R1"])
        self.assertEqual(payload["rungs"]["R1"]["evidence"][0]["type"], "claim_card")


if __name__ == "__main__":
    unittest.main()
