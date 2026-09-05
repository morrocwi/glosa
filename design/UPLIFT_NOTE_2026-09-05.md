# Uplift Note 2026-09-05 — 25 proposals from the Epistemic Fusion papers to glosa: what was wrong, what was fixed, what stands

Tier of this whole note: `Dr` (design synthesis / editorial reconciliation of prior reviews, not
itself a new independent check). No `Th_coqc` claim is made anywhere below. No novelty/first/prior-art
language. Comparisons are same/different/cited only.

---

## สรุปภาษาไทย (10 บรรทัด)

1. เอกสารนี้รวบรวมข้อเสนอทั้ง 25 ข้อจากการประชุม 2026-09-05 ที่นำแนวคิดจากเปเปอร์ Epistemic Fusion (v7.1/v8.1) เข้ามาสู่ glosa — ไม่ตัดทิ้งข้อไหน แม้จะถูกปฏิเสธในรอบแรก
2. รอบแรก (`MEETING_2026-09-05_judged.json`) เก็บไว้เพียง 4/25 ข้อ เพราะผู้เสนอ 21 ข้อที่เหลืออ้าง id ปลอม "C1–C11" ราวกับเป็น claim card จริง — grep แล้วไม่พบ id แบบนี้ในไฟล์ต้นฉบับเลย
3. ไฟล์ต้นฉบับจริงเลข F1–F20 (v7.1) และหัวข้อ "Problem n"/"Repair n" (v8.1) เท่านั้น — "C1–C8" กลับเป็น namespace ที่ glosa เองใช้อยู่แล้วสำหรับ chair ruling คนละเรื่อง เกิดการชนกันโดยตรง ผิดกฎ 17
4. คำสั่ง founder (BBL-2026-09-05-119): ห้ามลดคำกล่าวอ้างให้ผ่าน ต้อง "ยกงานขึ้น" แทน — แก้เลขบรรทัด อ้างของจริง เปิดเผยช่องว่างที่แท้จริง ไม่ปิดเงียบ
5. รอบสอง (`SESSION_ARCH_v0.4_rejudged.json` + `_SPEC.md`) ตรวจใหม่ทุกข้อด้วย citation แบบ file:line จริง ได้ผล: build_now 13 · with_revision 7 · still_open 4 จาก 24 ข้อ (ข้อ SA-5 หายไปจากการส่งต่อที่ตัดตอน)
6. SA-5 (K_like state-machine citation) ถูกสืบหาใหม่ในโน้ตนี้เอง — grep พบตำแหน่งจริงใน EPISTEMIC_FUSION v7.1/v8.1 ครบ แต่เป้าหมายเดิม (§7.3) ผิดหัวข้อ ต้องแก้เป็น §4.4 เท่านั้น
7. SA-5 ยังไม่ผ่านการตรวจสองรอบอิสระเหมือนอีก 24 ข้อ (ตรวจโดย AI ผู้ร่างเอกสารนี้เอง = maker ตรวจงานตัวเอง ไม่นับเป็น checker ตามกฎข้อ 3 ของ glosa) — จึงจัดสถานะ with_revision ไม่ใช่ build_now
8. รวมทั้งหมด 25 ข้อ: build_now 13 · with_revision 8 (รวม SA-5) · still_open 4
9. พบ namespace collision จริง 2 จุด: (ก) "C1–C8" ของ chair ruling ชนกับ id ปลอมที่ผู้เสนอใช้ (ข) เลข kernel rule 29 ใน `kernel/glosa_kernel.py` ชนกับเลข flag-rule 29 ใน `FOUNDATION_v0.6.md` §3.3 คนละไฟล์คนละความหมาย ต้องเขียนแยกชื่อเต็มเสมอ
10. เอกสารนี้เองมีข้อจำกัด: ไม่ได้ re-verify citation ทั้ง 24 ข้อจากไฟล์ต้นฉบับซ้ำอีกรอบ (อาศัยการตรวจของรอบสอง + สุ่มตรวจเอง) และยังไม่ผ่าน adversarial review อิสระก่อนแนบเข้า Zenodo — ต้องผ่าน gate นั้นก่อนเผยแพร่จริง

---

## Status

- **K-state:** `K0` (private candidate — this note has not been reviewed by anyone but the AI that
  drafted it and one direct-read spot-check pass by the same session; it is not `K1` until a human
  timestamps/publishes it, and not socially stress-tested until an independent reviewer runs a
  second pass per glosa rule 3).
- **Tier:** `Dr` throughout, with per-row tiers as inherited from `SESSION_ARCH_v0.4_rejudged.json`
  (`Dr`/`finite_diagnostic`/`Open`, never `Th_coqc`) — see §2 table.
- **Novelty:** none claimed. This note re-anchors and reconciles existing review artifacts; it
  introduces no new mechanism except the SA-5 re-anchoring in §2, which is itself only a citation
  correction to an existing named target (`design/FOUNDATION_v0.6.md` §4.4).
- **Human owner:** Yaoharee Lahtee. The problem, the hypothesis-selection, and every founder
  decision named in §2/§7 of `SESSION_ARCH_v0.4_SPEC.md` remain human-owned; nothing here
  substitutes for that.
