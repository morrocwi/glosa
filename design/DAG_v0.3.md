# glosa v0.3 — S3 improvement DAG (human-readable)

Source of truth: `design/DAG_v0.3.yaml`. Rendered graph: `docs/dag_v0.3.svg` (and `docs/dag_v0.3.dot` for `dot -Tsvg` if graphviz is later installed — it was not present on this workstation when this was generated, so `docs/gen_dag_svg.py` drew the SVG directly).

Readout, not truth: every node traces to a knowledge-harvest card id (`knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md`), a literature-review digest row (`records/lit/glosa-v0-3/DIGEST.md`), a publish-gate finding (`reviews/PUBLISH_GATE_v1_public.md`), or a CHANGELOG/TODO WARN item. No node is a decision until it is a row in the internal command-center's DECISIONS ledger (private).

**Counts:** 26 nodes, 25 edges — proposed=21, done=3, deferred=2. By kind: process=1, kernel=6, foundation=14, schema=3, docs=1, cli=1.

## Node table

| id | title | kind | status | target | evidence | human decision? |
|---|---|---|---|---|---|---|
| `eng.registry-check-ci-safe` | Registry check made CI-safe | process | done | kernel/glosa_kernel.py (validate_release_manifest) + CI workflow | kc-ep-051 | no |
| `eng.lit-manifest-fail-closed` | Literature-review manifest fails closed | kernel | done | kernel/glosa_kernel.py (validate_citation_card, validate_release_manifest) | kc-base-039, kc-ep-046 | no |
| `foundation.s1.0-infinity-tension-flag` | Infinity-as-transcendental-ground stays a flagged [Open] tension | foundation | deferred | FOUNDATION §1.0 Pillars | kc-ep-005 | no |
| `foundation.s1.0-ashari-ontology-analogue` | Partial theology-neutral ontology analogue (2 of 3 constructs) | foundation | proposed | FOUNDATION §1.0 Pillars — ontology | kc-ep-030, kc-ep-034 | yes |
| `foundation.honest-edges-agrippa` | Agrippa's trilemma applied to the tier system itself | foundation | proposed | FOUNDATION §12 Honest edges | kc-base-025, kc-base-031, kc-base-036 | no |
| `foundation.disclaimer-catalogue-expand` | Disclaimer catalogue — priority-scoping and standpoint-disclosure patterns | foundation | proposed | FOUNDATION §5 Systematic disclaimer catalogue | kc-he-013, kc-he-015, kc-he-019, kc-islam-007, kc-islam-016, kc-se-006 | no |
| `kernel.rule17-source-first` | Rule 17 — source-first citation | kernel | done | kernel/glosa_kernel.py rule17 / rule17w (validate_citation_card) | kc-base-039, kc-ai-019, kc-ep-046 | no |
| `foundation.pillars-readout-not-truth` | Pillars §1.0 cross-tradition citation set | foundation | proposed | FOUNDATION §1.0 Pillars — ontology/epistemology/methodology | kc-base-001, kc-base-005, kc-base-009, kc-base-027, kc-base-032, kc-ep-014, kc-ai-019, kc-islam-008 | no |
| `foundation.s5-scope-boundary-per-instance` | Non-clinical/non-medical/non-legal scope clause stays per-instance | foundation | proposed | FOUNDATION §5 Systematic disclaimer catalogue | kc-ai-023, kc-he-016 | yes |
| `kernel.unverified-verifiability-flag` | "Verifiable with no stated procedure" as a named narrow sub-case | kernel | proposed | FOUNDATION §5 disclaimer catalogue / kernel rule 17 | kc-tourism-006 | no |
| `docs.blackbox-log-formalize-source` | Blackbox Log named-origin citation | docs | proposed | FOUNDATION §2.3 Blackbox Note and R0/R1/R2 internal registers | kc-ep-047, kc-ai-008 | no |
| `foundation.non-collapse-table-expand` | Non-Collapse Table Appendix A — cross-tradition rows | foundation | proposed | FOUNDATION Appendix A Non-Collapse Table | kc-base-004, kc-base-021, kc-ep-021, kc-ep-023, kc-ep-024, kc-ep-026, kc-ep-027 | no |
| `foundation.responsibility-arrow-mother-eq` | Mother-equation framing for the Data→Inference→Claim arrow | foundation | proposed | FOUNDATION §2.1b Responsibility per arrow | kc-base-014, kc-base-020 | no |
| `kernel.pcs-red-flag` | Premature Category Stabilization (PCS) as a scoped kernel red-flag | kernel | proposed | FOUNDATION §5/§6 disclaimer+genre-router; kernel contaminated-concept table (base-018) | kc-ep-018, kc-ep-019, kc-ep-020, kc-islam-011, kc-tourism-002 | yes |
| `schema.verdict-class-vocabulary` | Verdict-class vocabulary field (DERIVED/FORCED/DEFINITIONAL-RELABEL/POSITED/BORROWED-SCALE/OPEN) | schema | proposed | FOUNDATION field base_relation (holds\|refined_by_later_work\|superseded\|outdated\|open) | kc-base-038 | no |
| `schema.prereg-gate-fields` | Frozen-preregistration gate as checkable fields, not a hard block | schema | proposed | FOUNDATION §2.1a Problem before observation / §7.3 Bounded-Judge Law | kc-he-002, kc-he-004, kc-he-005, kc-he-006, kc-he-007 | yes |
| `kernel.gate-rules-taxonomy-i-z` | I1–I4/Z1–Z4 injected-infinity/zero taxonomy in kernel gate rules | kernel | proposed | FOUNDATION §3.3 Kernel gate rules (specified, Dr, untested) | kc-base-006, kc-base-008, kc-base-016, kc-base-018, kc-base-034 | no |
| `foundation.ead-crosswalk` | Existence-Attribution-Disclosure (E-A-D) norm as the named source of §3.1 crosswalk | foundation | proposed | FOUNDATION §3.1 Five Questions ⇄ E-A-D ⇄ field crosswalk | kc-ep-042, kc-aihp-011, kc-ai-001 | no |
| `schema.claim-card-comparison-evidence-field` | Comparison/evidence-strength field — descriptive-only, no outperformance claim | schema | proposed | FOUNDATION §3.2 Field list (claim card schema) | kc-se-001, kc-se-002, kc-se-007, kc-se-009 | no |
| `foundation.possession-constitution-collapse` | Possession-Constitution Collapse / knower-fetishism as the named AI-authorship rule source | foundation | proposed | FOUNDATION §3.2b / §7 Gates & review (AI-authorship rules) | kc-ep-043, kc-ai-003, kc-ai-004, kc-aihp-013, kc-aihp-014 | no |
| `foundation.independence-ladder-i0-i5-source` | I0–I5 Independence Ladder named source citation | foundation | proposed | FOUNDATION §4.2 Independence Ladder I0–I5 | kc-ep-052, kc-ai-002 | no |
| `cli.genre-router-layer-confusion-check` | Genre-router layer-confusion diagnostic | cli | proposed | FOUNDATION §6 Genre router | kc-islam-009 | no |
| `rule17.claim-card-certification-open` | Claim card replaces institutional certification: kept [Open] | kernel | deferred | kernel rule 17 / FOUNDATION §4.2 Independence Ladder I0–I5 | kc-ai-006, kc-aihp-002, kc-aihp-003 | no |
| `foundation.k-state-standalone-scholar-cite` | K-state (Standalone Scholar) named-origin citation | foundation | proposed | FOUNDATION §4.4 K-state (Standalone Scholar, PRESERVE_EXACT) | kc-ep-041, kc-aihp-017, kc-ai-011 | no |
| `foundation.lrs-discovery-loop-extension` | Discovery-loop extension (candidate-set formation precedes evidential adjudication) | foundation | proposed | FOUNDATION §7.9 Literature Review System (LRS) / §6 discovery extension | kc-ep-045, kc-ep-046, kc-ep-048, kc-ep-049, kc-aihp-005, kc-aihp-006, kc-aihp-010, kc-aihp-020 | yes |
| `foundation.s7.9-intake-tier-flag` | Claim-tier intake flag — thin addition, not a new mechanism | foundation | proposed | FOUNDATION §7.9 Literature Review System (LRS) | kc-ai-024, kc-he-018 | yes |

