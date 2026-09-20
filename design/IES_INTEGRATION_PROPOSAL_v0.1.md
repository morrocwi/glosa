# IES Integration Proposal v0.1 — a Statistical Evidence Layer for the Literature Review System

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.
> **Status: PROPOSAL ONLY, PENDING FOUNDER DECISION — not adopted, not built, not part of the
> binding methodology.** Mirrors the decision-pending pattern already used for the discovery-routing
> and claim-tier-intake extensions (`FOUNDATION_v0.6.md` §7.9). Does not edit
> `methodology/P13_literature_review.md`, `design/S14_literature-review-system.md`,
> `design/FOUNDATION_v0.6.md`, or any schema file — those remain the founder's call after reviewing
> this proposal.
>
> **Source:** a working methodological knowledge base titled "Inferential Evidence Synthesis (IES)"
> (external draft, 2026-09-20, ~2300 lines), which already contains its own extensive read of
> glosa's LRS (its own §5, citing `S14_literature-review-system.md`, `FOUNDATION_v0.6.md`,
> `templates/knowledge/search_log.yaml`, `citation_card.yaml`, `dialogue_table.md`,
> `litreview_manifest.yaml`, `hypothesis_selection.yaml`) and proposes a Statistical Evidence Layer
> extension (its own §6, §24–25). This proposal verifies IES's reading against the live files in
> this repo, corrects/confirms it, and reformats the extension as a glosa-native additive patch
> rather than restating IES's own document.

## 1. What IES is, and its relationship to glosa's LRS

IES is an integrative methodological architecture for treating a literature corpus as an auditable
evidence dataset, built explicitly on top of established methods (systematic review, meta-analysis,
SWiM, qualitative evidence synthesis, realist review, GRADE, generalizability theory) plus glosa's
own LRS as a "methodological anchor" (its own §5). Its own Appendix D is explicit that only
established-external-methodology statements should be treated as settled; its integrative
architecture and proposed new objects (Statistical Evidence Layer, commensurability gate,
inferential claim object) are "proposals to be challenged... not established methodology" — the
same posture this proposal file takes toward glosa.

