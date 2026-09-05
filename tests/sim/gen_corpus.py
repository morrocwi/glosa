#!/usr/bin/env python3
"""K4-corpus generator.

Derives a small corpus (<=400 cards, no embeddings, no external calls) of claim_card /
citation_card variants from schema/examples/claim_card.example.json and
schema/examples/citation_card.example.json:

  (a) 60 VALID variants -- legally varied tier / claim_type / genre / k_state / evidence
      relations / responsibility-ownership presence, each constructed so it satisfies every
      kernel-checked rule (the disclaimers_emitted block is filled in by calling the kernel's
      own compute_disclaimers() rather than hand-guessed, so a valid card is valid by
      construction, not by luck).

  (b) 120 ADVERSARIAL variants, each carrying exactly ONE labelled defect from the fixed list
      in DEFECTS below (one defect per card -- never two defects stacked on the same card, so
      baseline.py's per-defect caught/missed count is never confounded by a second violation).

This is a READOUT-construction script, not a claim generator: everything here is a finite,
inspectable JSON fixture; whether the CURRENT kernel actually catches each defect is not
decided here -- that is exactly what sim/v0.3/baseline.py measures empirically by running
these cards through kernel/glosa_kernel.py. Tier of any number this script prints: finite_diagnostic
(counts over a fixed, printed corpus), never Th_coqc / Dr.

Writes:
  sim/v0.3/corpus/claims/*.json      -- claim_card payloads
  sim/v0.3/corpus/citations/*.json   -- citation_card payloads (one per claim, plus a few
                                         citation-only adversarial variants for citation-card
                                         defects)
  sim/v0.3/corpus/labels.json        -- {cards: [{id, claim_file, citation_file, kind,
                                         defect|null, expect_catch|null, note}]}
"""
import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent  # .../glosa
CORPUS_DIR = HERE / "corpus"
CLAIMS_DIR = CORPUS_DIR / "claims"
CITATIONS_DIR = CORPUS_DIR / "citations"

sys.path.insert(0, str(REPO / "kernel"))
import glosa_kernel as k  # noqa: E402

BASE_CLAIM = json.loads((REPO / "schema/examples/claim_card.example.json").read_text(encoding="utf-8"))
BASE_CITATION = json.loads((REPO / "schema/examples/citation_card.example.json").read_text(encoding="utf-8"))

TIERS = ["Th_coqc", "finite_diagnostic", "fit_calibrated", "Dr", "definition", "Open"]
K_STATES = ["K0", "K1", "K2", "K3"]
CLAIM_TYPES = [
    "EMPIRICAL", "FORMAL", "INTERPRETIVE", "NORMATIVE",
    "CONVENTIONAL_LEGAL", "DECISION", "SOCIAL", "HUMAN_PARTICIPANT",
]
GENRES = [
    "conceptual", "empirical_quant", "empirical_qual_practice", "case_study", "formal_proof",
    "systematic_review", "design_science", "archival", "position_reply", "MIXED_GENRE",
]
BEARINGS = ["SUPPORTS", "CHALLENGES", "NEUTRAL", "UNRESOLVED"]

# -------------------------------------------------------------------------------------------
# The 14 defect ids this corpus injects, one per adversarial card. `expect_catch` is this
# generator's own PREDICTION (based on reading kernel/glosa_kernel.py + schema allOf blocks
# before writing this file) of whether the CURRENT kernel names the defect -- baseline.py does
# NOT trust this field, it independently re-derives caught/missed by actually running the
# kernel. It is recorded here only so a human reading labels.json can see the generator's own
# prior, and compare it against baseline.json's measured outcome.
# -------------------------------------------------------------------------------------------
DEFECTS = [
    "hidden_ai_fill",
    "hidden_ai_fill_unmarked",
    "inflated_bearing",
    "missing_locator",
    "composite_quote",
    "k_state_rounded_up",
    "stub_public",
    "signature_missing",
    "injected_infinity",
    "verifiable_no_procedure",
    "premature_category",
    "tier_overclaim",
    "disclaimer_missing",
    "ownership_ai",
    "same_vendor_review",
]
N_ADVERSARIAL = 120
N_VALID = 60


def deep_merge(base, patch):
    out = copy.deepcopy(base)
    for key, val in patch.items():
        if isinstance(val, dict) and isinstance(out.get(key), dict):
            out[key] = deep_merge(out[key], val)
        else:
            out[key] = copy.deepcopy(val)
    return out


