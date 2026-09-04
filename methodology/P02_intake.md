> tier: Dr (specified; independently unreviewed)

# P2 — Intake (two questions; issue = retained difference; 0≠⊥; stakeholder≠agency)

## One-line rule

Before any analysis starts, pass a mandatory two-question intake gate: what is the retained
difference this issue names (never just a label), and who is affected versus who holds power over
it — and never collapse "checked, found no difference" into "not checked."

## Why

`design/FOUNDATION_v0.5.md` §2.2 names S1 Problem Intake as the first spine stage, gated by "Two-
question intake complete; standpoint declared; readiness verdict `READY_FOR_S2`" before any
evidence work begins. The retained-difference framing and the stakeholder/agency split are named
directly in `HANDOFF_2026-09-04_founding-meeting.md` §6 request 17's non-collapse list
("stakeholder≠agency" in the table this session built into FOUNDATION Appendix A) and realized as
`NC-62` (chair ruling C6, 2026-09-04, `design/FOUNDATION_v0.5.md` Appendix A Family H — "being
affected by a decision is not the same as holding power over it," re-derived independently,
pattern only, from the skillme protocol's own stakeholder-agency map). The `0≠⊥` distinction is
`NC-25` (Appendix A Family B) and is load-bearing at intake because a claim card's
`zero_vs_bottom` field (§3.2, `five_questions.separates`) must already distinguish "checked, no
difference found" from "not yet checked" the moment an issue is framed, or the distinction is lost
before it can be recorded.

## Inputs → outputs

- Input: the human's raw statement of the problem (a Blackbox Note line, P0/P15).
- Output: `schema/problem_card.schema.json` fields (FOUNDATION §2.2, S1) — the two-question intake
  answers, plus the stakeholder-agency map feeding `five_questions.assumed[]` entries later at P4.
  `zero_vs_bottom` itself lives in `claim_card.five_questions.separates`
  (`schema/claim_card.schema.json`) — one home, referenced here, not redefined.

## Gate

Self-check only at this stage (`READY_FOR_S2`, not a release gate) — FOUNDATION §2.2 states this
explicitly: the intake gate is a readiness check the intake-taker runs, not an independent-check
gate (that arrives later, at P6).

## Human / AI division of labour

Human: states the issue in their own words and owns the standpoint (FOUNDATION §2.2, S1 row).
AI: routes the intake — may ask clarifying questions to help the human sharpen what difference the
issue names — but **never infers Q2's answer** (who is affected vs. who holds power) on the
human's behalf; that inference risk is exactly what the stakeholder≠agency non-collapse guards
against.

## Disclaimers emitted

`D-STANDPOINT` (front matter, from P1) · `D-SCOPE` (once `scope.generalization_claimed` is first
touched at intake, even if left at `none`).

## Non-collapse pairs enforced

`NC-62` Stakeholder≠Agency · `NC-25` 0≠⊥ · `NC-26` "not checked"≠"checked, nothing found" ·
`NC-27` LOCAL_EVIDENCE_NOT_FOUND≠NO_LOCAL_EVIDENCE_EXISTS (the intake-stage form of the same
guard, closed fully at P5).

## What this card does NOT do

It does not produce a claim card — intake produces a Problem Card only; the claim card (P3) is a
later, separate artifact. It does not resolve stakeholder conflicts or decide whose interest wins —
mapping stakeholder≠agency is descriptive, not adjudicative. It does not advance
`scope.generalization_claimed` past `none` at this stage (FOUNDATION §2.2, S2 row's rule applies
by extension: intake is even earlier than S2, so no generalization claim is legal yet).