## Node detail (change / acceptance test / risk)

### `eng.registry-check-ci-safe` — Registry check made CI-safe
- **kind / status:** process / done
- **target:** kernel/glosa_kernel.py (validate_release_manifest) + CI workflow
- **change:** Registry self-report state-machine check (rule blocking method→released without a literature-review manifest) runs in CI, not only at release time, so a stage-skip (e.g. D-LIT-MODE) is caught before merge, not after tagging.
- **evidence:** kc-ep-051
- **acceptance test:** CI job fails a PR that advances registry stage past genre_routed without a PASS lit manifest.
- **risk:** Low — mechanical CI gate, already exercised by v0.1.0→v0.2.0 self-report gap it was built to catch.

### `eng.lit-manifest-fail-closed` — Literature-review manifest fails closed
- **kind / status:** kernel / done
- **target:** kernel/glosa_kernel.py (validate_citation_card, validate_release_manifest)
- **change:** A literature-review manifest with any non-conformant citation card (missing locator, wrong status) fails the whole manifest rather than silently dropping the bad card.
- **evidence:** kc-base-039, kc-ep-046
- **acceptance test:** Unit test: manifest with one card missing a locator field returns overall FAIL, not PASS-with-warning.
- **risk:** Low — already the shipped v0.2.0 behavior; carried here only to show DAG lineage into S3/S4.