def evidence_relation(independence_class, bearing="SUPPORTS", ev_id="ev-cat-001", review_mode="MAKER_SELF_CHECK", citation_ref="cite-cat-obs-001"):
    return {
        "evidence_id": ev_id,
        "bearing": bearing,
        "independence_class": independence_class,
        "citation_ref": citation_ref,
        "strength": "generated fixture",
        "review_mode": review_mode,
        "route_id": None,
        "asserted_by": "founder",
        "date": "2026-09-04",
        "notes": "",
    }


def min_independence_for(tier, k_state):
    """Smallest single independence_class that satisfies BOTH the tier-witness rule and the
    k_state-evidence rule for the given (tier, k_state) pair, per schema/claim_card.schema.json's
    allOf rules 2/3/4/9 (read directly out of the schema file, not guessed)."""
    need_i5 = k_state in ("K2", "K3")
    need_i4plus = tier in ("Th_coqc", "finite_diagnostic")
    need_i3plus = k_state == "K1"
    if need_i5:
        return "I5"
    if need_i4plus:
        return "I4"
    if need_i3plus:
        return "I3"
    return "I1"


def make_claim_id(kind, idx):
    """claim_card.schema.json requires claim_id to match ^GLOSA-CC-[0-9]{8}-[0-9]{4}$ -- an
    8-digit date-like segment plus a 4-digit sequence, no free-text suffix room. `kind` (0 for
    valid, 1 for adversarial) plus idx is folded into the 4-digit sequence so ids stay unique."""
    seq = kind * 5000 + idx
    return f"GLOSA-CC-20260905-{seq:04d}"


def make_citation_id(seq):
    """citation_card.schema.json requires id to match ^cite-[a-z0-9-]+-[0-9]{3}$."""
    return f"cite-corpus-{seq:03d}"


def build_valid_card(idx, tier, k_state, claim_type, genre, bearing, resp_present):
    ic = min_independence_for(tier, k_state)
    patch = {
        "claim_id": make_claim_id(0, idx),
        "tier": tier,
        "k_state": k_state,
        "claim_type": claim_type,
        "genre": genre,
        "status": "Draft",
        "five_questions": {
            "tested": {
                "evidence_relations": [evidence_relation(ic, bearing=bearing)],
            }
        },
        "scope": {
            "generalization_claimed": "none",
            "evidence_scope": "one household, one cat, 14 days",
            "claim_scope": "one household, one cat, 14 days",
        },
    }
    if not resp_present:
        patch["responsibility"] = None
    card = deep_merge(BASE_CLAIM, patch)
    if not resp_present:
        card.pop("responsibility", None)
    # Fill disclaimers_emitted from the kernel's own compute_disclaimers -- by construction this
    # can never mismatch the disclaimer-trigger allOf block (schema rule described at allOf[9]).
    card["disclaimers_emitted"] = k.compute_disclaimers(card)
    return card


def base_adversarial_card(idx, defect):
    """A structurally-valid Draft claim_card (same recipe as build_valid_card, tier=Dr/K0) that
    the defect injector then mutates. Starting from a clean base means each adversarial card
    carries exactly the one injected defect, never an incidental second violation."""
    card = build_valid_card(idx, tier="Dr", k_state="K0", claim_type="EMPIRICAL", genre="case_study", bearing="SUPPORTS", resp_present=True)
    card["claim_id"] = make_claim_id(1, idx)
    return card


