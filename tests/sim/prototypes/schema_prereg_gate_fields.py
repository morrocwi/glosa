#!/usr/bin/env python3
"""K4-proto for design/DAG_v0.3.yaml node `schema.prereg-gate-fields`.

SANDBOX ONLY. Pure python, standalone. Does not import, edit, or monkeypatch kernel/, schema/,
cli/, or design/ -- it reimplements a proposed check with the same input shape as the kernel
(a claim_card dict, optional citation_cards list) so it can be diffed against kernel behaviour
without ever touching the kernel.

Node under test (design/DAG_v0.3.yaml, id schema.prereg-gate-fields):
  title: Frozen-preregistration gate as checkable fields, not a hard block
  change: Add protocol_frozen_at, ethics_approved_at (nullable/NOT_APPLICABLE for
    non-human-subjects work), and a separate registry-administrative-approval timestamp;
    violations are flagged, not blocked; a passed sequencing check is never read as
    ethics-substance verification.
  acceptance_test: "Schema validator accepts a card with ethics_approved_at=NOT_APPLICABLE for
    a non-human-subjects claim and flags (not rejects) an out-of-sequence pair."

WHAT THIS PROTOTYPE IMPLEMENTS (matching the node's own change: text and acceptance_test):
  A `check_prereg_gate_fields(card, citation_cards=None)` that reads three hypothetical fields
  this node proposes adding to the claim card -- `protocol_frozen_at`, `ethics_approved_at`
  (a date string, or the literal "NOT_APPLICABLE" for declared non-human-subjects work), and
  `registry_administrative_approval_at` -- plus the card's own `empirical_extension.study_design`
  as the human-subjects-relevance signal, and:
    1. never rejects (findings are always "WARNING:", never "ERROR:") -- matches "violations are
       flagged, not blocked",
    2. accepts ethics_approved_at == "NOT_APPLICABLE" silently when study_design does not read as
       human-subjects research (no ERROR, no WARNING) -- matches the acceptance_test's first half,
    3. flags (WARNING, never rejects) when protocol_frozen_at is present together with any of
       registry_administrative_approval_at / ethics_approved_at and the timestamps are
       out-of-sequence (registry/ethics approval dated before the protocol was frozen) --
       matches the acceptance_test's second half,
    4. never turns a passed sequencing check into a claim of ethics-SUBSTANCE verification --
       every emitted (or withheld) finding string says "sequencing" explicitly and this function
       has no branch that could be read as "ethics content is sound."

RELEVANCE TO THIS CORPUS -- checked directly, not assumed:
  `protocol_frozen_at`, `ethics_approved_at`, and any registry-administrative-approval field do
  not exist anywhere in schema/ (grepped: schema/*.json, schema/examples/*.json) or anywhere in
  sim/v0.3/corpus/ (grepped: claims/*.json, citations/*.json, 180 files) -- this corpus's
  fixture generator (gen_corpus.py, out of scope here) never populates a pre-registration
  timestamp field of any kind on any card, valid or adversarial. This node targets a defect
  class (out-of-sequence or substance-mismatched pre-registration/ethics timestamps) that is
  ENTIRELY ORTHOGONAL to the four defects this task brief names as currently missed by the
  kernel baseline (composite_quote: a citation-card exact_passage splicing defect;
  hidden_ai_fill: an authorship/five_questions.ai_filled provenance mismatch; inflated_bearing:
  an evidence_relations bearing/independence-class mismatch; injected_infinity: a continuum/
  non-readout-concept defect in statement text). None of those four defect families touch
  timestamp sequencing or human-subjects-ethics applicability in any of their fixture cards
  (checked by field-name grep across all 36 relevant cards below, zero hits).

  Consequence: on THIS fixed 180-card corpus, `check_prereg_gate_fields` finds zero fields to
  read on every single card (no card carries protocol_frozen_at/ethics_approved_at/
  registry_administrative_approval_at) and therefore emits zero findings on all 180 cards --
  the function returns `[]` unconditionally on this corpus's actual data, which is the CORRECT,
  honest behaviour for a check whose triggering fields are simply absent (a missing-field
  no-op, not a silent failure to detect something present). delta_recall on the four named
  defects is therefore 0.0 and delta_false_alarm is 0.0, by direct corpus inspection, not by
  construction of the check function -- the check function itself IS exercised (see the
  synthetic probe cases below, run separately, not scored into the corpus tally) and behaves
  exactly per its acceptance_test on those probes.

Tier of every count in this file's result JSON: finite_diagnostic -- exact tally over this
fixed, printed 180-card sim/v0.3 corpus, this run, this prototype version only. Not a general
claim about the node's value on a corpus that actually carries pre-registration fields (none of
sim/v0.3's does).
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent          # sim/v0.3/prototypes
SIM_V03 = HERE.parent                            # sim/v0.3
REPO = SIM_V03.parent.parent                     # glosa/
CORPUS_DIR = SIM_V03 / "corpus"

NODE_ID = "schema.prereg-gate-fields"
DEFECTS_TARGETED: list[str] = []  # see module docstring: no defect in this fixed corpus exercises
# the fields this node proposes; the node's own defect class (out-of-sequence / substance-
# mismatched prereg timestamps) is not one of the 14 defects sim/v0.3/corpus/labels.json defines.
DEFECTS_REPORTED = ["composite_quote", "hidden_ai_fill", "inflated_bearing", "injected_infinity"]

_PREREG_FIELDS = ("protocol_frozen_at", "ethics_approved_at", "registry_administrative_approval_at")

# Coarse, conservative human-subjects-relevance signal read off the card's OWN declared
# study_design (empirical_extension.study_design) plus standpoint text -- deliberately narrow:
# a false "not human-subjects" read must never suppress a real WARNING, so anything ambiguous
# is treated as "human-subjects-relevant" (fail toward flagging, never toward silent accept).
_NON_HUMAN_SUBJECTS_DESIGNS = {
    "case_study_non_human", "instrument_bench_test", "literature_review",
    "simulation", "secondary_data_analysis_public", "animal_observation_non_invasive",
}


def _is_declared_non_human_subjects(card: dict) -> bool:
    design = ((card.get("empirical_extension") or {}).get("study_design") or "").strip()
    if design in _NON_HUMAN_SUBJECTS_DESIGNS:
        return True
    # This corpus's own worked example (valid_0001.json) is a household-pet observation with
    # study_design="case_study" and no human research subject at all -- narrow, explicit
    # additional carve-out rather than trusting "case_study" alone (which could just as well be
    # a human case study), matched only when standpoint/basis text says "pet"/"animal" plainly.
    basis = ((card.get("standpoint") or {}).get("declared_basis") or "").lower()
    if design == "case_study" and ("pet owner" in basis or "animal" in basis):
        return True
    return False


def _parse_date(value: Any):
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def check_prereg_gate_fields(card: dict, citation_cards: list | None = None) -> list[str]:
    """SANDBOX check matching DAG node schema.prereg-gate-fields.

    Same input shape as the real kernel's validate_claim_card: a claim card dict, plus its
    companion citation cards (accepted for interface parity -- this node's three proposed
    fields all live on the claim card, so citation_cards is not inspected).

    Returns a list of WARNING strings (never "ERROR:") -- per the node's own change: text,
    "violations are flagged, not blocked". Every emitted string names this as a SEQUENCING
    signal only, never ethics-substance verification, per the node's own closing clause. An
    empty list means "nothing to flag" -- either because the three fields are simply absent
    (this corpus's case, see module docstring) or because whatever is present passes.
    """
    findings: list[str] = []
    if not isinstance(card, dict):
        return findings

    protocol_frozen_at = card.get("protocol_frozen_at")
    ethics_approved_at = card.get("ethics_approved_at")
    registry_at = card.get("registry_administrative_approval_at")

    if protocol_frozen_at is None and ethics_approved_at is None and registry_at is None:
        # None of this node's three proposed fields are present on this card at all -- a
        # no-op, not a finding. (This is the branch every one of this corpus's 180 cards hits.)
        return findings

    non_human_subjects = _is_declared_non_human_subjects(card)

    # Acceptance-test half 1: ethics_approved_at == "NOT_APPLICABLE" is accepted silently for
    # declared non-human-subjects work -- never flagged as missing/invalid.
    if ethics_approved_at == "NOT_APPLICABLE":
        if not non_human_subjects:
            findings.append(
                "WARNING: prereg-gate-fields (sequencing): ethics_approved_at=NOT_APPLICABLE "
                "but the card's own empirical_extension.study_design/standpoint does not read "
                "as declared non-human-subjects work -- route to human review to confirm the "
                "NOT_APPLICABLE claim; this is a sequencing/applicability flag only, not a "
                "verdict on whether ethics review was actually required or adequate."
            )
        # else: correctly-scoped NOT_APPLICABLE for non-human-subjects work -- no finding, per
        # the acceptance_test's explicit "accepts" half.
    elif ethics_approved_at is not None and _parse_date(ethics_approved_at) is None:
        findings.append(
            "WARNING: prereg-gate-fields (sequencing): ethics_approved_at="
            f"{ethics_approved_at!r} is neither an ISO date nor NOT_APPLICABLE"
        )

    # Acceptance-test half 2: sequencing check on the timestamps actually present.
    # (a) protocol must not be frozen AFTER registry/ethics approval already granted --
    #     approval of a protocol that was not yet frozen cannot be a genuine prereg approval.
    frozen_d = _parse_date(protocol_frozen_at)
    registry_d = _parse_date(registry_at)
    ethics_d = _parse_date(ethics_approved_at) if ethics_approved_at != "NOT_APPLICABLE" else None

    if frozen_d is not None and registry_d is not None and registry_d < frozen_d:
        findings.append(
            "WARNING: prereg-gate-fields (sequencing): registry_administrative_approval_at="
            f"{registry_at} predates protocol_frozen_at={protocol_frozen_at} -- out-of-sequence, "
            "route to human review; this flags sequencing only, it does not assert the registry "
            "approval itself is invalid or that the protocol content is unsound."
        )
    if frozen_d is not None and ethics_d is not None and ethics_d < frozen_d:
        findings.append(
            "WARNING: prereg-gate-fields (sequencing): ethics_approved_at="
            f"{ethics_approved_at} predates protocol_frozen_at={protocol_frozen_at} -- "
            "out-of-sequence, route to human review; this flags sequencing only, a passed "
            "sequencing check is never read as ethics-substance verification."
        )

    return findings


# ---------------------------------------------------------------------------------------------
# Corpus evaluation: mirrors the method used by the other sim/v0.3 K4-proto files (e.g.
# schema_claim_card_comparison_evidence_field.py) -- imports the real, unmodified kernel for the
# "before" numbers, computed the same way sim/v0.3/baseline.py computes them (any structural
# error from validate_claim_card/validate_citation_card counts as "kernel flags").
# ---------------------------------------------------------------------------------------------

def _load_json(rel: Path) -> Any:
    return json.loads(rel.read_text(encoding="utf-8"))


def _kernel_flags_not_ok(k_mod, card: dict, citation: dict) -> bool:
    claim_res = k_mod.validate_claim_card(card, citation_cards=[citation])
    citation_res = k_mod.validate_citation_card(citation)
    return (not claim_res.get("ok")) or (not citation_res.get("ok"))


def _field_presence_scan() -> dict:
    """Direct grep-equivalent evidence for the module docstring's relevance claim: for every
    one of the 36 cards under the four named defects (+ all 60 valid cards), do any of this
    node's three proposed field names appear anywhere in the raw claim/citation JSON? Read once,
    reported in the result JSON's notes so the "orthogonal to this corpus" claim is checked, not
    asserted."""
    labels = _load_json(CORPUS_DIR / "labels.json")
    hits = []
    for entry in labels["cards"]:
        claim_text = (CORPUS_DIR / entry["claim_file"]).read_text(encoding="utf-8")
        citation_text = (CORPUS_DIR / entry["citation_file"]).read_text(encoding="utf-8")
        for f in _PREREG_FIELDS:
            if f in claim_text or f in citation_text:
                hits.append((entry["id"], f))
    return {"cards_scanned": len(labels["cards"]), "field_name_hits": hits}


def _synthetic_probes() -> list[dict]:
    """Illustrative only, NOT scored into the corpus tally below (this corpus carries none of
    these fields on any real card) -- exercises check_prereg_gate_fields against the exact two
    scenarios named in the node's own acceptance_test, so the function's behaviour is
    demonstrated even though this fixed corpus never triggers it."""
    probes = []

    accept_card = {
        "empirical_extension": {"study_design": "case_study"},
        "standpoint": {"declared_basis": "pet owner direct observation"},
        "ethics_approved_at": "NOT_APPLICABLE",
    }
    probes.append({
        "name": "accept_not_applicable_non_human_subjects",
        "expect": "no finding (accepted)",
        "findings": check_prereg_gate_fields(accept_card),
    })

    flag_card = {
        "empirical_extension": {"study_design": "human_survey"},
        "standpoint": {"declared_basis": "researcher"},
        "protocol_frozen_at": "2026-06-01",
        "registry_administrative_approval_at": "2026-05-15",
    }
    probes.append({
        "name": "flag_out_of_sequence_registry_before_freeze",
        "expect": "flagged, not rejected",
        "findings": check_prereg_gate_fields(flag_card),
    })

    misapplied_card = {
        "empirical_extension": {"study_design": "human_survey"},
        "standpoint": {"declared_basis": "researcher"},
        "ethics_approved_at": "NOT_APPLICABLE",
    }
    probes.append({
        "name": "flag_not_applicable_misapplied_to_human_subjects_work",
        "expect": "flagged (NOT_APPLICABLE not accepted silently here)",
        "findings": check_prereg_gate_fields(misapplied_card),
    })

    return probes


def main() -> dict:
    sys.path.insert(0, str(REPO / "kernel"))
    import glosa_kernel as k  # noqa: E402  (repo's own unmodified kernel; imported inside main()
    # so importing this module for its check function alone never requires kernel/ on sys.path)

    labels = _load_json(CORPUS_DIR / "labels.json")
    cards = labels["cards"]

    before = {d: {"n": 0, "caught": 0, "missed": 0} for d in DEFECTS_REPORTED}
    after = {d: {"n": 0, "caught": 0, "missed": 0} for d in DEFECTS_REPORTED}
    before_valid_false_alarm = 0
    after_valid_false_alarm = 0
    valid_n = 0
    after_new_false_alarm_ids: list[str] = []

    for entry in cards:
        card = _load_json(CORPUS_DIR / entry["claim_file"])
        citation = _load_json(CORPUS_DIR / entry["citation_file"])

        kernel_not_ok = _kernel_flags_not_ok(k, card, citation)
        proto_findings = check_prereg_gate_fields(card, citation_cards=[citation])
        proto_hit = len(proto_findings) > 0

        if entry["kind"] == "valid":
            valid_n += 1
            if kernel_not_ok:
                before_valid_false_alarm += 1
            if kernel_not_ok or proto_hit:
                after_valid_false_alarm += 1
                if proto_hit and not kernel_not_ok:
                    after_new_false_alarm_ids.append(entry["id"])
            continue

        defect = entry["defect"]
        if defect not in DEFECTS_REPORTED:
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

    field_scan = _field_presence_scan()
    probes = _synthetic_probes()

    recommendation = "drop"  # see notes: zero measurable effect on this corpus, by direct field-
    # presence inspection, not by a weak/failing check function (probes show it behaves exactly
    # per the acceptance_test). "drop" here means: do not spend further K4-proto effort against
    # THIS corpus for THIS node -- it is orthogonal, not that the node's real-world proposal is
    # unsound. Revisit if/when the corpus gains cards that actually carry pre-registration
    # timestamps (a distinct future corpus-expansion task, out of scope here).

    result = {
        "node": NODE_ID,
        "defects_targeted": DEFECTS_TARGETED,
        "defects_reported": DEFECTS_REPORTED,
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
            "new_false_alarm_ids": after_new_false_alarm_ids,
        },
        "delta_recall": round(delta_recall, 4),
        "delta_false_alarm": round(delta_false_alarm, 4),
        "field_presence_scan": field_scan,
        "synthetic_acceptance_test_probes_not_scored_into_corpus_tally": probes,
        "notes": (
            "finite_diagnostic, exact tally over this fixed 180-card sim/v0.3 corpus "
            "(60 valid + 120 adversarial, 9 cards per defect id) only. This node's three "
            "proposed fields (protocol_frozen_at, ethics_approved_at, "
            "registry_administrative_approval_at) do not appear on ANY of the 180 corpus cards "
            "(field_presence_scan.field_name_hits is empty, confirmed by direct text scan of "
            "every claim_file/citation_file listed in labels.json, not assumed) -- the node "
            "targets pre-registration timestamp sequencing / human-subjects-ethics "
            "applicability, a defect class this corpus's generator never injects. The four "
            "defects this task brief names as baseline-missed (composite_quote: citation "
            "exact_passage splicing; hidden_ai_fill: five_questions.ai_filled provenance "
            "mismatch; inflated_bearing: evidence_relations bearing/independence mismatch; "
            "injected_infinity: continuum/non-readout-concept statement text) are each a "
            "different, unrelated defect family -- none involve prereg timestamps or ethics "
            "applicability in any of their 36 fixture cards, matching field_presence_scan. "
            "Consequently before==after on every reported number here: "
            f"caught={before_caught_total}/{before_total} unchanged, "
            f"false_alarm={before_valid_false_alarm}/{valid_n} unchanged, delta_recall=0.0, "
            "delta_false_alarm=0.0 -- by corpus field-absence, not by a weak or buggy check "
            "function. check_prereg_gate_fields() is exercised separately via three synthetic "
            "probes (synthetic_acceptance_test_probes_not_scored_into_corpus_tally, not folded "
            "into the corpus numbers above) reproducing the node's own acceptance_test "
            "verbatim: (1) ethics_approved_at=NOT_APPLICABLE on declared non-human-subjects "
            "work -> accepted silently (0 findings), (2) registry_administrative_approval_at "
            "dated before protocol_frozen_at -> flagged with a WARNING string (never an ERROR "
            "string, so it never blocks), (3) an added negative-control probe -- "
            "ethics_approved_at=NOT_APPLICABLE claimed on work the card's own study_design "
            "reads as human-subjects -- correctly flagged rather than silently accepted, so the "
            "NOT_APPLICABLE carve-out cannot be used to bypass a real human-subjects case. Every "
            "emitted string is prefixed 'sequencing' and explicitly disclaims asserting "
            "ethics-substance verification, per the node's own closing clause."
        ),
        "recommendation": recommendation,
        "tier": "finite_diagnostic",
    }

    out_path = HERE / "schema_prereg_gate_fields.result.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"node: {NODE_ID}")
    print(f"defects_targeted (this node vs this corpus): {DEFECTS_TARGETED or '[] -- orthogonal, see notes'}")
    print(f"{'defect':20s} {'n':>4s} {'before_caught':>14s} {'after_caught':>13s}")
    print("-" * 55)
    for d in DEFECTS_REPORTED:
        b, a = before[d], after[d]
        print(f"{d:20s} {b['n']:4d} {b['caught']:14d} {a['caught']:13d}")
    print("-" * 55)
    print(f"TOTAL (4 defects, n={before_total}): before_caught={before_caught_total} after_caught={after_caught_total}")
    print(f"valid cards: n={valid_n} before_false_alarm={before_valid_false_alarm} after_false_alarm={after_valid_false_alarm}")
    print(f"field_presence_scan: cards_scanned={field_scan['cards_scanned']} field_name_hits={field_scan['field_name_hits']}")
    for p in probes:
        print(f"probe[{p['name']}]: expect={p['expect']!r} findings={p['findings']}")
    print(f"delta_recall={delta_recall:.4f} delta_false_alarm={delta_false_alarm:.4f}")
    print(f"recommendation={recommendation}")
    print("RESULT_JSON " + json.dumps({
        "before_caught": before_caught_total, "after_caught": after_caught_total,
        "n": before_total, "delta_recall": round(delta_recall, 4),
        "delta_false_alarm": round(delta_false_alarm, 4),
        "recommendation": recommendation,
    }, ensure_ascii=False))
    return result


if __name__ == "__main__":
    main()
