# FOUNDATION v0.7 patch note — session architecture, Human Mastery Gate wiring, dialogue-log fields, LRS defeater discipline

> **Tier: Dr, specified not applied.** This file states the exact text/field/rule diffs to apply
> to `FOUNDATION_v0.6.md` to produce v0.7. It does not itself edit `FOUNDATION_v0.6.md`, any
> `schema/*.json` file, or `kernel/glosa_kernel.py` — per this task's ownership scope (design/,
> methodology/, CHANGELOG, plugin pointer files, `llms.txt` only; schema and kernel edits are other
> workers' files in this pass). Readout, not truth; no novel/first/prior-art language; comparisons
> stay same/different/cited; no vendor name is credited anywhere in this file. K-state is
> unchanged at this pass: **K0** (no independent check has run on this patch itself, `NC-34`).
> Founder ruling BBL-2026-09-05-119 governs every judgment below: never lower a claim to make it
> pass — raise the work until it actually supports the claim as stated.
>
> Inputs read for this patch: `design/SESSION_ARCH_v0.4_SPEC.md` (both parts, in full),
> `design/SESSION_ARCH_v0.4_rejudged.json`, `design/FOUNDATION_v0.6.md` §2, §2.1a–§2.3, §3.2,
> §3.3, §5, §7.4, §7.5, §7.9, Appendix A, `design/FOUNDATION_v0.6_PATCH.md` (format precedent),
> `methodology/P17_human_mastery_gate.md`, `methodology/P18_session_architecture.md`,
> `methodology/P01_standpoint.md` (this pass's own edit), `kernel/glosa_kernel.py` (rule ceiling
> check only, not edited). Format follows `FOUNDATION_v0.6_PATCH.md`'s precedent: one section per
> node, target section · exact text · schema fields (specified, not applied) · kernel rule (with
> error/warning strings) · acceptance test · citations · status.
>
> Founder ruling BBL-2026-09-05-121 (no finding is ever dropped) applies to this patch's own
> structure: every one of the 24 proposals `design/SESSION_ARCH_v0.4_SPEC.md` scores (13
> `build_now`, 7 `with_revision`, 4 `still_open`) gets a section or an explicit carry-forward line
> below — none is silently omitted, per that ruling.

---

## 0. What this patch covers, and what it does not

- **13 `build_now` proposals** get a full section (§1–§10 below): four Part-1 session-architecture
  proposals (§1–§3), one blackbox-dialogue proposal (§4, with its claim-wording fix already
  applied), three human-uplift proposals (§5–§7), and five LRS-defeater proposals (§8–§10, two of
  which are new `kernel/glosa_kernel.py` python rules, kept in a distinct numbering namespace from
  this section's own §3.3 flag-rule sequence — see §9's namespace note).
- **7 `with_revision` proposals** get a short section stating the exact fix and the target text,
  **not yet applied** — §11.
- **4 `still_open` proposals** get a short section stating the raise-path (never a softened claim)
  — §12.
- **NC-77** (§13) and two new disclaimer-catalogue rows (§14) are specified here; **not yet added**
  to `methodology/data/non_collapse_table.json` or `methodology/data/disclaimer_catalogue.json` —
  those data files are outside this task's ownership list in this pass.
- **7 founder decisions** (`design/SESSION_ARCH_v0.4_SPEC.md` §7, plus the Part-2 additions in §1b
  item 7) are carried forward as pending-founder blocks — §15. None is defaulted silently; each
  states the spec's own recommended default where one exists, marked `pending founder`.
- **Rule numbering table** — §16 — states the full ledger: `kernel/glosa_kernel.py` python rules
  continue at **29, 30** (this pass); `FOUNDATION_v0.6.md` §3.3's own prose flag-rule sequence
  (currently ending at rule 28) separately gains a **flag-rule 29** proposal from
  `kernel.candidate-set-delta-cooking-step` (§11.3) — a different artifact, a different sequence,
  the same number, stated so a reader never conflates the two (per spec §1b item 6).

---

## 1. `session.boundary-blackbox-note` (SA-1) — session boundary + AI-reset fact

- **status:** ready to apply (spec §3: citations_verified, control_mechanical, invariant_ok, score 8)
- **FOUNDATION target:** §2.3 (new bullet under the Blackbox Note register description — **not**
  R0/R1/R2, which name the note's own internal reading stages, per spec §2.2's confirmed-by-direct-
  read correction).
- **Schema fields (specified, not applied):** `schema/blackbox_note.schema.json` top-level
  additions — `session_id` (string), `opened_at` (timestamp), `closed_at` (timestamp, nullable
  while open), `ai_state_at_boundary` (const `"reset"`), `human_retained_residue_ref` (nullable ref
  or literal `"none"`).
