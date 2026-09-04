---
name: glosa-literature-review
description: Run the glosa Literature Review System (LRS) - six stages (question framing, search protocol, acquisition, reading/extraction, citation verification, neighbour table + manifest), one dialogue-table row per source, two exit gates before a manifest freezes. Triggers - "literature review", "we reviewed the literature", "search protocol", "citation card", "neighbour table", "dialogue table", "did we actually read this", "cite this source", "PRISMA-lite".
---

# glosa-literature-review

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file. LRS
> itself is single-pass and unreviewed (`FOUNDATION_v0.5.md` §12) — its own worked example shows
> the gate working, not passing.

## Load first

- `../../../../methodology/P13_literature_review.md` — the full six-stage protocol (L1-L6),
  owning artifacts, exit gates. Note its own flagged naming collision with a `P13_genre_router.md`
  reference elsewhere — not resolved by this skill, read the card's own note.
- `../../../../design/S14_literature-review-system.md` — the full LRS design this card narrates,
  including the worked cat-question example (§10) and the two-gate mechanics.
- Schemas, one per stage artifact: `../../../../schema/search_log.schema.json`,
  `source_acquisition_log.schema.json`, `citation_card.schema.json`, `dialogue_table_row.schema.json`,
  `neighbour_table_row.schema.json`, `litreview_manifest.schema.json`,
  `hypothesis_selection.schema.json`.
- Fill-in templates: `../../../../templates/knowledge/search_log.yaml`,
  `source_acquisition_log.yaml`, `citation_card.yaml`, `dialogue_table.md`, `neighbour_table.md`,
  `litreview_manifest.yaml`, `hypothesis_selection.yaml`,
  `sr_protocol_prisma_lite.md`, `lit_review_gate_checklist.md`.

## One-line rule (pointer only)

Run once per lens-out hypothesis, never one merged search across several hypotheses. Six stages,
each with one owning artifact and one exit gate — full table in `P13_literature_review.md`.

## Related

- `../../../../design/S13_neighbour-table.md` — worked neighbour-table rewrite (same/different/
  cited language only, no priority-contest framing) that this system's L6 stage produces per row.
- `glosa-claim-card` — `claim_type`/`genre` from the claim card seed `frozen_scope` at L1.
- `glosa-independent-check` — L5's `claim_match_verified` needs an I5 human or decorrelated I3
  check, not a self-check.
- `glosa-publish-gate` — R4 re-runs this system's own accuracy gate independently at release time,
  never grandfathering a manifest that passed at freeze time.
