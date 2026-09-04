> tier: Dr (specified; independently unreviewed)

# P15 — Problem-first spine, responsibility per arrow, and the robustness axis

## One-line rule

The spine starts from a problem state, not from "observation" treated as a noun; every arrow the
spine draws (Data→Inference, Inference→Claim) names who performed it, with Inference→Claim always
human; and any `EMPIRICAL` claim card should carry an operationalization/study-design/bias-register/
robustness record — none of this is required to publish a stub, but its absence is named, not
silent.

## Why

Founder instruction, 2026-09-04 (Blackbox Log, concept DOI `10.5281/zenodo.22302518`), verbatim
(BBL-2026-09-04-083): *"แต่คำว่าสังเกต มันเป็นนามธรรม คือเป็นกริยา ถ้าเราเริ่มจำปัญหาหละ มันมีกระบวนการแบบนี้ไหม
เราก็เลยเสนอให้โฟกัสปัญหาแถน"* — "observation" is abstract, a verb; starting instead from the problem,
is there a process like this? The instruction to adopt this into the spine and to name
responsibility per arrow is BBL-2026-09-04-084. Both are cited, never restated as if this card's
own idea (`AGENTS.md` gate rule 6 — comparison language stays same/different/cited).

`design/FOUNDATION_v0.5.md` §2.1a/§2.1b carries the spec text this card narrates: the pre-readout
problem state precedes the Blackbox Note's first readout, the human-language question, the
lens-in/lens-out hypothesis, evidence, and provisional knowledge — and the spine deliberately never
writes "Reality →" as a node, because the lens never grants direct access to reality, only to what
was read out (`RA ≠ W`, §1.0 Pillars).

## Inputs → outputs

- Input: the Blackbox Note's first raw line (P0/§2.1a), the claim card in progress (P3).
- Output: `claim_card.responsibility` (`data_to_inference: human|ai|joint`,
  `inference_to_claim` const `human`, optional `notes`) and `claim_card.empirical_extension`
  (`operationalization[]`, `study_design`, `bias_register[]`, `robustness`) —
  `schema/claim_card.schema.json`, both OPTIONAL top-level blocks. This card narrates them; it
  does not redeclare their shape (one-fact-one-home).

## Gate

- **Responsibility (kernel rule 15, `kernel/glosa_kernel.py:_responsibility_error_for_card`):**
  when `responsibility` is present, `inference_to_claim` must be exactly `"human"` — a hard
  validation error ("rule15: Inference→Claim must be signed by the human") otherwise. The human
  signs the claim; AI is never an author (`AGENTS.md` gate rule 5, `CLAUDE.md` gate rule 5,
  unchanged repo-wide invariant — this card does not introduce a new authorship rule, it wires an
  existing one to a named field). `Data→Inference` carries no such restriction — it may be human,
  ai, or joint, same three-value vocabulary as `produced_by` (§3.2).
- **Responsibility, absent (kernel rule15w, warning only):** a card with no `responsibility` block
  still validates — the field is optional, per the K0-stub authoring-cost floor (§3.2a) — but emits
  `"rule15w: responsibility per arrow not declared (Data→Inference→Claim)"`, naming the silence
  rather than swallowing it.
- **Empirical extension (kernel rule16w, warning only):** a card with `claim_type: EMPIRICAL` and
  no `empirical_extension` block is legal but under-specified; emits
  `"rule16w: empirical claim without operationalization/study_design/bias_register/robustness"`.
  Never a hard fail — many legitimate K0 empirical stubs will not carry a bias register yet.

**Numbering note, stated plainly rather than silently reconciled:** `design/FOUNDATION_v0.5.md`
§3.3 already names its own rule 13 (`evidence_relations[].channel`, Bridge Burden) and rule 14
(`bearing: CHALLENGES` requires a non-empty `evidence_id`) — both spec-only, not yet implemented in
`kernel/`. This card's "rule 15"/"rule16w" are a separate, task-scoped kernel check keyed to the
`responsibility`/`empirical_extension` blocks this founder instruction added, not a renumbering or
replacement of §3.3's own rules. A future pass should reconcile the two numberings into one
sequence; until then both live in `kernel/glosa_kernel.py` under names that do not collide in code
(`_responsibility_error_for_card`, `_responsibility_warning_for_card`,
`_empirical_extension_warning_for_card`), only in their printed rule-number prefix.

## Human / AI division of labour

Human: performs (or is the sole legal signer of) the Inference→Claim arrow, always — non-delegable,
same invariant as `responsible: human` and `human_owner` elsewhere on the card. Human also owns the
bias-register's `mitigation`/`residual` judgment calls, since these are content judgments the kernel
can only check for presence, never correctness (chair ruling D2's presence-vs-correctness split,
§3.1, applied here). AI: may perform or co-perform Data→Inference (drafting an operationalization
row, proposing a bias type, drafting a robustness-check plan), and must disclose that contribution
under `ai_filled`/`responsibility.notes` — never silently folded into a `data_to_inference: human`
declaration when AI in fact did the drafting.

## The robustness axis, distinct from the independence ladder

`claim_card.empirical_extension.robustness` is a different question from the independence ladder
I0–I5 (§4.2). **Independence answers "who checked"** — was the check performed by the same model,
a different vendor, or an external human. **Robustness answers "does the result survive changing
data, method, analyst, tool, or time"** — a check can be run by a fully independent (I5) human and
still report `result: not_run` on every `what_varied` axis (nobody has yet re-run it with different
data), and conversely a single analyst (I1) can run and honestly report several robustness checks
without that raising independence class at all. The two axes are never collapsed into one number;
`robustness.status` (`not_run | partial | run`) and `checks[].result` (`same | different | not_run`
— comparison vocabulary only, `AGENTS.md` gate rule 6, never a novelty/priority word) are read
alongside `independent_check.independence_class`, not instead of it.