def inject_defect(card, citation, defect):
    """Mutate (card, citation) in place to carry exactly one instance of `defect`. Returns
    (card, citation, artifact_under_test) where artifact_under_test is 'claim' or 'citation' --
    which validator baseline.py should run to look for this defect."""
    if defect == "hidden_ai_fill":
        # S4b fix (v0.4): five_questions.seen.ai_assisted_fields NAMES a field that had AI
        # involvement in drafting its seen-recorded content, while every five_questions.ai_filled
        # value still reads a not-applicable placeholder -- the two disclosure records contradict
        # each other. This is the structural marker kernel rule27 (_hidden_ai_fill_error,
        # kernel/glosa_kernel.py:881) actually checks -- see design/FOUNDATION_v0.6_PATCH.md K-C2.
        # Prior to this pass, this generator only injected prose text with no ai_assisted_fields
        # marker at all, so rule27 was never exercised (S4b gap) -- that marker-less variant is
        # kept as the separate `hidden_ai_fill_unmarked` class below so the gap stays visible.
        card["five_questions"]["seen"]["ai_assisted_fields"] = ["access_model"]
        card["five_questions"]["seen"]["access_model"] = (
            "[AI-DRAFTED SUMMARY, presented as the household's own retained observation log] "
            "the cat reliably avoids litter boxes placed far from its resting area"
        )
        card["five_questions"]["ai_filled"]["retained_record_route"] = "none identified"
        return card, citation, "claim"

    if defect == "hidden_ai_fill_unmarked":
        # The pre-v0.4 variant of hidden_ai_fill: AI-drafted text is presented inside
        # five_questions.seen as if it were the human's own retained record, while ai_filled
        # claims nothing was AI-filled AND seen.ai_assisted_fields is left empty/absent -- so
        # kernel rule27 (a structural marker check, not a prose scan) has no marker to read and
        # cannot fire. This is the S4b gap made explicit as its own labelled defect class, not a
        # silently-fixed bug: it documents that a hidden-AI-fill with no self-disclosed marker at
        # all still slips through today, by design of what rule27 checks (marker vs marker,
        # never seen-vs-ai_filled prose content).
        card["five_questions"]["seen"]["access_model"] = (
            "[AI-DRAFTED SUMMARY, presented as the household's own retained observation log] "
            "the cat reliably avoids litter boxes placed far from its resting area"
        )
        card["five_questions"]["ai_filled"]["retained_record_route"] = "none identified"
        return card, citation, "claim"

    if defect == "inflated_bearing":
        # The only "evidence" is the claim's own lineage/context source (its own prior draft),
        # yet it is marked SUPPORTS at low independence -- inflating an own-context source into
        # apparent corroboration. No structural field distinguishes "own-lineage" from "external".
        card["five_questions"]["tested"]["evidence_relations"] = [
            evidence_relation("I1", bearing="SUPPORTS", ev_id="ev-own-lineage-001",
                               citation_ref="cite-cat-obs-001", review_mode="MAKER_SELF_CHECK")
        ]
        card["five_questions"]["tested"]["evidence_relations"][0]["notes"] = (
            "own-lineage source (this claim's own earlier draft / context note), marked SUPPORTS"
        )
        card["disclaimers_emitted"] = k.compute_disclaimers(card)
        return card, citation, "claim"

    if defect == "missing_locator":
        # A FETCHED, non-CANDIDATE citation card with no page/line locator -- kernel rule 17
        # (_citation_source_first_errors) should catch this on the CITATION card.
        citation["status"] = "VERIFIED"
        citation["fetch_status"] = "FETCHED"
        citation["page_or_locator"] = ""
        citation["line_or_paragraph"] = ""
        return card, citation, "citation"

    if defect == "composite_quote":
        # exact_passage stitches two non-adjacent spans with an ellipsis as if it were one
        # continuous verbatim quotation. No kernel check inspects exact_passage's own text shape.
        citation["exact_passage"] = "ทำไมแมวเยี่ยว … ไม่เป็นที่ (สรุปรวมจากสองช่วงที่ไม่ติดกัน)"
        citation["status"] = "VERIFIED"
        citation["fetch_status"] = "FETCHED"
        return card, citation, "citation"

    if defect == "k_state_rounded_up":
        # K1 claimed with no I3+ evidence_relation and no bounded-exception marker -- schema
        # allOf rule 9 should hard-fail this.
        card["k_state"] = "K1"
        card["five_questions"]["tested"]["evidence_relations"] = [evidence_relation("I1")]
        card["disclaimers_emitted"] = k.compute_disclaimers(card)
        return card, citation, "claim"

    if defect == "stub_public":
        # shape:stub cannot advance status past Draft -- schema allOf[0] should hard-fail this.
        card["shape"] = "stub"
        card["status"] = "Approved-for-Live"
        return card, citation, "claim"

    if defect == "signature_missing":
        # lens_translation.lens_ref set but hypothesis_world.signature absent -- kernel rule 12
        # (_lens_unsigned_error) should hard-fail this.
        card["lens_translation"]["lens_ref"] = "LENS-GENESIS-DELTA-R"
        card["hypothesis_world"].pop("signature", None)
        return card, citation, "claim"

    if defect == "injected_infinity":
        # A continuum/non-readout concept (infinite / exactly zero / limit->0) asserted as an
        # observed readout -- the information-discrete-math contaminated-concept guard is not
        # part of glosa_kernel's own text scans, so this is expected to slip through.
        card["statement"]["text"] = (
            "แมวไม่ถ่ายปัสสาวะนอกกระบะทรายเลยแม้แต่ครั้งเดียว ความน่าจะเป็นที่จะเกิดขึ้นคือศูนย์แท้ (exactly zero), "
            "เป็นค่า infinite reliability ของพฤติกรรมนี้"
        )
        return card, citation, "claim"

    if defect == "verifiable_no_procedure":
        # Statement text claims the finding is "verified" while independence never reaches I5 and
        # no reproduction procedure is named. compute_disclaimers's own D-DVP-NOT-K2 best-effort
        # text scan is the only kernel signal that could catch this.
        card["statement"]["text"] = (
            "แมวไม่ถ่ายปัสสาวะในกระบะทรายเมื่ออยู่ไกลที่นอน — ข้อสรุปนี้ verified แล้วโดยไม่มีขั้นตอนทำซ้ำที่ระบุไว้"
        )
        card["five_questions"]["tested"]["evidence_relations"] = [evidence_relation("I1")]
        # Deliberately do NOT recompute disclaimers_emitted here: the card's own declared list
        # is left as the (stale) one computed before the "verified" text was inserted, so it
        # omits the D-DVP-NOT-K2 disclaimer the new text now warrants -- that omission, caught
        # by diffing against a fresh compute_disclaimers(card) call, is this defect's signal.
        return card, citation, "claim"

    if defect == "premature_category":
        # generalization_claimed=population_claim asserted directly off n=1 (single-subject)
        # evidence -- schema rule 6 (_scope_exceeds_evidence) branch (b) should hard-fail this.
        card["scope"]["generalization_claimed"] = "population_claim"
        card["scope"]["evidence_scope"] = "one household, one cat (n=1), 14 days"
        card["scope"]["claim_scope"] = "all domestic cats"
        return card, citation, "claim"

    if defect == "tier_overclaim":
        # tier Th_coqc with only I3 (cross-vendor AI corroboration, never a mechanical/proof
        # witness) -- schema rule 2 should hard-fail this (fail_th_coqc_no_witness's own case).
        card["tier"] = "Th_coqc"
        card["five_questions"]["tested"]["evidence_relations"] = [evidence_relation("I3")]
        card["disclaimers_emitted"] = k.compute_disclaimers(card)
        return card, citation, "claim"

    if defect == "disclaimer_missing":
        # max independence I1 (I0-I2 band) but disclaimers_emitted omits D-INDEPENDENCE -- schema
        # allOf[9] disclaimer-trigger check should hard-fail this (fail_missing_disclaimer's case).
        card["five_questions"]["tested"]["evidence_relations"] = [evidence_relation("I1")]
        card["disclaimers_emitted"] = [d for d in k.compute_disclaimers(card) if d["id"] != "D-INDEPENDENCE"]
        return card, citation, "claim"

    if defect == "ownership_ai":
        # responsibility.ownership.question = "ai" -- kernel rule 15 (_responsibility_error_for_card)
        # should hard-fail this.
        card["responsibility"]["ownership"]["question"] = "ai"
        return card, citation, "claim"

    if defect == "same_vendor_review":
        # independent_check.status PASSED while independence_class is I1 (same model/session) --
        # schema allOf rule 1 (MC-02) should hard-fail this (fail_same_model_review's case).
        card["independent_check"]["status"] = "PASSED"
        card["independent_check"]["independence_class"] = "I1"
        card["independent_check"]["checker_id"] = "founder-session-2"
        card["independent_check"]["maker_id"] = "founder"
        card["independent_check"]["approver_id"] = "founder"
        return card, citation, "claim"

    raise ValueError(f"unknown defect {defect!r}")