- **Kernel rule (unnumbered pending founder ratification of §2.2, per spec §4):** a Blackbox Note
  pair sharing one `session_id`, split by an actual tool/process restart, must both carry
  `ai_state_at_boundary: reset` (literal) — `ERROR: ai_state_at_boundary missing or not literal
  'reset' across shared session_id`. Must fire: shared `session_id`, second file's field missing or
  non-literal. Must not fire: different `session_id` values on topically-similar notes.
- **Acceptance test:** two Blackbox Note files sharing `session_id`, split by a real process
  restart, both carry `ai_state_at_boundary: literal 'reset'`.
- **Citations:** `sources/notes/EPISTEMIC_FUSION_v7.1.txt:489, :490, :493, :496, :497, :328`.
- **Status:** `founder_decision_needed: true` — merge target for `kernel.session-boundary-momentum-
  reset-assertion` (§12.4 below), per spec §7 decision 2.

## 2. `schema.entry-resistance-precommit-field` — Problem Card resistance-route pre-commitment

- **status:** ready to apply (score 6)
- **FOUNDATION target:** §3.2's Problem Card field list — `intake.entry_anchor.resistance_route`
  (merges with HU-2's fuller `entry_anchor` block, §6 below), corrected from an earlier draft that
  pointed at §2.1a (which explicitly disclaims reopening S1–S6 ownership, `FOUNDATION_v0.6.md:354`).
- **Schema fields (specified, not applied):** `schema/problem_card.schema.json` `intake` object
  gains `entry_anchor.resistance_route` (string, naming a concrete route: source, record,
  experiment, critic, or authority).
- **Disclaimer added:** `D-NO-PRECOMMIT-ROUTE` (flag, non-mandatory — §14.2 below).
- **Kernel rule:** `FLAG: precommitted_resistance_route missing at READY_FOR_S2`. Must fire:
  `intake.entry_anchor.resistance_route` absent, `readiness.verdict=READY_FOR_S2`. Must not fire:
  field names a concrete route before the first AI-turn line in the linked Blackbox Note.
- **Citations:** `sources/notes/EPISTEMIC_FUSION_v7.1.txt:351, :356`, `FOUNDATION_v0.6.md:354,
  :425`, `design/DAG_v0.3.yaml:112`.
- **Status:** `founder_decision_needed: true`.

## 3. `schema.retention-direction-field` — hypothesis_selection retained-direction field

- **status:** ready to apply (score 8)
- **FOUNDATION target:** §3.2's `hypothesis_selection.yaml` field list (new field
  `retained_direction`); §5 disclaimer catalogue (new row `D-RETENTION-DIRECTION`, §14.1 below);
  Appendix A Family J (new row `NC-77`, §13 below). Corrected from an earlier draft's nonexistent
  "K1→K2 conversion ledger" target to the real `hypothesis_selection.yaml`.
- **Schema fields (specified, not applied):** `schema/hypothesis_selection.schema.json` new field
  `retained_direction`, enum `unknown | expansion | tunnel`, default `unknown`.
- **Kernel rule:** `WARN: retained_direction=unknown — no linked independent-check artifact for a
  row chosen across ≥2 sessions`. Must fire: `chosen` row spanning ≥2 sessions, no
  `evidence_relation`→review_report/falsifier link → forced `unknown`. Must not fire: a row whose
  `evidence_relation` resolves to an existing checker/falsifier verdict.
- **Acceptance test:** 100% of `chosen` rows spanning ≥2 sessions with no linked independent-check
  artifact tagged `retained_direction: unknown`; scoped to single-session rows until `session_id`
  lands (§1 above; spec §7 founder decision 7).
- **Blocked on:** §1 (`session.boundary-blackbox-note`) for `session_id` propagation into
  `hypothesis_selection.yaml`.
- **Citations:** `sources/notes/EPISTEMIC_FUSION_v8.1.txt:345, :347, :356, :361`,
  `FOUNDATION_v0.6.md:2259, :429`.
- **Status:** `founder_decision_needed: true`.

## 4. `schema.blackbox-question-trace` — per-turn question-evolution trace

- **status:** ready to apply, claim wording corrected (spec §9.1, score 6)
- **Claim correction applied in this patch:** the original motivating sentence cited "glosa's own
  Human Return Test," which does not exist anywhere in glosa's design docs (grep confirms zero
  hits outside `sources/`) — it is a construct from `sources/notes/EPISTEMIC_FUSION_v7.1.txt:467`
  glosa has not adopted. The corrected, fully-cited motivating gap: `question_human`/
  `question_readout` are single-shot per Claim Card (`FOUNDATION_v0.6.md:495`) with no field for
  how the question changed turn-to-turn.
- **FOUNDATION target:** §2.3 (Blackbox Note register description) — new optional top-level
  `question_trace[]`, distinct from `P18_session_architecture.md`'s Session-object `question_trace[]`
  row (which is Problem-Card-scoped, sourced from SA-3) — both are real, non-duplicate gaps at
  different granularities, per spec §9.4.
