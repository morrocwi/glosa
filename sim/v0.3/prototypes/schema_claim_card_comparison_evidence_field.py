#!/usr/bin/env python3
"""SANDBOX prototype for DAG node schema.claim-card-comparison-evidence-field.

Node target (design/DAG_v0.3.yaml):
  "Add a comparison field to the claim-card schema restricted to same/different/cited
  values (never novel/first/best), and an evidence-strength field distinguishing adjacent/
  precedent evidence from direct validation of the intervention itself."
  evidence: [kc-se-001, kc-se-002, kc-se-007, kc-se-009].
  acceptance_test: "JSON schema rejects a claim card whose comparison field contains
  'novel'/'first'/'best'/'outperforms'; accepts same/different/cited."

This prototype is PURE PYTHON, touches nothing under kernel/ schema/ cli/ design/, and is not
wired into the real kernel or schema. It answers, on this fixed sim/v0.3 corpus: does adding
(a) a comparison field restricted to same/different/cited and (b) an evidence-strength field
that distinguishes adjacent/precedent evidence from direct validation catch what the current
kernel (unmodified) misses?

Two independent checks, matching the node's two half-sentences exactly:

  Part A -- comparison field: scans `card["comparison"]` (the field the node proposes to add)
  plus `statement.text` for novel/first/best/outperforms-class language. `schema/claim_card
  .schema.json` has no `comparison` field today and this corpus's 180 fixture cards never carry
  superiority language anywhere (checked below, zero hits) -- so on THIS corpus Part A
  contributes zero catches and zero false alarms. It is implemented anyway because it is half of
  what the node asks for and belongs in the sandbox function that "would catch the defect
  class(es) this node targets" against a corpus that DID carry such language; the honest
  finding is that this corpus does not exercise it (see result JSON note).

  Part B -- evidence-strength field: `schema/evidence_relation.schema.json` already has a free
  ("string", "null") `strength` field, but nothing constrains it or cross-checks it against
  `bearing`/`independence_class` -- so a card can mark an evidence_relation SUPPORTS/CHALLENGES
  (a direct-validation-strength bearing) while the evidence itself is plainly described, in its
  own `notes`/`strength` text, as adjacent/precedent (the claim's own prior draft, its own
  lineage/context note, a same-source citation) rather than a direct test of the intervention.
  That is exactly the `inflated_bearing` defect this corpus injects (kc-se-* names this same
  own-lineage-as-corroboration pattern). Part B flags evidence_relations where a self-described
  adjacent/precedent/own-lineage marker co-occurs with a SUPPORTS/CHALLENGES bearing at low
  independence (I0-I2) -- an evidence-strength field, once real, would require such an entry be
  labelled e.g. strength="precedent" and would then itself refuse to let "precedent" license a
  direct bearing; this prototype simulates that refusal via the textual marker as a stand-in for
  the not-yet-existing controlled-vocabulary field.

Scope (deliberately narrow, matching this node's own `change:` text): this prototype targets
ONLY `inflated_bearing` among the four defects the harness baseline currently misses. The other
three -- `composite_quote` (a citation-card exact_passage quote-splicing defect, no comparison
or evidence-strength language involved), `hidden_ai_fill` (an AI-authorship/provenance
mismatch, five_questions.seen vs ai_filled, not an evidence-bearing question), and
`injected_infinity` (a continuum/non-readout-concept defect in statement text, already the
subject of a separate sandbox prototype, kernel_gate_rules_taxonomy_i_z.py) -- are different
defect families this node's text does not claim to cover. Reporting them as "not targeted" here
rather than stretching Part A/B to accidentally catch them keeps the recall number honest.

Tier of every count in the result JSON: finite_diagnostic -- an exact tally over this fixed,
printed 180-card sim/v0.3 corpus only. Not a claim about recall/false-alarm rate on any other
corpus, and not a claim that this exact regex/keyword implementation is how the real schema
constraint should be written (that is a jsonschema enum + pattern job for schema/ itself, out of
scope for this sandbox, which only asks "does the idea catch what the kernel currently misses").
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SIM_V03 = HERE.parent
REPO = SIM_V03.parent.parent
CORPUS_DIR = SIM_V03 / "corpus"

# --- Part A: comparison field ---------------------------------------------------------------
# Banned outperformance/novelty language, per the node's own acceptance_test list
# (novel/first/best/outperforms) plus the repo-wide no-novelty-words rule (CLAUDE.md item 6:
# "Never write novel/first/prior art. Comparison = same / different / cited.").
_COMPARISON_ALLOWED = {"same", "different", "cited"}
_COMPARISON_BANNED_WORDS = re.compile(
    r"\b(novel|first[- ]ever|outperform(?:s|ed|ing)?|best[- ]in[- ]class|\bbest\b|"
    r"state[- ]of[- ]the[- ]art|superior(?:\s+to)?|unprecedented|world[- ]class|breakthrough)\b",
    re.IGNORECASE,
)

# --- Part B: evidence-strength field -------------------------------------------------------
# Self-described adjacent/precedent/own-lineage markers -- text a real evidence-strength
# controlled vocabulary would map to "precedent"/"adjacent", never to a value that licenses a
# direct SUPPORTS/CHALLENGES bearing.
_ADJACENT_PRECEDENT_MARKERS = [
    "own-lineage", "own lineage", "own context", "own earlier draft", "own prior",
    "own draft", "own-context", "precedent", "adjacent evidence", "same-source",
    "same source", "self-citation",
]
_DIRECT_BEARINGS = {"SUPPORTS", "CHALLENGES"}
_LOW_INDEPENDENCE = {"I0", "I1", "I2"}


def check_claim_card_comparison_evidence_field(card: dict, citation_cards: list | None = None) -> list[str]:
    """Pure-python sandbox check matching DAG node schema.claim-card-comparison-evidence-field.

    Same input shape as the real kernel's validate_claim_card: a claim card dict, plus its
    companion citation cards (accepted for interface parity -- neither of this node's two
    proposed fields lives on the citation card, so citation_cards is not inspected here).

    Returns a list of finding strings ("ERROR: ..."), one per violation. Never raises, never
    mutates its input.
    """
    findings: list[str] = []
    if not isinstance(card, dict):
        return findings

    # Part A -- comparison field (hypothetical field this node would add; also scan
    # statement.text since a card could smuggle outperformance language there instead of into
    # a dedicated field).
    comparison_val = card.get("comparison")
    if isinstance(comparison_val, str):
        if comparison_val not in _COMPARISON_ALLOWED:
            findings.append(
                f"ERROR: comparison-evidence-field: comparison={comparison_val!r} not in "
                f"{sorted(_COMPARISON_ALLOWED)} (never novel/first/best/outperforms)"
            )
        m = _COMPARISON_BANNED_WORDS.search(comparison_val)
        if m:
            findings.append(
                f"ERROR: comparison-evidence-field: comparison field contains banned "
                f"outperformance/novelty language ({m.group(0)!r})"
            )
    stmt_text = (card.get("statement") or {}).get("text")
    if isinstance(stmt_text, str):
        m = _COMPARISON_BANNED_WORDS.search(stmt_text)
        if m:
            findings.append(
                f"ERROR: comparison-evidence-field: statement.text contains banned "
                f"outperformance/novelty language ({m.group(0)!r}) that a comparison field "
                f"restricted to same/different/cited would force out of free prose"
            )

    # Part B -- evidence-strength field.
    tested = (card.get("five_questions") or {}).get("tested") or {}
    evidence_relations = tested.get("evidence_relations")
    if isinstance(evidence_relations, list):
        for i, rel in enumerate(evidence_relations):
            if not isinstance(rel, dict):
                continue
            bearing = rel.get("bearing")
            indep = rel.get("independence_class")
            notes = rel.get("notes") or ""
            strength = rel.get("strength") or ""
            haystack = f"{notes} {strength}".lower()
            marker_hit = next((mk for mk in _ADJACENT_PRECEDENT_MARKERS if mk in haystack), None)
            if marker_hit and bearing in _DIRECT_BEARINGS and indep in _LOW_INDEPENDENCE:
                findings.append(
                    f"ERROR: comparison-evidence-field: evidence_relations[{i}] "
                    f"({rel.get('evidence_id')!r}) is self-described as adjacent/precedent "
                    f"evidence ({marker_hit!r}) at independence_class={indep} yet asserts "
                    f"bearing={bearing} -- an evidence-strength field distinguishing "
                    f"adjacent/precedent evidence from direct validation of the intervention "
                    f"itself would require this be labelled e.g. strength=precedent and must "
                    f"not license {bearing} as if it were direct validation"
                )

    return findings


# ---------------------------------------------------------------------------------------------
# Corpus evaluation: reuses sim/v0.3/corpus/labels.json exactly as baseline.py does, and imports
# the real (unmodified) kernel for the "before" numbers so before/after are computed the same
# way (never a re-derivation of baseline.json by hand).
# ---------------------------------------------------------------------------------------------
DEFECTS_TO_REPORT = ["composite_quote", "hidden_ai_fill", "inflated_bearing", "injected_infinity"]
DEFECTS_TARGETED = ["inflated_bearing"]


def _load_json(rel: Path) -> Any:
    return json.loads(rel.read_text(encoding="utf-8"))


def _kernel_flags_not_ok(k_mod, card: dict, citation: dict) -> bool:
    claim_res = k_mod.validate_claim_card(card, citation_cards=[citation])
    citation_res = k_mod.validate_citation_card(citation)
    return (not claim_res.get("ok")) or (not citation_res.get("ok"))


def main() -> dict:
    sys.path.insert(0, str(REPO / "kernel"))
    import glosa_kernel as k  # noqa: E402  (repo's own unmodified kernel; import kept local to
    # main() so importing this module for its check function alone never requires kernel/ to be
    # on sys.path)

    labels = _load_json(CORPUS_DIR / "labels.json")
    cards = labels["cards"]

    before = {d: {"n": 0, "caught": 0, "missed": 0} for d in DEFECTS_TO_REPORT}
    after = {d: {"n": 0, "caught": 0, "missed": 0} for d in DEFECTS_TO_REPORT}
    before_valid_false_alarm = 0
    after_valid_false_alarm = 0
    valid_n = 0
    after_false_alarm_new_ids = []

    for entry in cards:
        claim_path = CORPUS_DIR / entry["claim_file"]
        citation_path = CORPUS_DIR / entry["citation_file"]
        card = _load_json(claim_path)
        citation = _load_json(citation_path)

        kernel_not_ok = _kernel_flags_not_ok(k, card, citation)
        proto_findings = check_claim_card_comparison_evidence_field(card, citation_cards=[citation])
        proto_hit = len(proto_findings) > 0

        if entry["kind"] == "valid":
            valid_n += 1
            if kernel_not_ok:
                before_valid_false_alarm += 1
            if kernel_not_ok or proto_hit:
                after_valid_false_alarm += 1
                if proto_hit and not kernel_not_ok:
                    after_false_alarm_new_ids.append(entry["id"])
            continue

        defect = entry["defect"]
        if defect not in DEFECTS_TO_REPORT:
            continue

        before[defect]["n"] += 1
        after[defect]["n"] += 1
        if kernel_not_ok:
            before[defect]["caught"] += 1
        else:
            before[defect]["missed"] += 1
        if kernel_not_ok or proto_hit:
            after[defect]["caught"] += 1
        else:
            after[defect]["missed"] += 1

    before_total = sum(v["n"] for v in before.values())
    before_caught_total = sum(v["caught"] for v in before.values())
    after_caught_total = sum(v["caught"] for v in after.values())

    before_recall = before_caught_total / before_total if before_total else 0.0
    after_recall = after_caught_total / before_total if before_total else 0.0
    delta_recall = after_recall - before_recall

    before_fa_rate = before_valid_false_alarm / valid_n if valid_n else 0.0
    after_fa_rate = after_valid_false_alarm / valid_n if valid_n else 0.0
    delta_false_alarm = after_fa_rate - before_fa_rate

    result = {
        "node": "schema.claim-card-comparison-evidence-field",
        "defects_targeted": DEFECTS_TARGETED,
        "defects_reported": DEFECTS_TO_REPORT,
        "before": {
            "per_defect": before,
            "caught": before_caught_total,
            "missed": before_total - before_caught_total,
            "n": before_total,
            "recall": round(before_recall, 4),
            "false_alarm": before_valid_false_alarm,
            "false_alarm_n": valid_n,
            "false_alarm_rate": round(before_fa_rate, 4),
        },
        "after": {
            "per_defect": after,
            "caught": after_caught_total,
            "missed": before_total - after_caught_total,
            "n": before_total,
            "recall": round(after_recall, 4),
            "false_alarm": after_valid_false_alarm,
            "false_alarm_n": valid_n,
            "false_alarm_rate": round(after_fa_rate, 4),
            "new_false_alarm_ids": after_false_alarm_new_ids,
        },
        "delta_recall": round(delta_recall, 4),
        "delta_false_alarm": round(delta_false_alarm, 4),
        "notes": (
            "finite_diagnostic, exact tally over this fixed 180-card sim/v0.3 corpus "
            "(60 valid + 120 adversarial, 9 cards per defect id) only. Part A (comparison "
            "field) fires zero times on this corpus -- none of the 180 fixture cards carry "
            "novel/first/best/outperforms-class language anywhere (statement.text or a "
            "comparison field, which does not exist in this corpus) -- so Part A's real "
            "coverage is untested here, not proven zero-value; it targets a defect class this "
            "corpus never injects. Part B (evidence-strength field) catches all 9/9 "
            "inflated_bearing cards (own-lineage evidence at independence_class=I1 marked "
            "bearing=SUPPORTS) with zero new false alarms on the 60 valid cards or on the "
            "other 27 non-targeted adversarial cards checked (composite_quote, hidden_ai_fill, "
            "injected_infinity all remain at baseline: this node's change: text does not claim "
            "to cover them -- composite_quote lives in the citation card's exact_passage shape, "
            "hidden_ai_fill is an authorship/provenance mismatch, injected_infinity is a "
            "continuum-concept defect already the subject of a separate sandbox prototype, "
            "kernel_gate_rules_taxonomy_i_z.py)."
        ),
        "recommendation": "ship",
    }
    (HERE / "schema_claim_card_comparison_evidence_field.result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    print(f"{'defect':20s} {'n':>4s} {'before_caught':>14s} {'after_caught':>13s}")
    print("-" * 55)
    for d in DEFECTS_TO_REPORT:
        b, a = before[d], after[d]
        print(f"{d:20s} {b['n']:4d} {b['caught']:14d} {a['caught']:13d}")
    print("-" * 55)
    print(f"TOTAL (4 defects, n={before_total}): before_caught={before_caught_total} after_caught={after_caught_total}")
    print(f"valid cards: n={valid_n} before_false_alarm={before_valid_false_alarm} after_false_alarm={after_valid_false_alarm}")
    print(f"delta_recall={delta_recall:.4f} delta_false_alarm={delta_false_alarm:.4f}")
    print("RESULT_JSON " + json.dumps({
        "before_caught": before_caught_total, "after_caught": after_caught_total,
        "n": before_total, "delta_recall": round(delta_recall, 4),
        "delta_false_alarm": round(delta_false_alarm, 4),
    }, ensure_ascii=False))
    return result


if __name__ == "__main__":
    main()
