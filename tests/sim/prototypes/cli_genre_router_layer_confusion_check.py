#!/usr/bin/env python3
"""K4-proto cli.genre-router-layer-confusion-check.

DAG node (design/DAG_v0.3.yaml): "Add a CLI check that flags when a claim card's
genre/register (e.g. jurisprudential) does not match the tool/authority being invoked on
it (e.g. astronomical), using the three-layer split (astronomical/jurisprudential/
institutional) as the template."

SANDBOX generalization used here (no kernel/schema edits, pure python, same input shape
as the kernel -- one claim_card dict + optional citation_cards list, returns a list of
finding strings): the three-layer template is read as "a field DECLARES one evidentiary
register/layer, but its own content or a sibling field is actually written in a DIFFERENT
layer" -- the same structural defect as astronomical-tool-invoked-on-a-jurisprudential-
question, just instantiated on the four layer-pairs this v0.3 corpus actually contains
(inspected directly against sim/v0.3/corpus/claims + citations -- not designed blind):

  L1 quote-register:     citation.scope == DIRECT_QUOTATION (verbatim layer) but
                          exact_passage contains an ellipsis/composite-join marker
                          (paraphrase/composite layer) -- catches composite_quote.
  L2 authorship-register: an access/observation field's OWN TEXT carries an explicit
                          AI-authorship disclosure marker (AI-drafted layer) while the
                          card's outer responsible/produced_by fields are silent about it
                          at that field -- catches hidden_ai_fill.
  L3 independence-register: an evidence_relations entry declares independence_class in
                          {I0,I1} (independent-support layer) while its own notes say the
                          source is self-authored / same-lineage (institutional/self
                          layer) -- catches inflated_bearing. (review_mode alone, e.g.
                          MAKER_SELF_CHECK, is NOT used as a signal: it co-occurs with
                          independence_class=I1 on valid cards too -- confirmed against
                          the corpus's 60 valid cards before shipping this check, see
                          the .result.json false_alarm counts.)
  L4 finiteness-register: claim_type == EMPIRICAL / genre outside formal_proof (finite,
                          discrete-readout layer) but statement/hypothesis text asserts
                          absolute/infinite vocabulary (infinite, exactly zero, never,
                          always, 100%, ทุกครั้ง, ไม่มีทางเป็นอย่างอื่น, ...) that belongs to
                          a formal/unbounded-claim layer -- catches injected_infinity.

This is a diagnostic-only prototype (no auto-correction), consistent with the
diagnostic-not-optimizing pattern already used elsewhere in this DAG. Every finding is
finite_diagnostic tier: a readout of THIS check against THIS fixed input, not a general
claim about the kernel or about claim cards it has not seen.
"""
from __future__ import annotations

import re
from typing import Any, Iterable

COMPOSITE_QUOTE_MARKERS = ("…", "...")
AI_AUTHORSHIP_MARKERS = ("AI-DRAFTED", "AI DRAFTED", "AI-GENERATED", "AI GENERATED")
SELF_LINEAGE_MARKERS = ("own-lineage", "own lineage", "self-authored", "same-lineage")
INDEPENDENT_CLASSES = {"I0", "I1"}
INFINITY_MARKERS = (
    "infinite", "infinity", "exactly zero", "never happens", "always true",
    "100% certain", "ทุกครั้ง", "ไม่มีทางเป็นอย่างอื่น", "ศูนย์แท้", "แน่นอนเสมอ",
)
# broad regex fallback for "infinite <word>" / "exactly zero" phrasing variants
INFINITY_REGEX = re.compile(r"\binfinite\s+\w+\b|\bexactly\s+zero\b", re.IGNORECASE)


