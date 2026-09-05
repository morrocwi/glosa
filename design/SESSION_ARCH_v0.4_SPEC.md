# SESSION_ARCH_v0.4_SPEC.md

Founder ruling BBL-2026-09-05-119 governs every judgment below: never lower a claim to make
it pass — raise the work (evidence anchoring, defeater, failing control, build path) until it
actually supports the claim as stated. Rule 17 (file:line + continuous verbatim) applies to
every citation in this document. Tiers used: `Dr` / `finite_diagnostic` / `Open` — no `Th_coqc`
claims are made here. No novelty words, no vendor credit, no AI signature. Human owns the
problem/question/hypothesis-selection; AI (this document) proposes, never certifies.

---

## 1. สรุปสำหรับ founder (Thai, 10 บรรทัด)

1. ที่ประชุม 2026-09-05 เสนอ 8 proposal เรื่องสถาปัตยกรรม "session" — ขอบเขต session, ความจำที่หายไปของ AI ข้าม session, การคงอยู่ของสมมติฐานที่เลือกไว้ (retention), และ diagnostic เชิง lineage/momentum
2. หลังตรวจ citation แบบ file:line จริงทุกจุด (Rule 17) พบว่า 4 proposal อ้างอิงถูกต้องครบและมี control ที่รันได้จริง — พร้อม build: SA-1 (session boundary บน Blackbox Note), schema.entry-resistance-precommit-field (ช่อง R* ที่ Problem Card), kernel.reciprocal-lineage-diagnostic (χ_recip แบบ Open-tier รอ session_id), schema.retention-direction-field (ช่อง retained_direction บน hypothesis_selection.yaml)
3. 3 proposal มีจุดบกพร่องเล็กแต่แก้ได้ในรอบเดียว (เลขบรรทัดอ้างอิงผิด 1-2 บรรทัด หรือ build_path ยังไม่ครอบ acceptance_test เต็ม) — SA-3, SA-4, process.run-existing-open-falsifier-klike ต้องแก้ก่อน build
4. 2 proposal ยังไม่พร้อม: SA-2 มี citation ผิดจุดสำคัญ (อ้าง NC-33/34 ผิด 2 บรรทัด) และ acceptance test รันไม่ได้จริงเพราะ hypothesis_selection.yaml ยังไม่มี session_id — ต้องรอ SA-1 build ก่อน; kernel.session-boundary-momentum-reset-assertion เป็นข้อเสนอซ้ำกับ SA-1 (คนละชื่อ เป้าหมายเดียวกัน) ต้องรวมกันไม่ใช่ build สองรอบ
5. ทุก proposal ยึดหลักเดียวกัน: "การคงอยู่ (retention) ไม่ใช่หลักฐานทิศทาง (expansion/tunnel) ด้วยตัวมันเอง" — ต้องมี independent check เท่านั้นถึงจะบอกทิศทางได้ นี่คือ non-collapse rule ใหม่ NC-77
6. สิ่งที่ยังขาดจริงในระบบ (ไม่ใช่แค่ proposal ที่ผิด): hypothesis_selection.yaml ไม่มี session-grouping key เลย — ทำให้ SA-2 ยังทดสอบอัตโนมัติแบบเต็มรูปแบบไม่ได้จนกว่าจะเพิ่ม session_id
7. kernel/glosa_kernel.py มี `_max_independence_class` (I0–I5) อยู่แล้วจริง ใช้ต่อยอด falsifier H3 ได้โดยไม่ต้องสร้าง mechanism ใหม่
8. design/TODO_v0.3.md ไม่มีบรรทัด `[Open]` สำหรับ `rule17.claim-card-certification-open` ตามที่ DAG อ้าง — เป็นช่องว่างจริงที่ proposal เรื่อง H3 ต้องเปิดเผย ไม่ใช่ปิดเงียบ
9. งานที่ founder ต้องตัดสินใจเอง (ดูหัวข้อ 7): บ้านของ session-architecture (ต่อ Blackbox Note หรือไฟล์ session.yaml ใหม่), ตำแหน่ง NC-77 ใน DECISIONS.yaml ก่อนชนกับ proposal อื่น, ย้อนหลังหรือไม่ย้อนหลังสำหรับ field บังคับใหม่บน Problem Card, และรวม SA-1 กับ proposal ซ้ำเข้าด้วยกัน
10. ไม่มี proposal ใดถูก "ลดคำกล่าวอ้างให้ผ่าน" — ทุกจุดที่พบปัญหาคือยกงานขึ้น (แก้เลขบรรทัด, เพิ่ม script, เปิดเผยช่องว่างจริง) ตามคำสั่ง founder ruling BBL-2026-09-05-119

