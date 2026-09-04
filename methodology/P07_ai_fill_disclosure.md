> tier: Dr (specified; independently unreviewed)

# P7 — AI-Fill Disclosure (six-way audit per Readout Condition §8.2; AI output ≠ evidence)

## One-line rule

Every distinction AI contributed to a claim is disclosed, route-level, next to the specific claim
it touches — never as one blanket paragraph far away — split across the six audit categories the
Readout Condition names, and none of it is ever treated as evidence in its own right.

## Why

`design/FOUNDATION_v0.5.md` §3.1 (Q3, "AI เติมอะไร") ties this directly to Disclosure (D of E-A-D)
applied to a six-way AI-audit split, and chair ruling D2 states the mechanical limit honestly: the
kernel "can confirm every sub-field is explicit ('none identified' or filled), not that the AI's
self-report is complete or honest" — `silent_lift_check` is the one mechanized cross-check, and it
compares *represented* against *actual* dependency sets computed from the provenance DAG, never by
re-doing the epistemic work by hand. The Readout Condition itself is E∧A∧D jointly: "a card that
answers Q1/Q2/Q4 honestly but misattributes Q3 — crediting the source with a distinction AI
actually supplied — fails the condition even though every field looks filled" (§3.1). The `D-AIFILL`
placement rule ("never one blanket paragraph, far from the claim it discloses") is cited directly
in §3.3's own heading-rename rationale as the standard this document holds *itself* to, having
been caught failing it once (present-tense "enforced" language sitting 550 lines from its own
untested-prose disclaimer, per `reviews/COMPLETENESS_CRITIC.md` §5).

## Inputs → outputs

- Input: every point in P0–P6 where an AI session drafted, proposed, or computed something that
  entered a claim card.
- Output: `claim_card.five_questions.ai_filled` (`schema/claim_card.schema.json`) — full shape's
  six named sub-fields (`current_evidence, retrieved_tool_evidence, retained_record_route,
  model_calibration_assumption, prompt_system_constraint, decision_policy`), each explicit "none
  identified" or filled, never omitted; or the stub shape's `{used: bool, note: string}` (§3.2a,
  `note` required whenever `used: true`). Also feeds `claim_card.silent_lift_check
  {represented_dependency_set, actual_dependency_set, flags, status: not_run | run}` and
  `claim_card.provenance_dag {..., status: not_run | run}`.

## Gate

`silent_lift_check.flags` non-empty is a **hard failure**, blocking `status` advancement — not a
disclaimer (§3.3 rule 7). `provenance_dag.status` and `silent_lift_check.status` must both be
`run` (never left at the default `not_run`) before `k_state` may advance past K0, or before a card
may be cited from a CLAIM_MATRIX (§3.3 rule 11, chair ruling item 12) — the kernel treats `not_run`
as **⊥ (unknown)**, never as "checked, nothing found" (`NC-25`/`NC-26` applied to the kernel's own
gate, closing the gap where a user previously had no legal way to leave these fields honestly
unfilled pre-kernel, visibly distinguishable from a checked-and-clean result).

## Human / AI division of labour

AI: fills every `ai_filled` sub-field itself, discloses every inferential commitment it
contributed, and never advances a sub-field to "none identified" without actually checking.
Human: is the one who judges whether the AI's self-report is complete — since the kernel cannot
mechanically prove that (chair ruling D2) — and holds the epistemic responsibility for the finished
claim regardless of how much AI drafted (`NC-58`).

## Disclaimers emitted

`D-AIFILL` (any non-empty `ai_filled.*`, placed route-level next to the specific claim) ·
`D-SILENT-LIFT-GUARD` (the operational D in E-A-D, card `assumed`/`ai_filled` fields).

## Non-collapse pairs enforced

`NC-14` Existence≠Attribution≠Disclosure (E-A-D) · `NC-15` represented≠actual essential dependency
set (Silent Lift) · `NC-47` AI output≠Evidence · `NC-55` Discovery≠Justification · `NC-56` AI
exploration≠Human commitment · `NC-58` AIContribution≠EpistemicResponsibility · `NC-61` questions
defended without AI≠questions merely produced with AI.

## What this card does NOT do

It does not certify that an AI-fill disclosure is complete — only presence-checkable, per chair
ruling D2 (there is no mechanical test for a contribution that was never disclosed at all). It does
not promote AI output to evidence under any circumstance, however well-corroborated it later turns
out to be (`NC-47` is absolute, not a threshold). It does not run independently of P6 — a
`silent_lift_check` with non-empty flags still requires the independent-check machinery to resolve,
not a re-run of this card alone.
