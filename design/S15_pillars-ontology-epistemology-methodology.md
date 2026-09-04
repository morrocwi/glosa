# S15 — The Three Pillars of glosa: Ontology, Epistemology, Methodology

> **Tier: Dr.** Readout of one source, one pass, not yet independently checked (I0/I1 only —
> no cross-vendor or human check has run on this file). Every principle below is quoted with a
> line number from `sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt` (the 1139-line plain-text
> extraction of the founder's paper, "Written by AI. Still True.", v6, Aug 2026, preprint, not
> peer reviewed — the paper's own front matter, line 3). A quotation is this file's evidence for
> its own reading of the paper; it is not evidence that glosa's schema is correct or complete.
> Comparison language throughout is same/different/cited, never novel/first/prior-art (glosa
> gate rule 6). See also `docs/DEBATE_KIT.md` (the same material recast as a debate reference)
> and `lineage/RELATION_TO_WRITTEN_BY_AI.md` (the compact ledger this file expands).

**Source now published:** Zenodo DOI `10.5281/zenodo.22301202` (concept DOI
`10.5281/zenodo.22301201`), CC BY 4.0, deposited 2026-09-04 — see
`sources/citation_cards/CIT-written-by-ai-v6.yaml`.

Purpose (per HANDOFF §6 request 43): extract the paper's three pillars — a realist **ontology**
of pre-subjective constraint, a **role-separated epistemology** that blocks the
Possession–Constitution Collapse, and a **methodology of named channels and friction** — and, for
each principle, state what it means for glosa, which glosa field/gate already embodies it
(`PRESERVE_FUNCTION`) or must be added (`EXPAND`), and what it forbids.

---

## Pillar 1 — Ontology: pre-subjective constraint structure

### 1.1 Definition 1 and the realist minimum

> "A pre-subjective constraint structure is a worldly state, relation, trace, record, or lawful
> dependence capable of constraining which later representations succeed or fail, independently
> of whether any actual subject has yet represented or interpreted it." (lines 159–166)

> "Before anyone knew it, there was already something to get wrong. That sentence is the realist
> minimum of the paper." (lines 168–171)

**What it means for glosa.** A claim card, a source card, an observation card do not *create*
the world-state they report on. What they report on was already capable of making the report
right or wrong before the card existed. glosa's whole apparatus (tiers, independence classes,
falsifiers) exists to test a card's fit to something that does not wait for the card to be
written — never to manufacture that fit.

**PRESERVE_FUNCTION.** The claim card's `tested.falsifier` field (`FOUNDATION_v0.4.md` §3.2)
already requires "an observation/check outcome," not a definition or a restatement of the claim
— i.e. it already requires pointing at *something that could go the other way independently of
this card*. `scope.evidence_scope`/`scope.claim_scope` and the `Claim scope ≤ Evidence scope`
kernel rule (§3.3 rule 6) already assume evidence is a worldly constraint the claim answers to,
not a restatement the claim supplies for itself.

**Forbids.** Writing a claim card whose only "evidence" is the claim's own restatement, or
treating a `tier: Open` field as itself evidence that nothing can be known — Def. 1 says the
opposite: the world was already structured before the card; `Open` reports the card's current
epistemic position, not the world's.

### 1.2 RA = OA(W; ΠA) ≠ W ↔ retained distinction / readout-not-truth

> "Let a worldly condition be W, let an inquiry procedure or access operator be OA, and let RA be
> the record available to agent or system A under a selection policy ΠA: RA = OA(W; ΠA). ... It
> does not license the identification RA = W. Human observers do not escape this merely by having
> biographies." (lines 251–269)

**What it means for glosa.** This is, in the founder's paper's own vocabulary, exactly glosa's
readout-not-truth stance (CLAUDE.md gate rule 1; `EPIS-LENS`): a record is an operator-conditioned
readout of the world, never the world itself, and no amount of the operator being human changes
that. The paper's `RA = OA(W;ΠA)` formalizes the same distinction glosa's `lens_translation`
block encodes for the Readout Universe/Genesis lens (`access_relation_R`, `claim_function_Phi_z0`,
FOUNDATION §3.2). Same reading, cited independently — glosa does not claim the paper originated
readout-not-truth for glosa (that lineage runs through Readout Universe/Genesis, `lens_used`
block); it notes only that this paper's formalism lands on the same distinction (comparison =
same, per gate rule 6).

