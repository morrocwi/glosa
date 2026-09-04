# สรุปสำหรับ founder — เลือกสมมุติฐาน GLS-2026-001 (rigour-without-infrastructure)

**H1 (DESIGN)** — การ์ดข้ออ้าง 5 คำถาม + E-A-D + independence ladder ทำให้นักวิชาการเดี่ยวผลิตความรู้ที่ตรวจสอบได้โดยไม่ต้องพึ่งสถาบัน
- literature: เห็นด้วย 2 แหล่ง (diversity-epistemology, verification-cue), ต่างจริง 2 แหล่ง (boundary-work + Scholarly Kitchen ยังชี้ว่า credential ทำงานจริง), อ้างอิงเฉยๆ 3 แหล่ง (LLM-hallucination survey, SEA citizen-science, Thai TCIJ)
- gate: **accuracy=FAIL** (9/9 การ์ดยังแค่ METADATA_OK ยังไม่ผ่านตรวจอิสระ I3+/I5) · diversity=PASS_WITH_LIMITS (ภาษาอังกฤษ 89%, ทาง route เดียว)

**H2 (CONCEPTUAL)** — "ความเข้มงวด" เป็นคุณสมบัติของข้ออ้างเอง ไม่ใช่ที่สถาบันมอบให้
- literature: เห็นด้วย 2 แหล่ง (Freitag 2016, Srirot&Sohsomboon 2025 ไทย), ต่างจริง 1 แหล่ง (Scholarly Kitchen — falsifier ที่ใกล้เคียงที่สุดที่เจอ), orthogonal 6 แหล่ง
- gate: **accuracy=FAIL** (เหตุผลเดียวกับ H1) · diversity=PASS

**H3 (EMPIRICAL)** — ตรวจข้าม AI คนละยี่ห้อ (I3) จับ AI-fill/สมมติที่ไม่เปิดเผยได้ดีกว่าตรวจยี่ห้อเดียวกัน
- literature: เห็นด้วยบางส่วน 3 แหล่ง, แหล่งที่ทดสอบจริง (arXiv:2607.21656) พบผลไม่ชัดทางเดียว — ช่วยทางหนึ่ง แย่ลงอีกทาง
- gate: **accuracy=FAIL** (เหตุผลเดียวกัน) · diversity=PASS_WITH_LIMITS

**สรุปร่วม:** ทั้ง 3 สมมุติฐาน accuracy gate = FAIL เหมือนกันทั้งหมด เพราะการตรวจ claim-match ทุกใบยังทำโดย AI เซสชันเดียวกัน (I1) ยังไม่มีตรวจอิสระ (I3 ข้ามยี่ห้อ หรือ I5 คนนอก) — เป็นสถานะ FAIL ที่คาดไว้ ไม่ใช่ความผิดพลาด ตาม P13 ห้ามร่าง lit-review section จนกว่าจะมีตรวจอิสระจริง

ผมได้ร่าง `hypothesis_selection.yaml` แล้ว โดย pre-fill **chosen = H1** เพราะ H1 คือสมมุติฐานที่ abstract ของ founder เองบอกไว้อยู่แล้ว และ H2/H3 เป็นส่วนย่อยของ H1 (H2=แนวคิดข้างใต้ H1, H3=กลไกย่อยของ independence ladder ใน H1) — แต่ **นี่เป็นแค่ข้อเสนอของ AI ยังไม่ใช่การตัดสินใจของ founder**

## คำถามเดียวที่ founder ต้องตอบ
**เลือกสมมุติฐานไหน (H1 / H2 / H3 / มากกว่าหนึ่ง) เข้าสู่ genre router ต่อ — ยืนยันหรือแก้ `selection.chosen` ใน `hypothesis_selection.yaml`**