---

## 2. Session-architecture layer — one coherent design

### 2.1 The Session object

Not a new artifact by default — see §2.2 for the one-fact-one-home decision. Fields, each
traced to its source proposal and citation:

| field | type | source | citation |
|---|---|---|---|
| `session_id` | string | SA-1, schema.retention-direction-field | v7.1:489-490 (F8), v7.1:493 (F10) |
| `entry_anchor` (H0) | ref → Problem Card | schema.entry-resistance-precommit-field | v7.1:351 `ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*` |
| `human_owner` | string (non-delegable) | SA-3, FOUNDATION §2.2 S1 row | design/FOUNDATION_v0.6.md:425 |
| `ai_routes` | array (which independence-class route touched this session) | kernel.reciprocal-lineage-diagnostic | design/FOUNDATION_v0.6.md:1163 (`prompt_ancestry`) |
| `question_trace[]` | array of Problem Card refs opened this session | SA-3 | v7.1:353-354 (V_0) |
| `candidate_set_deltas[]` | array | schema.retention-direction-field | v8.1:345,347 (Gs/Ts/Δs) |
| `chooser_reaffirmations[]` | array (human re-selects at session reopen) | schema.retention-direction-field, SA-2 | v8.1:356 (Repair 8) |
| `resistance_precommit` (R*) | string (concrete route: source/record/experiment/critic/authority) | schema.entry-resistance-precommit-field | v7.1:356 |
| `retention_note` | ref → Blackbox Note `human_retained_residue_ref` | SA-1 | v7.1:489-490 |
| `retained_direction` | enum `unknown \| expansion \| tunnel` (default `unknown`) | SA-2, schema.retention-direction-field | v8.1:358-361 |
| `momentum diagnostics (m^H, m^AI, chi_recip)` | Open finite diagnostics, diagnostic-only, never feed a tier/verdict | kernel.reciprocal-lineage-diagnostic, SA-4 (declined as schema fields) | v7.1:447, v7.1:496, v7.1:554 |
| `ai_state_at_boundary` | fixed literal `reset` | SA-1 / kernel.session-boundary-momentum-reset-assertion | v7.1:328 `m^{AI}_{s+1,0} = 0 (by architectural scope definition)` |

### 2.2 Where it lives — decided by one-fact-one-home

Direct check: `schema/blackbox_note.schema.json` already owns per-line `speaker`/`ts` (proves
sequencing) and has a bare optional `session_ref` string (no open/close semantics).
`schema/hypothesis_selection.schema.json` already owns `decided_by`/`decided_at` (S3c, FOUNDATION
§2.2 line 429) but has no session-grouping key at all — confirmed by direct read, no `session_id`
field exists there today. `schema/problem_card.schema.json`'s `intake` object (S1) requires only
`{q1_issue, q2_user_proposal}` — no pre-exposure or resistance-route fields exist there either.

Decision (one-fact-one-home, no duplicate homes):
- **Session boundary + AI-reset fact** → lives on **Blackbox Note** (`opened_at`, `closed_at`,
  `ai_state_at_boundary`, `human_retained_residue_ref`) — SA-1's target, not a new `session.yaml`.
  Blackbox Note is the only artifact that already carries per-turn speaker sequencing; a new file
  would duplicate that fact in a second home.
- **Retained-direction-of-a-choice fact** → lives on **`hypothesis_selection.yaml`**
  (`retained_direction` field) — this is S3c's own artifact (the K1 selection ledger), not a new
  ledger; SA-2 and schema.retention-direction-field both correctly target it.
- **Pre-exposure content + precommitted route facts** → live on **`problem_card.schema.json`**'s
  `intake` object (S1) — SA-3's and schema.entry-resistance-precommit-field's corrected target,
  not §2.1a (which explicitly disclaims reopening S1-S6 ownership, FOUNDATION_v0.6.md:354).
