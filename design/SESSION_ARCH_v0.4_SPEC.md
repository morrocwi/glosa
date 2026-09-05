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

### 1b. สรุปปรับปรุง — รวม Part 2 (Thai, ≤12 บรรทัด)

1. Part 2 ตรวจอีก 15 proposal จาก 3 lens: blackbox-dialogue (5), lrs-defeaters (5), human-uplift (5) — รวมกับ Part 1 (9 proposal) เป็น 24 proposal ทั้งรอบนี้
2. รวมทั้งหมด: **build_now 13 · with_revision 7 · still_open 4** (Part 1 = 4/3/2, Part 2 = 9/4/2)
3. blackbox-dialogue build_now มีจุดเดียว: schema.blackbox-question-trace (ต้องแก้คำอ้าง "glosa's own Human Return Test" ที่ไม่มีจริงในเอกสาร glosa เองก่อน ship); อีก 3 ต้องแก้ก่อนสร้าง (line-origin enum, chooser-reaffirmation, candidate-set-delta) และ 1 ถูกปฏิเสธซ้ำจริง (language-bridge sub-field เคยถูกตัดสิน keep:false มาแล้วใน MEETING_2026-09-05_judged.json)
4. human-uplift build_now 3 จุด: HU-1 (ต่อสาย Human Mastery Gate ที่เขียนไว้แล้วเข้า publish gate จริง), HU-2 (entry-anchor H0 เต็มชุด), HU-5 (bound P01 completeness-prompt); HU-4 แก้ citation อย่างเดียวก็ build ได้; HU-3 ยังเปิดอยู่จริง (citation ปลอมจุดหนึ่ง + อ้าง defeater ผิดข้อ + รอ session_id จาก SA-1)
5. lrs-defeaters build_now ครบทั้ง 5: ไฟล์เป็น TODO-line ไม่สร้าง DAG node ใหม่, defeater_log ต้อง required+enum, dialogue_table เพิ่มคอลัมน์ `defeater_class` (ไม่ใช่ `claim_type` ซ้ำ), kernel rule29 ("strength of claim" ไม่ใช่ defeater), kernel rule30 (defeater_class ต้องจับคู่ style ให้ตรง v8.1)
6. เลข kernel rule ชนกันคนละชุด: kernel/glosa_kernel.py มี rule29/rule30 ใหม่ (2 proposal ข้างต้น) แต่ kernel.candidate-set-delta-cooking-step (blackbox-dialogue) เสนอ "rule 29" ในชุดคนละที่ (design/FOUNDATION_v0.6.md §3.3 flag-rule 26-28) — คนละ namespace ไม่ชนจริง แต่ต้องเขียนแยกให้ founder เห็นชัด ไม่ปล่อยให้อ่านว่าเลขเดียวกัน
7. งานที่ founder ต้องตัดสินเพิ่ม (นอกเหนือ §7 เดิม): ยืนยันแยก namespace rule29/30 ตามข้อ 6, อนุมัติ scope `chooser_reaffirmed` เฉพาะ `hsel-` หรือสร้าง cross-file validator เพิ่มสำหรับ `responsible:human`, และยืนยันถอน schema.blackbox-language-bridge-subfield ตาม chair ruling เดิมจริงหรือ founder จะ overrule
8. ไม่มี proposal ใดใน Part 2 ถูกลดคำกล่าวอ้างให้ผ่านเช่นกัน — คะแนนต่ำทุกจุดมี exact fix ระบุแล้ว (เลขบรรทัด, ไฟล์/tool เป้าหมายผิด, defeater อ้างผิดข้อ) ตาม BBL-2026-09-05-119

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

---

# PART 2 — Blackbox/dialogue, LRS-defeaters, human-uplift

Same governing rule as Part 1: founder ruling BBL-2026-09-05-119 (never lower a claim, raise the
work), Rule 17 (file:line + continuous verbatim), tiers `Dr`/`finite_diagnostic`/`Open` only, no
novelty words, no vendor credit, no AI signature, human owns problem/hypothesis-selection. Source:
`design/SESSION_ARCH_v0.4_rejudged.json`, the 15 rows with `lens` in
`{blackbox-dialogue, lrs-defeaters, human-uplift}`.