- **AI role:** drafted as assistant only. This note is a compilation/reconciliation pass, not a
  certification of any row's readiness — "build_now" below is the *reconciled reviewer verdict*
  carried over from `SESSION_ARCH_v0.4_rejudged.json`, not a release decision. Per glosa rule 8,
  no independent check ⇒ no release: none of the 25 rows are released by this note; each still
  needs its own `DECISIONS.yaml` row and, where flagged, a founder ruling before build.
- **Attribution:** no vendor/model name anywhere in this note or intended for the Zenodo record,
  per glosa rule 9 and `CLAUDE.md`'s binding instruction; AI involvement is disclosed by role only.

---

## 1. What happened

**Round 1** (`design/MEETING_2026-09-05_judged.json`, 25 rows) kept only 4 proposals
(`lrs.dr-tag-not-dag-node` 8.0, `HU-3` 6.5, `SA-2` 6.0, `SA-4` 5.0) and refuted the other 21. The
dominant refutation reason across those 21 was **citation fabrication**: proposers cited claim-card
ids such as `"C1"`, `"C2"`, `"C4"`, `"C5"`, `"C6"`, `"C7"`, `"C8"`, `"C9"`, `"C10"` as if these were
established evidence-card identifiers inside `sources/notes/EPISTEMIC_FUSION_v7.1.txt` /
`EPISTEMIC_FUSION_v8.1.txt`. A direct grep run this pass confirms, again, that no such scheme
exists in either source file:

```
grep -n "^C[0-9]" sources/notes/EPISTEMIC_FUSION_v7.1.txt sources/notes/EPISTEMIC_FUSION_v8.1.txt
→ zero hits in either file
```

The source papers number findings `F1`–`F20` (v7.1) or leave formulas/problems unlabeled under
prose headings like "Problem 1", "Repair 8" (v8.1) — never `C`-anything. Worse, `"C1"`–`"C8"` is
**already a live glosa id namespace**: `design/CHAIR_RULING_v1.md:23-30` uses `C1`..`C8` for chair
rulings on `independence_class`, the disclaimer catalogue, `fetch_status`, `verdict_tier`,
`review_mode`, non-collapse rows, lineage table, and `origin_blackbox_ref` — none of which is what
any proposer meant. Citing "C4"/"C5"/"C7"/"C8" for session-architecture content therefore collided
with an existing, unrelated meaning under Rule 17 (file:line + continuous verbatim citation).

**Founder ruling BBL-2026-09-05-119** ("never lower a claim to make it pass — raise the work") set
the correction discipline: every fabricated or off-by-N citation gets replaced by its real
file:line location, every genuinely weak mechanism gets its acceptance test tightened or its gap
disclosed honestly, and no row is quietly dropped to shrink the problem.

