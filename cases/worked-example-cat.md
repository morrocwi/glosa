tier: Dr (specified; independently unreviewed)

# Worked example: "ทำไมแมวเยี่ยวไม่เป็นที่" — the full round trip

> Canonical one-page demonstration of the spine's round-trip (`design/FOUNDATION_v0.5.md` §2.1,
> founder request 20), preserved human experience (§2.4, request 25/25b), the human-language
> question stored beside its formalizations (request 25b), and co-production visibility per step
> (request 24). Source: `the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518)` §6, request 26 — a
> founder-supplied worked example, reproduced and extended here exactly to that request's own
> content; nothing below is a real veterinary finding and nothing below is invented beyond what
> request 26 specified — where this document goes further than request 26's own text (e.g. filled
> template field values), it is marked `produced_by: ai` and stays at tier `Dr`/`Open` accordingly.

Every step below is tagged `produced_by: human | ai | joint` per §3.2's field of the same name —
visible per step, not only once at the document level (request 24).

---

## Step 0 — Blackbox Note (บันทึกกล่องดำ): raw human voice

`produced_by: human` (the line itself) / `produced_by: ai` (the template rendering below)

Per `templates/knowledge/blackbox_note.yaml`. This is the box being opened, not a polished
restatement of it.

```yaml
blackbox_note:
  id: BB-2026-09-04-01
  project: cat-urination-location
  session_ref: the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518) §6 request 26
  participants:
    - role: founder   # owner of the cat, not a veterinarian — standpoint declared at intake, §1 below
  language: th
  privacy_scan: done   # no other identifiable person named in the line
  public_lines_selected_by: founder
  lines:
    - n: 1
      ts: 2026-09-04T00:00:00+07:00   # exact time not given in the source request; date only is
                                        # confirmed (2026-09-04); time component is a placeholder,
                                        # not a verified fact — see "Honest edges" at the end
      speaker: founder
      kind: question
      text_verbatim: |
        ทำไมแมวเยี่ยวไม่เป็นที่
      distinction_introduced: >
        Names a repeated, observed behavior (urination outside a designated place) as the thing
        needing explanation — before any cause, diagnosis, or fix is proposed.
      became:
        - claim_card: GLOSA-CC-20260904-0001   # §3 below
        - rule: lens_translation.question_human field example, this document
      public: true
      ai_proposed: false
  cooking:
    - step: lens_in
      ts: 2026-09-04T00:05:00+07:00
      by: ai-assistant
      input_lines: [1]
      output_ref: "this document, Step 1"
      what_changed: >
        Translated the human question into a declared readout vocabulary (Q, X, R, Φ,
        formal_applicability) before any cause was proposed — Lens Law compliance.
    - step: analysis
      ts: 2026-09-04T00:10:00+07:00
      by: ai-assistant
      input_lines: [1]
      output_ref: "this document, Step 2"
      what_changed: >
        Identified four rivals sitting in one fiber under the household's current access, and
        typed each candidate augmentation needed to separate them.
    - step: lens_out
      ts: 2026-09-04T00:15:00+07:00
      by: joint
      input_lines: [1]
      output_ref: "this document, Step 3 / claim card hypothesis_world"
      what_changed: >
        Produced two to three candidate hypotheses in world language, each with a falsifier,
        instead of one confident diagnosis.
    - step: revision
      ts: 2026-09-04T00:20:00+07:00
      by: human
      input_lines: [1]
      output_ref: "hypothesis_selection.yaml, Step 6 below"
      what_changed: >
        Selected which hypothesis to carry forward and which to park — a human decision, never
        delegated to AI (`hypothesis_selection.yaml`'s `decided_by` field).
  r1_readout_ref: "this document, Step 1"
  r2_hypothesis_ref: "this document, Step 3"
  translation_status: reviewed   # the th->en rendering below is a rewrite of meaning, reviewed
                                   # against the verbatim line, never a word-for-word translation
  disclaimers: [D-BLACKBOX-NOTE, D-STANDPOINT, D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE]
```

**English rendering (rewritten, not translated):** "Why is the cat not urinating in [its
designated] place?" — the founder's own framing keeps "ไม่เป็นที่" (not-in-place) as the observed
category, not yet any of illness, dirty box, stress, or territorial marking.

