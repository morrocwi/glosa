# Spine and Claim Card summary (frozen excerpt)

> **Purpose:** a standalone, easy-to-open copy of the two sections `AGENTS.md`'s gate rule 2
> currently requires reading before editing anything in this repo, so a fresh session does not
> have to load the entire FOUNDATION document to satisfy the gate. This file is a **readout of one
> moment**, not a living document — when it and the source file disagree, the source file wins,
> and `tools/check_spine_summary_freshness.py` (below) is the mechanical check for exactly that
> drift.

## Source

- **Source file (repo-relative path):** `design/FOUNDATION_v0.6.md`
- **Sections excerpted:** `## 2. The spine ...` (§2, including §2.1–§2.5) and
  `## 3. The claim card — final schema field list` (§3, including §3.1–§3.3) — the two sections
  `AGENTS.md` gate rule 2 names ("§2 (spine) and §3 (claim card)").
- **Hash used, and why:** `git hash-object design/FOUNDATION_v0.6.md` (the **blob hash** of the
  file's exact content), not the commit hash of `git log -1 --format=%H -- <file>` (which names
  the commit that last touched the file, not the content directly) — chosen because the freshness
  checker below needs to compare *content*, and `git hash-object` is the direct, single-command way
  to recompute that from a working-tree file without also needing a commit walk.
  - **Blob hash (`git hash-object design/FOUNDATION_v0.6.md`):** `0abaafa9c6274276a13ed7aabcb76ebd95f474d3`
  - **For cross-reference only, not used by the checker:** the last commit that touched this file
    (`git log -1 --format=%H -- design/FOUNDATION_v0.6.md`) is `3096b49ad001e7926d6198cc51f0dbd1f74c12a6`.
- **Excerpt method:** **verbatim** — the two sections below are an exact `sed`-range copy of lines
  257–1108 of `design/FOUNDATION_v0.6.md` as of the blob hash above (the file's own line numbering
  at that hash: §2 opens at line 257, §3 closes at line 1108 immediately before the next `---`
  divider). No wording, formatting, or Thai text was altered, shortened, or translated. Nothing
  below this point is lightly excerpted; if a future revision of this summary ever does excerpt
  lightly, that revision must mark it inline the same way this note marks the current one as
  verbatim.

## Known open item this task found (flagged, not silently fixed)

`AGENTS.md` gate rule 2 currently reads:

> Read design/FOUNDATION_v0.5.md §2 (spine) and §3 (claim card) before editing anything ...
> (One canonical spec pair: design/CURRENT_SPEC.txt names FOUNDATION_v0.5.md + REPO_SPEC_v0.5.md.)

But `design/CURRENT_SPEC.txt` on this same commit actually names:

```
FOUNDATION_v0.6.md
REPO_SPEC_v0.6.md
```

So `AGENTS.md`'s own prose (both the file name in its gate rule and its parenthetical claim about
what `CURRENT_SPEC.txt` says) is stale — it still names v0.5 in both places, while the actual
current spec pair is v0.6. This summary was built against `FOUNDATION_v0.6.md` (the file
`CURRENT_SPEC.txt` actually points to) per this task's instruction to use whichever file is
*actually* current. **Suggestion, not applied here:** `AGENTS.md` gate rule 2 should be updated to
say `FOUNDATION_v0.6.md` / `REPO_SPEC_v0.6.md` in both the file name and the parenthetical. This is
a separate, flagged suggestion — this task deliberately did not edit `AGENTS.md`'s gate requirement
itself, per this task's own instruction not to change that silently.

Note also: `design/FOUNDATION_v0.7_PATCH.md` exists in the repo, but it is explicitly self-labeled
"Tier: Dr, specified not applied. This file states the exact text/field/rule diffs to apply to
`FOUNDATION_v0.6.md` to produce v0.7. It does not itself edit `FOUNDATION_v0.6.md` ..." — so v0.6
is correctly still the applied/current foundation text, not v0.7; this summary is not stale with
respect to that patch.

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
Academic hypothesis(es) + falsifier(s) (R2_1..R2_n, internal stage label,        │  spine —
world language — n candidate hypotheses from one lens-in/lens-out pass)          │  every
        │                                                                        │  transformation
        ▼                                                                        │  appended,
Literature Review System × n (LRS, §7.9 — ONE run per hypothesis, never one      │  never sealed
merged search across several: search → acquire → extract → dialogue table →     │
cite-check → litreview_manifest, per hypothesis, each frozen separately)         │
        │                                                                        │
        ▼                                                                        │
