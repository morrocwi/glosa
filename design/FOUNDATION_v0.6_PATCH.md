# FOUNDATION v0.6 patch note — S3 DAG closure + K4 still-missed defect classes

> **Tier: Dr, specified not applied.** This file states the exact text/field/rule diffs to apply
> to `FOUNDATION_v0.5.md` to produce v0.6. It does not itself edit `FOUNDATION_v0.5.md` — per this
> task's scope (`design/` only). Readout, not truth; no novel/first/prior-art language; comparisons
> stay same/different/cited; no vendor name is credited anywhere in this file. K-state is
> unchanged at this pass: **K0** (no independent check has run on this patch itself, `NC-34`).
> Inputs read for this patch: `design/ROADMAP_v0.3.md`, `design/DAG_v0.3.yaml` +
> `design/DAG_v0.3.md` (26 nodes), `sim/v0.3/report.md` (finite_diagnostic, one fixed 180-card
> corpus, this run only), `knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md`,
> `records/lit/glosa-v0-3/DIGEST.md`, `design/FOUNDATION_v0.5.md` §1, §2, §3.3, §5, §7, §7.8, §7.9,
> `design/FOUNDATION_v0.5_PATCH.md` (format precedent), `schema/README.md`, `kernel/glosa_kernel.py`.
> Format follows `FOUNDATION_v0.5_PATCH.md`'s precedent: one section per node, target section ·
> exact text · schema fields · kernel rule (with error/warning strings) · acceptance test ·
> evidence ids · status.

---

## 0. What this patch covers, and what it does not

- **17 DAG nodes at `status: proposed` (ship or revise per §S4/sim, or citation-only with no
  sim dependency) get a section below**, each ending `ready` or `pending-founder: <decision
  name>`.
- **3 new nodes** close the three defect classes `sim/v0.3/report.md` §4/§6 names as still missed
  after combining the two `ship`-recommended S4 prototypes (`composite_quote`, `hidden_ai_fill`)
  plus one class this patch adds proactively from the same report's channel/bearing discussion
  (`inflated_bearing`, already partly addressed by the shipped `schema.claim-card-comparison-
  evidence-field` node but not closed at the kernel-rule level) — `K-C1`, `K-C2`, `K-C3`.
- **6 nodes are founder-decision nodes** (`human_decision_needed: true` in the DAG) — text below is
  the text for the DAG's own stated `risk`-minimizing / evidence-majority option (never a
  unilateral AI decision), each marked `pending-founder`.
- **3 nodes ship without qualification** (`eng.registry-check-ci-safe`, `eng.lit-manifest-fail-
  closed`, `kernel.rule17-source-first` — already `done`, listed once for DAG lineage, no new text).
- **2 nodes are dropped this pass** (`kernel.unverified-verifiability-flag`,
  `schema.prereg-gate-fields`) — one line each, sim reason only, no patch text.
- **1 node is deferred, kept `[Open]`** already in FOUNDATION (`foundation.s1.0-infinity-tension-
  flag`) plus 1 more (`rule17.claim-card-certification-open`) — one line each, no patch text.
- Everything else (`foundation.*` citation-only nodes with `human_decision_needed: false`) gets a
  full section: these are the low-risk, additive citation lines the DAG's own risk column already
  calls Low.

Rule numbering in this patch continues from the kernel's shipped ceiling. FOUNDATION §3.3 text
currently states rules 1–14 in prose; `kernel/glosa_kernel.py` additionally implements rules
15–17 (responsibility arrow, empirical-extension warning, source-first citation) that were shipped
after v0.5's prose was written and are not yet folded into §3.3's numbered list. This patch's new
rules start at **18**. See the Rule numbering table (§ near the end).

---

## 1. `kernel.gate-rules-taxonomy-i-z` — I1–I4/Z1–Z4 injected-infinity/zero taxonomy

- **status:** ready (sim: **ship** — its own 9-card slice moved 0/9 → 9/9, delta_recall +1.0 on
  `injected_infinity`, delta_false_alarm 0, `sim/v0.3/report.md` §3/§4)
- **FOUNDATION target:** §3.3 Kernel gate rules — new numbered rules 18–19 (the taxonomy itself is
  a *classification*, not a single boolean rule; two rules make the classification checkable:
  one that requires a named I/Z-type tag whenever a hard-fail on injected infinity/zero fires, one
  that keeps the Fail-Able Gate Law's Type-P/Type-U split from collapsing into a single verdict).

**Exact text to insert into §3.3, after existing rule 17 (kernel-only, not yet in FOUNDATION prose
— see the numbering table), as new rules 18–19:**

> 18. A hard-fail raised for injected infinity/zero (§3.3 rule 8's `EXTERNAL_VALIDATION_PROPOSED`
>     scan and any future kernel scan of the same family) must carry a named type from the
>     taxonomy below — `injected_infinity_type: I1 | I2 | I3 | I4` or `injected_zero_type: Z1 |
>     Z2 | Z3 | Z4` — never a generic, untyped rejection. I1 = infinity asserted as a completed
>     totality with no construction shown; I2 = infinity used as a limiting idealization without
>     a stated convergence witness; I3 = infinity smuggled in as a rhetorical "always/never"
>     universal quantifier over an unbounded, unexamined domain; I4 = infinity used as a
>     transcendental ground for a normative claim (cross-referenced to the still-`[Open]`
>     `foundation.s1.0-infinity-tension-flag` — this rule classifies the *pattern*, it does not
>     resolve that flagged tension). Z1 = zero asserted as "nothing to report" where the correct
>     state is `⊥`/unknown (`NC-25`, `NC-26`); Z2 = a null result read as a universal negative
>     (`NC-27`); Z3 = a zero-count used to claim completeness of a search or check that was never
>     run to completion; Z4 = a vacuous-truth zero (an empty-domain universal) presented as
>     positive evidence.
> 19. **Fail-Able Gate Law:** a gate fires as **Type-P** (a positive, checkable pattern was
>     matched — cite the exact pattern) or **Type-U** (the gate could not determine a pattern and
>     is refusing on absence-of-evidence grounds) — the two are never merged into one undifferentiated
>     "gate failed" verdict. `disclaimers_emitted`/`review_report` must state which type fired.

**Schema fields (`claim_card.schema.json`, additive):**
```json
{
  "gate_fail_taxonomy": {
    "type": "object",
    "properties": {
      "injected_infinity_type": {"enum": ["I1", "I2", "I3", "I4", null]},
      "injected_zero_type": {"enum": ["Z1", "Z2", "Z3", "Z4", null]},
      "gate_type": {"enum": ["Type-P", "Type-U"]}
    },
    "required": ["gate_type"]
  }
}
```

**Kernel rule numbers / strings:**
- `rule18(TAXONOMY-UNTYPED)`: `"rule18: injected-infinity/zero hard-fail requires a named I1-I4/Z1-Z4 type, not a generic rejection"` (error).
- `rule19(GATE-TYPE-UNSTATED)`: `"rule19: gate verdict must state Type-P (pattern matched, named) or Type-U (absence-of-evidence refusal), never merged"` (error).

**Acceptance test (from the DAG, refined by sim):** the DAG's own test (8 synthetic cards, one per
I/Z type, each raises the correctly-named error) plus the sim-refined addition: run against the
existing `sim/v0.3/corpus/` `injected_infinity` fixture set (9 cards) — must reach 9/9 caught
*with* a named type on every hit, not merely 9/9 caught untyped (the prototype script currently
achieves the latter; this patch's rules 18/19 require the former as the acceptance bar going
forward).

