---
name: glosa-claim-card
description: Write or check a glosa claim card — the five-questions object (seen / separates / AI-filled / assumed / tested) every claim-level distinction must answer, in one of exactly two legal shapes (stub or full). Triggers - "claim card", "five questions", "stub vs full card", "is this claim tested", "ai_filled disclosure", "claim_type", "genre" (routing input for glosa-literature-review).
---

# glosa-claim-card

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../methodology/P03_claim_card.md` — the full protocol card (why, inputs/outputs, the
  stub/full gate, chair ruling D2 on what is mechanically checkable vs not).
- `../../../../schema/claim_card.schema.json` — the authoritative field list. Do not redeclare a
  second copy of it here or anywhere else.
- `../../../../design/FOUNDATION_v0.5.md` §3 — narrates the card; does not replace the schema.

## One-line rule (pointer only)

One claim-level distinction → one claim card → exactly one shape, `stub` or `full`, never a third
improvised shape. Full protocol, gate, and worked reasoning: `P03_claim_card.md` above.

## Related protocol cards

- `../../../../methodology/P02_intake.md` — the Problem Card that feeds this card's inputs.
- `../../../../methodology/P04_assumption_check.md` — Q4 (assumed).
- `../../../../methodology/P07_ai_fill_disclosure.md` — Q3 (`ai_filled`) disclosure shape.
- `../../../../methodology/P06_independent_check.md` (`glosa-independent-check`) — Q5 (tested) is
  the only genuinely mechanically-enforceable question; this card cannot self-certify it.

## Fill-in template

`../../../../templates/knowledge/` has no standalone `claim_card.yaml` template as of this
version — author the JSON/YAML directly against `schema/claim_card.schema.json`, or check
`../../../../design/REPO_SPEC_v0.5.md` for whether one has since been added.

## What this skill does not do

It never advances a card past `Pending Review` on its own (that needs `glosa-independent-check`),
and it never decides genre routing rules itself — `claim_type`/`genre` are handed to
`glosa-literature-review` and the genre router (`../../../../methodology/data/genre_router_table.json`),
whose own protocol card is pending (see `design/REPO_SPEC_v0.5.md`'s `P16_genre_router.md`
reference).