### `foundation.s1.0-infinity-tension-flag` — Infinity-as-transcendental-ground stays a flagged [Open] tension
- **kind / status:** foundation / deferred
- **target:** FOUNDATION §1.0 Pillars
- **change:** Keep infinity-as-transcendental-ground logged as an explicitly flagged [Open] tension in FOUNDATION §1.0 rather than building a formal reconciliation section this pass; the flag must note the stance's historical load-bearing role and cross-cultural diffusion.
- **evidence:** kc-ep-005
- **acceptance test:** FOUNDATION §1.0 contains an [Open] block naming the rival stance and citing its historical-priority sources, not a silent omission.
- **risk:** Medium — defensible default, but two strong historical-priority sources mean a future version may need to revisit rather than leave permanently deferred.

### `foundation.s1.0-ashari-ontology-analogue` — Partial theology-neutral ontology analogue (2 of 3 constructs)
- **kind / status:** foundation / proposed (human decision needed)
- **target:** FOUNDATION §1.0 Pillars — ontology
- **change:** Adopt a theology-neutral structural analogue for "Dependent Identity" (grounding/ ontological-dependence theory) and "Directed Selection" (Principle of Sufficient Reason) as FOUNDATION §1.0 ontology primitives; do NOT attempt the same move for "Dependent Order"/kasb or the five registers of faqr as a whole — those stay islam-domain.
- **evidence:** kc-ep-030, kc-ep-034
- **acceptance test:** FOUNDATION §1.0 diff cites grounding-theory and PSR sources directly, with an explicit line excluding kasb/faqr from the analogue.
- **risk:** Medium — partial adoption is defensible from the evidence but risks looking arbitrary without the full reasoning carried into the commit message.

### `foundation.honest-edges-agrippa` — Agrippa's trilemma applied to the tier system itself
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §12 Honest edges
- **change:** Cite Agrippa's-trilemma-applied-to-the-tier-system and "what this system explicitly does NOT claim" cards in §12 Honest edges, as the named philosophical grounding for why the tier ladder is never treated as self-certifying.
- **evidence:** kc-base-025, kc-base-031, kc-base-036
- **acceptance test:** §12 diff adds a named subsection citing Agrippa's trilemma with the three evidence card ids as sources.
- **risk:** Low — citation-only addition to an already-existing honest-edges section.

### `foundation.disclaimer-catalogue-expand` — Disclaimer catalogue — priority-scoping and standpoint-disclosure patterns
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §5 Systematic disclaimer catalogue
- **change:** Add reusable disclaimer patterns to §5: "novelty scoped to architecture, not mechanism," "analytical tool, not verdict," "theoretical/analytical, not empirical," and reflexive practitioner standpoint/conflict-of-interest disclosure.
- **evidence:** kc-he-013, kc-he-015, kc-he-019, kc-islam-007, kc-islam-016, kc-se-006
- **acceptance test:** §5 diff adds 4 named reusable clause patterns, each with a worked source example distinct from foundation.s5-scope-boundary-per-instance's per-instance jurisdiction clause.
- **risk:** Low — additive catalogue entries with existing worked examples; distinct scope from the AI-runtime-specific clause in foundation.s5-scope-boundary-per-instance.

### `kernel.rule17-source-first` — Rule 17 — source-first citation
- **kind / status:** kernel / done
- **target:** kernel/glosa_kernel.py rule17 / rule17w (validate_citation_card)
- **change:** A citation card cannot leave CANDIDATE status unless quote/page/line/link fields were filled from the opened source at read-time, never reconstructed from memory afterward.
- **evidence:** kc-base-039, kc-ai-019, kc-ep-046
- **acceptance test:** Unit test: card with status VERIFIED but empty verbatim/locator field raises rule17 error, not rule17w warning.
- **risk:** Low — shipped 0.2.0; this DAG's own S1/S2 harvest cards were produced under this rule.

