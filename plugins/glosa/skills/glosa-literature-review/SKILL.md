---
name: glosa-literature-review
description: Run the glosa Literature Review System (LRS) - six stages (question framing, search protocol, acquisition, reading/extraction, citation verification, neighbour table + manifest), one dialogue-table row per source, two exit gates before a manifest freezes. Also drives the optional architecture-first comparative review mode for architecture-shaped work (node-grain Supports/Challenges/Extends relations, non-collapse guard). Triggers - "literature review", "we reviewed the literature", "search protocol", "citation card", "neighbour table", "dialogue table", "did we actually read this", "cite this source", "PRISMA-lite", "architecture-first review", "ทบทวนวรรณกรรมแบบสถาปัตยกรรม", "Supports/Challenges/Extends", "literature as allies".
---

# glosa-literature-review

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file. LRS
> itself is single-pass and unreviewed (`FOUNDATION_v0.6.md` §12) — its own worked example shows
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
- Architecture-first mode (optional, §"Architecture-first comparative review" below):
  `../../../../design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md` (full procedure, worked example,
  forbidden-phrasing table), `../../../../design/S14_literature-review-system.md` §3.5 (binding
  summary), `../../../../templates/knowledge/architecture_map.md`,
  `../../../../templates/knowledge/architecture_dialogue_table.md`,
  `../../../../scripts/check_non_collapse.py`.

## One-line rule (pointer only)

Run once per lens-out hypothesis, never one merged search across several hypotheses. Six stages,
each with one owning artifact and one exit gate — full table in `P13_literature_review.md`.

## Architecture-first comparative review (ratified 2026-09-23) — optional, node grain

**When to use:** the work under review is itself an *architecture* — two or more named nodes
(mechanisms/stages/constructs) with transitions between them — not a single-claim hypothesis. A
single-claim hypothesis skips this mode entirely and uses L1–L6 unchanged. Provenance and full
detail: `design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md`; binding summary:
`design/S14_literature-review-system.md` §3.5.

**Steps:**
1. Freeze the architecture map **before** any search opens
   (`templates/knowledge/architecture_map.md`): `node_id`, `node_name` (work's own term),
   `mechanism` (one sentence, work's own vocabulary), `upstream_nodes`, `downstream_nodes`. This
   map **is** how L2's `frozen_scope` locks for this hypothesis — changing it after search begins
   is an L2 exit-gate violation.
2. For each admitted literature strand (same L2/L3 search-protocol and acquisition discipline as
   any other source), add one `templates/knowledge/architecture_dialogue_table.md` row per
   `(node, strand, relation)` triple, backed by the same citation-card discipline L4 requires.
3. Write one per-node synthesis sentence: what the architecture's own arrangement reveals that no
   single strand reveals alone, and what each strand still sees that the others miss — naming the
   strands drawn on.
4. Run the mandatory CHALLENGES pass: a node with every populated relation as SUPPORTS and no
   disclosed attempt to find a challenging strand is a flag. An unanswered CHALLENGES row marks
   that node `node_status: OPEN` with a stated reason; its claim may not be cited as settled
   downstream until closed.
5. Judge the whole, in prose, against the six-criteria yardstick: coherence, coverage,
   non-collapse, composability, explanatory reach, testability — never a summed score.
6. Before publish, run `python3 scripts/check_non_collapse.py <file>` on every file this mode
   produced or edited (WARN-only — it flags candidate ownership/subtraction phrasing for a human
   to read and dispose of; it never auto-fails a gate).

**The three relations (never a fourth, never an ownership move):**
- **SUPPORTS** — the strand, in its own terms, corroborates or independently arrives at something
  compatible with the node's claim.
- **CHALLENGES** — the strand, in its own terms, gives a reason to doubt, narrow, or reject the
  node's claim.
- **EXTENDS** — the strand adds resolution, mechanism detail, an adjacent case, or a boundary
  condition the node does not itself specify, without contradicting it. No hypothesis-grain
  analogue in `dialogue_table.md`'s enum — never coerced to `orthogonal`.

#### Forbidden phrasings → rewrites (full table: proposal §6) <!-- non-collapse:meta -->
| Forbidden | Rewrite |
|---|---|
| "[Node] is [strand]'s concept" / "[node] ← [theory]" | "[Strand] SUPPORTS/CHALLENGES/EXTENDS node N by [specific mechanism]; the architecture places N in a chain the strand's own framework does not itself specify." |
| "X already did this" | "X SUPPORTS/CHALLENGES/EXTENDS node N; the architecture's own contribution is [specific transition/mechanism X's framework does not cover]." |
| "not novel" / "novelty constraint" | State the specific relation (SUPPORTS/CHALLENGES/EXTENDS) instead — already banned repo-wide (`AGENTS.md` rule 6). |
| "reduces to X" | "N and X are same/different in [specific respect]; N does not reduce to X because [specific transition X's framework does not cover]." |

**Related to S13:** each whole-work `neighbour_table.md` row may carry an optional `node_refs:`
pointing at zero or more node-grain rows that bear on that neighbour — a pointer only, S13 stays
the whole-work same/different/cited comparison it already is.

## Related

- `../../../../design/S13_neighbour-table.md` — worked neighbour-table rewrite (same/different/
  cited language only, no priority-contest framing) that this system's L6 stage produces per row.
- `glosa-claim-card` — `claim_type`/`genre` from the claim card seed `frozen_scope` at L1.
- `glosa-independent-check` — L5's `claim_match_verified` needs an I5 human or decorrelated I3
  check, not a self-check.
- `glosa-publish-gate` — R4 re-runs this system's own accuracy gate independently at release time,
  never grandfathering a manifest that passed at freeze time.

## New this pass (v0.6) — pointer only, PENDING FOUNDER DECISION

`../../../../design/FOUNDATION_v0.6.md` §7.9 (`FOUNDATION_v0.6_PATCH.md` §4/§23): a claim-tier
intake flag (`citations[].intake_tier`/`intake_tier_reason`/`global_south_exempt`) and a
discovery-routing extension (`discovery_routing` block, `k_epi` gating) — both marked pending
founder decision (thin-layer-scope-confirmation / discovery-routing-stage-adoption), not yet
ratified. `templates/knowledge/litreview_manifest.yaml` already carries the fields; do not treat
either mechanism as binding until the founder decision lands.

**Ratified this pass (2026-09-23):** the architecture-first comparative review mode above (node
grain, `SUPPORTS/CHALLENGES/EXTENDS`) is ratified into the binding methodology — see the dedicated
section above, not pending.

## Source-first citation (kernel rule 17, 2026-09-04)

Never cite from memory. Open the source, record the link you read it from, the page/section, the line/paragraph, and one continuous verbatim passage — all four on the card — or leave the card at CANDIDATE. See FOUNDATION §7.8.
