> tier: Dr (specified; independently unreviewed)

# P18 — Session architecture

## One-line rule

A "session" is not a new file — it is a logical join, by `session_id`, across four artifacts that
already exist (Blackbox Note, `hypothesis_selection.yaml`, Problem Card, `kg_edge.yaml`); and
persistence of a chosen hypothesis across sessions is never, by itself, evidence of which direction
(expansion or tunnel) that persistence runs — only a linked independent check may set the sign.

## Why

`design/SESSION_ARCH_v0.4_SPEC.md` §2 (Part 1 of the 2026-09-05 session-architecture review)
verified four proposals build-ready (SA-1, `schema.entry-resistance-precommit-field`,
`kernel.reciprocal-lineage-diagnostic`, `schema.retention-direction-field`) and found no existing
protocol card narrated the resulting object. Without this card, a reader hits four separate schema
diffs (Blackbox Note session fields, a `retained_direction` field, a Problem Card `intake` block, a
`kg_edge.yaml` diagnostic) with no single place stating they compose into one thing, or why a fifth
`session.yaml` file was deliberately *not* created (§2.2's one-fact-one-home decision).

**Naming note, stated plainly:** this file ships as **P18** in this build pass. It is not named by
`design/SESSION_ARCH_v0.4_SPEC.md` under any P-number — the spec describes its content (§2, §6)
without assigning it a methodology card id. `P16`/`P17` were both already claimed elsewhere in
this same pass (see `P17_human_mastery_gate.md`'s own naming note); P18 is the next free slot in
the sequence as `methodology/README.md` lists it today. A future pass should reconcile this
alongside the P15/P16/P17 collisions already disclosed there, rather than treating any of these
numbers as final.

## The Session object — a logical view, not a fifth file

| field | type | lives on | source |
|---|---|---|---|
| `session_id` | string | Blackbox Note | SA-1, `schema.retention-direction-field` |
| `entry_anchor` (H0) | object `{unresolved, existing_evidence, change_condition, verification_intent, resistance_route}` | Problem Card `intake.entry_anchor` | `schema.entry-resistance-precommit-field` (R* conjunct), HU-2 (remaining four) |
| `human_owner` | string (non-delegable) | **Problem Card** `human_owner` (top-level, already `required`) | FOUNDATION §2.2 S1. MUST fix (ARCH_REVIEW_v0.7.json founder-invariants, one-fact-one-home): a prior draft of this row cited "Blackbox Note," but no `human_owner` field exists on `schema/blackbox_note.schema.json` (confirmed by direct read) or is named as a build target for it anywhere — `problem_card.schema.json` is this fact's one and only home; SA-3 does not add a second. |
| `ai_routes` | array, **derived/computed only, never stored** — grouped `kg_edge.yaml` rows by `session_id`, read off each row's `asserted_by`/`independence_class` | computed from `kg_edge.yaml` | `kernel.reciprocal-lineage-diagnostic`. MUST fix (ARCH_REVIEW_v0.7.json founder-invariants): `kg_edge.schema.json` has no `ai_routes` property and none is planned — like kernel rule31's `defeater_status_for_card` (derived from `defeater_log`, never a second schema field), this row is a computed VIEW over already-stored facts, not a fact with its own home, so it cannot itself violate one-fact-one-home. |
| `question_trace[]` | array of Problem Card refs opened this session | Problem Card | SA-3 (**still_open** — SESSION_ARCH_v0.4_SPEC.md §3/§9.2: fabricated citation, blocked on `session_id`; no schema field exists yet, not scaffolded by the CLI) |
| `candidate_set_deltas[]` | array | **still_open / not yet specified** | `schema.retention-direction-field`. MUST fix (ARCH_REVIEW_v0.7.json spec-code-fidelity, rule 10): no such field exists in `schema/hypothesis_selection.schema.json`, the DAG node's own `fields_added` (only `retained_direction`), any kernel/CLI code, or a CHANGELOG entry — unlike this pass's other named gaps (HU-2's remaining sub-fields, the missing `chi_recip` CLI subcommand), this row had no TODO/deferral anywhere. Recorded here as an explicit deferral: not built, no build_path assigned yet, per `schema/hypothesis_selection.schema.json`'s own `$comment`. |
| `chooser_reaffirmations[]` | array (human re-selects at session reopen) | `hypothesis_selection.yaml` | `schema.retention-direction-field`, SA-2 |
| `resistance_precommit` (R*) | string (concrete route) | Problem Card `intake.entry_anchor.resistance_route` (single home; the flat `intake.precommitted_resistance_route` sibling is deprecated) | `schema.entry-resistance-precommit-field` |
| `retention_note` | ref → Blackbox Note `human_retained_residue_ref` | Blackbox Note | SA-1 |
| `retained_direction` | enum `unknown \| expansion \| tunnel` (default `unknown`) | `hypothesis_selection.yaml` | SA-2, `schema.retention-direction-field` |
| `chi_recip` / `m^H` / `m^AI` | Open finite diagnostics, diagnostic-only | `kg_edge.yaml` + new CLI subcommand | `kernel.reciprocal-lineage-diagnostic`, SA-4 |
| `ai_state_at_boundary` | fixed literal `reset` (always -- never `carried`; the human's own retained residue is the separate `human_retained_residue_ref` fact) | Blackbox Note | SA-1 |

This card narrates the join; it does not redeclare any field's shape (one-fact-one-home) — every
row above cites the schema file that actually owns it. No `session.yaml` exists or should be
created: a fifth physical file duplicating facts already owned by the four artifacts above would
itself be the one-fact-one-home violation this card exists to prevent (`design/
SESSION_ARCH_v0.4_SPEC.md` §2.2).

## Where each fact lives, and why (one-fact-one-home)

- **Session boundary + AI-reset fact → Blackbox Note.** It is the only artifact that already
  carries per-line/per-turn speaker sequencing (`speaker`, `ts`); a new file would duplicate that
  sequencing fact in a second home.
- **Retained-direction-of-a-choice fact → `hypothesis_selection.yaml`.** This is already the K1
  selection ledger (`decided_by`/`decided_at`, S3c) — `retained_direction` is a new field on that
  existing artifact, not a new ledger.
- **Pre-exposure content + precommitted resistance-route facts → Problem Card `intake` object.**
  This is the artifact that already owns `q1_issue`/`q2_user_proposal` — the same object grows an
  `entry_anchor` sub-block (HU-2), not a sibling file.
- **Reciprocal-lineage/momentum diagnostics → `kg_edge.schema.json`** (new `session_id` field) plus
  a new CLI subcommand — never a schema field on any claim/problem card, since these numbers
  "cannot be read as warrant, truth, or human benefit" (see the disclaimer below) and do not belong
  beside fields that do carry warrant.

## The tunnel-vs-expansion disclaimer — NC-77

**Retention ≠ Direction.** Persistence or retention of a claim, habit, or chosen hypothesis across
two or more sessions is never, by itself, evidence that the persistence is *expansion* (a
genuinely reinforced, independently-supported line of work) rather than *tunnel* (a narrowing,
self-reinforcing loop with no outside check). Only a linked independent-check artifact — an
`evidence_relation` resolving to a review_report or falsifier verdict — may set the sign. Default:
`retained_direction: unknown`.

This is `design/SESSION_ARCH_v0.4_SPEC.md` §4's new Family J non-collapse row, `NC-77`, proposed
this pass. **Not yet added to `methodology/data/non_collapse_table.json` or the disclaimer
catalogue** — those data files are outside this task's ownership list; `design/
FOUNDATION_v0.7_PATCH.md` §4 specifies the exact row text, and the internal command-center's DECISIONS ledger (private) must reserve the `NC-77` id before any concurrent Family J proposal can claim it
(`design/SESSION_ARCH_v0.4_SPEC.md` §7, founder decision 3) — a founder-owned ledger write, not an
AI one.

- **Failing control — MUST fire:** a `chosen` `hypothesis_selection.yaml` row spanning ≥2 sessions
  with no `evidence_relation` linking to a review_report/falsifier → forced `retained_direction:
  unknown`.
- **MUST NOT fire:** a row whose `evidence_relation` resolves to an existing checker/falsifier
  verdict — that verdict's own sign stands, unmodified by retention alone.

## Momentum diagnostics — Open, diagnostic-only, never a gate

`chi_recip`, `m^H`, `m^AI` (reciprocal-lineage / momentum diagnostics, `kernel.reciprocal-lineage-
diagnostic`, SA-4) are specified this pass at tier **Open** — honestly not yet `Dr`, since no
`session_id` field exists anywhere in the repo today for them to be computed against (confirmed by
direct read, `design/SESSION_ARCH_v0.4_SPEC.md` §3). They become `Dr` once `session_id` lands on
Blackbox Note (SA-1) and `Open`→`finite_diagnostic` only after the fixture in §5's `momentum_
overclaimed` defect class actually runs. Wherever displayed, they must carry the source citation's
own disclaimer inline — "cannot be read as warrant, truth, or human benefit" — or the display is
itself a defect (`momentum_overclaimed`, per the spec's §5 fixture table), the direct enforcement
complement of SA-4's own declined-schematization clause. `SA-4` itself is a `with_revision`
proposal in this pass (three off-by-one/two line citations); this card treats the diagnostic's
*status* (Open, display-gated) as settled regardless of that pending citation fix, since the
citation defect does not touch the substantive "diagnostic-not-gate" claim.

## Gate — the five self-checks (§6, shared with `P17_human_mastery_gate.md`)

1. **Entry check** — Problem Card's `intake.entry_anchor.resistance_route` and
   `problem_stated_before_first_ai_response` populated before any AI candidate is generated for
   that Problem Card.
2. **Selection check** — every `chosen: true` row spanning ≥2 sessions carries a non-null
   `chooser_reaffirmations[]` entry per session, never a stale flag inherited from the first
   session.
3. **Direction check** — no `retained_direction` other than `unknown` without a resolvable
   `evidence_relation` (NC-77, above).
4. **Boundary check** — every session close writes a Blackbox Note `closed_at` and
   `ai_state_at_boundary: reset`; every session open references the prior note's
   `human_retained_residue_ref` or explicitly records `none`.
5. **Diagnostic-not-gate check** — any `chi_recip`/`m^H`/`m^AI` display carries the disclaimer
   above, or it is itself a `momentum_overclaimed` defect.

This is a self-check protocol for the human/AI pair, composing checks that already exist across
the four artifacts named above — it does not add a new certification layer
(`EPIS-KNOWLEDGE-VALIDATION`: no vertical-authority gate). `P17_human_mastery_gate.md`'s R8 is the
separate, narrower mechanical publish-gate wiring; see that card's "§6 merge" section for how the
two relate.

## Human / AI division of labour

Human: owns `human_owner`, every `chooser_reaffirmations[]` entry, and the resistance-route
precommitment — none of these may be AI-backfilled. AI: may compute `ai_routes[]` and the momentum
diagnostics mechanically, may draft `question_trace[]` entries, and must disclose any contribution
to `candidate_set_deltas[]` under `ai_filled` — never silently folded into a human-authored field.

## Disclaimers emitted

`D-RETENTION-DIRECTION` (new, NC-77 — specified in `design/FOUNDATION_v0.7_PATCH.md` §4, not yet
added to the catalogue file on disk) · `D-NO-PRECOMMIT-ROUTE` (flag, non-mandatory — Problem Card
reaching `READY_FOR_S2` with `intake.entry_anchor.resistance_route` null) · `D-STANDPOINT` ·
`D-AUTHORSHIP`.

## Non-collapse pairs enforced

`NC-77` (new, Family J, this card) · `NC-58` AIContribution≠EpistemicResponsibility (momentum
diagnostics computed by AI do not transfer epistemic weight) · `NC-25`/`NC-26` (a diagnostic at
`unknown`/`not_run` is honestly incomplete, never read as checked-and-clean) · `NC-01`
World≠Record≠Readout≠Meaning≠Truth≠Warrant≠Knowledge-Attribution (retention is a readout of
persistence, not warrant for a direction).

## What this card does NOT do

It does not create a `session.yaml` file (§2.2, above — settled, pending only the founder's formal
ratification per spec §7 decision 1). It does not itself add the `session_id` field to any schema,
the `retained_direction` field to `hypothesis_selection.schema.json`, the `entry_anchor` sub-object
to `problem_card.schema.json`, or the new CLI diagnostic subcommand — those are schema/kernel/CLI
edits outside this task's ownership list; `design/FOUNDATION_v0.7_PATCH.md` specifies their exact
text. It does not resolve the founder decisions `design/SESSION_ARCH_v0.4_SPEC.md` §7 lists
(ratifying §2.2, merging the duplicate `kernel.session-boundary-momentum-reset-assertion` proposal
into SA-1, reserving `NC-77`, SA-3 retroactivity, the SA-4 ledger row's `status` value, approving
the H3 sim, wiring `session_id` into `hypothesis_selection.yaml`) — those stay pending-founder,
named here rather than defaulted silently.

## TODO(session.boundary-blackbox-note)

Add `session_id`, `opened_at`, `closed_at`, `ai_state_at_boundary`, `human_retained_residue_ref` to
`schema/blackbox_note.schema.json` and `templates/knowledge/blackbox_note.yaml` — per
`design/SESSION_ARCH_v0.4_SPEC.md` §8 and `design/FOUNDATION_v0.7_PATCH.md` §2.
`founder_decision_needed: true` (merge target for the duplicate proposal, spec §7 decision 2).

## TODO(schema.retention-direction-field)

Add `retained_direction` to `schema/hypothesis_selection.schema.json`, blocked on `session_id`
propagating from the Blackbox Note build above for the ≥2-session half of its acceptance test — per
`design/SESSION_ARCH_v0.4_SPEC.md` §8 and `design/FOUNDATION_v0.7_PATCH.md` §2.