## 9. Per-proposal status (same rule as §3: `citations_verified && control_mechanical &&
invariant_ok && score>=6 → build_now`; one flag false but fixable → `build-with-revision`
with the exact fix stated; otherwise → `still_open` with the raise-path stated, never a
softened claim)

### 9.1 blackbox-dialogue

| id | citations_verified | defeater_legitimate | control_mechanical | invariant_ok | score | status | exact fix / raise-path |
|---|---|---|---|---|---|---|---|
| `schema.blackbox-question-trace` | true | true | true | true | 6 | **build_now** | `claim_as_stated` overreaches: "glosa's own Human Return Test" does not exist anywhere in glosa's design docs (grep confirms 0 hits outside `sources/`) — it is a construct from `sources/notes/EPISTEMIC_FUSION_v7.1.txt:467` that glosa has not adopted. Before ship, rewrite the motivating sentence to rest on the real, fully-cited gap alone: `question_human`/`question_readout` are single-shot per Claim Card (`design/FOUNDATION_v0.6.md:495`) with no field for how the question changed turn-to-turn. Build itself (top-level optional `question_trace[]` on `schema/blackbox_note.schema.json`, coverage-check extension to `tools/blackbox_log.py`) is unchanged. |
| `schema.blackbox-line-origin-enum` | true | true | false | true | 6 | **build-with-revision** | `failing_control` invokes "the claim_card's own creation timestamp" to bound the scan window; `claim_card.schema.json` has no required/reliable creation-timestamp field (only optional `revision_history[].date`). Fix: replace the cross-file timestamp comparison with the same-document `cooking[]`/`became[]` ordering check the proposal's own two fixtures already use (a `step: review`/`revision` cooking entry naming the line, occurring before its `became[]` entry, resolves `ai_proposed_adopted`; absent that, `ai_proposed_forgotten`). No other change to `lines[].origin` enum or the deprecated `ai_proposed` alias. |
| `kernel.candidate-set-delta-cooking-step` | true | true | false | true | 3 | **build-with-revision** | Two build-path defects, both fixable: (1) the named acceptance-test fixture `blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md` has zero schema-shaped `cooking[]` entries (it only has a prose pointer to an Appendix) — retarget the fixture to `schema/examples/blackbox_note.example.json` or a `projects/GLS-2026-001_*/blackbox_note.yaml` instance that actually carries `cooking[]` rows. (2) `build_path` names `tools/blackbox_log.py` for the checker extension — that script is the founder's daily voice-entry Blackbox LOG tool (BBL-YYYY-MM-DD-NNN), unrelated to the Blackbox Note's `cooking[]` schema; this is new checker tooling, not an extension of that file. Field addition itself (`candidate_set: {before, after, forgotten}` on `cooking.items`) and the flag semantics (`CANDIDATE-DROP-UNEXPLAINED`) are sound and unchanged. |
| `schema.blackbox-chooser-reaffirmation` | true | true | false | true | 4 | **build-with-revision** | The `hsel-` id-pattern branch (`became[]` target matches `^hsel-`) is mechanically build-ready as stated. The second trigger — "a claim_card whose `responsible` field is `human`" — is not: `became[].claim_card` is a bare string reference, so checking the referenced document's `responsible` field needs a cross-file validator this proposal never designs, and its own Fixture C only exercises the non-trigger (`responsible: ai`) case, never a genuine `responsible: human` trigger. Fix: either (a) scope the requirement to `hsel-` ids only and ship now, or (b) specify the cross-file validator and add a real Fixture D exercising the `responsible: human` branch before claiming it build-ready. |
| `schema.blackbox-language-bridge-subfield` | true | false | true | true | 1 | **still_open** | The proposal's own stated defeat condition already fires and was missed: `design/MEETING_2026-09-05_judged.json:84-92` already adjudicated this identical proposal (same id, title, target) `keep:false`, score 4.5, reason "the proposal's own acceptance_test premise ... is a misread of already-specified glosa content." Per the proposal's own defeater clause, this must be **withdrawn**, not revised — raise-path is not a schema fix, it is: found the existing chair ruling missed by this pass's defeater search (which only checked `FOUNDATION_v0.6.md`, `FOUNDATION_v0.6_PATCH.md`, and the schema file, never `design/MEETING_2026-09-05_judged.json`); only a founder overrule of that standing ruling could revive it. |

### 9.2 human-uplift

| id | citations_verified | defeater_legitimate | control_mechanical | invariant_ok | score | status | exact fix / raise-path |
|---|---|---|---|---|---|---|---|
| `HU-1` | true | true | true | true | 8 | **build_now** | None load-bearing. Note only: "no `FOUNDATION_v0.1.md` exists anywhere" is true for tracked files but a git tag `v0.1.0` exists — worth a one-line check of that tag's tree before treating the §7.5 pointer as unambiguously broken, though this doesn't change the verdict. |
| `HU-2` | true | true | true | true | 8 | **build_now** | None load-bearing. Note only: the defeater-search claim of "zero hits for 'evidence' in P02_intake.md" is not literally true (two incidental prose hits) — restate as "no field captures `E_0` specifically," which is the substantive claim and does survive. |
| `HU-3` | false | false | false | true | 2 | **still_open** | Three real defects, not one: (1) citation 7 (`hypothesis_selection.schema.json:1`) is fabricated — line 1 is `{`; the actual `required[]` array is `["id","problem_ref","decided_by","candidates","selection","cooking_log_ref"]` at line 7, omitting `decided_at`/`routes_to` (which exist elsewhere, lines 13/89, not contiguously) — correct to a real continuous verbatim excerpt. (2) `legitimate_defeater` cites `sources/notes/EPISTEMIC_FUSION_v8.1.txt:362-365`, which is about a *different* collapse (augmentation vs. synergy vs. return being empirically interchangeable), not about Repair 8's expansion-vs-tunnel sign — recite the defeater from `v8.1:359-361` directly, matching NC-77 in §4. (3) `failing_control` needs a `session_id` grouping key `hypothesis_selection.schema.json` does not yet have — restate `build_path` as explicitly blocked on `session.boundary-blackbox-note` (SA-1) landing, per §7 founder decision 7, rather than presented as runnable today. |
| `HU-4` | false | true | true | true | 3 | **build-with-revision** | All four citations are synthesized aggregations, not continuous verbatim at the stated line — mechanism and defeater are otherwise sound. Corrected citations: `schema/claim_card.schema.json` `required[]` starts at line 9 (not the quoted comma-joined list at line 1, which is `{`); `schema/hypothesis_selection.schema.json` `problem_ref` is at line 11, `required[]` at line 7 (not line 1); `templates/knowledge/advisor_prompt_packet.md`'s "Every `claim_card.json` listed..." line is at line 31, not 27; `schema/problem_card.schema.json`'s `"retained_difference_statement"` is at line 22, not 17. Re-cite all four at their real lines with genuine continuous excerpts before this proceeds; `problem_ref` field addition and the `BLOCKED: NO_PROBLEM_REF` control are otherwise build-ready. |
| `HU-5` | true | true | true | true | 8 | **build_now** | None. This is the corrected resubmission of an earlier same-day draft refuted for a fabricated `C6/C10 (EPISTEMIC_FUSION)` id (`design/MEETING_2026-09-05_judged.json:128-137`); it now cites `NC-58` directly and correctly, per that ruling's own revision instruction. |

### 9.3 lrs-defeaters

| id | citations_verified | defeater_legitimate | control_mechanical | invariant_ok | score | status | exact fix / raise-path |
|---|---|---|---|---|---|---|---|
| `lrs.dr-tag-not-dag-node` | true | true | true | true | 8 | **build_now** | None load-bearing. Before `scripts/check_dag_node_gate.sh` (not yet built) ships, pin one canonical path — `cpg/research/coordination/DECISIONS.yaml` — instead of the parenthetical "or the repo's local decisions log" alternative currently in `acceptance_test`. |
| `lrs.defeater-defeated-status-field` | true | true | true | true | 8 | **build_now** | None. |
| `lrs.dialogue-table-claim-type-column` | true | true | true | true | 8 | **build_now** | `claim_as_stated` ("Add a claim_type + legitimate_defeater column") is stale relative to `change`'s actual, better-reasoned deliverable (`defeater_class`, deliberately renamed to avoid the exact collision the proposal's own evidence proves at `kernel/glosa_kernel.py:643`, where `claim_type` already routes rule16w). Sync `claim_as_stated` to name `defeater_class` before v0.4 lock — a literal build of the stale wording would recreate the defect the proposal itself defeats. |
| `lrs.defeater-not-collapse-rule` | true | true | true | true | 6 | **build_now** | The `legitimate_defeater` frames "absence-of-instance ≠ defeater for a forward-looking guard" as directly derived from `sources/notes/EPISTEMIC_FUSION_v8.1.txt:51-53`'s Burden rule ("'The claim is strong' is not a counterexample..."), but that text is about defending an architecture claim against "it's strong," not about justifying a new kernel guard against "no instance found yet." State this as a reasoned analogy to the sibling pattern already used by `methodology/data/contaminated_concept_table.json` (a pre-write catalogue, not a log of caught instances), not as a direct textual derivation. Mechanism/build_path unchanged. |
| `lrs.claim-type-defeater-enum` | true | true | true | true | 8 | **build_now** | None load-bearing. Two disclosed-but-unresolved soft gaps carried forward honestly, not blocking: no independent test yet that a keyword/phrase heuristic reliably distinguishes the five defeater styles across prose beyond the two worked examples; the five v8.1 classes eventually needing their own glosa claim cards is a separate, explicitly-flagged parallel deliverable. |

### 9.4 Session object table additions (extends §2.1)

The five blackbox-dialogue proposals each add one field to the Session object's join surface.
None of these create a new physical file — per §2.2's one-fact-one-home decision, each lands on
Blackbox Note (the artifact that already owns per-line/per-cooking-step sequencing):

| field | type | source | build status | one-line note |
|---|---|---|---|---|
| `question_trace[]` | array `{n, ts, question_text, derived_from_line, note}` on Blackbox Note (top-level, optional) | `schema.blackbox-question-trace` | **build_now** (after the claim-wording fix in §9.1) | Distinct from §2.1's `question_trace[]` row (which was sourced from SA-3 and scoped to Problem Card refs opened in a session) — this is the per-turn question-evolution trace *inside one note*; both are real, non-duplicate gaps at different granularities and both stay in the Session join. |
| `lines[].origin` enum `[human_authored, ai_proposed_pending, ai_proposed_adopted, ai_proposed_forgotten]` | replaces `lines[].ai_proposed: boolean` | `schema.blackbox-line-origin-enum` | **build-with-revision** (§9.1 fix) | Deprecated `ai_proposed` alias kept one migration cycle (`true → ai_proposed_pending`), per glosa's additive-first schema discipline; this is the field §2.1's `ai_state_at_boundary` and `retention_note` rows sit beside on the same artifact. |
| `became[].chooser_reaffirmed: {by, ts}\|null` | conditional-required sub-field on `lines[].became[]` | `schema.blackbox-chooser-reaffirmation` | **build-with-revision** (§9.1 fix — scope to `hsel-` ids first) | This is the mechanism that makes §2.1's `chooser_reaffirmations[]` row (sourced from `schema.retention-direction-field`/SA-2) actually enforceable at the point a candidate becomes a `hypothesis_selection.yaml` row, rather than only a session-reopen check. |
| `cooking.items[].candidate_set: {before, after, forgotten}` | additive counts, no derived verdict | `kernel.candidate-set-delta-cooking-step` | **build-with-revision** (§9.1 fix — retarget fixture + tool) | Sits beside §2.1's `candidate_set_deltas[]` row (sourced from `schema.retention-direction-field`, scoped to the hypothesis-selection ledger) as the earlier-stage, cooking-log-level sibling of the same non-collapse discipline — confirmed non-duplicative of the LRS `k_epi` node (`design/DAG_v0.3.yaml:321-333`). |
| `cooking.items[].bridge_kind` enum `[bilingual_rewrite, lens_world_to_readout, lens_readout_to_world]`, required when `step==translation` | `schema.blackbox-language-bridge-subfield` | **still_open** — do not add to the Session object | Already refuted by standing chair ruling (§9.1) — not merged into §2.1's table; listed here only so a future pass does not re-propose it without checking `design/MEETING_2026-09-05_judged.json` first. |

---

## 10. LRS changes — dialogue_table claim-type/defeater columns and the two new kernel rules

Kernel rule numbers below continue the **`kernel/glosa_kernel.py`** python-rule sequence, which
stops at `rule28` (confirmed by direct read — no `rule29`/`rule30` exist yet, no collision). This
is a **different numbering sequence** from the `design/FOUNDATION_v0.6.md` §3.3 non-collapse
"flag-rule" sequence (rules 26–28, prose/disclaimer-style, distinct from the python-function
sequence) that `kernel.candidate-set-delta-cooking-step` (§9.1, build-with-revision) separately
asks to extend to "rule 29" — that is a same-numbered but non-colliding sibling in a different
artifact/namespace; both must be written out in full (`kernel.glosa_kernel.rule29` vs.
`FOUNDATION_v0.6.md §3.3 flag-rule29`) wherever either is referenced, per §1b item 6, so a reader
never conflates the two.

Filing note (`lrs.dr-tag-not-dag-node`, build_now): none of the four proposals below get a new
`design/DAG_v0.3.yaml` node yet. Per that proposal's own control, they are filed as one
`design/TODO_v0.3.md` open-items line pending P09 vetting + a citation card, and only gain a
`nodes:` entry once each has an approved `cpg/research/coordination/DECISIONS.yaml` row
(`design/DAG_v0.3.yaml:6`). The DAG-node stubs in §13 are the *post-decision* shape, not filed
today.

### 10.1 `dialogue_table.defeater_class` + `legitimate_defeater` columns (`lrs.dialogue-table-claim-type-column`, build_now)

- **Target:** `templates/knowledge/dialogue_table.md` (table header); `design/S14_literature-review-system.md` §3.4 (`lines 208-216` column list).
- **New columns:** `defeater_class` — enum `[phenomenological, constitutive, structural_formal, diagnostic, empirical]`, per `sources/notes/EPISTEMIC_FUSION_v8.1.txt:30-72`'s five-way claim-type separation; `legitimate_defeater` — free text naming what would actually defeat *this row's* agrees/disagrees stance, per that class.
- **Not named `claim_type`:** `claim_type` is already a schema-fixed enum on `claim_card.yaml` routing `kernel/glosa_kernel.py:643` (rule16w) — reusing that name on the dialogue table would collide with a different, already-wired field. `defeater_class` is a deliberately non-colliding sibling name (per the §9.3 fix, sync `claim_as_stated` to say so).
- **Error/warning string:** none (lint, not a hard schema validator) — `INCOMPLETE: dialogue_table row has a stance (agrees/disagrees = YES) but no defeater_class/legitimate_defeater`.
- **Failing control:** MUST fire — a row with `agrees with H = YES` or `disagrees with H = YES` populated but `defeater_class`/`legitimate_defeater` blank. MUST NOT fire — a row with both new columns filled from the fixed five-way enum and non-empty defeater text.
- **Applies forward-only** (new `dialogue_table.md` instances), not retrofitted.

### 10.2 `defeater_log` required + `outcome` enum (`lrs.defeater-defeated-status-field`, build_now)

- **Target:** `schema/claim_card.schema.json` `provenance_dag.defeater_log` (lines 437-441), currently `{"type":"array","items":{"type":"object"}}` with no `required` keys — untyped, despite `design/FOUNDATION_v0.6.md:775` already documenting the shape as `[{node, date, outcome}]`.
- **Change:** add `required: [node, date, outcome]` and `outcome: {enum: [claim_survived, claim_revised, claim_withdrawn]}` to the item schema. This is the field that distinguishes "defeater attempted and survived" (`outcome: claim_survived`, entry present) from "never tested" (`defeater_log: []`) — the actual gap named in §9.3, distinct from the already-refuted idea of a new top-level status field.
- **Error string:** standard `jsonschema` `ValidationError` (missing required key / enum mismatch) — no custom kernel message needed, pure declarative schema constraint.
- **Failing control:** MUST fire — `provenance_dag.defeater_log: [{"node": "n1"}]` (missing `date`/`outcome`, currently passes silently). MUST NOT fire — `[{"node": "n1", "date": "2026-09-05", "outcome": "claim_survived"}]`.
- **Tier:** `Dr` now → `finite_diagnostic` once `tests/test_schema_defeater_log.py` (new) exists and passes.

### 10.3 Kernel rule29 — "strength of the claim" is not a defeater (`lrs.defeater-not-collapse-rule`, build_now)

- **Target:** `kernel/glosa_kernel.py` (new `rule29`, next free number in the python-rule sequence — confirmed no collision); `methodology/data/non_defeater_phrase_table.json` (new, sibling shape to `methodology/data/contaminated_concept_table.json`).
- **Rule statement:** a `tested.falsifier` field matching strength-of-claim / feels-solid phrasing is never itself a legitimate defeater, regardless of `claim_type` — grounded in `sources/notes/EPISTEMIC_FUSION_v8.1.txt:51,53`'s Burden rule ("'The claim is strong' is not a counterexample, an inconsistency, a failed phenomenon, or contrary evidence"), applied here by analogy to a forward-looking preventive guard (per the §9.3 framing fix — analogy, not direct derivation).
- **Error/warning string:** `ERROR: rule29 — tested.falsifier reads as a strength-of-claim assertion, not a legitimate defeater (matched pattern: "<match>")`.
- **Failing control:** MUST fire on `/strength of (the |this )?claim|feels solid|feels right|intuitively (strong|solid|convincing)/i` inside `tested.falsifier`. MUST NOT fire on a falsifier stating an actual contrary-evidence or absence condition, e.g. "defeated by a documented case where retained_direction is negative across 3 consecutive turns."
- **Tier:** `Dr` (specified this pass) → `finite_diagnostic` once `tests/test_rule29_non_defeater_phrase.py` (new) ships; disclosed as evadable-by-omission like `rule27`/`rule28`, never claimed as a structural guarantee.

### 10.4 Kernel rule30 — `defeater_class`-appropriate falsifier phrasing (`lrs.claim-type-defeater-enum`, build_now)

- **Target:** `schema/claim_card.schema.json` `five_questions.tested` (new optional `defeater_class` field, additive — same five-way enum as §10.1, added as a **sibling** of `claim_type`, not an extension of it, since `schema/common.defs.json:154-165`'s existing `claim_type` enum (EMPIRICAL/FORMAL/INTERPRETIVE/NORMATIVE/CONVENTIONAL_LEGAL/DECISION/SOCIAL/HUMAN_PARTICIPANT) already drives rule16w and would collide on the bare string `EMPIRICAL`); `kernel/glosa_kernel.py` new `rule30`.
- **Rule statement:** `defeater_class`'s value must be paired with a `falsifier` phrasing style matching that class per `EPISTEMIC_FUSION_v8.1.txt` §1 — e.g. `empirical` requires a contrary-evidence/replication-style falsifier (`v8.1:45`), not an absence/misdescription/irrelevance-style falsifier (`v8.1:53-54`, the `phenomenological` pairing).
- **Error/warning string:** `ERROR: rule30 — defeater_class=<class> but tested.falsifier matches the <other-class> phrasing style, not <class>'s`.
- **Failing control:** MUST fire — `defeater_class: EMPIRICAL` with `falsifier`: "the phenomenon would be absent within the declared scope, systematically misdescribed, or explanatorily irrelevant" (wrong pairing — that is the `phenomenological` style). MUST NOT fire — `defeater_class: EMPIRICAL` with `falsifier`: "defeated by a documented failed replication in an independent sample" (correct pairing), nor `defeater_class: PHENOMENOLOGICAL` paired with the absence-style text.
- **Tier:** `Dr` (citation corrected, mechanism redesigned this pass; not yet built) → `finite_diagnostic` once `tests/test_rule30_defeater_class.py` (new) ships. Open dependency, disclosed not resolved: the five v8.1 classes eventually needing their own glosa claim cards is a separate prerequisite/parallel deliverable, not pre-cited here.

---

## 11. Human-uplift — Mastery Gate, entry anchor, completeness-prompt boundary

### 11.1 HU-1 — wire the Human Mastery Gate into the mechanical publish gate (merges with §6 outline)

§6's Human Mastery Gate protocol card outline treats the gate as already-composable across
existing artifacts. HU-1 (build_now) supplies the concrete missing plumbing §6 assumed but did not
itself specify:

- **Real defect, not "missing from scratch":** the 10-question live unaided-defense checklist
  already exists, verbatim, inside `templates/paper/arxiv-twocol/main.tex:375-378` (and its onecol
  twin) and is asserted as an enforcement mechanism by two non-collapse rows,
  `methodology/data/non_collapse_table.json:570` (NC-56) and `:620` (NC-61). What is missing:
  (a) `design/FOUNDATION_v0.6.md §7.5` (`line 1619`) is a broken pointer — `"Unchanged from v0.1
  §7.5"` (`line 1621`) where no `FOUNDATION_v0.1.md` file exists in the repo; (b) the checklist is
  scoped only to the arxiv paper genre, invisible to a code-release or dataset-release L3+
  artifact; (c) `methodology/P10_publish_gate.md`'s actual mechanical R1-R7 dimension list
  (`line 17` R1, `line 32` R7) never names the gate — the NC-56/NC-61 enforcement claim is
  currently prose-only.
- **Build:** extract the 10 questions into a genre-independent `methodology/P16_human_mastery_gate.md`;
  new `schema/human_mastery_gate.schema.json` with required `gate_status` enum
  `[PASS, PASS_WITH_NAMED_GAPS, NOT_READY]` plus the 10 answer fields, each author-only
  (never `ai_filled`); new **R8** dimension on `methodology/P10_publish_gate.md` requiring
  `gate_status != NOT_READY` for any L3+ artifact; fix `FOUNDATION_v0.6.md §7.5` to cite P16
  instead of the nonexistent v0.1.
- **Failing control:** MUST fire — a non-Paper-genre L3+ claim card with no `human_mastery_gate.yaml`
  linked, passing R1-R7 clean today (`grep -rn mastery schema/*.json` returns zero hits, confirmed) —
  must now return `BLOCKED: NO_MASTERY_GATE_LINKED` at R8. MUST NOT fire — an S5 Paper-genre
  artifact using the arxiv template with `Gate status:` already filled `PASS`.
- **§6 merge:** §6's five self-checks (entry/selection/direction/boundary/diagnostic-not-gate) stay
  the self-check protocol for the human/AI pair; HU-1's R8 is the separate, narrower mechanical
  publish-gate wiring that makes "no independent check ⇒ no release" apply to the Mastery Gate
  itself, not a duplicate certification layer.

### 11.2 HU-2 — entry anchor (merges with the H0 field in §2.1)

§2.1 already lists `entry_anchor (H0)` as a Session-object field sourced from
`schema.entry-resistance-precommit-field`, citing `v7.1:351`'s `ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*`.
That row only carried the `R*` conjunct (resistance-route precommitment) through to a schema field.
HU-2 (build_now) supplies the remaining conjuncts, confirmed absent from
`schema/problem_card.schema.json`'s `intake` object and `methodology/P02_intake.md` by direct grep
(zero hits for `unresolved`, `change_condition`, `verification_intent`, `resistance_route`,
`candidate`, `K_like`):

- **New sub-object:** `intake.entry_anchor: {unresolved (U_0), existing_evidence (E_0),
  change_condition (Φ_0), verification_intent (V_0), resistance_route (R*)}` — all optional,
  human-authored, `blackbox_line_ref`-backed like `q1_issue`/`q2_user_proposal`; never
  silently AI-backfilled (mirrors the existing `q2_user_proposal` "none" precedent,
  `schema/problem_card.schema.json:35-38`).
- **`C_0` (candidate contract)** is deliberately *not* a schema field: `v7.1:355` defines it as
  the human's standing acceptance that AI output begins as `K_like`, not certified knowledge — a
  disposition, not a fact to record per-intake, so it stays documentation-only in
  `methodology/P02_intake.md`, not a schema slot.
- **Failing control:** MUST fire — an intake with a stated prior model (`q2_user_proposal` present)
  but no `entry_anchor.change_condition` — nothing today distinguishes a fixed belief from an open
  one at the schema level. MUST NOT fire — `entry_anchor.change_condition: "none stated —
  exploratory"` (explicit honest-optional, not silently inferred).
- **§2.1 merge:** the Session object's `entry_anchor (H0)` row is now understood as this full
  five-sub-field block plus the pre-existing `R*`/`resistance_precommit` row, not `R*` alone —
  update the field's citation to also carry `v7.1:344` (`H_0 = (P_0, M_0, U_0, E_0, Φ_0)`) and
  `:351` alongside the existing `schema.entry-resistance-precommit-field` citation.
- **Forward-only**, per the retroactivity pattern in `design/MEETING_2026-09-05_uplift.md §5.3` —
  same default as §7 founder decision 4 for SA-3's fields, kept consistent across both proposals.

### 11.3 HU-5 — P01 completeness-prompt boundary (build_now)

- **Real gap:** `methodology/P01_standpoint.md:34-36` genuinely leaves the AI's completeness-prompting
  scope open-ended (a single "(e.g. ...)" example, no closed list), confirmed by direct read.
- **Build:** replace the open example with an enumerated, bounded prompt list (`Dr` tier, drafted
  from existing `declared_basis`/`disciplines_not_claimed` use cases already in repo claim cards).
  No schema change required — `ai_filled.*`'s existing disclosure shape
  (`design/FOUNDATION_v0.6.md:721,878`) already covers it; this closes the one channel that
  discipline does not yet cover (AI-*posed prompts*, not just AI-*filled answers*), extending
  `NC-58` (`methodology/data/non_collapse_table.json:586,590`,
  AIContribution≠EpistemicResponsibility) by the same logic.
- **Failing control:** MUST fire — an AI session prompting with a question outside the bounded set,
  unless logged `ai_filled.prompt_source: freeform` (disclosed, not silently treated as equivalent
  to a named prompt). MUST NOT fire — a prompt matching one of the named bounded items verbatim.
- **Provenance note:** this is a corrected resubmission of an earlier same-day draft refuted for
  citing a fabricated `C6/C10 (EPISTEMIC_FUSION)` id (`design/MEETING_2026-09-05_judged.json:128-137`);
  the correction — citing `NC-58` directly — is exactly what that ruling's own revision instruction
  asked for, and this is the pattern §1b item 8 and §9.2's HU-5 row both point at as "raise the
  work, don't lower the claim" done correctly.

### 11.4 HU-3 / HU-4 — still-open / build-with-revision, raise-path only (no softened claim)

- **HU-3 (still_open):** session-close retention-direction note gated to an independent-check
  field. Kept at full claim strength (no free-text expansion/tunnel classification without a
  linked independent check) — this is the same NC-77 discipline as §4/§9.4, applied to the
  Blackbox Note's own `cooking[]` log rather than `hypothesis_selection.yaml` directly. Raise-path
  (§9.2): fix the fabricated `hypothesis_selection.schema.json:1` citation to the real `required[]`
  array at line 7; re-cite the defeater from `v8.1:359-361` (Repair 8's actual expansion/tunnel
  sign clause) instead of the unrelated `:362-365` AUG/SYN/RET passage; and explicitly gate
  `build_path` as blocked on `session.boundary-blackbox-note` (SA-1, §8) landing before the
  acceptance test can run on real multi-session data.
- **HU-4 (build-with-revision):** `claim_card.schema.json` gains an optional `problem_ref` field
  (mirroring `hypothesis_selection.schema.json`'s existing one) so the advisor packet can trace a
  conversion recommendation back to the human-attributed intake statement that originated it,
  rather than re-litigating question quality at the advisor stage (which would duplicate the
  intake-stage gate already in `methodology/P02_intake.md`). Mechanism and defeater are sound;
  raise-path (§9.2) is citation-only — re-cite all four at their real lines with genuine continuous
  excerpts, not synthesized/aggregated field lists.

---

## 12. Sim fixtures — extends §5

Additive to §5's five fixtures (no renumbering):

| defect class | source proposal | fixture sketch |
|---|---|---|
| `question_trace_gap` | `schema.blackbox-question-trace` | A Blackbox Note with 2 `question`-kind lines (n=1, n=5) and 0 `question_trace` entries → coverage-check extension to `tools/blackbox_log.py` must report 1:1 coverage failure; add two `question_trace` rows referencing n=1/n=5 → must confirm full coverage (or an explicit `derived_from_line: null` marking a genuinely fresh question). |
| `candidate_forgotten_unrecorded` | `schema.blackbox-line-origin-enum` | Fixture A: line n=7 `ai_proposed_pending` → `became[claim_card cc-042]` with zero intervening `cooking[]` entries referencing n=7 → checker must output `origin=ai_proposed_forgotten`. Fixture B: identical but with one `{step: review, input_lines:[7]}` cooking entry inserted before the `became[]` entry → checker must output `origin=ai_proposed_adopted`. |
| `chooser_reaffirmation_missing` (hsel- scope only, per §9.1 fix) | `schema.blackbox-chooser-reaffirmation` | Fixture A: `became[]` entry naming an `hsel-` id, `chooser_reaffirmed` absent → schema validation FAILS. Fixture B: same entry with `chooser_reaffirmed` populated → PASSES. (Fixture C, the `responsible: human` non-`hsel-` branch, stays `[Open]` until the cross-file validator in §9.1's fix option (b) is built.) |
| `candidate_set_drop_unexplained` | `kernel.candidate-set-delta-cooking-step` | Against the corrected fixture target (`schema/examples/blackbox_note.example.json` or a real `projects/GLS-2026-001_*` instance, per §9.1 fix): (a) unexplained drop (`before:5, after:2`, no naming) → `CANDIDATE-DROP-UNEXPLAINED` fires; (b) explained drop (`what_changed` names the dropped candidates) → does not fire; (c) growth/steady-state (`after >= before`) → never flagged. |
| `dialogue_table_stance_without_defeater` | `lrs.dialogue-table-claim-type-column` | A `dialogue_table.md` row with `agrees with H = YES` and `defeater_class`/`legitimate_defeater` blank → header-anchored grep + row-completeness pytest fixture must flag `INCOMPLETE`. A row with both columns filled from the five-way enum → passes. |
| `defeater_log_untyped_entry` | `lrs.defeater-defeated-status-field` | `provenance_dag.defeater_log: [{"node":"n1"}]` (missing `date`/`outcome`) → `jsonschema.validate()` raises. `[{"node":"n1","date":"2026-09-05","outcome":"claim_survived"}]` → passes. |
| `strength_of_claim_defeater` | `lrs.defeater-not-collapse-rule` | `tested.falsifier: "the claim is simply too strong to be wrong"` → kernel rule29 error. `tested.falsifier: "defeated by a documented case where retained_direction is negative across 3 consecutive turns"` → no error. |
| `defeater_class_style_mismatch` | `lrs.claim-type-defeater-enum` | `defeater_class: EMPIRICAL` + phenomenological-style absence falsifier → rule30 error (category mismatch). `defeater_class: EMPIRICAL` + replication-style falsifier → passes. `defeater_class: PHENOMENOLOGICAL` + absence-style falsifier → passes. |
| `mastery_gate_unlinked` | `HU-1` | A non-Paper-genre L3+ claim card with no linked `human_mastery_gate.yaml` → R8 fails `BLOCKED: NO_MASTERY_GATE_LINKED`. A Paper-genre claim card using the arxiv template with `Gate status: PASS` filled → R8 passes. |
| `entry_anchor_change_condition_missing` | `HU-2` | An intake with `q2_user_proposal` present (a stated prior model) but `entry_anchor.change_condition` absent — scan reports the fraction of instances leaving each of the five sub-fields at the honest "not stated" value, never silently backfilled. `entry_anchor.change_condition: "none stated — exploratory"` is a valid, non-flagged honest-optional entry. |
| `completeness_prompt_outside_bounded_set` | `HU-5` | A Blackbox Note `cooking[]` entry tagged `step: lens_in` during standpoint capture, with an AI-authored prompt not drawn from `P01_standpoint.md`'s new bounded list and no `ai_filled.prompt_source: freeform` flag → flagged. A prompt matching one of the named bounded items, or correctly flagged `freeform` → passes. |

`kernel.candidate-set-delta-cooking-step`'s and `schema.blackbox-language-bridge-subfield`'s own
originally-proposed fixtures are folded into the rows above (former) or dropped with the proposal
(latter, per §9.1 — no fixture is added for a still-open, self-defeated proposal).

---

## 13. DAG_v0.4 node YAML — additions (extends §8's block, additive, no renumbering)

Per §10's filing note, none of the four `lrs-defeaters` proposals below get a live
`design/DAG_v0.3.yaml` node yet — they are filed today as one `design/TODO_v0.3.md` line
(`lrs.dr-tag-not-dag-node`, build_now). The stubs below are the *post-decision* shape, to be added
to `design/DAG_v0.4.yaml` only once each has an approved `cpg/research/coordination/DECISIONS.yaml`
row, per that proposal's own control.

```yaml
# design/DAG_v0.4.yaml (Part 2 additions — additive to §8's block and to DAG_v0.3.yaml, no
# renumbering of existing nodes)

- id: schema.blackbox-question-trace
  status: build_now
  target: schema/blackbox_note.schema.json (new top-level optional question_trace[])
  claim_correction_required: "drop the 'glosa's own Human Return Test' misattribution before ship (§9.1)"
  acceptance_test: "coverage-check extension to tools/blackbox_log.py: every lines[].kind==question line has a question_trace entry (or explicit derived_from_line: null)"
  citations: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:124, ':129, ':467, design/FOUNDATION_v0.6.md:495]
  founder_decision_needed: false

- id: schema.blackbox-line-origin-enum
  status: with_revision
  revision_needed:
    - "failing_control's cross-file claim_card creation-timestamp check is unusable; replace with same-document cooking[]/became[] ordering (§9.1)"
  target: schema/blackbox_note.schema.json lines[].origin enum (replaces ai_proposed boolean, deprecated alias kept one cycle)
  founder_decision_needed: true   # changes founder-visible disclosure semantics

- id: kernel.candidate-set-delta-cooking-step
  status: with_revision
  revision_needed:
    - "retarget acceptance_test fixture to schema/examples/blackbox_note.example.json or a real projects/GLS-2026-001_* instance (§9.1)"
    - "build new checker tooling; tools/blackbox_log.py is the wrong target (founder's daily voice-log BBL tool, unrelated)"
  target: schema/blackbox_note.schema.json cooking.items.candidate_set; FOUNDATION_v0.6.md §3.3 flag-rule29 (own namespace, see §10 header note — not kernel/glosa_kernel.py rule29)
  founder_decision_needed: false

- id: schema.blackbox-chooser-reaffirmation
  status: with_revision
  revision_needed:
    - "scope to became[] targets matching ^hsel- only for the build_now half, or design the cross-file responsible:human validator before claiming that half ready (§9.1)"
  target: schema/blackbox_note.schema.json lines[].became[].chooser_reaffirmed
  founder_decision_needed: true

- id: schema.blackbox-language-bridge-subfield
  status: still_open
  disposition: "already adjudicated keep:false in design/MEETING_2026-09-05_judged.json:84-92; withdraw per its own stated defeat condition unless founder overrules that standing ruling"
  founder_decision_needed: true

- id: hu.mastery-gate-wired
  status: build_now
  target:
    - methodology/P16_human_mastery_gate.md (new)
    - schema/human_mastery_gate.schema.json (new)
    - methodology/P10_publish_gate.md (new R8)
    - design/FOUNDATION_v0.6.md §7.5 (fix broken v0.1 pointer)
  acceptance_test: "Paper-genre artifact with Gate status PASS -> R8 passes; non-Paper L3+ artifact with no linked gate -> R8 BLOCKED: NO_MASTERY_GATE_LINKED"
  citations: [design/FOUNDATION_v0.6.md:1619, ':1621, templates/paper/arxiv-twocol/main.tex:375, ':378, methodology/data/non_collapse_table.json:570, ':620, methodology/P10_publish_gate.md:17, ':32]
  founder_decision_needed: true

- id: schema.entry-anchor-full-h0
  status: build_now
  target: schema/problem_card.schema.json intake.entry_anchor {unresolved, existing_evidence, change_condition, verification_intent, resistance_route}
  merges_with: schema.entry-resistance-precommit-field (§8 — R* conjunct only; this supplies U0/E0/Φ0/V0)
  acceptance_test: "schema validation passes with entry_anchor present; scan of N problem_card.yaml instances reports fraction of each sub-field filled vs. honest not-stated, never AI-backfilled"
  citations: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:344, ':351, ':355, ':356, schema/problem_card.schema.json:12]
  founder_decision_needed: true   # retroactive vs forward-only, same call as §7.4

- id: methodology.p01-bounded-completeness-prompt
  status: build_now
  target: methodology/P01_standpoint.md (enumerated bounded prompt list, replaces single e.g. example)
  acceptance_test: "grep confirms enumerated closed list; Blackbox Note cooking-log scan confirms every AI-authored lens_in prompt matches the list or is flagged ai_filled.prompt_source: freeform"
  citations: [methodology/P01_standpoint.md:34, ':35, ':36, methodology/data/non_collapse_table.json:586, ':590]
  founder_decision_needed: false

- id: hu.advisor-problem-ref-trace
  status: with_revision
  revision_needed:
    - "re-cite all 4 citations at their real lines with genuine continuous verbatim (§9.2): claim_card.schema.json required[] line 9; hypothesis_selection.schema.json problem_ref line 11/required line 7; advisor_prompt_packet.md line 31; problem_card.schema.json retained_difference_statement line 22"
  target: schema/claim_card.schema.json (new optional problem_ref); templates/knowledge/advisor_prompt_packet.md §1 (new step 1a, BLOCKED: NO_PROBLEM_REF)
  founder_decision_needed: false

- id: hu.retention-note-independent-check-gate
  status: still_open
  blocking_defect:
    - "citation hypothesis_selection.schema.json:1 is fabricated; real required[] array is at line 7 (§9.2)"
    - "legitimate_defeater cites the wrong v8.1 passage (:362-365 AUG/SYN/RET, not :359-361 expansion/tunnel sign)"
    - "failing_control needs session_id grouping key not yet built; blocked on session.boundary-blackbox-note (SA-1)"
  founder_decision_needed: true

- id: lrs.dialogue-table-defeater-class-column
  status: build_now
  target: templates/knowledge/dialogue_table.md (new columns defeater_class, legitimate_defeater); design/S14_literature-review-system.md §3.4
  claim_correction_required: "sync claim_as_stated to name defeater_class, not claim_type, before v0.4 lock (§9.3)"
  acceptance_test: "header-anchored grep confirms both new columns; pytest row-completeness fixture fails a populated-stance row missing either column"
  citations: [sources/notes/EPISTEMIC_FUSION_v8.1.txt:30, ':44, design/S14_literature-review-system.md:210, kernel/glosa_kernel.py:643]
  founder_decision_needed: false

- id: lrs.defeater-log-required-outcome-enum
  status: build_now
  target: schema/claim_card.schema.json provenance_dag.defeater_log items (required:[node,date,outcome], outcome enum)
  acceptance_test: "jsonschema validate() raises on {node} alone; passes on {node,date,outcome:claim_survived}"
  citations: [design/FOUNDATION_v0.6.md:775, schema/claim_card.schema.json:437, ':439]
  founder_decision_needed: false

- id: kernel.rule29-strength-of-claim-not-defeater
  status: build_now
  namespace_note: "kernel/glosa_kernel.py python-rule sequence — distinct from FOUNDATION_v0.6.md §3.3 flag-rule29 used by kernel.candidate-set-delta-cooking-step above (§10 header note)"
  target: kernel/glosa_kernel.py (new rule29); methodology/data/non_defeater_phrase_table.json (new)
  acceptance_test: "falsifier='the claim is simply too strong to be wrong' -> rule29 error; falsifier='defeated by a documented case where retained_direction is negative across 3 consecutive turns' -> no error"
  citations: [sources/notes/EPISTEMIC_FUSION_v8.1.txt:51, ':53]
  founder_decision_needed: false

- id: kernel.rule30-defeater-class-phrasing-match
  status: build_now
  namespace_note: "kernel/glosa_kernel.py python-rule sequence, next free after rule29 above"
  target: schema/claim_card.schema.json five_questions.tested.defeater_class (new, sibling of claim_type not an extension — schema/common.defs.json:154-165); kernel/glosa_kernel.py (new rule30)
  acceptance_test: "defeater_class=EMPIRICAL + phenomenological-style falsifier -> rule30 error; + replication-style falsifier -> pass; defeater_class=PHENOMENOLOGICAL + absence-style falsifier -> pass"
  citations: [schema/common.defs.json:154, schema/claim_card.schema.json:94, sources/notes/EPISTEMIC_FUSION_v8.1.txt:44, ':45, ':53, ':54]
  founder_decision_needed: true
```
