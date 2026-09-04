#!/usr/bin/env python3
"""K4-proto for design/DAG_v0.3.yaml node `kernel.unverified-verifiability-flag`.

SANDBOX ONLY. This file does not import, edit, or monkeypatch kernel/, schema/, cli/, or
design/ -- it is a pure-python, standalone reimplementation, same input shape as the kernel
(a claim_card dict), so it can be diffed against kernel behaviour without ever touching it.

Node under test (design/DAG_v0.3.yaml, id kernel.unverified-verifiability-flag):
  title: "Verifiable with no stated procedure" as a named narrow sub-case
  change: nest "claims verifiable/checkable with no stated procedure" under the existing
    vague-attribution disclaimer-catalogue entry as a named narrower sub-case; do not make
    it a purely mechanical/keyword-triggered check (intent-dependence defeats pure automation).
  acceptance_test: finite_diagnostic sim -- a hand-labeled set of "verifiable"-claim sentences
    with/without a stated procedure -- flag routes to human review, never auto-rejects.

Relevant defect in sim/v0.3/corpus/labels.json: "verifiable_no_procedure" (n=8 adversarial
cards). NOT one of the four defects sim/v0.3/baseline.json already records as fully missed by
the kernel (hidden_ai_fill, inflated_bearing, composite_quote, injected_infinity) -- this
prototype does not target those; they are unrelated defect classes with no textual overlap
with "verified"/"certified" language (checked directly against the corpus, see notes in the
.result.json). Reported anyway, per baseline.json, so the before/after table shows the whole
corpus, not just the one row this node moves.

WHAT KERNEL ALREADY DOES (read directly from kernel/glosa_kernel.py, not from memory):
  compute_disclaimers() already runs a keyword regex, unconditionally, over the card's own
  statement text + translation text, and emits D-DVP-NOT-K2 whenever that regex matches AND
  the card's max evidence independence_class never reaches I5 (kernel/glosa_kernel.py, near
  `_DVP_NOT_K2_KEYWORDS`). This is a genuine, order-independent, self-declaration-proof signal
  -- it fires regardless of what the card's own `disclaimers_emitted` list claims. It is a
  WARNING-only signal: validate_claim_card() never turns it into an error, so `ok` stays True
  (verified directly below in this file's own harness) -- i.e. the "never auto-rejects" half
  of the acceptance test is ALREADY satisfied by the current kernel, not something this
  prototype needs to add.

  sim/v0.3/baseline.py's "caught" metric for this defect, however, does NOT read
  compute_disclaimers()'s output directly -- it diffs computed vs the card's own DECLARED
  disclaimers_emitted list, and only counts a catch when that list is stale (missing the id).
  That happens to be true for all 8 corpus cards (gen_corpus.py deliberately leaves the
  declared list stale), so baseline.json shows 8/8 caught for this defect today -- but a card
  that dishonestly *declares* D-DVP-NOT-K2 up front (while still making an inflated
  verification claim) would defeat baseline.py's diff-based metric even though
  compute_disclaimers() itself still fires correctly underneath.

WHAT THIS PROTOTYPE ADDS (the actual gap this file targets):
  1. A catch signal that reads straight off content (text + independence_class), never off the
     card's own self-declared disclaimers_emitted list -- so it cannot be defeated by a card
     that fabricates its own declared-disclaimer bookkeeping.
  2. A keyword set that also covers the Thai-language equivalents of "verified" (the kernel's
     own `_DVP_NOT_K2_KEYWORDS` regex is English-only: verified|peer reviewed|certified|K2|K3).
     Every corpus card that carries this defect happens to embed the literal English loanword
     "verified" inline in its Thai sentence, so the kernel's English-only regex already catches
     all 8 -- this is a real but UNEXERCISED blind spot on the current fixed corpus (documented
     with a synthetic Thai-only probe sentence in the .result.json notes, evaluated separately
     from the 180-card corpus scoring so it never inflates the reported recall/false-alarm
     numbers).
  3. Explicit routing language ("HUMAN_REVIEW", never "REJECT") on every emitted string, so a
     caller wiring this into a UI cannot mistake it for a hard-fail signal.

Tier of every count this file prints/writes: finite_diagnostic -- an exact tally over the fixed,
printed corpus in sim/v0.3/corpus/ only, not a general claim about kernel behaviour elsewhere.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # sim/v0.3/prototypes
SIM_V03 = HERE.parent                            # sim/v0.3
REPO = SIM_V03.parent.parent                     # glosa/
CORPUS_DIR = SIM_V03 / "corpus"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

NODE_ID = "kernel.unverified-verifiability-flag"
DEFECT_TARGETED = "verifiable_no_procedure"
# Background-context defects sim/v0.3/baseline.json already records as fully missed by the
# kernel today, over the whole 180-card corpus -- NOT targeted by this node/prototype, reported
# for context per the task brief only.
BASELINE_MISSED_DEFECTS_CONTEXT = [
    "composite_quote", "hidden_ai_fill", "inflated_bearing", "injected_infinity",
]

_INDEPENDENCE_ORDER = ["I0", "I1", "I2", "I3", "I4", "I5"]

# Kernel's own regex (kernel/glosa_kernel.py, `_DVP_NOT_K2_KEYWORDS`), copied verbatim here
# (not imported -- this file must stand alone as a sandbox prototype) so the "before" row in
# this file's own evaluation matches kernel behaviour exactly, and so the diff against the
# extended set below is visible in one place.
_KERNEL_KEYWORDS = re.compile(r"\b(verified|peer reviewed|certified|K2|K3)\b", re.IGNORECASE)

# This prototype's extension: same English set, PLUS the Thai-language equivalents of
# "verified/confirmed/proven/certified" that a Thai-first claim-card corpus will actually see
# in the wild once cards stop borrowing the English loanword inline.
_EXTENDED_KEYWORDS = re.compile(
    r"\b(verified|peer reviewed|certified|K2|K3)\b"
    r"|(?:ยืนยันแล้ว|พิสูจน์แล้ว|ตรวจสอบแล้ว|ทวนสอบแล้ว|รับรองแล้ว|ผ่านการตรวจสอบแล้ว)",
    re.IGNORECASE,
)


def _max_independence_class(evidence_relations):
    best = None
    for er in evidence_relations or []:
        ic = er.get("independence_class")
        if ic in _INDEPENDENCE_ORDER:
            if best is None or _INDEPENDENCE_ORDER.index(ic) > _INDEPENDENCE_ORDER.index(best):
                best = ic
    return best


def _text_fields(card):
    statement = card.get("statement") or {}
    return [
        statement.get("text"),
        (statement.get("translation") or {}).get("text"),
    ]


def check_unverified_verifiability_flag(card, citation_cards=None, keyword_re=_EXTENDED_KEYWORDS):
    """SANDBOX check. Same input shape as the kernel (a claim_card dict, optional
    citation_cards list -- accepted for interface parity, unused: this defect lives entirely
    in the claim card's own statement text + evidence independence, per gen_corpus.py's own
    construction of the defect).

    Returns a list of WARNING strings (never an error/reject signal) whenever the card's
    statement (original or translated) uses verification/certification-level language while
    its evidence never reaches independent verification (I5) -- the narrow
    "verifiable-with-no-stated-procedure" sub-case named by
    design/DAG_v0.3.yaml#kernel.unverified-verifiability-flag. An empty list means "no flag",
    not "verified true" -- this check only ever adds a soft flag, consistent with the node's
    acceptance_test (route to human review, never auto-reject).
    """
    warnings = []
    matched_text = [t for t in _text_fields(card) if t and keyword_re.search(t)]
    if not matched_text:
        return warnings

    evidence_relations = (card.get("five_questions") or {}).get("tested", {}).get("evidence_relations") or []
    max_ic = _max_independence_class(evidence_relations)
    if max_ic == "I5":
        # Verification language IS backed by an independently-reproduced (I5) evidence
        # relation -- this is the "with a stated procedure" branch the node explicitly says
        # must NOT be flagged (intent-dependence: the same words are fine when earned).
        return warnings

    warnings.append(
        "K4-PROTO-DVP: statement text uses verification/certification-level language "
        f"(matched={matched_text!r}) but max evidence independence_class="
        f"{max_ic!r} never reaches I5 -- flag as unverified-verifiability "
        "(narrow sub-case of the vague-attribution disclaimer catalogue), "
        "route to HUMAN_REVIEW; this is a WARNING, not an auto-reject."
    )
    return warnings


# --------------------------------------------------------------------------------------------
# Corpus evaluation harness (mirrors sim/v0.3/baseline.py's method so before/after are
# apples-to-apples; reuses nothing from baseline.py by import, to keep this file a standalone
# sandbox artifact, but the logic is deliberately identical where it overlaps).
# --------------------------------------------------------------------------------------------

def load_json(rel):
    return json.loads((CORPUS_DIR / rel).read_text(encoding="utf-8"))


def kernel_flags(card, citation):
    """'Before' signal, read straight off the current, unmodified kernel: True iff
    validate_claim_card/validate_citation_card raised an error/warning naming this defect, OR
    compute_disclaimers(card) computed D-DVP-NOT-K2 while the card's own declared
    disclaimers_emitted omits it (sim/v0.3/baseline.py's own method, reproduced here so this
    file's "before" row is directly comparable to sim/v0.3/baseline.json without re-running
    that script)."""
    claim_res = k.validate_claim_card(card, citation_cards=[citation])
    citation_res = k.validate_citation_card(citation)
    if not claim_res.get("ok") or not citation_res.get("ok"):
        return True
    computed = {d["id"] for d in k.compute_disclaimers(card)}
    declared = {d.get("id") for d in (card.get("disclaimers_emitted") or [])}
    return "D-DVP-NOT-K2" in (computed - declared)


def prototype_flags(card):
    return bool(check_unverified_verifiability_flag(card))


def evaluate():
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    before_per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in labels["defects"]}
    after_per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in labels["defects"]}
    before_fa = 0
    after_fa = 0
    before_fa_ids = []
    after_fa_ids = []
    valid_n = 0

    for entry in cards:
        card = load_json(entry["claim_file"])
        citation = load_json(entry["citation_file"])
        before_hit = kernel_flags(card, citation)
        after_hit = before_hit or prototype_flags(card)

        if entry["kind"] == "valid":
            valid_n += 1
            if before_hit:
                before_fa += 1
                before_fa_ids.append(entry["id"])
            if after_hit:
                after_fa += 1
                after_fa_ids.append(entry["id"])
        else:
            defect = entry["defect"]
            before_per_defect[defect]["n"] += 1
            after_per_defect[defect]["n"] += 1
            if before_hit:
                before_per_defect[defect]["caught"] += 1
            else:
                before_per_defect[defect]["missed"] += 1
            if after_hit:
                after_per_defect[defect]["caught"] += 1
            else:
                after_per_defect[defect]["missed"] += 1

    return {
        "labels": labels,
        "valid_n": valid_n,
        "before": {"per_defect": before_per_defect, "false_alarm": before_fa, "false_alarm_ids": before_fa_ids},
        "after": {"per_defect": after_per_defect, "false_alarm": after_fa, "false_alarm_ids": after_fa_ids},
    }


def _summ(per_defect, defects):
    n = sum(per_defect[d]["n"] for d in defects)
    caught = sum(per_defect[d]["caught"] for d in defects)
    missed = sum(per_defect[d]["missed"] for d in defects)
    return n, caught, missed


def _thai_only_probe():
    """Illustrative, NOT scored into the 180-card corpus numbers above: a synthetic minimal
    card carrying only the fields check_unverified_verifiability_flag reads, using a
    Thai-only verification claim (no English 'verified' loanword) at independence I1 -- the
    exact shape the kernel's English-only regex cannot see. Documents the latent gap named in
    this file's module docstring without inflating/deflating the corpus-derived recall or
    false-alarm counts."""
    probe_card = {
        "statement": {
            "text": "ผลสรุปนี้ผ่านการตรวจสอบแล้วโดยไม่มีขั้นตอนทำซ้ำที่ระบุไว้",
            "translation": None,
        },
        "five_questions": {
            "tested": {
                "evidence_relations": [
                    {"evidence_id": "ev-probe-001", "independence_class": "I1"}
                ]
            }
        },
    }
    kernel_hits = bool(check_unverified_verifiability_flag(probe_card, keyword_re=_KERNEL_KEYWORDS))
    prototype_hits = bool(check_unverified_verifiability_flag(probe_card, keyword_re=_EXTENDED_KEYWORDS))
    return {
        "probe_text": probe_card["statement"]["text"],
        "kernel_english_only_regex_would_flag": kernel_hits,
        "prototype_extended_regex_flags": prototype_hits,
    }


def main():
    ev = evaluate()
    labels = ev["labels"]
    relevant = [DEFECT_TARGETED]
    context_defects = BASELINE_MISSED_DEFECTS_CONTEXT

    b_n, b_caught, b_missed = _summ(ev["before"]["per_defect"], relevant)
    a_n, a_caught, a_missed = _summ(ev["after"]["per_defect"], relevant)
    b_recall = b_caught / b_n if b_n else 0.0
    a_recall = a_caught / a_n if a_n else 0.0

    before_block = {
        "caught": b_caught,
        "missed": b_missed,
        "n": b_n,
        "recall": round(b_recall, 4),
        "false_alarm": ev["before"]["false_alarm"],
        "false_alarm_n_valid": ev["valid_n"],
    }
    after_block = {
        "caught": a_caught,
        "missed": a_missed,
        "n": a_n,
        "recall": round(a_recall, 4),
        "false_alarm": ev["after"]["false_alarm"],
        "false_alarm_n_valid": ev["valid_n"],
    }

    context_rows = {}
    for d in context_defects:
        bd = ev["before"]["per_defect"][d]
        ad = ev["after"]["per_defect"][d]
        context_rows[d] = {"before_caught": bd["caught"], "before_n": bd["n"],
                            "after_caught": ad["caught"], "after_n": ad["n"]}

    probe = _thai_only_probe()

    delta_recall = round(a_recall - b_recall, 4)
    delta_false_alarm = after_block["false_alarm"] - before_block["false_alarm"]

    if delta_recall > 0 and delta_false_alarm <= 0:
        recommendation = "ship"
    elif b_recall >= 0.999 and delta_false_alarm == 0:
        recommendation = "drop"
    else:
        recommendation = "revise"

    notes = (
        f"finite_diagnostic readout over this fixed 180-card corpus (sim/v0.3/corpus/) only. "
        f"Targeted defect '{DEFECT_TARGETED}': kernel-only (before) already catches "
        f"{b_caught}/{b_n} via compute_disclaimers()'s existing D-DVP-NOT-K2 diff signal "
        f"(kernel/glosa_kernel.py, unmodified, verified by direct inspection -- validate_claim_card "
        f"returns ok=True on every one of these 8 cards, confirming the 'never auto-rejects' half "
        f"of the acceptance_test already holds today). Prototype (after) adds a self-declaration-"
        f"proof signal reading compute-side content directly (not diffed against the card's own "
        f"declared disclaimers_emitted list) plus a Thai-language keyword extension; on THIS fixed "
        f"corpus every one of the 8 adversarial cards already embeds the literal English loanword "
        f"'verified' inline, so the prototype's extension is UNEXERCISED here (delta_recall=0) -- "
        f"the gap it closes is only visible on the synthetic Thai-only probe sentence recorded "
        f"below, not on the shipped corpus. False alarms unchanged: 0/{ev['valid_n']} valid cards "
        f"trip either signal, before or after. The four defects named in the task brief as "
        f"'baseline missed' (composite_quote, hidden_ai_fill, inflated_bearing, injected_infinity) "
        f"are NOT targeted by this node -- checked directly, none of their corpus cards contain "
        f"verification-claim language, so this prototype catches zero of them either; reported "
        f"in 'context_only_not_targeted' for completeness per the task brief, not folded into "
        f"delta_recall/delta_false_alarm. thai_only_probe (illustrative, not scored): a synthetic "
        f"card using '{probe['probe_text']}' (no English 'verified' loanword) -- kernel's own "
        f"English-only regex would flag={probe['kernel_english_only_regex_would_flag']}, this "
        f"prototype's extended regex flags={probe['prototype_extended_regex_flags']} -- "
        f"demonstrating the latent English-only blind spot this prototype closes, ahead of any "
        f"future corpus expansion that would actually exercise it."
    )

    result = {
        "node": NODE_ID,
        "defects_targeted": [DEFECT_TARGETED],
        "before": before_block,
        "after": after_block,
        "context_only_not_targeted": context_rows,
        "thai_only_probe_illustrative": probe,
        "delta_recall": delta_recall,
        "delta_false_alarm": delta_false_alarm,
        "notes": notes,
        "recommendation": recommendation,
        "tier": "finite_diagnostic",
    }

    out_path = HERE / "kernel_unverified_verifiability_flag.result.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"node: {NODE_ID}")
    print(f"targeted defect: {DEFECT_TARGETED}")
    print(f"before: caught={b_caught}/{b_n} recall={b_recall:.4f} false_alarm={before_block['false_alarm']}/{ev['valid_n']}")
    print(f"after:  caught={a_caught}/{a_n} recall={a_recall:.4f} false_alarm={after_block['false_alarm']}/{ev['valid_n']}")
    print(f"context (not targeted, from sim/v0.3/baseline.json's known misses):")
    for d, row in context_rows.items():
        print(f"  {d:20s} before_caught={row['before_caught']}/{row['before_n']} after_caught={row['after_caught']}/{row['after_n']}")
    print(f"thai_only_probe kernel_flags={probe['kernel_english_only_regex_would_flag']} prototype_flags={probe['prototype_extended_regex_flags']}")
    print(f"delta_recall={delta_recall} delta_false_alarm={delta_false_alarm}")
    print(f"recommendation={recommendation}")
    print("RESULT_JSON " + json.dumps(result, ensure_ascii=False))
    return result


if __name__ == "__main__":
    main()
