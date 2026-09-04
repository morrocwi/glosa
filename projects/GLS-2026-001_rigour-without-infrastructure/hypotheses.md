# Candidate hypotheses — GLS-2026-001 (rigour-without-infrastructure)

> tier: Dr (specified; independently unreviewed). Three candidates, lens-out from
> `lens_translation.md`, in world/discipline language (R2, per `design/FOUNDATION_v0.5.md` §2.3).
> **AI drafts candidates; AI never selects.** Selection among H1/H2/H3 (zero, one, or more) is the
> founder's own act, recorded later in a `hypothesis_selection.yaml` (S3c, §7.9) — not performed in
> this file. Each carries `claim_type` per `schema/claim_card.schema.json`'s vocabulary
> (`CONCEPTUAL | EMPIRICAL | DESIGN`).

---

## H1 — Design-science claim (the hypothesis implied by the founder's own abstract)

**id:** H1
**claim_type:** DESIGN

**statement (TH):** ถ้าทุกข้ออ้างที่ผู้ที่ไม่มีมหาวิทยาลัย ไม่มีแล็บ และไม่มีทีมวิจัยผลิตขึ้น
ถูกบันทึกเป็นการ์ดข้ออ้างที่ตอบห้าคำถามของผู้ก่อตั้ง (เห็นอะไรจริง / ข้อมูลแยกอะไรได้ / AI เติมอะไร /
สมมติอะไรไว้ / เคยผ่านการตรวจอิสระอะไรมาบ้าง) ผูกกับเงื่อนไข Existence-Attribution-Disclosure ของ
Readout Condition และผ่านประตูบันไดความเป็นอิสระ (independence ladder) ก่อนเผยแพร่สู่สาธารณะ
แล้ว คนที่ไม่มีสังกัดสถาบันก็สามารถผลิตความรู้ร่วมกับ AI ที่ความเข้มงวดของมันตรวจสอบได้โดยผู้อ่าน
โดยไม่ต้องพึ่งใบรับรองสถาบันเป็นบันไดผ่าน

**statement (EN):** If every claim a standalone scholar (no university, no lab, no research team)
produces is recorded as a claim card that answers the founder's five questions (what was actually
seen / what the data separates / what AI filled in / what is assumed / what independent test, if
any, it has survived), tied to the Readout Condition's Existence-Attribution-Disclosure conditions,
and passed through the independence ladder before any public release — then a person with no
institutional affiliation can co-produce knowledge with AI whose rigour a reader can check for
themselves, without an institutional credential serving as the thing that certifies it.

**falsifier:** A real claim card that passes every field the kernel can mechanically check (full
schema pass) is nonetheless found by a genuine independent reviewer (I5) to have a false answer at
Q2 (evidence/authority-to-believe test) or Q3 (AI-fill disclosure) — showing the mechanical check
does not actually track the epistemic property it claims to track.

**what evidence would separate it:** A corpus of claim cards produced under this discipline, each
run through the independence ladder up to at least I3 (cross-vendor AI check), with a subset also
reaching a genuine I5 (an outside human reviewer with no stake in the project) — compared against a
matched corpus of claims produced without the card discipline, scored on whether an independent
reader can recover the evidence/AI-fill boundary the maker recorded. This project's own paper
(`paper/main_th.md`) already discloses that, reflexively, its own ten claim cards currently sit at
I0 only (same-session self-check) — so this hypothesis is not yet evidenced by its own author-work,
which is stated as a finding, not hidden.

**Hypothesis derived with Readout Universe — Yaoharee Lahtee (lens, DOI
10.5281/zenodo.21529456); candidate proposed by AI, selection reserved to the founder.**

---

## H2 — Conceptual claim: rigour as a portable claim-level property, not an institutional one

**id:** H2
**claim_type:** CONCEPTUAL