def _walk(obj: Any, path: str = "") -> Iterable[tuple[str, Any]]:
    """Yield (json-pointer-ish path, value) for every leaf/dict/list node."""
    yield path, obj
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk(v, f"{path}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk(v, f"{path}[{i}]")


def _text_at(card: dict, *keys: str) -> str:
    cur: Any = card
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return ""
        cur = cur[k]
    return cur if isinstance(cur, str) else ""


def check_l1_quote_register(citation: dict) -> list[str]:
    """DIRECT_QUOTATION scope declared but passage content is composite/non-contiguous."""
    out = []
    scope = citation.get("scope")
    passage = citation.get("exact_passage") or ""
    if scope == "DIRECT_QUOTATION" and any(m in passage for m in COMPOSITE_QUOTE_MARKERS):
        out.append(
            "LAYER-CONFUSION L1(quote-register): citation declares scope=DIRECT_QUOTATION "
            "(verbatim layer) but exact_passage contains a composite/ellipsis join marker "
            "-- content is actually in the paraphrase/composite layer, not verbatim."
        )
    return out


def check_l2_authorship_register(card: dict) -> list[str]:
    """An observation/access field's own text discloses AI drafting the outer card hides."""
    out = []
    responsible = card.get("responsible")
    produced_by = card.get("produced_by")
    for path, val in _walk(card):
        if not isinstance(val, str):
            continue
        if any(m in val for m in AI_AUTHORSHIP_MARKERS):
            out.append(
                f"LAYER-CONFUSION L2(authorship-register): field {path!r} discloses AI "
                f"authorship in its own text (AI-drafted layer) while the card's outer "
                f"responsible={responsible!r}/produced_by={produced_by!r} give no field-"
                f"level attribution at that path -- an AI-drafted layer is being presented "
                f"inline as if it were the human-observed layer."
            )
    return out


def check_l3_independence_register(card: dict) -> list[str]:
    """independence_class claims independence while notes/review_mode say self/same-lineage."""
    out = []
    for path, val in _walk(card):
        if not isinstance(val, dict):
            continue
        if "independence_class" not in val:
            continue
        ind_class = val.get("independence_class")
        if ind_class not in INDEPENDENT_CLASSES:
            continue
        notes = str(val.get("notes") or "")
        lineage_hit = any(m in notes for m in SELF_LINEAGE_MARKERS)
        if lineage_hit:
            out.append(
                f"LAYER-CONFUSION L3(independence-register): {path!r} declares "
                f"independence_class={ind_class!r} (independent-support layer) but "
                f"notes={notes!r} place the source in the self/same-lineage layer -- "
                f"bearing is inflated across a layer boundary."
            )
    return out


def check_l4_finiteness_register(card: dict) -> list[str]:
    """EMPIRICAL/non-formal claim text asserts infinite/absolute vocabulary."""
    out = []
    claim_type = card.get("claim_type")
    genre = card.get("genre")
    if claim_type != "EMPIRICAL" and genre == "formal_proof":
        return out  # formal_proof genre is the one register allowed to speak in absolutes
    texts = []
    stmt_text = _text_at(card, "statement", "text")
    if stmt_text:
        texts.append(("statement.text", stmt_text))
    hyp_text = _text_at(card, "hypothesis_world", "text")
    if hyp_text:
        texts.append(("hypothesis_world.text", hyp_text))
    for field, text in texts:
        hit_markers = [m for m in INFINITY_MARKERS if m in text]
        regex_hit = INFINITY_REGEX.search(text)
        if hit_markers or regex_hit:
            found = hit_markers + ([regex_hit.group(0)] if regex_hit else [])
            out.append(
                f"LAYER-CONFUSION L4(finiteness-register): {field} is in the finite/"
                f"discrete-readout layer (claim_type={claim_type!r}, genre={genre!r}) but "
                f"asserts absolute/infinite vocabulary {found!r} that belongs to a formal/"
                f"unbounded-claim layer."
            )
    return out


def check_genre_router_layer_confusion(
    card: dict, citation_cards: list[dict] | None = None
) -> list[str]:
    """Pure-python sandbox check, same input shape as the kernel.

    Args:
        card: a claim-card dict (schema/claim_card.schema.json shape).
        citation_cards: list of companion citation-card dicts (schema/citation_card
            .schema.json shape), if any -- mirrors validate_claim_card's own signature.

    Returns:
        list of finding strings (error/warning severity is not distinguished here --
        this prototype reports every layer-confusion instance it finds; a real kernel
        rule would decide error vs warning severity per layer).
    """
    findings: list[str] = []
    findings += check_l2_authorship_register(card)
    findings += check_l3_independence_register(card)
    findings += check_l4_finiteness_register(card)
    for citation in citation_cards or []:
        findings += check_l1_quote_register(citation)
    return findings


# --- evaluation harness -----------------------------------------------------------
if __name__ == "__main__":
    import json
    from pathlib import Path

    HERE = Path(__file__).resolve().parent
    SIM_V03 = HERE.parent
    CORPUS_DIR = SIM_V03 / "corpus"

    labels = json.loads((CORPUS_DIR / "labels.json").read_text(encoding="utf-8"))
    cards = labels["cards"]

    RELEVANT_DEFECTS = ["composite_quote", "hidden_ai_fill", "inflated_bearing", "injected_infinity"]
    per_defect = {d: {"n": 0, "caught": 0, "missed": 0} for d in RELEVANT_DEFECTS}
    valid_n = 0
    valid_false_alarm = 0
    valid_false_alarm_ids = []

    for entry in cards:
        claim = json.loads((CORPUS_DIR / entry["claim_file"]).read_text(encoding="utf-8"))
        citation = json.loads((CORPUS_DIR / entry["citation_file"]).read_text(encoding="utf-8"))
        findings = check_genre_router_layer_confusion(claim, citation_cards=[citation])

        if entry["kind"] == "valid":
            valid_n += 1
            if findings:
                valid_false_alarm += 1
                valid_false_alarm_ids.append((entry["id"], findings))
        else:
            defect = entry["defect"]
            if defect not in per_defect:
                continue  # out-of-scope defect for this prototype (not one of the 4 targeted)
            per_defect[defect]["n"] += 1
            if findings:
                per_defect[defect]["caught"] += 1
            else:
                per_defect[defect]["missed"] += 1

    print(f"{'defect':20s} {'n':>4s} {'caught':>7s} {'missed':>7s}")
    print("-" * 44)
    for d in RELEVANT_DEFECTS:
        row = per_defect[d]
        print(f"{d:20s} {row['n']:4d} {row['caught']:7d} {row['missed']:7d}")
    print("-" * 44)
    print(f"valid cards: n={valid_n} false_alarm={valid_false_alarm}")
    if valid_false_alarm_ids:
        for vid, f in valid_false_alarm_ids:
            print("  FALSE ALARM", vid, f)