**Verified against the live repo (not just IES's own citations):**
- IES §5.5's claim that `citation_card.yaml` separates `metadata_verified` from
  `claim_match_verified` is accurate — confirmed directly in
  `schema/citation_card.schema.json:53-83` (two independently-flaggable booleans, `NC-18` cited at
  line 69) and `FOUNDATION_v0.6.md:1684-1685`.
- IES §5.7's claim that accuracy and diversity are separate gates is accurate — confirmed in
  `methodology/P13_literature_review.md:47-52` and `FOUNDATION_v0.6.md:1758-1770` (accuracy gate
  §5.5, diversity gate §5.6 of S14, asymmetric fail/downgrade semantics).
- IES §5.2's "one hypothesis, one LRS run" claim is accurate — `P13_literature_review.md:28-29`,
  `FOUNDATION_v0.6.md:1762-1765`.
- **One drift worth flagging, found while verifying, not part of IES's own claims:** the
  `glosa-literature-review` skill card (`plugins/glosa/skills/glosa-literature-review/SKILL.md`,
  "New this pass (v0.6)" section) states the claim-tier-intake and discovery-routing extensions are
  "PENDING FOUNDER DECISION," but `FOUNDATION_v0.6.md:1747-1841` (§7.9) explicitly marks both
  **"DECIDED (founder, delegated..., BBL-2026-09-05-122)."** This is a stale skill-card vs. current
  FOUNDATION mismatch, unrelated to IES — flagged here per this repo's own "flag, don't silently
  resolve" convention, not fixed by this proposal (out of scope for an IES integration patch).

## 2. IES chain mapped onto glosa's L1–L6 (node for node)

| IES evidence-selection chain (§1, §4) | glosa LRS stage | Match |
|---|---|---|
| Knowledge target | L1 question framing (`search_log.yaml.frozen_scope`, seeded from `hypothesis_world`) | Same concept, glosa's name is narrower (tied to one hypothesis, not a general "target") |
| Potential evidence universe / Accessible evidence universe | L2 search protocol (`frozen_scope`, `search_mode`) | Same concept |
| Recorded/published evidence, Retrieved evidence | L2–L3 (`search_log.yaml.sources_found`, `source_acquisition_log.yaml`) | Same concept |
| Eligible evidence | L3 acquisition (`acquisition_status ∈ {obtained, abstract_only, not_obtained}`) | Same concept, glosa's is a 3-value enum rather than a separate "eligible" stage; IES's "eligible" (met inclusion criteria) is arguably a sub-step of glosa's L2 `frozen_scope` inclusion/exclusion rules, not a separate gate |
| Analytic evidence set | L4 reading & extraction, feeding L6 `citations[]` | Same concept |
| Synthesis | **Not present as a stage** — glosa's L4 dialogue-table is qualitative-only (agrees/disagrees/orthogonal), no statistical synthesis step | **Genuine gap** — see §3 |
| Inference | **Not present as a distinct artifact** — glosa's manifest freezes evidence, but no downstream "claim" object exists in the LRS schemas themselves (claim cards exist upstream, per §3 of FOUNDATION, not as an LRS output) | **Partial gap** — see §3 |
| Inference boundary | Disclaimers (`D-LIT-CONCENTRATED`, `D-LIT-NOT-OBTAINED`, `D-LIT-MODE`) come close but are per-manifest flags, not a structured per-claim boundary statement (IES §12 Level 8: "Supported for / Not established for / Evidence absent for / Known counterconditions / Primary uncertainty") | **Partial gap** — see §3 |

**Conclusion of the mapping:** IES's evidence-selection chain (target → universe → retrieved →
eligible → analytic set) is **already covered, under different names, by L1–L4** — this is not new
ground, and no new stage should be added to duplicate it. The genuine gap starts **after** L4/L6:
glosa's LRS freezes a *verified, diverse evidence set*; it does not yet define what happens when
that set contains quantitative effect estimates that could be statistically synthesized, nor does
it define a structured claim/inference-boundary object downstream of the manifest.

## 3. What IES adds that glosa's LRS genuinely lacks

Confirmed by reading `S14_literature-review-system.md` in full and the manifest/citation-card
schemas: **glosa's current LRS has no statistical-synthesis concept at all.** `dialogue_table.md`
is qualitative (stance: agrees/disagrees/orthogonal/undetermined), and `litreview_manifest.yaml`'s
`citations[]`/`diversity_audit`/`accuracy` fields track citation-level verification and corpus
diversity, not effect sizes, pooling, heterogeneity, or generalization assessment. This is a real,
non-overlapping gap IES fills:

1. **Statistical Evidence Layer** (IES §6–§11): a `statistical_evidence_record` object per
   study/outcome (IES §24) — design, population, construct, reported statistic, reconstruction
   flags, dependency structure, verification. No glosa schema covers any of this today.
2. **Commensurability gate** (IES §17): an explicit `POOL | STRATIFY | DO_NOT_POOL | UNRESOLVED`
   decision before any pooling — glosa has no equivalent gate for quantitative synthesis (its
   accuracy/diversity gates are about citation verification and corpus composition, not statistical
   poolability).
3. **Generalization matrix** (IES §21, §43): a structured population/geography/institution/
   technology/outcome/time/context table comparing evidence-represented vs. intended target, with
   an explicit narrowing rule. Glosa's `diversity_audit` is the closest existing mechanism but
   measures corpus composition (language/discipline/source-type/geography/stance), not a target-vs-
   represented gap analysis tied to a specific claim.
4. **Inference boundary as a structured object, not a disclaimer** (IES §12 Level 8, §30
   `inferential_claim` object): "Supported for / Not established for / Evidence absent for / Known
   counterconditions / Primary uncertainty" as a required field set on every final claim. Glosa's
   disclaimer mechanism (`D-LIT-*`) flags manifest-level concerns but has no per-claim structured
   boundary object downstream of the LRS.