- **Reciprocal-lineage/momentum diagnostics** → live on **`schema/kg_edge.schema.json`** (new
  `session_id` field) plus a **new CLI subcommand**, never as a schema field on any claim/problem
  card (SA-4's decline is upheld) — diagnostic-only, per v7.1:496 "cannot be read as warrant,
  truth, or human benefit."

No single new `session.yaml` artifact is created by this spec: the Session object in §2.1 is a
**logical view** composed by joining Blackbox Note + hypothesis_selection.yaml + problem_card.yaml
+ kg_edge.yaml by `session_id`, not a fifth physical file. This avoids the one-fact-one-home
violation a standalone `session.yaml` would create (the same defect SA-1's original draft and
kernel.session-boundary-momentum-reset-assertion both would have produced if pointed at §2.3's
R0/R1/R2 registers instead of Blackbox Note itself — confirmed: FOUNDATION_v0.6.md:453 R1 names
the note's *internal reading stage*, not a session-momentum construct).

**Founder decision needed:** ratify that the Session object stays a logical join across four
existing artifacts rather than becoming its own file (see §7).

---

## 3. Per-proposal status (citations_verified && control_mechanical && invariant_ok && score>=6 → build_now)

| id | citations_verified | control_mechanical | invariant_ok | score | status | delta from original |
|---|---|---|---|---|---|---|
| SA-1 | true | true | true | 8 | **build_now** | none — original target/claim held |
| schema.entry-resistance-precommit-field | true | true | true | 6 | **build_now** | corrected target from §2.1a (disclaims reopening S1) to `problem_card.schema.json` `intake` object |
| kernel.reciprocal-lineage-diagnostic | true | true | true | 9 | **build_now** | corrected claim from "diagnose now" (false premise: no session_id/actor field exists) to "add session_id, then diagnose"; tier downgraded honestly to `Open` |
| schema.retention-direction-field | true | true | true | 8 | **build_now** | corrected target from a nonexistent "K1→K2 conversion ledger" to real `hypothesis_selection.yaml` |
| SA-4 | false | true | true | 4 | **with_revision** | fix 3 off-by-1/2 line citations (v7.1:550→548, :552→550, :494→495) and the irrelevant 4th citation (FOUNDATION:1670 padding) before logging |
| SA-3 | false | false | true | 5 | **with_revision** | fix v7.1:354→353 citation; build_path must add the timestamp cross-check script the acceptance_test itself requires, or narrow acceptance_test to the schema-required-fields half only |
| process.run-existing-open-falsifier-klike | false | true | true | 7 | **with_revision** | fix DAG_v0.3.yaml:76→78 citation; disclose in the row itself that TODO_v0.3.md has no matching `[Open]` line today (confirmed by direct read — the DAG node's own acceptance_test was never actually satisfied in-repo) |
| SA-2 | false | false | true | 4 | **still_open** | fix FOUNDATION_v0.6.md:2254→2256 citation; blocked on SA-1/session_id landing before its acceptance test can run on real multi-session data (currently only trivially true for single-session rows) |
| kernel.session-boundary-momentum-reset-assertion | (n/a — duplicate) | (n/a) | (n/a) | (n/a) | **still_open** | duplicate framing of SA-1 pointed at a different (wrong) FOUNDATION section (§2.3 R0/R1/R2, which govern Blackbox Note's internal reading stages, not session momentum); must be merged into SA-1, not built separately — building both would create two homes for the same fact |

---

## 4. Kernel rules 29+ (new this pass)

| rule | statement | enforced by | error/warning string | failing control |
|---|---|---|---|---|
| `NC-77` Family J | Retention≠Direction — persistence/retention of a claim, habit, or chosen hypothesis across ≥2 sessions is never by itself evidence it is expansion rather than tunnel; only a linked independent-check artifact may set the sign. Default: `retained_direction: unknown`. | `schema/hypothesis_selection.schema.json` `retained_direction` field, `D-RETENTION-DIRECTION` disclaimer | `WARN: retained_direction=unknown — no linked independent-check artifact for a row chosen across ≥2 sessions` | Must fire: `chosen` row spanning ≥2 sessions, no `evidence_relation`→review_report/falsifier link → forced `unknown`. Must NOT fire: a row whose `evidence_relation` resolves to an existing checker/falsifier verdict — that verdict's own sign stands. |
| `D-RETENTION-DIRECTION` (disclaimer, FOUNDATION §5) | States the NC-77 rule in disclaimer-catalogue form for any doc emitting a `retained_direction` value. | design/FOUNDATION_v0.6.md §5 | — | n/a (documentation-only) |
| `D-NO-PRECOMMIT-ROUTE` (flag, non-mandatory) | Flags — never blocks — a Problem Card reaching `READY_FOR_S2` with `intake.precommitted_resistance_route` null/absent. | `schema/problem_card.schema.json` `intake` object | `FLAG: precommitted_resistance_route missing at READY_FOR_S2` | Must fire: `intake.precommitted_resistance_route` absent + `readiness.verdict=READY_FOR_S2`. Must NOT fire: field names a concrete route (source/record/experiment/critic/authority) before the first AI-turn line in the linked Blackbox Note. |
| (session-boundary rule, unnumbered pending founder ratification of §2.2) | A Blackbox Note pair sharing one `session_id` split by an actual tool/process restart must both carry `ai_state_at_boundary: reset` (literal). | `schema/blackbox_note.schema.json` | `ERROR: ai_state_at_boundary missing or not literal 'reset' across shared session_id` | Must fire: shared `session_id`, second file's field missing/non-literal → reject. Must NOT fire: different `session_id` values on topically-similar notes. |

---

## 5. Sim fixtures to add

| defect class | source proposal | fixture sketch |
|---|---|---|
| `tunnel_unflagged` | schema.retention-direction-field, SA-2 | Synthetic `hypothesis_selection.yaml` rows, `chosen` across 2+ sessions, no independent-check link → must render `retained_direction: unknown`, never a bare pass. |
| `retention_undeclared` | SA-1 | Two Blackbox Notes sharing `session_id` across a real process restart, one missing `ai_state_at_boundary: reset` → must fail schema validation. |
| `chooser_forgotten` | schema.retention-direction-field (`chooser_reaffirmations[]`) | A session reopening a previously-chosen hypothesis without a fresh `chooser_reaffirmations[]` entry → flag, since S3c requires the human (not persistence) to reaffirm. |
| `question_drift_unlogged` | SA-3 (`question_trace[]`) | A session whose Problem Card sequence diverges from its own declared `q1_issue` without a new Problem Card being opened → flag as untracked drift. |
| `momentum_overclaimed` | kernel.reciprocal-lineage-diagnostic, SA-4 | Any document or code path that reads `chi_recip`/`m^H`/`m^AI` as if it were warrant, truth, or a release gate (v7.1:496) rather than an Open diagnostic → hard reject, this is the exact clause SA-4 declined to schematize and this fixture is its enforcement complement. |

H3 falsifier (process.run-existing-open-falsifier-klike) is a sixth, separately-scoped fixture
(`methodology/H3_falsifier_sim.py`): synthetic claim-card batch, 30% injected undisclosed
`ai_filled`, same-vendor vs cross-vendor (I1/I2 vs I4/I5) catch-rate comparison, plus a
zero-injection negative-control arm that must report 0/0. This is the only proposal in this pass
carrying an *empirical* (not structural/definitional) claim type per v8.1 §1, so it is the only
one whose defeater is "sufficiently strong contrary evidence," not internal inconsistency.

---

## 6. Human Mastery Gate protocol card outline (§7.5)

Purpose: keep hypothesis-selection and resistance-route pre-commitment human-owned in practice,
not just in schema `required` lists (mirrors FOUNDATION_v0.6.md:425's "AI: routes the intake,
never infers Q2's answer").

1. **Entry check** — Problem Card's `intake.precommitted_resistance_route` and
   `problem_stated_before_first_ai_response` must both be populated before any AI candidate is
   generated for that Problem Card (schema.entry-resistance-precommit-field, SA-3).
2. **Selection check** — every `hypothesis_selection.yaml` row with `selection.chosen: true` must
   carry `responsible: human` (already true per FOUNDATION_v0.6.md:429) and, if it spans ≥2
   sessions, a non-null `chooser_reaffirmations[]` entry per session, not a stale flag inherited
   from the first session.
3. **Direction check** — no `retained_direction` other than `unknown` may be written without a
   resolvable `evidence_relation` to a review_report/falsifier artifact (NC-77).
4. **Boundary check** — every session close writes a Blackbox Note `closed_at` and
   `ai_state_at_boundary: reset`; every session open either references the prior note's
   `human_retained_residue_ref` or explicitly records `none`.
5. **Diagnostic-not-gate check** — any place `chi_recip`/`m^H`/`m^AI` is displayed must carry the
   v7.1:496 disclaimer inline ("cannot be read as warrant, truth, or human benefit") or the display
   is itself a `momentum_overclaimed` defect (§5).

This card is a **self-check protocol for the human/AI pair**, not a release gate distinct from
existing K0/K1/K2 machinery — it composes checks 1-5 that already exist across the four artifacts
named in §2.2, it does not add a new certification layer (per EPIS-KNOWLEDGE-VALIDATION: no
vertical-authority gate is being introduced here).

---

## 7. Founder decisions (human-only)

1. **Ratify §2.2's one-fact-one-home decision**: Session object stays a logical join across
   Blackbox Note + hypothesis_selection.yaml + problem_card.yaml + kg_edge.yaml; no new
   `session.yaml` file is created. (Blocks: whether SA-1 and
   kernel.session-boundary-momentum-reset-assertion can be merged into one build.)
2. **Merge duplicate proposals**: kernel.session-boundary-momentum-reset-assertion duplicates
   SA-1's fields and defeater but points at the wrong FOUNDATION section (§2.3 R0/R1/R2 instead of
   Blackbox Note directly). Confirm SA-1 is canonical and the kernel.* proposal is retired without
   a separate build, to avoid two homes for `ai_state_at_boundary`.
3. **Reserve NC-77** in `cpg/research/coordination/DECISIONS.yaml` before any concurrent Family J
   proposal can claim the id (the id itself is independently verified free — see §3 — but the
   reservation act is a founder-owned ledger write, not an AI one).
4. **SA-3 retroactivity**: whether the three new required Problem Card fields
   (`problem_stated_before_first_ai_response`, `prior_model_or_guess`, `verification_intent`)
   apply to already-published Problem Cards or forward-only (recommended: forward-only, per
   meeting §5.3 — but this is the founder's call, not a default AI may set).
5. **SA-4 ledger row**: ratify logging the chi_recip/m^H/m^AI decline as `status: RECORDED` in
   `cpg/research/coordination/DECISIONS.yaml` (not the fabricated `DECLINED-FOR-NOW` value, which
   is not in that ledger's status enum).
6. **Approve building the H3 sim now**: this is the first genuinely empirical (n=0, untested)
   falsifier run under this framework since the fabricated-C-id incident; running it produces a
   real result either way (supported/not supported/inconclusive) rather than leaving the concept
   paper's own named falsifier at n=0 indefinitely.
7. **hypothesis_selection.yaml session-grouping key**: approve wiring `session_id` (from SA-1's
   Blackbox Note session boundary, once built) into `hypothesis_selection.yaml` as SA-2's own
   build_path names — without this, SA-2's acceptance test remains scoped to trivially-true
   single-session rows only, which per BBL-2026-09-05-119 is not an acceptable stopping point, only
   an honest interim state.

---

## 8. DAG_v0.4 node YAML block

```yaml
# design/DAG_v0.4.yaml (new nodes this pass — additive to DAG_v0.3.yaml, no renumbering of
# existing nodes; ids match the proposal ids verified above)

- id: session.boundary-blackbox-note        # SA-1
  status: build_now
  target:
    - templates/knowledge/blackbox_note.yaml
    - schema/blackbox_note.schema.json
    - design/FOUNDATION_v0.6.md §2.3 (new bullet, not R0/R1/R2)
  fields_added: [session_id, opened_at, closed_at, ai_state_at_boundary, human_retained_residue_ref]
  acceptance_test: "two Blackbox Note files sharing session_id split by a real process restart both carry ai_state_at_boundary literal 'reset'"
  citations: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:489, ':490, ':493, ':496, ':497, ':328]
  founder_decision_needed: true   # merge target for kernel.session-boundary-momentum-reset-assertion, see §7.2

- id: schema.entry-resistance-precommit-field
  status: build_now
  target: schema/problem_card.schema.json intake object (NOT FOUNDATION §2.1a)
  fields_added: [intake.precommitted_resistance_route]
  disclaimer_added: D-NO-PRECOMMIT-ROUTE (flag, non-mandatory)
  acceptance_test: "schema validator flags (does not reject) intake.precommitted_resistance_route null at READY_FOR_S2"
  citations: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:351, ':356, design/FOUNDATION_v0.6.md:354, ':425, design/DAG_v0.3.yaml:112]
  founder_decision_needed: true

- id: kernel.reciprocal-lineage-diagnostic
  status: build_now
  tier: Open   # honestly not yet Dr — becomes Dr then finite_diagnostic only after fixture runs
  target: schema/kg_edge.schema.json (new field session_id); new CLI glosa kg diagnose --chi-recip
  acceptance_test: "reproducible chi_recip count across two horizon-boundary settings on ≥90% of synthetic session_id-grouped sets; 'not computable' (never a numeric default) when session_id absent"
  citations: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:447, ':496, ':554, design/FOUNDATION_v0.6.md:1163]
  founder_decision_needed: true

- id: schema.retention-direction-field
  status: build_now
  target: schema/hypothesis_selection.schema.json (new field retained_direction), design/FOUNDATION_v0.6.md §5 (new disclaimer D-RETENTION-DIRECTION), Appendix A Family J (new row NC-77)
  acceptance_test: "100% of chosen rows spanning ≥2 sessions with no linked independent-check artifact tagged retained_direction:unknown; scoped to single-session rows until session_id lands (see founder decision 7)"
  blocked_on: session.boundary-blackbox-note (for session_id propagation into hypothesis_selection.yaml)
  citations: [sources/notes/EPISTEMIC_FUSION_v8.1.txt:345, ':347, ':356, ':361, design/FOUNDATION_v0.6.md:2259, ':429]
  founder_decision_needed: true

- id: schema.pre-exposure-anchor-fields        # SA-3, with_revision
  status: with_revision
  revision_needed:
    - "citation sources/notes/EPISTEMIC_FUSION_v7.1.txt:354 -> correct to :353"
    - "build_path must add the Problem-Card-vs-Blackbox-Note timestamp cross-check script the acceptance_test requires, or acceptance_test must be narrowed to the schema-required-fields half only"
  target: schema/problem_card.schema.json (3 new required fields)
  founder_decision_needed: true   # retroactive vs forward-only, see §7.4

- id: process.h3-falsifier-run                  # with_revision
  status: with_revision
  revision_needed:
    - "citation design/DAG_v0.3.yaml:76 -> correct to :78"
    - "row must disclose that design/TODO_v0.3.md carries no matching [Open] line today, contra the DAG node's own acceptance_test claim"
  target: methodology/H3_falsifier_sim.py (new); DECISIONS.yaml row recording result
  founder_decision_needed: false   # per proposal's own field, but see §7.6 for the go-ahead

- id: decisions.chi-recip-momentum-decline      # SA-4, with_revision
  status: with_revision
  revision_needed:
    - "3 citation line corrections: EPISTEMIC_FUSION_v7.1.txt:550->548, :552->550, :494->495"
    - "drop or replace the 4th citation (design/FOUNDATION_v0.6.md:1670, irrelevant boilerplate)"
  target: cpg/research/coordination/DECISIONS.yaml (status:RECORDED, not fabricated DECLINED-FOR-NOW); glosa/DECISIONS.md mirror
  founder_decision_needed: true

- id: schema.retention-direction-field.session-grouping-key   # SA-2, still_open
  status: still_open
  blocking_defect:
    - "citation design/FOUNDATION_v0.6.md:2254 -> correct to :2256"
    - "acceptance_test not mechanically runnable on real multi-session data until hypothesis_selection.yaml gains session_id (blocked on session.boundary-blackbox-note landing)"
  founder_decision_needed: true

- id: session.boundary-momentum-reset-duplicate   # kernel.session-boundary-momentum-reset-assertion, still_open
  status: still_open
  disposition: "merge into session.boundary-blackbox-note (SA-1); do not build as a second node — same fields, same defeater, wrong FOUNDATION section originally cited (§2.3 R0/R1/R2 instead of Blackbox Note)"
  founder_decision_needed: true
```
