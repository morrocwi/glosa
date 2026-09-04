"""Prototype SANDBOX check for DAG node foundation.s7.9-intake-tier-flag.

tier: finite_diagnostic (evaluated against sim/v0.3/corpus/labels.json — 60 valid + 120
adversarial cards; counts are printed by running this file directly, or see the sibling
.result.json which records the exact counts this run produced).

Readout-not-truth framing: this module does NOT implement the DAG node's actual proposal
(a flag-and-request-tier step layered on the AACODS-style LRS checklist for *source genre*
appraisal, e.g. distinguishing "policy-brief-only" intake from a rejected one). That proposal
is about literature-review source-genre handling and this sandbox corpus carries no
literature-search/genre-appraisal fixtures to exercise it against.

What this module actually is: a narrow SANDBOX probe built to answer the concrete question the
harness asked --- "does a thin, additional intake-tier-style flag layer catch the four named
defect classes the kernel-only baseline currently misses (composite_quote, hidden_ai_fill,
inflated_bearing, injected_infinity)?" All four are, in the DAG node's own vocabulary, cases
where the intake tier a card is presented at (VERIFIED citation / disclosed evidence-support /
plain empirical claim) does not match what the underlying material actually supports --- exactly
the "distinct flagged-not-blocked intake row" shape the node's acceptance_test asks for. Each
check below is a plain presence/regex heuristic over already-shaped JSON, mirrors the kernel's
own "SHAPE/PRESENCE/STRUCTURAL check, never a truth adjudication" discipline, and returns a
warning (flag), never a hard block, matching acceptance_test's "flagged-not-blocked" requirement.

Each detector was derived by diffing the 9 fixtures for each labeled defect against the 60 valid
cards in this same corpus (see the .result.json `notes` for the exact discriminating field). This
is DERIVED-FROM-CORPUS, not derived from the DAG node's literature-genre proposal text -- flag
this fact honestly rather than overclaiming that this file "implements s7.9".

Pure python, stdlib only, no network, no kernel import (this file is deliberately independent of
kernel/glosa_kernel.py so it can be run/scored standalone; it does not modify or wrap the kernel).
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

_INFINITY_MARKERS = [
    "infinite reliability",
    "infinite ",
    "exactly zero",
    "ศูนย์แท้",
    "infinit",
]

_COMPOSITE_QUOTE_MARKERS = [
    "สรุปรวม",
    "รวมจาก",
    "composite quote",
    "combined from",
    "…",
    "...",
]

_AI_MENTION_RE = re.compile(r"\bAI\b", re.IGNORECASE)

_OWN_LINEAGE_MARKERS = [
    "own-lineage",
    "own lineage",
    "own earlier draft",
    "own prior draft",
    "self-citation",
]

_NONE_IDENTIFIED = "none identified"


def _get(d: Any, *path, default=None):
    cur = d
    for p in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(p, default)
    return cur


def _all_text_snippets(card: Dict[str, Any]) -> List[str]:
    """Small set of the free-text fields worth scanning for injected-infinity language."""
    out = []
    stmt = _get(card, "statement", "text")
    if stmt:
        out.append(str(stmt))
    trans = _get(card, "statement", "translation", "text")
    if trans:
        out.append(str(trans))
    hyp = _get(card, "hypothesis_world", "text")
    if hyp:
        out.append(str(hyp))
    return out


def check_injected_infinity(card: Dict[str, Any]) -> List[str]:
    """Flag literal infinity / exact-zero-probability language injected into an empirical
    claim's own statement/hypothesis text. A finite readout (this corpus's whole epistemic
    floor) never legitimately asserts a continuum absolute -- 'infinite reliability' or
    'probability exactly zero' for an observed behavioural claim is a non-readout smuggled
    into claim text, not a measured finite result."""
    warnings = []
    for snippet in _all_text_snippets(card):
        low = snippet.lower()
        for marker in _INFINITY_MARKERS:
            if marker.lower() in low:
                warnings.append(
                    "SANDBOX s7.9-intake-tier-flag: injected_infinity candidate -- claim text "
                    f"contains non-readout absolute marker '{marker}': {snippet[:120]!r}"
                )
                break  # one flag per snippet is enough
    return warnings


def check_composite_quote(citation: Optional[Dict[str, Any]]) -> List[str]:
    """Flag a citation card that asserts scope=DIRECT_QUOTATION (a verbatim single passage) while
    its own exact_passage text carries an explicit composite/ellipsis marker -- i.e. the citation
    is silently presenting a stitched-together passage as one direct verbatim quote."""
    if not isinstance(citation, dict):
        return []
    warnings = []
    scope = citation.get("scope")
    passage = citation.get("exact_passage") or ""
    if scope == "DIRECT_QUOTATION":
        for marker in _COMPOSITE_QUOTE_MARKERS:
            if marker in passage:
                warnings.append(
                    "SANDBOX s7.9-intake-tier-flag: composite_quote candidate -- citation "
                    f"{citation.get('id', '?')} scope=DIRECT_QUOTATION but exact_passage carries "
                    f"a composite/ellipsis marker '{marker}': {passage[:120]!r}"
                )
                break
    return warnings


def check_hidden_ai_fill(card: Dict[str, Any]) -> List[str]:
    """Flag a card where every five_questions.ai_filled sub-field reads 'none identified' (i.e.
    the card's own disclosure section claims zero AI contribution to evidence/record-route/
    calibration/policy) while responsibility.notes or responsibility.ownership.notes elsewhere on
    the SAME card plainly narrates an AI contribution (drafted/proposed/generated/etc). That is
    the disclosure section hiding what the card's own responsibility narrative admits."""
    ai_filled = _get(card, "five_questions", "ai_filled")
    if not isinstance(ai_filled, dict) or not ai_filled:
        return []
    all_none = all(
        isinstance(v, str) and v.strip().lower() == _NONE_IDENTIFIED
        for v in ai_filled.values()
    )
    if not all_none:
        return []
    resp_notes = _get(card, "responsibility", "notes") or ""
    own_notes = _get(card, "responsibility", "ownership", "notes") or ""
    combined = f"{resp_notes} {own_notes}"
    if _AI_MENTION_RE.search(combined):
        return [
            "SANDBOX s7.9-intake-tier-flag: hidden_ai_fill candidate -- every "
            "five_questions.ai_filled field reads 'none identified' but responsibility "
            f"narrative mentions AI involvement: {combined.strip()[:160]!r}"
        ]
    return []


