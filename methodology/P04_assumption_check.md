> tier: Dr (specified; independently unreviewed)

# P4 — Assumption Check (typed augmentation; contaminated-concept table; identification ladder)

## One-line rule

Every non-source distinction a claim relies on — an access augmentation, a contrast-relevance
operation, an inferential commitment, a decision-policy augmentation — is named, typed, and given
an identification level; a full-text scan against the contaminated-concept table catches concepts
that smuggle a decision policy in as if it were an observation.

## Why

The worked example (`cases/worked-example-cat.md`, request 26, 2026-09-04) is the canonical
demonstration: "ไม่เป็นที่" ("not in its place") reads as an observation but is actually a
contaminated concept — a human decision policy about where urine belongs, dressed as a fact about
the cat. The AI's own "probably cystitis" in that example is a separate failure mode: an
inferential commitment drawn from a model prior, not from the case's own access route — exactly
what `five_questions.assumed[]`'s `type: inferential_commitment` and `ai_filled` (P7) exist to
catch and disclose rather than let ride silently. Chair ruling D2 (`design/FOUNDATION_v0.5.md`
§3.1, Q4 row) states plainly that the kernel can check that a listed assumption carries an
`identification_level`; it cannot prove the list is complete — "there is no mechanical test for an
assumption that was never entered at all," which is exactly why this card's discipline (naming
every augmentation deliberately, not waiting for the kernel to catch a gap) carries the real
weight.

## Inputs → outputs

- Input: the `lens_translation` block (P0) and the claim's `statement` (P3) — read for anything
  smuggled in as fact.
- Output: `claim_card.five_questions.assumed[]` (`schema/claim_card.schema.json`) — each entry
  `{id: "A#", type: access_augmentation | contrast_relevance_operation | inferential_commitment |
  decision_policy_augmentation, description, identification_level: "A0".."Am" | unidentified,
  contaminated_concept_hit}`. Also feeds `claim_card.identification_ladder.layers[]` and
  `.per_rival[]`.

## Gate

The full-text scan of `statement`, `assumed[].description`, and `ledger.*` against the
contaminated-concept table (Appendix C) fires `EXTERNAL_VALIDATION_PROPOSED` as a **hard fail**
whenever text proposes "getting external review to confirm this" as a legitimacy lever (§3.3 rule
8, `EPIS-KNOWLEDGE-VALIDATION`) — the one contaminated-concept hit this repo's own kernel rules
name explicitly as mechanically checkable text-matching, distinct from the harder, judgment-based
hits this card's human discipline must still catch.

## Human / AI division of labour

Human: judges whether a candidate assumption is actually load-bearing (does removing it change the
claim?) and assigns the `identification_level` for any assumption touching lived judgment (e.g. a
decision-policy augmentation about what "counts"). AI: proposes candidate assumptions from the
statement text, including flagging suspected contaminated-concept hits, but its own proposals are
themselves `ai_filled` entries (P7) — an AI's assumption-list is a candidate list, not a settled
one.

## Disclaimers emitted

`D-SILENT-LIFT-GUARD` (operational D in E-A-D, fires whenever an essential dependency is found
beyond the named source) · `D-AIFILL` (any AI-proposed assumption) · `D-EXTERNAL-INPUT` (any
assumption drawing on a vetted external skill/repo/paper).

## Non-collapse pairs enforced

`NC-15` represented≠actual essential dependency set (Silent Lift) · `NC-16` doxastic warrant≠
assertoric disclosure · `NC-20` reliable route≠crediting a specific source · `NC-21`
training-derived background≠current-case-specific access route.

## What this card does NOT do

It does not complete the identification ladder by itself for every rival — `per_rival[]` requires
naming rivals first, which is a substantive judgment call this card records but does not automate.
It does not decide the claim's tier — a fully typed assumption list with honest
`identification_level`s can still back only a `Dr`-tier claim if no `evidence_relation` reaches the
independence class §3.3 requires (that gate is P6). It does not retroactively fix a contaminated
concept already baked into an upstream Blackbox Note line — the note is never edited in place; a
correction is a new line (P15).