**Evidence ids:** kc-base-006, kc-base-008, kc-base-016, kc-base-018, kc-base-034.

---

## 2. `schema.claim-card-comparison-evidence-field` — comparison/evidence-strength field

- **status:** ready (sim: **ship** — targeted `inflated_bearing` only, +0.25 delta_recall on the
  4-defect/36-card set it reports against, delta_false_alarm 0, `sim/v0.3/report.md` §3)
- **FOUNDATION target:** §3.2 Field list (claim card schema)

**Exact text to insert into §3.2's field list, immediately after the existing `tested` block:**

> **`comparison`** (new field, schema_version bump — additive): `{ target: string | null,
> relation: same | different | cited | not_compared, basis: string }`. `relation` is a closed
> enum; the words "novel", "first", "best", and "outperforms" (and their Thai equivalents) are
> **schema-rejected** as `relation` or `basis` values (gate rule 6 enforced at the schema layer, not
> only as prose guidance). `not_compared` is legal and is the correct default when no comparison
> was attempted — it is never inferred from an empty field, an empty field is itself a validation
> error once `comparison` is present at all (no silent "not compared" via omission).
>
> **`evidence_strength`** (new field, additive): `{ class: direct_validation |
> adjacent_precedent, notes: string }`. `direct_validation` = the evidence bears on the
> intervention/claim itself; `adjacent_precedent` = the evidence bears on a related but distinct
> prior case and is being read across by analogy — this class may never be silently promoted to
> `direct_validation` in prose that cites it (`NC-72` Constraint≠evidence-for-us, applied here to
> evidence class rather than only to `bearing: CHALLENGES`).

**Schema fields:**
```json
{
  "comparison": {
    "type": "object",
    "properties": {
      "target": {"type": ["string", "null"]},
      "relation": {"enum": ["same", "different", "cited", "not_compared"]},
      "basis": {"type": "string", "not": {"pattern": "(?i)\\b(novel|first|best|outperform)\\w*\\b"}}
    },
    "required": ["relation", "basis"]
  },
  "evidence_strength": {
    "type": "object",
    "properties": {
      "class": {"enum": ["direct_validation", "adjacent_precedent"]},
      "notes": {"type": "string"}
    },
    "required": ["class"]
  }
}
```

**Kernel rule:**
- `rule20(NOVELTY-WORD-REJECTED)`: `"rule20: comparison.basis contains a novelty/priority word ('novel'/'first'/'best'/'outperform') — gate rule 6 forbids this at the schema layer"` (error).