## Disclaimers emitted

`D-STANDPOINT` (always) · `D-AUTHORSHIP` (always — Inference→Claim's human-only rule is one
concrete instance of this disclaimer's general claim) · `D-TIER` · `D-K-STATE` — none of this
card's own additions currently has a dedicated disclaimer-catalogue row; a future pass may add
`D-RESPONSIBILITY-UNDECLARED`/`D-EMPIRICAL-UNDERSPECIFIED` to
`methodology/data/disclaimer_catalogue.json` to mirror `rule15w`/`rule16w` as named catalogue rows —
not done in this pass (out of scope: this task touched `kernel/glosa_kernel.py`'s `validate_claim_card`
and `compute_disclaimers`'s own catalogue-reading logic was left unchanged, so `rule15w`/`rule16w`
surface today only in `validate_claim_card`'s `warnings` list, not yet in
`disclaimers_emitted`/`compute_disclaimers()`'s output).

## Non-collapse pairs enforced

`NC-01` World≠Record≠Readout≠Meaning≠Truth≠Warrant≠Knowledge-Attribution (applied to the spine's
own first node, §2.1a: problem state ≠ first readout) · `NC-14` Existence≠Attribution≠Disclosure ·
`NC-35` Observation≠Claim≠Inference≠Hypothesis≠Decision (the responsibility block names *who*
performs the Inference≠Claim step specifically) · `NC-57` Claim scope≤Evidence scope · `NC-71`
`RA≠W` (why the spine does not write "Reality →" as a node, §2.1a).

## What this card does NOT do

It does not make `responsibility` or `empirical_extension` required fields — both stay OPTIONAL on
`schema/claim_card.schema.json`, preserving the K0 low-authoring-cost floor P3 already defends
(§3.2a). It does not decide the robustness checks' *results* — the card only records what someone
else's method produced, honestly, same as P3's own closing line about the licensing test. It does
not reopen or renumber the Blackbox Note's own schema (§2.3), S1–S6 stage ownership (§2.2), or
FOUNDATION §3.3's pre-existing rules 1–12 and 13/14 — see the numbering note above.

## Thai summary (สรุปสั้น)

การ์ดนี้อธิบายสองสิ่งที่ผู้ก่อตั้งสั่งเพิ่มเข้าไปในแกน (spine) เมื่อ 2026-09-04 ตาม Blackbox Log
BBL-2026-09-04-083/084: (1) แกนเริ่มจาก "สภาวะปัญหา" ที่มีอยู่ก่อนใครจะไปสังเกตมัน — คำว่า "สังเกต" เป็นกริยา
ไม่ใช่จุดเริ่มต้น บันทึกกล่องดำ (Blackbox Note) คือการอ่านครั้งแรกต่อสภาวะปัญหานั้น จึงอยู่หัวแกนเสมอ และแกนจงใจ
ไม่เขียน "ความจริง →" เป็นจุดเริ่มต้น เพราะเลนส์ไม่เคยให้เข้าถึงความจริงตรง ๆ มีแต่สิ่งที่อ่านออกมาได้เท่านั้น; (2)
ทุกลูกศรในแกนต้องระบุว่าใครทำ — จากข้อมูลไปสู่การอนุมาน (Data→Inference) เป็นมนุษย์/AI/ร่วมกันก็ได้ แต่จาก
การอนุมานไปสู่ข้ออ้าง (Inference→Claim) ต้องเป็นมนุษย์เสมอ มนุษย์เป็นผู้ลงนามข้ออ้าง AI ไม่ใช่ผู้เขียนร่วมที่มีสิทธิ์
ลงนาม การ์ดข้ออ้างยังมีฟิลด์เสริม (ไม่บังคับ) สำหรับข้ออ้างเชิงประจักษ์ (EMPIRICAL) — วิธี operationalize
ตัวแปรนามธรรม, การออกแบบการศึกษา, ทะเบียนอคติ (bias register), และแกนความคงทน (robustness) ซึ่งแยกจาก
บันไดความเป็นอิสระ I0–I5 อย่างชัดเจน: ความเป็นอิสระตอบว่า "ใครตรวจ" ส่วนความคงทนตอบว่า "ผลลัพธ์ยังอยู่ไหม
เมื่อเปลี่ยนข้อมูล/วิธี/ผู้วิเคราะห์/เครื่องมือ/เวลา" ไม่ใช่คำถามเดียวกัน และไม่ถูกรวมเป็นตัวเลขเดียว ทุกฟิลด์ที่เพิ่มยัง
เป็นทางเลือก (optional) — การไม่ใส่ไม่ทำให้การ์ดล้มเหลว แต่ระบบจะเตือน (`rule15w`, `rule16w`) แทนที่จะเงียบไป
เฉย ๆ.

## Ownership criterion (founder, BBL-2026-09-04-086/087)

Problem, question and the *selection* of the hypothesis stay the human's (AI may draft candidates; the choice is human — BBL-088 wording); any tool may do the rest — founder verbatim: "จะใช้เอไอใช้แมวใช้หมี ก็ใช้ไปเถอะ เพราะนั่นคือเป้าหมายของความรู้ แก้ปัญหาให้ใครสักคน". The goal of knowledge under this criterion: solve a problem for someone. Card field `responsibility.ownership` (`problem`, `question`, `hypothesis_selection`, each const `human`), kernel rule 15. See FOUNDATION §2.1c.
