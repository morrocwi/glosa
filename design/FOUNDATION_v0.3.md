# Rigour Without Infrastructure — Foundation v0.3 (repo: glosa)

> **ARCHIVED — superseded by `FOUNDATION_v0.5.md` / `REPO_SPEC_v0.5.md`; kept for lineage. Do not use as current spec.**


> **Tier: Dr** (third-pass synthesis — fixes every must-fix item from two independent adversarial
> reviews of `FOUNDATION_v0.2.md`/`REPO_SPEC_v0.2.md`: `reviews/FOUNDATION_v0.2_anchor.md`
> (PASS_WITH_REVISION, 3 must-fix) and `reviews/FOUNDATION_v0.2_usability.md`
> (PASS_WITH_REVISION, 9 must-fix); one fixer, applying `design/CHAIR_RULING_v1.md`'s binding
> rulings where the reviews left a choice open. Not itself independently re-checked — this
> document must still pass a fresh `PUB-ADVERSARIAL-REVIEW` / MIMCG round before any of it is
> treated as settled).
> readout-not-truth applies to every line below: this is a *proposal*, not a ratified
> specification. Founder = research direction, core ideas, and every ruling cited below
> (Yaoharee Lahtee). AI (the AI assistant, fixer seat) applied all 12 must-fix items exactly per the chair's
> rulings below, and did not re-litigate anything already settled.
>
> **Repo name is `glosa`** (founder decision, `the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518)`
> §6 request 34 — founder picked option 2 of a ≤3-syllable list: *glosa* = a marginal gloss
> written beside the text). Repo already created at `~/ANSE.ASIA/glosa` (local Forgejo only, no
> public remote yet). The methodology keeps its full name, **Rigour Without Infrastructure** —
> only the repo, plugin, CLI, kernel module, and MCP server are named `glosa`.
>
> **License: CC BY 4.0 for the whole repository, single license** (founder decision, request 33 —
> supersedes v0.2's MIT-code/CC-BY-prose split). See §11 and `REPO_SPEC_v0.3.md`.
>
> **Read in full for this synthesis:** `design/FOUNDATION_v0.2.md` (999 lines, full), `design/
> REPO_SPEC_v0.2.md` (full), `reviews/FOUNDATION_v0.2_anchor.md` (full), `reviews/
> FOUNDATION_v0.2_usability.md` (full), `design/CHAIR_RULING_v1.md` (binding),
> `the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518)` §6 requests 33–34 (verbatim). Every other
> source v0.2 read (`FOUNDATION_v0.1.md`, `REPO_SPEC_v0.1.md`, `reviews/COMPLETENESS_CRITIC.md`,
> all twelve S8–S13 review passes, `sources/*`, `design/S0–S13`) is carried forward unread-again in
> this pass; nothing there is silently assumed changed.
> **Not read in this pass, same as v0.2 §12:** the 169/180 non-ancestor Zenodo records (listed, not
> interpreted — see §12), the full `anchor-v10.md` operating log beyond S12's spot-reads, the
> formal appendix of `READOUT_CONDITION_2026-08.txt`, and the PDF of that paper directly (the `.txt`
> extraction was used).

---

## 1. Positioning & lineage

### 1.1 What glosa is, in one sentence per binding rule (founder ruling, request 31d)

glosa answers exactly three questions and claims no more: **(1) which problem** — a person with no
university, no lab, no research team needs to know, for one claim at a time, what licenses them to
believe it (`the internal build plan (local file, not public)` §0); **(2) by which method** — a claim card that must answer the
founder's five questions, tied mechanically to the Readout Condition's Existence-Attribution-
Disclosure norm, gated by an independent-check ladder before anything is released; **(3) how the
nearest neighbours do it the same or differently** — `design/S13_neighbour-table.md`, a
descriptive comparison, never a priority contest.

**Founder ruling (request 31, 2026-09-04, binding, chair ruling A2):** *"เราไม่สนเรื่องใหม่ ...
เน้นไปที่เราเสนออะไรก็พอ เพราะเราไม่ได้แข่งขันใคร โลกผ่านจุดนั้นไปแล้ว — เป็นยุคการผลิตงาน"* — glosa states
what it proposes, what it builds on, and what would make it wrong; it does not claim priority and
does not compete with knowledge-authority (request 31b). Comparison language throughout this
document, the paper, and every schema is *same / different / cited* — never a claim that glosa
took, borrowed, or was first with anything — except when a human explicitly instructed adoption
(a Blackbox Note line or `DECISIONS.yaml` row must name it, request 31g–31i). This is why S13's
original collision-audit framing is superseded, not merely renamed: `design/S13_market-
collision-audit.md` stays on disk as the Dr-tier research readout it always was, and its content
now lives, restated in the required form, at `design/S13_neighbour-table.md` (§13 below, deliverable
3 of this synthesis round).

**Stance sentence, for the paper's own positioning paragraph (request 31b, verbatim target):** "We
are not competing with knowledge-authority and make no priority claim; we state what we propose,
what we build on, and what would make us wrong."

### 1.2 Relation to direct ancestors (macro vs micro, per `the internal build plan (local file, not public)` §1)

| Ancestor | Grain | What glosa takes | What glosa does not touch |
|---|---|---|---|
| **The Standalone Scholar** (Zenodo 10.5281/zenodo.22163849; skill `ai-native-scholarship v1.0.0`, PUB) | macro — scholar career architecture: K0→K3, DVP, conversion, dual-track, legitimacy | K-state ladder, DVP mechanics, Human Mastery Gate, SCRAM, legitimacy architecture — all `PRESERVE_EXACT`/`PRESERVE_FUNCTION` (ledger, §1.4). **Cited as a dependency by name + version + DOI (chair ruling B3), not merged into `plugins/`** — glosa re-derives only the protocol functions it needs, each row logged `PRESERVE_FUNCTION`/`EXPAND` in `lineage/RELATION_TO_STANDALONE_SCHOLAR.md`. | glosa's claim card is a **K0/K1-internal object**; it never claims to *be* K1, K2, K3, or a DVP run. |
| **The Readout Condition** (Aug 2026, not yet on Zenodo as of this session) | the epistemic engine — E-A-D, typed provenance DAG, identification ladder, defeater routing, silent lift | The founder named this "very important, must go into the paper" (request 4). glosa's Five Questions are a claim-grain instantiation of the paper's own "three practical questions." | glosa does not attempt to extend or re-prove the paper's formal propositions; it operationalizes them into a schema. |
| **Readout Universe / Readout Genesis** (PUB) | tier discipline, Lens Law, forced/borrowed/Open ledger | The 6-tier ladder (`Th_coqc/finite_diagnostic/fit_calibrated/Dr/definition/Open`), Lens Law as the mandatory `lens_translation` block before any Five Question is answered, and — **added this pass, chair ruling C7** — readout_genesis's `label_inflation_guard.py` (the tier-inflation lint) as a named lineage row, `PRESERVE_FUNCTION` into kernel rules 2–3 of §3.3. | — |
| **grr-epistemic-foundation** (local skill, upstream CC BY 4.0) | Claim Object / Evidence Relation / Warrant Profile vocabulary | The *pattern* (typed claim, typed evidence relation, warrant is multi-axis) — **not** its literal enum strings, independently re-derived (`claim_type`, §3.2). | — |
| **maker-checker-gate (MIMCG)** | L0–L5 consequence table, MC-01..05, release state machine | Every gate in §7 | — |
| **zero-readout-certifies** (PUB, DOI-carrying Coq companion) — **added this pass, closing `reviews/COMPLETENESS_CRITIC.md` §2's finding that this ancestor's own artifacts (`CLAIM_MATRIX.md`, `scripts/check_repo.sh`, `scripts/check_version.py`, the CITATION.cff/.zenodo.json/codemeta.json triple-consistency check, and an "AI-assistance disclosure" section) were reused near-verbatim in `REPO_SPEC_v0.1.md` with zero lineage tag** | `PRESERVE_EXACT`/`EXPAND` (chair ruling C7): the six-way HOLD-discipline boundary statement pattern, `CLAIM_MATRIX.md` as the `\claimref{}` resolution file, `check_repo.sh`/`check_version.py` as the version/consistency checkers, the CITATION/.zenodo/codemeta triple-equality check, and the AI-disclosure section as a required paper section | glosa does not adopt zero-readout-certifies' specific mathematical claims or Coq theorems — only the release/citation-hygiene mechanism. |

### 1.3 Master anchor-preservation ledger

Unchanged from v0.1 (the 17 Standalone Scholar invariants + Readout Condition mechanisms +
MIMCG mechanisms table) — every field-location reference in that table is still accurate against
this v0.2's schema, since none of the chair ruling's changes touch a field this ledger points to
by name other than `origin_r0_ref`/`origin_dialogue_ref` → `origin_blackbox_ref` (see §2.3, §3.2).
The full 17-row table, the Readout Condition mechanism table, and the MIMCG mechanism paragraph
from `FOUNDATION_v0.1.md` §1.3 (lines 64–101) are carried forward unchanged and are not
reproduced a second time here to avoid drift between two copies (one-fact-one-home); this
document's §1.3 **is** that table, verbatim, with one row updated:

| # | SS §2 invariant | Status | Where it now lives (v0.2) |
|---|---|---|---|
| 6 | DVP ≠ K2 | `PRESERVE_EXACT`, mechanized | Independence ladder I0–I5 (§4.2) + `k_state` gate requiring I5 for K2/K3 (§3.2) — **plus the bounded I2+I4 exception for a single-vendor scholar (chair ruling B4), which never opens a K2 door** |

All other 16 rows, the Readout Condition mechanism table, and the MIMCG mechanism paragraph are
unchanged from v0.1 §1.3 and are incorporated here by reference to avoid a second, driftable copy.

**glosa-original mechanisms** (no direct ancestor, all `Dr`-tier, unreviewed by anyone outside this
design round except by the chair's own ruling): the Independence Ladder I0–I5 (§4.2), the
Non-Collapse Table (Appendix A), the 9-genre router with cross-cutting `venue_track`/`companion_of`
attributes (§6, chair ruling B1), the Project Advisor role (§7.7), the Citation Integrity
subsystem generalized to distinction-grain (§7.8), and the **Blackbox Note** (บันทึกกล่องดำ,
§2.3 — renamed from "Register Zero / เสียงสด" by founder ruling, request 32, chair ruling A1).

---

## 2. The spine: ปัญหา → ประสบการณ์ → สมมติฐานวิชาการ → วิธีวิทยาเข้มข้น → paper → Zenodo/GitHub

### 2.1 The round-trip (founder request 20 — "the spine")

> *"เริ่มจากมองปัญหาด้วยเลนส์ readout ก่อน แล้วแปลกลับเป็นภาษาโลกเพื่อสกัดสมมติฐาน — อันนี้คือแกนเลยนะ"*

The spine is a **round trip**: a problem met in the world is translated **into** the readout
vocabulary first (lens-in, per the Lens Law), analysed there, then translated **back** into
world/discipline language to extract the academic hypothesis and its falsifier — with the lineage
of every term preserved so nothing is silently promoted.

```
World problem (Blackbox Note, บันทึกกล่องดำ — verbatim, untranslated raw lines)
        │  [lens-in: Lens Law — declare Q, X, R, Φ before touching evidence]     ┐
        ▼                                                                        │
Readout formulation (R1, internal stage label) ── analysis under E-A-D,          │  cooking:
        │  identification ladder, tier discipline                               │  log runs
        │  [lens-out: translate back into discipline language]                  │  alongside
        ▼                                                                        │  the whole
Academic hypothesis + falsifier (R2, internal stage label, world language)       │  spine —
        │                                                                        │  every
        ▼                                                                        │  transformation
Rigorous method (tiers, MIMCG, DVP, disclaimers) → paper (genre-routed)          │  appended,
        │                                                                        │  never sealed
        ▼                                                                        ┘
Zenodo + GitHub (K1)
```

The raw-voice box is named **Blackbox Note (บันทึกกล่องดำ)**, superseding "Register Zero (R0) /
เสียงสด" (founder ruling, request 32, chair ruling A1). R0/R1/R2 survive only as internal stage
labels inside the note's own `r1_readout_ref`/`r2_hypothesis_ref` pointers
(`design/templates/knowledge/blackbox_note.yaml`). The name states a sociology-of-knowledge
stance the founder specified directly: *"เพื่อแสดงความเป็นสังคมวิทยาความรู้ว่า การเข้าใจความรู้ต้องไปดู
ตอนที่มันเกิด และเราจะเก็บการปรุงมันไว้ในเอกสารตลอดไป"* — understanding a piece of knowledge requires
opening the box at the moment it was made, not reading only the sealed, polished result. The note
carries two parts, both published with the work, never sealed: (a) the raw verbatim lines
(unchanged from R0's rules — never edited in place, a correction is a new line), and (b) the
`cooking:` log — every later transformation (lens-in, analysis, lens-out, revision, translation,
review), by whom, which lines it drew on, and what distinction changed. Full schema:
`design/templates/knowledge/blackbox_note.yaml`.

### 2.2 Six stages, six owning artifacts, six gates

Unchanged from v0.1 §2.2 in structure and content, with one field-name substitution applied
throughout the co-production and gate columns: every occurrence of `origin_r0_ref`/`origin_
dialogue_ref` is now `origin_blackbox_ref` (§3.2, chair ruling A1/C8), and S5's exit gate now names
the appendix by its new title:

| Stage | Thai | Owns artifact | K-state at exit | Gate into next stage | Co-production split (request 24) |
|---|---|---|---|---|---|
| **S1 Problem intake** | ปัญหา | Problem Card (`schema/problem_card.schema.json`) | K0 | Two-question intake complete; standpoint declared; readiness verdict `READY_FOR_S2` (self-check, not a release gate) | Human: states the issue, own words, own standpoint. AI: routes the intake, never infers Q2's answer. |
| **S2 Experience → record** | ประสบการณ์ | Source Card + Observation Card + `logbook.jsonl` | K0 | `access_type` typed (including `provenance_indeterminate`); `scope.generalization_claimed` never advanced past `none` at this stage | Human: is the observer/source of record for anything human-participant. AI: may transcribe under `access_mode: ai_assisted_capture`, never sole observer of a human-participant event. |
| **S3 Hypothesis via readout lens** | สมมติฐานวิชาการ | Claim Card (§3, the canonical schema) | K0 | `lens_translation` filled before `five_questions`; `non_claims` non-empty; `tested.falsifier` non-empty and names an observation, not a negation | Human: owns the falsifier judgment and the standpoint. AI: fills `ai_filled.*`, discloses every inferential commitment it contributed. |
| **S4 Rigorous method** | วิธีวิทยาเข้มข้น | `review_report`, `evidence_relation`, disclaimer set attached | K0→K1 (only with ≥I3, §4.2, subject to the bounded I2+I4 exception, chair ruling B4) | MIMCG gate table (§7.1) passed at the consequence level the artifact reaches | Human: is Checker or Approver whenever the artifact reaches L3+; never the same identity as Maker. AI: may be Checker only at I2/I3 (never sole gate to K1 without an I3 route; never K2 alone). |
| **S5 Paper / genre** | เปเปอร์ | Genre-routed manuscript (§6), Claim Matrix, Blackbox Note appendix | K1-candidate | Human Mastery Gate (§7.5) `PASS`/`PASS WITH NAMED GAPS`; every `\claimref{}` resolves in the Claim Matrix; **"Blackbox Note: how this work was made" appendix present** (hard gate, request 28/32) | Human: defends the paper unaided (Human Mastery Gate). AI: drafted structure/prose under disclosed route, never the mastery-gate answer itself. |
| **S6 Publish / archive** | บันทึกเข้า Zenodo/GitHub | Release manifest, CITATION.cff/.zenodo.json/codemeta.json, Zenodo DOI | K1 (published) | `PUB-ADVERSARIAL-REVIEW` R1–R7 (§7.4) passed; version triple-equality (`PRESERVE_EXACT` from zero-readout-certifies, §1.2); PR-only merge | Human: founder is the non-delegable Approver and sole formal author. AI: attribution lives only in commit trailers, AI-assistance disclosure, and `ai_filled` fields — never in `CITATION.cff` authorship. |

### 2.3 Blackbox Note and R0/R1/R2 internal registers (founder ruling, request 32, supersedes request 30's "Register Zero")

Three internal stage labels, all retained, never collapsed into one polished version, all living
inside one note:

- **Blackbox Note (บันทึกกล่องดำ) — raw human voice + cooking log.** Verbatim, untranslated, typos
  kept, timestamped, speaker-by-role. Template: `templates/knowledge/blackbox_note.yaml` (ids
  `BB-YYYY-MM-DD-NN`). Never edited in place; a correction is a new line. Tier `positional/Dr`.
  Selection into any published appendix is done by the human owner of the voice; AI may propose
  candidates only (`ai_proposed: true`).
- **R1 — Readout formulation** (internal label, lives inside the note's `r1_readout_ref`). The
  lens-in translation: `lens_translation.question_readout`, `local_contrast_space_X`,
  `access_relation_R`, `claim_function_Phi_z0` (the `lens_translation` block of the Claim Card,
  §3.2 — `question_readout` is the field name; earlier drafts called this `question_Q`, retired
  this pass, must-fix 5, to stop it being conflated with §3.1's unrelated "founder's Q1..Q5").
- **R2 — World-language hypothesis** (internal label, `r2_hypothesis_ref`). The lens-out
  translation: the top-level `hypothesis_world` field (§3.2) — the academic hypothesis + falsifier
  in the discipline's own words, pointing via `hypothesis_world.falsifier_ref` to `five_questions.
  tested.falsifier`, and carrying a pointer back through R1 to the Blackbox Note
  (`origin_blackbox_ref`, §3.2).

Refinement 25b (founder): the **human-language research question itself** is stored and published
alongside its formalizations — a "Question as lived / Question as readout / Hypothesis" block in
the paper, never only the polished form, realized this pass (must-fix 5) as three exact,
named fields in §3.2, one home each: **`lens_translation.question_human`** (`{text_verbatim,
language, blackbox_line_ref}` — the question as lived, verbatim, pointing at its Blackbox Note
line), **`lens_translation.question_readout`** (R1, the Lens Law's contrast-question — the
existing field previously named `question_Q`; one home, this is where it lives), and the
top-level **`hypothesis_world`** (R2, `{text, language, falsifier_ref}`). Before this pass these
three names appeared only in this prose paragraph and not in §3.2's actual field list — `reviews/
FOUNDATION_v0.2_usability.md` finding (l) named this a direct, uncaught contradiction between two
sections of the same document; it is closed by the field additions in §3.2. Worked demonstration:
`cases/worked-example-cat.md` (the "ทำไมแมวเยี่ยวไม่เป็นที่" round-trip, request 26).

### 2.4 Preserved human experience (request 25) and the mandatory Blackbox Note appendix (requests 28, 32)

Two related, distinct obligations, both binding on every genre (§6):

1. **The lived experience that led to the research is preserved, typed, never deleted** — a
   first-person "context of discovery" record. Tier `Dr`/positional, tagged `SelfExperience ≠
   GeneralEvidence` (`NC-64`, Appendix A — id newly assigned this pass per chair ruling C6). Lives
   in S2's Observation Card and in a per-genre field/section on the structure column (§6.2, closing
   the gap `reviews/S11_anchor.md` Must-fix 2 found: v0.1 named this obligation in prose but did
   not give every genre's own structure column a place for it).
2. **Mandatory appendix "Blackbox Note: how this work was made"** (request 28/32, founder: *"ทำให้
   เป็นเกณฑ์บังคับ"*) — every glosa paper carries this appendix or **fails the release gate** (§7.4).
   It is a **curated** subset of Blackbox Note lines (only lines with a `became:` forward link,
   request 30b: *"กระชับและเท่าที่จำเป็น"*), verbatim, dated, by role, **plus the cooking log entries
   relevant to those lines** (request 32's requirement that the cooking is published, never
   sealed). This session's own founder↔the AI assistant exchange (`sources/DIALOGUE_2026-09-04_founder-
   fable_DRAFT.md`) is the first instance, not yet public pending the founder's line-by-line
   selection.

### 2.5 Bilingual handling (binding rule)

Unchanged from v0.1 §2.5: Thai is the source of truth wherever the founder or a user wrote in
Thai; English is a rewrite of meaning, never a translation of words. Every bilingual field carries
`{th, en, translation_status: missing|machine|reviewed|verified}`. `translation_status` never
silently advances. Blackbox Note lines are never translated in place.

---

## 3. The claim card — final schema field list

One claim-level distinction = one card, in one of two legal shapes (chair ruling B2, resolving
v0.1 §10 dispute 2). `scripts/validate_claim_card.py` (kernel) is the *only* enforcement point; no
other file may redeclare a field name.

### 3.1 Five Questions ⇄ E-A-D ⇄ field (binding crosswalk, one map)

| # | Founder's question | Readout Condition principle | Claim card field group | Mechanically checkable? |
|---|---|---|---|---|
| Q1 | เราเห็นอะไรจริง | **E — Existence** (Principle 7): every load-bearing distinction has *some* provenance path, or is marked provenance-indeterminate | `five_questions.seen` | Presence + shape only |
| Q2 | ข้อมูลแยกอะไรได้ | The licensing test itself (fiber constancy / pointwise neighbourhood / access admissibility) — what R *alone* distinguishes | `five_questions.separates`, `zero_vs_bottom` (0 ≠ ⊥, never collapsed) | **Presence-checkable only, not correctness-checkable** (chair ruling D2, stated here rather than only in §12) — the kernel can confirm the field is non-empty and `zero_vs_bottom` holds a valid enum value; it cannot confirm the licensing test's *result* is correct. This is `Mechanical validity ≠ Semantic validity` (`NC-17`) applied to glosa's own validator. |
| Q3 | AI เติมอะไร | **D — Disclosure** applied to the six-way AI-audit split | `five_questions.ai_filled` | **Presence-checkable only** (chair ruling D2) — the kernel can confirm every sub-field is explicit ("none identified" or filled), not that the AI's self-report is complete or honest. `silent_lift_check` is the only mechanized cross-check, and it compares *represented* against *actual* dependency sets computed from the provenance DAG, not from re-doing the epistemic work by hand. |
| Q4 | สมมติอะไรไว้ | **A — Attribution** and Disclosure of every non-source node (identification ladder) | `five_questions.assumed[]` + `identification_ladder` | **Presence-checkable only** (chair ruling D2) — the kernel can check that listed assumptions carry an `identification_level`; it cannot prove the list is complete (there is no mechanical test for an assumption that was never entered at all). |
| Q5 | เจอหลักฐาน/คำคัดค้านอิสระหรือยัง | Essential dependency set + defeater routing, realized as an Evidence Relation bundle + Independent Check | `five_questions.tested` + `independent_check` | **The one genuinely mechanically enforceable question** (chair ruling D2) — the pairwise-distinct maker/checker/approver check (§7.2) and the tier-vs-independence-class gates (§3.3) are structural, payload-level checks the kernel can run without semantic judgment. This is exactly why the independent check exists: it is the licensed route to closing what Q2/Q3/Q4 cannot mechanically close on their own. |

The Readout Condition is E∧A∧D: a card that answers Q1/Q2/Q4 honestly but misattributes Q3 —
crediting the source with a distinction AI actually supplied — fails the condition even though
every field looks filled. `silent_lift_check` is the mechanized test for exactly this.

### 3.2 Field list

```
claim_card:
  schema_version: "0.4.0"                          # bumped from v0.2's 0.3.0 this pass — the new
                                                    # `question_human`/`question_readout`/
                                                    # `hypothesis_world` fields, the stub `ai_filled`
                                                    # fixed shape, the `disclaimers_emitted` shape
                                                    # change (bare-string array → `{id, params?}`
                                                    # objects), and the `provenance_dag`/
                                                    # `silent_lift_check` `status` fields are breaking
                                                    # changes against v0.2's own schema (must-fixes
                                                    # 5, 9, 10, 12). Earlier bump, v0.1's 0.2.0 →
                                                    # v0.2's 0.3.0, was for origin_blackbox_ref,
                                                    # shape:stub|full, and companion attributes.
  claim_id: string                                 # GLOSA-CC-YYYYMMDD-NNNN
  shape: stub | full                               # chair ruling B2 — see §3.2a for the legal-shape rule
  statement: { language: th|en, text, is_verbatim_quote: bool,
               translation: { text, language, translation_status } }
  standpoint: { declared_basis, disciplines_not_claimed[], method_basis }
  claim_type: EMPIRICAL | FORMAL | INTERPRETIVE | NORMATIVE | CONVENTIONAL_LEGAL | DECISION |
              SOCIAL | HUMAN_PARTICIPANT
                                                    # independently re-derived taxonomy, not copied
                                                    # verbatim from any private skill's exact enum
  genre: <one of the 9 §6 genre ids> | MIXED_GENRE
  venue_track: international | thai_tci | none      # `none` added this pass (must-fix 8, usability
                                                    # review finding (d)) — K0 work never headed to
                                                    # any venue is not forced into a publication-track
                                                    # choice. chair ruling B1's cross-cutting attribute,
                                                    # replaces v0.1's separate genre rows 1/2
  companion_of: <artifact id> | null                # chair ruling B1 — this artifact is a companion
                                                    # rendering of another artifact, any genre
  produced_by: human | ai | joint                  # request 24 — co-production visibility
  responsible: human                               # const; non-delegable
  origin_blackbox_ref: string | null                # chair ruling A1/C8 — replaces origin_r0_ref
                                                    # AND origin_dialogue_ref with one field, one home
  lens_translation:
    question_human: { text_verbatim: string, language: th|en, blackbox_line_ref: string }
                                                    # NEW this pass (must-fix 5) — the human-language
                                                    # research question, verbatim, dated via the
                                                    # Blackbox Note line it points to. This is the
                                                    # field §2.3's "question_human" promise resolves to;
                                                    # it was previously undeclared anywhere in §3.2
                                                    # (usability review finding (l)).
    question_readout: string                        # = the Lens Law's own contrast-question. One
                                                    # home, one name (must-fix 5): this field is what
                                                    # earlier drafts and §3.1's founder-Q crosswalk both
                                                    # called `question_Q` — `question_Q` is retired as a
                                                    # field name to stop the two unrelated "Q"s
                                                    # (founder's five questions Q1..Q5 in §3.1, and this
                                                    # Lens Law question) from being conflated on the
                                                    # page (usability review finding (e)). Any prior
                                                    # reference to `lens_translation.question_Q`
                                                    # elsewhere in this document means this field.
    local_contrast_space_X: [string, minItems 1], restriction_provenance: string|null,
    access_relation_R, claim_function_Phi_z0,
    formal_applicability: exact_functional | relational_pointwise | stochastic | not_applicable_narrative
                                                    # four values DEFINED in plain language at §3.2b
                                                    # this pass (must-fix 6) — previously undefined
                                                    # anywhere in the read set (usability review's
                                                    # "single worst usability gap").
  hypothesis_world: { text: string, language: th|en, falsifier_ref: string }
                                                    # NEW, top-level, this pass (must-fix 5) — the
                                                    # lens-out academic hypothesis in world/discipline
                                                    # language, pointing to `five_questions.tested.
                                                    # falsifier`. Resolves §2.3's "hypothesis_world"
                                                    # promise, previously also undeclared in §3.2.
  five_questions:
    seen: { record_ref, as_of, retrievable_original: bool, access_model, citation_refs: [citation_card.id] }
    separates: { value_z0, licensing_test: { regime, result, notes }, zero_vs_bottom: 0_checked_no_difference | distinct_difference_found | unresolved_bottom }
    ai_filled: { current_evidence, retrieved_tool_evidence, retained_record_route,
                 model_calibration_assumption, prompt_system_constraint, decision_policy }
                                                    # every field explicit "none identified", never omitted
                                                    # — full-shape only; the stub shape's collapsed
                                                    # `ai_filled` has its own shape, §3.2a.
    assumed: [ { id: "A#", type: access_augmentation | contrast_relevance_operation |
                 inferential_commitment | decision_policy_augmentation, description,
                 identification_level: "A0".."Am" | unidentified, contaminated_concept_hit } ]
    tested: { evidence_relations: [ { evidence_id, bearing: SUPPORTS|CHALLENGES|NEUTRAL|UNRESOLVED,
                independence_class: <I0..I5, §4.2>, strength, citation_ref } ],
              falsifier: string (required, non-empty, must name an observation/check outcome),
              dissent_records: [ { by, date, content, resolved: bool } ] }   # append-only
  identification_ladder: { layers: [{id, adds}], per_rival: [{rival, first_identification_level}] }
  provenance_dag: { nodes: [{id, kind}], edges: [{from,to}],
                    essential_dependency_set: [string],  # computed by validator, never hand-typed
                    defeater_log: [{node, date, outcome}],
                    status: not_run | run }              # NEW this pass (must-fix 12) — default
                                                    # `not_run`; see §3.3 rule on this field below.
  silent_lift_check: { represented_dependency_set: [], actual_dependency_set: [], flags: [],
                        status: not_run | run }           # `status` NEW this pass (must-fix 12) —
                                                    # non-empty flags = hard fail, blocks status advancement.
                                                    # default status `not_run`.
  scope: { generalization_claimed: none | pattern_candidate | population_claim,
           evidence_scope: string, claim_scope: string }
                                                    # kernel rule: claim_scope may not exceed evidence_scope
  tier: Th_coqc | finite_diagnostic | fit_calibrated | Dr | definition | Open
  k_state: K0 | K1 | K2 | K3
  ledger: { forced: [string], borrowed: [string], open: [string] }
  non_claims: [string]                             # required, minItems 1
  legal_epistemic_separation: { applicable: bool, notes: string }
  independent_check:
    status: NONE | PENDING | PASSED | FAILED
    maker_id, checker_id, approver_id: string       # MC-01: kernel requires these pairwise distinct
                                                    # whenever status advances past Pending Review
    independence_class: I0 | I1 | I2 | I3 | I4 | I5  # §4.2 — ONE string ladder in every schema
                                                    # (chair ruling C1); ordinal is a derived mapping
                                                    # in the kernel only, never a second schema field
    mc_level: L0 | L1 | L2 | L3 | L4 | L5
    date, expires_at: date | null                  # approvals expire (MC's T4); null only at L0/L1;
                                                    # ALSO the bounded I2+I4 exception's own
                                                    # expiry (chair ruling B4, ≤90 days) uses this field
  disclaimers_emitted: [ { id: <D-* id, §5>, params: object | omitted } ]
                                                    # NEW shape this pass (must-fix 10) — was a flat
                                                    # array of bare ids; could not represent a
                                                    # parameterized disclaimer (`D-INDEPENDENCE-LEVEL`
                                                    # with `level`, `D-CITATION-UNVERIFIED` with
                                                    # `state`, or HANDOFF's own worked-example wording
                                                    # "D-SCOPE(n=1)") — usability review Must-fix 7.
                                                    # `params` is omitted (not an empty object) when the
                                                    # id carries no parameter.
  status: Draft | Pending Review | Approved-for-Test | Approved-for-Live | Monitor | Rollback
  lineage: { derives_from: [], supersedes: [], superseded_by: null }
  related_source_cards, related_observation_cards, related_citation_cards: [string]
  human_owner: string, minLength 1                 # non-delegable
  revision_history: [ { rev, date, by, note } ]
```

### 3.2a Two legal shapes, one schema (chair ruling B2)

Resolving v0.1 §10 dispute 2 (founder request 1 — "an ordinary person with no lab/team can open
this and start working immediately" — against schema purity), the claim card has exactly two legal
shapes, both validated by the same `claim_card.schema.json`:

- **`shape: stub`** — legal for K0 work and for any card **not** foregrounded in a paper. A stub
  requires only: `statement`, `standpoint`, `tier` (must be ≤ `Dr`), one `tested.falsifier`,
  `non_claims` (≥1), `origin_blackbox_ref`, `ai_filled` collapsed to the fixed shape defined below,
  and `produced_by`. Every other field group may be `null`/absent. **Kernel rule: a stub cannot be
  cited publicly and cannot advance `status` past `Draft`.** This is the guard against the founder's
  own worry — that the full schema's authoring cost would make a frontline user simply not use the
  tool, defeating `the internal build plan (local file, not public)` §0's purpose — while still preventing a stub from silently leaking
  into a published claim (the "silent lift" risk Position A of the original dispute named).
  - **Stub `ai_filled` shape (defined this pass, must-fix 9 — usability review finding (b) found
    this shape previously unstated, so two frontline users would each invent a different one):**
    ```
    ai_filled: { used: bool, note: string }
    ```
    `note` is **required whenever `used: true`** (one line, plain language — e.g. "AI proposed the
    box-condition hypothesis; owner supplied every observation and the falsifier judgment") and may
    be an empty string when `used: false`. This is the *only* legal shape for a stub's `ai_filled`;
    `schema/claim_card.schema.json` validates against exactly these two keys, nothing else, for any
    card where `shape: stub`. It is deliberately not the six-field full-shape `ai_filled` (§3.2) —
    a stub's whole purpose is lower authoring cost.
- **`shape: full`** — required for any card cited in a CLAIM_MATRIX, any card reaching tier ≥
  `fit_calibrated`, and any card leaving the repo (reaching K1). All field groups in §3.2 are
  populated (with explicit "none identified" where empty is honest, never a silent omission).

### 3.2b `formal_applicability` — plain-language definitions (must-fix 6)

Previously the four enum values were used in §3.2 but defined nowhere in any document a frontline
user or a fresh AI session could read — `reviews/FOUNDATION_v0.2_usability.md` called this "the
single field a frontline user has the least chance of filling correctly," since the correct
definitions lived only in the Readout Condition's formal appendix, which this document's own §12
admits was never read even by the synthesizer. Fixed here, in plain language, no formal-appendix
read required:

| Value | Plain-language meaning | Who may assign |
|---|---|---|
| `exact_functional` | A **deterministic reading**: the same input always produces the same value under the access relation `R` — no ambiguity, no noise, repeatable in principle by anyone using the same `R`. | Any user who has actually checked repeatability, or by default when the claim is a formal/mechanical readout. |
| `relational_pointwise` | Readings that **cannot be told apart within a neighbourhood** — two nearby inputs may or may not yield distinguishable outputs under `R`, and the relation is **non-transitive** (A indistinguishable from B, B indistinguishable from C, does not imply A indistinguishable from C). Typical of fine-grained perceptual/behavioural distinctions. | A checker who has verified the non-transitivity property applies here, or an I3+ route. |
| `stochastic` | **Noisy or probabilistic readings** — the same input can produce different values across repetitions, and only a distribution, rate, or confidence interval is meaningful. | Anyone reporting measured variance/frequency data. |
| `not_applicable_narrative` | **No formal readout structure at all** — a narrative, interpretive, or positional claim with no access relation `R` and no repeatable value `z0` to speak of. | **Default for a frontline user** (rule below). |

**Rule (usability-first default, must-fix 6):** a frontline user filling this field for the first
time, or anyone unsure, **defaults to `not_applicable_narrative`** — this is always a legal,
honest choice for any claim, since every claim can be read narratively even when a formal reading
also exists. A checker at I2+ may **upgrade** the value to one of the other three when they have
verified the claim actually has the corresponding formal structure; a checker may never *downgrade*
a value a maker chose without recording why in `revision_history`.

### 3.3 Kernel gate rules (specified, Dr, untested)

**Heading renamed from v0.1's "the fixes — these are what 'final' means here" (chair ruling D1):**
every rule below is *specified*, not *implemented*. None of it has been run through `jsonschema`,
instantiated against a real example, or tested against the deliberate-FAIL fixtures §9 names.
`reviews/COMPLETENESS_CRITIC.md` §5 found the old heading's "fixed here, not left open" language
sat 550 lines from its own untested-prose disclaimer in v0.1's §12 — this heading states the honest
status at the point of first claim, per `D-AIFILL`'s own placement rule ("never one blanket
paragraph, far from the claim it discloses").

Convergent reviewer findings across S3/S4/S7 showed the schemas as drafted let a **solo AI
session** reach `tier: Th_coqc`, `k_state: K2`, and `status: Approved-for-Live` with **zero
humans and zero mechanical artifacts involved**, directly contradicting `DVP ≠ K2` and MC-05.
These rules are the specified fix:

1. `independent_check.status` may be `PASSED` only when `independence_class ∉ {I0, I1}` (MC-02).
2. `tier: Th_coqc` requires ≥1 `evidence_relation` with `independence_class == I4` (a proof kernel
   run, `Print Assumptions` disclosed) **or** `I5` confirming a formal artifact — never `I3` alone.
3. `tier: finite_diagnostic` requires ≥1 `evidence_relation` with `independence_class ∈ {I4, I5}`
   supplying a reproduction command or retrievable original. An `I3` (cross-vendor AI) route may
   *corroborate* a mechanical result but does not itself license the tier (Bounded-Judge Law, §7.3).
4. `k_state` may be `K2` or `K3` only when ≥1 `evidence_relation` has `independence_class == I5`
   (external human, non-founder), **or**, under the bounded exception (chair ruling B4), a claim
   may reach `K1` only — never `K2` — via I2+I4 with `D-SAME-VENDOR` and a live
   `independent_check.expires_at` ≤ 90 days from `date`; past expiry, either an I3+ route replaces
   it or the card drops to K0. No stacking of I0–I4 routes ever opens the K2 door (`DVP ≠ K2`).
5. `status` may advance past `Pending Review` only when `maker_id`, `checker_id`, and `approver_id`
   are pairwise distinct (MC-01) — checked on the payload directly, not on a caller's self-declared
   role.
6. `scope.claim_scope` may not exceed `scope.evidence_scope` (kernel string-containment/human-
   reviewed check, `Claim scope ≤ Evidence scope`).
7. `silent_lift_check.flags` non-empty is a **hard failure**, blocking `status` advancement — not a
   disclaimer.
8. A full-text scan of `statement`, `assumed[].description`, and `ledger.*` against the
   contaminated-concept table (Appendix C) fires `EXTERNAL_VALIDATION_PROPOSED` as a **hard fail**
   whenever text proposes "getting external review to confirm this" as a legitimacy lever
   (`EPIS-KNOWLEDGE-VALIDATION`).
9. **`k_state` may be `K1` only when ≥1 `evidence_relation` has `independence_class ≥ I3`, OR the
   bounded B4 exception holds (both an `I2` and an `I4` route present in `tested.evidence_relations`,
   `D-SAME-VENDOR` present in `disclaimers_emitted`, and `independent_check.expires_at` ≤ 90 days
   from `date`)** (chair ruling item 1, new this pass — the rule that had been missing since v0.2,
   the exact gap `reviews/FOUNDATION_v0.2_anchor.md` Must-fix 1 found: §4.2's own table and §2.2's
   stage-gate both already stated this bar in prose, but no numbered kernel rule enforced it, and
   §6.4's independent bullet contradicted it at a weaker `≥ I2` threshold. This rule and the §6.4
   fix below close both halves of that gap together — see §6.4.). Rule 4 above continues to gate
   K2/K3 only; this rule is its K1-side twin, closing the "solo AI reaches K-anything with zero
   humans" bug this section's own opening paragraph names as the thing rules 1–9 are meant to fix.
10. **`shape: stub` cards fail `status` advancement past `Draft` and fail any citation-check that
   looks them up from a CLAIM_MATRIX** (chair ruling B2 — renumbered from rule 9 to rule 10 this
   pass to make room for the K1-floor rule above).
11. **`provenance_dag.status` and `silent_lift_check.status` must both be `run` before `k_state`
   may advance past `K0`, or before a card may be cited from a CLAIM_MATRIX** (chair ruling item
   12, new this pass). Default value for both is `not_run`. The kernel treats `not_run` as **⊥
   (unknown)**, never as "checked, nothing found" (`NC-25`/`NC-26` applied to the kernel's own
   gate, not just to citation search coverage) — a card sitting at `not_run` is honestly
   incomplete, not honestly clean. This closes the gap `reviews/FOUNDATION_v0.2_usability.md`
   finding (h) found: before this pass, a user had no legal way to leave
   `provenance_dag.essential_dependency_set`/`silent_lift_check.*` unfilled pre-kernel that was
   visibly distinguishable from a checked-and-clean result.

---

## 4. Tier + independence-class + K-state vocabulary

One table, per founder request 21. This resolves the 4-way type fork (string vs. integer, 5 vs. 6
values, different casing) that S3/S4/S7 independently produced, plus the S10-specific fork the
chair ruling closes below (C1).

### 4.1 Tier ladder (six values, never collapsed)

| Tier | Meaning | Who may assign |
|---|---|---|
| `Th_coqc` | Machine-checked, axiom-free | Only with independent_check §3.3 rule 2 |
| `finite_diagnostic` | Measured/computed, finite, reproducible by a named command | §3.3 rule 3 |
| `fit_calibrated` | A model fit/calibrated to data; holds within the fit's declared domain | Calibration set + domain named as an inferential-commitment node |
| `Dr` | Declared bridge / human-AI narrative synthesis — the default | Default, downgrade-safe |
| `definition` | Stipulative — true by declaration | Naming conventions only |
| `Open` | Not established; a rival unidentified or a defeater emptied the essential path set | Forced automatically by the identification ladder or Proposition-3-style defeat |

### 4.2 Independence Ladder I0–I5 (chair ruling on request 18 — one string ladder, every schema)

**Convergence fix (chair ruling C1):** `independence_class` is the string ladder `I0..I5` in
*every* schema that carries it — claim card, evidence relation, review report, citation card, kg
edge. Any 0–5 ordinal (S4's original type, or an MIMCG "class" number) is a **derived mapping
computed in the kernel only**, never a second schema-level field.

| Level | Definition | Can raise | Cannot raise | K-state ceiling | MIMCG class (derived ordinal, never a second schema field) |
|---|---|---|---|---|---|
| **I0 — Self** | Same session re-reads its own output | Nothing; not a `tested:` entry at all | `tier`, `k_state` | K0 | 0 |
| **I1 — Same model, new session** | Fresh conversation, identical model | L1 "2nd reader" only | L2+ DVP minimum; K1 floor | K0 | 1 |
| **I2 — Same vendor, other model** | Different model, same vendor | One DVP route toward L2's ≥3 minimum; part of the bounded exception (below) | K1 floor alone (I3 or the bounded exception required); `Th_coqc`/`finite_diagnostic` alone | K0→K1 only combined with I3+, or the bounded I2+I4 exception | 2 (weak) |
| **I3 — Different vendor** | Materially different model family/vendor | **Founder-set minimum bar for K1 public-provisional** — but a minimum, never sufficient on its own (chair ruling B4, fixing S10's "sufficient" wording). `finite_diagnostic`/`Dr` where routes reproduce a mechanical result | **Never K2** (`DVP ≠ K2`); never `Th_coqc` alone | K1 (floor), never K2 | 2 (strong) |
| **I4 — Mechanical / original-record** | Proof kernel, executed test, schema validator, direct original-source lookup | `Th_coqc` (proof) or `finite_diagnostic` (executed, reproducible); paired with I2 under the bounded exception below | K-state alone (no human friction occurred) | K1 unless combined with I5 | 3 |
| **I5 — Independent external human (non-founder)** | A person outside this session's authorship | **The only route to K2** (and, with formal/empirical constraint, K3) | — | K2/K3 | 4 |
| *(orthogonal)* Founder as Approver | Release authority, never a verification level | Authorizes release | Never substitutes for I5 as a check | — | 5 |

**Ordering rule:** the maximum claim tier a route set can support is bounded by the *highest*
independence level actually reached, never by the count of routes at a lower level
(`ManyModels⇏Independence`, NC-31, Appendix A).

**Bounded I2+I4 exception (chair ruling B4, new this pass — I3 stays the K1 floor, this is the one
carve-out).** If a scholar can reach only one vendor, a claim may be published at **K1 only** with
I2 **plus** an I4 mechanical/original-record check, carrying `D-SAME-VENDOR` and `independent_
check.expires_at` ≤ 90 days from `date`. After expiry, either an I3+ route replaces it or the card
drops to K0. I3 remains a *minimum*, never a sufficient condition by itself (§3.3 rule 3's
Bounded-Judge Law already enforced this for tier; this exception is the K-state-side analogue,
narrowly scoped so it never opens a route to K2).

**Local-model DVP route (chair ruling B5, new this pass, resolving v0.1 §10 dispute 5).**
Best-effort, never mandatory — hardware constraints (e.g. a 4GB GPU too small for a competitive
local model) are real and acknowledged. A local-model route counts as **I3** only when its model
family is vendor-distinct from every other route already in the set; otherwise it is treated as an
**I2** route in the Route Dependence Matrix, subject to the same rules as any other same-vendor
route.

### 4.3 DVP mechanics (the engine behind I2/I3)

Route Dependence Matrix (`templates/knowledge/route_dependence_matrix.yaml`): `route_id, vendor,
model, prompt_ancestry, operator, evidence_base, external_anchor, shared_with[], independence_
level`. **Disagreement Ledger — Resolve or Declare**, never averaged, never silently dropped
(`nature: construct|source|mechanism|boundary|venue|epistemic_tier`; `outcome: RESOLVED|DECLARED`;
`RESOLVED` requires a `decisive_record`, never null). **Per-project home, one merged view (chair
ruling B6, new this pass):** `DISAGREEMENT_LEDGER.md` and `XENON_LEDGER.md` (§7.8) each live inside
their owning project directory (one problem = one project, §8.1), append-only; `glosa kg merge`
renders the repo-wide view from all project ledgers — the same pattern already used for the kg
(one home per project, one union view), closing v0.1 §10 dispute 6.

**Operator-Decorrelation Control**: pre-committed acceptance criteria frozen before any route runs;
blind route identity when handed to a synthesizing role; randomized presentation order; a **Query
Stop Rule** (one recorded attempt per acceptance-criteria version — re-asking until a route agrees
is a named SCRAM condition, §7.7). Role library, reused verbatim, not renamed: **Advocate,
Nearest-Concept Prosecutor, Falsifier, Source Auditor, Hostile Reviewer, Translation Reviewer,
Method/Empirical Designer** — any DVP set backing an I3 claim requires ≥1 Falsifier or Hostile
Reviewer.

**Vendor-neutral execution** (request 13): a plain Markdown/YAML prompt packet
(`templates/knowledge/cross_vendor_review_packet.md`) dropped at
`reviews/routes/<claim_id>/<route_id>/PACKET.md`; any agent — the AI coding tool, Codex, Gemini CLI, a
local model — reads it and writes `review_report.yaml` back, no shared session or orchestration
tool required. Identical gate block ships in `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` at repo root:

```
## glosa cross-vendor review gate
If you were pointed at a file under reviews/routes/*/PACKET.md: you are one route in a
Decorrelated Verification Protocol. Read ONLY your assigned packet — do not read other routes'
review_report.yaml, do not read the claim's authorship history beyond the packet. Fill in
review_report.yaml exactly to schema/review_report.schema.json. State your verdict's tier
explicitly (Bounded-Judge Law) — an untiered verdict is invalid. Do not edit the claim card. Do
not re-run your role on the same claim without a new PACKET version (Query Stop Rule).
```

### 4.4 K-state (Standalone Scholar, `PRESERVE_EXACT`)

K0 Private Candidate → K1 Public Provisional (timestamped, citable, **explicitly not peer
reviewed**) → K2 Socially Stress-Tested (K1 + substantive external human friction) → K3
Reviewed/Empirically Constrained (K2 + certification/replication as appropriate).

---

## 5. Systematic disclaimer catalogue

One master, typed, enumerable table (chair ruling C2 — vocabulary convergence over the four
incompatible vocabularies S1/S4/S5/S6/S7/S8/S10/S12 each independently invented). Home file:
`methodology/data/disclaimer_catalogue.json` (§8). Every id has a stable string, a machine-testable
`trigger_condition`, bilingual wording (TH source-of-truth, rewritten not translated), and a
placement rule. `gate_release` refuses release while any `mandatory: true` trigger is active and
its id is absent from `disclaimer_ids` — no id may resolve to a catch-all `"OTHER"` bucket.

**Convergence decisions applied this pass (chair ruling C2):**
- S8's per-citation-state disclosures fold under **`D-CITATION-UNVERIFIED` with a `state`
  parameter** (`state ∈ {NOT_FETCHED, FETCH_FAILED, MISMATCH, CHALLENGED, SCRAMMED, SUPERSEDED}`),
  the simpler of the two ruling-offered options. **Honest correction this pass (must-fix 4,
  `reviews/FOUNDATION_v0.2_anchor.md` Must-fix 3 / Vocabulary forks §2):** v0.2's own framing here
  — "a single id with a state parameter reuses the existing enum instead of minting a sixth
  vocabulary" — was itself an overclaim. `D-CITATION-UNVERIFIED.state` is a **derived, third
  vocabulary**, not a literal reuse of either existing citation-card enum: it draws two values from
  `fetch_status`, three from `status`, and mints one value (`MISMATCH`) that appears in neither.
  Stated plainly, with the exact mapping, rather than claimed as a reuse:

  | `D-CITATION-UNVERIFIED.state` value | Derived from | Mapping rule |
  |---|---|---|
  | `NOT_FETCHED` | `citation_card.fetch_status` | `fetch_status == NOT_FETCHED` |
  | `FETCH_FAILED` | `citation_card.fetch_status` | `fetch_status == FETCH_FAILED` |
  | `MISMATCH` | `citation_card.status` **+** `claim_match_verified` | `status == CHALLENGED` **and** `claim_match_verified == false` — the specific case where a source was fetched and exists, but the passage does not support the scope claimed (Integrity Firewall's `claim_match_verified` boolean, §7.8). This value exists in neither source enum on its own; it is this document's own derived condition, named here for the first time rather than left implicit. |
  | `CHALLENGED` | `citation_card.status` | `status == CHALLENGED` **and** `claim_match_verified` is not `false` (i.e. the challenge is about something other than scope-match — e.g. a dispute over the source's own correctness) — this disambiguates it from `MISMATCH` above, which is the CHALLENGED sub-case this pass makes explicit. |
  | `SCRAMMED` | `citation_card.status` | `status == SCRAMMED` |
  | `SUPERSEDED` | `citation_card.status` | `status == SUPERSEDED` |

  This mapping is a **derived enum, computed by the kernel from `fetch_status`/`status`/
  `claim_match_verified` — never a second hand-typed field on the citation card itself.** Six
  separate disclaimer ids were rejected because they would duplicate the citation card's own
  `fetch_status`/`status` enums as disclaimer ids, which is exactly the one-fact-one-home violation
  request 21 forbids; a single id with a derived-state parameter keeps one enforcement point (the
  citation card's own two source enums) while still giving the disclaimer catalogue one place to
  cite from.
- S10's `D-INDEPENDENCE` had a different trigger than S4's original id (`reviews/S10_honesty-
  usability.md` Must-fix 1 confirmed the mismatch directly). Per the ruling's own instruction, it
  becomes **`D-INDEPENDENCE-LEVEL`** with the level as a parameter, while S4's original `D-
  INDEPENDENCE` (trigger: `tested`'s strongest entry is I0–I2) is unchanged.
- S12's three advisor ids (`D-ADVISOR`, `D-ADVISOR-NOT-K2`, `D-ADVISOR-EXPIRED`) are retained as in
  v0.1, with `D-ADVISOR`'s wording pointed at `D-NO-VERTICAL-AUTHORITY` by citation rather than
  restated (closing `reviews/S12_anchor.md` Must-fix 2's duplication finding).
- `D-BLACKBOX-NOTE` replaces `D-ORIGIN-DIALOGUE` (chair ruling A1).

| id | Category | Trigger | Placement |
|---|---|---|---|
| `D-STANDPOINT` | Standpoint | Always on | Paper front matter, README, every claim card |
| `D-NONEXPERT` | Standpoint | Always on | Restores S1's "disciplines explicitly not claimed" disclosure |
| `D-SCOPE` | Scope | `ClaimScope` could exceed `EvidenceScope` | Immediately after the claim in `paper/main.md`; claim card `scope` field |
| `D-NONCLAIM` | Scope | Every card (paired `non_claims`) | `NON_CLAIMS.md`; paper abstract pointer |
| `D-AIFILL` | AI-fill | Any non-empty `ai_filled.*` | Route-level, next to the specific claim — never one blanket paragraph |
| `D-TIER` | Tier | Every quantitative/factual claim | Inline; card `tier` field |
| `D-INDEPENDENCE` | Independence | `tested`'s strongest entry is I0–I2 | Card `tested`; anywhere cited publicly |
| `D-INDEPENDENCE-LEVEL` | Independence | Any published surface names a specific independence level (S10's own trigger, distinct from `D-INDEPENDENCE` above) | Wherever that level is stated (e.g. `parameter: level=I2`) |
| `D-DVP-NOT-K2` | Independence | Public text uses "verified/peer reviewed/certified/K2/K3" while `tested` tops out below I5 | Wherever that language appears |
| `D-SAME-VENDOR` | Independence | Route Dependence Matrix shows only I1/I2, **including the bounded I2+I4 exception (§4.2)** | Route Dependence Matrix header; card `independent_check` when the exception is used |
| `D-OPERATOR-SHARED` | Independence | Matrix `operator` field identical across all routes, ODC undocumented | Matrix header |
| `D-DISAGREEMENT-OPEN` | Independence | Disagreement Ledger `outcome: DECLARED` | Ledger entry; card `tested` |
| `D-LEGAL-NEQ-EPISTEMIC` | Legal | License/permit/certification cited | Wherever the legal fact is cited |
| `D-NOT-DIAGNOSTIC` | Domain safety | Health/clinical/legal-advice/financial-advice content | Any such card or repo-level notice |
| `D-NO-NEGATIVE-UNVERIFIED-PERSON` | Domain safety | Content readable as negative/accusatory about an identifiable person/org with no verifiable source | Editorial checklist; never published as narrative prose |
| `D-TRANSLATION` | Bilingual | Any bilingual artifact | Front matter; per-field in `_th`/`_en` schemas |
| `D-DISSENT-PRESERVED` | Revision | Any dissent/deviation record exists | `reviews/`, append-only |
| `D-SILENT-LIFT-GUARD` | Provenance | Essential dependency beyond the named source | Card `assumed`/`ai_filled` fields — the operational D in E-A-D |
| `D-EXTERNAL-INPUT` | Provenance | Draws on a vetted external skill/repo/paper | Card `assumed`; `lineage/` |
| `D-NO-VERTICAL-AUTHORITY` | Legitimacy | Any mention of peer review/publication venue/institutional accept-reject | Paper legitimacy section; P6 |
| `D-NO-EPISTEMIC-VETO` | Legitimacy | Always on | `CLAIM_BOUNDARY.md` |
| `D-DERIVED-PATTERNS` | Provenance | Any pattern re-derived from a private ANSE.ASIA repo | README §Lineage |
| `D-K-STATE` | Release | Every public surface, always | README badge, Zenodo description, paper front matter |
| `D-AUTHORSHIP` | Release | Always on | CITATION.cff + README |
| `D-REVISION-LIVE` | Release | Always on | CHANGELOG.md + `reviews/` |
| `D-PARTIAL-SET` | Structural honesty | A 3-lane structure (DVP routes, solution lanes) has <3 admissible members | Wherever a 3-lane structure is presented |
| `D-CANDIDATE-STATUS` | Release | Any artifact not yet through an I4/I5 check | Every Draft/Pending-Review artifact |
| `D-COMPARISON` | Positioning | Any comparison to a market tool/skill (superseded S5's "D12 Novelty discipline" per founder ruling, request 31 — no novelty framing, descriptive same/different/cited only) | Related-work section; `neighbour_table.md` rows |
| `D-CITATION-UNVERIFIED` | Citation | Citation `fetch_status ∈ {NOT_FETCHED, FETCH_FAILED, UNCHECKED_OFFLINE}` cited, **or `state` parameter set per the convergence decision above** | Wherever the citation is used |
| `D-BLACKBOX-NOTE` | Co-production | Every research document (mandatory, request 28/32) — **replaces `D-ORIGIN-DIALOGUE`** | Appendix "Blackbox Note: how this work was made" |
| `D-ADVISOR` | Advisor | Every `conversion_plan.yaml` | Plan front fields; wording cites `D-NO-VERTICAL-AUTHORITY` rather than restating it |
| `D-ADVISOR-NOT-K2` | Advisor | Any plan referencing a K-state | Plan; K1→K2 ledger row |
| `D-ADVISOR-EXPIRED` | Advisor | Plan stale (artifact revised or `expires_at` passed) | Any surfacing UI/tool |

---

## 6. Genre router

### 6.1 Consolidation decision (chair ruling B1, resolving v0.1 §10 dispute 1)

**9 core genre rows + two cross-cutting attributes.** `genre ∈ {conceptual, empirical_quant,
empirical_qual_practice, case_study, formal_proof, systematic_review, design_science, archival,
position_reply}` plus `venue_track: international | thai_tci | none` (`none` added must-fix 8 —
legal for K0 work never intended for any venue) and `companion_of: <artifact id> | null`.
บทความวิชาการ = `conceptual`/`systematic_review`/`position_reply` with `venue_track:
thai_tci`; บทความวิจัย = `empirical_*`/`case_study` with `venue_track: thai_tci`; a Thai companion
is any genre with `companion_of` set. **S11's DAG content for the Thai rows is preserved as
track-specific section requirements attached to the track (PRESERVE_FUNCTION), not as separate
genre rows.** Reason (per the ruling): request 21's "one stable system, fewer parallel rows," and
the fact that S11's own genre 12 (Thai companion) already treated Thai-ness as an attribute rather
than a distinct structural genre.

This resolves v0.1 §10 dispute 1 in favour of Position B (the cross-cutting-attribute reading);
Position A's underlying concern — that Thai academic convention has different required sections,
ethics norms, and TCI reviewer expectations — is **not discarded**, it is preserved as the
track-specific requirement column below (§6.2), attached mechanically to `venue_track: thai_tci`
rather than living as a separate row.

### 6.2 The 9-row table + track-specific requirements

| # | Genre | Structure | IMRAD? | Claim ceiling | Extra mandatory disclaimers | Blackbox Note appendix required? | Preserved-experience field |
|---|---|---|---|---|---|---|---|
| 1 | `conceptual` | Phenomenon → Existing explanations → Precise inadequacy → Rival concepts (neighbour table, §13) → Mechanism → Boundary → Propositions → Self-application | No | `Dr` on propositions | `D-COMPARISON`, `D-NONCLAIM` | Yes | "Problem reconstruction" section |
| 2 | `empirical_quant` | IMRAD + frozen prereg variant | Yes | `[result]` only if CI excludes null, else `[directional]` | `D-SCOPE` (sample) | Yes | "Context of discovery" subsection under Introduction |
| 3 | `empirical_qual_practice` | Context/Practice → Observation → Reflection → Boundary | Partial | K1 by default regardless of tier | `D-STANDPOINT`, `D-INDEPENDENCE` always-on | Yes | "Practice context" section, first-class not a footnote |
| 4 | `case_study` | Case selection/boundary → Data sources → Timeline → Mechanism → Explicit non-generalization | Partial | `Dr` interpretive; underlying cards may be `finite_diagnostic` | `D-NO-NEGATIVE-UNVERIFIED-PERSON` always-on | Yes | "Positionality" section |
| 5 | `formal_proof` | Definitions/Axioms → Lemmas → Theorems → Mechanical check → Formalization-fidelity review (`FID`, class-4) → Claim Matrix | No | `Th_coqc` only with `independent_check.status==PASSED`; else `Open`, never `Dr` | none beyond floor | Yes | "Motivating problem" section |
| 6 | `systematic_review` | PRISMA-2020 flow + fallback labels (`SYSTEMATIC_REVIEW \| TARGETED_SEARCH \| SCOPING_SEARCH \| RAPID_EVIDENCE_CHALLENGE \| FIELD_OBSERVATION_LOG`) — FC-S8-1 hard block on mislabeling | Partial | Ceiling bounded by weakest included source's tier | none beyond floor | Yes | "Why this review" section |
| 7 | `design_science` | DSRM: Problem → Objectives → Design → Demonstration → Evaluation → Communication | No | `finite_diagnostic` on "it runs"; `Dr` on "it solves the problem well" | none beyond floor | Yes | "Problem as lived" section |
| 8 | `archival` | Record inventory → Retrievability statement → Translation status → Non-affiliation statement | No | `finite_diagnostic` "record exists/reads X"; `Dr` interpretive gloss, kept separate | `D-TRANSLATION` mandatory | Yes | "Why this record matters" section |
| 9 | `position_reply` | Target claim → Disagreement/addition → Argument → Scope of reply | No | `Dr`; ceiling capped by the *target* claim's own independence class (Bounded-Judge Law) | none beyond floor | Yes | "What prompted this reply" section |

**`venue_track: thai_tci` requirements (attached to any of the 9 rows above, PRESERVE_FUNCTION
from S11's original genre 1/2/12 DAG content, per chair ruling B1):** Thai-language section labels;
Thai ethics-committee disclosure norms where a human-participant claim_type is present; TCI
reviewer-expectation checklist (author affiliations, Thai abstract, Thai keyword set); the genre's
claim ceiling and disclaimer set are otherwise **unchanged** — the track adds section/format/
disclosure requirements, it never raises or lowers a tier ceiling.

**`companion_of` requirements (any genre, PRESERVE_FUNCTION from S11's original genre 12):** the
companion artifact inherits its target's structure and never exceeds the target's own tier by
rewriting alone; `D-TRANSLATION` is mandatory.

### 6.3 Why IMRAD fits only genres with a real access event

Unchanged from v0.1 §6.3: IMRAD's four headers are a claim about provenance, not a neutral format.
**Design rule:** IMRAD is licensed exactly when a claim card in that genre answers
`five_questions.seen` with a real, dated, `retrievable_original: true` access event the author or a
named instrument performed.

### 6.3b Genre routing procedure (must-fix 11 — replaces the stale S5 7-question router)

`reviews/FOUNDATION_v0.2_usability.md` §3 found the only decision procedure on disk
(`design/S5_paper-and-academic-templates.md` §1.2's seven yes/no questions) still routes to the
**old** 7-genre set, never updated to match chair ruling B1's 9-genre taxonomy — the router was not
computable from a real claim card. Fixed here as an ordered list, each question computable
directly from a named claim-card field, ending in one of the 9 genre ids or `MIXED_GENRE`:

1. **Is `five_questions.tested.evidence_relations` empty of any mechanical/formal artifact, and is
   `lens_translation.formal_applicability == exact_functional` with a machine-checked or executed
   proof intended?** *(reads: `tested.evidence_relations[].independence_class`,
   `lens_translation.formal_applicability`)* → yes → **`formal_proof`**. No → continue.
2. **Was the evidence gathered via a documented systematic/targeted/scoping literature search
   (a `search_log` exists for this claim), rather than the author's own direct observation?**
   *(reads: `related_citation_cards`, presence of a linked `search_log.yaml`)* → yes →
   **`systematic_review`**. No → continue.
3. **Does `five_questions.seen.access_model` name a retrievable archival record (a document,
   register, artifact) rather than a live observation or a designed intervention?** *(reads:
   `five_questions.seen.access_model`, `five_questions.seen.retrievable_original`)* → yes →
   **`archival`**. No → continue.
4. **Does this claim's `statement` explicitly target and respond to another named claim/artifact
   (agree, disagree, extend, correct it)?** *(reads: `companion_of` is null but the claim
   references another `claim_id`/`citation_card` as its subject, or `lineage.derives_from` names
   exactly one prior claim as the thing being replied to)* → yes → **`position_reply`**. No →
   continue.
5. **Did the author design and build an artifact (tool, protocol, template, system) as the
   contribution, rather than report on an existing situation?** *(reads: `claim_type ==
   DECISION`/`FORMAL` combined with `five_questions.assumed[].type ==
   decision_policy_augmentation` naming a built artifact)* → yes → **`design_science`**. No →
   continue.
6. **Is `scope.generalization_claimed` set to `population_claim`, with a frozen pre-registered
   design named in `five_questions.tested`?** *(reads: `scope.generalization_claimed`,
   `tested.evidence_relations[].strength`)* → yes → **`empirical_quant`**. No → continue.
7. **Is `scope.generalization_claimed` set to `none` or `pattern_candidate`, with
   `standpoint.declared_basis` naming direct practice/lived observation as the evidence source?**
   *(reads: `scope.generalization_claimed`, `standpoint.declared_basis`)* → yes → does the claim
   name a bounded, individually-identifiable case with its own timeline (a specific person,
   household, organization, or event)? → yes → **`case_study`**; no (a practice pattern without one
   bounded case) → **`empirical_qual_practice`**.
8. **Is `lens_translation.formal_applicability == not_applicable_narrative` and no branch above
   matched?** *(reads: `lens_translation.formal_applicability`)* → yes → **`conceptual`**.
9. **More than one branch above matched with comparable strength** (e.g. a case study that is also
   a position reply) → **`MIXED_GENRE`**, naming every matched id in `revision_history`; a human
   Approver breaks the tie for the paper's primary structure at Human Mastery Gate (§7.5).

`venue_track` and `companion_of` are **never inputs to this procedure** — they are set
independently, after a genre id is chosen, per §6.1/§6.2's track-attribute rule. This list
supersedes S5's 7-question procedure; `methodology/P13_genre_router.md` narrates this list
directly rather than citing S5.

### 6.4 Mandatory gates threaded through every genre

Every genre's terminal Publish node requires, in addition to its own column above:
- **`review_report.independence_class ≥ I3` on file (OR the bounded B4 exception's full condition
  set — an I2 route paired with an I4 route, `D-SAME-VENDOR` emitted, `independent_check.
  expires_at` ≤ 90 days) and every citation reachable from the paper at `status: VERIFIED`** (§7.4,
  §7.8). **Corrected this pass (chair ruling item 1, closing `reviews/FOUNDATION_v0.2_anchor.md`
  Must-fix 1):** v0.2 stated this bullet as a bare `≥ I2`, contradicting §4.2's own table (I2
  "cannot raise: K1 floor alone") and §2.2's stage-gate (K0→K1 "only with ≥I3 ... subject to the
  bounded I2+I4 exception"), and had no numbered kernel rule enforcing either version — a
  constructible payload could reach `k_state: K1` on bare I2 evidence. §3.3 rule 9 (new this pass)
  is the kernel-side twin of this fix; both must read the same threshold, which they now do.
- **`origin_blackbox_ref` populated and the curated Blackbox Note appendix present** — a hard
  precondition on every genre's Publish node (fixing the gap two independent reviews found where a
  founder-mandated release-gate criterion was silently absent from all 12 original DAGs).
- **The three-question lit-review scaffold (request 31d/31e)**: every genre's related-work/
  lit-review section routes through `design/S13_neighbour-table.md`'s format (which problem · by
  which method · same/different/cited per neighbour) — not a chronological or prestige-ordered
  survey. S8's `search_log` + citation cards feed this table directly.
- A disclaimer rollup matching this genre's column plus the universal floor (`D-STANDPOINT`,
  `D-SCOPE`, `D-NONCLAIM`, `D-AIFILL`, `D-TIER`, `D-LEGAL-NEQ-EPISTEMIC`, `D-NO-VERTICAL-
  AUTHORITY`).
- `produced_by`/`responsible` visible per claim (request 24) — not just at the document level.

---

## 7. Gates & review

### 7.1 MIMCG L0–L5 mapped onto glosa artifact types

The general L0–L5 table, "round up when uncertain," and the Class-5-never-substitutes-for-I5 rule
are unchanged from v0.1 §7.1 and incorporated by reference from the MIMCG skill for full detail.
**The L3 and L5 rows are reconciled and stated explicitly this pass (chair ruling item 2, closing
`reviews/FOUNDATION_v0.2_anchor.md`/`_usability.md`'s shared finding that v0.2's own L3 line — "I2/
I3 AND I5 (human) required" — conflicted with §4.2's "I3 is the K1 floor," and that the usability
review's cat-example walk (§4 there) could not resolve from the documents read whether an I3-only
route can actually be "cited publicly" without also clearing an I5 human leg):**

| Level | Artifact scope | Required check | Note |
|---|---|---|---|
| L0 | Private draft, not shared | Self-check only | No independent check required |
| L1 | Shared informally within one session/team | 1 independent "2nd reader" (`independence_class ≥ I1`) | |
| L2 | Shared cross-session / DVP corroboration | ≥3 DVP routes, `I2` minimum | |
| **L3** | **Public `main` / publicly cited** | **An `I3` check on file (or the bounded B4 exception's full condition set, §4.2) PLUS a distinct human Approver (the founder, class-5 release authority)** | **Reconciled this pass — the human requirement at L3 is a release-authority function (the Approver's sign-off to publish), never a verification level. It is satisfied by the founder as Approver, not by an `I5` independent checker.** An `I5` external-human *checker* is not required to reach L3; it is required only for K2/K3 and for L5 (row below). **`K1 via I3 can be public; it is public-provisional, never K2.`** This is the sentence that resolves the usability review's flagged tension: a K1 card checked at I3 and approved by the founder can sit on public `main`, cited, dated — it simply can never claim more than K1 while it does. |
| L4 | Mechanical/original-record artifact release | `I4` mechanical check | |
| **L5** | **Any surface using "verified / K2 / certified" wording, minting a DOI, or submitted to a journal/venue** | **`I5` (independent external human, non-founder) required** | **Reconciled this pass — L5, not L3, is where an `I5` checker is mandatory.** This is the same bar §3.3 rule 4 sets for `k_state: K2`/`K3` at the schema level; L5 is its MIMCG-side restatement. The founder's Approver role at L3 never substitutes for this L5 `I5` requirement (Class-5-never-substitutes-for-I5 rule, unchanged). |

**L3's exception coverage, unchanged from v0.2:** the bounded I2+I4 exception (§4.2) satisfies L3's
`I3`-or-exception leg exactly as any I3 route would, still requiring the founder's Approver
sign-off; the exception only ever licenses K1, never a shortcut past L5's `I5` requirement.

### 7.2 Maker–Checker–Approver separation (MC-01)

Unchanged from v0.1 §7.2 — three distinct identities, checked directly on the documents being
graded, not only at a transport boundary.

### 7.3 Bounded-Judge Law

Unchanged from v0.1 §7.3. A `review_report` without `verdict_tier` (the **six** tiers of §4.1, not
four — chair ruling C4, fixing the gap `reviews/S10_honesty-usability.md` Must-fix 4 found where
S10's own schema and packet template carried only 4 of the 6 values) is invalid and cannot back any
`tested:` entry, regardless of independence level.

### 7.4 Release state machine (one canonical name set)

Unchanged from v0.1 §7.4 — `Draft → Pending Review → (Revise ↺) → Approved-for-Test →
Approved-for-Live → Monitor`, `Rollback` reachable from any live state, ungated;
`Approved-for-Public ≡ Approved-for-Test` and `Published ≡ Approved-for-Live` at repository
granularity.

**PUB-ADVERSARIAL-REVIEW, seven dimensions** (R1 leak scan, R2 license coverage, R3 tier fidelity,
R4 citation accuracy, R5 anchor-preservation audit, R6 overclaim/register scan, R7 completeness) —
run by an independent pass, never the maker; verdict `PASS | PASS_WITH_LIMITS | FAIL | HUMAN_
REVIEW`, one vocabulary reused everywhere.

### 7.5 Human Mastery Gate

Unchanged from v0.1 §7.5.

### 7.6 K1→K2 conversion ledger

Unchanged from v0.1 §7.6 (`GLOSA_K1_K2_LEDGER.md`, the ten reused columns, the "does not count" list
— stars, downloads, shares, an uncredited AI citation).

### 7.7 The Project Advisor (a third role — request 22)

Activates only after `gate_release` returns `PASS`/`PASS_WITH_LIMITS` on an L3+ artifact — never on
unreleased work. **Not** Maker, Checker, or Approver of the same artifact. Reads (never writes) the
release manifest, linked claim/evidence/citation cards, the project's kg, and the existing K1→K2
ledger; produces one `conversion_plan.yaml` per release: K-state now, Global route, Thai/local
route (GDA six questions), next 3 *addressed* conversion actions, a rejection budget/survival
buffer, a fixed "what NOT to do" list, and a candidate (never confirmed) K1→K2 ledger row. Tier
always `Dr`.

**Dependency, not merge (chair ruling B3, resolving v0.1 §10 dispute 3):** the advisor's knowledge
base is **cited as a dependency, by name + version + DOI** —
`ai-native-scholarship v1.0.0` (Zenodo record cited in §1.2) — not merged into `plugins/`. glosa
re-derives only the specific protocol functions it needs (conversion-first, dual-track, GDA,
K1→K2 ledger, back-catalog activation, friction-vs-fellowship routing, SCRAM), each logged
`PRESERVE_FUNCTION`/`EXPAND` in `lineage/RELATION_TO_STANDALONE_SCHOLAR.md`; `methodology/data/
advisor_knowledge_base.json` is a **citation + distillation**, never a republish of `anchor-v10.md`.
This remains a founder veto point (`FOUNDATION` §11 item 4).

Governed by exactly two equations, both gates not universal laws: **mint–convert coupling**
(`new_flagship_recommended ⇒ mint_count ≤ λ·conversion_count`, `λ` never a shipped constant — cold-
start default is zero new flagships, conversion-only) and **Reactivity License**
(`increase_mint_rate ⇒ integrity_clean ∧ xenon_below_threshold ∧ conversion_log_operational`).

**SCRAM rules (specified, Dr, untested — chair ruling D1 applied here too)**: refuses to advise,
`status: BLOCKED`, on: an unverified citation in scope, K1 misrepresented as K2/K3, a venue
disclosure gap, the advisor's own identity conflict, or an open Xenon-ledger item above threshold.
None of these SCRAM conditions has yet been reduced to a mechanically-checkable predicate
(`reviews/S12_honesty-usability.md` Must-fix 1 found `K_STATE_MISREPRESENTED` in particular is not
machine-checkable as specified) — a future revision must either state the predicate exactly or mark
the condition human-judgment-only. Vendor-neutral: one kernel function (`advise()`), CLI (`glosa
advise`), MCP tool, and a self-contained prompt packet (`templates/knowledge/
advisor_prompt_packet.md`) for any AI with no CLI/MCP access.

### 7.8 Citation integrity subsystem (request 16 — generalized to distinction-grain)

**Integrity Firewall** (Standalone Scholar §18.1, `PRESERVE_FUNCTION`, split into two independently-
flaggable booleans): AI candidate → OriginalSource → **`metadata_verified`** (existence/metadata
check, Crossref/OpenAlex/PubMed lookup) → **`claim_match_verified`** (a named human or decorrelated
AI route reads the exact passage and confirms scope) → VerifiedCitation. **Source existence ≠ Claim
support** (NC-18) is the non-collapsible boundary between the two booleans. Citation card fields:
`identifier.{kind: DOI|PMID|PMCID|ISBN|ARXIV|OFFICIAL_URL|BLACKBOX_NOTE|OTHER_STABLE, value}`
(**`BLACKBOX_NOTE` added this pass, chair ruling C8, replacing the S8 gap/"DIALOGUE_RECORD" kind —
a Blackbox Note is a first-class citable object under this same firewall, verification method
`verbatim_diff_against_note`**), `fetch_status: FETCHED|NOT_FETCHED|FETCH_FAILED|
PAYWALLED_ABSTRACT_ONLY|UNCHECKED_OFFLINE` (one enum, chair ruling C3, reused by `design/
S13_neighbour-table.md`), `exact_passage`, `scope: DIRECT_QUOTATION|PARAPHRASE|
SUPPORTS_GENERAL_CLAIM_ONLY|CONTEXT_ONLY_NOT_EVIDENCE`, `evidence_tier`, `independence_class`
(the same I0–I5 ladder, §4.2), `status: CANDIDATE|METADATA_OK|VERIFIED|CHALLENGED|SCRAMMED|
SUPERSEDED`. `SCRAM` on a fabricated citation forces the backed claim card to `Open` immediately and
hard-blocks publish. `XENON_LEDGER.md` (append-only, never purged, **per-project home, one merged
view — chair ruling B6**) records every `SCRAMMED` card: `date, citation_card_id, error_type,
found_by, correction, claim_impact`.

**Systematic review honesty**: PRISMA-2020 + Cochrane Ch.4 as the transparency floor; four fallback
labels (`SYSTEMATIC_REVIEW | TARGETED_SEARCH | SCOPING_SEARCH | RAPID_EVIDENCE_CHALLENGE`) plus a
fifth for non-literature evidence (`FIELD_OBSERVATION_LOG`); **FC-S8-1** (hard block): calling
anything less than a full SR protocol a "systematic review." `LOCAL_EVIDENCE_NOT_FOUND ≠ NO_LOCAL_
EVIDENCE_EXISTS` (NC-27) — a search-coverage fact is never promoted to a universal negative.

`review_mode` enum (chair ruling C5, fixing the drop `reviews/S8_anchor.md`/`S8_honesty-
usability.md` found): `MAKER_SELF_CHECK | DECORRELATED_AI_ROUTE | HUMAN_REVIEW |
MECHANICAL_CHECK | SYSTEMATIC_LITERATURE_SEARCH | INTERNAL_DATA_AUDIT`. `INTERNAL_DATA_AUDIT`
(skillme's own sixth mode) is **restored** here rather than left superseded, since no design in
this round names a reason to drop it and it covers exactly the case (an internal, self-held-data
check, e.g. re-reading one's own logbook) none of the other five modes describes.

---

## 8. Repo layout + one-fact-one-home map

Full directory tree: `design/REPO_SPEC_v0.2.md` (companion file to this document, updated for every
rename in this synthesis). Compact "which file owns which rule" summary — unchanged in structure
from v0.1 §8, with these v0.2 additions:

| Rule lives in | Enforced by | Narrated in |
|---|---|---|
| Blackbox Note content | `records/blackbox/<id>.yaml` per project (chair ruling B6 pattern) | `paper/BLACKBOX_NOTE_APPENDIX.md` |
| Per-project ledgers (Disagreement, Xenon) + repo-wide merged view | `glosa kg merge` / `glosa ledger merge` | `methodology/P6_independent_check.md`, `P*_citation` |
| Per-project kg + repo-wide merged view | `glosa kg validate|merge` | §8.1 below |

### 8.1 Named knowledge-infrastructure subsystems (request 14/15)

Unchanged from v0.1 §8.1 in content, with **"per project, unioned by `glosa kg merge`"** now stated
identically for the kg (already true in v0.1), the Disagreement Ledger, and the Xenon Ledger
(chair ruling B6 extends the same pattern to all three, closing v0.1 §10 dispute 6):

| Subsystem | Rule | Canonical home | Gate |
|---|---|---|---|
| **Citemap + kggraph** | One canonical graph (ISO 30401 pattern); citemap is a *view* of the full kg, never a second store. Node types: `claim\|source\|equation\|project\|person_role\|concept`; edge types: `supports\|challenges\|derives_from\|borrows\|supersedes\|cites` | `kg/{nodes,edges}.jsonl` **per project**, unioned by `glosa kg merge` | `glosa kg validate`: edges resolve, no dangling `ref`, no two `ACTIVE` cards claiming one canonical ref, no `derives_from` cycle |
| **One problem = one project** | Every declared problem gets exactly one project directory; a project splits when its `CLAIM_BOUNDARY.md` needs an "and," or two claims' assumptions contradict | `templates/knowledge/project_skeleton.md` | Reviewer check at L2+ |
| **Sub-library spin-out** | A mechanism reused by ≥2 projects gets its own README/LICENSE/CITATION.cff/tests/tier ledger; consuming projects switch to a `borrows`/`derives_from` kg edge | `templates/knowledge/library_spinout_checklist.md` | A `DECISIONS.md` row records the spin-out |
| **Equation/definition registry** | Registered once, at first use; `owner, first_use_year, external_first_publication, source_citation_card_id, tier, borrowed_vs_derived_status`; never re-registered | `EQUATION_REGISTRY.md` + `templates/knowledge/equation_registry_row.yaml` | Buckingham-trap guard |
| **Disagreement Ledger** | Per-project, append-only; records Resolve-or-Declare outcomes (§4.3) | Per project directory | `glosa kg merge` renders repo-wide view |
| **Xenon Ledger** | Per-project, append-only, never purged; records `SCRAMMED` citations (§7.8) | Per project directory | `glosa kg merge` renders repo-wide view |
| **Research-library interface** | The private Zotero+Calibre+Paperless shelf is the source-ledger *substrate*; the public citation card carries only a public identifier | Interface boundary only | R1 leak-scan check |

---

## 9. Callable layer — schemas → kernel → CLI → MCP → plugin

Unchanged from v0.1 §9 in structure. One field-name fix propagates through: any function or
transport that reads/writes `origin_r0_ref`/`origin_dialogue_ref` now reads/writes `origin_
blackbox_ref` (chair ruling A1/C8). `kernel/glosa_kernel.py` remains stdlib-only, pure,
offline — no network call inside a `validate_*`/`gate_release`/`defeater_route` function.

**Kernel functions** (fixed against the schema in §3): `validate_claim_card`, `validate_evidence_
relation`, `validate_intake`, `validate_review_report`, `validate_readiness`, `validate_release_
manifest`, `validate_citation_card`, `compute_disclaimers`, `route_genre`, `gate_release`,
`defeater_route`, `advise` (§7.7), `kg_validate`/`kg_merge` (§8.1), `ledger_merge` (**new this
pass, chair ruling B6** — merges per-project Disagreement/Xenon ledgers into the repo-wide view),
`cite_check` (§7.8), `schema_summary`, `demo_run`, `self_test`.

**CLI, MCP server, the AI coding tool plugin, Accuracy gate**: unchanged from v0.1 §9 in every detail
except `glosa ledger merge` is added to the CLI surface alongside `glosa kg validate|merge|render`.
Until the five-item Accuracy gate passes, every artifact this layer produces carries `tier: Dr`
and `D-CANDIDATE-STATUS`.

---

## 10. Disputes resolved by chair ruling (formerly "unresolved disputes")

Every dispute v0.1 §10 left for the AI assistant is now resolved by `design/CHAIR_RULING_v1.md`; see §13 below
for the dispute-by-ruling-by-location table. None of the six is re-litigated here. For the historical
record, the six original disputes and their resolving ruling item are:

1. Genre taxonomy (7+MIXED_GENRE vs 12-row, Thai split as row vs. attribute) → **B1** (§6.1).
2. Card granularity (full always vs. lightweight stub) → **B2** (§3.2a).
3. `ai-native-scholarship` relationship (cite vs. merge) → **B3** (§7.7, §1.2).
4. Same-vendor-different-model (I2) substituting for cross-vendor (I3) as the K1 floor → **B4**
   (§4.2, the bounded exception).
5. Local-model DVP route mandatory or best-effort → **B5** (§4.2).
6. Repo-wide vs. per-claim Disagreement/Xenon Ledger → **B6** (§4.3, §7.8, §8.1).

B1–B4 are chair rulings the founder may still overturn (chair ruling F).

---

## 11. Founder decisions required

- **Item 1 (repo name): DECIDED — `glosa`** (request 34). A "standalonescholar" proposal was raised
  and withdrawn by the founder before this name was chosen.
- **Item 3 (license split): DECIDED this pass — CC BY 4.0 for the whole repository, single
  license** (request 33, must-fix 3), superseding v0.1/v0.2's MIT-code/CC-BY-prose split. Note for
  the founder, carried forward from the founder's own flag in request 33: CC BY on code is legal
  but unusual; **if a code-specific license is ever wanted, it must be added later as an explicit
  dual grant, never silently folded in.** See `REPO_SPEC_v0.3.md` for the resulting tree change
  (`LICENSE` only; `LICENSE-TEXT.md`/`LICENSES.md` dropped).
- **B1–B4 above are chair rulings, not founder-settled facts** — the founder may overturn any of
  them; nothing in §§3–9 should be read as foreclosing that.
- **Item 7 (who occupies I5) is the single most consequential open item**: without a named
  external human, no glosa claim can ever be K2. Chair recommendation (not a ruling, since this is
  a founder-only decision): the first I5 candidates are the founder's existing correspondents named
  in the Standalone Scholar's own K1→K2 ledger.

The remaining 17 open items (TH/EN direction; `ai-native-scholarship` cite-vs-merge veto;
anonymization depth for private-repo case narratives; which license-less PUBLIC repos get a
LICENSE before citation; who is I5; who is the Project Advisor for the founder's own projects;
whether domain-safety disclaimers are also standing repo-wide notices; citation-checker CI network
policy; ISBN verification investment; sub-library spin-out threshold; Zenodo webhook vs. manual
deposit; `check_leak.sh` denylist visibility; Forgejo network-exposure confirmation; Thai TCI
journal target; LaTeX Thai-font gap priority; Advisor type-pool refresh cadence; `λ`/`β_min`
calibration scope) are carried forward unchanged from `FOUNDATION_v0.1.md`/`FOUNDATION_v0.2.md`
§11 and are not retyped here to avoid a driftable second copy. Items 1 and 3 above are removed from
that carried-forward count, now that both are decided.

---

## 12. Honest edges — what is still Dr / untested, and what was NOT read

**This document itself.** Three synthesis passes now (v0.1, v0.2, this v0.3), one chair ruling, and
now **two independent adversarial reviews of v0.2** (`reviews/FOUNDATION_v0.2_anchor.md`,
`reviews/FOUNDATION_v0.2_usability.md`) whose combined 12 must-fix items this pass applies in full
(§13). Still no independent I2+ re-check of *this* synthesis pass itself — per this project's own
MIMCG rule, it may not be treated as settled until such a review runs and the founder rules on
§11.

**Review-count sentence, updated this pass: 14 designs, 28 reviews, 1 critic, 1 chair ruling, 2
independent reviews of v0.2.** All 28 S8–S13 review files remain read into this synthesis
(unchanged from v0.2's own count, chair ruling D3), and the two v0.2-targeted reviews add 12
must-fix items, all applied this pass (§13's table gains 12 new rows). Every S8–S13 Must-fix not
resolved by a named chair-ruling item is still carried forward explicitly as an unresolved
must-fix (list unchanged from v0.2, reproduced below) — this pass's fixes target only the two
v0.2-review must-fix sets, not the older S8–S13 carry-forward list.

**Remaining open items the two v0.2 reviews found but which are not among the 12 must-fix items
this pass was scoped to fix (carried forward, not silently dropped):** `five_questions.separates.
licensing_test.regime` still has no defined vocabulary or examples; `assumed[].
contaminated_concept_hit`'s type (boolean vs. table-row reference vs. free text) is still
unstated; whether a joint human+AI `maker_id` counts as one or two identities for MC-01's
pairwise-distinct check is still unaddressed; `claim_type`'s 8 values still have no obvious fit for
an anecdotal single-subject non-human-participant empirical observation (`EMPIRICAL` remains the
least-wrong default, unresolved); present-tense "enforced"/"refuses"/"hard failure" language
throughout §3.3/§7 for unimplemented mechanisms is a register issue not fixed by this pass's
content changes; `templates/knowledge/dialogue_card.yaml`'s status as a possibly-redundant artifact
next to a Blackbox Note line with `kind: reply` remains open (`REPO_SPEC_v0.3.md`).
**`design/templates/knowledge/blackbox_note.yaml`'s own header still calls the mandatory appendix
"Human–AI dialogue before this work"** (the pre-rename title; current name per chair ruling A1 is
"Blackbox Note: how this work was made") **and its `disclaimers:` example still cites
`D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE`, an id that does not exist in §5's master catalogue** (the
nearest match, `NC-64`, is a Non-Collapse Table row, not a disclaimer id) — both flagged by the
usability review's ambiguities list, neither is one of the 12 numbered must-fix items this pass was
scoped to, and neither is fixed here; a future revision should either add the missing disclaimer id
to §5 or point the template at an existing one, and finish the template's own title rename.

**Sources read only partially by this synthesis or by any prior stage:** unchanged from v0.1 §12 —
`STANDALONE_SCHOLAR_v3.txt` (targeted ranges), `READOUT_CONDITION_2026-08.txt` (core sections, not
the formal appendix/bibliography), `The_Readout_Condition_Full_Paper_Elevated.pdf` (relied on the
`.txt` extraction), the local session transcript (not public; curated lines in blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md) (36 founder lines only; AI's own
replies remain in the session transcript).

**`sources/zenodo_lahtee_records.json` (180 records) — chair ruling D5 applied:** 169 of 180
records remain unread by this design round; they are to be **listed, not interpreted**, in
`lineage/PRIOR_WORK.md` when that file is built (still not on disk — `REPO_SPEC_v0.2.md` §"not
yet on disk"). This v0.2 does not interpret any of the 169; stating this plainly here, rather than
only in a footnote, is the fix chair ruling D5 asked for.

**Nothing in this document has been executed as code.** Unchanged from v0.1 §12: S5's two LaTeX
templates are the only artifacts in the entire design round actually compiled and independently
re-verified — **and `reviews/COMPLETENESS_CRITIC.md` §4 found the compiled `disclaimers.tex` still
carries "D12 — Novelty discipline" language, contradicting founder ruling 31, uncaught by any prior
review.** This synthesis records the finding but has not regenerated the LaTeX; **regenerating both
`disclaimers.tex` files (via the not-yet-built `scripts/render_disclaimers.py`, §8) and recompiling
both PDFs is an open action item this document cannot itself close**, since it is a design document,
not a build step. Every schema, gate rule, and kernel function in §§3–9 remains `Dr`-tier prose.

**Must-fix items from the S8–S13 reviews not resolved by a named chair-ruling item, carried forward
open (per this synthesis's instruction to fold every must-fix the ruling does not already
resolve):**
- `reviews/S9_anchor.md` Must-fix 3: NC-02's "enforced by" column cites a claim-card mechanism
  (`Warrant Profile`) that does not exist as a named field in this schema's §3.2 — the row should
  instead cite `standpoint`/`tier` jointly, or a new field should be proposed; not fixed here.
- `reviews/S10_anchor.md` Must-fix 2: the Route Dependence Matrix schema in S10 and the one in
  `templates/knowledge/route_dependence_matrix.yaml` (already built) have not been checked
  field-by-field against each other in this pass; flagged, not reconciled.
- `reviews/S9_honesty-usability.md` Must-fix 1: unpublished-local-file citations presented at the
  same trust level as public-repo citations in S9's own sourcing — not corrected in this pass since
  it is internal to S9's own file, not a FOUNDATION field; flagged for S9's own next revision.
- `reviews/S11_honesty-usability.md` Must-fix 3: a misattributed citation in S11 §9.1 supporting a
  claim not yet true — internal to S11's own file, not re-verified in this pass.
- `reviews/S12_anchor.md` Must-fix 3/4: S12's self-declared "PASS" preservation verdict is not
  independently supported, and the advisor's independence claim is untested against its hardest
  case (the founder as both maker and the only available advisor) — this remains open; §11's
  founder-decision item 8 already names the second half of this gap.
- `reviews/S12_honesty-usability.md` Must-fix 4: the three advisor disclaimers ship with no Thai
  wording yet — per the bilingual rule (§2.5), `translation_status: missing` applies to their `th`
  field until a human or reviewed-machine pass fills it; not filled in this synthesis.

**The full Non-Collapse Table (Appendix A)** is, by S9's own honest-edges note, a readout that is
"not proven exhaustive." Three new rows are added this pass (chair ruling C6, §Appendix A) but the
table's own honest-edges caveat is unchanged.

**Genre-router merge (§6)** is stated as a decision, not yet verified: whether S5's compiled LaTeX
templates render correctly when driven by the new 9-row + `venue_track`/`companion_of` framing
(rather than either S5's original 7-row table or v0.1's 12-row table) has not been checked by
anyone — this is now a *third* unverified rendering claim layered on the same two never-rechecked
templates identified in v0.1.

---

## 13. Chair rulings applied

| Dispute / finding | Ruling id | Where applied in this document |
|---|---|---|
| Blackbox Note rename (supersedes Register Zero/R0) | A1 | §1.3, §2.1, §2.3, §2.4, §3.2 (`origin_blackbox_ref`), §5 (`D-BLACKBOX-NOTE`), §7.8 (`BLACKBOX_NOTE` identifier kind) |
| No novelty/priority language; three-question positioning; lit-review scaffold | A2 | §1.1, §6.4, `design/S13_neighbour-table.md` |
| Human–AI co-production visibility, human experience preserved, `became:` links, curated appendix | A3 | §2.2, §2.4, §6.2 (preserved-experience column) |
| Genre taxonomy → 9 rows + `venue_track` + `companion_of` | B1 | §6.1, §6.2, §3.2 |
| Card granularity → `shape: stub \| full` | B2 | §3.2, §3.2a, §3.3 rule 10 (renumbered this pass) |
| `ai-native-scholarship` cited as dependency, not merged | B3 | §1.2, §7.7 |
| I3 stays the K1 floor; bounded I2+I4 exception | B4 | §1.3 (row 6), §3.3 rules 4 and 9 (new this pass), §4.2, §5 (`D-SAME-VENDOR`), §6.4, §7.1 (L3/L5) |
| Local-model DVP route = best-effort, I3 only if vendor-distinct | B5 | §4.2 |
| Ledgers per project, one rendered view | B6 | §4.3, §7.8, §8.1, §9 (`ledger_merge`) |
| `independence_class` one string ladder, every schema | C1 | §4.2, §3.2, §7.8 |
| One disclaimer catalogue; citation-state folded into `D-CITATION-UNVERIFIED`; `D-INDEPENDENCE-LEVEL` split | C2 | §5 |
| `fetch_status` one enum, reused by neighbour table | C3 | §7.8, `design/S13_neighbour-table.md` |
| `verdict_tier` six tiers | C4 | §7.3 |
| `review_mode` restores `INTERNAL_DATA_AUDIT` | C5 | §7.8 |
| Non-collapse table append `NC-62..64` | C6 | Appendix A, §2.4, §3.1 |
| Lineage adds zero-readout-certifies and `label_inflation_guard.py` | C7 | §1.2 |
| `origin_blackbox_ref` one origin field; `BLACKBOX_NOTE` citation kind | C8 | §3.2, §7.8 |
| §3.3 heading renamed to state untested status at point of claim | D1 | §3.3, §7.7 (SCRAM rules) |
| Q2/Q3/Q4 presence-vs-correctness stated in §3.1 | D2 | §3.1 |
| Review-count sentence updated | D3 | §12 |
| S13 rows without URL → `NOT_FETCHED`/Open; S13 rewritten to neighbour-table format | D4 | `design/S13_neighbour-table.md` |
| §12 lists 169/180 unread Zenodo records | D5 | §12 |

### 13.1 v0.2 review must-fix items applied this pass

| # | Must-fix (source review) | Where applied |
|---|---|---|
| 1 | K1-floor kernel gate missing; §6.4 weaker than §4.2 (`FOUNDATION_v0.2_anchor.md` Must-fix 1) | §3.3 new rule 9; §6.4 first bullet corrected to `≥ I3` (or B4 exception) |
| 2 | §7.1 L3 vs §4.2 I3-floor contradiction on the human-check requirement (`FOUNDATION_v0.2_anchor.md` Vocabulary forks; `FOUNDATION_v0.2_usability.md` §4 row (b)) | §7.1, L3/L5 rows rewritten: L3 = I3-or-exception + human Approver (not I5 checker); L5 = I5 required for K2/K3 wording/DOI/journal; "K1 via I3 can be public; it is public-provisional, never K2" stated explicitly |
| 3 | License split stale against founder decision (`FOUNDATION_v0.2_anchor.md` Must-fix 2) | §11 item 3 marked DECIDED (CC BY 4.0 whole repo); `REPO_SPEC_v0.3.md` tree (`LICENSE` only) |
| 4 | `D-CITATION-UNVERIFIED.state` framed as a "reuse," actually a third vocabulary (`FOUNDATION_v0.2_anchor.md` Must-fix 3 / Vocabulary forks §2) | §5, mapping table from `fetch_status`/`status`/`claim_match_verified` to `state`, including `MISMATCH` |
| 5 | `question_human`/`question_readout`/`hypothesis_world` promised in §2.3 but absent from §3.2 (`FOUNDATION_v0.2_usability.md` finding (l), Must-fix 1) | §3.2 `lens_translation.question_human`, `lens_translation.question_readout` (replaces `question_Q`), top-level `hypothesis_world`; §2.3 rewritten to point at exact fields |
| 6 | `formal_applicability`'s 4 values undefined anywhere readable (`FOUNDATION_v0.2_usability.md` finding (f), Must-fix 2 — "single worst usability gap") | §3.2b, plain-language definitions + frontline-default rule |
| 7 | Stale 4-value `verdict_tier` in `cross_vendor_review_packet.md` (`FOUNDATION_v0.2_usability.md` §1, §7, Must-fix 3) | `design/templates/knowledge/cross_vendor_review_packet.md` updated to six values (both occurrences) |
| 8 | `venue_track` has no null/none value for K0 work (`FOUNDATION_v0.2_usability.md` finding (d), Must-fix 5) | §3.2, §6.1 — `venue_track: international \| thai_tci \| none` |
| 9 | Stub `ai_filled` shape unstated (`FOUNDATION_v0.2_usability.md` finding (b), Must-fix 6) | §3.2a — `{used: bool, note: string}`, note required when `used: true` |
| 10 | `disclaimers_emitted` cannot carry parameters (`FOUNDATION_v0.2_usability.md` finding (j), Must-fix 7) | §3.2 — `[{id, params?}]` shape |
| 11 | Genre router (S5's 7-question procedure) not reconciled with the 9-genre taxonomy (`FOUNDATION_v0.2_usability.md` §3, Must-fix 8) | §6.3b, new ordered 9-question procedure, each question tied to a named claim-card field |
| 12 | No honest way to leave `provenance_dag`/`silent_lift_check` unfilled pre-kernel (`FOUNDATION_v0.2_usability.md` finding (h), Must-fix 9) | §3.2 `status: not_run \| run` on both fields; §3.3 new rule 11 (kernel treats `not_run` as ⊥, both required `run` before K1) |
| §1 three-question positioning + era-of-production stance | E (§1) | §1.1 |
| §2 spine relabels Blackbox Note box + cooking log | E (§2) | §2.1 |
| §5 catalogue merged | E (§5) | §5 |
| §6 per B1 | E (§6) | §6 |
| §7.8 per C8 | E (§7.8) | §7.8 |
| Appendix A per C6 | E (App. A) | Appendix A |
| Appendix B per A2/D4 | E (App. B) | Appendix B |
| New §13 | E (§13) | This section |
| B1–B4 overturnable; I5 is the consequential open item | F | §10, §11 |

---

## Appendix A — The Non-Collapse Table (request 17, in full)

Reproduced from `design/S9_non-collapse-table.md`, plus three rows appended this pass (chair ruling
C6 — append-only, ids never reused). 64 rows across seven families. Full table, columns, and
"how the table is used" mechanism preserved unabridged in the source file; the compact index below
gives id, pair, and the glosa field/gate that enforces it.

### Family A — Truth / Warrant
`NC-01` World≠Record≠Readout≠Meaning≠Truth≠Warrant≠Knowledge-Attribution · `NC-02` Truth≠Warrant≠
Practical Efficacy≠Ethical/Legal Legitimacy · `NC-03` Legitimacy≠Truth (horizontal & vertical) ·
`NC-04` legal≠epistemic · `NC-05` Solving≠true · `NC-06` correct output≠true theory (Bounded-Judge
Law) · `NC-07` Conformance≠Truth · `NC-08` readout≠truth (universal lens) · `NC-09` M_A[n]≠θ(E) ·
`NC-10` finite_diagnostic≠proof · `NC-11` Th_coqc≠finite_diagnostic≠Dr≠Open≠fit_calibrated≠
definition · `NC-12` Verified MATH≠true physics · `NC-13` Institutional accept/reject≠Truth.
*Enforced by: `tier`, verdict_tier, verdict enum, §1.3/§4.1, §7.3.*

### Family B — Access / Inference
`NC-14` Existence≠Attribution≠Disclosure (E-A-D) · `NC-15` represented≠actual essential dependency
set (Silent Lift) · `NC-16` doxastic warrant≠assertoric disclosure · `NC-17` Mechanical validity≠
Semantic validity · `NC-18` Source existence≠Claim support · `NC-19` metadata_verification≠
scope_verification · `NC-20` reliable route≠crediting a specific source · `NC-21` training-derived
background≠current-case-specific access route · `NC-22` access model K̃≠literally reading K* ·
`NC-23` P_A≠H_A (appearance≠epistemic horizon) · `NC-24` forced≠borrowed≠Open · `NC-25` 0≠⊥ ·
`NC-26` "not checked"≠"checked, nothing found" (A2) · `NC-27` LOCAL_EVIDENCE_NOT_FOUND≠NO_LOCAL_
EVIDENCE_EXISTS. *Enforced by: `silent_lift_check`, citation card booleans, `zero_vs_bottom`, §3.3,
§7.8.*

### Family C — Independence / Review
`NC-28` maker≠checker≠approver · `NC-29` AI generator≠AI reviewer of the same commit · `NC-30`
same-model self-approval≠review (MC-02) · `NC-31` ManyModels⇏Independence · `NC-32` DVP≠K2 ·
`NC-33` K1≠Certification · `NC-34` No independent check⇒No K2 / No independent check⇒No release
(two distinct gates) · `NC-35` Observation≠Claim≠Inference≠Hypothesis≠Decision≠Valid-checkpoint≠
Success≠Skill-plan≠Installed-skill≠Design-doc≠Working-product · `NC-36` Reproduction≠Replication ·
`NC-37` Evidence≠Evidence Relation. *Enforced by: `independent_check`, §4.2, §7.1–7.2.*

### Family D — Credit / Legitimacy
`NC-38` Credit≠EpistemicValue · `NC-39` Attention≠Credit · `NC-40` Friction≠Fellowship · `NC-41`
Friendship≠IndependentEvidence; Correspondence≠PeerReview; IntellectualAffinity≠Truth · `NC-42`
Production-supercritical≠Credit-supercritical · `NC-43` Latent≠Legible programme coherence ·
`NC-44` ActivationAction≠CreditEvent · `NC-45` PositionalAccess≠PopulationAuthority; CommunityTrust
≠Representativeness. *Enforced by: §7.6, §7.7.*

### Family E — Evidence / Search
`NC-46` Systematic Review≠Rapid/Scoping/Targeted evidence challenge · `NC-47` AI output≠Evidence ·
`NC-48` Global/Anglophone route≠Local/Thai-language route. *Enforced by: `review_mode` enum, §7.8.*

### Family F — Practice / Positional
`NC-49` Practice experience≠Population evidence · `NC-50` Intervention creator≠Sole evaluator ·
`NC-51` Author positional counter-readout≠External K2 · `NC-52` Thai track≠Public relations ·
`NC-53` No human available≠Research stop · `NC-54` Standpoint disclosure≠Domain-credentialed
authority. *Enforced by: `scope.generalization_claimed`, `standpoint`, §1.3.*

### Family G — AI / Authorship
`NC-55` Discovery≠Justification · `NC-56` AI exploration≠Human commitment · `NC-57` Claim scope≤
Evidence scope · `NC-58` AIContribution≠EpistemicResponsibility · `NC-59` AI-candidate output≠
Verified citation (Integrity Firewall) · `NC-60` Founder=ideas/direction≠AI=assistant · `NC-61`
questions defended without AI≠questions merely produced with AI. *Enforced by: `ai_filled`,
`produced_by`/`responsible`, §7.5, §7.8.*

### Family H — New this pass (chair ruling C6)
`NC-62` Stakeholder ≠ Agency — being affected by a decision is not the same as holding power over
it (skillme's stakeholder-agency map, re-derived independently, pattern only). *Enforced by:
`five_questions.assumed[]` review; the Project Advisor's stakeholder framing, §7.7.*
`NC-63` Representationality ≠ Selectivity — that a source is *representative* of a population is a
different property from that a source was *selected* by some (possibly biased) process; conflating
them silently launders a selection artifact into a population claim. *Enforced by:
`scope.generalization_claimed`, §3.2.*
`NC-64` SelfExperience ≠ GeneralEvidence — a first-person account licenses a claim about that
person's own experience, never automatically a claim about a population. *Enforced by:
`standpoint`, the preserved-experience field per genre (§6.2), §2.4.*

---

## Appendix B — Market/neighbour positioning (founder ruling, request 31 — supersedes S13's original framing)

Per request 31 and chair ruling A2/D4, the market audit's original file
(`design/S13_market-collision-audit.md`, Dr, one pass, 5/5 spot-checked facts confirmed accurate by
independent review) is retained on disk as the underlying research readout, and is **rewritten in
full into `design/S13_neighbour-table.md`** — the third deliverable of this synthesis round. That
file is the canonical, cited form; this appendix states only the framing rule and points there.

**Framing rule (unchanged from v0.1, restated without "residual"/"concession" language per A2):**
every row states what problem a neighbour solves, by which method, and how it is the same as or
different from glosa — never a novelty contest, never "no tool does this." Wording rule: comparison
text never says "we take/reuse/borrow from them" by default — it says same/different/cited;
"adopted from" is used only when a human explicitly instructed adoption, with a Blackbox Note line
or `DECISIONS.yaml` row naming it (request 31g–31i). The closest real neighbour found is
**nanopublications** (assertion-level, citable, machine-readable provenance objects) — stated in
`design/S13_neighbour-table.md` descriptively (same: assertion-level provenance packaging;
different: glosa ties the assertion to a source-licensing/identification-ladder check and a
mechanically-bound independence-tier ceiling that nanopublications' own page does not state), never
as "glosa must concede novelty to nanopublications" (that framing is retired with S13's original
document). **Not yet wired into any gate** (`reviews/S13_anchor.md` Must-fix 1, still open in this
pass): a future revision should cite an entry from `S13_neighbour-table.md` from the `D-COMPARISON`
disclaimer trigger (§5) whenever a `conceptual`-genre paper makes a same/different claim, tiered no
higher than the audit's own independence level.