### `foundation.pillars-readout-not-truth` — Pillars §1.0 cross-tradition citation set
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §1.0 Pillars — ontology/epistemology/methodology
- **change:** Cite the cross-tradition convergence set (readout-not-truth, bounded knower, tracking truth, δ_R primitive) directly in FOUNDATION §1.0 alongside the base texts, as independently-arrived-at parallel formulations, not as external validation.
- **evidence:** kc-base-001, kc-base-005, kc-base-009, kc-base-027, kc-base-032, kc-ep-014, kc-ai-019, kc-islam-008
- **acceptance test:** FOUNDATION §1.0 diff adds citation lines for each evidence card id with no wording change to the base doctrine text.
- **risk:** Low — citation-only addition, no doctrinal change to the already-adopted base texts.

### `foundation.s5-scope-boundary-per-instance` — Non-clinical/non-medical/non-legal scope clause stays per-instance
- **kind / status:** foundation / proposed (human decision needed)
- **target:** FOUNDATION §5 Systematic disclaimer catalogue
- **change:** Do not standardize one reusable disclaimer text across all AI-runtime instances; require each instance to pair its disclaimer with an explicit context/jurisdiction check (time-criticality, deployment jurisdiction, legal-category availability).
- **evidence:** kc-ai-023, kc-he-016
- **acceptance test:** FOUNDATION §5 diff reviewed: every disclaimer entry carries a jurisdiction/time-criticality field, not just boilerplate text.
- **risk:** Medium — the evidence largely defeats a single standardized clause; risk is per-instance variation becoming unmanaged per-hub duplication.

### `kernel.unverified-verifiability-flag` — "Verifiable with no stated procedure" as a named narrow sub-case
- **kind / status:** kernel / proposed
- **target:** FOUNDATION §5 disclaimer catalogue / kernel rule 17
- **change:** Nest "claims verifiable/checkable with no stated procedure" under the existing vague-attribution disclaimer-catalogue entry as a named narrower sub-case; do not make it a purely mechanical/keyword-triggered check (intent-dependence defeats pure automation).
- **evidence:** kc-tourism-006
- **acceptance test:** finite_diagnostic sim: a hand-labeled set of 'verifiable'-claim sentences with/without a stated procedure — flag routes to human review, never auto-rejects.
- **risk:** Low-medium — well-supported as a narrow addition; main risk is over-automating detection given intent-dependence.

### `docs.blackbox-log-formalize-source` — Blackbox Log named-origin citation
- **kind / status:** docs / proposed
- **target:** FOUNDATION §2.3 Blackbox Note and R0/R1/R2 internal registers
- **change:** Cite "Blackbox Log: daily append-only verbatim voice record" directly as the named artifact §2.3 already formalizes, resolving the currently uncredited Blackbox Note appendix language.
- **evidence:** kc-ep-047, kc-ai-008
- **acceptance test:** §2.3 diff adds the named citation line; PUBLISH_GATE_v1 finding B-10 (Blackbox Log provenance disclosure) cross-referenced, not contradicted.
- **risk:** Low — citation-only; must stay consistent with the B-10 disclosed removal+restore correction entry already on record.

### `foundation.non-collapse-table-expand` — Non-Collapse Table Appendix A — cross-tradition rows
- **kind / status:** foundation / proposed
- **target:** FOUNDATION Appendix A Non-Collapse Table
- **change:** Add rows to Appendix A Family A (Truth/Warrant) and Family B (Access/Inference) citing the equal-number fallacy, same-shaped-formula-three-tiers, and θ(E) relational-invariance cards as parallel non-collapse cases outside the base corpus.
- **evidence:** kc-base-004, kc-base-021, kc-ep-021, kc-ep-023, kc-ep-024, kc-ep-026, kc-ep-027
- **acceptance test:** Appendix A table has ≥3 new rows, each with a card id + source DOI, no row lacking a locator (rule 17).
- **risk:** Low — additive table rows; requires foundation.pillars-readout-not-truth land first so terminology matches.

### `foundation.responsibility-arrow-mother-eq` — Mother-equation framing for the Data→Inference→Claim arrow
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §2.1b Responsibility per arrow
- **change:** Cite the "record is a translation, never the truth itself" mother-equation framing directly in §2.1b to strengthen the existing Data→Inference→Claim responsibility text.
- **evidence:** kc-base-014, kc-base-020
- **acceptance test:** §2.1b diff adds the mother-equation citation without altering the existing rule 15/16w wording.
- **risk:** Low — citation-only; requires foundation.pillars-readout-not-truth for shared vocabulary.

