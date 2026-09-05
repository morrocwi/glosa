"""tests/test_blackbox_question_trace.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers `schema.blackbox-question-trace` (design/SESSION_ARCH_v0.4_SPEC.md §9.1/§9.4, build_now):
the additive `question_trace[]` field on `schema/blackbox_note.schema.json`, and
`tools/blackbox_log.py`'s `question_trace_coverage()` mechanical coverage-check extension --
every `lines[].kind == "question"` line must have a matching `question_trace[].n` entry (or an
explicit `derived_from_line: null` marking a genuinely fresh question), per the
`question_trace_gap` fixture sketch in design/SESSION_ARCH_v0.4_SPEC.md §12.
"""

import copy
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "kernel"))

import blackbox_log as bbl  # noqa: E402
import glosa_kernel as k  # noqa: E402

EXAMPLES_DIR = REPO_ROOT / "schema" / "examples"


def load_example(name):
    return json.loads((EXAMPLES_DIR / name).read_text(encoding="utf-8"))


class BlackboxQuestionTraceSchemaTest(unittest.TestCase):
    """schema/blackbox_note.schema.json accepts the new optional top-level question_trace[]."""

    def test_shipped_example_still_validates(self):
        note = load_example("blackbox_note.example.json")
        res = k.validate_blackbox_note(note)
        self.assertTrue(res["ok"], res["errors"])

    def test_question_trace_field_validates(self):
        note = copy.deepcopy(load_example("blackbox_note.example.json"))
        note["question_trace"] = [
            {"n": 1, "ts": "2026-09-04T07:20:08Z", "question_text": "ทำไมแมวเยี่ยวไม่เป็นที่", "derived_from_line": None, "note": ""}
        ]
        res = k.validate_blackbox_note(note)
        self.assertTrue(res["ok"], res["errors"])

    def test_question_trace_entry_missing_required_field_rejected(self):
        note = copy.deepcopy(load_example("blackbox_note.example.json"))
        note["question_trace"] = [{"n": 1, "ts": "2026-09-04T07:20:08Z"}]  # missing question_text/derived_from_line
        res = k.validate_blackbox_note(note)
        self.assertFalse(res["ok"])


class QuestionTraceCoverageTest(unittest.TestCase):
    """tools/blackbox_log.py question_trace_coverage() -- the coverage-check extension."""

    def _note(self, question_ns, trace_entries=None):
        return {
            "id": "BB-2026-09-05-01",
            "project": "p",
            "participants": [{"role": "founder"}],
            "language": "en",
            "privacy_scan": "done",
            "lines": [
                {
                    "n": n, "ts": "2026-09-05T00:00:00Z", "speaker": "founder", "kind": "question",
                    "text_verbatim": f"q{n}", "public": False, "ai_proposed": False,
                }
                for n in question_ns
            ],
            "cooking": [],
            "question_trace": trace_entries or [],
        }

    def test_two_question_lines_zero_trace_entries_reports_both_gaps(self):
        note = self._note([1, 5])
        res = bbl.question_trace_coverage(note)
        self.assertFalse(res["ok"])
        self.assertEqual(len(res["errors"]), 2)
        self.assertTrue(any("n=1" in e for e in res["errors"]))
        self.assertTrue(any("n=5" in e for e in res["errors"]))

    def test_two_question_lines_fully_covered_passes(self):
        note = self._note(
            [1, 5],
            trace_entries=[
                {"n": 1, "ts": "t", "question_text": "q1", "derived_from_line": None, "note": ""},
                {"n": 5, "ts": "t", "question_text": "q5 reformed", "derived_from_line": 1, "note": ""},
            ],
        )
        res = bbl.question_trace_coverage(note)
        self.assertTrue(res["ok"], res["errors"])

    def test_partial_coverage_reports_only_the_uncovered_line(self):
        note = self._note(
            [1, 5],
            trace_entries=[{"n": 1, "ts": "t", "question_text": "q1", "derived_from_line": None, "note": ""}],
        )
        res = bbl.question_trace_coverage(note)
        self.assertFalse(res["ok"])
        self.assertEqual(len(res["errors"]), 1)
        self.assertIn("n=5", res["errors"][0])

    def test_non_question_lines_never_required_to_be_covered(self):
        note = self._note([])
        note["lines"].append({
            "n": 1, "ts": "t", "speaker": "founder", "kind": "proposal", "text_verbatim": "x",
            "public": False, "ai_proposed": False,
        })
        res = bbl.question_trace_coverage(note)
        self.assertTrue(res["ok"], res["errors"])

    def test_check_note_cli_helper(self):
        import tempfile
        note = self._note(
            [1],
            trace_entries=[{"n": 1, "ts": "t", "question_text": "q1", "derived_from_line": None, "note": ""}],
        )
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(note, f)
            path = f.name
        self.assertTrue(bbl.check_note(path))


if __name__ == "__main__":
    unittest.main()