- **Schema fields (specified, not applied):** `schema/blackbox_note.schema.json` top-level
  optional `question_trace[]`, items `{n, ts, question_text, derived_from_line, note}`.
- **Acceptance test:** coverage-check extension to `tools/blackbox_log.py` — every `lines[].kind
  == question` line has a `question_trace` entry (or explicit `derived_from_line: null`).
- **Citations:** `sources/notes/EPISTEMIC_FUSION_v7.1.txt:124, :129, :467`,
  `FOUNDATION_v0.6.md:495`.
- **Status:** `founder_decision_needed: false`.

## 5. `hu.mastery-gate-wired` (HU-1) — Human Mastery Gate wired to publish-gate R8

- **status:** ready to apply (score 8) — narrated in full by `methodology/P17_human_mastery_gate.md`.
- **FOUNDATION target:** §7.5, replace `"Unchanged from v0.1 §7.5"` (line 1621) — that pointer is
  broken, no `FOUNDATION_v0.1.md` exists anywhere in the repo (confirmed by direct read) — with a
  pointer to `methodology/P17_human_mastery_gate.md` and a statement of R8; §7.4/`methodology/
  P10_publish_gate.md`'s R1–R7 dimension list gains a new **R8**.
- **Schema fields (specified, not applied):** new `schema/human_mastery_gate.schema.json` —
  required `gate_status` enum `PASS | PASS_WITH_NAMED_GAPS | NOT_READY` plus the ten answer fields
  from `templates/paper/arxiv-twocol/main.tex:375-378` (and its onecol twin), each human-authored,
  never `ai_filled`.
- **Kernel rule (R8):** `BLOCKED: NO_MASTERY_GATE_LINKED`. Must fire: a non-Paper-genre L3+ claim
  card with no `human_mastery_gate.yaml` linked, currently passing R1–R7 clean (`grep -rn mastery
  schema/*.json` returns zero hits today, confirmed). Must not fire: an S5 Paper-genre artifact
  using the arXiv template with `Gate status:` already filled `PASS`.
- **Acceptance test:** Paper-genre artifact with `Gate status: PASS` → R8 passes; non-Paper L3+
  artifact with no linked gate → R8 `BLOCKED: NO_MASTERY_GATE_LINKED`.
- **Citations:** `FOUNDATION_v0.6.md:1619, :1621`, `templates/paper/arxiv-twocol/main.tex:375,
  :378`, `methodology/data/non_collapse_table.json:570, :620`, `methodology/P10_publish_gate.md:17,
  :32`.
- **Status:** `founder_decision_needed: true`.

## 6. `schema.entry-anchor-full-h0` (HU-2) — full entry-anchor H0 block

- **status:** ready to apply (score 8) — narrated by `methodology/P18_session_architecture.md`'s
  Session-object table.
