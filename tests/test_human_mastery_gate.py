"""tests/test_human_mastery_gate.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers `hu.mastery-gate-wired` (HU-1, design/SESSION_ARCH_v0.4_SPEC.md §11.1, build_now):
`schema/human_mastery_gate.schema.json`, `kernel.glosa_kernel.validate_human_mastery_gate`,
`mastery_gate_r8_status` (R8's BLOCKED: NO_MASTERY_GATE_LINKED failing control from
methodology/P10_publish_gate.md), and `gate_release`'s R8 warning on a missing
`human_mastery_gate_ref` (pending founder ratification, never a hard fail per P17).
"""

import copy
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "kernel"))

import glosa_kernel as k  # noqa: E402

EXAMPLES_DIR = REPO_ROOT / "schema" / "examples"


def load_example(name):
    return json.loads((EXAMPLES_DIR / name).read_text(encoding="utf-8"))


class HumanMasteryGateSchemaTest(unittest.TestCase):
    def setUp(self):
        self.gate = load_example("human_mastery_gate.example.json")

    def test_shipped_example_passes(self):
        res = k.validate_human_mastery_gate(self.gate)
        self.assertTrue(res["ok"], res["errors"])

    def test_missing_answer_field_rejected(self):
        gate = copy.deepcopy(self.gate)
        del gate["answers"]["falsifying_record"]
        res = k.validate_human_mastery_gate(gate)
        self.assertFalse(res["ok"])

    def test_pass_with_named_gaps_requires_named_gaps(self):
        gate = copy.deepcopy(self.gate)
        gate["gate_status"] = "PASS_WITH_NAMED_GAPS"
        res = k.validate_human_mastery_gate(gate)
        self.assertFalse(res["ok"])  # named_gaps missing

        gate["named_gaps"] = ["strongest_counterexample"]
        res = k.validate_human_mastery_gate(gate)
        self.assertTrue(res["ok"], res["errors"])

    def test_ai_filled_disclosure_forces_not_ready(self):
        gate = copy.deepcopy(self.gate)
        gate["ai_filled"] = ["the_problem"]
        # gate_status is still PASS from the fixture -- must be rejected (P17 non-delegable rule)
        res = k.validate_human_mastery_gate(gate)
        self.assertFalse(res["ok"])

        gate["gate_status"] = "NOT_READY"
        res = k.validate_human_mastery_gate(gate)
        self.assertTrue(res["ok"], res["errors"])

    def test_not_ready_with_no_ai_filled_is_legal(self):
        gate = copy.deepcopy(self.gate)
        gate["gate_status"] = "NOT_READY"
        res = k.validate_human_mastery_gate(gate)
        self.assertTrue(res["ok"], res["errors"])


class MasteryGateR8StatusTest(unittest.TestCase):
    def test_no_gate_linked_blocked(self):
        status, reason = k.mastery_gate_r8_status(None)
        self.assertEqual(status, "BLOCKED")
        self.assertIn("NO_MASTERY_GATE_LINKED", reason)

    def test_pass_gate_passes_r8(self):
        gate = load_example("human_mastery_gate.example.json")
        status, reason = k.mastery_gate_r8_status(gate)
        self.assertEqual(status, "PASS")

    def test_pass_with_named_gaps_passes_r8(self):
        gate = copy.deepcopy(load_example("human_mastery_gate.example.json"))
        gate["gate_status"] = "PASS_WITH_NAMED_GAPS"
        gate["named_gaps"] = ["strongest_counterexample"]
        status, reason = k.mastery_gate_r8_status(gate)
        self.assertEqual(status, "PASS")

    def test_not_ready_gate_blocks_r8(self):
        gate = copy.deepcopy(load_example("human_mastery_gate.example.json"))
        gate["gate_status"] = "NOT_READY"
        status, reason = k.mastery_gate_r8_status(gate)
        self.assertEqual(status, "BLOCKED")


class GateReleaseMasteryGateWarningTest(unittest.TestCase):
    def setUp(self):
        self.manifest = load_example("release_manifest.example.json")
        self.card = load_example("claim_card.example.json")

    def test_missing_human_mastery_gate_ref_warns(self):
        manifest = copy.deepcopy(self.manifest)
        manifest.pop("human_mastery_gate_ref", None)
        result = k.gate_release(manifest, [self.card], [])
        self.assertTrue(any("NO_MASTERY_GATE_LINKED" in r for r in result["reasons"]), result["reasons"])

    def test_missing_human_mastery_gate_ref_is_not_a_hard_fail(self):
        manifest = copy.deepcopy(self.manifest)
        manifest.pop("human_mastery_gate_ref", None)
        manifest["status"] = "Draft"
        manifest["gate_verdict"] = "PASS_WITH_LIMITS"
        result = k.gate_release(manifest, [self.card], [])
        # the warning fires but never sets hard_fail on its own
        self.assertTrue(any("NO_MASTERY_GATE_LINKED" in r for r in result["reasons"]))

    def test_present_human_mastery_gate_ref_no_warning(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["human_mastery_gate_ref"] = "hmg-cat-litterbox-001"
        result = k.gate_release(manifest, [self.card], [])
        self.assertFalse(any("NO_MASTERY_GATE_LINKED" in r for r in result["reasons"]), result["reasons"])


if __name__ == "__main__":
    unittest.main()
