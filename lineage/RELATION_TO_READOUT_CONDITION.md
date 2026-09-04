tier: Dr (specified; independently unreviewed)

# Relation to The Readout Condition

> Readout, not truth. Source read for this file: `sources/READOUT_CONDITION_2026-08.txt` (the
> `.txt` extraction of `The_Readout_Condition_Full_Paper_Elevated.pdf`), core sections only — the
> formal appendix and bibliography were **not** read, by this design round's own admission
> (`design/FOUNDATION_v0.3.md` §12, "Honest edges"). Everything below is glosa's own operational
> reading of the paper's principles, not a restatement of proofs; where a mapping is
> presence-checkable only, this file says so (chair ruling D2, `FOUNDATION_v0.3.md` §3.1). As of
> this session (2026-09-04) the paper is not yet on Zenodo — cited here by title and the local
> extraction date only, no DOI available yet.

## 1. E-A-D → glosa fields

The Readout Condition is `E ∧ A ∧ D` (Principles 7–9 of the source paper). glosa's Five Questions
(`FOUNDATION_v0.3.md` §1.1, §3.1) are named, in the founder's own words, as **a claim-grain
instantiation** of this norm — not an extension or re-proof of it.

| Paper principle | Paper statement (plain) | glosa field(s) | Mechanically checkable? |
|---|---|---|---|
| **Principle 7 — E (provenance existence)** | For every load-bearing claim distinction, some provenance path exists, or the claim is marked provenance-indeterminate. | `five_questions.seen` (Q1) — `record_ref, as_of, retrievable_original, access_model, citation_refs` | Presence + shape only |
| **Principle 8 — A (provenance attribution)** | If a claim credits distinction *d* to source *S*, *S* must pass the licensing test for *d* (fiber discrimination / pointwise neighbourhood exclusion / access admissibility, depending on the case). | `five_questions.separates` (Q2) — `value_z0, licensing_test.{regime,result,notes}, zero_vs_bottom` | **Presence-checkable only, not correctness-checkable** (chair ruling D2) — the kernel can confirm the field is filled and `zero_vs_bottom` holds a valid enum value; it cannot confirm the licensing test's *result* is correct. |
| **Principle 9 — D (provenance disclosure)** | Every non-source node on an essential dependency path must remain declared or recoverable; omitting one while representing the claim as source-generated is a silent lift. | `five_questions.ai_filled` (Q3, the six-way AI-audit split) + `silent_lift_check` | **Presence-checkable only** (chair ruling D2) for `ai_filled`; `silent_lift_check` is the one *mechanized cross-check* the kernel actually runs — it compares `represented_dependency_set` against `actual_dependency_set` computed from `provenance_dag`, never a re-do of the epistemic work by hand. Non-empty `flags` is a **hard failure** (`FOUNDATION_v0.3.md` §3.3 kernel rule 7), not a disclaimer. |

**The condition is conjunctive, not additive.** A card that answers Q1/Q2/Q4 honestly but
misattributes Q3 — crediting the source with a distinction AI actually supplied — fails the
Readout Condition even though every field "looks filled." `silent_lift_check` exists exactly to
catch this case (`FOUNDATION_v0.3.md` §3.1).

## 2. Typed augmentation → `five_questions.assumed[]`

The paper's Definitions 4–5 name specific augmentation types (an inferential commitment — model,
prior, theory, bridge principle, calibration assumption, changing what can be inferred without
adding new access; a decision-policy augmentation — a loss function, threshold, or institutional
rule mapping an epistemic state to an action). glosa's `five_questions.assumed[].type` enum
(`access_augmentation | contrast_relevance_operation | inferential_commitment |
decision_policy_augmentation`) is glosa's own operational typing of "the weakest augmentation
layer for each dependency," independently named — not the paper's own formal vocabulary copied
verbatim, in the same spirit as `grr-epistemic-foundation`'s pattern-not-strings reuse
(`FOUNDATION_v0.3.md` §1.2). Each entry also carries `identification_level: "A0".."Am" |
unidentified` and `contaminated_concept_hit`.

## 3. Identification ladder → `identification_ladder`

The paper locates each claim's assumption-dependence on an ordered/nested sequence of
augmentation-layer sets, `A0 ⊆ A1 ⊆ ... ⊆ Am`, and asks: at which layer does the distinction first
become identified? glosa's `identification_ladder` field group
(`{layers: [{id, adds}], per_rival: [{rival, first_identification_level}]}`, `FOUNDATION_v0.3.md`
§3.2) is glosa's direct operationalization of this — one ladder per claim, one entry per rival
explanation, each naming the weakest layer at which that rival is ruled out. **Not attempted:**
the paper's own honest caveat that real scientific assumptions are often only partially ordered,
not a clean nested ladder (source, §"identification ladder requires an explicit ordering...
assumptions may be partially ordered rather than..."), is inherited as-is — glosa's schema forces
a ladder shape and does not attempt to solve the partial-order case.

## 4. Silent lift → `silent_lift_check`

Paper Definition 7: let λ(d) be the actual essential dependency set of distinction *d* and λ̂(d)
the dependency set represented to oneself or others. A silent lift occurs when an essential node
is omitted, or a source is credited with *d* despite failing its licensing condition. glosa's
`silent_lift_check: { represented_dependency_set, actual_dependency_set, flags, status: not_run |
run }` is a direct field-level mirror of this definition — `represented_dependency_set` ≈ λ̂(d),
`actual_dependency_set` ≈ λ(d), `flags` fires on any symmetric-difference finding. Per kernel rule
11 (`FOUNDATION_v0.3.md` §3.3), `status: not_run` is treated as ⊥ (unknown), never as
"checked, nothing found" — a card sitting at `not_run` is honestly incomplete, not honestly
clean, mirroring the paper's own `0 ≠ ⊥` discipline (also present directly in
`five_questions.separates.zero_vs_bottom`).