---

## Step 1 — Lens-in: Q, X, R, Φ, formal_applicability

`produced_by: ai` (drafted the formalization) — `standpoint.declared_basis: owner, not veterinarian`
(`produced_by: human`, declared at intake, never inferred by AI, per Two-Question Intake / `skillme`
pattern re-derived here).

| Lens Law element | Value | Note |
|---|---|---|
| `question_human` | "ทำไมแมวเยี่ยวไม่เป็นที่" (verbatim, `blackbox_line_ref: BB-2026-09-04-01#1`) | The question as lived — kept, never only the formalized version (request 25b) |
| `question_readout` (R1) | "Under the access currently available (owner's direct observation of location only, no medical/behavioral instrumentation), what distinguishes 'in-box' events from 'out-of-box' events, and what does 'ไม่เป็นที่' as a category currently fail to separate?" | The Lens Law's own contrast-question — declared *before* touching any candidate cause |
| `local_contrast_space_X` | `{in_box, out_of_box}` as currently observed; explicitly **not yet** separated into `{illness, dirty_box, stress, marking}` | This is the fiber-collapse the analysis in Step 2 names directly |
| `restriction_provenance` | `owner's direct observation only — no urinalysis, no vet exam, no household-change log yet performed` | Named so the restriction is visible, not silently assumed |
| `access_relation_R` | Owner's unaided, unscheduled observation of location + rough recall of frequency; not a structured observation log at this stage | |
| `claim_function_Phi_z0` | "the mechanism causing out-of-box urination" — currently unresolved (`z0` not yet identified) | |
| `formal_applicability` | `not_applicable_narrative` | Per §3.2b's plain-language definitions: no exact/relational/stochastic functional form is being fit here; this is a practice/observational problem, not a formal or statistical one at this stage |

**Contaminated-concept flag:** "ไม่เป็นที่" ("not in [the right] place") is itself a **human decision
policy**, not a description of the cat's state — it presupposes a boundary (the box, or wherever
"the place" is) that the household defined, not something the cat itself distinguishes on its own
terms. This is logged as `five_questions.assumed[]` item `A1` (below), type
`decision_policy_augmentation` — the identification ladder (Step 2) treats it as an augmentation
the household added, not part of the access source itself.

---

## Step 2 — Analysis: four rivals in one fiber, augmentation types, identification ladder

`produced_by: ai` (drafted) / `produced_by: human` (owns the falsifier judgment, per §3.2's
`tested.falsifier` and the co-production split, request 24)

**Four rivals currently indistinguishable under the household's current access** (they all produce
the *same* observed readout — "out-of-box urination" — so `local_contrast_space_X` as currently
defined cannot separate them; this is the fiber the question sits in):

1. **Illness** (e.g. a urinary tract condition) — medical rival.
2. **Dirty/aversive box condition** (litter type, cleanliness, box placement, number of boxes) —
   environmental rival.
3. **Household stress/change** (new pet, person, furniture, schedule change) — behavioral rival.
4. **Territorial/communicative marking** (distinct from elimination) — behavioral rival, distinct
   mechanism from #3.

**Each rival needs a different access augmentation to be separated from the others** — this is
where the identification ladder does its work (`identification_ladder.layers`, §3.2):

| Rival | Augmentation needed | `assumed[].type` | `identification_level` |
|---|---|---|---|
| Illness | **New access**: urinalysis / veterinary exam — this is not obtainable from the owner's own observation at all | `access_augmentation` | Unidentified from current access; requires a genuinely new observation instrument (a human handoff, below) |
| Dirty/aversive box | **Fiber-separating intervention**: change one box variable (litter, cleanliness, placement, count) and observe whether the out-of-box rate changes | `access_augmentation` | A1 — identifiable from the owner's own household, no external instrument needed |
| Household stress/change | **Record**: a dated log of household changes cross-referenced against the existing frequency recall | `contrast_relevance_operation` | A1 — identifiable from existing household knowledge, needs structuring not new access |
| Territorial marking | **Observation**: posture and target-surface pattern (horizontal vs vertical surface, volume) during an actual event, not recalled after the fact | `access_augmentation` | A2 — requires catching an event in progress, one level harder than a static record |