_citation_seq = [0]


def make_citation_for(claim_id):
    cit = copy.deepcopy(BASE_CITATION)
    _citation_seq[0] += 1
    cit["id"] = make_citation_id(_citation_seq[0])
    cit["claim_ref"] = claim_id
    return cit


def main():
    CLAIMS_DIR.mkdir(parents=True, exist_ok=True)
    CITATIONS_DIR.mkdir(parents=True, exist_ok=True)
    for f in list(CLAIMS_DIR.glob("*.json")) + list(CITATIONS_DIR.glob("*.json")):
        f.unlink()

    labels = {"n_valid": N_VALID, "n_adversarial": N_ADVERSARIAL, "defects": DEFECTS, "cards": []}

    # --- (a) 60 VALID variants ------------------------------------------------------------
    combos = []
    for tier in TIERS:
        for k_state in K_STATES:
            combos.append((tier, k_state))
    # 6 tiers x 4 k_states = 24 (tier,k_state) pairs; cross with claim_type/genre/bearing/resp
    # cycling to reach exactly 60, each field cycled independently so no two cards are identical.
    idx = 0
    for i in range(N_VALID):
        tier, k_state = combos[i % len(combos)]
        claim_type = CLAIM_TYPES[i % len(CLAIM_TYPES)]
        genre = GENRES[i % len(GENRES)]
        bearing = BEARINGS[i % len(BEARINGS)]
        resp_present = (i % 2 == 0)
        idx += 1
        card = build_valid_card(idx, tier, k_state, claim_type, genre, bearing, resp_present)
        cit = make_citation_for(card["claim_id"])
        card["related_citation_cards"] = [cit["id"]]
        card["five_questions"]["tested"]["evidence_relations"][0]["citation_ref"] = cit["id"]
        claim_file = f"valid_{idx:04d}.json"
        cit_file = f"valid_{idx:04d}.json"
        (CLAIMS_DIR / claim_file).write_text(json.dumps(card, ensure_ascii=False, indent=1), encoding="utf-8")
        (CITATIONS_DIR / cit_file).write_text(json.dumps(cit, ensure_ascii=False, indent=1), encoding="utf-8")
        labels["cards"].append({
            "id": card["claim_id"],
            "kind": "valid",
            "defect": None,
            "claim_file": f"claims/{claim_file}",
            "citation_file": f"citations/{cit_file}",
            "artifact_under_test": "claim",
        })

    # --- (b) 120 ADVERSARIAL variants, one defect each -------------------------------------
    n_defects = len(DEFECTS)
    base_n = N_ADVERSARIAL // n_defects
    extra = N_ADVERSARIAL % n_defects
    counts = {d: base_n + (1 if i < extra else 0) for i, d in enumerate(DEFECTS)}
    assert sum(counts.values()) == N_ADVERSARIAL

    aidx = 0
    for defect in DEFECTS:
        for j in range(counts[defect]):
            aidx += 1
            card = base_adversarial_card(aidx, defect)
            cit = make_citation_for(card["claim_id"])
            card["related_citation_cards"] = [cit["id"]]
            card["five_questions"]["tested"]["evidence_relations"][0]["citation_ref"] = cit["id"]
            card, cit, artifact = inject_defect(card, cit, defect)
            claim_file = f"adv_{defect}_{j+1:03d}.json"
            cit_file = f"adv_{defect}_{j+1:03d}.json"
            (CLAIMS_DIR / claim_file).write_text(json.dumps(card, ensure_ascii=False, indent=1), encoding="utf-8")
            (CITATIONS_DIR / cit_file).write_text(json.dumps(cit, ensure_ascii=False, indent=1), encoding="utf-8")
            labels["cards"].append({
                "id": card["claim_id"],
                "kind": "adversarial",
                "defect": defect,
                "claim_file": f"claims/{claim_file}",
                "citation_file": f"citations/{cit_file}",
                "artifact_under_test": artifact,
            })

    (CORPUS_DIR / "labels.json").write_text(json.dumps(labels, ensure_ascii=False, indent=1), encoding="utf-8")

    n_valid_written = sum(1 for c in labels["cards"] if c["kind"] == "valid")
    n_adv_written = sum(1 for c in labels["cards"] if c["kind"] == "adversarial")
    print(f"gen_corpus: wrote {n_valid_written} valid + {n_adv_written} adversarial cards "
          f"({n_valid_written + n_adv_written} total) to {CORPUS_DIR}")
    print(f"gen_corpus: per-defect counts: {counts}")


if __name__ == "__main__":
    main()
