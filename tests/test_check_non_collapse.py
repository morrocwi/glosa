"""tests/test_check_non_collapse.py

tier: finite_diagnostic (tests executed via `python3 -m pytest -q tests`, run from the glosa
repo root).

Covers `scripts/check_non_collapse.py` (R4 resolution, `design/
ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md` §3d/§8): a WARN-only, never-auto-fails checker for
ownership/subtraction phrasing ("[node] is [strand]'s concept" style collapses). Cases: a real
EN hit, a clean line, a Thai hit, a non-collapse:meta section skip, and the --strict exit-code
opt-in.
"""

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import check_non_collapse as ncc  # noqa: E402


class TestHit(unittest.TestCase):
    def test_reduces_to_is_flagged(self):
        text = "The node N2 reduces to classical PID theory."
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        path, lineno, label, excerpt = hits[0]
        self.assertEqual(lineno, 1)
        self.assertEqual(label, "reduces to")
        self.assertIn("reduces to", excerpt)

    def test_arrow_theory_ownership_is_flagged(self):
        text = "Wrong phrasing: N2 <- theory of adaptive control."
        hits = list(ncc.scan_text("t.md", text))
        self.assertTrue(any(h[2] == "<- theory (arrow ownership)" for h in hits))

    def test_borrowed_from_is_flagged(self):
        text = "This mechanism is borrowed from control theory."
        hits = list(ncc.scan_text("t.md", text))
        self.assertTrue(any(h[2] == "borrowed from" for h in hits))


class TestCleanLine(unittest.TestCase):
    def test_ally_phrasing_is_not_flagged(self):
        text = (
            "CSC gives detailed representation/control mechanisms inside semantic cognition; "
            "the work's architecture places semantic transformation on a chain from readout "
            "through agency to a later stage CSC does not itself specify."
        )
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(hits, [])

    def test_relation_vocabulary_is_not_flagged(self):
        text = "X SUPPORTS node N; X CHALLENGES a boundary condition; X EXTENDS the mechanism."
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(hits, [])


class TestNewPatterns(unittest.TestCase):
    """Patterns added to close C2 (2026-09-23 cross-vendor review): phrases the proposal's own
    docstring/§6 table said this checker flags, that the original pattern list did not actually
    contain."""

    def test_is_strands_concept_is_flagged(self):
        text = "N2 is PID theory's concept."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("is ...'s concept", labels)

    def test_comes_from_is_flagged(self):
        text = "The work's meaning-node comes from Derrida."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("comes from", labels)

    def test_no_novelty_is_flagged(self):  # forbidden-phrase-family case
        text = "There is no novelty here at all."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("no novelty", labels)

    def test_already_has_and_isnt_new_are_flagged(self):
        text = "Since Capability Approach already has 'capability', this node isn't new."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("already has 'X' (quoted-term ownership)", labels)
        self.assertIn("isn't new / is not new", labels)

    def test_already_has_without_a_quoted_term_is_not_flagged(self):
        # Legitimate prose ("a mechanism the architecture already has") must not be flagged —
        # only the ownership-move shape "already has '<quoted term>'" is a candidate.
        text = "a mechanism the architecture already has. The founder asked that this be general."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertNotIn("already has 'X' (quoted-term ownership)", labels)

    def test_must_shift_the_claim_is_flagged(self):
        text = "X already covers this, so we must shift the claim elsewhere."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("must shift the claim", labels)


class TestArrowAndIsAPatterns(unittest.TestCase):
    """Patterns added to close C4/finding-9 (2026-09-23 cross-vendor review, PR #9): the original
    arrow pattern required the literal word 'theory' immediately after the arrow, so it missed
    'N2 <- PID theory.' (a named strand between the arrow and 'theory'); and no pattern at all
    caught the 'N2 is a PID controller.' ownership shape."""

    def test_arrow_named_strand_then_theory_is_flagged(self):
        text = "N2 <- PID theory."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("<- named strand (arrow ownership)", labels)

    def test_arrow_named_strand_unicode_then_theory_is_flagged(self):
        text = "N2 ← PID theory."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("<- named strand (arrow ownership)", labels)

    def test_arrow_named_strand_then_controller_is_flagged(self):
        text = "N2 <- PID controller."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("<- named strand (arrow ownership)", labels)

    def test_is_a_named_controller_is_flagged(self):
        text = "N2 is a PID controller."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("is a <name> controller/model/theory (ownership)", labels)

    def test_is_a_named_model_is_flagged(self):
        text = "The node is a Bayesian model."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("is a <name> controller/model/theory (ownership)", labels)

    def test_is_a_named_theory_is_flagged(self):
        text = "N2 is a classical control theory."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("is a <name> controller/model/theory (ownership)", labels)

    def test_unrelated_is_a_sentence_is_not_flagged_by_new_patterns(self):
        # ally phrasing ("X is a mature, well-studied instance of Y") must not trip the new
        # ownership pattern just because the word "instance" is nearby -- no controller/model/
        # theory keyword falls inside the sentence's own scoping window here.
        text = "A proportional-integral-derivative controller is a mature, well-studied instance of exactly this update-rule pattern."
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertNotIn("is a <name> controller/model/theory (ownership)", labels)
        self.assertNotIn("<- named strand (arrow ownership)", labels)