**`five_questions.assumed[]` (full list, this claim):**
```
- id: A1
  type: decision_policy_augmentation
  description: "'ไม่เป็นที่' presupposes a household-defined boundary (the box/designated place);
                the cat's own readout does not distinguish 'in the household's chosen spot' from
                'elsewhere' on its own terms."
  identification_level: A1
  contaminated_concept_hit: true
- id: A2
  type: inferential_commitment
  description: "AI's initial framing toward 'probably cystitis' is a prior drawn from the model's
                training distribution over similar-sounding presentations, not from any observation
                of this specific cat — an inferential commitment the AI supplied, not the owner."
  identification_level: unidentified
  contaminated_concept_hit: false
```

`A2` above is the **AI-filled inferential commitment named directly by request 26** ("AI's
'probably cystitis' = inferential commitment from model prior → `ai_filled`"): it must appear in
`five_questions.ai_filled.model_calibration_assumption`, disclosed, never presented as an
observation of this cat.

**Medical rival → human handoff (mandatory, non-negotiable):** rival #1 (illness) cannot be
confirmed or ruled out by any AI reasoning over the reported observations — it requires an access
instrument (urinalysis, physical exam) that only a veterinarian can perform. This is logged as a
hard boundary, not a soft suggestion: no candidate hypothesis below may resolve `Φ` toward "not
illness" without this handoff having occurred. `D-NOT-DIAGNOSTIC` is emitted (Step 5) precisely
because this is health/clinical content.

---

## Step 3 — Lens-out: hypothesis_world (R2), 2–3 candidates with falsifiers

`produced_by: joint` — AI drafted the candidate hypotheses and their falsifier shape; the human
(founder, as the standpoint-declared owner) is the one who judges whether each falsifier is
actually reachable and meaningful, per `tested.falsifier`'s ownership rule (§2.2 stage S3 table).

| # | `hypothesis_world.text` (R2, world language) | Falsifier (`tested.falsifier`) | Routed rival(s) |
|---|---|---|---|
| H1 | "Out-of-box urination is driven by an aversive box condition (litter/cleanliness/placement/count), not by illness or household stress." | "If changing one box variable at a time over a defined observation window (proposed: 14 days) does not reduce the out-of-box rate, this hypothesis is false." | #2 |
| H2 | "Out-of-box urination is a territorial/marking behavior, distinct from elimination need." | "If observed events consistently show elimination posture and volume on a horizontal surface (not the marking posture/pattern on a vertical surface), this hypothesis is false." | #4 |
| H0 (medical, routed to human expert, not carried forward as a glosa hypothesis) | "Out-of-box urination has an underlying medical cause." | Falsifier requires a veterinary urinalysis/exam result — **outside glosa's own evidence-gathering scope**; H0 is not falsified or supported by anything in this document, it is handed off. | #1 |

H3 (household stress/change, rival #3) is **not** promoted to a standalone hypothesis at this pass
— per the honest-edges discipline, it is named in Step 2's rival list and left as an open
alternative the LRS dialogue table (Step 4) and the 14-day observation window (H1) may or may not
surface, rather than force-fit into a third parallel hypothesis with no distinct falsifier design
yet proposed.

---

## Step 4 — LRS stub (Literature Review System), per hypothesis

`produced_by: ai` (drafted stub) — this is a **stub**, not a run LRS, since request 26 supplies a
worked example, not an actual literature search; every field below states the honest stub state
rather than inventing search results.

Per `templates/knowledge/search_log.yaml` + `templates/knowledge/litreview_manifest.yaml`
(`design/S14_literature-review-system.md`):

```yaml
search_log:
  id: search-cat-urination-h1-001
  claim_or_hypothesis_ref: hypothesis-H1-cat-urination
  review_mode: TARGETED_SEARCH        # honestly labeled — NOT systematic_review (FC-S8-1)
  frozen_scope:
    hypothesis_or_falsifier: "H1 — see Step 3 above"
    question_type: mechanism
    concepts_synonyms_vocabulary: ["periuria", "inappropriate elimination", "litter box aversion"]
    global_sources: []      # NOT run in this worked example
    local_context_sources: []
  queries:
    support: []
    challenge: []
  sources_found: []          # none fetched — this is a stub, not a completed search
  summary_disclaimer: >
    This is a search_log STUB for demonstration purposes only. No search was actually executed;
    no citation_card exists yet for this hypothesis. TARGETED_SEARCH is the honest label chosen in
    advance for the mode this would run under, per skillme's fallback-label discipline — it is not
    a claim that a search occurred.

litreview_manifest:
  id: litrev-cat-urination-h1-001
  hypothesis_ref: hypothesis-H1-cat-urination
  search_log_ref: search-cat-urination-h1-001
  status: DRAFTING            # never FROZEN — no real search ran
  citations: []                # NOT_FETCHED / no sources — honestly empty, not omitted
  gate:
    accuracy_gate: PENDING
    diversity_gate: PENDING
    overall: PENDING
    blocked_reason: "No LRS run has actually been performed for this worked example; this stub
                      demonstrates the required SHAPE of the manifest, not a passed gate."
  human_owner: founder
```

**Manifest gate is honestly `FAIL`/`PENDING`, not `PASS`** — per S14's own hard rule, no lit-review
section may be drafted or published for a hypothesis until its manifest reaches at least
`PASS_WITH_LIMITS`. This worked example therefore cannot legally proceed to a published paper on H1
or H2 as written; it stops at the case-study/practice-report genre (Step 6) precisely because no
literature review has actually been run.

---

## Step 5 — Hypothesis selection (human decision)

`produced_by: human` (the selection itself, non-delegable) — per `templates/knowledge/
hypothesis_selection.yaml`.

```yaml
hypothesis_selection:
  id: hsel-cat-urination-001
  problem_ref: problem-cat-urination-not-in-place
  decided_by: "founder (cat owner)"
  decided_at: "2026-09-04"
  candidates:
    - hypothesis_ref: hypothesis-H1-cat-urination
      hypothesis_world: "Out-of-box urination is driven by an aversive box condition..."
      lrs_manifest_ref: litrev-cat-urination-h1-001
      criteria:
        developability:
          note: "Directly testable at home with a 14-day intervention window; no external access needed."
        access_evidence_available: { can_we_get_new_access: "yes", note: "owner can change box variables directly" }
        falsifier_reachable_with_our_resources: { value: "yes" }
        independence_routes_available: { max_reachable_independence_class: "I0" }
        risk_and_ethics: { human_participant_or_vulnerable_subject: "no", domain_safety_flags: [] }
        genre_fit: { candidate_genres: ["empirical_qual_practice", "case_study"] }
      accuracy_gate_at_selection_time: PENDING
      diversity_gate_at_selection_time: PENDING
    - hypothesis_ref: hypothesis-H2-cat-urination
      hypothesis_world: "Out-of-box urination is a territorial/marking behavior..."
      criteria:
        developability:
          note: "Requires catching an event in progress (posture/surface observation); harder to schedule than H1."
        access_evidence_available: { can_we_get_new_access: "partial" }
        falsifier_reachable_with_our_resources: { value: "partial" }
        independence_routes_available: { max_reachable_independence_class: "I0" }
        genre_fit: { candidate_genres: ["empirical_qual_practice", "case_study"] }
      accuracy_gate_at_selection_time: PENDING
      diversity_gate_at_selection_time: PENDING
  selection:
    chosen: [hypothesis-H1-cat-urination]
    reason: >
      H1's falsifier is reachable immediately with resources the owner already has (change one box
      variable, observe 14 days); H2 requires catching an event live, which is harder to schedule
      and lower-confidence to observe correctly on the first pass. H1 is tried first; H2 stays
      parked, not discarded.
    parked:
      - hypothesis_ref: hypothesis-H2-cat-urination
        reason: "Lower near-term developability (harder observation event); revisit if H1's
                  14-day window does not reduce the out-of-box rate."
  cooking_log_ref: "BB-2026-09-04-01#cooking[3] (the 'revision' step)"
  routes_to: "genre router, Step 6 below"
```

H0 (medical) is never a candidate in this selection at all — it was routed to a human expert
(veterinarian) in Step 2 and does not compete with H1/H2 as a glosa-carried hypothesis.

---

## Step 6 — Genre route

`produced_by: ai` (ran the routing procedure) — per `design/FOUNDATION_v0.5.md` §6.3b's ordered
question list, against H1's claim card:

1. Formal/mechanical proof intended? No (`formal_applicability: not_applicable_narrative` was set
   at lens-in, and no proof is intended). → continue.
2. Documented systematic/targeted/scoping search backing this? The `search_log` exists but is a
   **stub** (`status: DRAFTING`, no sources fetched) — not a completed backing search for a
   `systematic_review` genre routing. → continue (routing procedure reads presence of a *linked*
   search_log; a stub with zero fetched sources does not license `systematic_review`).
3. Archival record? No — this is a live household observation, not a retrievable archival document.
   → continue.
4. Targets/responds to another named claim? No. → continue.
5. Built artifact as the contribution? No — this reports on an existing situation (the cat's
   behavior), not a designed tool/protocol. → continue.
6. `scope.generalization_claimed == population_claim` with a frozen prereg design? No —
   `scope.generalization_claimed: none` (this is about one specific cat/household). → continue.
7. `scope.generalization_claimed ∈ {none, pattern_candidate}` with
   `standpoint.declared_basis` naming direct practice/lived observation? **Yes.** Does the claim
   name a bounded, individually-identifiable case with its own timeline (a specific
   person/household/organization/event)? **Yes — this specific cat and household, with a proposed
   14-day timeline.** → **`case_study`**.

**Route result:** `genre: case_study`, `venue_track: none` (this is K0 practice work, not headed to
any venue at this stage — the `none` value added specifically so K0 work is not forced into a
publication-track choice, §6.1), `companion_of: null`.

*(Note: request 26's own text suggested `empirical_qual_practice`; running the actual §6.3b
procedure against this claim's own fields — a bounded, individually-identifiable case with a named
timeline — lands on `case_study` instead, per branch 7's own sub-question. Both genres share the
same disclaimer floor and neither reaches IMRAD, §6.2 rows 3/4; the difference is recorded honestly
here rather than silently forcing the routing procedure's output to match the earlier informal
framing — an instance of the routing procedure existing specifically so genre choice is
computable, not asserted.)*

**Genre `case_study` (§6.2 row 4) requirements this claim inherits:**
- Structure: Case selection/boundary → Data sources → Timeline → Mechanism → Explicit
  non-generalization.
- Claim ceiling: `Dr` interpretive; underlying cards may be `finite_diagnostic` (e.g. a directly
  counted out-of-box frequency, if logged).
- Mandatory disclaimer: `D-NO-NEGATIVE-UNVERIFIED-PERSON` (always-on for this genre — not triggered
  by content here, since no person is named negatively, but the genre requires it be checked).
- Blackbox Note appendix: **required** (hard gate, §2.4/§6.4) — this document *is* that appendix in
  miniature.
- Preserved-experience field: "Positionality" section — the founder's own standpoint as the
  observing owner, not a veterinarian, stated once and carried through.

---

## Step 7 — Stub card and full card

`produced_by: ai` (drafted both shapes) / `standpoint`, `tested.falsifier`, `human_owner`:
`produced_by: human`.

### Stub shape (legal for this K0 case at this stage, per §3.2a)

```yaml
claim_card:
  schema_version: "0.4.0"
  claim_id: GLOSA-CC-20260904-0001
  shape: stub
  statement:
    language: th
    text: "แมวเยี่ยวนอกกระบะทรายเพราะสภาพกระบะ/ทราย (สมมติฐาน ยังไม่ยืนยัน)"
    is_verbatim_quote: false
    translation:
      text: "The cat urinates outside the litter box because of the box/litter condition (hypothesis, unconfirmed)."
      language: en
      translation_status: reviewed
  standpoint:
    declared_basis: "owner, direct household observation; not a veterinarian"
    disciplines_not_claimed: ["veterinary medicine", "animal behaviorism"]
    method_basis: "direct observation + planned box-variable intervention"
  claim_type: EMPIRICAL
  produced_by: joint
  responsible: human
  origin_blackbox_ref: BB-2026-09-04-01
  five_questions:
    tested:
      falsifier: "If a 14-day single-variable box-condition change does not reduce the out-of-box
                   urination rate, H1 is false."
      evidence_relations: []
      dissent_records: []
    ai_filled:
      used: true
      note: "AI proposed the box-condition and marking-behavior hypotheses and their falsifier
             shapes, and flagged the AI's own initial 'probably cystitis' framing as an unverified
             model prior, not an observation. Owner supplied the actual observations, the household
             context, and the selection decision (H1 over H2, H0 handed off to a vet)."
  non_claims:
    - "Does not claim illness has been ruled out (medical rival requires a veterinary exam, not
       performed as part of this claim)."
    - "Does not claim this generalizes to any other cat or household."
  human_owner: "founder"
  tier: Dr
  status: Draft
```

*(`claim_type`, `responsible`, `five_questions` — the top-level schema wrapper with `tested`+
`ai_filled` nested inside it, not `tested`/`ai_filled` as siblings of `standpoint` — and
`human_owner`/`status` are all schema-required even at `shape: stub` (§3.2a). The prior version of
this block was missing all five, which made `cli/glosa claim validate` on the extracted block
return `FAIL`. This shape now matches the output of `cli/glosa claim new --shape stub`'s own
scaffold, adapted with this worked example's narrative content, and has been re-validated against
`schema/claim_card.schema.json` with `jsonschema.Draft7Validator` — `ok: true, verdict: PASS`, no
errors — the same check `cli/glosa claim validate` runs.)*

### Full shape (fields the stub leaves null/absent, filled here for demonstration only — this
claim would remain a `stub` in practice until it is foregrounded in a published document; the full
shape below exists to show every field the round-trip actually touched)

```yaml
claim_card:
  schema_version: "0.4.0"
  claim_id: GLOSA-CC-20260904-0001
  shape: full
  statement: { language: th, text: "แมวเยี่ยวนอกกระบะทรายเพราะสภาพกระบะ/ทราย (สมมติฐาน ยังไม่ยืนยัน)",
               is_verbatim_quote: false,
               translation: { text: "The cat urinates outside the litter box because of the box/litter condition (hypothesis, unconfirmed).",
                              language: en, translation_status: reviewed } }
  standpoint: { declared_basis: "owner, direct household observation; not a veterinarian",
                disciplines_not_claimed: ["veterinary medicine", "animal behaviorism"],
                method_basis: "direct observation + planned box-variable intervention" }
  claim_type: EMPIRICAL
  genre: case_study
  venue_track: none
  companion_of: null
  produced_by: joint
  responsible: human
  origin_blackbox_ref: BB-2026-09-04-01
  lens_translation:
    question_human: { text_verbatim: "ทำไมแมวเยี่ยวไม่เป็นที่", language: th,
                       blackbox_line_ref: "BB-2026-09-04-01#1" }
    question_readout: "Under the access currently available (owner's direct observation of
                        location only), what distinguishes 'in-box' from 'out-of-box' events, and
                        what does 'ไม่เป็นที่' currently fail to separate?"
    local_contrast_space_X: ["in_box", "out_of_box"]
    restriction_provenance: "owner's direct observation only — no urinalysis, no vet exam, no
                              structured household-change log yet performed"
    access_relation_R: "owner's unaided, unscheduled observation of location + rough frequency recall"
    claim_function_Phi_z0: "the mechanism causing out-of-box urination — unresolved (z0 not yet identified)"
    formal_applicability: not_applicable_narrative
  hypothesis_world: { text: "Out-of-box urination is driven by an aversive box condition
                             (litter/cleanliness/placement/count), not by illness or household stress.",
                       language: en, falsifier_ref: "five_questions.tested.falsifier" }
  five_questions:
    seen: { record_ref: "owner's recall, not a structured log", as_of: "2026-09-04",
            retrievable_original: false, access_model: "direct_observation_unstructured",
            citation_refs: [] }
    separates: { value_z0: "unresolved", licensing_test: { regime: "none run", result: "n/a",
                 notes: "no fiber-separating intervention run yet" },
                 zero_vs_bottom: unresolved_bottom }
    ai_filled: { current_evidence: "none identified beyond the owner's own recall",
                 retrieved_tool_evidence: "none identified",
                 retained_record_route: "none identified — no structured log exists yet",
                 model_calibration_assumption: "AI's initial framing toward a specific medical
                   cause (e.g. cystitis) is a prior from training-distribution pattern-matching on
                   similar-sounding presentations, not an observation of this cat — disclosed here
                   as A2 in the identification ladder above, never treated as evidence",
                 prompt_system_constraint: "none identified",
                 decision_policy: "the household's own definition of 'the place' (A1, contaminated
                   concept) is a decision policy, not part of the cat's own observable state" }
    assumed:
      - { id: "A1", type: decision_policy_augmentation,
          description: "'ไม่เป็นที่' presupposes a household-defined boundary.",
          identification_level: "A1", contaminated_concept_hit: true }
      - { id: "A2", type: inferential_commitment,
          description: "AI's initial 'probably cystitis' framing is a model prior, not an observation.",
          identification_level: unidentified, contaminated_concept_hit: false }
    tested:
      evidence_relations: []   # none run yet — the 14-day intervention has not occurred
      falsifier: "If a 14-day single-variable box-condition change does not reduce the out-of-box
                   urination rate, H1 is false."
      dissent_records: []
  identification_ladder:
    layers:
      - { id: "L0", adds: "raw location readout (in-box / out-of-box)" }
      - { id: "L1", adds: "household-defined boundary ('the place')" }
      - { id: "L2", adds: "candidate rival mechanisms (illness / box condition / stress / marking)" }
    per_rival:
      - { rival: "illness", first_identification_level: "requires new access (vet exam) — not
                                                            reachable at any layer above without it" }
      - { rival: "dirty/aversive box", first_identification_level: "L2 (A1 augmentation)" }
      - { rival: "household stress/change", first_identification_level: "L2 (A1 augmentation)" }
      - { rival: "territorial marking", first_identification_level: "L2 (A2 augmentation, requires
                                                                        catching an event live)" }
  provenance_dag: { nodes: [], edges: [], essential_dependency_set: [], defeater_log: [], status: not_run }
  silent_lift_check: { represented_dependency_set: [], actual_dependency_set: [], flags: [], status: not_run }
  scope: { generalization_claimed: none, evidence_scope: "one cat, one household",
           claim_scope: "one cat, one household" }
  tier: Dr
  k_state: K0
  ledger: { forced: [], borrowed: [], open: ["illness rival — requires veterinary access to resolve"] }
  non_claims:
    - "Does not claim illness has been ruled out."
    - "Does not claim this generalizes to any other cat or household."
    - "Does not claim the 14-day window is long enough to be conclusive either way — it is the
       owner's own chosen falsifier design, not a validated protocol."
  legal_epistemic_separation: { applicable: false, notes: "no license/permit/certification involved" }
  independent_check: { status: NONE, maker_id: null, checker_id: null, approver_id: null,
                        independence_class: I0, mc_level: L0, date: "2026-09-04", expires_at: null }
  disclaimers_emitted:
    - { id: "D-STANDPOINT" }
    - { id: "D-NONEXPERT" }
    - { id: "D-SCOPE", params: { n: 1 } }
    - { id: "D-NONCLAIM" }
    - { id: "D-AIFILL" }
    - { id: "D-TIER" }
    - { id: "D-NOT-DIAGNOSTIC" }
    - { id: "D-BLACKBOX-NOTE" }
    - { id: "D-INDEPENDENCE", params: { level: "I0" } }
  status: Draft
  lineage: { derives_from: [], supersedes: [], superseded_by: null }
  related_source_cards: []
  related_observation_cards: []
  related_citation_cards: []
  human_owner: "founder"
  revision_history:
    - { rev: "1", date: "2026-09-04", by: "joint", note: "initial round-trip demonstration" }
```

---

## Step 8 — Disclaimers emitted (rollup)

`produced_by: ai` (computed against §5's trigger conditions)

| id | Why it fires here |
|---|---|
| `D-STANDPOINT` | Always on |
| `D-NONEXPERT` | Owner explicitly not a veterinarian/behaviorist (`disciplines_not_claimed`) |
| `D-SCOPE(n=1)` | One cat, one household — exactly the worked-example wording HANDOFF §6 request 26 itself names |
| `D-NONCLAIM` | `non_claims` populated |
| `D-AIFILL` | `ai_filled.model_calibration_assumption` non-empty (the "probably cystitis" prior) |
| `D-TIER` | Every factual statement here is `Dr`, stated inline |
| `D-NOT-DIAGNOSTIC` | Health/clinical content (the medical rival) is present, even though it is routed out rather than resolved |
| `D-BLACKBOX-NOTE` | Mandatory on every research document (request 28/32) — this document's own appendix requirement is Step 0 itself |
| `D-INDEPENDENCE(level=I0)` | `tested.evidence_relations` is empty; the strongest thing on file is a same-session self-read — I0, no standing (§4.2 table) |

---

## Step 9 — Independence ceiling under three routes

`produced_by: ai` (computed against §4.2's ladder) — this section directly answers the worked
example's own closing requirement.

| Route | Independence class reached | `k_state` ceiling this licenses | What is still missing |
|---|---|---|---|
| **(a) the AI assistant only** | I0 (same session re-reading its own output) or, at best, I1 if a fresh the AI assistant session re-reads this document later | K0 only — "cannot raise `tier`/`k_state` at all" beyond the default `Dr`/K0 already assigned | Any independent check whatsoever; per §4.2's own table, I0 "is not a `tested:` entry at all" |
| **(b) + Gemini** (a materially different vendor added as a second route, e.g. reviewing this document's own reasoning) | I3 — different vendor | K1 **floor** only, and only combined with a founder Approver sign-off at the release-authority level (§7.1 L3 row) — **never K2**, and I3 alone is a *minimum*, never sufficient by itself (chair ruling B4) | Still no I5 human check; still no actual 14-day observation run (the falsifier has not been tested against reality by anyone, human or AI); `D-DVP-NOT-K2` would fire if this were ever described as "verified" |
| **(c) + external human** (a person outside this session's authorship, e.g. a veterinarian consulted on the medical rival, or an independent reader of the case write-up) | I5 — the only route to K2 (and, with formal/empirical constraint, K3) | K2 becomes reachable **once the I5 route has substantively engaged with the claim** (not merely been shown it) — e.g. a veterinarian's exam result resolving the illness rival is exactly the kind of I5, mechanical/original-record-backed (I4-adjacent) check this claim currently lacks entirely | Even with (c), K2 applies only to whatever specific sub-claim the human actually checked (e.g. "illness ruled out by exam") — it does not automatically raise H1's own box-condition claim, which still needs its own 14-day observation run before `tested.evidence_relations` has anything in it at all |

**Plain statement of the ceiling right now, before any of (a)/(b)/(c) beyond what is on paper
today:** this entire worked example sits at `tier: Dr`, `k_state: K0`, `independence_class: I0` —
a drafted hypothesis set with a named falsifier, not yet tested by anyone, human or AI. That is the
honest, current state of the round trip, and it is exactly what the case-study genre's own claim
ceiling (`Dr` interpretive) and this document's disclaimers already say.

---

## Honest edges (what is not settled in this worked example)

- The exact clock time of Blackbox Note line 1 is not given in `HANDOFF_2026-09-04_ultracode-
  foundation-meeting.md` §6 request 26 — only the date (2026-09-04) is confirmed there; the
  `ts` field above is marked as a placeholder in its own YAML comment rather than presented as a
  verified fact.
- The genre-router result (`case_study`) differs from HANDOFF §6 request 26's own informal
  framing (`empirical_qual_practice`) — this document runs the actual §6.3b procedure and reports
  the result honestly rather than silently matching the earlier prose, per the note in Step 6.
- No search has actually been run for the LRS stub (Step 4); no citation exists yet for either
  hypothesis; no 14-day observation has actually taken place. Every table above that looks like a
  result is a **planned design**, not a completed check — the whole document sits at K0/I0 per
  Step 9, and no field anywhere in this file should be read as claiming otherwise.