**PRESERVE_FUNCTION.** `five_questions.seen` (Q1, "what did we actually see") already separates
the record from the world by requiring `record_ref`, `access_model`, and
`retrievable_original: bool` rather than a bare assertion; `provenance_dag` types every node's
kind rather than collapsing them into one undifferentiated "source."

**Forbids.** Any field or prose that reads `record` and `world` as interchangeable — e.g.
treating a citation card's `metadata_verified: true` as if it verified the claim (the paper's own
`m(A) ≠ ρ(A)`, §1.4 below, and glosa's `NC-18` Source existence ≠ Claim support already forbid
exactly this).

---

## Pillar 2 — Epistemology: Role Separation and the Possession–Constitution Collapse

### 2.1 Principle 1 (Role Separation) and Table 1's ten roles

> "Generation, truth, evidential support, reliability, understanding, possession, endorsement,
> accountability, credibility, and institutional authorization are distinct epistemic roles. No
> pair may be identified merely because one human agent often occupies both." (lines 276–279)

Table 1 (lines 313–360) gives ten roles, each with a governing question and what it is *not*.
The crosswalk below maps every role to the glosa field, gate, or disclaimer that already carries
it, or names the gap.

| Role (Table 1) | Governing question | glosa mapping | Status |
|---|---|---|---|
| **Truth** | Is p the case? | **No field asserts this.** glosa has no `truth: bool` anywhere in the claim card schema (`FOUNDATION_v0.4.md` §3.2) — only `tier`, `k_state`, and `tested.evidence_relations`. `D-NO-VERTICAL-AUTHORITY` and gate rule 6 (never claim novelty/first) sit beside the same discipline: glosa never certifies truth, only reports a route and its tier. | `PRESERVE_FUNCTION` — the absence is itself the correct feature; no new field should ever be added named `truth` or `verified: true` outside a typed, scoped field like `metadata_verified`. |
| **Constraint** | What worldly difference can make a later representation fail? | `tested.falsifier` (must name an observation/check outcome, not a restatement) + `identification_ladder.per_rival` (a named rival's first identification level) + `provenance_dag.defeater_log` (node, date, outcome). | `PRESERVE_FUNCTION`. |
| **Evidence** | What bears on whether p should be accepted? | `tested.evidence_relations[]` — `{evidence_id, bearing, independence_class, strength, citation_ref}`. | `PRESERVE_FUNCTION`, but see Bridge Burden below — the paper's evidence role additionally requires a named *channel*, which the current field list does not carry explicitly. `EXPAND` (see §2.3). |
| **Reliability** | How well does a process discriminate success from error across cases? | Independence class `I0..I5` (§4.2) + `mc_level` + `tier` gates (§3.3 rules 2–4, 9) — reliability is read off the *route*, never off a label. | `PRESERVE_FUNCTION`. |
| **Provenance** | By what route did this representation arrive? | `provenance_dag`, `origin_blackbox_ref`, `lens_translation.lens_ref`, `ai_filled.*`. | `PRESERVE_FUNCTION`. |
| **Credibility** | How much epistemic weight is assigned to a source? | Citation card fields: `metadata_verified`, `evidence_tier`, `status` (`FOUNDATION` §7.8, `templates/knowledge/citation_card.yaml`). | `PRESERVE_FUNCTION`, with the same Bridge Burden gap as Evidence — see §2.3. |
| **Accountability** | Who can answer, correct, retract, or defend? | `responsible: human` (const, non-delegable, FOUNDATION §3.2), `human_owner`, MC-01 maker/checker/approver pairwise-distinct rule (§3.3 rule 5). | `PRESERVE_FUNCTION`. |
| **Legitimacy** | What social or institutional standing is granted? | `D-NO-VERTICAL-AUTHORITY` disclaimer (fires on any mention of peer review / venue / institutional accept-reject) + `k_state` (K1 = public-provisional, never institutionally granted; K2/K3 gated on `I5`, an independent *person*, never an institution's stamp, §4.2). | `PRESERVE_FUNCTION`. |
| **Authorship** | Who, if anyone, knows p? *(Table 1's "Authorship" row is actually glossed as "who is properly answerable for the scholarly act," line 349–350 — see note below)* | `CITATION.cff` (founder as sole formal author) + commit trailers for AI attribution; `produced_by: human\|ai\|joint` records *generation*, never authorship. | `PRESERVE_FUNCTION`. *Note:* Table 1 lists Authorship's governing question as answerability for the scholarly act (not "who knows p" — that is the separate **Possession** row, line 351). glosa keeps this separation: `CITATION.cff`/commit-trailer split is Authorship; the absence of any "knower" field (below) is Possession. |
| **Possession** | Who, if anyone, knows p? | **Not modelled.** glosa has no field that asks or answers who "knows" a claim — deliberately, per this pillar (§2.2 below). | `PRESERVE_FUNCTION` by omission — adding a "possession" field would itself commit the Possession–Constitution Collapse the paper diagnoses (a claim card does not need a knower to be a well-formed, gated record). |

### 2.2 Definition 2 (Possession–Constitution Collapse) and Definition 3 (knower fetishism) — glosa's own diagnosis, not a claim about others

> "The Possession–Constitution Collapse occurs when a condition on who can possess knowledge is
> treated as a condition on what can constitute, constrain, retain, transmit, or generate
> epistemically significant structure." (lines 247–249)

> "Knower fetishism is the treatment of the recognized identity, humanity, credentials, or social
> standing of a knower as though it possessed epistemic value in itself, after abstracting away
> the evidential and relational work through which that status earns epistemic relevance."
> (lines 540–544)

**What it means for glosa — stated as glosa's diagnosis, not a claim about any named tool, person,
or institution (readout-not-truth; no accusation without a verifiable, identified source).** The
paper names, in general philosophical terms, exactly the failure mode glosa's own schema was
built to make structurally hard to commit: crediting a claim card's route because a human name
sits on it, rather than because a named channel (evidence, independence, checks) does the work.
glosa states this as a **design reason internal to its own schema**, not as an accusation against
any specific person, institution, or tool (`feedback-no-negative-unverified-org-content` — no
identifiable target without a verifiable source).

**PRESERVE_FUNCTION.** The whole non-collapse table (Appendix A of `FOUNDATION_v0.4.md`;
`design/S9_non-collapse-table.md`) is glosa's operationalization of this exact diagnosis —
`NC-38` Credit≠EpistemicValue, `NC-58` AIContribution≠EpistemicResponsibility, and the new rows
in this pass (`NC-65`..`NC-73`, deliverable 2) extend it directly from this paper's vocabulary.

**Forbids.** Any glosa gate, template, or prose sentence that would raise a card's tier or
`k_state` because of *who* is named as `produced_by` or `human_owner`, rather than because of the
independence class actually reached (§3.3 rules 1–4, 9 already forbid this mechanically).

### 2.3 Bridge Burden (Principle 2) and No Bare Pedigree (Principle 3)

> "Any inference from source metadata to a change in epistemic standing must identify the
> mediating relation that does the work — for example reliability, independence, access,
> assurance, accountability, calibration, or error correlation. Where no such bridge is supplied,
> the inference is pedigree substitution rather than source-sensitive epistemology." (lines
> 302–306)

> "A source label is epistemically incomplete reporting. The relevant object is not merely who or
> what produced the claim, but the tuple of production procedure, selection conditions,
> dependencies, checks, error model, inferential role, and answerability that makes the source cue
> evidentially useful." (lines 390–396)

**What it means for glosa.** Every place glosa lets a source-metadata fact (`produced_by: ai`,
`ai_filled.used: true`, a citation's `evidence_tier`) move a card's standing must name *which*
channel is doing the work — never let the label alone move `tier`, `k_state`, or a reader's
credence.

**EXPAND — add a `channel` field.** Neither `tested.evidence_relations[]` (claim card, §3.2) nor
the citation card's credibility-bearing fields (`metadata_verified`, `evidence_tier`,
`verification_method`, `templates/knowledge/citation_card.yaml`) currently name *which* channel
(reliability / independence / access / assurance / accountability / calibration / error
correlation) a given entry is claimed to bear on. This is a genuine gap against Principle 2, not
yet present in FOUNDATION_v0.4 — patched in `design/FOUNDATION_v0.5_PATCH.md` §3 of this round:
`evidence_relation.channel: reliability | independence | access | assurance | accountability |
calibration | error_correlation | other(named)`, and a parallel `credibility_channel` note on the
citation card.

**No Bare Pedigree as the citation card's own tuple.** Principle 3's tuple already maps onto
existing `citation_card.yaml` fields, one-to-one, without a new field:

| Principle 3 tuple element | `citation_card.yaml` field |
|---|---|
| production procedure | `verification_method` |
| selection conditions | `identifier.kind` + `fetch_status` |
| dependencies | `related`/`superseded_by`, `xenon_ledger_ref` |
| checks | `metadata_verified` + `claim_match_verified` (two *distinct* booleans — the card's own binding invariant, line 8 of the template, already states `metadata_verified != claim_match_verified`, matching the paper's `m(A) ≠ ρ(A)`, see NC-66 in deliverable 2) |
| error model | `evidence_tier` |
| inferential role | `scope` (`DIRECT_QUOTATION \| PARAPHRASE \| SUPPORTS_GENERAL_CLAIM_ONLY \| CONTEXT_ONLY_NOT_EVIDENCE`) |
| answerability | `who_verified` / `claim_match_verified_by` |

**PRESERVE_FUNCTION.** This tuple was already fully present before this reading — it is stated
here as a named crosswalk, not a change, per `feedback-check-existing-machinery-before-new-schema`.

**Forbids.** Citing a source by identifier alone (`identifier.value` present, `status: CANDIDATE`)
as if that discharged the citation obligation — `status` may only reach `VERIFIED` when *both*
`metadata_verified` and `claim_match_verified` are true (template line 47–48), which is the
card's own machine-checkable form of "a source label is epistemically incomplete reporting."

### 2.4 Provenance Relevance Constraint (Principle 4) and Residual Provenance Effect (Definition 4) — the RPE reviewer check

> "Provenance may rationally alter epistemic standing insofar as it changes total evidence,
> reliability, dependence, assurance, accountability, or another specified epistemically relevant
> condition. Provenance has no additional freestanding force merely by redescribing the origin of
> an otherwise fixed epistemic route." (lines 600–603)

> "A Residual Provenance Effect occurs when epistemic assessment changes with provenance after the
> epistemically relevant pathways through which provenance could rationally matter have been held
> fixed or explicitly represented." (lines 567–569)

**What it means for glosa.** Every independent-check review (`review_report`, MIMCG gate, §7.1)
must ask, as a named step, whether the checker's verdict would change if `produced_by` were
swapped between `human`/`ai`/`joint` with every other field (evidence, independence class,
disclosed `ai_filled`) held fixed. If it would, the reviewer must **name the residual channel**
(the specific reliability/dependence/accountability relation actually doing the work) — or, if
none can be named, **drop the residual** rather than let it silently move the verdict.

**EXPAND — the RPE check, patched into the review report template.** Not currently a named step
in any existing FOUNDATION_v0.4 gate table. Patch text in
`design/FOUNDATION_v0.5_PATCH.md` §4: a required `rpe_check` block on `review_report` —
`{credence_before_channel_fix, credence_after_channel_fix, residual_named: string|null,
residual_dropped: bool}` — with the kernel rule that `residual_named` and `residual_dropped`
cannot both be empty/false when `credence_before_channel_fix ≠ credence_after_channel_fix`.

**Binding companion rule — `D-AIFILL` is never a blanket penalty.** The paper's own concession
(lines 505–506: "AI provenance can rationally lower confidence when it identifies a real failure
mode") is preserved: `D-AIFILL` (FOUNDATION §5) already fires "route-level, next to the specific
claim — never one blanket paragraph" (existing placement rule). This pass makes explicit what was
implicit: `D-AIFILL` discloses a route property, it is not itself a penalty, deduction, or tier
cap — any tier/independence effect must be justified by the specific `ai_filled.*` sub-field named
(e.g. `model_calibration_assumption`), never by the mere fact that `ai_filled.used: true`. Stated
as a **binding gate rule addition**, patch note §4.

### 2.5 Friction, not magic (Principle 5) and the Verification Paradox

> "Institutional certification has epistemic force insofar as institutions produce reliable
> epistemic friction: criticism, validation, replication, robustness testing, archival continuity,
> correction, and answerability. Certification does not create truth by status alone." (lines
> 688–691)

> "Institutions should be difficult places for claims to survive, not difficult places for claims
> to enter." (lines 725–726)

> "If certification adds criticism, replication, methodological checking, or accountability,
> there is no paradox... But if every epistemically relevant feature is already fixed and the
> remaining difference is only the stamp, then certification is recognizing permission rather than
> producing warrant." (lines 736–743)

**What it means for glosa — glosa's stance on K-states and horizontal authority.** glosa's whole
gate architecture (MIMCG L0–L5, independence ladder I0–I5, K0→K1→K2→K3) is a **friction
machine**: entry is cheap (any user may open a K0 `shape: stub` claim card with almost no
authoring cost, §3.2a), survival is expensive (advancing tier or K-state requires named,
independently-reachable checks, never a stamp). This is the same shape as "difficult to survive,
not difficult to enter," applied to a schema instead of an institution — cited as *same*, not
adopted from the paper (`EPIS-KNOWLEDGE-VALIDATION`: horizontal, no vertical certification;
`D-NO-VERTICAL-AUTHORITY` already forbids treating any institution's accept/reject as truth).

**PRESERVE_FUNCTION.** §3.3 rule 10 (`shape: stub` cards cannot advance past `Draft` or be cited)
+ §3.2a (stub authoring cost near zero) together *are* the entry-is-cheap half; §3.3 rules 1–4, 9
(independence-class floors for tier/K-state advancement) are the survival-is-expensive half.
`k_state`'s K2/K3 ceiling requiring `I5` (an independent, non-founder human, §4.2) rather than any
institutional stamp is glosa's answer to the Verification Paradox: the check that raises a
card is a named independent route, never a badge.

**Forbids.** Any future glosa field or gate that lets an institutional name, credential, or venue
acceptance *itself* raise `tier` or `k_state` without an accompanying independence-class route —
this would reopen exactly the "certification is recognizing permission rather than producing
warrant" failure the paper names.

### 2.6 Equal liability to epistemic testing, not equal credibility (Objection 11)

> "Remove automatic human credit and explicit epistemic standards become more important:
> evidence, calibration, track record, independence, reproducibility, error detection,
> answerability, and criticism. The proposal is not equal credibility. It is equal liability to
> epistemic testing." (lines 891–894)

**What it means for glosa.** Every claim card, regardless of `produced_by: human|ai|joint`, passes
through the *same* MIMCG gate table and the *same* independence-class floors (§3.3, §7.1) — that
is the "equal liability" half. The card's resulting `tier`/`independence_class`/`k_state` can
still differ card-by-card once the checks actually run — that is the "not equal credibility" half:
glosa never levels every card to the same tier, it levels every card to the same *test*.

**PRESERVE_FUNCTION.** No `produced_by`-conditional branch exists anywhere in the kernel rules
(§3.3) — a human-authored card and an AI-drafted card with identical evidence and identical
independence-class routes reach identical `tier`/`k_state` ceilings. This is already true by
omission; stating it here names the property so a future schema change cannot silently break it.

---

## Pillar 3 — Methodology: route dependence, accountability split, and unknown-unknowns

### 3.1 Objection 8 — two buttons ≠ two checks → Route Dependence Matrix

> "A claim can appear independently verified while the generator, verifier, retrieval system,
> benchmark, or dataset share a hidden common source. Two checks may therefore be one epistemic
> route wearing two interfaces... Independence is a property of the route, not the number of
> reviewers or buttons at its end." (lines 827–835)

**What it means for glosa.** Independence is never counted by interface count (two chat windows,
two model names shown to a user) — it is read off the actual dependency structure of the route
(shared training data, shared operator, shared prompt ancestry).

**PRESERVE_FUNCTION.** `independence_class` is the single string ladder `I0..I5` in every schema
(§4.2, chair ruling C1) specifically so that a route cannot inflate its class by adding more
low-independence checks (`NC-31` ManyModels⇏Independence, already in the table). The Route
Dependence Matrix (`templates/knowledge/route_dependence_matrix.yaml`, per `llms.txt`) and
`D-OPERATOR-SHARED`/`D-SAME-VENDOR` disclaimers (FOUNDATION §5) are glosa's mechanized form of
"independence is a route property" — recording `operator` per route so two same-operator routes
cannot silently count as two.

**Forbids.** Treating a second AI session, a second model call, or a second retrieval pass as an
independent check by default — `NC-31` and the I0/I1 ceiling on `tested:` entries already forbid
exactly this (§4.2 table: I0/I1 "cannot raise" tier or k_state past K0).

### 3.2 Objection 9 — accountability human, generation/verification may be AI

> "Accountability may remain human. Generation need not. Verification need not. Calculation need
> not. Retrieval need not. The point of role decomposition is precisely to preserve accountability
> without pretending that the accountable person personally performed every epistemically
> productive operation." (lines 848–851)

**What it means for glosa.** `responsible: human` is a constant field, non-delegable, independent
of `produced_by`. An AI may generate the draft, run the mechanical check (`I4`), or even supply an
`I2`/`I3` cross-model verification route — the human accountable party never changes because of
that.

**PRESERVE_FUNCTION.** `responsible: human` (const, FOUNDATION §3.2) already states this exactly;
`produced_by: human|ai|joint` is deliberately a *separate* field from `responsible`, precisely so
that generation and accountability can vary independently, matching the paper's own separation.

### 3.3 Objection 7 — unknown-unknowns are uncertainty, never evidence

> "The objection limits empirical identification; it does not license a source label to become a
> universal solvent... Ignorance is allowed to be uncertainty. It is not allowed to cosplay as
> evidence. An unfalsifiable pedigree penalty is not caution; it is immunity from correction."
> (lines 795–805)

**What it means for glosa.** A card may honestly carry unresolved uncertainty (`tier: Open`,
`identification_ladder` rival `unidentified`, `zero_vs_bottom: unresolved_bottom`) — but no field
may treat an *unnamed, unrepresented* possible failure mode as itself a piece of counter-evidence
against a route that has already named and passed its checks. Uncertainty is recorded as
uncertainty (an open field), never smuggled into `tested.evidence_relations[]` as a `bearing:
CHALLENGES` entry with no `evidence_id`.

**EXPAND.** Not previously a named rule: add to `design/FOUNDATION_v0.5_PATCH.md` a kernel-rule
note that `tested.evidence_relations[].bearing` may never be `CHALLENGES` with an empty
`evidence_id` — an unnamed defeater is not a defeater, it is an open item, and belongs in
`non_claims`/`identification_ladder`'s `unidentified` value, not in the evidence list disguised as
a challenge. New non-collapse row for this: `NC-72` (deliverable 2).

### 3.4 The disclosure challenge — glosa's AI-disclosure wording template

> "Disclosure challenge. Generative AI assisted with literature mapping, adversarial argument
> testing, language editing, and LaTeX drafting for this manuscript. The author selected, checked,
> revised, and endorses the final argument. If this disclosure lowers your assessment, do not
> merely report the discomfort. Identify the proposition, inference, evidential relation, or
> reliability condition that became worse when you learned it." (lines 43–46)

**What it means for glosa.** This is the exact rhetorical move `D-AIFILL` and the RPE check (§2.4
above) are built to enforce mechanically rather than leave as a rhetorical challenge to a reader.
glosa's AI-disclosure template, for any document's front matter (paper, README, claim card
`ai_filled.note`), adapts this wording directly, cited as *same move, glosa's own wording*:

> **glosa AI-disclosure template (Dr, for reuse in any glosa front matter):**
> "AI assisted with `<name the roles: drafting / literature search / mechanical checking /
> language editing / route comparison>` in this work. The human owner (`human_owner`) selected,
> checked, and endorses the final claim; `responsible: human`. If a specific `ai_filled.*` field
> above changes your assessment of this claim, name the reliability, independence, or evidential
> channel it affects (`design/FOUNDATION_v0.5_PATCH.md` §4, RPE check) rather than the fact of AI
> involvement alone — an unnamed channel is a residual, and this document requires residuals to
> be named or dropped, never left silent."

**Forbids.** Any glosa AI-disclosure sentence that stops at naming AI involvement without also
inviting (or in the reviewer case, requiring) the reader/checker to name the channel — a
disclosure that does not enable a channel-check is decoration, not disclosure, under Principle 2.

---

## Cross-reference

- Non-collapse rows added from this reading: `NC-65`..`NC-73`, `design/S9_non-collapse-table.md`.
- Ledger form of this file: `lineage/RELATION_TO_WRITTEN_BY_AI.md`.
- Debate form of this file (founder request, "ใช้เป็นข้อถกเถียงเมื่อต้องทะเลาะกับคนเรื่องญาณวิทยาและการ
  ทำงานร่วมกับ AI"): `docs/DEBATE_KIT.md` — maps the paper's fourteen objections plus glosa-specific
  attacks into attack → principle → reply → counter-question → glosa artifact.
- Patch text (§2.3 `channel` field, §2.4 RPE check, §3.4 disclosure template, `lens_used.display`
  extension): `design/FOUNDATION_v0.5_PATCH.md`.
- Citation record for the source paper: `sources/citation_cards/CIT-written-by-ai-v6.yaml`.
