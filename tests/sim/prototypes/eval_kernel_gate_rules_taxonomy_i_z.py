#!/usr/bin/env python3
"""Evaluation harness for the kernel.gate-rules-taxonomy-i-z SANDBOX prototype.

Runs the fixed sim/v0.3 corpus (labels.json) through:
  BEFORE = kernel only (validate_claim_card + validate_citation_card + compute_disclaimers diff,
           same "caught" logic as sim/v0.3/baseline.py, re-derived here rather than imported so
           this script has no side effect on baseline.py or its baseline.json).
  AFTER  = BEFORE OR the prototype's check_gate_rules_taxonomy_i_z(card) returning >=1 finding.

Reports caught/missed for the defect(s) this node targets (injected_infinity -- see this
prototype's own module docstring for why the scope is that one defect, not all four the task
brief lists as baseline-missed) and false alarms on the 60 valid cards, before vs after.

Writes nothing on its own; sim/v0.3/prototypes/kernel_gate_rules_taxonomy_i_z.result.json is
written by the caller (or by hand) from this script's printed RESULT_JSON line, per task
instructions. This script never touches kernel/, schema/, cli/, or design/.

Tier: finite_diagnostic -- exact tally over this fixed 180-card corpus, this run, this prototype
version. Not a general claim about kernel or prototype quality beyond this corpus.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SIM_DIR = HERE.parent
REPO = SIM_DIR.parent.parent
CORPUS_DIR = SIM_DIR / "corpus"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

sys.path.insert(0, str(HERE))
from kernel_gate_rules_taxonomy_i_z import check_gate_rules_taxonomy_i_z  # noqa: E402

DEFECTS_TARGETED = ["injected_infinity"]

# Same disclaimer-signal map as baseline.py, needed only so "kernel-flags-not-ok" is computed
# identically to the harness baseline (verifiable_no_procedure / disclaimer_missing rely on it;
# irrelevant to injected_infinity but kept for an apples-to-apples BEFORE number).
DEFECT_DISCLAIMER_SIGNAL = {
    "verifiable_no_procedure": "D-DVP-NOT-K2",
    "disclaimer_missing": "D-INDEPENDENCE",
}


def load_json(rel):
    return json.loads((CORPUS_DIR / rel).read_text(encoding="utf-8"))


def kernel_run(entry):
    card = load_json(entry["claim_file"])
    citation = load_json(entry["citation_file"])
    claim_res = k.validate_claim_card(card, citation_cards=[citation])
    citation_res = k.validate_citation_card(citation)
    computed_disclaimers = {d["id"] for d in k.compute_disclaimers(card)}
    declared_disclaimers = {d.get("id") for d in (card.get("disclaimers_emitted") or [])}
    disclaimer_gap = computed_disclaimers - declared_disclaimers
    return card, {
        "claim_ok": claim_res.get("ok"),
        "citation_ok": citation_res.get("ok"),
        "disclaimer_gap": sorted(disclaimer_gap),
    }


def kernel_flags_not_ok(defect, run_result):
    """Same semantics as baseline.py's defect_caught(): did the UNMODIFIED kernel raise
    anything at all attributable to this card (structural error, or its designated disclaimer
    gap)? This is the BEFORE signal."""
    signal_id = DEFECT_DISCLAIMER_SIGNAL.get(defect)
    if signal_id and signal_id in run_result["disclaimer_gap"]:
        return True
    if not run_result["claim_ok"] or not run_result["citation_ok"]:
        return True
    return False


def main():
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    before = {"caught": 0, "missed": 0, "n": 0}
    after = {"caught": 0, "missed": 0, "n": 0}
    before_false_alarm = 0
    after_false_alarm = 0
    valid_n = 0
    missed_ids_before = []
    missed_ids_after = []
    after_new_false_alarm_ids = []

    for entry in cards:
        card, run_result = kernel_run(entry)
        kernel_flag = kernel_flags_not_ok(entry.get("defect", ""), run_result)
        proto_findings = check_gate_rules_taxonomy_i_z(card)
        proto_flag = len(proto_findings) > 0
        combined_flag = kernel_flag or proto_flag

        if entry["kind"] == "valid":
            valid_n += 1
            if kernel_flag:
                before_false_alarm += 1
            if combined_flag:
                after_false_alarm += 1
                if not kernel_flag:
                    after_new_false_alarm_ids.append(entry["id"])
        else:
            defect = entry["defect"]
            if defect not in DEFECTS_TARGETED:
                continue  # only report the defect(s) this node targets, per task instructions
            before["n"] += 1
            after["n"] += 1
            if kernel_flag:
                before["caught"] += 1
            else:
                before["missed"] += 1
                missed_ids_before.append(entry["id"])
            if combined_flag:
                after["caught"] += 1
            else:
                after["missed"] += 1
                missed_ids_after.append(entry["id"])

    out = {
        "defects_targeted": DEFECTS_TARGETED,
        "before": {
            "n": before["n"],
            "caught": before["caught"],
            "missed": before["missed"],
            "false_alarm": before_false_alarm,
            "false_alarm_of_valid_n": valid_n,
        },
        "after": {
            "n": after["n"],
            "caught": after["caught"],
            "missed": after["missed"],
            "false_alarm": after_false_alarm,
            "false_alarm_of_valid_n": valid_n,
            "new_false_alarm_ids": after_new_false_alarm_ids,
        },
        "missed_ids_before_sample": missed_ids_before[:5],
        "missed_ids_after_sample": missed_ids_after[:5],
        "tier": "finite_diagnostic",
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print("RESULT_JSON " + json.dumps(out, ensure_ascii=False))
    return out


if __name__ == "__main__":
    main()