Hypothesis selection (human, non-delegable — hypothesis_selection.yaml compares  │
the n manifests/dialogue tables; parked candidates are kept, never deleted;      │
the choice is logged in the Blackbox Note's cooking log, §7.9)                   │
        │                                                                        │
        ▼                                                                        │
Genre route (§6, venue_track) → rigorous method (tiers, MIMCG, DVP,              │
disclaimers, S4 gates) → paper (genre-routed)                                    │
        │                                                                        │
        ▼                                                                        ┘
Zenodo + GitHub (K1)
```

**Spine change this pass (founder requests 35b/35d, binding):** LRS and hypothesis selection are
now named stages of the spine itself, not an appendage of S3 or S4 — S3 owns the lens translation
only, S4's method design consumes the *selected* hypothesis's evidence base and does not itself run
searches. Full detail: §7.9 and `design/S14_literature-review-system.md`.

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

### 2.1a Problem before observation (founder instruction, 2026-09-04, BBL-2026-09-04-083/084)

**Founder's own line (BBL-2026-09-04-083, Blackbox Log, concept DOI `10.5281/zenodo.22302518`,
verbatim):** *"แต่คำว่าสังเกต มันเป็นนามธรรม คือเป็นกริยา ถ้าเราเริ่มจำปัญหาหละ มันมีกระบวนการแบบนี้ไหม
เราก็เลยเสนอให้โฟกัสปัญหาแถน"* — "observation" is abstract, it is a verb; if we started from the
problem instead, is there a process like this? The founder proposed focusing on the problem first
(BBL-2026-09-04-084 carries the instruction to adopt this into the spine, cited alongside).

A problematic state exists in the world **before** any knower acts on it — before it is looked at,
named, or measured. "Observation" is not itself a starting node; it is a verb, the *first act* a
knower performs on that pre-existing state. glosa's Blackbox Note is the record of exactly that
first act — the first readout of the problem state, raw, in the knower's own words, timestamped and
never edited in place (§2.3) — which is why it sits at the head of the spine rather than being
folded into S1 Problem intake as an afterthought.

Making the pre-readout layer visible, the spine (§2.1's diagram) reads, one layer finer at its own
head:

```
Problem state (unread, pre-subjective — no record exists of it yet)
        │
        ▼
First human readout (the Blackbox Note's raw line — verbatim, untranslated, this IS "observation"
        │  as a verb, not a noun: the knower's first act on the problem state)
        ▼
Human-language question (question_human, §2.3/§3.2 — the question as lived)
        │  [lens-in: Lens Law]
        ▼
Hypothesis (lens-out, signed — hypothesis_world.signature, §3.2, kernel rule 12)
        │
        ▼
Evidence (five_questions.tested)
        │
        ▼
Provisional knowledge (K0, K1, ...)
```

**We deliberately do not write "Reality →" as the first node.** The lens never grants direct access
to reality — only to what was read out (`RA = OA(W;ΠA) ≠ W`, §1.0 Pillars, ontology). Writing
"Reality" as a spine node would silently claim the record touches the world-in-itself; the honest
first node is the problem state as it stood before any readout, immediately followed by the first
readout that is the only thing anyone ever actually has. This is the same discipline §1.0's
ontology pillar already states for the claim card (`RA ≠ W`), applied here to the spine's own
starting point.

This subsection adds vocabulary to §2.1's existing diagram; it does not replace or renumber that
diagram, and does not reopen S1–S6 stage ownership (§2.2) or the Blackbox Note's own schema
(§2.3/`schema/blackbox_note.schema.json`), which are unchanged.

### 2.1b Responsibility per arrow: Data → Inference → Claim (founder instruction, 2026-09-04, BBL-2026-09-04-083/084)

Every arrow in the spine — not only the whole pipeline as one undifferentiated "co-production" — is
named by who performed it: `human`, `ai`, or `joint`. Two arrows are singled out because they carry
the most consequence:

- **Data → Inference** (the move from a recorded observation to a drawn inference about it) may be
  performed by human, AI, or jointly — `produced_by`'s existing three-value vocabulary (§3.2)
  applies here directly, no new enum needed.
- **Inference → Claim** (the move from an inference to a standpoint-committed claim someone will
  publicly hold) is **always human**. The human signs the claim; AI is never an author
  (`AGENTS.md` gate rule 5, `CLAUDE.md` gate rule 5, unchanged repo-wide invariant). This is not a
  new rule so much as this pass naming, per-arrow, a distinction that was previously stated only at
  the whole-artifact level (`responsible: human`, `produced_by`, §3.2).

This is spec text for a `responsibility` block on the claim card (schema-expressible; see §3
below) — `data_to_inference: human|ai|joint`, `inference_to_claim: human` (const), optional
`notes`. A card that declares `responsibility` but signs `inference_to_claim` as anything other
than `human` fails validation (kernel rule — see §3.3). A card that omits `responsibility`
entirely still passes (the field is optional, since a K0-stub authoring-cost floor already exists,
§3.2a) but emits a warning naming the arrow that was left undeclared, per this section's own
discipline: silence about who did the inference-to-claim step is the same class of problem §3.3
rule 7/12 already treat as unacceptable when applied to lens authorship — applied here to
authorship of the claim itself.

**Mother-equation framing (cited, kc-base-014, kc-base-020 — this pass, v0.6,
`design/FOUNDATION_v0.6_PATCH.md` §17).** "A record is a translation, never the truth itself" —
cited here as the framing that grounds why this section's Data→Inference→Claim responsibility
split treats each arrow as carrying its own, non-transferable responsibility obligation, rather
than one blanket "the data supports the claim" statement.

### 2.1c Ownership criterion: problem, question, and the *selection* of the hypothesis stay human (founder instruction, 2026-09-04, BBL-2026-09-04-086/087, wording corrected in BBL-2026-09-04-088)

Founder's line, verbatim (Blackbox Log BBL-2026-09-04-088, correcting -086; concept DOI 10.5281/zenodo.22302518):

> ถ้าปัญหายังเป็นของเรา / คำถามยังเป็นของเรา / และ 'การเลือก'สมมุติฐานยังเป็นของเรา / แล้วนำไปสู่การแก้ปัญหาให้เรา
> จะใช้เอไอใช้แมวใช้หมี ก็ใช้ไปเถอะ เพราะนั่นคือเป้าหมายของความรู้ — แก้ปัญหาให้ใครสักคน

Read through the spine (§2.1a) this is the criterion that answers "which part is us?" when the
tools are AI: three acts on the spine — owning the **problem**, asking the **question**, and **selecting the
hypothesis** — are the human's; every other node (retrieval, drafting, analysis, checking, rendering) may
be performed by any tool. Ownership here means the human-language question was the human's, the
problem was the human's own problematic state (§2.1a), and the hypothesis — whoever drafted the candidates, AI included — was *selected* and signed
by the human (§7.4 D-LENS-UNSIGNED, §2.1b Inference → Claim). The goal of knowledge under this
criterion is stated as the founder stated it: to solve a problem for someone — not to prove the
author right, not to earn a status.

Spec consequence (schema-expressible, §3): the `responsibility` block gains an optional
`ownership` object `{ problem, question, hypothesis_selection }`, each `human` (const) — AI may
propose candidate hypotheses; the choice is the human's. A card that declares
`ownership` with any of the three not `human` fails validation (kernel rule 15, same rule as the
signed Inference → Claim arrow, since it is the same criterion seen from three nodes). A card that
omits `ownership` passes with the rule-15 warning. Comparison to neighbours: "human-in-the-loop"
framings in the AI-assisted-research literature describe the same shape of concern (same);
they usually place the human at *review* or *approval* points rather than at problem, question and
hypothesis ownership (different); citation card PENDING for that comparison.

### 2.2 Six stages, six owning artifacts, six gates

Unchanged from v0.1 §2.2 in structure and content, with one field-name substitution applied
throughout the co-production and gate columns: every occurrence of `origin_r0_ref`/`origin_
dialogue_ref` is now `origin_blackbox_ref` (§3.2, chair ruling A1/C8), S5's exit gate now names
the appendix by its new title, and this pass adds two new rows, **S3b** and **S3c** (founder
requests 35b/35d), between S3 and S4 — see §7.9 for the full Literature Review System these two
rows own:

| Stage | Thai | Owns artifact | K-state at exit | Gate into next stage | Co-production split (request 24) |
|---|---|---|---|---|---|
| **S1 Problem intake** | ปัญหา | Problem Card (`schema/problem_card.schema.json`) | K0 | Two-question intake complete; standpoint declared; readiness verdict `READY_FOR_S2` (self-check, not a release gate) | Human: states the issue, own words, own standpoint. AI: routes the intake, never infers Q2's answer. |
| **S2 Experience → record** | ประสบการณ์ | Source Card + Observation Card + `logbook.jsonl` | K0 | `access_type` typed (including `provenance_indeterminate`); `scope.generalization_claimed` never advanced past `none` at this stage | Human: is the observer/source of record for anything human-participant. AI: may transcribe under `access_mode: ai_assisted_capture`, never sole observer of a human-participant event. |
| **S3 Hypothesis via readout lens** | สมมติฐานวิชาการ | Claim Card (§3, the canonical schema), n candidate `hypothesis_world` values (R2_1..R2_n) | K0 | `lens_translation` filled before `five_questions`; `non_claims` non-empty; `tested.falsifier` non-empty and names an observation, not a negation | Human: owns the falsifier judgment and the standpoint. AI: fills `ai_filled.*`, discloses every inferential commitment it contributed. |
| **S3b Literature review (LRS × n)** *(new this pass, request 35/35b)* | ทบทวนวรรณกรรม | `litreview_manifest.yaml` + `dialogue_table.md`, one pair per hypothesis (§7.9) | K0 | `litreview_manifest.gate.overall ∈ {PASS, PASS_WITH_LIMITS}` for this hypothesis's manifest, or the hypothesis carries `D-CITATION-UNVERIFIED`/`D-LIT-*` disclosure and does not proceed to S3c selection with a hidden `FAIL` | Human: holds the private research-library shelf, is the I5 route or confirms a decorrelated I3 route, signs the manifest as `human_owner`. AI: runs searches, drafts dialogue-table rows, never self-certifies its own `claim_match_verified`. |
| **S3c Hypothesis selection** *(new this pass, request 35d)* | เลือกสมมติฐาน | `hypothesis_selection.yaml` (§7.9) | K0 | `selection.chosen` (zero, one, or more) recorded with a non-empty `reason`; every parked candidate keeps a non-empty `reason` and its manifest/dialogue table stay in the repo; the event is appended to the Blackbox Note's `cooking:` log | Human: makes the selection (non-delegable, `responsible: human`). AI: proposes the comparison table's contents, never the decision. |
| **S4 Rigorous method** | วิธีวิทยาเข้มข้น | `review_report`, `evidence_relation`, disclaimer set attached | K0→K1 (only with ≥I3, §4.2, subject to the bounded I2+I4 exception, chair ruling B4) | MIMCG gate table (§7.1) passed at the consequence level the artifact reaches | Human: is Checker or Approver whenever the artifact reaches L3+; never the same identity as Maker. AI: may be Checker only at I2/I3 (never sole gate to K1 without an I3 route; never K2 alone). |
| **S5 Paper / genre** | เปเปอร์ | Genre-routed manuscript (§6), Claim Matrix, Blackbox Note appendix | K1-candidate | Human Mastery Gate (§7.5) `PASS`/`PASS WITH NAMED GAPS`; every `\claimref{}` resolves in the Claim Matrix; **"Blackbox Note: how this work was made" appendix present** (hard gate, request 28/32) | Human: defends the paper unaided (Human Mastery Gate). AI: drafted structure/prose under disclosed route, never the mastery-gate answer itself. |
| **S6 Publish / archive** | บันทึกเข้า Zenodo/GitHub | Release manifest, CITATION.cff/.zenodo.json/codemeta.json, Zenodo DOI | K1 (published) | `PUB-ADVERSARIAL-REVIEW` R1–R7 (§7.4) passed; version triple-equality (`PRESERVE_EXACT` from zero-readout-certifies, §1.2); PR-only merge | Human: founder is the non-delegable Approver and sole formal author. AI: attribution lives only in commit trailers, AI-assistance disclosure, and `ai_filled` fields — never in `CITATION.cff` authorship. |

### 2.3 Blackbox Note and R0/R1/R2 internal registers (founder ruling, request 32, supersedes request 30's "Register Zero")

Three internal stage labels, all retained, never collapsed into one polished version, all living
inside one note:

- **Blackbox Note (บันทึกกล่องดำ) — raw human voice + cooking log.** Verbatim, untranslated, typos
  kept, timestamped, speaker-by-role. Template: `templates/knowledge/blackbox_note.yaml` (ids
  `BB-YYYY-MM-DD-NN`). Never edited in place; a correction is a new line. Tier `positional/Dr`.
  Disclosure: the public Blackbox Log had one pre-release history mutation on 2026-09-04 (an
  AI-written line removed, seven founder lines dropped by a tooling error and restored with their
  original ids); it is recorded as a correction entry (BBL-2026-09-04-082) and visible in the
  Zenodo version history, not hidden. The rule stands; the violation is on the record.
  Selection into any published appendix is done by the human owner of the voice; AI may propose
  candidates only (`ai_proposed: true`).
  **Named source (this pass, v0.6, kc-ep-047, kc-ai-008, `design/FOUNDATION_v0.6_PATCH.md` §22).**
  "Blackbox Log: daily append-only verbatim voice record" is cited directly as the named artifact
  this bullet already formalizes — resolving the previously uncredited appendix language.
  Consistent with, not contradicting, `PUBLISH_GATE_v1_public.md` finding B-10's disclosed
  removal+restore correction entry (the disclosure paragraph immediately above).
- **R1 — Readout formulation** (internal label, lives inside the note's `r1_readout_ref`). The
  lens-in translation: `lens_translation.question_readout`, `local_contrast_space_X`,
  `access_relation_R`, `claim_function_Phi_z0` (the `lens_translation` block of the Claim Card,
  §3.2 — `question_readout` is the field name; earlier drafts called this `question_Q`, retired
  this pass, must-fix 5, to stop it being conflated with §3.1's unrelated "founder's Q1..Q5").
- **`lens_used` — the required lens-attribution block (NEW this pass, founder requests 38/38b,
  binding).** Every Blackbox Note now carries a **required** `lens_used` block naming the lens that
  looked at the problem and extracted the hypothesis. **Short form, printed everywhere v0.4 needs
  to name the lens (claim card `lens_ref`, paper front matter, Blackbox appendix): `display: "Readout
  Universe — Yaoharee Lahtee"`** (request 38b, exact wording). The block's other fields carry the
  long form and are read, not reprinted, wherever the short form is used: `description`
  (readout-not-truth; retained distinction; Readout Condition E–A–D), `author` (Yaoharee Lahtee),
  `orcid` (`0009-0005-3861-0626`), `references` (`10.5281/zenodo.21529456`,
  `10.5281/zenodo.21665100`, *The Readout Condition* (Aug 2026), `github.com/morrocwi/
  readout_universe`), `version_or_date_read`, `what_it_did_here.{lens_in, lens_out}` — what
  distinctions became visible reading the problem as a readout, and how the hypothesis was
  translated back into world language — and `if_other_lens`: if a different lens was used, that
  lens and its author are named instead of the display string above; a work may list more than one.
  Template: `design/templates/knowledge/blackbox_note.yaml` (already carries this block).
  **`attribution ≠ authority`** (the block's own required note, carried verbatim): naming the lens
  credits its source and lets a future reader replace it with a different lens — it does not make
  the lens's reading true, and it is not a vertical-authority citation
  (`EPIS-KNOWLEDGE-VALIDATION`). The claim card's own pointer to this block is
  `lens_translation.lens_ref` (§3.2).
  **`references` list extension, spec only, not yet applied to the template (new this pass, v0.5,
  §1.0 Pillars):** add `10.5281/zenodo.22301318` (*The Readout Condition*, Aug 2026, concept DOI
  `10.5281/zenodo.22301317`) and `10.5281/zenodo.22301202` (*Written by AI. Still True.*, Aug
  2026) to `lens_used.references` — additive only, cited alongside as the pillars source for the
  Role Separation / Possession-Constitution Collapse / Bridge Burden mechanisms this pass adds,
  never a change to `lens_used.display`'s wording (which stays exactly "Readout Universe —
  Yaoharee Lahtee," per founder requests 38/38b, unchanged). Both DOIs were confirmed published
  (CC BY 4.0) 2026-09-04 (`sources/citation_cards/CIT-written-by-ai-v6.yaml` for the second). This
  edit belongs to whichever fixer owns `templates/knowledge/blackbox_note.yaml`.
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
   sealed), **plus the note's `lens_used` block, in full** (NEW this pass, request 38/38b) — the
   appendix names which lens read the problem, by author and reference, every time; the paper's own
   front matter carries the short form of the same attribution next to the "Question as lived /
   Question as readout / Hypothesis" block (§2.3 above): **`lens_used.display`, exactly "Readout
   Universe — Yaoharee Lahtee"** (or the named `if_other_lens` value when a different lens was
   used). This session's own founder↔the AI assistant exchange (`sources/DIALOGUE_2026-09-04_the local session transcript (not public)`) is the first instance, not yet public pending the founder's line-by-line
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

**Named source (this pass, v0.6, `design/FOUNDATION_v0.6_PATCH.md` §18).** The
Existence-Attribution-Disclosure (E-A-D) norm underlying this crosswalk is cited directly to The
Readout Condition papers (kc-ep-042, kc-aihp-011, kc-ai-001) — the crosswalk table itself is
unchanged; this closes the gap of an until-now uncredited mapping.

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
  schema_version: "0.7.0"                          # bumped this pass (v0.6 doc, `design/
                                                    # FOUNDATION_v0.6_PATCH.md`) — adds `comparison`,
                                                    # `evidence_strength`, `verdict_class`,
                                                    # `gate_fail_taxonomy`, `gate_construction_status`,
                                                    # `five_questions.seen.ai_assisted_fields` (all
                                                    # additive/optional, no breaking change).
                                                    # Deliberately lands *after* the already-reserved
                                                    # "0.6.0" below (that bump was queued earlier and
                                                    # is separately still not applied to schema/
                                                    # claim_card.schema.json on disk), so the two
                                                    # change sets do not collide on one version
                                                    # number. Not yet applied to schema/claim_card
                                                    # .schema.json on disk — spec only, open item for
                                                    # the schema-owning fixer.
  # --- prior bump history ---
  # schema_version: "0.6.0"                        # bumped this pass (v0.5 doc, §1.0 Pillars) —
                                                    # adds `tested.evidence_relations[].channel`
                                                    # (new optional key, additive) and kernel rules
                                                    # 13/14 (§3.3); `review_report.rpe_check` is a
                                                    # separate schema (schema/review_report.schema
                                                    # .json), not part of this claim-card bump.
                                                    # Not yet applied to schema/claim_card.schema
                                                    # .json on disk — spec only, open item for the
                                                    # schema-owning fixer.
  # --- prior bump history ---
  # schema_version: "0.5.0"                        # bumped from v0.3's 0.4.0 this pass — adds
                                                    # `litreview_manifest_ref` and
                                                    # `hypothesis_selection_ref` (request 35/35d,
                                                    # §7.9, both nullable — additive) AND
                                                    # `lens_translation.lens_ref` (request 38/38b,
                                                    # §2.3 — REQUIRED, so this half of the bump is
                                                    # breaking against v0.3's schema, unlike the two
                                                    # nullable ref fields). Prior bump (0.4.0) added the new
                                                    # `question_human`/`question_readout`/
                                                    # `hypothesis_world` fields, the stub `ai_filled`
                                                    # fixed shape, the `disclaimers_emitted` shape
                                                    # change (bare-string array → `{id, params?}`
                                                    # objects), and the `provenance_dag`/
                                                    # `silent_lift_check` `status` fields — breaking
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
  litreview_manifest_ref: string | null             # NEW this pass (request 35, §7.9) — REQUIRED
                                                    # for any `shape: full` card that cites literature
                                                    # (any non-empty `related_citation_cards` sourced
                                                    # via a search rather than direct observation).
                                                    # Points at the frozen `litreview_manifest.yaml`
                                                    # id for the hypothesis this card instantiates.
                                                    # Null is legal only when the card cites no
                                                    # literature at all (a pure direct-observation or
                                                    # formal card) — kernel checks presence against
                                                    # `related_citation_cards` non-emptiness, never
                                                    # against the manifest's own gate verdict (that is
                                                    # §7.9's own gate, not a second copy here).
  hypothesis_selection_ref: string | null           # NEW this pass (request 35d, §7.9) — REQUIRED
                                                    # when this card's `hypothesis_world` was one of
                                                    # n ≥ 2 candidate hypotheses compared in a
                                                    # `hypothesis_selection.yaml` run. Points at that
                                                    # file's id. Null is legal only when the card's
                                                    # hypothesis was never part of a multi-candidate
                                                    # selection (n=1, no LRS-side comparison ever ran).
  lens_translation:
    lens_ref: string                                 # NEW this pass (founder requests 38/38b, §2.3)
                                                    # — REQUIRED, points at the `lens_used` block of
                                                    # the Blackbox Note this card's `origin_blackbox_
                                                    # ref` names. Printed as `lens_used.display`
                                                    # ("Readout Universe — Yaoharee Lahtee," exact
                                                    # wording, or the named `if_other_lens` value)
                                                    # wherever this field surfaces publicly. Kernel
                                                    # rule: presence-checkable only (the block exists
                                                    # and is non-empty), never a correctness check on
                                                    # the lens's own reading — same Q2/Q3/Q4-style
                                                    # presence-vs-correctness split chair ruling D2
                                                    # already states for §3.1. `attribution ≠
                                                    # authority`: this field credits a source, it
                                                    # never raises tier or independence class.
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
  hypothesis_world: { text: string, language: th|en, falsifier_ref: string,
                       signature: string }
                                                    # NEW, top-level, this pass (must-fix 5) — the
                                                    # lens-out academic hypothesis in world/discipline
                                                    # language, pointing to `five_questions.tested.
                                                    # falsifier`. Resolves §2.3's "hypothesis_world"
                                                    # promise, previously also undeclared in §3.2.
                                                    # `signature` NEW this pass (founder request
                                                    # 38d, binding) — REQUIRED whenever the card's
                                                    # `lens_translation.lens_ref` is non-empty (i.e.
                                                    # `lens_used` is present on the originating
                                                    # Blackbox Note): exact form "Hypothesis derived
                                                    # with <lens_used.display>; co-produced by <human
                                                    # role> + <AI vendor/model>; <date>" (e.g.
                                                    # "Hypothesis derived with Readout Universe —
                                                    # Yaoharee Lahtee (lens); co-produced by founder +
                                                    # the AI assistant Sonnet; 2026-09-04"). When no lens was
                                                    # used, `signature` still must be non-empty and
                                                    # says so explicitly (e.g. "Not derived through a
                                                    # named lens") — silence is never legal either way
                                                    # (§3.3 new rule 12). This same line is printed
                                                    # under every hypothesis statement in the paper
                                                    # (H1, H2, ...) and in each candidate row of
                                                    # `hypothesis_selection.yaml` (§7.9).
  five_questions:
    seen: { record_ref, as_of, retrievable_original: bool, access_model, citation_refs: [citation_card.id],
            ai_assisted_fields: [string] }           # NEW this pass (v0.6, K-C2, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` K-C2) — default `[]`.
                                                    # Names which of the card's own fields had AI
                                                    # involvement in drafting their `seen`-recorded
                                                    # content — a structural marker, not a prose scan.
                                                    # See §3.3 rule 27.
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
                independence_class: <I0..I5, §4.2>, strength, citation_ref,
                channel: reliability | independence | access | assurance | accountability |
                         calibration | error_correlation | other(named)
                                                    # NEW this pass (v0.5, §1.0 Pillars — Bridge
                                                    # Burden) — required whenever this entry is
                                                    # claimed to change a card's tier/k_state;
                                                    # `other(named)` requires the specific relation
                                                    # named inline, never bare "other". An entry
                                                    # with no `channel` may still exist (a raw,
                                                    # unprocessed evidence log line) but may NOT be
                                                    # cited as the reason `tier` or `k_state`
                                                    # advanced — kernel rule 15 below.
              } ],
              falsifier: string (required, non-empty, must name an observation/check outcome),
              dissent_records: [ { by, date, content, resolved: bool } ] }   # append-only
  comparison: { target: string | null, relation: same | different | cited | not_compared, basis: string }
                                                    # NEW this pass (v0.6, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` §2) — `relation` is a
                                                    # closed enum; the words "novel", "first", "best",
                                                    # "outperforms" and their Thai equivalents (ใหม่,
                                                    # ครั้งแรก, ดีที่สุด, เหนือกว่า) are schema-rejected as
                                                    # `relation` or `basis` values (gate rule 6 —
                                                    # CLAUDE.md/AGENTS.md's governance-file novelty
                                                    # ban, disambiguated from this FOUNDATION's own
                                                    # numbered kernel rule 6, `scope.claim_scope ≤
                                                    # scope.evidence_scope`). `not_compared` is legal
                                                    # and is the correct default when no comparison
                                                    # was attempted — never inferred from an empty
                                                    # field; an empty field is itself a validation
                                                    # error once `comparison` is present at all. See
                                                    # §3.3 rule 20.
  evidence_strength: { class: direct_validation | adjacent_precedent, notes: string }
                                                    # NEW this pass (v0.6, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` §2) — `direct_
                                                    # validation` = the evidence bears on the
                                                    # intervention/claim itself; `adjacent_precedent`
                                                    # = the evidence bears on a related but distinct
                                                    # prior case, read across by analogy — this class
                                                    # may never be silently promoted to `direct_
                                                    # validation` in prose that cites it (`NC-72`
                                                    # Constraint≠evidence-for-us, applied here to
                                                    # evidence class).
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
  verdict_class: DERIVED | FORCED | DEFINITIONAL-RELABEL | POSITED | BORROWED-SCALE | OPEN
                                                    # NEW this pass (v0.6, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` §5) — a **different
                                                    # axis** from `base_relation` (how a claim relates
                                                    # to a base text): `verdict_class` states what
                                                    # *kind* of derivation the claim itself is,
                                                    # independent of any base-text relation; the two
                                                    # fields are never collapsed into one enum. An
                                                    # unlisted seventh value is a hard schema error
                                                    # (§3.3 rule 23).
  gate_fail_taxonomy: { injected_infinity_type: I1 | I2 | I3 | I4 | null,
                        injected_zero_type: Z1 | Z2 | Z3 | Z4 | null }
                                                    # NEW this pass (v0.6, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` §1) — a hard-fail
                                                    # raised when claim-card prose injects a
                                                    # non-readout infinity/zero must carry a named
                                                    # type from kc-base-016's own taxonomy, verbatim,
                                                    # never a generic untyped rejection. See §3.3
                                                    # rule 18.
  gate_construction_status: { gate_id: string, type: Type-P | Type-U, failing_control_ref: string | null }
                                                    # NEW this pass (v0.6, `design/
                                                    # FOUNDATION_v0.6_PATCH.md` §1) — a per-gate
                                                    # construction/validation record (Fail-Able Gate
                                                    # Law, kc-base-008), never a per-firing verdict.
                                                    # `failing_control_ref` required non-null when
                                                    # `type=Type-P`. See §3.3 rule 19.
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