**Round 2** (`design/SESSION_ARCH_v0.4_rejudged.json`, 24 rows + `design/SESSION_ARCH_v0.4_SPEC.md`)
re-anchored every citation to file:line with continuous verbatim text and re-ran the same
`citations_verified && control_mechanical && invariant_ok && score>=6 → build_now` rule (one
fixable defect → `with_revision`; a scope/mechanism conflict → `still_open`). Result: **13
build_now, 7 with_revision, 4 still_open** out of 24. **One proposal, `SA-5`, is absent from that
24-row file** — per `CLAUDE.md` rule 10 (added this same day, Blackbox Log BBL-2026-09-05-121,
"No finding is ever dropped... after one proposal (SA-5) fell out of a re-anchoring pass through a
truncated hand-off"), this is the exact incident that rule exists to name. §2 below re-anchors
SA-5 directly against the source files, so this note's own table restores the full count of 25 and
does not repeat the drop.

---

## 2. All 25 proposals

Columns: **claim as stated** is carried verbatim/near-verbatim from the proposal, unchanged by this
note. **What was wrong (r1)** names the round-1 defect. **Correction** gives the real file:line and
a verbatim excerpt (≤25 words) that replaces the fabricated citation. **Status now** is the
round-2 reconciled verdict (`build_now` / `with_revision` / `still_open`), from
`SESSION_ARCH_v0.4_SPEC.md` §3/§9, except `SA-5` which this note re-anchors directly (marked
below) and holds at `with_revision` pending an independent second check, per glosa rule 3.

| id | lens | claim as stated (unchanged) | what was wrong (r1) | correction (file:line, verbatim ≤25 words) | legitimate defeater | failing control | status now | build path |
|---|---|---|---|---|---|---|---|---|
| SA-1 | session-architecture | Session has a nameable boundary where AI-side momentum resets to zero by scope-definition; human-retained residue may alter the next session's start state; Blackbox Note should carry this. | Cited fabricated "C4"/"C5" for the reset/asymmetry claim — no such ids exist. | v7.1:490 "session boundary in the human, because AI-side momentum is reset by definition in this arc..."; v7.1:493 F10 "Reciprocal momentum is session-bounded." | Structural/definitional claim; defeated only by a demonstrated glosa mechanism already recording per-session AI-state reset without this field. | Two Blackbox Notes sharing one `session_id`, split by a real process restart — `ai_state_at_boundary: reset` must be present in both or schema validation fails. | **build_now** | `templates/knowledge/blackbox_note.yaml` + `schema/blackbox_note.schema.json` (session_id/opened_at/closed_at/ai_state_at_boundary/human_retained_residue_ref) + `FOUNDATION_v0.6.md` §2.3 |
| schema.entry-resistance-precommit-field | kernel-gates | Precommitted resistance-route field (R*) at claim-card intake, flag-not-block, declared before the AI candidate exists. | Cited fabricated "C2"/"C5" — no such ids exist anywhere in glosa. | v7.1:351 "ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*"; v7.1:356 "R* — precommitted resistance route: specify how..." | Structural/formal proposal; defeated if incoherent, redundant, or non-identifiable per v8.1 §1. | Problem Card at S1 with `precommitted_resistance_route` null and `readiness.verdict=READY_FOR_S2` → flagged (not blocked). | **build_now** | `schema/problem_card.schema.json` `intake.precommitted_resistance_route` (string) + new flag `D-NO-PRECOMMIT-ROUTE` |
| kernel.reciprocal-lineage-diagnostic | kernel-gates | Reciprocal-lineage diagnostic (χ_recip) over kg edges, diagnostic-only, using session_id/actor/timestamp fields. | Cited fabricated "C7"/"C8" — these are glosa's own unrelated chair-ruling ids. | v7.1:447 "chi_recip[s,L]: How many readout-distinguishable reciprocal descendants..."; v7.1:496 "cannot be read as warrant, truth, or human benefit." | Diagnostic; defeated if not codeable reproducibly or unstable under reasonable segmentation/horizon choices. | kg edges sharing one `session_id`, same lineage traversed by human- and AI-asserted edges — χ_recip must be computable, reproducible across two horizon settings, else "not computable" (never a numeric default). | **build_now** (tier honestly `Open`, not `Dr`, until fixtures run) | new `session_id` field on `schema/kg_edge.schema.json`; new CLI `glosa kg diagnose --chi-recip`; sim fixture before any tier upgrade |
| schema.retention-direction-field | kernel-gates | Retention-direction field (expansion/tunnel/undetermined) on the hypothesis-selection ledger, so persistence alone is never read as validation. | Cited fabricated "C9" and a nonexistent "K1→K2 conversion ledger" target. | v8.1:345,347 "Gs = g(...)", "Ts = h(...), Δs = Gs − Ts"; `FOUNDATION_v0.6.md`:2255-2256 NC-32/NC-34 pattern precedent. | Structural/formal; defeated if redundant with an existing field or adds no explanatory/predictive information. | `hypothesis_selection.yaml` row `chosen` across ≥2 sessions with no linked independent-check artifact → must render `retained_direction: unknown`, never a bare pass. | **build_now** | `retained_direction` enum on `schema/hypothesis_selection.schema.json`; disclaimer `D-RETENTION-DIRECTION`; Appendix A row **NC-77** |
| SA-4 | session-architecture | glosa explicitly declines, and logs the decline, to add `chi_recip`/`m^H`/`m^AI` as schema fields now, because no multi-turn evidence mechanism exists and both diagnostics carry self-defeat clauses. | Kept in r1, but reasons flagged reusing glosa's own "C7"/"C8" chair-ruling ids for the source cards. | v7.1:550 "Remove m^{AI}_{s,t}... if within-session path history adds no effect"; v7.1:554 "Drop chi_recip[s,L]... if lineage-linked reciprocal descendants cannot..." | Non-adoption/scope-boundary claim; defeated only by glosa actually building a multi-turn/dialogue-history evidence mechanism (the proposal's own named `revisit_condition`). | Any future PR adding `chi_recip`/`m^H`/`m^AI` (or an equivalent renamed field) before that mechanism exists must fail review. | **with_revision** | the internal command-center's DECISIONS ledger (private) row, `status: RECORDED` (not the non-existent `DECLINED-FOR-NOW` value) — 3 line-number fixes + drop 1 irrelevant citation |
| SA-3 | session-architecture | Human's problem statement, prior model, and verification intent must be captured before first AI exposure, matching v8.1's Fogliato-defeater finding. | Cited fabricated "C5"; also conflated S1 Problem Card with S2 Observation Card as one target. | v8.1:132 "Problem 1 - AI Arrives Before a Human [Baseline Exists]"; v7.1:351 `ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*`. | Process-sequencing-plus-content claim; defeated by showing the content fields are already captured elsewhere (e.g. Blackbox Note's own speaker/timestamp fields). | Problem Card whose linked Blackbox Note shows the first AI-speaker line before any human-speaker line, or whose three new fields are absent, must fail. | **with_revision** | `schema/problem_card.schema.json` (3 new required fields), single named schema file only — add the timestamp cross-check script the acceptance test itself requires |
| process.run-existing-open-falsifier-klike | kernel-gates | Run the falsifier test the DAG already deferred (`rule17.claim-card-certification-open`) — no new mechanism, close the existing `[Open]` item. | Cited fabricated "C6"/"C10" as candidate evidence ids. | `design/DAG_v0.3.yaml:78` (corrected from a mis-cited `:76`) — node `rule17.claim-card-certification-open`, status `deferred`. | Empirical claim (v8.1 §1: causal/quantitative/universal claims); defeated by sufficiently strong contrary evidence from the sim run itself. | 30% injected undisclosed `ai_filled` in a synthetic claim-card batch → same-vendor vs cross-vendor catch-rate comparison must run, plus a zero-injection negative control reporting 0/0. | **with_revision** | `methodology/H3_falsifier_sim.py` (new); row must also disclose `design/TODO_v0.3.md` carries no matching `[Open]` line today |
| SA-2 | session-architecture | Retention/persistence of a claim or habit across sessions is never by itself evidence of expansion vs. tunnel; only an independent check may reclassify it. Default: `retained_direction: unknown`. | Kept in r1, but cited fabricated "C3"/"C9" for the direction-neutrality claim. | v8.1:358-359 "ηs > 0, ∆s > 0 ⇒ durable expansion; ηs > 0, ∆s < 0 ⇒ durable epistemic tunnel." (verified 1-line off at `FOUNDATION_v0.6.md`:2254→2256). | Direction-classification claim; defeated only by a linked independent-check artifact establishing the sign of Δs directly — never by persistence/engagement signals (v8.1:361). | `hypothesis_selection.yaml` row `chosen` across ≥2 sessions, no `evidence_relation` → forced `unknown`; a row with a resolvable checker verdict may carry the verdict's own sign. | **still_open** | Blocked on `session.boundary-blackbox-note` (SA-1) landing session_id before the scan can run on real multi-session data — currently only trivially true for single-session rows |
| kernel.session-boundary-momentum-reset-assertion | kernel-gates | Session-boundary AI-momentum reset assertion, mechanical and CI-checkable. | Cited "C1"-style ids that misread every source they pointed at. | v7.1:328 "m^{AI}_{s+1,0} = 0 (by architectural scope definition)"; v7.1:497 F12 cross-session persistence asymmetry. | Constitutive/scope claim; defeated by internal inconsistency or a documented case where AI-side state legitimately survives a boundary. | Two Blackbox Notes sharing a `session_ref` split by a tool restart, second file's `ai_state_at_boundary` missing/non-literal → reject. | **still_open** (duplicate) | Merge into `session.boundary-blackbox-note` (SA-1) — same fields, same defeater, originally pointed at the wrong FOUNDATION section (§2.3 R0/R1/R2 instead of Blackbox Note) |
| schema.blackbox-question-trace | blackbox-dialogue | Blackbox Note records a question only twice (single-shot); no field records how the live question changed turn-to-turn. | Cited "C1 P1/P2"/"C5" that don't say what the proposal claims. | v7.1:129 "Q_H,t ⟶(T_AI) {Q_i,t+1, K_like_i,t}"; v7.1:467 "What is my next question, and why is it better formed than the previous one?" | Structural-coverage claim; defeated by evidence per-turn question evolution is already captured elsewhere. | Blackbox Note with two `kind:question` lines and zero `question_trace` entries → coverage-check must fail; entries added → must pass. | **build_now** | New top-level optional `question_trace[]` on `schema/blackbox_note.schema.json`; drop the false "glosa's own Human Return Test" framing before ship |
| schema.blackbox-line-origin-enum | blackbox-dialogue | Bare boolean `ai_proposed` cannot represent the named transition hazard — `K_like` silently upgraded to `K_assumed`. | Cited "C2"/"C6"/"C10" — none exist. | v7.1:364 "AI(Q) = K_like, K_like ≠ K_validated"; v7.1:485 F6 "Candidate forgetting is a central transition hazard. When K_like is silently upgraded..." | Representational-insufficiency claim; defeated by showing the boolean plus an existing field already distinguishes the hazard. | Line `ai_proposed:true` later gaining a `became[]` entry with zero intervening `cooking[]` reference → must resolve `ai_proposed_forgotten`; one `review`-step entry present → `ai_proposed_adopted`. | **with_revision** | `lines[].origin` enum (replaces boolean, deprecated alias kept 1 cycle); replace the cross-file timestamp check with same-document `cooking[]`/`became[]` ordering |
| kernel.candidate-set-delta-cooking-step | blackbox-dialogue | Cooking log records a step happened but not the candidate-set growth/collapse count the same discipline demands elsewhere. | Cited "C3"/"C9" that grep confirms do not exist anywhere in glosa. | v7.1:417 "k_s — candidate multiplication generated during the session..."; v7.1:446 "The architecture therefore separates three questions that must not collapse:" | Mechanism-shape claim; defeated by showing a verdict is being smuggled in via the count rather than kept as an additive, non-collapsing field. | `{step: analysis, candidate_set:{before:5, after:2}}` with no naming of what changed → `CANDIDATE-DROP-UNEXPLAINED` fires; growth/steady-state never flags. | **with_revision** | `cooking.items.candidate_set` field; retarget acceptance-test fixture (real repo instance, not a prose-only Appendix pointer) and build new checker tooling (not `tools/blackbox_log.py`, the founder's unrelated daily-log tool) |
| schema.blackbox-chooser-reaffirmation | blackbox-dialogue | `became[]` link records that a candidate became something, but not whether the human who holds non-delegable selection authority reaffirmed it at reopen. | Citations misread their sources (chair C4/C7-style reuse). | v7.1:368 "K_like → K_assumed (validation bypass)"; `FOUNDATION_v0.6.md`:429 S3c Hypothesis selection row (non-delegable, `responsible: human`). | Missing-authority-check claim; defeated by evidence the reaffirmation is already captured elsewhere. | `became[]` entry naming an `hsel-` id with `chooser_reaffirmed` absent → schema validation fails; populated → passes. | **with_revision** | `became[].chooser_reaffirmed` sub-field; scope the mandatory half to `^hsel-` ids only, or design the cross-file `responsible:human` validator before claiming the wider trigger ready |
| schema.blackbox-language-bridge-subfield | blackbox-dialogue | `translation`-step cooking entries conflate a bilingual TH/EN rewrite with a world↔readout lens translation glosa's own text already distinguishes. | Citations checked out structurally but the underlying "unresolved seam" premise was itself a misread of already-specified content. | `MEETING_2026-09-05_judged.json`:84-92 — same id/title/target already adjudicated `keep:false`, score 4.5, "a misread of already-specified glosa content." | Specification-gap claim; the proposal's own defeat condition already fired and was missed by round 2's re-anchoring search (which never checked `MEETING_2026-09-05_judged.json`). | A cooking entry `{step:"translation", ...}` with no `bridge_kind` — moot, since the premise itself is refuted. | **still_open** | Withdraw per its own stated defeat condition; only a founder overrule of the standing chair ruling could revive it |
| HU-1 | human-uplift | Write the missing Human Mastery Gate protocol card — §7.5 currently points at nothing. | Cited fabricated ids claiming the mechanism was entirely missing. | `FOUNDATION_v0.6.md`:1619,1621 "### 7.5 Human Mastery Gate / Unchanged from v0.1 §7.5" — no `FOUNDATION_v0.1.md` exists; `templates/paper/arxiv-twocol/main.tex`:375-378 (real 10-question checklist). | Buildability/gap-existence claim; defeated by a located artifact already performing the wiring claimed missing. | Non-Paper-genre L3+ claim card with no `human_mastery_gate.yaml` linked, passing R1-R7 clean → must now return `BLOCKED: NO_MASTERY_GATE_LINKED` at new R8. | **build_now** | `methodology/P16_human_mastery_gate.md` (new, genre-independent); `schema/human_mastery_gate.schema.json`; new R8 on `methodology/P10_publish_gate.md`; fix the broken v0.1 pointer |
| HU-2 | human-uplift | Add an entry-anchor block (H0-style) to the intake stage, ahead of first AI exposure. | Cited fabricated "C5" plus an unregistered external FAccT citation the source text doesn't carry. | v7.1:344 "H_0 = (P_0, M_0, U_0, E_0, Φ_0)"; v7.1:351 `ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*`. | Gap-existence claim; defeated by a located field already capturing `E_0` specifically (not incidental prose mentions of "evidence"). | Intake with a stated prior model (`M_0`) but no declared `change_condition` (`Φ_0`) → nothing today distinguishes a fixed belief from an open one. | **build_now** | `intake.entry_anchor {unresolved, existing_evidence, change_condition, verification_intent, resistance_route}` on `schema/problem_card.schema.json`, all optional/human-authored, never AI-backfilled |
| HU-3 | human-uplift | Session-close retention note in the Blackbox Note cooking log — human states direction, not just content, of what was retained. | Kept in r1 (6.5), but cited fabricated "C3"/"C4" for the same direction-neutrality claim as SA-2. | v8.1:359-361 "ηs > 0, ∆s > 0 ⇒ durable expansion; ... ⇒ durable epistemic tunnel" — corrected from a wrongly-cited `:362-365` (a different collapse: AUG/SYN/RET, not expansion/tunnel). | Direction-claim (evaluative); defeated by evidence the proposed positive/negative pattern doesn't hold. | `hypothesis_selection.yaml` row `chosen` across ≥2 sessions with no cooking-log revision-kind `retention_note` → flagged. | **still_open** | Three real defects: fabricated `hypothesis_selection.schema.json:1` citation (real `required[]` at line 7); wrong defeater passage; `build_path` needs a `session_id` grouping key it doesn't have — blocked on SA-1 |
| HU-4 | human-uplift | Advisor packet gains a "question quality" self-check step before recommending conversion actions. | Fabricated citation aggregating field lists that don't exist at the quoted line. | `schema/claim_card.schema.json` `required[]` starts at line 9 (not line 1, which is `{`); `templates/knowledge/advisor_prompt_packet.md`'s "Every `claim_card.json` listed..." line is at line 31, not 27. | Buildability claim; defeated by a located existing field already achieving claim-card-to-intake traceability. | `claim_card.json` with `produced_by: joint`/`ai` whose statement diverges from its `problem_card`'s `retained_difference_statement`, no resolvable `problem_ref` → `BLOCKED: NO_PROBLEM_REF`. | **with_revision** | New optional `problem_ref` on `schema/claim_card.schema.json` — re-cite all 4 citations at their real lines with genuine continuous verbatim, mechanism otherwise sound |
| HU-5 | human-uplift | P01_standpoint's "AI may prompt for completeness" gets a named, bounded question set instead of an open-ended AI judgment call. | Fabricated "C6/C10 (EPISTEMIC_FUSION)" second evidence item. | `methodology/P01_standpoint.md`:34-36 "AI: may prompt for completeness (e.g. ...) but never fills declared_basis..." — real, unbounded text confirmed by direct read. | Buildability/scope claim; defeated if a closed list re-narrows P01's non-delegability further than intended. | AI session prompting with a question outside the bounded set, no `ai_filled.prompt_source: freeform` flag → flagged. | **build_now** | Replace the open `(e.g. ...)` example with an enumerated, bounded prompt list; cites `NC-58` (AIContribution≠EpistemicResponsibility) directly, correctly |
| lrs.dr-tag-not-dag-node | lrs-defeaters | Do not create a new DAG_v0.3 node for the LRS-defeater lens — file as an `[Open]` TODO line instead, pending P09 vetting. | Kept in r1 with the highest score (8.0), no fabrication found. | `design/DAG_v0.3.yaml`:6 "...every `proposed` node needs the internal command-center's DECISIONS ledger..." — verbatim confirmed by direct read. | Conventional/procedural claim; defeated by evidence the artifact already exists elsewhere. | A diff adding a new `- id: lrs.*` block under `nodes:` with no matching id in `DECISIONS.yaml` → must fail. | **build_now** | One `design/TODO_v0.3.md` line naming the four lrs sub-proposals as pending P09 vetting; pin one canonical decisions-log path, not a parenthetical alternative |
| lrs.defeater-defeated-status-field | lrs-defeaters | Track defeater-attempted-and-survived vs. never-tested as a claim_card status, not just `tested.falsifier` presence. | Refuted in r1 as duplicating an existing mechanism (no fabrication, a real redundancy claim). | `FOUNDATION_v0.6.md`:775 "defeater_log: [{node, date, outcome}]"; `schema/claim_card.schema.json`:437-441 (untyped array, no `required`). | Structural/formal proposal; defeated if the added constraint is redundant or adds no explanatory information — the gap is real: the field exists but is untyped. | `provenance_dag.defeater_log: [{"node":"n1"}]` (missing `date`/`outcome`, currently passes silently) → schema validation must now raise. | **build_now** | Add `required:[node,date,outcome]` + `outcome` enum to the existing `defeater_log` item schema — declarative-only, no new field |
| lrs.dialogue-table-claim-type-column | lrs-defeaters | Add a `claim_type` + `legitimate_defeater` column to the LRS `dialogue_table` template. | Round-1 rejection flagged a naming collision with the schema-fixed `claim_type` field, not a citation fabrication. | v8.1:30 "1. Claim Types, Evidence, and Legitimate [Defeaters]"; `kernel/glosa_kernel.py`:643 (existing `claim_type` already routes rule16w). | Structural/formal proposal; defeated by redundancy with an existing field — avoided by renaming, not by dropping the proposal. | `dialogue_table.md` row with a populated agree/disagree stance but blank `defeater_class`/`legitimate_defeater` → must flag `INCOMPLETE`. | **build_now** | New columns named `defeater_class` (not `claim_type` — deliberately non-colliding) + `legitimate_defeater` on `templates/knowledge/dialogue_table.md`; sync `claim_as_stated` wording to the corrected name |
| lrs.defeater-not-collapse-rule | lrs-defeaters | Kernel rule: reject "strength of the claim" or "feels solid" as a stated defeater, regardless of `claim_type`. | Round-1 refutation: the exact quoted defeater phrases were never found anywhere in-repo (an absence-of-instance, not a fabrication of citation id). | v8.1:51 "'The claim is strong' is not a counterexample, an inconsistency, a failed phenomenon, or contrary evidence." | Structural/formal proposal; defeated if redundant or dominated by a rival mechanism. | `tested.falsifier` matching a strength-of-claim/feels-solid pattern → rule error; a genuine contrary-evidence falsifier → no error. | **build_now** | New `kernel/glosa_kernel.py` rule29 (own namespace, see §3) + `methodology/data/non_defeater_phrase_table.json`; frame as a reasoned analogy to a forward-looking guard, not a direct textual derivation |
| lrs.claim-type-defeater-enum | lrs-defeaters | Extend `claim_type` + add a claim-type-scoped defeater field and matching kernel rule. | Cited "schema/claim_card.schema.json:154-165" for the enum, which is actually a `$ref`, not the enum itself. | `schema/common.defs.json`:154-165 (real location of the `claim_type` enum block); v8.1:44-53 (five-way taxonomy). | Constitutive/structural claim; defeated by internal inconsistency or a counterexample where a claim card's actual defeater style contradicts the declared class. | `defeater_class: EMPIRICAL` + phenomenological-style absence falsifier → rule30 error; + replication-style falsifier → passes. | **build_now** | New `defeater_class` sibling field (not an extension of `claim_type`, to avoid the `EMPIRICAL` value collision) + `kernel/glosa_kernel.py` rule30 |
| **SA-5** (re-anchored this note, missing from `_rejudged.json` per `CLAUDE.md` rule 10) | session-architecture | K_like state-machine citation added to §4.4/§7.3, not a new mechanism. | Round-1 refutation: target mismatch — §7.3 (`Bounded-Judge Law`) governs `review_report.verdict_tier` requirements and carries no K-state content at all; citing K_like there is a category error, independent of any id-fabrication. | v7.1:29 "Knowledge-like candidate K_like \| Definition \| Default starting status of AI output; not a truth verdict."; v7.1:364 "AI(Q) = K_like, K_like ≠ K_validated"; v8.1:146 "Klike −−−→ Kchecked" — all grep-confirmed this pass. | Citation/cross-reference addition, not empirical; its legitimate defeater is showing K_like and glosa's K0 denote unrelated things — refuted, since v7.1:29 gives K_like the identical role as K0 "Private Candidate" (`FOUNDATION_v0.6.md`:1203); the real risk is the *opposite* failure mode — collapsing K_like's finer `K_assumed` "validation bypass" hazard (v7.1:368, F6 at :485) silently into K0/K1, which would erase the exact hazard this citation exists to name. | MUST fire: any doc/schema treats `K_like` as identical to K0 without disclosing the `K_assumed` validation-bypass hazard. MUST NOT fire: a citation naming K_like purely as the source term for K0's "not yet a truth verdict" starting-state property. | **with_revision** (content and citations verified this pass, but by the same session that drafted this note — no independent second skeptic pass yet, per glosa rule 3 this does not count as checked) | One citation sentence added to `FOUNDATION_v0.6.md` §4.4 (after line 1201) naming v7.1:29,355,364,368,485 and v8.1:138,146,422 as the source micro-state vocabulary, plus a one-line "see also NC-47, NC-59" cross-reference at Appendix A Family G (`FOUNDATION_v0.6.md`:2278-2283); **drop §7.3 as a target entirely** — no new NC row, no edit to existing K0-K3 definition text |

Totals: **25 rows.** `build_now` = 13 (unchanged from round 2) · `with_revision` = 8 (round 2's 7,
plus SA-5) · `still_open` = 4.

---

## 3. Two namespace collisions found, and how they are avoided

1. **`C1`–`C8` collision.** `design/CHAIR_RULING_v1.md`:23-30 already uses `C1`..`C8` for chair
   rulings unrelated to session architecture (`independence_class`, the disclaimer catalogue,
   `fetch_status`, `verdict_tier`, `review_mode`, non-collapse rows, lineage table,
   `origin_blackbox_ref`). Twenty-one of the 25 proposals in round 1 reused this exact letter-number
   pattern (`"C4"`, `"C5"`, `"C7"`, `"C8"`, `"C9"`, `"C10"`, `"C1"`) for content from the source
   papers, which do not use that scheme at all (`F1`–`F20` in v7.1; unlabeled "Problem n"/"Repair n"
   headings in v8.1). Avoidance: every corrected citation in §2 now uses `file:line`, never a bare
   letter-number id; where a source concept genuinely deserves a short handle for repeated
   reference (e.g. `chi_recip`, `retained_direction`), the handle is the concept's own name from the
   source text, not a re-minted `Cn`.
2. **`rule29` collision.** `kernel/glosa_kernel.py`'s python-rule sequence stops at `rule28`
   (confirmed by direct read this pass — no `rule29`/`rule30` exist yet there). `FOUNDATION_v0.6.md`
   §3.3's own prose/disclaimer-style "flag-rule" sequence separately runs rules 26-28.
   `lrs.defeater-not-collapse-rule` and `lrs.claim-type-defeater-enum` (§2, both `build_now`) claim
   the next free `kernel/glosa_kernel.py` slots, `rule29`/`rule30`. `kernel.candidate-set-delta-cooking-step`
   (§2, `with_revision`) separately asks to extend `FOUNDATION_v0.6.md` §3.3's own sequence to
   "rule 29" — a same-numbered but non-colliding sibling in a different artifact/namespace.
   Avoidance: every reference to either sequence in this note and in any future `DECISIONS.yaml` row
   must write the full qualified name — `kernel.glosa_kernel.rule29` vs.
   `FOUNDATION_v0.6.md §3.3 flag-rule29` — never the bare number alone.

---

## 4. What the Epistemic Fusion papers gain from this pass

**Now has a mechanical control in glosa** (13 `build_now` rows, §2): the session-boundary
AI-reset asymmetry (F8/F10/F12, v7.1) → `SA-1`'s Blackbox Note fields; the pre-commitment of a
checking route (`R*`, v7.1:351/356) → `schema.entry-resistance-precommit-field`; the direction-
neutrality of retention (`Gs`/`Ts`/`Δs`, Repair 8, v8.1:341-361) → `schema.retention-direction-field`
and its `NC-77` non-collapse row; the full `H0=(P0,M0,U0,E0,Φ0)` entry-anchor apparatus (v7.1:344)
→ `HU-2`; the missing Human Mastery Gate wiring (already-real 10-question checklist,
`templates/paper/arxiv-twocol/main.tex`:375-378) → `HU-1`'s new R8 publish-gate dimension; the
bounded-completeness-prompt discipline (extending `NC-58`) → `HU-5`; and v8.1 §1's five-way
claim-type/legitimate-defeater taxonomy (phenomenological/constitutive/structural_formal/
diagnostic/empirical, v8.1:30-53) → the `lrs-defeaters` lens's five `build_now` rows
(`dialogue_table` columns, `defeater_log` typing, kernel rules 29/30, the TODO-line filing
discipline).

**Stays `Open`, honestly:** the reciprocal-lineage diagnostic `chi_recip` (v7.1:447-554) is
`build_now` for its plumbing (a `session_id` field + a CLI subcommand) but its *tier* stays `Open`
until a reproducibility fixture actually runs — it is never treated as a warrant, truth, or release
gate (v7.1:496), matching the source's own framing of it as diagnostic-only. The momentum scores
`m^H`/`m^AI` (v7.1:550-554) are explicitly **declined** as schema fields (`SA-4`), per their own
documented self-defeat clause and glosa's current lack of any multi-turn/dialogue-history evidence
mechanism — the papers' own hedge on these two constructs is upheld, not overridden. `SA-2`'s
`hypothesis_selection.yaml` application of the same Repair-8 direction-neutrality principle stays
`still_open` until `SA-1` supplies a `session_id` grouping key — the mechanism is sound but not yet
executable on real multi-session data, which per BBL-2026-09-05-119 must be disclosed as an honest
gap, not narrowed into a vacuous single-session-only test and called done. `HU-3`'s session-close
retention note (same Repair-8 principle, applied to the Blackbox Note's own cooking log instead of
the hypothesis ledger) stays `still_open` for the same reason plus its own uncorrected citation
defect. `SA-3`'s pre-exposure H0-lite field and `schema.blackbox-language-bridge-subfield` both stay
un-adopted in their current form — the former needs a single named schema target, the latter is
withdrawn per a standing chair ruling its own proposer missed.

---

## 5. Defeaters for this note itself

1. **This note is a same-session compilation, not an independent check.** Per glosa rule 3
   ("maker ≠ checker ≠ approver... same-model self-review has no standing"), the reconciliation in
   §2 for the 24 rows carried over from `SESSION_ARCH_v0.4_rejudged.json` relies on that file's own
   two-skeptic-verified `citations_verified`/`control_mechanical`/`invariant_ok` fields rather than
   a fresh from-scratch re-grep of all ~90 citations across 24 rows by this session. This session
   did spot-verify a subset directly this pass (the `C1`–`C[0-9]` absence grep in §1; the K_like
   passages, `FOUNDATION_v0.6.md` §4.4/§7.3, and NC-47/NC-59 locations for SA-5 in §2) — those
   specific claims carry direct-read confirmation from this session; the remaining citations in §2
   are relayed from round 2's own verification, not re-verified here, and should be read as such
   (a `Dr`-tier compilation of `finite_diagnostic`-tier upstream checks, not a fresh
   `finite_diagnostic` pass in its own right).
2. **SA-5's re-anchoring in §2 has had no independent second-skeptic pass**, unlike the other 24
   rows. It is marked `with_revision` rather than `build_now` for exactly this reason, not because
   a defect was found in the citations themselves. A legitimate defeater to SA-5's `with_revision`
   status would be a second, independent read confirming the same file:line citations and the same
   §4.4-not-§7.3 target correction — until that happens, this row should not be treated as more
   settled than a solo pass warrants.
3. **This note has not passed the publish gate.** Per glosa rule 8 ("no independent check ⇒ no
   release... public push only through the publish gate (PR + adversarial review + leak scan)") and
   `PUB-ADVERSARIAL-REVIEW`'s privacy/security-leak-scan requirement, this note must not be attached
   to the public Zenodo record (concept DOI 10.5281/zenodo.22318039; v7.1 = 22318040, v8.1 =
   22319715) before an independent adversarial pass runs R1-R7 on it — including a leak scan for
   local paths/usernames and a check that no vendor/model name was introduced anywhere in this
   document, contrary to `CLAUDE.md`'s binding no-AI-attribution rule.
4. **The 13/8/4 count itself could be stale** the moment any of the 8 `with_revision` or 4
   `still_open` rows is actually revised and re-scored — this note is a snapshot of the 2026-09-05
   reconciliation state, not a live query against `DECISIONS.yaml`. A future reader should re-run
   `python tools/anse_sync/cli.py list decisions` (from `the internal command-center/`) rather than treat this table as
   current beyond the date in its filename.
5. **No claim in this note has been through a founder ruling.** Every row marked
   `founder_decision_needed: true` in the underlying `SESSION_ARCH_v0.4_rejudged.json`/`_SPEC.md`
   (most `build_now` rows included — see `SESSION_ARCH_v0.4_SPEC.md` §7) still requires a human
   decision before any schema/kernel change lands; this note recommends nothing be built solely on
   its own authority.
