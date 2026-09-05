# MEETING 2026-09-05 — Session-Architecture Uplift (SA-1..SA-4)

## สรุปภาษาไทย (12 บรรทัด)

1. หัวข้อ: เพิ่มความสามารถของ glosa ให้ "มองเห็น" session ระหว่างมนุษย์กับ AI เป็นวัตถุหนึ่ง (ขอบเขต session, สิ่งที่มนุษย์ถือต่อ, ทิศทางของสิ่งที่ค้างอยู่) โดยอ้างอิง EPISTEMIC_FUSION_v7.1/v8.1
2. มีข้อเสนอ 4 ข้อ (SA-1..SA-4) ทุกข้อผ่านการตรวจสองรอบอิสระ (สองผู้ตรวจ = skeptic คนละคน)
3. ปัญหาที่พบซ้ำในทุกข้อ: อ้าง id เช่น "C4/C5/C7/C8/C9" ราวกับเป็น claim card ที่มีอยู่จริง — grep แล้วไม่พบ id แบบนี้ในไฟล์ต้นฉบับเลย
4. หนักกว่านั้น: "C1–C8" เป็น namespace ที่ glosa ใช้อยู่แล้วจริงใน `design/CHAIR_RULING_v1.md` (ความหมายคนละเรื่อง) — ชนกันโดยตรง ผิดกฎ 17 (source-first citation)
5. เนื้อหาที่อ้างถึงกลับเป็นของจริง ตรวจสอบแล้วมีอยู่ในไฟล์ต้นฉบับ เพียงแค่ id ที่แปะไว้เป็นของปลอม/คิดขึ้นเอง
6. SA-1 (session_boundary field ใน Blackbox Note): ผู้ตรวจคนหนึ่งให้ตก (evidence เสีย) อีกคนให้เก็บแบบต้องแก้ก่อน — ตัดสิน: เก็บแบบมีเงื่อนไข (revise)
7. SA-2 (retained_direction disclaimer + NC row ใหม่): ทั้งสองผู้ตรวจให้เก็บ คะแนนเท่ากัน (6/6) พร้อม revision ชัดเจน — คะแนนสูงสุดของรอบนี้
8. SA-3 (H0-lite ใน S1): ผู้ตรวจคนหนึ่งให้ตก (ชนกับ scope ของ §2.1a เอง + citation ผิด) อีกคนให้เก็บแบบมีเงื่อนไข — ตัดสิน: ตกเป็นดีฟอลต์ ต้อง resubmit ใหม่
9. SA-4 (บันทึกปฏิเสธไม่รับ momentum scoring m^H/m^AI เข้า schema ตอนนี้): ทั้งสองผู้ตรวจให้เก็บ เป็นงาน "บันทึกการไม่ทำ" ความเสี่ยงต่ำสุด
10. ไม่มีข้อเสนอใดละเมิด founder invariant (สิทธิ์เป็นเจ้าของปัญหา/สมมติฐานของมนุษย์, AI ไม่เซ็นรับรอง, ไม่มีคำ novelty/first)
11. ทุกข้อต้องแก้ citation จาก "C-เลข" เป็น file:line ก่อนเข้า DECISIONS.yaml จริง — นี่คือเงื่อนไขร่วมของทุกข้อที่เก็บไว้
12. คำถามที่ต้องให้ founder ตัดสิน 3 ข้อ: retroactive scope ของ SA-3, การจัดสรร NC id ใหม่ (ชน DECISIONS.yaml), และจะแยก v0.3.1 (แก้ citation+SA-2/SA-4) กับ v0.4 (SA-1/SA-3 หลัง resubmit) หรือไม่

---

## 1. Scope and method

This is a chaired synthesis of four judged proposals (SA-1..SA-4), each already reviewed by two
independent skeptic passes (adversarial verification per `maker-checker-gate` discipline). The
chair does not re-run the reviews; it reconciles them, verifies the reconciliation against the
repo directly, and produces one ranked list plus the founder-facing decisions. Tier of everything
below: `Dr` (design synthesis, not yet built or tested) unless marked otherwise. Every point below
cites file + line; no vendor names used as credit; no novelty/first/prior-art language.