class TestFencedCodeBlocks(unittest.TestCase):
    """C1 (2026-09-23 cross-vendor review): a `#` line inside a fenced code block must never be
    treated as a heading, so it can never open or close a meta-skip region — only a real
    (non-fenced) heading carrying the marker may do that. Content inside a fence is still
    scanned for phrases like any other line."""

    def test_meta_marker_heading_inside_fence_does_not_open_a_skip_region(self):
        text = "\n".join([
            "## Real section",
            "Showing the marker syntax as an example, inside a fence:",
            "```",
            "## Example heading <!-- non-collapse:meta -->",
            "```",
            "this node reduces to a prior theory (must still be flagged)",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 6)
        self.assertEqual(hits[0][2], "reduces to")

    def test_phrase_inside_a_plain_fence_is_still_scanned(self):
        text = "\n".join([
            "```",
            "this node reduces to a prior theory",
            "```",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 2)

    def test_real_meta_heading_outside_fence_still_skips_normally(self):
        text = "\n".join([
            "## Forbidden phrases <!-- non-collapse:meta -->",
            "example: this node reduces to a prior theory",
            "## Next section",
            "this node reduces to a prior theory",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 4)

    def test_tilde_fence_also_suppresses_heading_detection(self):
        text = "\n".join([
            "~~~",
            "## fake heading <!-- non-collapse:meta -->",
            "~~~",
            "this node reduces to a prior theory (must still be flagged)",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 4)


class TestThaiHit(unittest.TestCase):
    def test_mai_mai_is_flagged(self):
        text = "แนวคิดนี้ไม่ใหม่เพราะมีคนทำไปแล้ว"
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("ไม่ใหม่", labels)
        self.assertIn("ทำไปแล้ว", labels)

    def test_pen_kae_is_flagged(self):
        text = "โหนดนี้เป็นแค่การลดรูปเป็นทฤษฎีเดิม"
        hits = list(ncc.scan_text("t.md", text))
        labels = {h[2] for h in hits}
        self.assertIn("เป็นแค่", labels)
        self.assertIn("ลดรูปเป็น", labels)


class TestMetaSectionSkip(unittest.TestCase):
    def test_meta_heading_section_is_skipped_until_same_or_shallower_heading(self):
        text = "\n".join([
            "# Title",
            "",
            "## Forbidden phrases <!-- non-collapse:meta -->",
            "",
            'Example of a bad phrase: "N2 reduces to PID theory."',
            'Another: "this is just borrowed from control theory."',
            "",
            "## Next real section",
            "",
            "This node reduces to the prior framework.",
        ])
        hits = list(ncc.scan_text("t.md", text))
        # Only the hit in the real (non-meta) section after the boundary heading should fire.
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 10)  # line number of the real-section sentence
        self.assertEqual(hits[0][2], "reduces to")

    def test_meta_section_closes_on_equal_level_heading_not_deeper_one(self):
        text = "\n".join([
            "## Meta <!-- non-collapse:meta -->",
            "still skipped: reduces to X",
            "### A deeper heading does not close the meta section",
            "still skipped: reduces to X",
            "## Sibling heading closes it",
            "not skipped: reduces to X",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][1], 6)

    def test_meta_marker_without_heading_prefix_is_not_a_boundary(self):
        text = "\n".join([
            "This line mentions <!-- non-collapse:meta --> but is not a heading.",
            "so this still gets scanned: reduces to X",
        ])
        hits = list(ncc.scan_text("t.md", text))
        self.assertEqual(len(hits), 1)


class TestStrictExitCode(unittest.TestCase):
    def _write(self, tmp_path: Path, text: str) -> Path:
        p = tmp_path / "sample.md"
        p.write_text(text, encoding="utf-8")
        return p

    def test_exit_0_without_strict_even_with_hits(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = self._write(Path(d), "this node reduces to a prior theory")
            rc = ncc.main([str(p)])
            self.assertEqual(rc, 0)

    def test_exit_1_with_strict_and_hits(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = self._write(Path(d), "this node reduces to a prior theory")
            rc = ncc.main([str(p), "--strict"])
            self.assertEqual(rc, 1)

    def test_exit_0_with_strict_and_no_hits(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = self._write(Path(d), "this is a clean ally-phrasing sentence")
            rc = ncc.main([str(p), "--strict"])
            self.assertEqual(rc, 0)

    def test_no_paths_returns_2(self):
        rc = ncc.main([])
        self.assertEqual(rc, 2)


class TestStrictIOErrors(unittest.TestCase):
    """C3 (2026-09-23 cross-vendor review): a missing or non-UTF-8 path under --strict must be a
    hard usage/IO error (exit 2), not silently absorbed into a clean exit 0. Without --strict, the
    same input stays warn-and-continue (exit 0), unchanged from before."""

    def test_missing_path_without_strict_still_exits_0(self):
        rc = ncc.main(["/nonexistent/path/does-not-exist.md"])
        self.assertEqual(rc, 0)

    def test_missing_path_with_strict_exits_2(self):
        rc = ncc.main(["/nonexistent/path/does-not-exist.md", "--strict"])
        self.assertEqual(rc, 2)

    def test_non_utf8_path_with_strict_exits_2(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.md"
            p.write_bytes(b"\xff\xfe not valid utf-8")
            rc = ncc.main([str(p), "--strict"])
            self.assertEqual(rc, 2)

    def test_non_utf8_path_without_strict_exits_0(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.md"
            p.write_bytes(b"\xff\xfe not valid utf-8")
            rc = ncc.main([str(p)])
            self.assertEqual(rc, 0)

    def test_check_paths_reports_errors_separately_from_hits(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            good = Path(d) / "good.md"
            good.write_text("this node reduces to a prior theory", encoding="utf-8")
            missing = str(Path(d) / "missing.md")
            hits, errors = ncc.check_paths([str(good), missing])
            self.assertEqual(len(hits), 1)
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], missing)


if __name__ == "__main__":
    unittest.main()