### `kernel.pcs-red-flag` — Premature Category Stabilization (PCS) as a scoped kernel red-flag
- **kind / status:** kernel / proposed (human decision needed)
- **target:** FOUNDATION §5/§6 disclaimer+genre-router; kernel contaminated-concept table (base-018)
- **change:** Add PCS to the contaminated-concept/red-flag table, but only when BOTH closure-timing AND absence-of-adaptation/contextual-fit hold jointly; explicitly not merged with the clinical term "premature closure."
- **evidence:** kc-ep-018, kc-ep-019, kc-ep-020, kc-islam-011, kc-tourism-002
- **acceptance test:** finite_diagnostic sim: run N synthetic claim cards with (a) timing-only closure, (b) timing+no-adaptation, (c) neither — kernel flags only class (b); precision on class (b) must be 100% on the synthetic set before this ships.
- **risk:** Medium — real cross-domain support, but two independent counter-cases (decoupled closure, successful non-premature adoption) risk over-generalization if scoping is dropped.

### `schema.verdict-class-vocabulary` — Verdict-class vocabulary field (DERIVED/FORCED/DEFINITIONAL-RELABEL/POSITED/BORROWED-SCALE/OPEN)
- **kind / status:** schema / proposed
- **target:** FOUNDATION field base_relation (holds|refined_by_later_work|superseded|outdated|open)
- **change:** Add the six-value verdict-class vocabulary as an enum on the `base_relation` field (currently holds/refined_by_later_work/superseded/outdated/open) so a claim card can state which verdict class a derivation belongs to, not only its relation to a base text.
- **evidence:** kc-base-038
- **acceptance test:** JSON schema validates a claim card with verdict_class=FORCED and rejects an unlisted seventh value.
- **risk:** Low-medium — additive enum field; requires foundation.non-collapse-table-expand to land first so Appendix A rows can reference the new field consistently.

### `schema.prereg-gate-fields` — Frozen-preregistration gate as checkable fields, not a hard block
- **kind / status:** schema / proposed (human decision needed)
- **target:** FOUNDATION §2.1a Problem before observation / §7.3 Bounded-Judge Law
- **change:** Add protocol_frozen_at, ethics_approved_at (nullable/NOT_APPLICABLE for non-human-subjects work), and a separate registry-administrative-approval timestamp; violations are flagged, not blocked; a passed sequencing check is never read as ethics-substance verification.
- **evidence:** kc-he-002, kc-he-004, kc-he-005, kc-he-006, kc-he-007
- **acceptance test:** Schema validator accepts a card with ethics_approved_at=NOT_APPLICABLE for a non-human-subjects claim and flags (not rejects) an out-of-sequence pair.
- **risk:** High if implemented as a hard universal block — real registries do not hard-block this way; a naive implementation would misdescribe practice and could block legitimate research.

### `kernel.gate-rules-taxonomy-i-z` — I1–I4/Z1–Z4 injected-infinity/zero taxonomy in kernel gate rules
- **kind / status:** kernel / proposed
- **target:** FOUNDATION §3.3 Kernel gate rules (specified, Dr, untested)
- **change:** Encode the injected-infinity/zero taxonomy (I1–I4 infinity types, Z1–Z4 zero types) and the Fail-Able Gate Law (Type-P vs Type-U) as named kernel gate-rule categories, alongside the existing contaminated-concept table.
- **evidence:** kc-base-006, kc-base-008, kc-base-016, kc-base-018, kc-base-034
- **acceptance test:** Unit tests: 8 synthetic claim cards (one per I/Z type) each raise the correctly-named gate error, not a generic rejection.
- **risk:** Medium — currently Dr/untested per FOUNDATION §3.3 itself; shipping without S4 simulation coverage would violate the roadmap's own no-ship-without-measured-effect rule.

### `foundation.ead-crosswalk` — Existence-Attribution-Disclosure (E-A-D) norm as the named source of §3.1 crosswalk
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §3.1 Five Questions ⇄ E-A-D ⇄ field crosswalk
- **change:** Cite The Readout Condition papers directly as the named source of the existing Five-Questions ⇄ E-A-D ⇄ field crosswalk in §3.1, rather than leaving the crosswalk uncredited.
- **evidence:** kc-ep-042, kc-aihp-011, kc-ai-001
- **acceptance test:** §3.1 diff adds a citation line naming the E-A-D source papers directly above the crosswalk table.
- **risk:** Low — citation-only; requires schema.verdict-class-vocabulary land first for consistent field naming.

