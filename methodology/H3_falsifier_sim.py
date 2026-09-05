#!/usr/bin/env python3
"""H3 falsifier simulation (design/DAG_v0.3.yaml / DECISIONS.md 2026-09-05, "H3 falsifier sim
approved to build and run", founder-delegated BBL-122).

H3 (as stated): cross-vendor (I3) checking of claim cards catches undisclosed AI-fill /
undisclosed assumptions at a higher rate than same-vendor re-checking.

This script is a PROXY, not a real I3 run -- disclosed plainly, not once but everywhere a number
appears below. No second vendor is invoked anywhere in this repo; both "routes" are deterministic
Python run in this one process, on this one machine, by this one worker. What the proxy actually
compares:

  route A ("same-vendor" proxy) -- the maker's OWN field-completeness check: for each card, is
    every disclosure-relevant field present and non-empty? This is exactly the kind of check a
    maker re-running its own rule set on its own output would perform -- "did I fill in the
    form" -- and it never reads across fields or across the claim/citation boundary.

  route B ("cross-route" proxy) -- the kernel's three INDEPENDENT structural rules that this repo
    already ships, called directly (not through the full validator, so nothing outside these three
    rules can contribute to route B's count):
      - rule27 (_hidden_ai_fill_error, kernel/glosa_kernel.py) -- five_questions.seen.
        ai_assisted_fields vs five_questions.ai_filled cross-check.
      - rule28 (_inflated_bearing_errors, kernel/glosa_kernel.py) -- evidence_relations bearing
        vs the resolved citation_card's own scope / same-lineage notes.
      - rule26 (_composite_quote_error, kernel/glosa_kernel.py) -- exact_passage splice-marker
        shape check (on the citation_card).

Corpus: N=40 claim/citation card pairs, drawn from the EXISTING sim corpus
(tests/sim/corpus/{claims,citations,labels.json}, built by tests/sim/gen_corpus.py, already on
disk -- this script does not regenerate or mutate that corpus). Every card carries exactly one
labelled, known defect from one of five classes that this repo's own defect taxonomy already
frames as undisclosed-AI-fill or undisclosed-assumption defects:

  hidden_ai_fill            (8) -- AI-drafted text presented as human retained record, WITH a
                                    self-disclosed ai_assisted_fields marker rule27 can read.
  hidden_ai_fill_unmarked   (8) -- the same hidden AI-fill, but with NO marker at all (the S4b
                                    gap gen_corpus.py's own comments name -- included here because
                                    a fair proxy must include the case where the defect exists and
                                    is not caught by either route, not just the cases designed to
                                    be caught).
  inflated_bearing          (8) -- an own-lineage/context source marked SUPPORTS without
                                    disclosing it is not independent evidence (an undisclosed
                                    assumption of evidentiary weight).
  composite_quote           (8) -- a spliced/assembled quotation presented as one continuous
                                    passage (an undisclosed assumption of continuity).
  same_vendor_review        (8) -- an independent_check marked PASSED at independence_class I1
                                    (same model/session) -- an undisclosed assumption of
                                    independence; this is the one class route B (27/28/26) is NOT
                                    designed to reach, kept in the N=40 anyway so route B's count
                                    is not inflated by only including classes it targets, and so a
                                    B <= A finding remains genuinely possible here, not
                                    pre-decided by which 40 cards were chosen.
                                    ------------------------------------------------------------
                                    total: 40

Tier of every count this script prints or writes: finite_diagnostic -- an exact tally over this
one fixed 40-card selection, this run, today. Not a claim about H3 in general, not a claim about
any other corpus, and NOT a claim about what a real cross-vendor (I3) run would find -- a real I3
run remains the decisive test this proxy stands in for.

Fail-Able Gate Law (BBL-119): this script is not a new kernel rule, so it does not itself carry a
rule id -- but its own two control fixtures (build_passing_control / build_failing_control) are
its failing-control + passing-control pair, exercised by tests/test_h3_falsifier.py, so the
harness itself is falsifiable: a passing-control card must score zero catches on both routes, and
a failing-control card (a hidden_ai_fill defect, the one class engineered to be caught) must score
at least one catch on route B.

The falsifier direction is reported honestly whichever way it comes out: if route B's catch count
is <= route A's on this N=40 selection, that DEFEATS H3 in this proxy, and this script says so in
its own printed/written output rather than only reporting a "B wins" framing.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SIM_DIR = REPO / "tests" / "sim"
CORPUS_DIR = SIM_DIR / "corpus"
H3_DIR = SIM_DIR / "h3"
REPORT_PATH = SIM_DIR / "report.md"
RESULTS_PATH = H3_DIR / "h3_results.json"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

DEFECT_CLASSES = [
    "hidden_ai_fill",
    "hidden_ai_fill_unmarked",
    "inflated_bearing",
    "composite_quote",
    "same_vendor_review",
]
N_PER_CLASS = 8
N_EXPECTED = len(DEFECT_CLASSES) * N_PER_CLASS  # 40


# --------------------------------------------------------------------------------------------
# Corpus selection (reads the EXISTING tests/sim/corpus/ fixtures; never regenerates them).
# --------------------------------------------------------------------------------------------

def load_selection():
    """Return the 40 (label, claim_card, citation_card) tuples for the five defect classes
    above, read directly off tests/sim/corpus/labels.json + corpus/{claims,citations}/*.json.
    Raises if the on-disk corpus does not actually carry 8 of each class -- this script never
    silently pads or trims the N=40 it claims to run."""
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))["cards"]
    selection = []
    for defect in DEFECT_CLASSES:
        rows = [r for r in labels if r.get("defect") == defect]
        if len(rows) != N_PER_CLASS:
            raise RuntimeError(
                f"H3 sim expects exactly {N_PER_CLASS} '{defect}' cards in "
                f"tests/sim/corpus/labels.json, found {len(rows)} -- corpus on disk does not "
                "match this script's stated N=40 design; fix the mismatch before running."
            )
        for row in rows:
            claim = json.loads((CORPUS_DIR / row["claim_file"]).read_text(encoding="utf-8"))
            citation = json.loads((CORPUS_DIR / row["citation_file"]).read_text(encoding="utf-8"))
            selection.append({"label": row, "claim": claim, "citation": citation})
    if len(selection) != N_EXPECTED:
        raise RuntimeError(f"H3 sim selection is {len(selection)} cards, expected {N_EXPECTED}.")
    return selection


# --------------------------------------------------------------------------------------------
# Route A -- "same-vendor" proxy: the maker's own field-completeness check. Presence/non-empty
# only -- never a cross-field or cross-artifact comparison. This is a deliberate, disclosed
# asymmetry (see module docstring): it is what a maker re-checking its OWN output, without an
# independent second reader, mechanically amounts to -- "is the form filled in", not "is the
# content self-consistent".
# --------------------------------------------------------------------------------------------

def _non_empty(value):
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


def route_a_maker_completeness_catches(claim, citation):
    """Return a list of finding strings ('completeness gap: <field>') for any disclosure-
    relevant field that is missing/empty on this pair. Never inspects field CONTENT for
    contradiction -- only presence. Returns [] when every checked field is populated (this is
    the expected outcome for every one of the 40 seeded defects, since none of them blanks a
    field -- they all leave every field non-empty but semantically wrong; see module docstring)."""
    findings = []
    fq = (claim.get("five_questions") or {})
    seen = fq.get("seen") or {}
    ai_filled = fq.get("ai_filled") or {}
    tested = fq.get("tested") or {}
    checks = {
        "five_questions.seen.access_model": seen.get("access_model"),
        "five_questions.ai_filled (any entry)": list(ai_filled.values()) if isinstance(ai_filled, dict) else None,
        "five_questions.tested.evidence_relations": tested.get("evidence_relations"),
        "citation.exact_passage": citation.get("exact_passage"),
    }
    # NOTE: independent_check.{checker_id,approver_id,status} are deliberately NOT checked here.
    # A Draft-stage card legitimately carries independent_check.status == "NONE" with checker_id/
    # approver_id null (no check has happened yet) -- that is a valid, complete state, not a
    # completeness gap. Folding those fields in here would make route A trip on every card that
    # has not yet been independently checked (a lifecycle fact) rather than on the actual
    # per-defect disclosure gap this route is trying to (fail to) find -- a confound, not a
    # finding. Excluded after this was caught empirically on the first run of this script (see
    # tests/sim/h3/h3_results.json commit history / tests/sim/report.md H3 section).
    for field_name, value in checks.items():
        if not _non_empty(value):
            findings.append(f"completeness gap: {field_name} is missing/empty")
    return findings


# --------------------------------------------------------------------------------------------
# Route B -- cross-route proxy: the kernel's own independent rules 27/28/26, called DIRECTLY
# (not through validate_claim_card/validate_citation_card) so that nothing outside these three
# named rules contributes to route B's count.
# --------------------------------------------------------------------------------------------

def route_b_kernel_rules_catches(claim, citation):
    """Return a list of finding strings from rule27/rule28/rule26, called directly. `citation`
    is passed to rule28 as the sole entry of `citation_cards` so a resolvable citation_ref can
    actually resolve (mirrors how validate_claim_card is normally called with the companion
    citation card, per tests/sim/baseline.py's own convention)."""
    findings = []
    r27 = k._hidden_ai_fill_error(claim)
    if r27:
        findings.append(r27)
    r28_errors, _not_checked = k._inflated_bearing_errors(claim, citation_cards=[citation])
    findings.extend(r28_errors)
    r26 = k._composite_quote_error(citation)
    if r26:
        findings.append(r26)
    return findings


# --------------------------------------------------------------------------------------------
# Fail-Able Gate Law controls (BBL-119): a passing control (clean card, both routes silent) and
# a failing control (a known hidden_ai_fill defect, route B must catch it). Exercised by
# tests/test_h3_falsifier.py -- kept here, not duplicated, so the test imports the same fixtures
# this script's own report run uses.
# --------------------------------------------------------------------------------------------

def build_passing_control():
    """A structurally clean claim/citation pair (the same recipe tests/sim/gen_corpus.py uses
    for its 60 valid cards) -- both routes must report zero findings on this pair."""
    base_claim = json.loads((REPO / "schema/examples/claim_card.example.json").read_text(encoding="utf-8"))
    base_citation = json.loads((REPO / "schema/examples/citation_card.example.json").read_text(encoding="utf-8"))
    claim = copy.deepcopy(base_claim)
    citation = copy.deepcopy(base_citation)
    # Make sure the fields route A checks are populated, and nothing route B watches for is present.
    fq = claim.setdefault("five_questions", {})
    fq.setdefault("seen", {})["access_model"] = "founder's own retained observation log"
    fq.setdefault("ai_filled", {})["retained_record_route"] = "none identified"
    fq.setdefault("tested", {})["evidence_relations"] = [
        {
            "evidence_id": "ev-control-001",
            "bearing": "NEUTRAL",
            "independence_class": "I1",
            "citation_ref": citation.get("id", "cite-control-001"),
            "strength": "context",
            "review_mode": "MAKER_SELF_CHECK",
            "route_id": None,
            "asserted_by": "founder",
            "date": "2026-09-05",
            "notes": "",
        }
    ]
    citation["exact_passage"] = "a single continuous verbatim passage, no splice marker"
    claim["independent_check"] = {
        "status": "PASSED",
        "independence_class": "I3",
        "checker_id": "vendor-2",
        "maker_id": "founder",
        "approver_id": "founder",
    }
    return claim, citation


def build_failing_control():
    """A known hidden_ai_fill defect (route B's rule27 is designed to catch this one) -- pulled
    from the on-disk corpus rather than re-synthesized, so the control exercises the SAME fixture
    the H3 selection itself uses."""
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))["cards"]
    row = next(r for r in labels if r.get("defect") == "hidden_ai_fill")
    claim = json.loads((CORPUS_DIR / row["claim_file"]).read_text(encoding="utf-8"))
    citation = json.loads((CORPUS_DIR / row["citation_file"]).read_text(encoding="utf-8"))
    return claim, citation


# --------------------------------------------------------------------------------------------
# Main run
# --------------------------------------------------------------------------------------------

def run():
    selection = load_selection()
    per_defect = {d: {"n": 0, "route_a_caught": 0, "route_b_caught": 0} for d in DEFECT_CLASSES}
    rows = []
    for entry in selection:
        defect = entry["label"]["defect"]
        claim, citation = entry["claim"], entry["citation"]
        a_findings = route_a_maker_completeness_catches(claim, citation)
        b_findings = route_b_kernel_rules_catches(claim, citation)
        per_defect[defect]["n"] += 1
        if a_findings:
            per_defect[defect]["route_a_caught"] += 1
        if b_findings:
            per_defect[defect]["route_b_caught"] += 1
        rows.append(
            {
                "id": entry["label"]["id"],
                "defect": defect,
                "route_a_findings": a_findings,
                "route_b_findings": b_findings,
            }
        )

    total_n = sum(v["n"] for v in per_defect.values())
    total_a = sum(v["route_a_caught"] for v in per_defect.values())
    total_b = sum(v["route_b_caught"] for v in per_defect.values())

    # Controls
    pc_claim, pc_citation = build_passing_control()
    pc_a = route_a_maker_completeness_catches(pc_claim, pc_citation)
    pc_b = route_b_kernel_rules_catches(pc_claim, pc_citation)
    fc_claim, fc_citation = build_failing_control()
    fc_a = route_a_maker_completeness_catches(fc_claim, fc_citation)
    fc_b = route_b_kernel_rules_catches(fc_claim, fc_citation)

    h3_direction = "SUPPORTED_IN_THIS_PROXY" if total_b > total_a else "DEFEATED_IN_THIS_PROXY" if total_b <= total_a and total_a > 0 else "NOT_DECIDED_IN_THIS_PROXY"
    if total_b <= total_a:
        h3_direction = "DEFEATED_IN_THIS_PROXY (route B did not out-catch route A)"
    else:
        h3_direction = "SUPPORTED_IN_THIS_PROXY (route B out-caught route A)"

    result = {
        "tier": "finite_diagnostic",
        "n": total_n,
        "n_expected": N_EXPECTED,
        "route_a_caught_total": total_a,
        "route_b_caught_total": total_b,
        "difference_b_minus_a": total_b - total_a,
        "h3_falsifier_direction": h3_direction,
        "per_defect": per_defect,
        "controls": {
            "passing_control": {"route_a_findings": pc_a, "route_b_findings": pc_b, "expected": "both empty"},
            "failing_control": {"route_a_findings": fc_a, "route_b_findings": fc_b, "expected": "route_b non-empty (rule27)"},
        },
        "rows": rows,
        "proxy_disclosure": (
            "PROXY, not a real cross-vendor (I3) run: no second vendor was invoked. route A "
            "and route B are both deterministic Python in this one process. A real I3 run "
            "remains the decisive test for H3; this script measures a mechanical stand-in only."
        ),
        "note": "readout over this fixed 40-card selection, this run, today -- not a general claim about H3.",
    }
    return result


def write_outputs(result):
    H3_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = []
    lines.append("## H3 falsifier simulation (proxy)")
    lines.append("")
    lines.append(
        "Tier: **finite_diagnostic** -- an exact tally over one fixed 40-card selection drawn "
        "from `tests/sim/corpus/` (built by `tests/sim/gen_corpus.py`), this run, today. "
        "**This is a PROXY, not a real cross-vendor (I3) run** -- no second vendor is invoked "
        "anywhere; both routes are deterministic Python run in this one process. A real I3 run "
        "remains the decisive test for H3."
    )
    lines.append("")
    lines.append(
        "H3 as stated: cross-vendor (I3) checking of claim cards catches undisclosed AI-fill / "
        "undisclosed assumptions at a higher rate than same-vendor re-checking. Route A (same-"
        "vendor proxy) = the maker's own field-completeness check (is every disclosure field "
        "present/non-empty, never cross-field). Route B (cross-route proxy) = the kernel's "
        "independent rules 27 (`_hidden_ai_fill_error`), 28 (`_inflated_bearing_errors`), 26 "
        "(`_composite_quote_error`), called directly."
    )
    lines.append("")
    lines.append("| defect class | n | route A caught | route B caught |")
    lines.append("|---|---|---|---|")
    for d in DEFECT_CLASSES:
        v = result["per_defect"][d]
        lines.append(f"| {d} | {v['n']} | {v['route_a_caught']} | {v['route_b_caught']} |")
    lines.append(f"| **total** | **{result['n']}** | **{result['route_a_caught_total']}** | **{result['route_b_caught_total']}** |")
    lines.append("")
    lines.append(
        f"Difference (B - A): **{result['difference_b_minus_a']}**. Falsifier direction: "
        f"**{result['h3_falsifier_direction']}** -- reported honestly whichever way it came out "
        "(B <= A would defeat H3 in this proxy, per this task's own instruction)."
    )
    lines.append("")
    lines.append(
        "Controls (Fail-Able Gate Law, BBL-119): passing control (clean fixture) -> route A "
        f"findings {result['controls']['passing_control']['route_a_findings']!r}, route B "
        f"findings {result['controls']['passing_control']['route_b_findings']!r}. Failing "
        "control (a known `hidden_ai_fill` fixture) -> route A findings "
        f"{result['controls']['failing_control']['route_a_findings']!r}, route B findings "
        f"{result['controls']['failing_control']['route_b_findings']!r}."
    )
    lines.append("")
    lines.append(
        "Corpus-construction caveat: every seeded defect leaves every field non-empty (semantically "
        "wrong, never blank), so route A's 0/40 is guaranteed by how the corpus was built, not an "
        "empirical finding about same-vendor checks in general. Route A is deliberately the weakest "
        "honest maker-side check, so the difference measures rule-set independence inside one "
        "process, not vendor independence; H3 as a hypothesis keeps tier `Open` until a real I3 run "
        "exists."
    )
    lines.append("")
    lines.append(
        "Caveat disclosed plainly: `same_vendor_review` (8 of the 40) is a class route B's "
        "rules 27/28/26 are not designed to reach at all -- included so this N=40 is not "
        "curated to guarantee a B-wins outcome. Full per-card findings: "
        "`tests/sim/h3/h3_results.json`."
    )
    lines.append("")
    section = "\n".join(lines)

    existing = REPORT_PATH.read_text(encoding="utf-8") if REPORT_PATH.exists() else ""
    marker = "## H3 falsifier simulation (proxy)"
    if marker in existing:
        head, _, rest = existing.partition(marker)
        # drop the old section body up to the next "## " heading (or EOF)
        rest_after_heading = rest.split("\n", 1)[1] if "\n" in rest else ""
        next_idx = rest_after_heading.find("\n## ")
        tail = rest_after_heading[next_idx:] if next_idx != -1 else ""
        new_content = head + section + tail
    else:
        sep = "\n" if existing.endswith("\n") or existing == "" else "\n\n"
        new_content = existing + sep + section
    REPORT_PATH.write_text(new_content, encoding="utf-8")


def main():
    result = run()
    write_outputs(result)
    print(json.dumps({k_: v for k_, v in result.items() if k_ != "rows"}, indent=1, ensure_ascii=False))
    return result


if __name__ == "__main__":
    main()
