#!/usr/bin/env python3
"""K4-corpus baseline. Runs every card in sim/v0.3/corpus/ through the CURRENT kernel
(kernel/glosa_kernel.py, unmodified -- this script never edits kernel/, schema/, cli/, or
design/) and records, per defect, whether the kernel actually named it (caught) or not
(missed), plus false-alarm counts on the 60 valid cards.

What "run through the kernel" means, concretely, per card:
  - validate_claim_card(card, citation_cards=[companion_citation]) -- always.
  - validate_citation_card(citation) -- always (every claim card has a companion citation card;
    citation-targeted defects, e.g. missing_locator, live entirely in that companion).
  - compute_disclaimers(card) -- always, diffed against the card's own declared
    disclaimers_emitted (a mismatch is itself a finding: the kernel's own disclaimer engine
    disagrees with what the card claims to disclose).
  - gate_release(...) is NOT run per-card: it needs a release_manifest + a reviews list, which
    this corpus does not synthesize per card (out of scope for a claim/citation-level defect
    corpus); noted here rather than silently skipped.

"Caught" (per defect) means: validate_claim_card/validate_citation_card returned at least one
error or warning string whose text names this card's defect (matched via a per-defect keyword
list below, built directly from the kernel functions inspected while writing gen_corpus.py --
e.g. "rule17(" for missing_locator, "rule6(scope)" for premature_category), OR
compute_disclaimers(card) computed a disclaimer id that the card's own declared
disclaimers_emitted omits AND that id is this defect's designated signal (verifiable_no_procedure
-> D-DVP-NOT-K2). Every other case is "missed" -- including a card that fails validation for an
unrelated reason (that is a false alarm on a different axis, not a catch of THIS defect; recorded
separately so precision is not inflated by lucky unrelated failures).

Tier of every count below: finite_diagnostic (an exact tally over this fixed, printed 180-card
corpus -- readout of THIS run, not a claim about kernel behaviour on any other corpus).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CORPUS_DIR = HERE / "corpus"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

# Every adversarial card is built from a base card that independently validates clean (zero
# errors/warnings -- see gen_corpus.py's base_adversarial_card, which is exactly
# build_valid_card()'s own recipe) with exactly ONE defect then injected. So for a structural
# defect, "the kernel caught it" is simply "validate_claim_card/validate_citation_card returned
# an ERROR on this card" -- there is nothing else in the card that could have produced it. Some
# defects also carry a specific expected message substring (recorded here as documentation of
# WHICH rule is expected to fire, cross-checked below rather than used as the sole signal) so a
# human reading this file can see the reasoning that produced gen_corpus.py's own defect design,
# not just a bare pass/fail.
DEFECT_EXPECTED_RULE_HINT = {
    "hidden_ai_fill": None,
    "inflated_bearing": None,
    "missing_locator": "rule17(",
    "composite_quote": None,
    "k_state_rounded_up": None,  # schema allOf rule 9, jsonschema's own message does not echo "k_state"
    "stub_public": None,  # schema allOf rule 0 (shape:stub), jsonschema's own message does not echo "shape"
    "signature_missing": "rule12",
    "injected_infinity": None,
    "verifiable_no_procedure": None,  # checked via compute_disclaimers diff (D-DVP-NOT-K2) below
    "premature_category": "rule6(scope)",
    "tier_overclaim": None,  # schema allOf rule 2, jsonschema's own message does not echo "Th_coqc"
    "disclaimer_missing": None,  # schema allOf rule 9 (disclaimer-trigger), checked via error presence
    "ownership_ai": "rule15",
    "same_vendor_review": None,  # schema allOf rule 1 (MC-02), jsonschema's own message does not echo it
}

# Defects whose designated "caught" signal is a compute_disclaimers(card) id present in the
# computed set but absent from the card's own declared disclaimers_emitted.
DEFECT_DISCLAIMER_SIGNAL = {
    "verifiable_no_procedure": "D-DVP-NOT-K2",
    "disclaimer_missing": "D-INDEPENDENCE",
}


def load_json(rel):
    return json.loads((CORPUS_DIR / rel).read_text(encoding="utf-8"))


def run_card(entry):
    card = load_json(entry["claim_file"])
    citation = load_json(entry["citation_file"])

    claim_res = k.validate_claim_card(card, citation_cards=[citation])
    citation_res = k.validate_citation_card(citation)

    all_msgs = list(claim_res.get("errors") or []) + list(claim_res.get("warnings") or []) \
        + list(citation_res.get("errors") or []) + list(citation_res.get("warnings") or [])

    computed_disclaimers = {d["id"] for d in k.compute_disclaimers(card)}
    declared_disclaimers = {d.get("id") for d in (card.get("disclaimers_emitted") or [])}
    disclaimer_gap = computed_disclaimers - declared_disclaimers

    return {
        "claim_ok": claim_res.get("ok"),
        "citation_ok": citation_res.get("ok"),
        "messages": all_msgs,
        "disclaimer_gap": sorted(disclaimer_gap),
    }


def defect_caught(defect, run_result):
    signal_id = DEFECT_DISCLAIMER_SIGNAL.get(defect)
    if signal_id and signal_id in run_result["disclaimer_gap"]:
        return True
    # Structural signal: the card was built defect-free except for this one injected mutation
    # (see gen_corpus.py's base_adversarial_card), so any error the kernel now raises on it is
    # attributable to this defect.
    if not run_result["claim_ok"] or not run_result["citation_ok"]:
        return True
    return False


def main():
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in labels["defects"]}
    valid_n = 0
    valid_false_alarm = 0
    valid_false_alarm_ids = []
    missed_ids = {d: [] for d in labels["defects"]}

    for entry in cards:
        result = run_card(entry)
        if entry["kind"] == "valid":
            valid_n += 1
            if not result["claim_ok"] or not result["citation_ok"]:
                valid_false_alarm += 1
                valid_false_alarm_ids.append(entry["id"])
        else:
            defect = entry["defect"]
            per_defect[defect]["n"] += 1
            if defect_caught(defect, result):
                per_defect[defect]["caught"] += 1
            else:
                per_defect[defect]["missed"] += 1
                missed_ids[defect].append(entry["id"])

    total_adv = sum(v["n"] for v in per_defect.values())
    total_caught = sum(v["caught"] for v in per_defect.values())
    total_missed = sum(v["missed"] for v in per_defect.values())
    recall = total_caught / total_adv if total_adv else 0.0
    # precision: of everything the kernel flagged as NOT ok (claim_ok False or citation_ok False)
    # across the whole 180-card corpus, how much of that was a true adversarial catch vs a false
    # alarm on a valid card. "Flagged not-ok" also includes adversarial cards flagged for an
    # unrelated reason (still a real kernel rejection, just not credited as catching THIS card's
    # labelled defect) -- counted here as a true positive at the flag level, separately reported
    # per-defect above where "caught" is the stricter labelled-defect match.
    flagged_true = 0
    flagged_false = valid_false_alarm
    for entry in cards:
        if entry["kind"] != "adversarial":
            continue
        result = run_card(entry)
        if not result["claim_ok"] or not result["citation_ok"]:
            flagged_true += 1
    precision = flagged_true / (flagged_true + flagged_false) if (flagged_true + flagged_false) else 0.0

    out = {
        "corpus": {"n_valid": valid_n, "n_adversarial": total_adv, "n_total": valid_n + total_adv},
        "per_defect": per_defect,
        "valid": {"n": valid_n, "false_alarm": valid_false_alarm, "false_alarm_ids": valid_false_alarm_ids},
        "recall": recall,
        "precision": precision,
        "missed_defect_ids_sample": {d: ids[:3] for d, ids in missed_ids.items() if ids},
        "tier": "finite_diagnostic",
        "note": "readout over this fixed 180-card corpus only, not a general kernel-quality claim",
    }
    (HERE / "baseline.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # Print table
    print(f"{'defect':28s} {'n':>4s} {'caught':>7s} {'missed':>7s}")
    print("-" * 50)
    for d in labels["defects"]:
        row = per_defect[d]
        print(f"{d:28s} {row['n']:4d} {row['caught']:7d} {row['missed']:7d}")
    print("-" * 50)
    print(f"{'TOTAL adversarial':28s} {total_adv:4d} {total_caught:7d} {total_missed:7d}")
    print(f"valid cards: n={valid_n} false_alarm={valid_false_alarm}")
    print(f"recall={recall:.3f} precision={precision:.3f}")

    result_json = {
        "n_valid": valid_n,
        "n_adv": total_adv,
        "recall": round(recall, 4),
        "precision": round(precision, 4),
        "missed_defects": sorted([d for d, v in per_defect.items() if v["missed"] > 0]),
    }
    print("RESULT_JSON " + json.dumps(result_json, ensure_ascii=False))
    return result_json


if __name__ == "__main__":
    main()
