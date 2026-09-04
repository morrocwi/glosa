> tier: Dr (specified; independently unreviewed)

# P0 — Lens (readout-not-truth; lens-in / lens-out round trip)

## One-line rule

Before touching evidence for any claim, translate the problem **into** the readout vocabulary
first (lens-in), analyse there, then translate **back** into world/discipline language (lens-out)
— never analyse a problem directly in world-language and call the result rigorous.

## Why

Founder ruling, request 20, 2026-09-04 (`HANDOFF_2026-09-04_founding-meeting.md` §6, "THE SPINE" —
*"เริ่มจากมองปัญหาด้วยเลนส์ readout ก่อน แล้วแปลกลับเป็นภาษาโลกเพื่อสกัดสมมติฐาน — อันนี้คือแกนเลยนะ"*),
carried into `design/FOUNDATION_v0.5.md` §2.1 as "the spine is a round trip." The worked
demonstration (`cases/worked-example-cat.md`, request 26) shows what skipping lens-in produces: an
AI's unlensed "probably cystitis" collapsed a household-decision question ("ไม่เป็นที่" = a
contaminated concept, a human decision policy dressed as an observation) into a diagnosis it had
no access route to. FOUNDATION §2.3 names the three internal registers this card must never
collapse: R1 (readout formulation) and R2 (world-language hypothesis), both living beside — never
replacing — the raw human line in the Blackbox Note.

## Inputs → outputs

- Input: a Blackbox Note line (`templates/knowledge/blackbox_note.yaml`) carrying the problem as
  first met, verbatim.
- Output: `claim_card.lens_translation` (`schema/claim_card.schema.json`) — specifically
  `question_human` (the lens-in target's own record of the question as lived),
  `question_readout` (R1), `local_contrast_space_X`, `access_relation_R`, `claim_function_Phi_z0`,
  `formal_applicability` — and the top-level `hypothesis_world` field (R2), which points back via
  `hypothesis_world.falsifier_ref` to `five_questions.tested.falsifier`.
- Every field name above is defined once, in `schema/claim_card.schema.json`; this card only
  narrates the *order of operations* (lens-in before analysis, lens-out before the hypothesis is
  stated), never a second copy of the field list (`design/FOUNDATION_v0.5.md` §3.2 is the one
  home).

## Gate

`lens_translation` must be filled **before** `five_questions` (FOUNDATION §2.2, S3 exit gate) —
the kernel-side version of this ordering rule is `validate_claim_card`'s field-presence check,
specified but not yet implemented (`design/FOUNDATION_v0.5.md` §9, §3.3 heading note).

## Human / AI division of labour

Human: owns `question_human` (the verbatim question as lived) and the falsifier judgment in
`hypothesis_world`. AI: may draft the lens-in formulation (`question_readout`,
`local_contrast_space_X`, `access_relation_R`) from the human's stated problem, but every such
contribution is disclosed under P7, never silently folded into `question_human`.

## Disclaimers emitted

`D-STANDPOINT` (always on, front matter), `D-AIFILL` (whenever AI drafted any lens_translation
sub-field).

## Non-collapse pairs enforced

`NC-08` readout≠truth (universal lens) · `NC-14` Existence≠Attribution≠Disclosure (E-A-D) ·
`NC-22` access model K̃≠literally reading K* · `NC-25` 0≠⊥.

## What this card does NOT do

It does not itself decide *what* the readout formulation says (that is P3's Five Questions) —
lens-in/lens-out is an ordering discipline, not a content generator. It does not license skipping
the round trip for a claim that "looks obviously narrative" — `formal_applicability:
not_applicable_narrative` (§3.2b) is still a lens_translation value the round trip must record, not
an exit from the round trip. It does not certify anything — no independent check runs at this
stage (that is P6).