5. **Certainty-of-evidence record** (IES §14, borrowing GRADE's logic): bias/inconsistency/
   indirectness/imprecision/publication-bias as named, separately-scored dimensions. Glosa's
   `accuracy`/`diversity_audit` gates are adjacent but score different things (citation correctness
   and corpus composition, not the GRADE-style certainty-in-the-body-of-evidence judgment).

## 4. What glosa already has that this proposal must not weaken or duplicate

IES itself already names most of these as inherited safeguards (its own §44), verified here against
the live files rather than taken on IES's word:

- Source-first citation, `metadata_verified ≠ claim_match_verified`, the secondary-citation ban
  (`FC-S14-1`) — `citation_card.schema.json`, `P13_literature_review.md:60-62`.
- One-hypothesis-per-run, never merged — `P13_literature_review.md:28-29`.
- Frozen scope before results — `search_log.yaml.frozen_scope`, `P13_literature_review.md:36`.
- Support/challenge query separation — `FOUNDATION_v0.6.md` (via S14, cited but not re-quoted here
  per one-fact-one-home).
- Accuracy gate ≠ diversity gate, asymmetric fail/downgrade — `FOUNDATION_v0.6.md:1758-1770`.
- Human-owned hypothesis selection, never AI-alone — `P13_literature_review.md:64-69`.
- Maker ≠ checker (`CLAUDE.md` rule 3) — directly relevant to IES §39.1's own proposed reviewer-
  agreement validation study and to any statistical-extraction verification step this proposal adds.

**Any adopted version of this proposal must compose with these, not replace or duplicate them** —
e.g. a new statistical-extraction verification step should reuse the existing `independence_class`
(I0–I5) ladder rather than inventing a parallel verification vocabulary, and a new
inference-boundary object should reuse existing `D-LIT-*` disclaimer ids where they already cover
the same trigger rather than minting duplicates (the same "S14 mints no duplicate vocabulary for a
trigger an existing id already covers" discipline `FOUNDATION_v0.6.md:1841` already states).

## 5. Where IES and glosa's framing genuinely differ (not papered over)

- **IES is domain-general and includes quantitative meta-analysis methodology (Cochrane-style)
  glosa's LRS was never designed for.** Glosa's LRS was built for a solo-scholar, claim-card-driven
  workflow where a hypothesis is usually being *tested against* a small, purpose-searched
  literature, not a full Cochrane-style systematic review with pooled effect sizes as the primary
  output. Importing the full Statistical Evidence Layer wholesale risks over-building for a use case
  (formal meta-analysis with 10+ commensurable studies) that may be rare in glosa's actual usage —
  this proposal recommends adopting the **schema objects and gate logic** (§6 below) without
  requiring every LRS run to attempt statistical synthesis; `statistical_synthesis.applicable: false`
  should be the honest default for most runs, not a rare exception.
- **IES's "evidence unit map" (paper ≠ study ≠ sample ≠ comparison ≠ outcome ≠ follow-up ≠
  estimate, §19)** has no equivalent granularity anywhere in glosa's schemas, which track at the
  citation-use level (one card per source backing one exact claim). This is a genuinely finer unit
  distinction than glosa currently makes, needed only when statistical pooling is attempted — this
  proposal scopes it as an additive field on the new `statistical_evidence_record`, not a change to
  `citation_card.schema.json`'s existing one-card-per-use model.
- **No direct conflict was found** between IES's principles and glosa's Non-Collapse Table
  (`FOUNDATION_v0.6.md` Appendix A) — IES's own §44 explicitly lists the non-collapse pairs it
  inherits (`Source existence ≠ claim support`, `Claim scope ≤ evidence scope`, etc.) and they match
  glosa's existing pairs rather than contradicting them.

## 6. Concrete proposed additions (additive only, schema versions bumped, nothing removed)

**6.1 New schema file (proposed): `schema/statistical_evidence_record.schema.json`**
Fields per IES §24, adapted to glosa naming conventions (`snake_case`, explicit null defaults,
`$ref` to `common.defs.json` where an existing enum already fits — e.g. reuse `independence_class`
for the `verification.independently_checked_by` route rather than inventing a new ladder):
`record_id`, `citation_card_ref` (FK into `citation_card.schema.json`, since the statistic must
trace back to a verified source-first citation, not stand alone), `study_id`, `sample_id`, `design`,
`population`, `construct`, `reported_statistic`, `reconstruction`, `effect_for_synthesis`,
`dependency`, `risk_of_bias_ref`, `verification`, `synthesis_eligibility`.

**6.2 New schema file (proposed): `schema/commensurability_gate.schema.json`**
Per IES §17, as a required upstream gate before any `statistical_synthesis.model` is filled in on
the manifest extension below — `decision: POOL | STRATIFY | DO_NOT_POOL | UNRESOLVED` with a
required `reason` field, mirroring the existing `gate.overall` pattern in
`litreview_manifest.schema.json` (never silently defaulting to POOL).

**6.3 Additive block on `litreview_manifest.schema.json` (proposed, optional, default inert):**
`statistical_synthesis: { applicable: bool (default false), synthesis_question, included_statistical_records: [], dependence_audit, commensurability_ref, model, summary, moderators, sensitivity_analyses, publication_bias_assessment, generalization_matrix, inference_boundary }`
— mirrors the existing `discovery_routing: { used: bool, ... }` additive-block pattern already in
this schema (`FOUNDATION_v0.6.md:1900-1907`), so `applicable: false` (default) means the block does
not apply and none of its sub-fields are required, exactly matching that precedent's `used: false`
semantics.

**6.4 New object type (proposed): `inferential_claim`** per IES §30, living downstream of the LRS
manifest (not inside it) — this is closer in spirit to the existing claim card (`FOUNDATION_v0.6.md`
§3) than to an LRS artifact, so the founder-decidable question is whether this becomes a new
additive block **on the claim card itself** (an `evidence_synthesis_boundary` field naming Supported
for / Not established for / Evidence absent for / Known counterconditions / Primary uncertainty)
rather than a wholly new schema file — this proposal recommends the claim-card-field route to avoid
a fourth "one fact, many homes" object, but flags it explicitly as the founder's call, not decided
here.

**6.5 Kernel rule (proposed, unbuilt):** mirroring `rule22`/`rule25`'s pattern
(`P13_literature_review.md:112-118`, `:90-95`) — a new rule requiring `statistical_synthesis.
commensurability_ref` to resolve to a real `commensurability_gate` record with
`decision != UNRESOLVED` before `statistical_synthesis.model` may be non-`none`, so a manifest
cannot silently pool without having actually run the gate.

## 7. What this proposal explicitly does NOT do

- Does not touch any binding file (`P13_literature_review.md`, `S14_literature-review-system.md`,
  `FOUNDATION_v0.6.md`, any `schema/*.json`, any `templates/knowledge/*`).
- Does not claim IES is validated methodology — per IES's own Appendix D, only the established
  external methods it cites (meta-analysis, GRADE, PRISMA, SWiM, realist review) are settled
  practice; the integrative architecture and every new object listed in §6 above are proposals.
- Does not resolve the stale skill-card-vs-FOUNDATION discrepancy noted in §1 — that is a separate,
  unrelated fix.
- Does not build any kernel rule, validator, or CLI verb — §6.5 names what would need building, not
  what has been built.

## 8. Recommended next step (not a decision, a recommendation)

If the founder wants to adopt this: (a) rule on §6.4's placement question (new object vs. claim-card
field) first, since it affects the other schema shapes; (b) draft the two new schema files (§6.1,
§6.2) as their own PR, reviewed independently per this repo's maker≠checker≠approver rule (`CLAUDE.md`
rule 3) — the same session that drafted this proposal should not self-approve the schemas; (c) run
one real LRS hypothesis end-to-end with `statistical_synthesis.applicable: true` as the acceptance
test, the same "worked example, honestly shown failing or passing" standard S14 §10 already set for
the base LRS, before treating any of this as more than Dr-tier.