- **FOUNDATION target:** §3.2's Problem Card field list — merges with §2 above (`schema.entry-
  resistance-precommit-field` supplied only the `R*` conjunct; HU-2 supplies the remaining four).
- **Schema fields (specified, not applied):** `schema/problem_card.schema.json` `intake` object
  new sub-object `entry_anchor: {unresolved (U_0), existing_evidence (E_0), change_condition (Φ_0),
  verification_intent (V_0), resistance_route (R*)}` — all optional, human-authored,
  `blackbox_line_ref`-backed like `q1_issue`/`q2_user_proposal`; never silently AI-backfilled.
  `C_0` (candidate contract) is deliberately **not** a schema field — `v7.1:355` defines it as the
  human's standing disposition that AI output begins as `K_like`, documentation-only
  (`methodology/P02_intake.md`), not a per-intake record.
- **Kernel rule:** no hard fail. Must fire (scan, not gate): an intake with a stated prior model
  (`q2_user_proposal` present) but no `entry_anchor.change_condition` — nothing today distinguishes
  a fixed belief from an open one at the schema level. Must not fire:
  `entry_anchor.change_condition: "none stated — exploratory"` (explicit honest-optional).
- **Acceptance test:** schema validation passes with `entry_anchor` present; scan of N
  `problem_card.yaml` instances reports the fraction of each sub-field filled vs. honest
  not-stated, never AI-backfilled.
- **Citations:** `sources/notes/EPISTEMIC_FUSION_v7.1.txt:344, :351, :355, :356`,
  `schema/problem_card.schema.json:12`.
- **Status:** `founder_decision_needed: true` — retroactive vs. forward-only, same call as §15.4.

## 7. `methodology.p01-bounded-completeness-prompt` (HU-5) — P01 completeness-prompt bound

- **status:** applied this pass — `methodology/P01_standpoint.md`'s "Human / AI division of
  labour" section now carries the enumerated, bounded five-item prompt list in place of the
  open-ended `(e.g. ...)` example.
- **FOUNDATION target:** none — no schema change required, per the spec's own note: `ai_filled.*`'s
  existing disclosure shape (`FOUNDATION_v0.6.md:721, :878`) already covers the `prompt_source:
  freeform` disclosure this bound relies on.
- **Kernel rule:** none (no schema field), documentation-level bound only. Failing control (manual/
  future-lint, not a hard schema gate): an AI-authored `lens_in`-stage prompt not drawn from
  `P01_standpoint.md`'s bounded list, without `ai_filled.prompt_source: freeform` logged.
- **Citations:** `methodology/P01_standpoint.md:34, :35, :36`, `methodology/data/
  non_collapse_table.json:586, :590` (`NC-58`).
- **Status:** `founder_decision_needed: false`. Extends `NC-58` (AIContribution≠
  EpistemicResponsibility) by the same logic already applied to AI-*filled answers*, to AI-*posed
  prompts* — the one channel that discipline did not yet cover.

## 8. `lrs.dialogue-table-defeater-class-column` — `defeater_class` / `legitimate_defeater` columns

- **status:** ready to apply (score 8)
- **FOUNDATION target:** §7.9 (LRS) — `design/S14_literature-review-system.md` §3.4 column list
  (lines 208–216); `templates/knowledge/dialogue_table.md` table header.
- **Schema/template fields (specified, not applied):** two new columns — `defeater_class` (enum
  `phenomenological | constitutive | structural_formal | diagnostic | empirical`, per
  `EPISTEMIC_FUSION_v8.1.txt:30-72`'s five-way claim-type separation) and `legitimate_defeater`
  (free text). **Not named `claim_type`** — that name is already a schema-fixed enum on
  `claim_card.yaml` routing `kernel/glosa_kernel.py:643` (rule16w); reusing it here would collide
  with a different, already-wired field. `defeater_class` is deliberately non-colliding.
- **Kernel rule (lint, not hard gate):** `INCOMPLETE: dialogue_table row has a stance (agrees/
  disagrees = YES) but no defeater_class/legitimate_defeater`. Must fire: a row with a populated
  stance but blank new columns. Must not fire: both columns filled from the fixed five-way enum,
  non-empty defeater text.
- **Acceptance test:** header-anchored grep confirms both new columns; pytest row-completeness
  fixture fails a populated-stance row missing either column.
- **Applies forward-only** (new `dialogue_table.md` instances), not retrofitted.
- **Citations:** `EPISTEMIC_FUSION_v8.1.txt:30, :44`, `S14_literature-review-system.md:210`,
  `kernel/glosa_kernel.py:643`.
- **Status:** `founder_decision_needed: false`.

## 9. `lrs.defeater-log-required-outcome-enum` — `defeater_log` required + `outcome` enum

- **status:** ready to apply (score 8)
- **FOUNDATION target:** §3.2 `provenance_dag.defeater_log` field description (currently
  documented in prose at `FOUNDATION_v0.6.md:775` as `[{node, date, outcome}]` but the schema item
  itself, `schema/claim_card.schema.json:437-441`, is untyped — `{"type":"array","items":
  {"type":"object"}}`, no `required` keys).
- **Schema fields (specified, not applied):** add `required: [node, date, outcome]` and `outcome:
  {enum: [claim_survived, claim_revised, claim_withdrawn]}` to the `defeater_log` item schema.
- **Kernel rule:** standard `jsonschema.ValidationError` (missing required key / enum mismatch) —
  no custom kernel message needed, pure declarative schema constraint.
- **Acceptance test:** `[{"node": "n1"}]` (missing `date`/`outcome`, currently passes silently) →
  `jsonschema.validate()` raises. `[{"node": "n1", "date": "2026-09-05", "outcome":
  "claim_survived"}]` → passes.
- **Tier:** `Dr` now → `finite_diagnostic` once `tests/test_schema_defeater_log.py` (new) exists and
  passes.
- **Citations:** `FOUNDATION_v0.6.md:775`, `schema/claim_card.schema.json:437, :439`.
- **Status:** `founder_decision_needed: false`.

## 10. Kernel rule29 / rule30 — `kernel/glosa_kernel.py` python-rule namespace (`lrs.defeater-not-collapse-rule`, `lrs.claim-type-defeater-enum`)

**Namespace note (spec §10, §1b item 6):** these are `kernel/glosa_kernel.py` python-function
rules, continuing that sequence past its shipped ceiling of `rule28` (confirmed by direct read — no
`rule29`/`rule30` exist yet). This is a **different sequence** from `FOUNDATION_v0.6.md` §3.3's own
prose flag-rule sequence (rules 1–28), which `kernel.candidate-set-delta-cooking-step` (§11.3
below) separately proposes to extend to "flag-rule 29" — a same-numbered but non-colliding sibling
in a different artifact. Both are written out in full below and everywhere either is referenced
(`kernel.glosa_kernel.rule29` vs. `FOUNDATION_v0.6.md §3.3 flag-rule29`) so a reader never conflates
the two. See §16's rule numbering table.

### 10a. `rule29` — "strength of the claim" is not a defeater

- **status:** ready to apply (score 6)
- **Target:** `kernel/glosa_kernel.py` (new `rule29`); `methodology/data/
  non_defeater_phrase_table.json` (new, sibling shape to `methodology/data/
  contaminated_concept_table.json`).
- **Rule statement:** a `tested.falsifier` field matching strength-of-claim / feels-solid phrasing
  is never itself a legitimate defeater, regardless of `claim_type` — grounded in
  `EPISTEMIC_FUSION_v8.1.txt:51, :53`'s Burden rule ("'The claim is strong' is not a
  counterexample, an inconsistency, a failed phenomenon, or contrary evidence"), applied here **by
  reasoned analogy** to a forward-looking preventive guard, not as a direct textual derivation
  (spec §9.3's framing fix — the source text defends an architecture claim against "it's strong,"
  not a new kernel guard against "no instance found yet").
- **Error string:** `ERROR: rule29 — tested.falsifier reads as a strength-of-claim assertion, not a
  legitimate defeater (matched pattern: "<match>")`.
- **Failing control:** must fire on `/strength of (the |this )?claim|feels solid|feels right|
  intuitively (strong|solid|convincing)/i` inside `tested.falsifier`. Must not fire on a falsifier
  stating an actual contrary-evidence or absence condition, e.g. "defeated by a documented case
  where retained_direction is negative across 3 consecutive turns."
- **Tier:** `Dr` (specified this pass) → `finite_diagnostic` once `tests/
  test_rule29_non_defeater_phrase.py` ships; disclosed as evadable-by-omission like rule27/rule28,
  never claimed as a structural guarantee.
- **Citations:** `EPISTEMIC_FUSION_v8.1.txt:51, :53`.
- **Status:** `founder_decision_needed: false`.

### 10b. `rule30` — `defeater_class`-appropriate falsifier phrasing

- **status:** ready to apply (score 8)
- **Target:** `schema/claim_card.schema.json` `five_questions.tested` (new optional
  `defeater_class` field, same five-way enum as §8, added as a **sibling** of `claim_type`, not an
  extension — `schema/common.defs.json:154-165`'s existing `claim_type` enum (EMPIRICAL/FORMAL/
  INTERPRETIVE/NORMATIVE/CONVENTIONAL_LEGAL/DECISION/SOCIAL/HUMAN_PARTICIPANT) already drives
  rule16w and would collide on the bare string `EMPIRICAL`); `kernel/glosa_kernel.py` (new
  `rule30`).
- **Rule statement:** `defeater_class`'s value must be paired with a `falsifier` phrasing style
  matching that class per `EPISTEMIC_FUSION_v8.1.txt` §1 — e.g. `empirical` requires a
  contrary-evidence/replication-style falsifier (`v8.1:45`), not an absence/misdescription/
  irrelevance-style falsifier (`v8.1:53-54`, the `phenomenological` pairing).
- **Error string:** `ERROR: rule30 — defeater_class=<class> but tested.falsifier matches the
  <other-class> phrasing style, not <class>'s`.
