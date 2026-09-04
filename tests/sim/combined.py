#!/usr/bin/env python3
"""K4-report combined run: kernel (unmodified) OR-ed with every prototype this report's
recommendation table marks "ship", over the same fixed 180-card sim/v0.3/corpus/.

Ship set (from sim/v0.3/report.md S4 table, decided in this task):
  - prototypes/kernel_gate_rules_taxonomy_i_z.py   -> check_gate_rules_taxonomy_i_z
  - prototypes/schema_claim_card_comparison_evidence_field.py
        -> check_claim_card_comparison_evidence_field

This script never edits kernel/, schema/, cli/, or design/ -- it only imports the sandbox
prototype modules (which themselves do not monkeypatch the kernel) and the kernel itself, and
reuses baseline.py's own defect_caught()/run_card() logic so the "kernel alone" half of this
count is derived the same way baseline.json was, not re-implemented differently.

Tier of every number this script prints: finite_diagnostic -- an exact tally over this one
fixed, printed 180-card corpus (sim/v0.3/corpus/), this run, these two prototype files as they
exist on disk right now. Not a general claim about kernel/prototype quality on any other corpus.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CORPUS_DIR = HERE / "corpus"
PROTO_DIR = HERE / "prototypes"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

sys.path.insert(0, str(PROTO_DIR))
from kernel_gate_rules_taxonomy_i_z import check_gate_rules_taxonomy_i_z  # noqa: E402
from schema_claim_card_comparison_evidence_field import (  # noqa: E402
    check_claim_card_comparison_evidence_field,
)

sys.path.insert(0, str(HERE))
from baseline import DEFECT_DISCLAIMER_SIGNAL, defect_caught, run_card  # noqa: E402

SHIP_CHECKS = [
    ("kernel.gate-rules-taxonomy-i-z", check_gate_rules_taxonomy_i_z),
    ("schema.claim-card-comparison-evidence-field", check_claim_card_comparison_evidence_field),
]


def load_json(rel):
    return json.loads((CORPUS_DIR / rel).read_text(encoding="utf-8"))


def prototype_flags(card, citation):
    """Return the union of findings from every ship-recommended prototype on this one card."""
    findings = []
    for name, fn in SHIP_CHECKS:
        try:
            hits = fn(card, citation_cards=[citation]) or []
        except TypeError:
            # a couple of prototype check_* signatures take (card,) only
            hits = fn(card) or []
        for h in hits:
            findings.append((name, h))
    return findings


def main():
    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in labels["defects"]}
    valid_n = 0
    valid_false_alarm = 0
    valid_false_alarm_ids = []
    new_false_alarm_from_prototypes = []
    missed_ids = {d: [] for d in labels["defects"]}

    for entry in cards:
        card = load_json(entry["claim_file"])
        citation = load_json(entry["citation_file"])
        kresult = run_card(entry)
        proto_hits = prototype_flags(card, citation)

        if entry["kind"] == "valid":
            valid_n += 1
            kernel_bad = (not kresult["claim_ok"]) or (not kresult["citation_ok"])
            proto_bad = len(proto_hits) > 0
            if kernel_bad or proto_bad:
                valid_false_alarm += 1
                valid_false_alarm_ids.append(entry["id"])
                if proto_bad and not kernel_bad:
                    new_false_alarm_from_prototypes.append(entry["id"])
        else:
            defect = entry["defect"]
            per_defect[defect]["n"] += 1
            caught = defect_caught(defect, kresult) or (len(proto_hits) > 0)
            if caught:
                per_defect[defect]["caught"] += 1
            else:
                per_defect[defect]["missed"] += 1
                missed_ids[defect].append(entry["id"])

    total_adv = sum(v["n"] for v in per_defect.values())
    total_caught = sum(v["caught"] for v in per_defect.values())
    total_missed = sum(v["missed"] for v in per_defect.values())
    recall = total_caught / total_adv if total_adv else 0.0
    false_alarm_rate = valid_false_alarm / valid_n if valid_n else 0.0

    out = {
        "ship_prototypes": [name for name, _ in SHIP_CHECKS],
        "corpus": {"n_valid": valid_n, "n_adversarial": total_adv, "n_total": valid_n + total_adv},
        "per_defect": per_defect,
        "valid": {
            "n": valid_n,
            "false_alarm": valid_false_alarm,
            "false_alarm_ids": valid_false_alarm_ids,
            "new_false_alarm_from_prototypes": new_false_alarm_from_prototypes,
        },
        "recall": recall,
        "false_alarm_rate": false_alarm_rate,
        "missed_defect_ids_sample": {d: ids[:3] for d, ids in missed_ids.items() if ids},
        "tier": "finite_diagnostic",
        "note": "kernel (unmodified) OR ship-recommended prototypes, over this fixed 180-card corpus only",
    }
    (HERE / "combined.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"{'defect':28s} {'n':>4s} {'caught':>7s} {'missed':>7s}")
    print("-" * 50)
    for d in labels["defects"]:
        row = per_defect[d]
        print(f"{d:28s} {row['n']:4d} {row['caught']:7d} {row['missed']:7d}")
    print("-" * 50)
    print(f"{'TOTAL adversarial':28s} {total_adv:4d} {total_caught:7d} {total_missed:7d}")
    print(f"valid cards: n={valid_n} false_alarm={valid_false_alarm}")
    print(f"recall={recall:.4f} false_alarm_rate={false_alarm_rate:.4f}")

    result_json = {
        "n_valid": valid_n,
        "n_adv": total_adv,
        "recall": round(recall, 4),
        "false_alarm_rate": round(false_alarm_rate, 4),
        "missed_defects": sorted([d for d, v in per_defect.items() if v["missed"] > 0]),
    }
    print("RESULT_JSON " + json.dumps(result_json, ensure_ascii=False))
    return result_json


if __name__ == "__main__":
    main()