### `schema.claim-card-comparison-evidence-field` — Comparison/evidence-strength field — descriptive-only, no outperformance claim
- **kind / status:** schema / proposed
- **target:** FOUNDATION §3.2 Field list (claim card schema)
- **change:** Add a comparison field to the claim-card schema restricted to same/different/cited values (never novel/first/best), and an evidence-strength field distinguishing adjacent/ precedent evidence from direct validation of the intervention itself.
- **evidence:** kc-se-001, kc-se-002, kc-se-007, kc-se-009
- **acceptance test:** JSON schema rejects a claim card whose comparison field contains 'novel'/'first'/'best'/'outperforms'; accepts same/different/cited.
- **risk:** Low — directly enforces this repo's own no-novelty-words rule at the schema layer instead of only as prose guidance.

### `foundation.possession-constitution-collapse` — Possession-Constitution Collapse / knower-fetishism as the named AI-authorship rule source
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §3.2b / §7 Gates & review (AI-authorship rules)
- **change:** Cite "Possession-Constitution Collapse" and "knower fetishism" directly as the named source for why an AI-drafted claim card is not disqualified by authorship alone, and for the "channel over face" / provenance-only-metadata rule already implicit in rule 17.
- **evidence:** kc-ep-043, kc-ai-003, kc-ai-004, kc-aihp-013, kc-aihp-014
- **acceptance test:** §3.2b/§7 diff cites the named source papers alongside the existing rule-17 provenance-only-channel text.
- **risk:** Low-medium — citation-only, but touches AI-authorship rules directly tied to CHANGELOG 0.2.0 gate rule 9 (no AI attribution without permission); requires foundation.ead-crosswalk land first.

### `foundation.independence-ladder-i0-i5-source` — I0–I5 Independence Ladder named source citation
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §4.2 Independence Ladder I0–I5
- **change:** Cite "Rigour Without Infrastructure" directly as the named source of the I0–I5 Independence Ladder and the falsifiable-propositions framing already used in §4.2.
- **evidence:** kc-ep-052, kc-ai-002
- **acceptance test:** §4.2 diff adds the named citation without renumbering or redefining the existing I0–I5 classes.
- **risk:** Low — citation-only; requires foundation.ead-crosswalk land first for a consistent citation block.

### `cli.genre-router-layer-confusion-check` — Genre-router layer-confusion diagnostic
- **kind / status:** cli / proposed
- **target:** FOUNDATION §6 Genre router
- **change:** Add a CLI check that flags when a claim card's genre/register (e.g. jurisprudential) does not match the tool/authority being invoked on it (e.g. astronomical), using the three-layer split (astronomical/jurisprudential/institutional) as the template.
- **evidence:** kc-islam-009
- **acceptance test:** CLI run against a synthetic mismatched-layer card set (N=10) flags all mismatches with zero false positives on a matched-layer control set.
- **risk:** Low-medium — diagnostic-only (no auto-correction), consistent with the diagnostic-not-optimizing pattern already adopted elsewhere in this DAG.

### `rule17.claim-card-certification-open` — Claim card replaces institutional certification: kept [Open]
- **kind / status:** kernel / deferred
- **target:** kernel rule 17 / FOUNDATION §4.2 Independence Ladder I0–I5
- **change:** Do NOT formalize "claim card substitutes for institutional certification" into kernel rule 17 or the I0–I5 ladder this pass; keep it logged [Open] pending a falsifier that tests claim cards directly (not badges/Registered Reports by analogy).
- **evidence:** kc-ai-006, kc-aihp-002, kc-aihp-003
- **acceptance test:** design/TODO_v0.3.md carries an explicit [Open] line with the falsifier condition; no kernel diff lands for this claim in v0.3.
- **risk:** Low (no change made) — flagged risk is silent drift if this stays unaddressed across future minor versions without a scoped falsifier ever getting written.

### `foundation.k-state-standalone-scholar-cite` — K-state (Standalone Scholar) named-origin citation
- **kind / status:** foundation / proposed
- **target:** FOUNDATION §4.4 K-state (Standalone Scholar, PRESERVE_EXACT)
- **change:** Cite "The Standalone Scholar" directly as the named origin of the K-state concept and PRESERVE_EXACT dual-track architecture already used in §4.4.
- **evidence:** kc-ep-041, kc-aihp-017, kc-ai-011
- **acceptance test:** §4.4 diff adds the named citation without altering the existing K-state/PRESERVE_EXACT definitions.
- **risk:** Low — citation-only; requires foundation.independence-ladder-i0-i5-source for a consistent citation block ordering.