**statement (TH):** "ความเข้มงวด" ไม่ใช่คุณสมบัติที่กลไกสถาบัน (แล็บ ภาควิชา คณะกรรมการตรวจ) มอบให้กับ
ข้ออ้างจากภายนอก แต่เป็นคุณสมบัติที่ข้ออ้างชิ้นหนึ่งสามารถ "พกติดตัว" ได้เองผ่านโครงสร้างการบันทึกของมัน
(ตอบได้ว่าเห็นอะไร แยกอะไร AI เติมอะไร สมมติอะไร ผ่านการตรวจอิสระอะไรมา) — สถาบันเป็นเพียง*หนึ่งใน*
กลไกที่เคยทำให้เกิดคุณสมบัตินี้ได้ในอดีต ไม่ใช่แหล่งเดียวที่เป็นไปได้

**statement (EN):** "Rigour" is not a property that institutional machinery (lab, department,
review committee) confers on a claim from the outside; it is a property a single claim can carry
in its own recorded structure (what was seen, what separates, what AI filled, what is assumed, what
independent check it survived) — institutions are *one* historical mechanism that has produced this
property, not the only possible one.

**falsifier:** A claim card that answers all five questions honestly and completely, checked at I3,
is shown to still require an institutional credential (not just an independent human reviewer) to
be treated as rigorous by its actual intended readers — i.e. the credential does load-bearing work
the card's own fields cannot substitute for, for at least one class of reader/decision this project
cares about.

**what evidence would separate it:** Reader studies or field evidence on whether a target audience
(e.g. journal editors, grant reviewers, or the practitioner's own community) treats a
well-formed claim card as sufficient without also asking "who backs this / what institution is
behind it" — separating cases where the card discipline substitutes for institutional trust from
cases where it does not.

**Hypothesis derived with Readout Universe — Yaoharee Lahtee (lens, DOI
10.5281/zenodo.21529456); candidate proposed by AI, selection reserved to the founder.**

---

## H3 — Empirical claim: cross-vendor AI checking measurably raises detection of undisclosed AI-fill

**id:** H3
**claim_type:** EMPIRICAL

**statement (TH):** เมื่อการ์ดข้ออ้างถูกตรวจโดย AI คนละยี่ห้อ (cross-vendor, ระดับความเป็นอิสระ I3)
แทนที่จะตรวจซ้ำด้วย AI ยี่ห้อเดียวกับที่ผลิตการ์ด (I0/I1) อัตราการจับได้ของ AI-fill ที่ไม่เปิดเผย
(ฟิลด์ Q3 เป็นเท็จ) หรือข้อสมมติที่ไม่เปิดเผย (ฟิลด์ Q4 เป็นเท็จ) จะสูงขึ้นอย่างมีนัยสำคัญ เทียบกับ
การตรวจด้วยยี่ห้อเดียวกัน

**statement (EN):** When claim cards are checked by a *different* AI vendor from the one that
produced them (cross-vendor, independence level I3) instead of being re-checked by the same vendor
that produced the card (I0/I1), the rate at which undisclosed AI-fill (a false Q3 field) or
undisclosed assumptions (a false Q4 field) is caught rises measurably compared to same-vendor
re-checking.

**falsifier:** A controlled comparison (same set of claim cards, deliberately seeded with a known
number of undisclosed AI-fill/assumption instances, checked by same-vendor vs. cross-vendor
routes) shows no significant difference in detection rate, or shows cross-vendor checking performs
worse — that would falsify the independence-ladder mechanism this project's methodology cards
(`methodology/`) currently assume works.

**what evidence would separate it:** A seeded-error benchmark: N claim cards with a known,
logged set of deliberately undisclosed AI-fill/assumption instances, split into same-vendor-check
and cross-vendor-check arms, scored by detection rate with a pre-registered scoring rubric —
tiered `fit_calibrated` at best until run, `Dr` until then.

**Hypothesis derived with Readout Universe — Yaoharee Lahtee (lens, DOI
10.5281/zenodo.21529456); candidate proposed by AI, selection reserved to the founder.**

---

## Selection status

**Not selected.** Per Blackbox Note line 12 (correcting line 11; public log id
`BBL-2026-09-04-088`): *"...และ 'การเลือก'สมมุติฐานยังเป็นของเรา..."* — the selection among H1, H2,
H3 (zero, one, or more may be chosen; parked candidates are kept, never deleted) is reserved to the
founder and will be recorded in a future `hypothesis_selection.yaml` (S3c, per
`design/FOUNDATION_v0.5.md` §7.9), not in this file.