- **Failing control:** must fire — `defeater_class: EMPIRICAL` with a phenomenological absence-
  style falsifier (wrong pairing). Must not fire — `defeater_class: EMPIRICAL` with a
  replication-style falsifier (correct pairing), nor `defeater_class: PHENOMENOLOGICAL` paired with
  the absence-style text.
- **Tier:** `Dr` (citation corrected, mechanism redesigned this pass; not yet built) →
  `finite_diagnostic` once `tests/test_rule30_defeater_class.py` ships. Open dependency, disclosed
  not resolved: the five v8.1 classes eventually needing their own glosa claim cards is a separate
  prerequisite/parallel deliverable, not pre-cited here.
- **Citations:** `schema/common.defs.json:154`, `schema/claim_card.schema.json:94`,
  `EPISTEMIC_FUSION_v8.1.txt:44, :45, :53, :54`.
- **Status:** `founder_decision_needed: true`.

---

## 11. `with_revision` proposals — exact fix stated, not yet applied

Per BBL-2026-09-05-119: none of the following has its claim lowered to pass — each carries the
exact fix required before it may build.

### 11.1 `SA-4` — `chi_recip`/`m^H`/`m^AI` decline, logged
Fix 3 off-by-1/2 line citations (`v7.1:550→548`, `:552→550`, `:494→495`) and drop the irrelevant
4th citation (`FOUNDATION_v0.6.md:1670`, unrelated boilerplate) before logging. Target:
`cpg/research/coordination/DECISIONS.yaml` (`status: RECORDED`, not the fabricated
`DECLINED-FOR-NOW` value, not in that ledger's status enum), mirrored in `glosa/DECISIONS.md`.
Founder decision needed (§15.5).

### 11.2 `SA-3` — pre-exposure anchor fields
Fix citation `EPISTEMIC_FUSION_v7.1.txt:354 → :353`. `build_path` must add the Problem-Card-vs-
Blackbox-Note timestamp cross-check script its own `acceptance_test` requires, or narrow the
`acceptance_test` to the schema-required-fields half only. Target: `schema/problem_card.schema.json`
(three new required fields: `problem_stated_before_first_ai_response`, `prior_model_or_guess`,
`verification_intent`). Founder decision needed — retroactivity, §15.4.

### 11.3 `kernel.candidate-set-delta-cooking-step` — `candidate_set` on `cooking.items`
Two fixable build-path defects: (1) retarget the named acceptance-test fixture
(`blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md` has zero schema-shaped `cooking[]` entries) to
`schema/examples/blackbox_note.example.json` or a real `projects/GLS-2026-001_*/blackbox_note.yaml`
instance; (2) `tools/blackbox_log.py` is the wrong build target (the founder's daily voice-entry
Blackbox LOG tool, BBL-YYYY-MM-DD-NNN, unrelated to the Blackbox Note's `cooking[]` schema) — this
needs new checker tooling. Field addition (`candidate_set: {before, after, forgotten}` on
`cooking.items`) and the flag (`CANDIDATE-DROP-UNEXPLAINED`) are sound. Target additionally names
**`FOUNDATION_v0.6.md §3.3 flag-rule29`** — its own namespace, distinct from §10's
`kernel.glosa_kernel.py rule29` above (§16). Founder decision needed: `false` per the proposal's own
field.

### 11.4 `schema.blackbox-line-origin-enum` — `lines[].origin` enum
`failing_control` invokes "the claim_card's own creation timestamp" — `claim_card.schema.json` has
no required/reliable creation-timestamp field (only optional `revision_history[].date`). Fix:
replace the cross-file timestamp comparison with the same-document `cooking[]`/`became[]` ordering
check the proposal's own two fixtures already use (a `step: review`/`revision` cooking entry naming
the line, occurring before its `became[]` entry, resolves `ai_proposed_adopted`; absent that,
`ai_proposed_forgotten`). Target: `schema/blackbox_note.schema.json` `lines[].origin` enum
(`human_authored, ai_proposed_pending, ai_proposed_adopted, ai_proposed_forgotten`), replacing
`lines[].ai_proposed: boolean`; deprecated alias kept one migration cycle. Founder decision needed:
`true` (changes founder-visible disclosure semantics).

### 11.5 `schema.blackbox-chooser-reaffirmation` — `became[].chooser_reaffirmed`
The `hsel-` id-pattern branch is mechanically build-ready. The second trigger ("a claim_card whose
`responsible` field is `human`") needs a cross-file validator this proposal never designs, and its
own Fixture C only exercises the non-trigger case. Fix: either (a) scope to `hsel-` ids only and
ship now, or (b) specify the cross-file validator and add a real Fixture D exercising the
`responsible: human` branch first. Target: `schema/blackbox_note.schema.json`
`lines[].became[].chooser_reaffirmed: {by, ts} | null`. Founder decision needed: `true`.

### 11.6 `HU-4` — advisor `problem_ref` trace
All four citations are synthesized aggregations, not continuous verbatim at the stated line —
mechanism and defeater are otherwise sound. Corrected citations: `schema/claim_card.schema.json`
`required[]` starts at line 9 (not line 1, which is `{`); `schema/hypothesis_selection.schema.json`
`problem_ref` at line 11, `required[]` at line 7 (not line 1); `templates/knowledge/
advisor_prompt_packet.md`'s "Every `claim_card.json` listed..." line at line 31 (not 27);
`schema/problem_card.schema.json`'s `"retained_difference_statement"` at line 22 (not 17). Target:
`schema/claim_card.schema.json` (new optional `problem_ref`); `templates/knowledge/
advisor_prompt_packet.md` §1 (new step 1a, `BLOCKED: NO_PROBLEM_REF`). Founder decision needed:
`false`.

### 11.7 `process.run-existing-open-falsifier-klike` — H3 falsifier sim
Fix citation `design/DAG_v0.3.yaml:76 → :78`. Disclose in the row itself that
`design/TODO_v0.3.md` has no matching `[Open]` line today (confirmed by direct read — the DAG
node's own `acceptance_test` was never actually satisfied in-repo). Target:
`methodology/H3_falsifier_sim.py` (new); a `DECISIONS.yaml` row recording the result. Founder
decision needed: `false` per the proposal's own field, but §15.6 names the founder go-ahead this
still requires.

---

## 12. `still_open` proposals — raise-path only, no softened claim

### 12.1 `SA-2` — hypothesis_selection session-grouping key
Fix citation `FOUNDATION_v0.6.md:2254 → :2256`. Blocked on §1 (`session.boundary-blackbox-note`)
landing session_id before its acceptance test can run on real multi-session data — currently only
trivially true for single-session rows. Raise-path: land §1, then re-run. Founder decision needed
(§15.7).

### 12.2 `HU-3` — session-close retention-direction note on Blackbox Note `cooking[]`
Three real defects: (1) the citation `hypothesis_selection.schema.json:1` is fabricated — line 1
is `{`; the real `required[]` array is at line 7 (`["id","problem_ref","decided_by","candidates",
"selection","cooking_log_ref"]`), omitting `decided_at`/`routes_to` (lines 13/89, not contiguous);
(2) `legitimate_defeater` cites `EPISTEMIC_FUSION_v8.1.txt:362-365`, about a different collapse
(AUG/SYN/RET interchangeability), not Repair 8's expansion-vs-tunnel sign — re-cite from
`v8.1:359-361`, matching `NC-77` (§13); (3) `failing_control` needs the `session_id` grouping key
`hypothesis_selection.schema.json` does not yet have — restate `build_path` as explicitly blocked
on §1 landing, not runnable today. Kept at full claim strength — no free-text expansion/tunnel
classification without a linked independent check, same NC-77 discipline as §3/§13, applied to the
Blackbox Note's own `cooking[]` log rather than `hypothesis_selection.yaml` directly.

### 12.3 `schema.blackbox-language-bridge-subfield` — withdrawn, not revised
The proposal's own stated defeat condition already fires and was missed:
`design/MEETING_2026-09-05_judged.json:84-92` already adjudicated this identical proposal (same
id, title, target) `keep:false`, score 4.5. Per the proposal's own defeater clause this is
**withdrawn**, not revised — the raise-path is not a schema fix, it is: the existing chair ruling
was missed by this pass's defeater search (which checked only `FOUNDATION_v0.6.md`,
`FOUNDATION_v0.6_PATCH.md`, and the schema file, never `MEETING_2026-09-05_judged.json`). Only a
founder overrule of the standing ruling could revive it (§15's Part-2 addition, spec §1b item 7).

### 12.4 `kernel.session-boundary-momentum-reset-assertion` — duplicate of SA-1
Duplicate framing of §1, pointed at the wrong FOUNDATION section (§2.3's R0/R1/R2, which govern the
Blackbox Note's own internal reading stages, not session momentum). Raise-path: merge into §1, not
build separately — building both would create two homes for `ai_state_at_boundary` (one-fact-
one-home violation). Founder decision needed (§15.2).

---

## 13. Appendix A, Family J — new row `NC-77`

**Target:** `Appendix A — The Non-Collapse Table`, `Family J — Cross-tradition parallels` (currently
`NC-74`..`NC-76`). New row, specified here, **not yet added** to
`methodology/data/non_collapse_table.json` (outside this task's ownership list):

> `NC-77` **Retention≠Direction** — persistence or retention of a claim, habit, or chosen
> hypothesis across ≥2 sessions is never by itself evidence it is expansion rather than tunnel;
> only a linked independent-check artifact may set the sign. Default: `retained_direction:
> unknown`. *Source:* `EPISTEMIC_FUSION_v8.1.txt:358-361` (Repair 8). *Enforced by:*
> `schema/hypothesis_selection.schema.json` `retained_direction` field (§3 above),
> `D-RETENTION-DIRECTION` (§14.1). Full narration: `methodology/P18_session_architecture.md`.

**Reservation note (spec §7 decision 3):** the id `NC-77` is independently verified free (next
unused Family J id, confirmed by direct read of the table as it stands at `NC-76`), but reserving
it in `cpg/research/coordination/DECISIONS.yaml` is a founder-owned ledger write before any
concurrent Family J proposal can claim it — not an AI-owned act. Pending founder, §15.3.

---

## 14. New disclaimer-catalogue rows (specified, not yet applied to `methodology/data/disclaimer_catalogue.json`)

### 14.1 `D-RETENTION-DIRECTION`
States `NC-77` in disclaimer-catalogue form for any document emitting a `retained_direction`
value. `trigger_condition`: a `hypothesis_selection.yaml` row's `retained_direction` field is
non-default (`expansion` or `tunnel`) without a resolvable `evidence_relation`. Placement: adjacent
to the first display of `retained_direction` in any rendered document. Mandatory: `true` when the
trigger condition holds.

### 14.2 `D-NO-PRECOMMIT-ROUTE`
Flags — never blocks — a Problem Card reaching `READY_FOR_S2` with
`intake.entry_anchor.resistance_route` null or absent. `trigger_condition`:
`intake.entry_anchor.resistance_route` absent, `readiness.verdict = READY_FOR_S2`. Placement:
Problem Card readiness summary. Mandatory: `false` (flag, not a hard gate — per §2's kernel rule).

---

## 15. Founder decisions carried forward (pending; recommended default stated where the spec names one)

1. **Ratify §2.2's (`P18_session_architecture.md`'s) one-fact-one-home decision** — Session object
   stays a logical join across four existing artifacts; no new `session.yaml`. Blocks whether §1
   and §12.4 can be merged into one build.
2. **Merge duplicate proposals** — confirm §1 (`SA-1`) canonical, §12.4
   (`kernel.session-boundary-momentum-reset-assertion`) retired without a separate build.
3. **Reserve `NC-77`** in `cpg/research/coordination/DECISIONS.yaml` before any concurrent Family J
   proposal can claim the id (§13).
4. **`SA-3`/HU-2 retroactivity** — whether the new required/optional Problem Card fields apply to
   already-published Problem Cards, or forward-only. **Spec's recommended default:
   forward-only** (per meeting §5.3) — the founder's call, not an AI default.
5. **`SA-4` ledger row** — ratify logging the `chi_recip`/`m^H`/`m^AI` decline as
   `status: RECORDED` in `DECISIONS.yaml` (not the fabricated `DECLINED-FOR-NOW` value).
6. **Approve building the H3 sim now** (§11.7) — the first genuinely empirical (n=0, untested)
   falsifier run under this framework since the fabricated-C-id incident.
7. **`hypothesis_selection.yaml` session-grouping key** — approve wiring `session_id` (from §1,
   once built) into `hypothesis_selection.yaml` per `SA-2`'s own `build_path`; without it `SA-2`'s
   acceptance test stays scoped to trivially-true single-session rows only — per BBL-2026-09-05-119
   not an acceptable stopping point, only an honest interim state.

**Part-2 additions (spec §1b item 7):**

8. **Confirm the rule29/30 namespace split** (§16 below) — `kernel/glosa_kernel.py rule29`/`rule30`
   vs. `FOUNDATION_v0.6.md §3.3 flag-rule29` are distinct, non-colliding sequences; state this
   explicitly wherever either is cited, per spec §1b item 6, rather than letting a reader assume
   one shared sequence.
9. **`chooser_reaffirmed` scope** — approve scoping the requirement to `hsel-` ids only (§11.5
   option a), or approve building the cross-file `responsible: human` validator (§11.5 option b)
   before that half ships.
10. **`schema.blackbox-language-bridge-subfield` withdrawal** — confirm withdrawal per the
    standing `MEETING_2026-09-05_judged.json:84-92` ruling (§12.3), or explicitly overrule it.

---

## 16. Rule numbering table (full ledger this pass)

| sequence | artifact | ceiling before this pass | new this pass | source |
|---|---|---|---|---|
| python kernel rules | `kernel/glosa_kernel.py` | 28 (confirmed by direct read, no `rule29`/`rule30` exist) | **29** (strength-of-claim not a defeater, §10a), **30** (defeater_class phrasing match, §10b) | `lrs.defeater-not-collapse-rule`, `lrs.claim-type-defeater-enum` |
| FOUNDATION §3.3 prose flag-rules | `design/FOUNDATION_v0.6.md` §3.3 | 28 (rules 1–28, prose/disclaimer-style) | proposed **flag-rule 29** (`candidate_set` on `cooking.items`, §11.3) — `with_revision`, not yet applied | `kernel.candidate-set-delta-cooking-step` |
| Non-collapse table | Appendix A | `NC-76` (Family J) | **`NC-77`** (§13) — specified, not yet in `non_collapse_table.json` | `schema.retention-direction-field`, `SA-2` |

These two rule-29 numbers are **same-numbered, non-colliding siblings in different artifacts** —
`kernel.glosa_kernel.rule29` is a python function on claim cards; `FOUNDATION_v0.6.md §3.3
flag-rule29` is a prose rule on Blackbox Note cooking-log entries. Neither this patch nor any
downstream document may cite "rule29" bare without naming which sequence it means (spec §1b item
6, founder decision 8 above).

---

## 17. What this patch does not cover

- The market/positioning table (Appendix B) — untouched this pass.
- Any change to `schema/claim_card.schema.json`'s existing required-field list beyond the additive
  fields named above — no field is removed or narrowed.
- Actually applying any of the schema/kernel/template diffs specified above — this file is Dr,
  specified-not-applied, same discipline as `FOUNDATION_v0.6_PATCH.md` before it.
- Independent review of this patch itself — K0, single-pass, same-model; per `PUB-ADVERSARIAL-
  REVIEW`/`AGENTS.md` gate rule 8, no independent check has run, so none of this may be cited as
  more than `Dr` until one does.