### `foundation.lrs-discovery-loop-extension` — Discovery-loop extension (candidate-set formation precedes evidential adjudication)
- **kind / status:** foundation / proposed (human decision needed)
- **target:** FOUNDATION §7.9 Literature Review System (LRS) / §6 discovery extension
- **change:** Extend §7.9 LRS with a discovery-routing stage (human retains the question, AI recursively decomposes and gates candidates; k_epi as the epistemic-multiplication construct) — gated as an extension, not a replacement of the existing LRS pipeline.
- **evidence:** kc-ep-045, kc-ep-046, kc-ep-048, kc-ep-049, kc-aihp-005, kc-aihp-006, kc-aihp-010, kc-aihp-020
- **acceptance test:** S4 finite_diagnostic sim compares LRS precision/recall on the same question set with and without the discovery-routing stage; ship only if recall improves without a precision drop.
- **risk:** Medium — DIGEST logs the underlying agenda-paper claim as still open (kc-aihp-008/009 not adopted here); this node only operationalizes the already-'holds'/'adapt' cards, not the open agenda claim.

### `foundation.s7.9-intake-tier-flag` — Claim-tier intake flag — thin addition, not a new mechanism
- **kind / status:** foundation / proposed (human decision needed)
- **target:** FOUNDATION §7.9 Literature Review System (LRS)
- **change:** Add a flag-and-request-tier step only as a thin layer on the existing AACODS-style checklist (trace-to-original + appraise); explicitly exempt Global South anecdotal/expert/local-knowledge evidence genres from being treated as automatically suspect.
- **evidence:** kc-ai-024, kc-he-018
- **acceptance test:** LRS run on a policy-brief-only source set produces a flagged-not-blocked intake row, distinct from a rejected row.
- **risk:** Medium — real gap exists, but the mechanism as posed risks duplicating existing checklist machinery or over-policing legitimate non-graded evidence.

## Topological order (build/decision sequence)

