> tier: Dr (specified; independently unreviewed)

# P3 — Claim Card (five questions ⇄ E-A-D; stub vs full)

## One-line rule

One claim-level distinction gets one claim card, answering the founder's five questions
(seen / separates / AI-filled / assumed / tested) which mechanically map onto the Readout
Condition's Existence-Attribution-Disclosure norm — in one of exactly two legal shapes, `stub` or
`full`, never a third improvised shape.

## Why

The five-questions crosswalk is `design/FOUNDATION_v0.5.md` §3.1, itself an "instantiation of the
paper's own 'three practical questions'" from the Readout Condition (§1.2), operationalizing E-A-D
into a schema. The founder set the questions directly (request 20/24 lineage,
`HANDOFF_2026-09-04_founding-meeting.md` §6). The two-shape resolution is chair ruling B2 (2026-
09-04, `design/FOUNDATION_v0.5.md` §3.2a), closing v0.1 §10 dispute 2 — a fight between "an
ordinary person with no lab/team can open this and start working immediately" (founder request 1)
and schema purity: a full card's authoring cost would make a frontline user simply not use the
tool, defeating `the internal build plan (local file, not public)` §0's purpose, while an unguarded lightweight shape risked "silent
lift" of an under-evidenced stub into a published claim. The stub `ai_filled` shape
(`{used, note}`) was itself a fix (must-fix 9, `reviews/FOUNDATION_v0.2_usability.md` finding
(b)) for a documented usability gap: two frontline users had each invented a different
undocumented shape before this pass defined one.

## Inputs → outputs

- Input: `lens_translation` (P0), `standpoint` (P1), the Problem Card (P2).
- Output: `claim_card` per `schema/claim_card.schema.json` — the full field list lives there and
  only there (FOUNDATION §3.2 narrates it, does not redeclare a second copy). Key groups this card
  is directly responsible for: `five_questions.{seen, separates, ai_filled, assumed, tested}`,
  `shape: stub | full`, `claim_type`, `genre` (handed to P13 for routing).

## Gate

**Chair ruling D2** (`design/FOUNDATION_v0.5.md` §3.1): Q1 (seen), Q3 (ai_filled), Q4 (assumed)
are *presence-checkable only* by the kernel — it can confirm a field is filled, never that the
content is correct or complete. Only Q5 (tested, via `independent_check`) is genuinely
mechanically enforceable (pairwise-distinct maker/checker/approver, §7.2; tier-vs-independence
gates, §3.3). A `shape: stub` card is hard-blocked from advancing `status` past `Draft` and from
being cited from a CLAIM_MATRIX (§3.3 rule 10, chair ruling B2).

## Human / AI division of labour

Human: owns the falsifier judgment inside `tested.falsifier` and the standpoint underlying `seen`
(FOUNDATION §2.2, S3 row). AI: fills `ai_filled.*` (full shape's six sub-fields, or the stub's
`{used, note}`) and discloses every inferential commitment it contributed — never silently
advances `ai_filled` to "none identified" without checking.

## Disclaimers emitted

`D-TIER` (every quantitative/factual claim) · `D-AIFILL` (any non-empty `ai_filled.*`) ·
`D-SCOPE` · `D-NONCLAIM` (paired with the required `non_claims` field, minItems 1) ·
`D-CANDIDATE-STATUS` (any artifact not yet through an I4/I5 check).

## Non-collapse pairs enforced

`NC-01` World≠Record≠Readout≠Meaning≠Truth≠Warrant≠Knowledge-Attribution · `NC-14`
Existence≠Attribution≠Disclosure (E-A-D) · `NC-35` Observation≠Claim≠Inference≠Hypothesis≠
Decision · `NC-57` Claim scope≤Evidence scope · `NC-63` Representationality≠Selectivity.

## What this card does NOT do

It does not license itself as public or citable at `shape: stub` — a stub is a legal, lower-cost
K0 working object, never a published claim (§3.2a). It does not run the independent check itself
(P6 owns that) — `independent_check.status` starts `NONE` on every new card. It does not decide
genre (P13 reads the completed card to route it) and does not resolve the licensing test's
*correctness* (`separates.licensing_test.result`) — the card only records the result someone
else's method produced, honestly, at whatever independence level backs it.
