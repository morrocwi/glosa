"""tests/test_defeater_status_warning.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers kernel rule31 (`lrs.defeater-defeated-status-field`, design/SESSION_ARCH_v0.4_SPEC.md
§10.2, build_now) and `glosa_kernel.defeater_status_for_card()`.

Deliberate design note (see kernel/glosa_kernel.py's own comment block above rule31): §10.2's
real gap was already closed by making `provenance_dag.defeater_log` required `[node, date,
outcome]` with an `outcome` enum -- and that same section explicitly names a NEW TOP-LEVEL status
field the "already-refuted idea" it deliberately did not add (one-fact-one-home). `defeater_status`
is therefore implemented here as a DERIVED value computed from `defeater_log`, never a second
schema field that could drift out of sync with it, surfaced only as a rule31 WARNING (never a
hard fail) once a card has advanced past Draft with no defeater ever attempted.
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


class DefeaterStatusForCardTest(unittest.TestCase):
    def test_empty_defeater_log_is_untested(self):
        self.assertEqual(k.defeater_status_for_card({"provenance_dag": {"defeater_log": []}}), "untested")

    def test_absent_provenance_dag_is_untested(self):
        self.assertEqual(k.defeater_status_for_card({}), "untested")

    def test_survived_entry_is_tested_survived(self):
        card = {"provenance_dag": {"defeater_log": [{"node": "n1", "date": "2026-09-05", "outcome": "claim_survived"}]}}
        self.assertEqual(k.defeater_status_for_card(card), "tested_survived")

    def test_revised_entry_is_tested_defeated(self):
        card = {"provenance_dag": {"defeater_log": [{"node": "n1", "date": "2026-09-05", "outcome": "claim_revised"}]}}
        self.assertEqual(k.defeater_status_for_card(card), "tested_defeated")

    def test_withdrawn_entry_is_tested_defeated(self):
        card = {"provenance_dag": {"defeater_log": [{"node": "n1", "date": "2026-09-05", "outcome": "claim_withdrawn"}]}}
        self.assertEqual(k.defeater_status_for_card(card), "tested_defeated")

    def test_mixed_survived_and_withdrawn_is_tested_defeated(self):
        card = {"provenance_dag": {"defeater_log": [
            {"node": "n1", "date": "2026-09-05", "outcome": "claim_survived"},
            {"node": "n2", "date": "2026-09-05", "outcome": "claim_withdrawn"},
        ]}}
        self.assertEqual(k.defeater_status_for_card(card), "tested_defeated")


class Rule31DefeaterStatusWarningTest(unittest.TestCase):
    def setUp(self):
        self.card = load_example("claim_card.example.json")  # status: Draft, defeater_log: []

    def test_draft_status_untested_no_warning(self):
        self.assertEqual(self.card.get("status"), "Draft")
        res = k.validate_claim_card(self.card, citation_cards=[load_example("citation_card.example.json")])
        self.assertFalse(any("rule31" in w for w in res["warnings"]), res["warnings"])

    def test_pending_review_untested_warns(self):
        card = copy.deepcopy(self.card)
        card["status"] = "Pending Review"
        res = k.validate_claim_card(card, citation_cards=[load_example("citation_card.example.json")])
        self.assertTrue(any("rule31" in w for w in res["warnings"]), res["warnings"])
        self.assertTrue(res["ok"], res["errors"])  # warning only, never a hard fail

    def test_approved_for_test_untested_warns(self):
        card = copy.deepcopy(self.card)
        card["status"] = "Approved-for-Test"
        res = k.validate_claim_card(card, citation_cards=[load_example("citation_card.example.json")])
        self.assertTrue(any("rule31" in w for w in res["warnings"]), res["warnings"])

    def test_pending_review_with_logged_defeater_no_warning(self):
        card = copy.deepcopy(self.card)
        card["status"] = "Pending Review"
        card["provenance_dag"]["defeater_log"] = [
            {"node": "n1", "date": "2026-09-05", "outcome": "claim_survived"}
        ]
        res = k.validate_claim_card(card, citation_cards=[load_example("citation_card.example.json")])
        self.assertFalse(any("rule31" in w for w in res["warnings"]), res["warnings"])


if __name__ == "__main__":
    unittest.main()