def check_inflated_bearing(card: Dict[str, Any]) -> List[str]:
    """Flag an evidence_relation that asserts a directional bearing (SUPPORTS/REFUTES, i.e. not
    NEUTRAL/AMBIGUOUS) while its own notes field admits the source is the claim's own lineage
    (an earlier draft / context note of the same claim, or a self-citation) -- using a claim's own
    prior draft as if it were outside evidentiary support inflates the apparent evidentiary
    bearing of a self-referential note."""
    warnings = []
    relations = _get(card, "five_questions", "tested", "evidence_relations") or []
    if not isinstance(relations, list):
        return []
    for rel in relations:
        if not isinstance(rel, dict):
            continue
        bearing = str(rel.get("bearing", "")).upper()
        notes = str(rel.get("notes", "") or "")
        if bearing in ("SUPPORTS", "REFUTES"):
            low = notes.lower()
            for marker in _OWN_LINEAGE_MARKERS:
                if marker in low:
                    warnings.append(
                        "SANDBOX s7.9-intake-tier-flag: inflated_bearing candidate -- "
                        f"evidence_relation {rel.get('evidence_id', '?')} bearing={bearing} but "
                        f"notes admits own-lineage source: {notes[:160]!r}"
                    )
                    break
    return warnings


def intake_tier_flag_check(
    card: Dict[str, Any], citation_cards: Optional[List[Dict[str, Any]]] = None
) -> List[str]:
    """Entry point matching the kernel's `k.validate_*(card, citation_cards=...)` calling shape.

    `card` is a claim_card payload. `citation_cards` is an optional list of citation_card
    payloads (as passed to k.validate_claim_card); this prototype uses whichever of those match
    a citation_ref referenced by the card's own evidence_relations (falling back to
    `related_citation_cards` ids) to run check_composite_quote against.

    Returns a flat list of warning strings (never raises, never hard-fails -- this is a SANDBOX
    flag layer, matching the DAG node's acceptance_test: "a flagged-not-blocked intake row,
    distinct from a rejected row").
    """
    if not isinstance(card, dict):
        return ["SANDBOX s7.9-intake-tier-flag: card is not an object -- skipped"]

    warnings: List[str] = []
    warnings.extend(check_injected_infinity(card))
    warnings.extend(check_hidden_ai_fill(card))
    warnings.extend(check_inflated_bearing(card))

    citation_cards = citation_cards or []
    if citation_cards:
        wanted_ids = set()
        relations = _get(card, "five_questions", "tested", "evidence_relations") or []
        if isinstance(relations, list):
            for rel in relations:
                if isinstance(rel, dict) and rel.get("citation_ref"):
                    wanted_ids.add(rel["citation_ref"])
        for ref in card.get("related_citation_cards") or []:
            wanted_ids.add(ref)
        for citation in citation_cards:
            if not isinstance(citation, dict):
                continue
            if not wanted_ids or citation.get("id") in wanted_ids:
                warnings.extend(check_composite_quote(citation))

    return warnings


if __name__ == "__main__":
    import json
    from pathlib import Path

    corpus_dir = Path(__file__).resolve().parents[1] / "corpus"
    labels = json.loads((corpus_dir / "labels.json").read_text(encoding="utf-8"))

    n_flagged = 0
    n_cards = 0
    for entry in labels["cards"]:
        claim = json.loads((corpus_dir / entry["claim_file"]).read_text(encoding="utf-8"))
        citation = json.loads((corpus_dir / entry["citation_file"]).read_text(encoding="utf-8"))
        n_cards += 1
        flags = intake_tier_flag_check(claim, citation_cards=[citation])
        if flags:
            n_flagged += 1
    print(f"scanned {n_cards} cards, {n_flagged} produced >=1 SANDBOX warning")