## 5. Defeater routing → `provenance_dag.defeater_log` + `defeater_route`

Paper Proposition 3: for a distinction *d* with currently-adequate licensing paths Π(d), a
node-specific defeater Δv leaves surviving paths Π_Δv(d) = {p ∈ Π(d) : v ∉ V(p)}; *d* loses all
provenance support iff Δv targets an essential node (one on every path). glosa's
`provenance_dag: { nodes, edges, essential_dependency_set (computed by validator, never
hand-typed), defeater_log: [{node, date, outcome}], status }` and the kernel function
`defeater_route` (`FOUNDATION_v0.3.md` §9) are the direct operational mirror: `defeater_route`'s
job is exactly Proposition 3's path-deletion computation over glosa's own DAG shape. **Not
attempted:** the paper's Corollary 1 (misrouted defeat under silent lift, i.e. what happens when
the represented and actual essential sets differ and a defeater lands in the gap) is not itself
re-derived as a separate glosa mechanism — it falls out for free once `silent_lift_check` and
`defeater_route` are both run, but glosa does not name or test this composed case on its own.

## 6. AI audit (six-way split) → `five_questions.ai_filled`

The paper's Principle 9 (D, disclosure) is applied by glosa specifically to AI contribution via a
six-field split, none of which may be silently omitted (every field states "none identified" or
is filled): `current_evidence, retrieved_tool_evidence, retained_record_route,
model_calibration_assumption, prompt_system_constraint, decision_policy`. This full six-field
shape applies only to `shape: full` cards; a `shape: stub` card collapses this to
`{used: bool, note: string}` (`FOUNDATION_v0.3.md` §3.2a) — a deliberately lower-cost, still-honest
shape for K0 frontline use.

## 7. The paper's three practical questions → glosa fields and kernel functions

The paper's own closing simplification (§11, "Its three practical questions remain simple"):

1. **What does the attributed source distinguish?**
2. **Which distinction does the claim add?**
3. **Which provenance path makes that addition licit?**

glosa's mapping:

| Practical question | glosa field(s) | Kernel function |
|---|---|---|
| 1. What does the source distinguish? | `five_questions.seen` + `five_questions.separates.licensing_test` | `validate_claim_card` (presence/shape) |
| 2. Which distinction does the claim add? | `five_questions.assumed[]` + `five_questions.ai_filled` + `identification_ladder` | `silent_lift_check` (computed cross-check) |
| 3. Which provenance path makes the addition licit? | `five_questions.tested.evidence_relations` + `independent_check` + `provenance_dag.essential_dependency_set` | `defeater_route`, `gate_release` |

This crosswalk is the same one `FOUNDATION_v0.3.md` §3.1 draws for the founder's own five Thai
questions (เราเห็นอะไรจริง / ข้อมูลแยกอะไรได้ / AI เติมอะไร / สมมติอะไรไว้ /
เจอหลักฐาน/คำคัดค้านอิสระหรือยัง) — the founder's five questions and the paper's three practical
questions are two independently-phrased entries into the same E-A-D norm, both resolved into the
same claim-card field groups rather than kept as two separate, competing question sets.

## 8. What glosa does NOT attempt

- glosa does not extend, re-derive, or re-prove any of the paper's formal propositions (1–9) or
  its iterated-readout-chain results (§6 of the source). It operationalizes the principles into a
  schema and a set of presence/shape checks — nothing in glosa's kernel is a proof of anything in
  the paper.
- glosa does not read or rely on the paper's formal appendix or bibliography — not read by this
  design round (`FOUNDATION_v0.3.md` §12).
- glosa's kernel cannot verify the *correctness* of a licensing test, an assumption list's
  *completeness*, or an AI-fill disclosure's *honesty* — only their *presence and shape*
  (chair ruling D2, §1 table above). The one exception is `silent_lift_check`, which is a real
  computed cross-check, not merely a presence check — but even it compares two *declared* sets
  against each other, not against ground truth.
- glosa does not attempt the partial-order generalization of the identification ladder that the
  paper itself flags as an open modeling question for complex scientific practice.
- glosa never treats an external human's involvement in this note-writing exercise as itself
  satisfying I5/K2 — this file is `Dr`-tier, unreviewed, written by the same session that also
  authored the schema it describes (I0, at best I1 once re-read fresh).