Direct chair verification (this pass, independent of both skeptics):

- `grep -n "^C[0-9]" sources/notes/EPISTEMIC_FUSION_v7.1.txt sources/notes/EPISTEMIC_FUSION_v8.1.txt`
  → zero hits in either file. Both source notes number findings as `F1..F20` (v7.1) or leave
  formulas/problems unlabeled with headings like "Problem 1", "Repair 8" (v8.1). **No "C1–C11"
  claim-numbering scheme exists in either source file.** This confirms, independently, the
  citation-fabrication finding both skeptics raised on all four proposals.
- `design/CHAIR_RULING_v1.md:23-30` shows `C1..C8` is already a live glosa id namespace (chair
  rulings on `independence_class`, disclaimer catalogue, `fetch_status`, `verdict_tier`,
  `review_mode`, non-collapse rows, lineage table, `origin_blackbox_ref`) — unrelated to session
  architecture. Reusing "C4/C5/C7/C8" for the new proposals collides with this existing meaning.
  finite_diagnostic, confirmed by direct read.
- The real source locations, verified this pass:
  - `sources/notes/EPISTEMIC_FUSION_v7.1.txt:493` F10 "Reciprocal momentum is session-bounded";
    `:497` F12 "cross-session persistence"; `:351` `ENTRY_H→AI = H_0 ∧ V_0 ∧ C_0 ∧ R*`.
  - `sources/notes/EPISTEMIC_FUSION_v8.1.txt:132` "Problem 1 – AI Arrives Before a Human [Baseline
    Exists]"; `:345-350` `Gs = g(...)`, `Ts = h(...)`, `Δs = Gs − Ts`; `:356` "Repair 8 — Separate
    retention magnitude from re[tained direction]".
  - `design/FOUNDATION_v0.6.md:2255-2256` NC-32 "DVP≠K2", NC-34 "No independent check⇒No
    K2/No release"; `:2306-2311` highest assigned row is NC-76 (Family J) — next free id is
    **NC-77**, confirming SA-2's own hedge is correct.
  - `design/FOUNDATION_v0.6.md:1670` confirms `BLACKBOX_NOTE` as an `identifier.kind` (chair
    ruling C8 — the *glosa* C8, not the source's), i.e. Blackbox Note is already the place
    session-scoped raw dialogue lives, per §2.3.

No file in `design/DAG_v0.3.yaml` or `design/FOUNDATION_v0.6.md` mentions `session_boundary`,
`momentum`, `tunnel`, or `retained_direction` — the underlying gap claim ("glosa has no
session-architecture node") is confirmed genuine across all four proposals, independent of the
citation defect.

---

## 2. What today's knowledge changes about glosa's picture of a human-AI session

1. glosa currently has no artifact-level notion of a "session" as a bounded object — Blackbox Note
   (`templates/knowledge/blackbox_note.yaml`, `schema/blackbox_note.schema.json`) records raw
   timestamped/speaker-tagged lines, but nothing marks where a session opens, closes, or what
   crosses the boundary.
2. The source material's core move (v7.1 F10/F12, v8.1 Repair 8) is: within a session, human and
   AI outputs can mutually reshape each other (`sources/notes/EPISTEMIC_FUSION_v7.1.txt:493`); but
   the AI carries nothing forward across a session boundary — only the human does. glosa has no
   field naming that asymmetry.
3. A second, separate move: retention of a claim/habit after a session is direction-neutral.
   `Δs = Gs − Ts` (`sources/notes/EPISTEMIC_FUSION_v8.1.txt:345-347`) can be positive (durable
   expansion) or negative (durable tunnel) — persistence alone (`η_s>0`) cannot tell you which.
4. This second move is structurally identical to a discipline glosa already enforces elsewhere:
   NC-32 "DVP≠K2" and NC-34 "No independent check⇒No K2/No release"
   (`design/FOUNDATION_v0.6.md:2255-2256`) — i.e. "a thing sticking around is not itself a check."
   The proposals correctly generalize an existing glosa refusal-pattern to a new domain (session
   retention) rather than inventing a new epistemic stance.
5. A third move (v8.1 "Problem 1", line 132) says a human baseline must be elicited *before* first
   AI exposure, not reconstructed after — this matches glosa's own existing rule
   `design/FOUNDATION_v0.6.md` §2.1a "Problem before observation" (founder instruction
   BBL-2026-09-04-083/084), so this is confirmation of an existing rule with a source, not a new
   rule.
6. A fourth item (momentum scores `m^H`/`m^AI`, reciprocal-lineage diagnostic `chi_recip`) is
   explicitly self-defeating in its own source — both carry a documented removal clause
   ("remove if path-history adds no explanatory value beyond current state") — and glosa has no
   multi-turn/dialogue-history evidence mechanism today (claim card, evidence relation, review
   report are all single-artifact-scoped). Adopting these as schema fields now would import an
   untested diagnostic as if load-bearing.
7. None of the four proposals asks glosa to compute a new score, rank a hypothesis, or certify
   anything — three are schema/documentation additions (fields, a disclaimer row) and one is an
   explicit non-adoption record. This keeps the uplift inside glosa's existing register
   (structure-naming, not new arithmetic), consistent with K-state discipline.
8. The uplift, if all four land, gives glosa exactly three new capabilities: (a) name a session's
   open/close and what the human carries forward past an AI-side reset (SA-1); (b) refuse to let
   "it stuck around" answer "was it a real expansion" without an independent check (SA-2); (c) log,
   rather than silently skip, the decision not to build momentum scoring yet (SA-4).
9. What is explicitly left `Open`: the full `H0=(P0,M0,U0,E0,Φ0)/κ0` apparatus (SA-3's own scoping
   choice), and the entire `m^H`/`m^AI`/`chi_recip` momentum-diagnostic family (SA-4's explicit
   non-adoption). Both are honest boundaries, not gaps hidden by omission.
10. Every proposal's underlying mechanism checked out against the actual source text (v7.1/v8.1);
    only the citation *labels* attached to that content are wrong. This is a citation-hygiene
    problem across all four, not a substance problem in three of the four (SA-3 has a substance
    problem too — see §4).

---

## 3. Ranked leverage points (kept by at least one skeptic; ordered by reconciled score)

Reconciliation rule applied: where the two skeptics disagree on `keep`, the chair does not average
scores — it treats the proposal as "keep, conditional on the stated fixes" only when the rejecting
skeptic's objection is a fixable citation/scoping defect (not a substance defect), and as "reject,
resubmit" when the rejecting skeptic found a scope/mechanism conflict with existing glosa rules.

### #1 — SA-2: `retained_direction: unknown` gating (D-RETENTION-DIRECTION)

- **What**: a new disclaimer-catalogue row + Appendix A non-collapse row stating that retention of
  a claim/habit across sessions is never by itself evidence it is an "expansion" rather than a
  "tunnel"; only an independent check outcome may reclassify it. Default: `retained_direction:
  unknown`.
- **Why**: closes a real gap — nothing in glosa currently blocks a `hypothesis_selection.yaml` row
  that stayed `chosen` across sessions from being silently read as validated.
- **Evidence (corrected)**: `sources/notes/EPISTEMIC_FUSION_v8.1.txt:341-350` (Gs/Ts/Δs
  definitions), `:356-361` (Repair 8, direction-neutrality of retention); pattern precedent
  `design/FOUNDATION_v0.6.md:2255-2256` (NC-32, NC-34).
- **Acceptance test**: scan of N `hypothesis_selection.yaml` rows `chosen` across ≥2 sessions with
  no linked independent-check artifact → 100% tagged `retained_direction: unknown`; a row with a
  linked checker finding/falsifier result may carry `expansion`/`tunnel`.
- **Cost / DAG target**: S. New DAG node `session.retention-direction-gate` (new id — no existing
  node covers this); new Appendix A row **NC-77** (next free id per direct verification above,
  §1); new `design/FOUNDATION_v0.6.md` §5 disclaimer id `D-RETENTION-DIRECTION`.
- **Both skeptics: keep, score 6/6.** Reconciled verdict: **keep, conditional** on two fixes before
  a DECISIONS.yaml row: (1) replace "C3"/"C9" with the file:line citations above; (2) define the
  session-grouping key the scanner needs (current `hypothesis_selection.yaml` has no session id
  field — `decided_by`/`decided_at` alone cannot group rows into sessions), or narrow the
  acceptance test to what's checkable without it.

### #2 — SA-4: log non-adoption of momentum scoring (DECLINED-FOR-NOW)

- **What**: a `DECISIONS.yaml` row explicitly declining to add `chi_recip`/`m^H`/`m^AI` as schema
  fields now, citing (a) no multi-turn evidence mechanism exists in glosa today, (b) both
  diagnostics carry an untested self-defeat clause in their own source.
- **Why**: prevents the momentum-scoring idea from being silently re-proposed later without this
  context, at near-zero cost/risk.
- **Evidence (corrected)**: `sources/notes/EPISTEMIC_FUSION_v7.1.txt:550,554` (explicit removal
  clauses for `m^H` and `chi_recip`); repo grep confirms no session-history/dialogue field in any
  current schema.
- **Acceptance test**: `DECISIONS.yaml` contains one row, `status: DECLINED-FOR-NOW`, `reason`
  citing the self-defeat clause, `revisit_condition: glosa begins modeling multi-turn dialogue
  history as evidence`; grep confirms no matching field silently exists in any claim_card template.
- **Cost / DAG target**: S. No new DAG node — a non-adoption note attached to the nearest sibling
  node (the SA-2 node above, once it exists) rather than a phantom node.
- **Both skeptics: keep, score 4/4.** Reconciled verdict: **keep**, with the naming caution that
  the DECISIONS.yaml row must tag these as *source* card ids (e.g. "EPISTEMIC_FUSION_v7.1 F-series,
  lines 550/554") — not "C7"/"C8" — to avoid colliding with `design/CHAIR_RULING_v1.md`'s own C7/C8
  (lineage table, `origin_blackbox_ref`).

### #3 — SA-1: `session_boundary` block on Blackbox Note

- **What**: add `session_id`, `opened_at`, `closed_at`, `human_retained_residue_ref`, and a fixed
  literal `ai_state_at_boundary: reset` to `templates/knowledge/blackbox_note.yaml`.
- **Why**: names the session boundary and what the human carries across it — no new scoring.
- **Evidence (corrected)**: `sources/notes/EPISTEMIC_FUSION_v7.1.txt:493,497` (F10 session-bounded
  reciprocal reshaping; F12 cross-session persistence asymmetry — AI resets, human doesn't).
- **Acceptance test**: given two Blackbox Note files sharing a `session_id` split across a tool
  restart, a schema validator confirms `ai_state_at_boundary: reset` present in both, and
  `human_retained_residue_ref` resolves to an existing repo artifact.
- **Cost / DAG target**: S, but see gap below. Target: `templates/knowledge/blackbox_note.yaml` +
  `schema/blackbox_note.schema.json` (the proposal's original `target` omitted the schema file —
  corrected here) + `design/FOUNDATION_v0.6.md` §2.3.
- **Skeptics split (2 vs 6).** Reconciled verdict: **keep, conditional** — the rejecting skeptic's
  objection (fabricated "C4"/"C5" ids) is a citation defect, fixable the same way as SA-2/SA-4; it
  is not a scope conflict with any existing glosa rule. Required fixes before a DECISIONS.yaml row:
  (1) file:line citations as above; (2) add `schema/blackbox_note.schema.json` to `target` and
  either add a cross-reference validator (a small extension to `tools/blackbox_log.py`, not covered
  by "cost: S" as currently scoped) or narrow the acceptance test to what plain JSON Schema alone
  can prove (presence + literal value of `ai_state_at_boundary`), leaving ref-resolution as a
  separately scoped follow-up.

---

## 4. Rejected — reject-as-default, resubmit required

### SA-3: H0-lite field on S1 (`problem_stated_before_first_ai_response`, `prior_model_or_guess`,
`verification_intent`)

- **Skeptic reasons** (one line each, both independent of each other):
  - Skeptic A: cites "C5" as a claim id — no such id exists in either source file
    (`grep` confirms zero); target names "S1/Observation Card" but per
    `design/FOUNDATION_v0.6.md` §2.2, S1 owns the Problem Card and S2 owns the Observation Card —
    two different stages, two different schema files, conflated in the proposal.
  - Skeptic B: same citation defect, plus the proposal's own cited section §2.1a explicitly states
    it "does not reopen S1–S6 stage ownership (§2.2)" (`design/FOUNDATION_v0.6.md` ~line 353-355),
    while the proposal's `target` is exactly to extend the §2.2 S1 stage table — a direct tension
    with the section it leans on for authority.
- **Chair note**: unlike SA-1/SA-2/SA-4, this is not only a citation-label problem — the stage
  target itself is ambiguous/self-contradicting (S1 Problem Card vs. S2 Observation Card vs. the
  Blackbox Note's own existing `speaker`/timestamp fields, which one skeptic showed can already
  answer the acceptance test's core question — "did a human line precede the first AI line" —
  without new required fields at all). Reconciled default: **reject**, resubmit with (a) a single
  named schema file, not two conflated stages; (b) the real citation
  (`EPISTEMIC_FUSION_v8.1.txt:132` "Problem 1"; `v7.1.txt:351` `ENTRY_H→AI`); (c) an explicit
  argument for why the existing Blackbox Note timestamp/speaker fields are insufficient for the
  stated acceptance test, since as scoped they may already suffice.

---

## 5. Founder decisions required

1. **SA-1 target correction — one schema file or two?** SA-1's acceptance test needs
   `human_retained_residue_ref` to resolve cross-file, which plain JSON Schema cannot do. Recommend:
   scope SA-1 to `blackbox_note.yaml`/`schema/blackbox_note.schema.json` only, add the
   cross-reference check as a small `tools/blackbox_log.py` extension in a *separate*, explicitly
   costed follow-up rather than folding it into "cost: S" now. **Recommended option: split now,
   ship the schema field this pass, defer the validator.**
2. **NC-77 id assignment — coordinate via DECISIONS.yaml first, or reserve now?** SA-2's new
   Appendix A row is confirmed next-free at NC-77 (verified this pass), but SA-2's own risk note
   flags collision if another proposal claims a Family J row concurrently. **Recommended option:
   reserve NC-77 for `session.retention-direction-gate` in this meeting's DECISIONS.yaml row now,
   rather than leaving it open to a race.**
3. **SA-3 retroactivity, once resubmitted** — if a corrected H0-lite proposal returns, applying it
   retroactively to already-published Blackbox Notes will surface real gaps in prior sessions
   (including this workspace's own). **Recommended option: forward-only** (apply to sessions opened
   after the field is added), not retroactive — consistent with how other schema additions in this
   repo have been rolled out per `design/FOUNDATION_v0.6.md`'s versioning pattern, but this needs an
   explicit founder ruling before SA-3 resubmission, not an assumption baked in by the chair.

---

## 6. Proposed v0.3.1 / v0.4 scope split

- **v0.3.1 (this pass — citation-hygiene-gated, low risk, ship after fixes above)**:
  - SA-2 (`retained_direction` gate, NC-77, `D-RETENTION-DIRECTION`) — fix citations + define
    session-grouping key.
  - SA-4 (DECLINED-FOR-NOW momentum-scoring row) — fix citation tags to avoid C7/C8 collision.
  - SA-1 (`session_boundary` block) — fix citations, correct target to include the schema file,
    narrow or defer the cross-reference half of the acceptance test.
- **v0.4 (next pass — needs a resubmission + a founder ruling first)**:
  - SA-3 (H0-lite), only after: (a) resubmission with a single named schema file and real
    citations, (b) founder ruling on retroactivity (§5.3 above).
  - Any future re-proposal of momentum/`chi_recip` scoring, gated on SA-4's stated
    `revisit_condition` (glosa first gaining a multi-turn dialogue-history evidence mechanism) —
    do not reopen before that condition is met.

---

## Appendix — new DAG nodes (append to `design/DAG_v0.3.yaml`, same schema as existing nodes)

```yaml
nodes:
  - id: session.retention-direction-gate
    title: Retention-direction disclaimer + non-collapse row (D-RETENTION-DIRECTION)
    change: >
      Add disclaimer id D-RETENTION-DIRECTION (design/FOUNDATION_v0.6.md §5) and Appendix A row
      NC-77 stating that retention/persistence of a claim or habit across sessions is never by
      itself evidence it is an expansion rather than a tunnel; only an independent check outcome
      may reclassify it. Default status for any retained-but-unchecked item: retained_direction:
      unknown. Schema: add optional `retained_direction` enum [unknown, expansion, tunnel] to
      schema/hypothesis_selection.schema.json (additionalProperties: true already permits this).
    kind: schema+doc
    target: design/FOUNDATION_v0.6.md §5 + Appendix A (NC-77); schema/hypothesis_selection.schema.json
    evidence: [sources/notes/EPISTEMIC_FUSION_v8.1.txt:341-361, design/FOUNDATION_v0.6.md:2255-2256]
    acceptance_test: >
      Given N hypothesis_selection.yaml rows chosen across >=2 sessions with no linked
      independent-check artifact, a scan confirms 100% tagged retained_direction: unknown; a row
      with a linked checker finding/falsifier result may carry expansion or tunnel.
    risk: Low — additive field + disclaimer id; blocked on defining a session-grouping key for the scanner.
    status: proposed
    human_decision_needed: false

  - id: session.momentum-scoring-declined
    title: Non-adoption record for chi_recip / m^H / m^AI momentum scoring
    change: >
      Log a DECISIONS.yaml row declining to add chi_recip (reciprocal-lineage diagnostic) or
      m^H/m^AI (finite-history momentum scores) as glosa schema fields at this time. No DAG node
      is built; this node exists only to attach the non-adoption note and its revisit_condition.
    kind: process
    target: the internal command-center's DECISIONS ledger (private) (new row, status DECLINED-FOR-NOW)
    evidence: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:550, sources/notes/EPISTEMIC_FUSION_v7.1.txt:554]
    acceptance_test: >
      DECISIONS.yaml contains one row with status DECLINED-FOR-NOW, reason citing the self-defeat
      clause, revisit_condition: glosa begins modeling multi-turn dialogue history as evidence;
      grep confirms the row exists and no equivalent field silently exists in any claim_card template.
    risk: Very low — documentation-only.
    status: proposed
    human_decision_needed: false

  - id: session.boundary-field
    title: session_boundary block on Blackbox Note
    change: >
      Add session_id, opened_at, closed_at, human_retained_residue_ref, and fixed literal
      ai_state_at_boundary: reset to templates/knowledge/blackbox_note.yaml and
      schema/blackbox_note.schema.json. Cross-file resolution of human_retained_residue_ref is a
      separately scoped follow-up (tools/blackbox_log.py extension), not covered by this node's cost.
    kind: schema
    target: templates/knowledge/blackbox_note.yaml; schema/blackbox_note.schema.json; design/FOUNDATION_v0.6.md §2.3
    evidence: [sources/notes/EPISTEMIC_FUSION_v7.1.txt:493, sources/notes/EPISTEMIC_FUSION_v7.1.txt:497]
    acceptance_test: >
      Given two Blackbox Note files sharing a session_id split across a tool restart, a schema
      validator confirms ai_state_at_boundary is present and equals reset in both.
    risk: Low — additive schema field; ref-resolution half deferred to a follow-up node.
    status: proposed
    human_decision_needed: true  # retroactive-vs-forward-only application, see MEETING §5.3 analogue for SA-1's own logs
```
