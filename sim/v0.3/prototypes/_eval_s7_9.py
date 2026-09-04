"""One-off eval harness for foundation_s7_9_intake_tier_flag.py against sim/v0.3/corpus.
Not part of the deliverable API -- just used to produce the before/after counts recorded in
foundation_s7_9_intake_tier_flag.result.json. Safe to delete; re-run any time to reproduce.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "kernel"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import glosa_kernel as k  # noqa: E402
from foundation_s7_9_intake_tier_flag import intake_tier_flag_check  # noqa: E402

CORPUS = ROOT / "sim" / "v0.3" / "corpus"
TARGET_DEFECTS = {"composite_quote", "hidden_ai_fill", "inflated_bearing", "injected_infinity"}

labels = json.loads((CORPUS / "labels.json").read_text(encoding="utf-8"))

before = {d: {"caught": 0, "missed": 0} for d in TARGET_DEFECTS}
after = {d: {"caught": 0, "missed": 0} for d in TARGET_DEFECTS}
before_fa = 0
after_fa = 0
n_valid = 0

for entry in labels["cards"]:
    claim = json.loads((CORPUS / entry["claim_file"]).read_text(encoding="utf-8"))
    citation = json.loads((CORPUS / entry["citation_file"]).read_text(encoding="utf-8"))
    defect = entry["defect"]

    kernel_result = k.validate_claim_card(claim, citation_cards=[citation], allow_no_jsonschema=True)
    kernel_flagged = bool(kernel_result.get("errors")) or bool(kernel_result.get("warnings"))

    proto_flags = intake_tier_flag_check(claim, citation_cards=[citation])
    combined_flagged = kernel_flagged or bool(proto_flags)

    if entry["kind"] == "valid":
        n_valid += 1
        if kernel_flagged:
            before_fa += 1
        if combined_flagged:
            after_fa += 1
    elif defect in TARGET_DEFECTS:
        if kernel_flagged:
            before[defect]["caught"] += 1
        else:
            before[defect]["missed"] += 1
        if combined_flagged:
            after[defect]["caught"] += 1
        else:
            after[defect]["missed"] += 1

print("n_valid", n_valid)
print("BEFORE (kernel only):")
for d in sorted(TARGET_DEFECTS):
    print(" ", d, before[d])
print(" false_alarm on valid:", before_fa)
print("AFTER (kernel + prototype):")
for d in sorted(TARGET_DEFECTS):
    print(" ", d, after[d])
print(" false_alarm on valid:", after_fa)