**Acceptance test (DAG's own, unchanged — already schema-checkable):** "JSON schema rejects a claim
card whose comparison field contains 'novel'/'first'/'best'/'outperforms'; accepts same/different/
cited." Refined by sim: additionally re-run the 9-card `inflated_bearing` fixture slice and confirm
9/9 caught via `evidence_strength.class` misclassification detection, matching the S4 prototype's
measured +0.25 delta on the 36-card 4-defect subset.

**Evidence ids:** kc-se-001, kc-se-002, kc-se-007, kc-se-009.

---

## 3. `cli.genre-router-layer-confusion-check` — genre-router layer-confusion diagnostic

- **status:** pending-founder: promote-from-revise-to-ship-gate — sim recommends **revise**, not
  ship, because its four layer-checks are keyword/phrase matches tuned to one corpus's own
  generator vocabulary (`sim/v0.3/report.md` §3, first bullet) and it substitutes the 180-card
  corpus for its own named N=10 acceptance fixture rather than running that literal fixture. The
  **recommended option** below is: land the mechanism as a diagnostic-only CLI check (matches the
  DAG's own low-risk framing — "diagnostic-only, no auto-correction") but gate its promotion out of
  `revise` on a held-out, differently-worded fixture batch per §6 of the sim report, not on this
  corpus alone.
- **FOUNDATION target:** §6 Genre router

**Exact text to insert into §6, after §6.3b (genre routing procedure):**

> **6.3c Layer-confusion diagnostic.** A claim card's genre/register (e.g. jurisprudential) can be
> checked against the tool/authority actually invoked on it (e.g. astronomical) using the existing
> three-layer split (astronomical / jurisprudential / institutional, §6.1) as the template. This is
> a **diagnostic, not a corrective**: it flags a mismatch for human review and never auto-reroutes
> a card's genre. **Honest limit (carried forward from the S4 sim, not silently dropped):** the
> shipped detector is a keyword/marker match calibrated against one synthetic corpus's generator
> vocabulary; it is expected to under-generalize to differently-worded real cards until a held-out
> fixture batch (§ sim report §6 follow-up) confirms otherwise. Tier of any "N flagged, zero false
> positives" claim about this check: `finite_diagnostic`, scoped to the corpus it was run against —
> never stated as a general detection rate.

**Schema fields:** none new (reads existing `genre`, `venue_track`, and a new CLI-only output
object, not a claim-card field):
```json
{"layer_confusion_flag": {"layer_claimed": "string", "layer_invoked": "string", "confidence": "finite_diagnostic_scoped"}}
```

**Kernel rule:**
- `rule21(LAYER-MISMATCH-FLAGGED)`: `"rule21: genre/register layer does not match invoked tool/authority layer -- routed to human review, not auto-corrected"` (warning, not error — diagnostic-only per the DAG's own risk framing).

**Acceptance test (DAG's literal test, kept as the ship-gate, refined by sim):** "CLI run against a
synthetic mismatched-layer card set (N=10) flags all mismatches with zero false positives on a
matched-layer control set" — **run as the DAG's own literal N=10 fixture, not substituted with the
180-card corpus** (the sim report's own flagged gap), plus a held-out differently-worded N=10
fixture before this leaves `revise`.

**Evidence ids:** kc-islam-009.

---

## 4. `foundation.s7.9-intake-tier-flag` — claim-tier intake flag

- **status:** pending-founder: thin-layer-scope-confirmation. DAG marks `human_decision_needed:
  true`; sim recommends **revise** (its four detectors are reverse-engineered from this corpus's
  fixtures, not from the node's own proposed AACODS-style mechanism, which has no fixtures here —
  `sim/v0.3/report.md` §3). **Recommended option:** adopt the DAG's own thin-layer text verbatim
  (a flag-and-request-tier step layered on the existing AACODS-style checklist, with the Global
  South evidence-genre exemption), but do not claim the sim's measured +1.0 delta as evidence for
  *this* mechanism — that number was produced by a different (defect-detector) proxy, not the
  actual proposed AACODS layer, and the sim report says so explicitly.
- **FOUNDATION target:** §7.9 Literature Review System (LRS)

**Exact text to insert into §7.9, after the "Two separate manifest gates" subsection:**

> **Claim-tier intake flag (thin addition to the accuracy gate, not a new mechanism).** At L4
> (reading & extraction), a source is flagged `intake_tier: request_tier` when its own genre would
> normally suppress an AACODS trace-to-original+appraise pass (e.g. a policy brief, a grey-literature
> report, an anecdotal/expert/local-knowledge account) — the flag requests a tier assignment rather
> than rejecting the source outright. **Explicit exemption:** Global South anecdotal, expert, and
> local-knowledge evidence genres are never treated as automatically suspect by this flag alone;
> the flag names a gap in the existing checklist's coverage, not a downgrade of the source's
> standing. A flagged-and-tiered row is distinct in the manifest from a rejected row.

**Schema fields (`litreview_manifest.yaml`, additive):**
```yaml
sources_found:
  - intake_tier: request_tier | not_flagged   # NEW — default not_flagged
    intake_tier_reason: string | null          # required non-empty when intake_tier=request_tier
    global_south_exempt: bool                  # NEW — true suppresses the D-LIT-* suspicion framing
```

**Kernel rule:**
- `rule22(INTAKE-TIER-UNTIERED)`: `"rule22: source flagged intake_tier=request_tier requires a non-empty intake_tier_reason and a distinct manifest row, never merged with a rejected row"` (error).

**Acceptance test (DAG's own, kept):** "LRS run on a policy-brief-only source set produces a
flagged-not-blocked intake row, distinct from a rejected row." **Sim caveat carried forward
explicitly:** this test must be run against fixtures built for the actual AACODS-layer mechanism,
not against the existing 180-card corpus (which has no such fixtures) — the sim's +1.0 number does
not certify this mechanism and must not be cited as if it did.

**Evidence ids:** kc-ai-024, kc-he-018.

---

## 5. `schema.verdict-class-vocabulary` — verdict-class vocabulary field

- **status:** pending-founder: none (no `human_decision_needed` flag on this node) but **sim
  status is revise, not ship** — flagged here as a scope caveat rather than a founder decision:
  the four detectors backing its measured +1.0 delta are hand-curated from one exemplar fixture
  per defect class, individually falsifiable by an out-of-lexicon counter-fixture, and the node's
  own literal acceptance test (schema enum accepting `FORCED`, rejecting a 7th value) was not run
  in S4 (`sim/v0.3/report.md` §3, third bullet). **Recommended option:** land the schema enum
  itself (a static, mechanically checkable addition unaffected by the lexicon-fragility finding)
  and treat the lexicon-based detection claim as still open pending the out-of-lexicon holdout.
- **FOUNDATION target:** FOUNDATION field `base_relation` (holds|refined_by_later_work|superseded|
  outdated|open)

**Exact text to insert adjacent to `base_relation`'s definition (§3.2 or wherever `base_relation`
is defined in the shipped schema — FOUNDATION currently states this field only by reference to the
DAG's own target line, not with an inline definition; this patch adds one):**

> **`verdict_class`** (new field, additive, six-value enum): `DERIVED | FORCED | DEFINITIONAL-
> RELABEL | POSITED | BORROWED-SCALE | OPEN`. This is a **different axis** from `base_relation`:
> `base_relation` states how a claim relates to a base text (holds/refined/superseded/outdated/
> open); `verdict_class` states what *kind* of derivation the claim itself is, independent of any
> base-text relation. A card may have `base_relation: holds` and `verdict_class: BORROWED-SCALE` at
> the same time — the two fields are never collapsed into one enum.

**Schema fields:**
```json
{
  "verdict_class": {"enum": ["DERIVED", "FORCED", "DEFINITIONAL-RELABEL", "POSITED", "BORROWED-SCALE", "OPEN"]}
}
```

**Kernel rule:**
- `rule23(VERDICT-CLASS-UNLISTED)`: `"rule23: verdict_class must be one of the six listed values -- an unlisted seventh value is a hard schema-validation error"` (error, schema-enforced per §3.3's own "fully schema-enforced" category, no kernel code needed — parallels rule 1/2/10/11's schema-only enforcement).

**Acceptance test (DAG's literal test, now actually run, closing the sim gap):** "JSON schema
validates a claim card with `verdict_class=FORCED` and rejects an unlisted seventh value." — this
patch requires this literal test be executed before ship, since sim confirms it was not run this
pass.

**Evidence ids:** kc-base-038.

---

## 6. `kernel.pcs-red-flag` — Premature Category Stabilization (PCS) red-flag

- **status:** pending-founder: PCS-scoping-confirmation (DAG `human_decision_needed: true`; sim:
  **revise** — the real corpus has zero fixtures of this concept at all, so its measured delta is
  0.0 by construction, not by weak design; separately, its own literal N=60/3-class synthetic
  acceptance test was run independently and passed exactly, but on a same-lexicon self-test, not
  the shipped corpus). **Recommended option:** adopt the DAG's own scoped text (PCS fires only when
  BOTH closure-timing AND absence-of-adaptation hold jointly; never merged with the clinical term
  "premature closure") and require an out-of-lexicon holdout plus independent adversarial review
  before this leaves `revise` — exactly what the sim report itself recommends.
- **FOUNDATION target:** §5/§6 disclaimer+genre-router; kernel contaminated-concept table
  (base-018)

**Exact text to insert into §5's disclaimer catalogue, as a new contaminated-concept-table row
(not a new disclaimer id — PCS is a red-flag on the *contaminated-concept* scan, §3.3 rule 8's
family, not a standalone disclaimer trigger):**

> **Premature Category Stabilization (PCS)** — added to the contaminated-concept table this pass,
> scoped narrowly: fires only when a claim exhibits **both** (a) closure-timing (a category/
> conclusion locked in before the evidence-gathering step that would normally precede it) **and**
> (b) absence-of-adaptation/contextual-fit (the locked category is never revisited against a
> changed context). Timing alone, or lack-of-adaptation alone, does not fire this flag — two
> independent counter-cases exist (decoupled closure that later corrects itself; successful
> non-premature adoption that looks timing-early but was contextually validated) and over-broad
> scoping would misfire on both. **Never merged with the clinical term "premature closure"** — a
> distinct, unrelated diagnostic concept from a different domain; same-shaped name, different
> mechanism (comparison: different, not same).

**Schema fields:** none new — this is a kernel text-scan rule (§3.3 rule 8's family), not a schema
field, matching how rule 8 itself is kernel-only (schema/README.md's own "3 permanently kernel-only"
category).

**Kernel rule:**
- `rule24(PCS-JOINT-CONDITION)`: `"rule24: Premature Category Stabilization flag requires BOTH closure-timing AND absence-of-adaptation to hold jointly -- neither alone fires this flag"` (error, when both hold); `"rule24w: closure-timing present without absence-of-adaptation (or vice versa) -- logged, not flagged as PCS"` (warning).

**Acceptance test (DAG's own, refined by sim):** "finite_diagnostic sim: run N synthetic claim
cards with (a) timing-only closure, (b) timing+no-adaptation, (c) neither — kernel flags only class
(b); precision on class (b) must be 100% on the synthetic set before this ships." **Sim refinement:**
this test must additionally include an out-of-lexicon holdout batch (differently-worded class-(b)
fixtures not built from the same generator vocabulary as the N=60/3-class self-test that already
passed) — the self-test alone is same-lexicon and does not license `ship`.

**Evidence ids:** kc-ep-018, kc-ep-019, kc-ep-020, kc-islam-011, kc-tourism-002.

---

## 7. `kernel.unverified-verifiability-flag` — DROPPED

Sim reason (§3, §6): delta_recall 0.0 — `verifiable_no_procedure` is already 8/8 caught via the
kernel's existing `D-DVP-NOT-K2` disclaimer trigger; the prototype adds no measured coverage over
the unmodified kernel on this corpus. No patch text. The DAG's underlying concern (nest "verifiable
with no stated procedure" under the vague-attribution catalogue entry, intent-dependence defeats
pure automation) remains a fair reading of `kc-tourism-006` but is not actioned this pass absent a
measured gap to close.

## 8. `schema.prereg-gate-fields` — DROPPED

Sim reason (§3, §6): delta_recall/delta_false_alarm both 0.0 — the corpus has zero fixtures
carrying prereg timestamp/ethics-applicability sequencing at all, so no movement could be measured
either way. **Separately flagged (DAG risk column, High):** a naive hard-block implementation would
misdescribe real registry practice; per this DAG node's own risk note, the founder decision this
node names (`pending-founder: prereg-gate-hard-vs-soft`, not resolved by this patch) stays open —
dropped from this pass's ship set on sim grounds alone, independent of that separate founder
question.

---

## 9. `foundation.s1.0-infinity-tension-flag` — DEFERRED (kept `[Open]`, unchanged)

One line, DAG's own sim/status reason: `deferred`, not proposed for build this pass — the flag
must stay an explicit `[Open]` block in §1.0 (already present per `FOUNDATION_v0.5_PATCH.md`'s own
§1.0 insertion) rather than a formal reconciliation; no new text this patch. Evidence: kc-ep-005.

## 10. `rule17.claim-card-certification-open` — DEFERRED (kept `[Open]`, unchanged)

One line, DAG's own reason: kept `[Open]` pending a falsifier that tests claim cards directly, not
formalized into rule 17 or the I0–I5 ladder this pass. No new text this patch. Evidence:
kc-ai-006, kc-aihp-002, kc-aihp-003.

---

## 11. `foundation.s1.0-ashari-ontology-analogue` — partial theology-neutral ontology analogue

- **status:** pending-founder: partial-analogue-adoption (DAG `human_decision_needed: true`, risk
  Medium — "partial adoption is defensible from the evidence but risks looking arbitrary without
  the full reasoning carried into the commit message"). **Recommended option (the DAG's own stated
  change, adopted in full, with the arbitrariness risk addressed by stating the exclusion reason
  inline rather than only in a commit message):**
- **FOUNDATION target:** §1.0 Pillars — ontology

**Exact text to insert into §1.0, in the existing "Ontology" paragraph, as an additional sentence
after the existing `RA = OA(W;ΠA) ≠ W` sentence:**

> A theology-neutral structural analogue is adopted for two of the three constructs this reading
> surfaces: "Dependent Identity" maps to grounding/ontological-dependence theory, and "Directed
> Selection" maps to the Principle of Sufficient Reason — both cited directly (kc-ep-030, kc-ep-034)
> as parallel formulations, comparison: same structural role, not identical content. **Excluded by
> the same reasoning, stated here rather than only in a commit message:** "Dependent Order" (kasb)
> and the five registers of faqr as a whole are not given a structural analogue — their content is
> specific to their originating discourse in a way the other two constructs are not, and forcing an
> analogue would misrepresent rather than translate them. This is a partial adoption by design, not
> an oversight.

**Schema fields:** none (prose-only, ontology section).

**Kernel rule:** none (no mechanically-checkable claim; citation-only prose addition).

**Acceptance test (DAG's own, unchanged):** "FOUNDATION §1.0 diff cites grounding-theory and PSR
sources directly, with an explicit line excluding kasb/faqr from the analogue."

**Evidence ids:** kc-ep-030, kc-ep-034.

---

## 12. `foundation.honest-edges-agrippa` — Agrippa's trilemma applied to the tier system

- **status:** ready (no human decision flagged; Low risk, citation-only)
- **FOUNDATION target:** §12 Honest edges

**Exact text to insert into §12, as a new named subsection:**

> **Agrippa's trilemma, applied to the tier system itself.** The tier ladder (`Th_coqc |
> finite_diagnostic | fit_calibrated | Dr | definition | Open`) is not self-certifying — any
> justification chain for "why trust this tier assignment" terminates in infinite regress,
> circularity, or an unjustified stopping point (Agrippa's trilemma, cited kc-base-025, kc-base-031,
> kc-base-036), exactly like any other justificatory chain. The tier system's honest response is not
> to claim escape from the trilemma but to make the stopping point explicit and checkable
> (`independent_check`, §7.2's maker/checker/approver separation) rather than silent — the trilemma
> is why `EPIS-KNOWLEDGE-VALIDATION`'s horizontal-only stance is a design necessity, not a
> preference: there is no non-circular vertical stopping point available to appeal to instead.

**Schema fields:** none.

**Kernel rule:** none (prose-only philosophical grounding, no new mechanical check).

**Acceptance test (DAG's own, unchanged):** "§12 diff adds a named subsection citing Agrippa's
trilemma with the three evidence card ids as sources."

**Evidence ids:** kc-base-025, kc-base-031, kc-base-036.

---

## 13. `foundation.disclaimer-catalogue-expand` — novelty-scoping and standpoint-disclosure patterns

- **status:** ready (Low risk, additive catalogue entries)
- **FOUNDATION target:** §5 Systematic disclaimer catalogue

**Exact text to insert into §5, as four new reusable clause patterns (not new `D-*` ids — reusable
prose templates, cited by name where used):**

> **Reusable disclaimer patterns (new this pass):**
> 1. *"Novelty scoped to architecture, not mechanism"* — used when a claim assembles existing
>    mechanisms into a new arrangement without claiming any individual mechanism is new (kc-he-013).
> 2. *"Analytical tool, not verdict"* — used when a schema/checklist/framework produces a
>    structured description, not a pass/fail judgment on the thing it describes (kc-he-015).
> 3. *"Theoretical/analytical, not empirical"* — used when a claim is a conceptual/structural
>    argument with no data collection behind it, distinct from `tier: Dr`'s broader meaning
>    (kc-he-019, kc-islam-007).
> 4. *Reflexive practitioner standpoint/conflict-of-interest disclosure* — used whenever the
>    author's own practice, role, or position could plausibly bias the claim being made
>    (kc-islam-016, kc-se-006).
>
> These are distinct in scope from `foundation.s5-scope-boundary-per-instance`'s per-instance
> jurisdiction clause (§14 below) — that clause is about legal/deployment context; these four are
> about the claim's own epistemic scope and the author's standpoint.

**Schema fields:** none (catalogue prose, `methodology/data/disclaimer_catalogue.json` gains four
named pattern strings, not new `D-*` trigger ids — no schema change).

**Kernel rule:** none (these are author-selected prose patterns, not mechanically triggered).

**Acceptance test (DAG's own, unchanged):** "§5 diff adds 4 named reusable clause patterns, each
with a worked source example distinct from foundation.s5-scope-boundary-per-instance's per-instance
jurisdiction clause."

**Evidence ids:** kc-he-013, kc-he-015, kc-he-019, kc-islam-007, kc-islam-016, kc-se-006.

---

## 14. `foundation.s5-scope-boundary-per-instance` — per-instance scope clause

- **status:** pending-founder: per-instance-vs-standardized-disclaimer (DAG `human_decision_needed:
  true`, risk Medium — "the evidence largely defeats a single standardized clause; risk is
  per-instance variation becoming unmanaged per-hub duplication"). **Recommended option (the DAG's
  own stated change — per-instance, not standardized, since that is what the evidence majority
  supports):**
- **FOUNDATION target:** §5 Systematic disclaimer catalogue

**Exact text to insert into §5, as a new rule on the non-clinical/non-medical/non-legal scope
clause:**

> **Non-clinical/non-medical/non-legal scope clause — per-instance, not standardized.** No single
> reusable disclaimer text is mandated across all AI-runtime instances of glosa-adjacent tooling.
> Each instance's disclaimer must instead be **paired with an explicit context/jurisdiction check**:
> time-criticality (is a delay-sensitive decision plausible here), deployment jurisdiction (which
> legal regime applies), and legal-category availability (does the relevant professional category
> even exist/apply in this jurisdiction). **Named risk, tracked not solved by this rule:** per-
> instance variation risks becoming unmanaged duplication across hubs/deployments — this rule does
> not build a registry to prevent that; it is logged here as an accepted, disclosed limitation.

**Schema fields:** none (deployment-level disclaimer text, not a claim-card field).

**Kernel rule:** none (a deployment-configuration requirement, not a claim-card-level check).

**Acceptance test (DAG's own, unchanged):** "FOUNDATION §5 diff reviewed: every disclaimer entry
carries a jurisdiction/time-criticality field, not just boilerplate text."

**Evidence ids:** kc-ai-023, kc-he-016.

---

## 15. `foundation.pillars-readout-not-truth` — Pillars §1.0 cross-tradition citation set

- **status:** ready (Low risk, citation-only, no wording change to base doctrine)
- **FOUNDATION target:** §1.0 Pillars — ontology/epistemology/methodology

**Exact text to insert into §1.0, as a new closing paragraph:**

> **Cross-tradition citation set (this pass).** The readout-not-truth stance, the bounded-knower
> framing, "tracking truth" as a named epistemic target, and the δ_R primitive each appear,
> independently arrived at, in the cited base texts and in kc-base-001, kc-base-005, kc-base-009,
> kc-base-027, kc-base-032, kc-ep-014, kc-ai-019, kc-islam-008. These are cited as **parallel,
> independently-arrived-at formulations** — comparison: same underlying distinction, cited, never
> as external validation of glosa's own stance (`EPIS-KNOWLEDGE-VALIDATION`) and never as
> priority/first-arrival framing (gate rule 6).

**Schema fields:** none.

**Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "FOUNDATION §1.0 diff adds citation lines for each
evidence card id with no wording change to the base doctrine text."

**Evidence ids:** kc-base-001, kc-base-005, kc-base-009, kc-base-027, kc-base-032, kc-ep-014,
kc-ai-019, kc-islam-008.

---

## 16. `foundation.non-collapse-table-expand` — Appendix A cross-tradition rows

- **status:** ready (requires §15 land first for shared terminology, per DAG edge)
- **FOUNDATION target:** Appendix A Non-Collapse Table

**Exact text to insert into Appendix A, as a new Family J:**

> ### Family J — Cross-tradition parallels (new this pass, v0.6)
> `NC-74` Equal-number-of-distinctions≠Equal-epistemic-standing (the equal-number fallacy;
> kc-base-004) · `NC-75` Same-shaped formula≠Same tier (three formally identical tiers can carry
> different epistemic weight; kc-base-021, kc-ep-021) · `NC-76` θ(E) relational invariance≠
> θ(E) absolute value (kc-ep-023, kc-ep-024, kc-ep-026, kc-ep-027). *Enforced by: `tier`,
> `evidence_strength.class` (§2 above), §1.0 Pillars. Full rows: `design/S9_non-collapse-
> table.md`.*

Also update Appendix A's opening line ("73 rows across eight families") to "76 rows across nine
families."

**Schema fields:** none (table is prose/reference, not a schema object).

**Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "Appendix A table has ≥3 new rows, each with a card id
+ source DOI, no row lacking a locator (rule 17)."

**Evidence ids:** kc-base-004, kc-base-021, kc-ep-021, kc-ep-023, kc-ep-024, kc-ep-026, kc-ep-027.

---

## 17. `foundation.responsibility-arrow-mother-eq` — mother-equation framing

- **status:** ready (requires §15 land first, per DAG edge)
- **FOUNDATION target:** §2.1b Responsibility per arrow

**Exact text to insert into §2.1b, as a citation-only addition, no change to existing rule 15/16w
wording:**

> **Mother-equation framing (cited, kc-base-014, kc-base-020).** "A record is a translation, never
> the truth itself" — cited here as the framing that grounds why §2.1b's existing Data→Inference→
> Claim responsibility split treats each arrow as carrying its own, non-transferable responsibility
> obligation, rather than one blanket "the data supports the claim" statement.

**Schema fields:** none.

**Kernel rule:** none (citation-only; rules 15/16w already implemented in kernel, unchanged).

**Acceptance test (DAG's own, unchanged):** "§2.1b diff adds the mother-equation citation without
altering the existing rule 15/16w wording."

**Evidence ids:** kc-base-014, kc-base-020.

---

## 18. `foundation.ead-crosswalk` — E-A-D norm as named source of §3.1 crosswalk

- **status:** ready (requires §5 schema.verdict-class-vocabulary land first per DAG edge, for
  consistent field naming — the citation itself does not depend on the schema field, only the
  DAG's stated build order does)
- **FOUNDATION target:** §3.1 Five Questions ⇄ E-A-D ⇄ field crosswalk

**Exact text to insert directly above the §3.1 crosswalk table:**

> **Named source (this pass).** The Existence-Attribution-Disclosure (E-A-D) norm underlying this
> crosswalk is cited directly to The Readout Condition papers (kc-ep-042, kc-aihp-011, kc-ai-001) —
> the crosswalk table itself is unchanged; this closes the gap of an until-now uncredited mapping.

**Schema fields:** none. **Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "§3.1 diff adds a citation line naming the E-A-D source
papers directly above the crosswalk table."

**Evidence ids:** kc-ep-042, kc-aihp-011, kc-ai-001.

---

## 19. `foundation.possession-constitution-collapse` — named AI-authorship rule source

- **status:** ready (requires §18 land first per DAG edge)
- **FOUNDATION target:** §3.2b / §7 Gates & review (AI-authorship rules)

**Exact text to insert into §3.2b, adjacent to the existing rule-17 provenance-only-channel text:**

> **Named source (this pass).** "Possession-Constitution Collapse" and "knower fetishism" (cited:
> kc-ep-043, kc-ai-003, kc-ai-004, kc-aihp-013, kc-aihp-014) are the named source for why an
> AI-drafted claim card is not disqualified by authorship alone, and for the "channel over face" /
> provenance-only-metadata rule already implicit in rule 17 (source-first citation) — the rule text
> itself is unchanged; this adds the citation.

**Schema fields:** none. **Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "§3.2b/§7 diff cites the named source papers alongside
the existing rule-17 provenance-only-channel text."

**Evidence ids:** kc-ep-043, kc-ai-003, kc-ai-004, kc-aihp-013, kc-aihp-014.

---

## 20. `foundation.independence-ladder-i0-i5-source` — I0–I5 named source

- **status:** ready (requires §18 land first per DAG edge)
- **FOUNDATION target:** §4.2 Independence Ladder I0–I5

**Exact text to insert into §4.2, as a citation-only addition, no renumbering/redefinition:**

> **Named source (this pass, kc-ep-052, kc-ai-002).** The I0–I5 Independence Ladder and the
> falsifiable-propositions framing already used in this section are cited to "Rigour Without
> Infrastructure" — the ladder's existing five classes and definitions are unchanged.

**Schema fields:** none. **Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "§4.2 diff adds the named citation without renumbering
or redefining the existing I0–I5 classes."

**Evidence ids:** kc-ep-052, kc-ai-002.

---

## 21. `foundation.k-state-standalone-scholar-cite` — K-state named origin

- **status:** ready (requires §20 land first per DAG edge)
- **FOUNDATION target:** §4.4 K-state (Standalone Scholar, PRESERVE_EXACT)

**Exact text to insert into §4.4, as a citation-only addition:**

> **Named source (this pass, kc-ep-041, kc-aihp-017, kc-ai-011).** "The Standalone Scholar" is
> cited as the named origin of the K-state concept and the PRESERVE_EXACT dual-track architecture
> already used in this section — existing definitions unchanged.

**Schema fields:** none. **Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "§4.4 diff adds the named citation without altering the
existing K-state/PRESERVE_EXACT definitions."

**Evidence ids:** kc-ep-041, kc-aihp-017, kc-ai-011.

---

## 22. `docs.blackbox-log-formalize-source` — Blackbox Log named-origin citation

- **status:** ready (Low risk, citation-only)
- **FOUNDATION target:** §2.3 Blackbox Note and R0/R1/R2 internal registers

**Exact text to insert into §2.3's Blackbox Note bullet, as a citation-only addition:**

> **Named source (this pass, kc-ep-047, kc-ai-008).** "Blackbox Log: daily append-only verbatim
> voice record" is cited directly as the named artifact this section already formalizes —
> resolving the previously uncredited appendix language. Consistent with, not contradicting,
> `PUBLISH_GATE_v1_public.md` finding B-10's disclosed removal+restore correction entry.

**Schema fields:** none. **Kernel rule:** none.

**Acceptance test (DAG's own, unchanged):** "§2.3 diff adds the named citation line;
PUBLISH_GATE_v1 finding B-10 (Blackbox Log provenance disclosure) cross-referenced, not
contradicted."

**Evidence ids:** kc-ep-047, kc-ai-008.

---

## 23. `foundation.lrs-discovery-loop-extension` — discovery-loop extension

- **status:** pending-founder: discovery-routing-stage-adoption (DAG `human_decision_needed: true`,
  risk Medium — the underlying agenda-paper claim (kc-aihp-008/009) stays `[Open]`, not adopted;
  this node only operationalizes already-`holds`/`adapt` cards). **Recommended option (DAG's own
  stated change, gated as an extension not a replacement):**
- **FOUNDATION target:** §7.9 Literature Review System (LRS) / §6 discovery extension

**Exact text to insert into §7.9, after the Hypothesis selection subsection:**

> **Discovery-routing extension (gated, this pass).** §7.9's L1–L6 pipeline may be preceded by a
> discovery-routing stage: the human retains ownership of the question; the AI recursively
> decomposes it into candidate sub-questions and gates each candidate before it enters L1, using
> `k_epi` (the epistemic-multiplication construct, cited kc-ep-045, kc-ep-046, kc-ep-048, kc-ep-049,
> kc-aihp-005, kc-aihp-006, kc-aihp-010, kc-aihp-020) as the gating construct. This is an
> **extension**, never a replacement — every candidate that survives the gate still runs the full
> L1–L6 pipeline unchanged. **Not adopted this pass:** the broader agenda-paper claim behind this
> construct (kc-aihp-008, kc-aihp-009) stays logged `[Open]` — this text operationalizes only the
> already-`holds`/`adapt` cards, not the open agenda claim itself.

**Schema fields (`litreview_manifest.yaml`, additive):**
```yaml
discovery_routing:
  used: bool                       # default false
  candidate_questions: [string]
  k_epi_gate_log: [{question, gated_out: bool, reason}]
```

**Kernel rule:**
- `rule25(DISCOVERY-CANDIDATE-UNGATED)`: `"rule25: discovery_routing.used=true requires every candidate_questions entry to have a k_epi_gate_log row before it may enter L1"` (error).

**Acceptance test (DAG's own, unchanged):** "S4 finite_diagnostic sim compares LRS precision/recall
on the same question set with and without the discovery-routing stage; ship only if recall
improves without a precision drop." Not yet run this pass — no fixtures exist for this mechanism.

**Evidence ids:** kc-ep-045, kc-ep-046, kc-ep-048, kc-ep-049, kc-aihp-005, kc-aihp-006, kc-aihp-010,
kc-aihp-020.

---

## New nodes: the three still-missed K4 defect classes

`sim/v0.3/report.md` §4/§6: after combining the two ship-recommended S4 prototypes, `composite_
quote` and `hidden_ai_fill` remain 9/9 missed each; `inflated_bearing` is closed at the schema
level by §2 above but not yet at the kernel-rule level (a card could still satisfy the new schema
fields while the underlying citation card's own scope disqualifies the bearing claimed). These
three nodes close all three at the kernel-rule level, continuing the DAG numbering with a `K-C`
prefix (Kernel-Closure) since they were not part of the original 26-node DAG.

### K-C1 — composite-quote detector

- **status:** ready (closes a named sim gap directly; mechanically checkable, no lexicon-fragility
  risk of the kind flagged against the three "revise" S4 prototypes, since this rule is a
  structural check on `exact_passage`/locator shape, not a keyword match on prose content)
- **FOUNDATION target:** §7.8 Citation integrity subsystem (Integrity Firewall) — new hard rule

**Exact text to insert into §7.8, after the existing Integrity Firewall paragraph:**

> **Composite-quote detector (new this pass, closes a K4 sim-confirmed gap).** A citation card's
> `exact_passage` containing an ellipsis marker ("…", "...", or a spaced double-hyphen " -- " used
> as an ellipsis substitute) **splicing across a boundary**, or a single citation card whose
> `exact_passage` cites **two non-adjacent locators** (e.g. page 3 and page 47 concatenated into
> one quoted string), is a composite quote: text assembled from non-contiguous source material and
> presented as one continuous passage. This is a hard error, not a disclaimer — a composite quote
> defeats `claim_match_verified` by construction, since no single passage in the original source
> reads as quoted (`NC-18` Source existence≠Claim support, applied to passage-level contiguity).

**Schema fields (`citation_card.yaml` / `citation_card.schema.json`, additive validation, not a new
field — the check reads existing `exact_passage` and `identifier`/locator fields):**
```json
{
  "exact_passage": {
    "type": "string",
    "not": {"pattern": "(\\.\\.\\.|…|\\s--\\s)"}
  },
  "locators": {
    "type": "array",
    "maxItems": 1,
    "description": "a single exact_passage may cite at most one contiguous locator; a second, non-adjacent locator on the same passage is the composite-quote pattern this rule blocks"
  }
}
```

**Kernel rule number / strings:**
- `rule26(COMPOSITE-QUOTE)`: `"rule26: exact_passage contains an ellipsis/splice marker ('…'/'...'/' -- ') or cites two non-adjacent locators -- composite quotes are not verifiable as a single continuous passage"` (error).

**Acceptance test (from the sim numbers):** re-run the 9-card `composite_quote` fixture slice from
`sim/v0.3/corpus/`; must reach 9/9 caught (from the baseline's 0/9, `sim/v0.3/report.md` §2) with
zero new false alarms on the 60 valid cards (all of which have single-locator, splice-free
`exact_passage` values by construction, per the corpus generator's own valid-card method, §1 of the
report).

**Evidence ids:** sim/v0.3/report.md §1–§2 (defect id `composite_quote`, corpus generator
`sim/v0.3/gen_corpus.py`); FOUNDATION §7.8 `exact_passage`/`scope` field definitions.

---

### K-C2 — hidden-AI-fill detector

- **status:** ready (closes a named sim gap directly; structural cross-check between two existing
  fields, not a prose keyword match)
- **FOUNDATION target:** §2.3 Blackbox Note / cooking log; §3.1 crosswalk (`five_questions.seen`
  vs `five_questions.ai_filled`)

**Exact text to insert into §2.3, after the Blackbox Note bullet's cooking-log description:**

> **Hidden-AI-fill detector (new this pass, closes a K4 sim-confirmed gap).** When a Blackbox
> Note's cooking log (or a card's own `ai_filled` sub-fields) lists an AI drafting step for a
> specific field, but `five_questions.seen` presents that same field's content as directly observed
> (no `ai_filled.*` marker on that field, `record_ref` implying a first-hand read), the two records
> contradict each other — this is a hard error, not a disclaimer, since it is exactly the E-A-D
> Disclosure failure (`five_questions.ai_filled`'s crosswalk, §3.1) that `silent_lift_check` is
> designed to catch structurally rather than by re-doing the epistemic work by hand.

**Schema fields:** none new — the check is a cross-field consistency rule between the existing
`five_questions.seen`, `five_questions.ai_filled`, and the Blackbox Note's `cooking:` log entries
(no new field, a kernel-only comparison, matching the class of check §3.3 rules 5/6/8 already are).

**Kernel rule number / strings:**
- `rule27(HIDDEN-AI-FILL)`: `"rule27: cooking log / ai_filled lists an AI drafting step for a field that five_questions.seen presents as directly observed -- contradiction between disclosure records"` (error).

**Acceptance test (from the sim numbers):** re-run the 9-card `hidden_ai_fill` fixture slice; must
reach 9/9 caught (from baseline's 0/9) with zero new false alarms on the 60 valid cards (whose
`ai_filled`/`seen`/cooking-log fields agree by construction, per the generator's valid-card method).

**Evidence ids:** sim/v0.3/report.md §1–§2 (defect id `hidden_ai_fill`); FOUNDATION §3.1 crosswalk
(Q1 `five_questions.seen`, Q3 `five_questions.ai_filled`); §2.3 Blackbox Note cooking log.

---

### K-C3 — inflated-bearing detector

- **status:** ready (closes the kernel-rule half of the gap §2 above closes at the schema level —
  a card can satisfy `evidence_strength.class` shape-wise while the underlying citation card's own
  `scope` still disqualifies the claimed bearing; this rule is the cross-object check that catches
  that case)
- **FOUNDATION target:** §7.8 Citation integrity subsystem / §3.2 `tested.evidence_relations[]`

**Exact text to insert into §7.8, after the K-C1 composite-quote text above:**

> **Inflated-bearing detector (new this pass, closes a K4 sim-confirmed gap, kernel-rule half of
> `schema.claim-card-comparison-evidence-field`, §2 above).** An `evidence_relations[]` entry with
> `bearing: SUPPORTS` whose `citation_ref` points at a citation card with `scope:
> CONTEXT_ONLY_NOT_EVIDENCE`, or whose `notes` field marks the source as same-lineage/own-lineage
> (the citing and cited work share an author, a project, or a direct derivation relationship), is a
> hard error **unless** `strength` explicitly states "context" (i.e. the entry is honestly scoped
> as background/context support, not evidentiary support). This closes the case §2's schema-only
> `evidence_strength` field cannot catch alone: a card can satisfy the schema shape while the
> underlying citation's own `scope`/lineage disqualifies the bearing being claimed at the object-
> cross-reference level.

**Schema fields:** none new — reads existing `tested.evidence_relations[].bearing`,
`tested.evidence_relations[].strength`, and the referenced citation card's existing `scope` and
`notes` fields (a cross-object kernel check, same class as §3.3 rules 5/6).

**Kernel rule number / strings:**
- `rule28(INFLATED-BEARING)`: `"rule28: evidence_relation bearing=SUPPORTS cites a scope=CONTEXT_ONLY_NOT_EVIDENCE or same-lineage citation card without strength='context' -- bearing is inflated relative to what the citation actually supports"` (error).

**Acceptance test (from the sim numbers):** re-run the 9-card `inflated_bearing` fixture slice; must
reach 9/9 caught by this kernel rule *in addition to* the schema-level catch from §2 above (the S4
prototype already measured +0.25 delta / 9 cards caught via the schema-adjacent detector; this rule
is the object-cross-reference backstop for cards that pass the schema shape check but still cite a
disqualifying source), zero new false alarms on the 60 valid cards.

**Evidence ids:** sim/v0.3/report.md §1–§2 (defect id `inflated_bearing`); FOUNDATION §7.8 `scope`
enum (`CONTEXT_ONLY_NOT_EVIDENCE`); §3.2 `tested.evidence_relations[]` field shape.

---

## Non-collapse table additions

Rows added by this patch beyond `NC-74`..`NC-76` already placed in §16 above — none; §16's Family
J (`NC-74`, `NC-75`, `NC-76`) is the complete set this pass adds. No further non-collapse
distinction was identified as load-bearing in the K-C1/K-C2/K-C3 kernel rules above (each is a
structural/cross-field check, not a new conceptual distinction requiring its own table row) or in
the founder-decision nodes (each reuses an existing non-collapse pair already tabulated — `NC-17`
Mechanical validity≠Semantic validity covers the layer-confusion diagnostic's own honest limit,
`NC-72` Constraint≠evidence-for-us covers `evidence_strength.class`'s adjacent/direct split).

| id | pair | enforced by |
|---|---|---|
| `NC-74` | Equal-number-of-distinctions≠Equal-epistemic-standing | `tier`, §1.0 Pillars |
| `NC-75` | Same-shaped formula≠Same tier | `tier`, `evidence_strength.class` |
| `NC-76` | θ(E) relational invariance≠θ(E) absolute value | §1.0 Pillars |

---

## Rule numbering table

| range | status | source |
|---|---|---|
| 1–11 | shipped (kernel + schema, per `schema/README.md`'s enforcement table) | FOUNDATION_v0.5.md §3.3 |
| 12 | shipped (kernel: `rule12`/`rule12b`, D-LENS-UNSIGNED/D-LENS-UNCITED) | FOUNDATION_v0.5.md §3.3 rule 12, `kernel/glosa_kernel.py` |
| 13–14 | **spec-only** — stated in FOUNDATION §3.3 prose, no kernel/schema implementation found in `kernel/glosa_kernel.py` this pass | FOUNDATION_v0.5.md §3.3 rules 13/14 |
| 15–17 | **shipped in kernel, not yet folded into FOUNDATION §3.3's numbered prose** — `rule15`/`rule15w` (responsibility arrow), `rule16w` (empirical_extension warning), `rule17`/`rule17w` (source-first citation) | `kernel/glosa_kernel.py` |
| 18–28 | **this patch** — 18/19 injected-infinity/zero taxonomy + Fail-Able Gate Law (§1), 20 novelty-word rejection (§2), 21 layer-mismatch flag (§3, warning), 22 intake-tier untiered (§4), 23 verdict-class unlisted (§5), 24/24w PCS joint-condition (§6), 25 discovery-candidate ungated (§23), 26 composite-quote (K-C1), 27 hidden-AI-fill (K-C2), 28 inflated-bearing (K-C3) | this patch |

**Open item for the schema/kernel-owning fixer (not resolved by this patch, flagged per
`FOUNDATION_v0.5_PATCH.md`'s own precedent):** fold rules 15–17 into FOUNDATION §3.3's numbered
prose before or alongside applying this patch's 18–28, so the numbered list in FOUNDATION text
matches what `kernel/glosa_kernel.py` actually implements — the gap identified here (kernel ahead
of FOUNDATION prose by three rules) should not be allowed to widen further with this patch's own
ten new rules layered on top of an already-stale numbered list.

---

## Founder decisions required before any build (per node, this patch)

Per `EPIS-KNOWLEDGE-VALIDATION` (no external validation lever; founder is the internal decision
owner per `design/ROADMAP_v0.3.md`), none of the `pending-founder` sections above may be committed
to `DECISIONS.yaml` or built without an explicit founder ruling on the named decision:

- §3 `cli.genre-router-layer-confusion-check` — decision: `promote-from-revise-to-ship-gate`
- §4 `foundation.s7.9-intake-tier-flag` — decision: `thin-layer-scope-confirmation`
- §6 `kernel.pcs-red-flag` — decision: `PCS-scoping-confirmation`
- §11 `foundation.s1.0-ashari-ontology-analogue` — decision: `partial-analogue-adoption`
- §14 `foundation.s5-scope-boundary-per-instance` — decision: `per-instance-vs-standardized-disclaimer`
- §23 `foundation.lrs-discovery-loop-extension` — decision: `discovery-routing-stage-adoption`
- §8 `schema.prereg-gate-fields` (dropped this pass on sim grounds, but its own founder question —
  `prereg-gate-hard-vs-soft` — was already open before this patch and stays open)

## Open items for the AI assistant / next synthesis pass

1. Apply §1–§23 and K-C1–K-C3 above to `FOUNDATION_v0.5.md`, bump `schema_version` per its own
   convention once the additive/breaking classification is confirmed (this patch's additions —
   `comparison`, `evidence_strength`, `verdict_class`, `gate_fail_taxonomy`, LRS manifest fields —
   are all additive/optional; no breaking change identified this pass).
2. Fold kernel rules 15–17 into FOUNDATION §3.3's numbered prose (flagged in the Rule numbering
   table above) before this patch's 18–28 widen the same gap.
3. Run the acceptance tests marked "not yet run this pass" (K4 taxonomy typed-hit requirement,
   §5's literal enum test, §6's out-of-lexicon holdout, §23's precision/recall comparison) before
   any of those nodes moves from `ready`/`pending-founder` to `done`.
4. An I2+ (cross-vendor or human) check of this entire patch has not run — every mapping above is
   Dr, single-pass, same-model (this session's own maker-checker-gate finding applies).
