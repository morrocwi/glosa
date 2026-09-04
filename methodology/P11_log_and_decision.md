# P11 — Log & decision

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction; AI drafted this card,
> narrating `FOUNDATION_v0.5.md` §2 (spine), §2.3 (Blackbox Note cooking log), and this
> workspace's own decision-recording discipline. Comparison language is same/different/cited only.

## id

`P11`

## Rule

Two append-only records, never edited in place, both required whenever they apply:

1. **`logbook.jsonl`** — one entry per meaningful event (an observation, a diagnosis run (`P8`), a
   vetting act (`P9`), a review, a publish attempt, a dissent). Each entry is a typed row, never a
   free-text diary: `{ts, kind, actor, ref, summary, tier}`. `kind` names the event class (e.g.
   `observation | diagnosis | vetting | review | publish_attempt | dissent | ruling`); `ref` points
   at the artifact/claim card it concerns; nothing in `logbook.jsonl` is deleted or rewritten — a
   correction is a new row with `kind: correction` pointing back at the row it corrects.
2. **`DECISIONS.md`** (or the project's `DECISIONS.yaml` where the callable layer is in use) — a
   chat decision, a founder ruling, or a chair ruling is not "done" until it is a row here, with
   `date, decided_by, statement, ref` — never left only in a conversation transcript.

Both are **cross-referenced, not merged**: a `logbook.jsonl` row of `kind: ruling` points at the
`DECISIONS.md` row it produced; a `DECISIONS.md` row may cite the `logbook.jsonl` rows that led to
it. This is the same one-fact-one-home discipline (`P0`) applied to process records — the decision
lives in one file, the event trail that produced it lives in another, and each cites the other by
id rather than restating it.

## Why / incident

Two workspace-standing rules converge on this card: (a) "a chat decision is not 'done' until it is
a row" is a binding rule already enforced machine-wide in this founder's workspace (the command-
center gate) — glosa inherits it rather than inventing a second decision-recording convention; (b)
dissent-erasure is a named failure this repo's own governance explicitly forbids (`FOUNDATION_
v0.3.md` §1.1's "no epistemic veto" stance, `D-DISSENT-PRESERVED`) — a disagreement recorded once
and later quietly dropped from the file is indistinguishable, to a later reader, from a
disagreement that was never raised, which is exactly the silent-lift failure mode (`NC-15`) applied
to process history instead of evidence.

## Inputs → outputs

- **Inputs:** any event worth recording (an observation, a check, a ruling, a dissent); for a
  Blackbox Note-adjacent event, the note's own line ids (`origin_blackbox_ref`).
- **Outputs:** a `logbook.jsonl` row (always); a `DECISIONS.md`/`DECISIONS.yaml` row (whenever the
  event is a ruling/decision, not merely an observation); for a hypothesis-selection event
  specifically, an entry in the Blackbox Note's own `cooking:` log (`P13`/`S14` §6 — selection is
  itself a "cooking" transformation of raw material, per the founder's own requirement that every
  transformation is published, never sealed).

## Gate

A ruling/decision that exists only in a conversation transcript may not be cited from a claim card
or a review as an authority for anything (`independent_check`, `assumed[]`) until it has a
`DECISIONS.md` row. A dissent record (`tested.dissent_records[]` on a claim card, or a
Disagreement Ledger `DECLARED` outcome, `P6`) may never be removed from the file it lives in — an
overturned or superseded dissent gets a new row marking it `resolved: true` with a pointer to what
resolved it; the original row stays.

## Human / AI split

Human: is the `decided_by` on any `DECISIONS.md` row recording a founder/chair ruling — this is
non-delegable, matching the claim card's own `human_owner`/`responsible` fields. AI: may write
`logbook.jsonl` rows for events it directly performed or observed, and may draft a `DECISIONS.md`
row's wording for a human to confirm, but may not itself be the `decided_by` on any ruling row.

## Disclaimers

`D-DISSENT-PRESERVED` (any dissent/deviation record exists), `D-BLACKBOX-NOTE` (any cooking-log
entry feeding a mandatory appendix), `D-REVISION-LIVE` (CHANGELOG/`reviews/` reflect the decision).

## NC pairs

`NC-15` represented ≠ actual essential dependency set (Silent Lift — applied here to process
history: a decision trail that silently drops a dissent misrepresents what was actually
considered) · `NC-24` forced ≠ borrowed ≠ Open · `NC-26` "not checked" ≠ "checked, nothing found"
(A2 — applied to logbook completeness: an event not logged is not evidence nothing happened).

## Not-do

- Do not edit a `logbook.jsonl` row in place — append a correction row instead.
- Do not delete or silently rewrite a dissent record; mark it `resolved` with a pointer if it is
  superseded.
- Do not treat a conversation-only decision as citable authority for a claim card or a gate.
- Do not merge `logbook.jsonl` and `DECISIONS.md` into one file — they answer different questions
  (what happened, in order vs. what was decided, as a queryable row) and merging them would
  violate one-fact-one-home the same way a duplicate schema field would.
- Do not let an AI session record itself as `decided_by` on a ruling row.

## Tier

Dr (specified; independently unreviewed).
