# glosa — ความเข้มงวดโดยไม่มีโครงสร้างค้ำ (Rigour Without Infrastructure)

> **สถานะ: K0 — เผยแพร่สาธารณะเป็นฉบับทำงาน (timestamped, อ้างอิงได้, ยังไม่ผ่าน peer review, ยังไม่มีการตรวจสอบอิสระ)** (tier: Dr) · ทุกอย่างในนี้คือ readout ไม่ใช่ความจริงสุดท้าย

**glosa** (สเปนยุคกลาง: "คำอธิบายข้างขอบ" ที่นักปราชญ์เขียนแนบตัวบท) คือระเบียบวิธีสำหรับคนที่ไม่มีมหาวิทยาลัย ไม่มีแล็บ ไม่มีทีมวิจัย ที่จะผลิตความรู้จากพื้นที่ของตนเองร่วมกับ AI อย่างเข้มงวด โดยทุกข้ออ้างต้องตอบย้อนกลับได้ว่า **เราเห็นอะไรจริง · ข้อมูลแยกอะไรได้ · AI เติมอะไร · สมมติอะไรไว้ · เคยเจอหลักฐานหรือคำคัดค้านอิสระหรือยัง**

งานนี้ตอบแค่ 3 คำถาม: **แก้ปัญหาอะไร · ด้วยวิธีไหน · เพื่อนบ้านใกล้เคียงทำเหมือนหรือต่างอย่างไร** เราไม่อ้างความใหม่ ไม่แข่งกับอำนาจความรู้ และบอกไว้ว่าอะไรจะทำให้เราผิด


## Install (ติดตั้ง — one line, no ssh, no root)
```bash
curl -fsSL https://raw.githubusercontent.com/morrocwi/glosa/main/install.sh | bash
```
Then `glosa doctor` · Claude Code: `claude plugin marketplace add morrocwi/glosa` + `claude plugin install glosa@yaoharee-lahtee-glosa` (new session) · other AIs: `plugins/glosa/PROMPT_PACKET.md` · full guide: `INSTALL.md`.

## เริ่มอ่านที่ไหน
- มนุษย์: `design/FOUNDATION_v0.5.md` (รากฐานทั้งระบบ — ยังเป็นร่าง; สเปกเดียวที่ใช้งานจริง ดู `design/CURRENT_SPEC.txt`) → `templates/knowledge/blackbox_note.yaml` (บันทึกกล่องดำ: เสียงดิบ + การปรุง) → `templates/paper/` (LaTeX arXiv 1/2 คอลัมน์ compile แล้ว)
- AI ทุกยี่ห้อ: `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` (บล็อกเดียวกัน) และ `llms.txt`

## หาคำสั่งได้จากไหน (CLI discoverability)
ทุกคำสั่งที่ใช้งานได้จริงอยู่ในที่เดียว ไม่ต้องเดา: รายการเต็มอยู่ที่ `cli/README.md`, และ
`./cli/glosa --help` คือแหล่งความจริงที่เป็นปัจจุบันที่สุด (README อาจตกยุคได้ แต่ `--help` อ่านจากโค้ดตรง ๆ).
ตัวอย่างเริ่มต้น: `./cli/glosa intake new --project <name> --human-owner <you>`.

## ผู้ทำ
แนวคิดและทิศทาง: Yaoharee Lahtee (มนุษย์ ผู้รับผิดชอบ) · AI ช่วยสำรวจ ร่าง จัดโครง และตรวจฝ่ายค้าน (ดู `blackbox/`) — AI ไม่ใช่ผู้เขียน

## สัญญาอนุญาต
CC BY 4.0 ทั้ง repository (`LICENSE`)

---

## English (rewritten, not translated)
**glosa** is a methodology for people with no university, lab, or research team to co-produce rigorous knowledge with AI from their own ground. Every claim must answer five questions (what was actually seen · what the data separates · what the AI filled in · what was assumed · whether it has met independent evidence or objection), bound to the Readout Condition (existence / attribution / disclosure of every distinction). The work answers three questions only — which problem, by which method, how the nearest neighbours do it the same or differently — and makes no priority claim. Status: K0 public working release (timestamped, citable, not peer reviewed, no independent check), tier Dr. See `design/FOUNDATION_v0.5.md` (canonical spec pair: `design/CURRENT_SPEC.txt`).

### CLI discoverability
Every real command lives in one place — no guessing which doc is current: the full list is at
`cli/README.md`, and `./cli/glosa --help` is the up-to-date source of truth (it reads the live
argparse dispatch, so it cannot go stale the way prose can). Starting example:
`./cli/glosa intake new --project <name> --human-owner <you>`.

## Documents of record (v0.1.0)
- Paper PDF: `dist/glosa-paper-0.1.0-en.pdf` (EN) · `dist/glosa-paper-0.1.0-th.pdf` (TH, source of truth). Source: `paper/main_en.md`, `paper/main_th.md`.
- Blackbox Log (ปูมกล่องดำ, founder voice only, Thai): concept DOI 10.5281/zenodo.22302518 · local `blackbox/log/`.
- Installable skills: `plugins/glosa/skills/` (Claude plugin), `mcp/glosa_mcp_server.py` (MCP), `cli/glosa` (CLI). Toolchain list: `TOOLCHAIN.md`.
- K-state of this release: **K0** (public working release, timestamped, citable, not peer reviewed, no independent check). The Zenodo DOI in `CITATION.cff` resolves only once the record is published, which happens at the same time as the public push.
- Registry self-report: `registry/RESEARCH_REGISTRY.yaml` GLS-2026-001 is at `genre_routed`, not `released` — the state machine refuses to advance without an LRS manifest, and this paper has none (positioning table only). Known gap, stated by the tool itself.