Computed from `requires`/`informs` edges (Kahn's algorithm; `conflicts` edges do not constrain order — they mark a tension to resolve, not a dependency).

1. `eng.registry-check-ci-safe` (done)
2. `eng.lit-manifest-fail-closed` (done)
3. `foundation.s1.0-infinity-tension-flag` (deferred)
4. `foundation.s1.0-ashari-ontology-analogue` (proposed)
5. `foundation.honest-edges-agrippa` (proposed)
6. `foundation.disclaimer-catalogue-expand` (proposed)
7. `kernel.rule17-source-first` (done)
8. `foundation.pillars-readout-not-truth` (proposed)
9. `foundation.s5-scope-boundary-per-instance` (proposed)
10. `kernel.unverified-verifiability-flag` (proposed)
11. `docs.blackbox-log-formalize-source` (proposed)
12. `foundation.non-collapse-table-expand` (proposed)
13. `foundation.responsibility-arrow-mother-eq` (proposed)
14. `kernel.pcs-red-flag` (proposed)
15. `schema.verdict-class-vocabulary` (proposed)
16. `schema.prereg-gate-fields` (proposed)
17. `kernel.gate-rules-taxonomy-i-z` (proposed)
18. `foundation.ead-crosswalk` (proposed)
19. `schema.claim-card-comparison-evidence-field` (proposed)
20. `foundation.possession-constitution-collapse` (proposed)
21. `foundation.independence-ladder-i0-i5-source` (proposed)
22. `cli.genre-router-layer-confusion-check` (proposed)
23. `rule17.claim-card-certification-open` (deferred)
24. `foundation.k-state-standalone-scholar-cite` (proposed)
25. `foundation.lrs-discovery-loop-extension` (proposed)
26. `foundation.s7.9-intake-tier-flag` (proposed)

## Edges

| from | to | kind |
|---|---|---|
| `eng.lit-manifest-fail-closed` | `kernel.rule17-source-first` | requires |
| `kernel.rule17-source-first` | `kernel.gate-rules-taxonomy-i-z` | informs |
| `kernel.rule17-source-first` | `docs.blackbox-log-formalize-source` | informs |
| `eng.registry-check-ci-safe` | `schema.prereg-gate-fields` | informs |
| `foundation.pillars-readout-not-truth` | `foundation.non-collapse-table-expand` | requires |
| `foundation.pillars-readout-not-truth` | `foundation.responsibility-arrow-mother-eq` | requires |
| `foundation.honest-edges-agrippa` | `foundation.pillars-readout-not-truth` | informs |
| `foundation.s1.0-infinity-tension-flag` | `foundation.pillars-readout-not-truth` | conflicts |
| `foundation.s1.0-ashari-ontology-analogue` | `foundation.pillars-readout-not-truth` | informs |
| `foundation.non-collapse-table-expand` | `schema.verdict-class-vocabulary` | requires |
| `schema.verdict-class-vocabulary` | `foundation.ead-crosswalk` | requires |
| `schema.verdict-class-vocabulary` | `schema.claim-card-comparison-evidence-field` | informs |
| `foundation.ead-crosswalk` | `foundation.possession-constitution-collapse` | requires |
| `foundation.ead-crosswalk` | `foundation.independence-ladder-i0-i5-source` | requires |
| `foundation.ead-crosswalk` | `cli.genre-router-layer-confusion-check` | informs |
| `foundation.independence-ladder-i0-i5-source` | `foundation.k-state-standalone-scholar-cite` | requires |
| `foundation.independence-ladder-i0-i5-source` | `rule17.claim-card-certification-open` | informs |
| `foundation.independence-ladder-i0-i5-source` | `foundation.lrs-discovery-loop-extension` | requires |
| `foundation.non-collapse-table-expand` | `kernel.pcs-red-flag` | informs |
| `kernel.pcs-red-flag` | `kernel.gate-rules-taxonomy-i-z` | informs |
| `foundation.disclaimer-catalogue-expand` | `foundation.s5-scope-boundary-per-instance` | requires |
| `foundation.disclaimer-catalogue-expand` | `kernel.unverified-verifiability-flag` | informs |
| `foundation.disclaimer-catalogue-expand` | `foundation.s7.9-intake-tier-flag` | informs |
| `foundation.lrs-discovery-loop-extension` | `foundation.s7.9-intake-tier-flag` | informs |
| `foundation.responsibility-arrow-mother-eq` | `schema.prereg-gate-fields` | informs |

## Founder decisions required before S6 build

Every node below is `proposed` (or `deferred` pending its own falsifier) and is flagged `human_decision_needed: true` — none may be committed to `DECISIONS.yaml` or built without an explicit founder ruling, per `EPIS-KNOWLEDGE-VALIDATION` (no external validation lever; the founder is the internal decision owner named in `design/ROADMAP_v0.3.md`).

- `kernel.pcs-red-flag` — Premature Category Stabilization (PCS) as a scoped kernel red-flag (risk: Medium — real cross-domain support, but two independent counter-cases (decoupled closure, successful non-premature adoption) risk over-generalization if scoping is dropped.)
- `foundation.s5-scope-boundary-per-instance` — Non-clinical/non-medical/non-legal scope clause stays per-instance (risk: Medium — the evidence largely defeats a single standardized clause; risk is per-instance variation becoming unmanaged per-hub duplication.)
- `foundation.s7.9-intake-tier-flag` — Claim-tier intake flag — thin addition, not a new mechanism (risk: Medium — real gap exists, but the mechanism as posed risks duplicating existing checklist machinery or over-policing legitimate non-graded evidence.)
- `schema.prereg-gate-fields` — Frozen-preregistration gate as checkable fields, not a hard block (risk: High if implemented as a hard universal block — real registries do not hard-block this way; a naive implementation would misdescribe practice and could block legitimate research.)
- `foundation.s1.0-ashari-ontology-analogue` — Partial theology-neutral ontology analogue (2 of 3 constructs) (risk: Medium — partial adoption is defensible from the evidence but risks looking arbitrary without the full reasoning carried into the commit message.)
- `foundation.lrs-discovery-loop-extension` — Discovery-loop extension (candidate-set formation precedes evidential adjudication) (risk: Medium — DIGEST logs the underlying agenda-paper claim as still open (kc-aihp-008/009 not adopted here); this node only operationalizes the already-'holds'/'adapt' cards, not the open agenda claim.)

## Deferred nodes (kept `[Open]` per DIGEST, not built this pass)

- `rule17.claim-card-certification-open` — Claim card replaces institutional certification: kept [Open]: Do NOT formalize "claim card substitutes for institutional certification" into kernel rule 17 or the I0–I5 ladder this pass; keep it logged [Open] pending a falsifier that tests claim cards directly (not badges/Registered Reports by analogy).
- `foundation.s1.0-infinity-tension-flag` — Infinity-as-transcendental-ground stays a flagged [Open] tension: Keep infinity-as-transcendental-ground logged as an explicitly flagged [Open] tension in FOUNDATION §1.0 rather than building a formal reconciliation section this pass; the flag must note the stance's historical load-bearing role and cross-cultural diffusion.