**Parallel Bridge Burden field on `citation_card.yaml` (spec only, not yet applied to the
template — v0.5, §1.0 Pillars):** `templates/knowledge/citation_card.yaml` should carry a
parallel note field, not a new boolean (the card's existing tuple already covers the mechanism —
`design/S15_pillars-ontology-epistemology-methodology.md` Pillar 2 §2.3's crosswalk table):

```yaml
credibility_channel: ""   # one line naming which of verification_method / identifier.kind /
                          # metadata_verified / claim_match_verified / evidence_tier / scope /
                          # who_verified is doing the work when this card's status is cited as a
                          # reason to raise or lower confidence in the claim it backs. Optional but
                          # recommended; required whenever the card is cited in a `D-COMPARISON` or
                          # `D-AIFILL` context (Bridge Burden applied to citation use specifically).
```

This field is specified here, not applied to the template file — that edit belongs to whichever
fixer owns `templates/knowledge/citation_card.yaml` (see `design/FOUNDATION_v0.5_PATCH.md` §3,
open item 1).

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
12. **`hypothesis_world.signature` must be non-empty; `lens_translation.lens_ref` non-empty
   requires the signature to actually name that lens (new this pass, founder request 38d,
   binding).** A card whose `lens_ref` is populated but whose `hypothesis_world.signature` is empty
   or absent is a **hard validation error**, not a warning — fires `D-LENS-UNSIGNED` (§5). A card
   with no lens used still requires a non-empty `signature` stating so explicitly (e.g. "Not
   derived through a named lens") — an empty string is illegal either way; silence about
   authorship-of-method is exactly the kind of silent lift §3.3 rule 7 already treats as a hard
   failure, applied here to the hypothesis-derivation step specifically.
13. **An `evidence_relations[]` entry with no `channel` (or `channel: other` with no named
   relation) may be logged, but may never be cited in `disclaimers_emitted`, a review report, or
   public prose as the reason a card's `tier` or `k_state` advanced** (new this pass, v0.5, §1.0
   Pillars — Bridge Burden, `NC-66`/`NC-70`).
14. **An `evidence_relations[]` entry with `bearing: CHALLENGES` requires a non-empty
   `evidence_id`** (new this pass, v0.5, §1.0 Pillars). An unnamed, unrepresented possible failure
   mode is not a defeater — it is an open item, and belongs in `identification_ladder`'s
   `unidentified` value or `non_claims`, never in the evidence list disguised as a challenge
   (`NC-72`).

**Rules 15–17 (folded into this numbered list this pass, v0.6 — shipped in `kernel/
glosa_kernel.py` before this pass but not previously folded into this prose list; text drawn from
where each rule already appears elsewhere in this document, unchanged):**

15. **`responsibility.inference_to_claim` must equal `human` (const); `ownership.problem`,
   `ownership.question`, and `ownership.hypothesis_selection` must each equal `human` (const) when
   the `ownership` block is present** (§2.1b, §2.1c). A card that declares `responsibility` but
   signs `inference_to_claim` as anything other than `human`, or declares `ownership` with any of
   the three not `human`, fails validation — a hard error. A card that omits `responsibility` or
   `ownership` entirely still passes (both fields optional, per the K0-stub authoring-cost floor,
   §3.2a) but emits `rule15w`, a warning naming the arrow/field left undeclared — silence about
   who did the inference-to-claim step or the selection step is the same class of problem rule 7/12
   already treat as unacceptable when applied to lens authorship, applied here to authorship of the
   claim/selection itself.
16. **A card whose `standpoint.declared_basis` extends beyond direct practice/lived observation
   into a population-level or generalized empirical claim without `scope.generalization_claimed`
   advancing past `none` emits `rule16w`, a warning** (empirical-extension warning) — logged, not a
   hard fail, naming the mismatch between declared basis and generalization scope for a human
   reviewer's attention (§3.1 Q1/§3.2 `scope`).
17. **Source-first citation**: a citation card whose text was fetched must carry all four of
   `fetched_from_url`, `page_or_locator`, `line_or_paragraph`, and one continuous verbatim
   `exact_passage` (no ellipses, no composite quotes) before it may stand above `CANDIDATE` (§8,
   BBL-2026-09-04-100/101); `rule17w` fires when any one of the four is present but another is
   missing (partial provenance, logged not blocked below `CANDIDATE`).

**Rules 18–28 (new this pass, v0.6, `design/FOUNDATION_v0.6_PATCH.md` §1–§23, K-C1–K-C3):**

18. **Injected-infinity/zero scan (new standalone kernel text-scan rule, ported from the S4
   prototype — not an extension of rule 8's `EXTERNAL_VALIDATION_PROPOSED` scan, an unrelated
   family).** A hard-fail raised when claim-card prose injects a non-readout infinity/zero must
   carry a named type from `kc-base-016`'s own taxonomy, verbatim — `injected_infinity_type: I1 |
   I2 | I3 | I4` or `injected_zero_type: Z1 | Z2 | Z3 | Z4` — never a generic, untyped rejection.
   Per `kc-base-016`: I1 = ℝ-completeness (LUB/Dedekind); I2 = `h→0`; I3 = `Re,Λ→∞`; I4 = actual
   `+∞`. Z1 = the point `r=0`; Z2 = reached continuum `h=0`; Z3 = absolute rest `v=0,T=0`; Z4 = the
   true void. Reciprocity `1/0=∞` names zero and infinity as one non-readout seen from two sides,
   never two separate facts (cross-referenced to the still-`[Open]` `foundation.s1.0-infinity-
   tension-flag`, §1.0 — this rule classifies the *pattern*, it does not resolve that flagged
   tension). `rule18(TAXONOMY-UNTYPED)`: `"rule18: injected-infinity/zero hard-fail requires a
   named I1-I4/Z1-Z4 type per kc-base-016, not a generic rejection"` (error).
19. **Fail-Able Gate Law (matches its cited source, `kc-base-008`, verbatim — a gate-construction
   requirement, not a per-verdict split).** A gate may only be labeled **Type-P** (genuinely
   evidence-bearing) once it has been shown, by construction, to carry both a machine-derived
   passing control and a machine-derived failing control that it correctly rejected. A gate that
   has only ever demonstrated passing cases — no matter how many — has not shown it can tell signal
   from absence of signal, and stays **Type-U** until a real failing control is produced and
   correctly rejected. `review_report`/gate documentation must state, per gate, which label applies
   and cite the failing-control evidence for any gate claimed Type-P. `rule19(GATE-TYPE-UNSTATED)`:
   `"rule19: a gate may not be recorded Type-P without a cited machine-derived failing control it
   correctly rejected -- absent that, it stays Type-U"` (error).
20. **Novelty-word rejection**: `comparison.basis` (§3.2) containing a novelty/priority word
   ("novel"/"first"/"best"/"outperform", English or Thai — ใหม่/ครั้งแรก/ดีที่สุด/เหนือกว่า) is a
   schema-level hard error (gate rule 6, disambiguated from CLAUDE.md/AGENTS.md's own governance
   novelty ban of the same name). `rule20(NOVELTY-WORD-REJECTED)`: `"rule20: comparison.basis
   contains a novelty/priority word ('novel'/'first'/'best'/'outperform', English or Thai) -- gate
   rule 6 forbids this at the schema layer"` (error).
21. **Genre/register layer-mismatch diagnostic** (§6.3c) — flags a claim card's genre/register
   against the tool/authority actually invoked on it; diagnostic-only, never auto-reroutes.
   `rule21(LAYER-MISMATCH-FLAGGED)`: `"rule21: genre/register layer does not match invoked
   tool/authority layer -- routed to human review, not auto-corrected"` (warning, not error —
   diagnostic-only, §6.3c's own pending-founder scope note applies).
22. **Claim-tier intake flag** (§7.9) — a `litreview_manifest.yaml` `citations[]` entry flagged
   `intake_tier: request_tier` requires a non-empty `intake_tier_reason`, never merged with a
   rejected row. `rule22(INTAKE-TIER-UNTIERED)`: `"rule22: a citations[] entry flagged
   intake_tier=request_tier requires a non-empty intake_tier_reason, never merged with a rejected
   row"` (error) — pending-founder scope note applies (§7.9).
23. **Verdict-class vocabulary**: `verdict_class` (§3.2) must be one of the six listed values — an
   unlisted seventh value is a hard schema-validation error. `rule23(VERDICT-CLASS-UNLISTED)`:
   `"rule23: verdict_class must be one of the six listed values -- an unlisted seventh value is a
   hard schema-validation error"` (error, schema-enforced, no kernel code needed — parallels rule
   1/2/10/11's schema-only enforcement).
24. **Premature Category Stabilization (PCS) red-flag** (§5, pending-founder) — fires only when a
   claim exhibits **both** (a) closure-timing and (b) absence-of-adaptation jointly; neither alone
   fires this flag. `rule24(PCS-JOINT-CONDITION)`: `"rule24: Premature Category Stabilization flag
   requires BOTH closure-timing AND absence-of-adaptation to hold jointly -- neither alone fires
   this flag"` (error, when both hold); `rule24w`: `"closure-timing present without absence-of-
   adaptation (or vice versa) -- logged, not flagged as PCS"` (warning).
25. **Discovery-routing extension** (§7.9, pending-founder) — `discovery_routing.used=true`
   requires every `candidate_questions` entry to have a `k_epi_gate_log` row before it may enter
   L1. `rule25(DISCOVERY-CANDIDATE-UNGATED)`: `"rule25: discovery_routing.used=true requires every
   candidate_questions entry to have a k_epi_gate_log row before it may enter L1"` (error).
26. **Composite-quote detector** (§7.8, K-C1) — a citation card's `exact_passage` containing an
   ellipsis marker ("…", "...", or a spaced double-hyphen " -- ") splicing across a boundary is a
   composite quote: text assembled from non-contiguous source material presented as one continuous
   passage — a hard error, not a disclaimer (`NC-18` Source existence≠Claim support, applied to
   passage-level contiguity). `rule26(COMPOSITE-QUOTE)`: `"rule26: exact_passage contains an
   ellipsis/splice marker ('…'/'...'/' -- ') -- composite quotes are not verifiable as a single
   continuous passage"` (error).
27. **Hidden-AI-fill detector** (§7.8, K-C2) — when a field name appears in
   `five_questions.seen.ai_assisted_fields` but the corresponding `five_questions.ai_filled`
   sub-field is absent, empty, or reads a not-applicable placeholder while `seen`'s own content for
   that field still reads as a first-hand, directly-observed record, the two records contradict
   each other — a hard error, the E-A-D Disclosure failure `silent_lift_check` is designed to
   catch structurally. `rule27(HIDDEN-AI-FILL)`: `"rule27: five_questions.seen.ai_assisted_fields
   names a field with AI involvement that ai_filled does not correspondingly disclose --
   contradiction between disclosure records"` (error).
28. **Inflated-bearing detector** (§7.8, K-C3) — an `evidence_relations[]` entry with `bearing:
   SUPPORTS` is a hard error unless `strength` explicitly states "context" when either (a)
   `citation_ref` does not resolve to any known citation card, or (b) the resolved citation card's
   own `scope` is `CONTEXT_ONLY_NOT_EVIDENCE`, or (c) the claim card's own `evidence_relations[].
   notes` marks the source as same-lineage/own-lineage.
   `rule28(INFLATED-BEARING)`: `"rule28: evidence_relation bearing=SUPPORTS has an unresolvable
   citation_ref, or cites a scope=CONTEXT_ONLY_NOT_EVIDENCE citation card, or the claim card's own
   notes mark it same-lineage, without strength='context' -- bearing is inflated relative to what
   the citation actually supports"` (error).

**Companion binding rule (§5 disclaimer catalogue, `D-AIFILL` entry, new this pass, v0.5):**
`D-AIFILL` discloses a route property; it is never itself a tier/independence penalty. Any tier or
independence effect attributed to an `ai_filled.*` sub-field must be justified by that specific
sub-field, named, not by `ai_filled.used: true` alone.

---

