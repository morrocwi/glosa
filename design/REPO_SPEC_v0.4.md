# glosa Repo Spec v0.4 — directory tree, one-line purpose, owner-rule

> **ARCHIVED — superseded by `FOUNDATION_v0.5.md` / `REPO_SPEC_v0.5.md`; kept for lineage. Do not use as current spec.**


> **Tier: Dr.** Companion to `design/FOUNDATION_v0.4.md`. Updates `REPO_SPEC_v0.3.md` to fold in the
> Literature Review System (LRS, `design/S14_literature-review-system.md`, founder requests 35,
> 35b–35f) — a new methodology card, five new templates, a new per-project `lit/` directory, new
> CLI/MCP entries, and one field rename (`search_log.yaml`'s `review_mode` → `search_mode`,
> `FOUNDATION_v0.4.md` §7.9) — **plus the mid-run lens-attribution/signature requirements
> (founder requests 38, 38b, 38c, 38d):** every Blackbox Note carries a required `lens_used` block
> (`blackbox_note.schema.json`); the claim card gains `lens_translation.lens_ref` and
> `hypothesis_world.signature` (both required when a lens is used, `claim_card.schema.json`
> v0.5.0); the release gate hard-blocks on `D-LENS-UNCITED`/`D-LENS-UNSIGNED` when either the
> lens's citation+repo or the hypothesis signature is missing. Everything from v0.3 is carried
> forward unchanged except where this document states otherwise. The repo already exists at
> `~/ANSE.ASIA/glosa` (local Forgejo only,
> commit `74ebde8` on `main`, no public remote yet). Renames/consolidations from `design/
> CHAIR_RULING_v1.md` carried forward unchanged: Blackbox Note (A1), one disclaimer catalogue (C2),
> per-project ledgers + merged view (B6), per-project kg + merged view, the 9-genre router with
> `venue_track`/`companion_of` attributes (B1, now also carrying `venue_track: none`, must-fix 8),
> `plugins/glosa/`, `kernel/`, `cli/`.
>
> **Methodology-card renumbering this pass:** the new LRS card takes the number **P13**
> (`methodology/P13_literature_review.md`) — the position that best matches the spine's own S3b/S3c
> placement, between the hypothesis card (P3) and the independent-check card (P6). The existing
> `P13_genre_router.md` is renumbered to **P16** (`methodology/P16_genre_router.md`) to make room;
> its content, its `SKILL.md` pointer, and every citation of it elsewhere in this tree are updated
> to the new filename, nothing else about it changes. This is a filename/number change only, not a
> content or ownership change.
>
> **NOT YET ON DISK, except the bare repo shell.** Every path below beyond the already-created
> `~/ANSE.ASIA/glosa` root is a design-time specification. As of this synthesis pass (2026-09-04),
> nothing in this tree exists as a file or directory in the design repo's own working copy except
> the design/reviews/sources/surveys files already present here — check `git status`/`ls` before
> assuming any path below is real in either repo. TH/EN direction and the remaining 17-item founder
> decision list (`FOUNDATION_v0.4.md` §11) must still be ratified before P-A bootstrap builds the
> rest of this tree for real.
>
> **One-fact-one-home discipline, unchanged from v0.1/v0.2:** a file in `methodology/` states a
> rule in prose. A file in `schema/` states a rule's shape. A file in `methodology/data/` states a
> rule's *content* when machine-read. A file in `kernel/`/`scripts/` enforces a rule. A file in
> `paper/` narrates a rule by citation. A file in `plugins/`/`cli/`/`mcp/` invokes a rule. No file
> may do two of these five jobs for the same rule.

```
glosa/
│
├── README.md                          # L0 thesis. TH-first (rewritten, not translated) then EN.
│                                       #   States "open it and work." Carries D-K-STATE badge.
│                                       #   Owner: founder (content), AI drafts under disclosure.
├── AI_START_HERE.md                   # Read-order + do/don't for any AI session opening this repo
│                                       #   cold.
├── AGENTS.md                          # Reviewer/AI conduct rules; "restate thesis before judging."
│                                       #   Carries the vendor-neutral cross-vendor review gate block
│                                       #   (FOUNDATION §4.3) — identical text to CLAUDE.md/GEMINI.md.
├── CLAUDE.md                          # Same gate block as AGENTS.md, the AI assistant-specific filename.
├── GEMINI.md                          # Same gate block, Gemini-specific filename.
├── llms.txt                           # Machine index for any LLM reading the repo cold.
├── CITATION.cff                       # Founder sole author. AI never in this file's authorship
│                                       #   array (D-AUTHORSHIP). PRESERVE_EXACT pattern from
│                                       #   zero-readout-certifies (FOUNDATION §1.2).
├── .zenodo.json                       # Zenodo deposit metadata; related_identifiers to the direct-
│                                       #   ancestor DOIs, NOW INCLUDING zero-readout-certifies
│                                       #   (FOUNDATION §1.2, chair ruling C7).
├── codemeta.json                      # Kept in lockstep with CITATION.cff (check_version.py).
├── LICENSE                            # CC BY 4.0, WHOLE REPOSITORY, single license (founder
│                                       #   decision, request 33, must-fix 3 — DECIDED this pass).
│                                       #   Supersedes v0.2's MIT-code/CC-BY-prose split:
│                                       #   `LICENSE-TEXT.md` and `LICENSES.md` are DROPPED — there
│                                       #   is now exactly one license file covering every path in
│                                       #   this tree, code included. Founder's own flagged caveat,
│                                       #   carried forward: CC BY on code is legal but unusual — if
│                                       #   a code-specific license is ever wanted, it must be added
│                                       #   later as an explicit dual grant, never silently.
├── CLAIM_BOUNDARY.md                  # L0 — glosa's own claim ceiling about itself.
├── ASSUMPTIONS.md                     # A1.. — repo-level assumptions.
├── NON_CLAIMS.md                      # NC1.. — repo-level non-claims.
├── CHANGELOG.md                       # Append-only; every entry carries a tier label.
├── DECISIONS.md                       # glosa-local mirror of cpg's DECISIONS.yaml lifecycle.
├── GLOSA_K1_K2_LEDGER.md              # K1→K2 conversion ledger (FOUNDATION §7.6). Row 1 is the
│                                       #   repo itself. Renamed from `RWI_K1_K2_LEDGER.md`.
│
├── paper/                             # Narrates methodology/*, never restates.
│   ├── main.md                        #   TH, source of truth.
│   ├── main_en.md                     #   EN, rewritten (not translated) companion.
│   ├── main.tex                       #   Compiles to both arXiv 1-col and 2-col via a class switch.
│   ├── main.bib
│   ├── CLAIM_MATRIX.md                #   Every numbered claim ↔ claim_id; `\claimref{}` resolves
│   │                                  #   here. PRESERVE_EXACT from zero-readout-certifies
│   │                                  #   (FOUNDATION §1.2, chair ruling C7 — now explicitly
│   │                                  #   lineage-tagged, closing COMPLETENESS_CRITIC §2's finding
│   │                                  #   that v0.1 reused this near-verbatim with no tag at all).
│   ├── BLACKBOX_NOTE_APPENDIX.md      #   RENAMED from ORIGIN_DIALOGUE_APPENDIX.md (chair ruling A1)
│   │                                  #   — mandatory (request 28/32). Curated Blackbox Note lines
│   │                                  #   with `became:` links + the relevant cooking-log entries.
│   │                                  #   Release gate FAILS without this file present and
│   │                                  #   non-empty for any paper.
│   ├── LIT_REVIEW_SCAFFOLD.md         #   NEW — the three-question scaffold (request 31d/31e):
│   │                                  #   which problem / by which method / neighbour-by-neighbour
│   │                                  #   same-different-cited table, cites
│   │                                  #   design/S13_neighbour-table.md's content. GAINS a hard
│   │                                  #   line this pass (request 35, FOUNDATION §7.9): this
│   │                                  #   scaffold may not be filled in for any hypothesis whose
│   │                                  #   `litreview_manifest.gate.overall` is not `PASS`/
│   │                                  #   `PASS_WITH_LIMITS` — points at `records/lit/<hypothesis-
│   │                                  #   ref>/litreview_manifest.yaml`, never restates its content.
│   └── thai-tci/                      #   `venue_track: thai_tci` section/format variant for any
│                                      #   of the 9 genres (not the separate rows v0.1's 12-row
│                                      #   table used) — not yet built, FOUNDATION §6.1/§11 item 16.
│
├── methodology/                       # L1 — protocol cards, prose only. One card = one file.
│   ├── P0_lens.md                     #   Readout-not-truth as default reading stance.
│   ├── P1_standpoint.md               #   Declare who speaks, from what base, what's not claimed.
│   ├── P2_intake.md                   #   Two-question gate before any analysis starts.
│   ├── P3_claim_card.md               #   The atomic unit — narrates FOUNDATION §3's schema,
│   │                                  #   INCLUDING the two legal shapes (stub|full, §3.2a).
│   ├── P4_assumption_check.md         #   Contaminated-concept scan (Appendix C) + named assumptions.
│   ├── P5_evidence_challenge.md       #   Bidirectional, global+local evidence search.
│   ├── P6_independent_check.md        #   MIMCG L0–L5 + Independence Ladder I0–I5 + DVP, INCLUDING
│   │                                  #   the bounded I2+I4 exception (chair ruling B4).
│   ├── P7_ai_fill_disclosure.md       #   What AI added, route-level, never silently merged.
│   ├── P8_diagnosis.md                #   Don't trust one instrument; plausible vs. verified language.
│   ├── P9_vet_external_input.md       #   Any outside source is untrusted until read in full.
│   ├── P10_publish_gate.md            #   Adversarial review + leak scan before public-facing.
│   ├── P11_log_and_decision.md        #   Append-only logbook + DECISIONS row; dissent never erased.
│   ├── P12_readiness.md               #   Pre-work readiness report, fail-closed.
│   ├── P13_literature_review.md       #   NEW this pass (request 35, FOUNDATION §7.9) — narrates
│   │                                  #   the Literature Review System (LRS) BY REFERENCE to
│   │                                  #   `design/S14_literature-review-system.md`: six stages
│   │                                  #   (L1-L6), per-hypothesis trigger (35b), dialogue-table
│   │                                  #   conversation form (35c), hypothesis selection (35d), the
│   │                                  #   two coupled manifest gates (35e), stratified selection
│   │                                  #   (35f). Takes the number P13 — see the renumbering note
│   │                                  #   in this document's header.
│   ├── P14_project_advisor.md         #   The third role (FOUNDATION §7.7) — activation trigger,
│   │                                  #   what it reads/writes, SCRAM conditions (specified, Dr,
│   │                                  #   untested per chair ruling D1 — this file must say so).
│   ├── P15_blackbox_note.md           #   NEW — the raw-voice + cooking-log discipline (chair
│   │                                  #   ruling A1/A2's request-32 rename): what goes in, who
│   │                                  #   selects for the appendix, the never-sealed rule. Gains
│   │                                  #   one line this pass: a hypothesis-selection event (P13)
│   │                                  #   is a `cooking:` entry like any other transformation.
│   ├── P16_genre_router.md            #   RENUMBERED this pass from P13 (see this document's
│   │                                  #   header) to make room for P13_literature_review.md.
│   │                                  #   Content otherwise unchanged: narrates FOUNDATION §6's
│   │                                  #   9-genre table + `venue_track`/`companion_of` attributes
│   │                                  #   (chair ruling B1) + §6.3b's decision procedure/
│   │                                  #   MIXED_GENRE tie-break; cites methodology/data/
│   │                                  #   genre_router_table.json. Gains one line this pass: every
│   │                                  #   genre's related-work component names its gate as
│   │                                  #   `litreview_manifest.gate.overall ∈ {PASS,
│   │                                  #   PASS_WITH_LIMITS}` (FOUNDATION §6.4).
│   └── data/                          #   Machine-read rule CONTENT.
│       ├── disclaimer_catalogue.json  #     FOUNDATION §5's ONE master table (chair ruling C2 —
│                                      #     citation-state folded into D-CITATION-UNVERIFIED,
│                                      #     D-INDEPENDENCE-LEVEL split from D-INDEPENDENCE,
│                                      #     D-BLACKBOX-NOTE replaces D-ORIGIN-DIALOGUE).
│       ├── genre_router_table.json    #     FOUNDATION §6.2's 9-row table + venue_track/
│                                      #     companion_of attributes, data form.
│       ├── contaminated_concept_table.json   # Appendix C, machine form.
│       └── advisor_knowledge_base.json       # Distilled decision rules from ai-native-scholarship
│                                      #     v1.0.0, CITED BY NAME+VERSION+DOI (chair ruling B3) —
│                                      #     a citation+distillation, never a republish of
│                                      #     anchor-v10.md.
│
├── schema/                            # L2 — the ONLY place a field name is defined.
│   ├── common.defs.json               #   Shared enums: tier, independence_class (I0-I5, ONE
│                                      #   string ladder everywhere per chair ruling C1), k_state,
│                                      #   bearing, verdict_tier (SIX values, chair ruling C4),
│                                      #   mc_level, mimcg_role, bilingual_text, review_mode (SIX
│                                      #   values incl. INTERNAL_DATA_AUDIT, chair ruling C5),
│                                      #   fetch_status (ONE enum, chair ruling C3), genre (9 ids
│                                      #   + MIXED_GENRE, chair ruling B1), venue_track (now incl. `none`, must-fix 8),
│                                      #   companion_of.
│   ├── claim_card.schema.json         #   FOUNDATION §3.2, the canonical schema — v0.5.0 this pass
│                                      #   (bumped from v0.4.0: adds `litreview_manifest_ref` and
│                                      #   `hypothesis_selection_ref`, both nullable — additive,
│                                      #   request 35/35d; adds `lens_translation.lens_ref`
│                                      #   (REQUIRED, breaking) and `hypothesis_world.signature`
│                                      #   (REQUIRED, breaking, kernel rule 12) — request 38/38b/38d,
│                                      #   FOUNDATION §2.3/§3.2/§3.3). Prior bump to
│                                      #   v0.4.0 added `question_human`/`question_readout`/
│                                      #   `hypothesis_world`, the fixed stub `ai_filled` shape, the
│                                      #   `disclaimers_emitted` object-array shape, and
│                                      #   `provenance_dag`/`silent_lift_check` `status` fields —
│                                      #   breaking changes, must-fixes 5/9/10/12. Also carries
│                                      #   `shape: stub|full` (chair ruling B2), `origin_blackbox_
│                                      #   ref` (replaces origin_r0_ref + origin_dialogue_ref,
│                                      #   chair ruling A1/C8), `venue_track` (now incl. `none`,
│                                      #   must-fix 8), `companion_of`.
│   ├── evidence_relation.schema.json
│   ├── review_report.schema.json      #   `verdict_tier` — SIX values (chair ruling C4).
│   ├── disclaimer.schema.json         #   Shape only; content in methodology/data/. Gains five new
│                                      #   ids this pass: `D-LIT-MODE`, `D-LIT-NOT-OBTAINED`,
│                                      #   `D-LIT-CONCENTRATED` (FOUNDATION §5/§7.9, request 35),
│                                      #   `D-LENS-UNCITED` (request 38c), `D-LENS-UNSIGNED`
│                                      #   (request 38d).
│   ├── intake.schema.json             #   = S1's problem_card.schema.json, one object, one name.
│   ├── readiness.schema.json
│   ├── release_manifest.schema.json
│   ├── citation_card.schema.json      #   `identifier.kind` adds `BLACKBOX_NOTE` (chair ruling C8,
│                                      #   replaces the S8 gap / "DIALOGUE_RECORD"); `independence_
│                                      #   class`; `fetch_status` uses the one enum (chair ruling C3).
│                                      #   LRS (§9's litreview_manifest.schema.json below) is a
│                                      #   CONSUMER of this schema, not a re-designer of it.
│   ├── search_log.schema.json         #   RENAMED FIELD this pass: `review_mode` -> `search_mode`
│                                      #   (FOUNDATION §7.9, resolving the S14 §2.2/§9.4 name
│                                      #   collision against FOUNDATION §7.8's own differently-scoped
│                                      #   `review_mode` verification-route enum, which is unchanged).
│   ├── litreview_manifest.schema.json #   NEW this pass (request 35, FOUNDATION §7.9) — per-hypothesis
│                                      #   frozen ledger shape; the two-gate (`accuracy_gate`/
│                                      #   `diversity_gate`/`overall`) object matching `templates/
│                                      #   knowledge/litreview_manifest.yaml`.
│   ├── source_acquisition_log.schema.json  # NEW this pass — public-safe bridge shape between a
│                                      #   search result and a citation card's `fetch_status`;
│                                      #   enforces the `rl`-boundary leak rule (no local path/Zotero
│                                      #   key/Paperless id ever validates as a legal field value).
│   ├── dialogue_table.schema.json     #   NEW this pass — the conversation-with-the-problem row
│                                      #   shape (source | how it sees the problem | what it
│                                      #   separates | what it assumes | agrees | disagrees | what it
│                                      #   would say against us | citation_card | verified); no
│                                      #   date-order/priority field exists to enforce request 35c.
│   ├── hypothesis_selection.schema.json #  NEW this pass — the human comparison-and-choice object;
│                                      #   `responsible: human` non-delegable, matching claim_card.
│                                      #   Each candidate row carries its own `hypothesis_world.
│                                      #   signature` (request 38d) — a candidate with `lens_ref` set
│                                      #   and an empty signature fails validation before comparison.
│   ├── kg_node.schema.json
│   ├── kg_edge.schema.json
│   ├── equation_registry_row.schema.json
│   ├── blackbox_note.schema.json      #   RENAMED from r0_record.schema.json (chair ruling A1).
│                                      #   REQUIRES `lens_used` this pass (founder requests
│                                      #   38/38b/38c, FOUNDATION §2.3/§7.4): `display` (short-form
│                                      #   string, e.g. "Readout Universe — Yaoharee Lahtee"),
│                                      #   `description`, `author`, `orcid`, `references[]`,
│                                      #   `repo_urls[]` (REQUIRED — the lens's own git repo,
│                                      #   `github.com/morrocwi/readout_universe` and/or
│                                      #   `readout_genesis`), `repo_ref` (commit/tag or date read),
│                                      #   `must_appear_in_document: true` (const — the release-gate
│                                      #   trigger for `D-LENS-UNCITED`, §7.4), `version_or_date_read`,
│                                      #   `what_it_did_here.{lens_in,lens_out}`, `if_other_lens`,
│                                      #   `note` (const "attribution ≠ authority" — never omitted).
│   ├── conversion_plan.schema.json    #   Project Advisor output (FOUNDATION §7.7).
│   ├── route_dependence_matrix.schema.json
│   ├── disagreement_ledger.schema.json #  Per-project instance shape (chair ruling B6).
│   ├── xenon_ledger.schema.json        #  NEW — per-project instance shape (chair ruling B6;
│                                      #   was undeclared as its own schema in v0.1, only narrated
│                                      #   in prose at FOUNDATION §7.8).
│   └── examples/                      #   One valid.json + one invalid.json per schema — CI fixtures.
│
├── templates/                         # Human-fillable instances of the schema shapes.
│   ├── claim_card.yaml (BOTH a stub example and a full example — chair ruling B2) · evidence_
│   │   relation.yaml · assumptions.md · non_claims.md
│   ├── ai_fill_ledger.md · review_report.md · readiness_report.md · logbook.jsonl (seed, empty)
│   ├── paper-outline/                 #   One outline per genre — 9 genres (chair ruling B1) +
│   │                                  #   one `thai-tci-requirements.md` cross-cutting sheet
│   │                                  #   (replaces the three separate Thai-genre outlines v0.1's
│   │                                  #   12-row table implied) + one `companion.md` sheet.
│   └── knowledge/                     #   Already physically built this design round (S8/S10/S12),
│                                      #   PLUS the chair-updated files from prior syntheses AND the
│                                      #   five NEW S14/LRS templates this pass (request 35):
│       ├── citation_card.yaml · search_log.yaml         #   search_log.yaml's `review_mode` field
│                                      #   is RENAMED `search_mode` this pass (FOUNDATION §7.9) —
│                                      #   already renamed on disk.
│       ├── sr_protocol_prisma_lite.md
│       ├── kg_node.yaml · kg_edge.yaml · equation_registry_row.yaml
│       ├── project_skeleton.md · library_spinout_checklist.md
│       ├── neighbour_table.md         #     Chair-updated (renders design/S13_neighbour-table.md's
│                                      #     row format) — already renamed/updated on disk.
│       ├── route_dependence_matrix.yaml · cross_vendor_review_packet.md
│       ├── blackbox_note.yaml         #     RENAMED from r0_record.yaml (chair ruling A1) —
│                                      #     already renamed/updated on disk. FIXED this pass
│                                      #     (FOUNDATION §12): header title corrected to "Blackbox
│                                      #     Note: how this work was made"; the undefined
│                                      #     `D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE` disclaimer id
│                                      #     replaced with the existing `D-STANDPOINT` id.
│       ├── litreview_manifest.yaml    #   NEW this pass (request 35/35e) — per-hypothesis frozen
│                                      #     manifest: every citation card, status, the diversity
│                                      #     roll-up, the stratified selection table, both gates.
│                                      #     Already built on disk (S14 deliverable).
│       ├── source_acquisition_log.yaml #  NEW this pass (request 35) — public-safe bridge between a
│                                      #     search result and a citation card's `fetch_status`;
│                                      #     records the `rl`-boundary honestly, never a local path/
│                                      #     Zotero key/Paperless id. Already built on disk.
│       ├── lit_review_gate_checklist.md #  NEW this pass (request 35) — the literal checklist an
│                                      #     independent reviewer runs before a lit-review section
│                                      #     may be drafted or published. Already built on disk.
│       ├── dialogue_table.md          #   NEW this pass (request 35c) — the "conversation with the
│                                      #     problem" table: source | how it sees the problem | what
│                                      #     it separates | what it assumes | agrees | disagrees |
│                                      #     what it would say against us | citation_card | verified.
│                                      #     Replaces a chronological survey as the default lit-review
│                                      #     output; date is metadata only, never sets row order.
│                                      #     Already built on disk.
│       ├── hypothesis_selection.yaml  #   NEW this pass (request 35d) — the human's comparison and
│                                      #     choice among n candidate hypotheses after their n LRS
│                                      #     runs; `responsible: human`, non-delegable. Already built
│                                      #     on disk.
│       ├── conversion_plan.yaml · advisor_prompt_packet.md
│       └── dialogue_card.yaml         #   Curated origin-dialogue instance template — still not
│                                      #   yet built (flagged open, FOUNDATION §12); a Blackbox
│                                      #   Note line with `kind: reply` covers most of the same
│                                      #   ground now, but a dedicated dialogue_card for a *paired*
│                                      #   human-AI exchange record is not yet designed as distinct
│                                      #   from a Blackbox Note line — open question, not resolved
│                                      #   by this synthesis. **Not to be confused with
│                                      #   `dialogue_table.md` above** — different artifact, different
│                                      #   purpose (a per-hypothesis source table vs. a paired
│                                      #   human-AI exchange record).
│
├── records/                           # glosa's OWN S1–S3 pipeline artifacts (self-application
│                                      #   worked examples), PER PROJECT (chair ruling B6 pattern).
│   ├── problems/<id>.yaml             #   Problem Cards (S1).
│   ├── sources/<id>.yaml              #   Source Cards (S2).
│   ├── observations/<id>.yaml         #   Observation Cards (S2).
│   ├── claims/<id>.yaml               #   Claim Cards (both shapes, §3.2a).
│   ├── blackbox/<id>.yaml             #   NEW — Blackbox Note instances (chair ruling A1), one per
│                                      #   project, per `blackbox_note.schema.json`.
│   ├── lit/<hypothesis-ref>/          #   NEW this pass (request 35, FOUNDATION §7.9) — ONE
│                                      #   subdirectory per lens-out hypothesis (never merged across
│                                      #   hypotheses, per 35b), holding that hypothesis's own LRS
│                                      #   run:
│   │   ├── search_log.yaml            #     Frozen search episode object (S8, `search_mode` field).
│   │   ├── source_acquisition_log/<id>.yaml   # One row per acquisition attempt (§L3).
│   │   ├── dialogue_table.md          #     This hypothesis's conversation-with-the-problem table.
│   │   └── litreview_manifest.yaml    #     Frozen manifest; gate.overall gates S4/S5 for this
│                                      #     hypothesis (FOUNDATION §7.9).
│   ├── hypothesis_selection/<id>.yaml #   NEW this pass (request 35d) — ONE per problem (compares
│                                      #   the n `lit/<hypothesis-ref>/` runs above); `decided_by` a
│                                      #   human, non-delegable; cross-links every `parked` candidate
│                                      #   rather than deleting it.
│   └── logbook.jsonl                  #   Append-only; every card write is one line here.
│
├── kg/                                 # Repo-scope MERGED VIEW ONLY (chair ruling B6 — the
│                                      #   canonical per-project home is now `<project>/kg/`,
│                                      #   this top-level directory is `glosa kg merge`'s OUTPUT,
│                                      #   never hand-edited).
│   ├── nodes.jsonl
│   └── edges.jsonl                     #   Generated FROM the per-project cards (`glosa kg merge`) —
│                                      #   never a hand-maintained second source of truth.
│
├── ledgers/                            # NEW top-level directory (chair ruling B6) — the repo-wide
│   │                                  #   MERGED VIEW of every project's Disagreement and Xenon
│   │                                  #   ledgers, output of `glosa ledger merge`, never hand-edited.
│   ├── DISAGREEMENT_LEDGER.md          #   Merged view; canonical rows live per-project.
│   └── XENON_LEDGER.md                 #   Merged view; canonical rows live per-project. Replaces
│                                      #   v0.1's single repo-root XENON_LEDGER.md, which is now
│                                      #   this merged output rather than the source of record.
│
├── cases/                             # Worked examples, PUB sources only, license-checked per case.
│   ├── worked-example-cat.md          #   Request 26's "ทำไมแมวเยี่ยวไม่เป็นที่" round-trip demo.
│   ├── re-t-phe.md · seth-moca.md · rrhm-open-lab.md · islamic-archive-th.md · birca.md
│   └── (private-repo lessons appear ONLY as anonymized method narratives — never linked, named)
│   # Each substantial case follows templates/knowledge/project_skeleton.md internally (its own
│   # claims/, sources/, blackbox/, kg/, ledgers, paper/, reviews/) — "one problem = one project."
│
├── incidents/                          # Incident library — "why this rule exists," append-only.
│   ├── INDEX.md                        #   Table: incident → protocol card(s)/gate(s) it justifies.
│   └── 2026-07-24_curl-vs-browser.md · 2026-08-01_check_docs-no-baseline.md ·
│       2026-08-08_skillme-rm-rf.md · 2026-08-03_readout-universe-license-leak.md ·
│       2026-06-30_rag-overclaim.md · 2026-08-09_hosting-vendor-ip-ban.md · …
│
├── lineage/
│   ├── PRIOR_WORK.md                   #   From sources/zenodo_lahtee_records.json — 180 records.
│                                      #   Chair ruling D5: the 169 non-ancestor records are LISTED
│                                      #   here, not interpreted; only the direct ancestors named
│                                      #   in FOUNDATION §1.2 (now including zero-readout-certifies,
│                                      #   chair ruling C7) get an anchor-preservation row.
│   └── RELATION_TO_STANDALONE_SCHOLAR.md   # The master ledger, FOUNDATION §1.3, moved here
│                                      #   verbatim once ratified. Also carries the NEW
│                                      #   zero-readout-certifies and label_inflation_guard.py
│                                      #   rows (chair ruling C7).
│
├── reviews/                            # Dated adversarial review reports = MIMCG evidence bundle.
│   ├── YYYY-MM-DD_<stage>_<reviewer-route>.md
│   └── routes/<claim_id>/<route_id>/  #   Cross-vendor DVP file-based handoff:
│       ├── PACKET.md                  #     vendor-neutral prompt packet, no orchestration needed.
│       └── review_report.yaml         #     written back by whichever agent picked up the packet.
│                                      #     `verdict_tier` field uses the SIX-value enum (C4).
│
├── .claude-plugin/
│   └── marketplace.json                #   source clones the WHOLE repo, no path: into a subtree.
├── plugins/
│   └── glosa/                          #   Canonical name — repo name `glosa` (request 34)
│       │                              #   propagates to the plugin directory this pass.
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── glosa-intake/SKILL.md            → cites methodology/P2_intake.md
│           ├── glosa-claim-card/SKILL.md        → cites methodology/P3_claim_card.md
│           ├── glosa-evidence-challenge/SKILL.md → cites methodology/P5_evidence_challenge.md
│           ├── glosa-independent-check/SKILL.md  → cites methodology/P6_independent_check.md
│           ├── glosa-disclaimer-system/SKILL.md  → cites methodology/data/disclaimer_catalogue.json
│           ├── glosa-publish-gate/SKILL.md       → cites methodology/P10_publish_gate.md
│           ├── glosa-literature-review/SKILL.md  → cites methodology/P13_literature_review.md (NEW
│                                      #   this pass, request 35 — six-stage LRS pipeline,
│                                      #   per-hypothesis gate, dialogue-table form)
│           ├── glosa-genre-router/SKILL.md       → cites methodology/P16_genre_router.md (RENUMBERED
│                                      #   this pass from P13 — see this document's header note)
│           ├── glosa-project-advisor/SKILL.md    → cites methodology/P14_project_advisor.md
│           ├── glosa-cite-check/SKILL.md         → cites methodology/P9_vet_external_input.md
│           │                                  #   + FOUNDATION §7.8 citation firewall
│           └── glosa-blackbox-note/SKILL.md      → cites methodology/P15_blackbox_note.md (NEW,
│                                      #   chair ruling A1 — v0.1 had no dedicated skill for the
│                                      #   raw-voice discipline; it was implicit inside intake/
│                                      #   claim-card. Given request 32's mandatory-appendix rule,
│                                      #   this is now split out.)
│
├── kernel/                             # L3 core — pure, stdlib-only.
│   ├── glosa_kernel.py         #   validate_*, compute_disclaimers, route_genre,
│                                      #   gate_release, defeater_route, advise, kg_validate,
│                                      #   kg_merge, ledger_merge (NEW — chair ruling B6),
│                                      #   cite_check, schema_summary, demo_run, self_test,
│                                      #   lit_manifest_gate / lit_diversity_audit / lit_select_check
│                                      #   (NEW this pass, request 35, FOUNDATION §7.9 — computes
│                                      #   `litreview_manifest.gate.{accuracy_gate,diversity_gate,
│                                      #   overall}`, never a second hand-typed verdict).
│   └── tests/
│       ├── test_schemas_valid.py · test_validate_claim_card.py · test_gate_release.py ·
│       │   test_stub_cannot_advance.py (NEW — chair ruling B2's kernel rule 10, renumbered this pass) ·
│       │   test_bounded_i2i4_exception_expiry.py (NEW — chair ruling B4) ·
│       │   test_lit_manifest_gate.py (NEW this pass, request 35 — accuracy/diversity gate math,
│       │     including the small-N floor, the stakes floor, and the PASS_WITH_LIMITS diversity
│       │     downgrade path) ·
│       │   test_lit_secondary_citation_ban.py (NEW this pass — FC-S14-1) · …
│       └── fixtures/
│           ├── pass_cycle/
│           ├── fail_same_model_review/
│           ├── fail_no_independent_check/
│           ├── fail_missing_disclaimer/
│           ├── fail_th_coqc_no_witness/
│           ├── fail_stub_cited_publicly/   # NEW — chair ruling B2
│           └── fail_lit_manifest_not_verified/   # NEW this pass, request 35 — the cat-question
│                                      #   worked example's own honest FAIL (S14 §10) becomes the
│                                      #   seed for this fixture.
│
├── cli/
│   └── glosa                             #   Console-script entry point calling kernel.main.
│                                      #   Adds `glosa ledger merge` alongside `glosa kg validate|
│                                      #   merge|render` (chair ruling B6), PLUS this pass (request
│                                      #   35, FOUNDATION §7.9): `glosa lit new|search|freeze|
│                                      #   acquire|extract|cite-check|table|select|manifest`.
│                                      #   `glosa lit select` has no `--auto` flag (requires a human
│                                      #   `decided_by` before writing a non-empty
│                                      #   `selection.chosen`).
│
├── mcp/
│   ├── glosa_mcp_server.py               #   One tool per kernel function, incl. `glosa_ledger_merge`,
│                                      #   PLUS this pass (request 35): `lit_new`, `lit_search`,
│                                      #   `lit_freeze`, `lit_acquire`, `lit_extract`,
│                                      #   `lit_cite_check`, `lit_table`, `lit_select`,
│                                      #   `lit_manifest` — vendor-neutral per request 13, callable
│                                      #   identically from the AI coding tool, Codex, Gemini CLI, or a
│                                      #   local model via the same PACKET.md pattern §4.3 uses.
│   └── TOOLS.md                        #   Human-readable tool list + capability-gating explanation.
│                                      #   Gains the nine `lit_*` tools' capability notes this pass.
│
├── scripts/                            # Repo-maintenance ONLY.
│   ├── check_repo.sh                   #   Required files present; JSON metadata parses; no
│                                      #   build artifacts committed; single-LICENSE presence check
│                                      #   (must-fix 3 — no LICENSES.md glob-map needed once the
│                                      #   whole repo is one CC BY 4.0 license).
│                                      #   PRESERVE_EXACT from zero-readout-certifies (chair
│                                      #   ruling C7 — now lineage-tagged).
│   ├── check_version.py                #   git tag == CITATION.cff == .zenodo.json == codemeta.json
│                                      #   == plugin.json, all equal. Same lineage tag as above.
│   ├── check_leak.sh                   #   Local usernames/paths/IPs/session-ID shapes/private-repo
│                                      #   path fragments.
│   ├── check_skill_pointers.py         #   Every SKILL.md → methodology/ path resolves.
│   └── render_disclaimers.py           #   Regenerates both templates' disclaimers.tex from
│                                      #   methodology/data/disclaimer_catalogue.json. **Priority
│                                      #   note (COMPLETENESS_CRITIC §4): the two ALREADY-COMPILED
│                                      #   `design/templates/arxiv-{onecol,twocol}/disclaimers.tex`
│                                      #   files still say "D12 — Novelty discipline," violating
│                                      #   founder ruling 31 — this script's first real run must
│                                      #   regenerate and recompile both, not just future ones.**
│
└── .github/
    └── workflows/ci.yml                #   Mechanical checkers only: repo-consistency, version,
                                        #   leak scan, claim-card + citation-card schema validation
                                        #   (incl. shape:stub|full and origin_blackbox_ref),
                                        #   overclaim/tier heuristic scan (incl. a grep for "novel/
                                        #   novelty/first/unprecedented/prior art" per founder
                                        #   ruling 31 — NEW check this pass), license coverage,
                                        #   plugin-manifest validation, kernel test suite, MCP
                                        #   tools/list+call smoke test, PLUS this pass (request 35):
                                        #   litreview_manifest/source_acquisition_log/dialogue_table/
                                        #   hypothesis_selection schema validation and a
                                        #   `no local rl-shelf path/Zotero key/Paperless id` leak
                                        #   check scoped specifically to every `source_acquisition_
                                        #   log.yaml` row. Runs on every PR + tag push.
```

## Resolved-from table — every deviation from `REPO_SPEC_v0.3.md`, and why

| Deviation | v0.3's tree | This spec (v0.4) | Resolved per |
|---|---|---|---|
| `methodology/P13_literature_review.md` added; existing `P13_genre_router.md` → `P16_genre_router.md` | `P13_genre_router.md` only | New `P13_literature_review.md` (LRS, cited by reference to S14); genre router renumbered to `P16` to make room | Request 35, FOUNDATION §7.9; renumbering choice stated in this document's header |
| Five new LRS templates added under `templates/knowledge/` | Not present | `litreview_manifest.yaml`, `source_acquisition_log.yaml`, `lit_review_gate_checklist.md`, `dialogue_table.md`, `hypothesis_selection.yaml` (all already built on disk as S14 deliverables) | Request 35/35c/35d/35e/35f |
| `records/lit/<hypothesis-ref>/` and `records/hypothesis_selection/<id>.yaml` added | Not present | New per-project subdirectories: one LRS run per hypothesis, never merged (35b); one selection file per problem comparing all its hypotheses (35d) | Request 35b/35d |
| `search_log.yaml`'s `review_mode` field → `search_mode` | Shared field name with FOUNDATION §7.8's differently-scoped `review_mode` verification-route enum | Renamed to end the collision; §7.8's `review_mode` unchanged | FOUNDATION_v0.4.md §7.9, resolving S14 §2.2/§9.4/§12 item 1 (a vocabulary decision, not a resolution of S14 §12's still-open items 2–5) |
| `claim_card.schema.json` gains `litreview_manifest_ref`/`hypothesis_selection_ref`; schema_version 0.4.0 → 0.5.0 (additive) | Two fields absent | Both present, nullable | Request 35/35d, FOUNDATION §7.9 |
| CLI/MCP gain `glosa lit new\|search\|freeze\|acquire\|extract\|cite-check\|table\|select\|manifest` + nine `lit_*` MCP tools | Not present | Present, vendor-neutral per request 13 | Request 35, S14 §9 |
| `disclaimer_catalogue.json` gains `D-LIT-MODE`, `D-LIT-NOT-OBTAINED`, `D-LIT-CONCENTRATED` | Not present | Three new ids | Request 35/35e, FOUNDATION §5/§7.9 |
| `design/templates/knowledge/blackbox_note.yaml` header + `disclaimers:` list fixed | Header named the pre-rename appendix title; `disclaimers:` cited a non-existent id | Header corrected; non-existent id replaced with the existing `D-STANDPOINT` id | FOUNDATION_v0.4.md §12 (closes the two defects v0.3 §12 flagged but did not fix) |
| `blackbox_note.yaml` gains a REQUIRED `lens_used` block | Not present | `display`, `description`, `author`, `orcid`, `references[]`, `repo_urls[]`, `repo_ref`, `must_appear_in_document`, `version_or_date_read`, `what_it_did_here`, `if_other_lens`, `note` | Founder requests 38/38b/38c |
| `claim_card.schema.json` gains `lens_translation.lens_ref` and `hypothesis_world.signature` (both required when a lens is used) | Neither field present | Both present; kernel rule 12 hard-fails an unsigned lens-derived hypothesis | Founder requests 38/38d, FOUNDATION §2.3/§3.2/§3.3 |
| `disclaimer_catalogue.json` gains `D-LENS-UNCITED`, `D-LENS-UNSIGNED` | Not present | Two new ids, both hard release-gate blocks | Founder requests 38c/38d |
| Release gate (§7.4/§6.4) gains the lens-citation + hypothesis-signature checks, plus the reflexive "glosa cites glosa" rule | Not present | New hard-block checks | Founder request 38c |

## Deviations carried forward from `REPO_SPEC_v0.2.md` (v0.3's own table, unchanged)

| Deviation | v0.2's tree | v0.3's spec | Resolved per |
|---|---|---|---|
| Repo name `rigour-without-infrastructure` → `glosa`; tree root, plugin dir, CLI, kernel module, MCP server all renamed | Root `rigour-without-infrastructure/`, `plugins/rigour-without-infrastructure/`, CLI `rwi`, `kernel/rwi_protocol_kernel.py`, `mcp/rwi_mcp_server.py` | Root `glosa/`, `plugins/glosa/`, CLI `glosa`, `kernel/glosa_kernel.py`, `mcp/glosa_mcp_server.py` (skill ids `glosa-*` throughout `plugins/glosa/skills/`) | Founder decision, request 34 — the methodology keeps its full name, Rigour Without Infrastructure; only the repo/tooling identifier changes |
| `LICENSE` (MIT) + `LICENSE-TEXT.md` (CC BY 4.0) + `LICENSES.md` (glob map) → single `LICENSE` (CC BY 4.0, whole repo) | Split license, `LICENSES.md` path-glob map, `check_repo.sh` walking it | One `LICENSE` file, no split, `check_repo.sh` checks only for its presence | Founder decision, request 33, must-fix 3 |
| `RWI_K1_K2_LEDGER.md` → `GLOSA_K1_K2_LEDGER.md` | Named for the old repo id | Renamed to match | Follows from the repo rename, request 34 |
| `common.defs.json`'s `venue_track` enum gains `none` | Two values (`international`, `thai_tci`) | Three values, `none` legal for K0 work never headed to a venue | Must-fix 8 |
| `kernel/tests/` gains `test_bounded_i2i4_exception_expiry.py`'s sibling coverage for the new K1-floor rule; `test_stub_cannot_advance.py` cites kernel rule 10, not 9 | Rule numbered 9 in `FOUNDATION_v0.2.md` §3.3 | Renumbered to rule 10 in `FOUNDATION_v0.3.md` §3.3 to make room for the new K1-floor rule 9 | Chair ruling item 1 (must-fix 1) |
| `r0_record.{yaml,schema.json}` → `blackbox_note.{yaml,schema.json}` | `templates/knowledge/r0_record.yaml`, `schema/r0_record.schema.json` | `templates/knowledge/blackbox_note.yaml` (already renamed on disk), `schema/blackbox_note.schema.json` | Chair ruling A1 (founder request 32) |
| `paper/ORIGIN_DIALOGUE_APPENDIX.md` → `paper/BLACKBOX_NOTE_APPENDIX.md` | Named `ORIGIN_DIALOGUE_APPENDIX.md` | Renamed; same mandatory-gate role | Chair ruling A1 |
| `methodology/P15_blackbox_note.md` added | Not present (P0–P14 only) | New card, split out from the intake/claim-card cards it was implicit in | Request 32's mandatory-appendix rule now needs its own protocol card; `plugins/.../glosa-blackbox-note/SKILL.md` added to match |
| `records/blackbox/<id>.yaml` added | Not in v0.1's `records/` tree | New subdirectory, per project | Chair ruling A1 + B6 pattern |
| `kg/` becomes a MERGED-VIEW-ONLY directory; canonical home moves to `<project>/kg/` | v0.1: `kg/{nodes,edges}.jsonl` at repo root "+1 per project," ambiguous about which was canonical | Explicit: per-project is canonical, repo-root is `glosa kg merge`'s generated output only | Chair ruling B6 — same pattern extended from the kg (already partially per-project in v0.1) to the ledgers, made explicit for both |
| `ledgers/` top-level directory added; `XENON_LEDGER.md`/`DISAGREEMENT_LEDGER.md` move from repo-root single files to per-project canonical + repo-root merged view | v0.1: single repo-root `XENON_LEDGER.md`; `DISAGREEMENT_LEDGER.md` not in the tree at all (only named in FOUNDATION prose) | `ledgers/DISAGREEMENT_LEDGER.md` and `ledgers/XENON_LEDGER.md` as merged views; canonical rows live in each project | Chair ruling B6, resolving FOUNDATION_v0.1 §10 dispute 6 |
| `schema/xenon_ledger.schema.json` added | Not present — Xenon Ledger was narrated only in FOUNDATION §7.8 prose, no schema file | New schema file, matching the per-project instance shape | Chair ruling B6 makes the ledger a real per-project artifact needing its own schema, not only a prose row-format |
| `paper/LIT_REVIEW_SCAFFOLD.md` added | Not present | New file, cites `design/S13_neighbour-table.md`'s three-question format | Founder ruling, request 31d/31e |
| Genre outline count: 12 → 9 + 2 cross-cutting sheets | `templates/paper-outline/` had one outline per each of 12 genre rows | 9 genre outlines + `thai-tci-requirements.md` + `companion.md` | Chair ruling B1 |
| `.github/workflows/ci.yml` novelty-language grep added | Not present as a named CI check | New check: grep for "novel/novelty/first/unprecedented/prior art" across `paper/`, `methodology/`, `README.md` | Founder ruling 31, closing the gap `reviews/COMPLETENESS_CRITIC.md` §4 found (compiled `disclaimers.tex` still carrying "D12 Novelty discipline" with no automated catch) |
| `scripts/render_disclaimers.py` priority note added | Present, undated priority | Explicit priority note: its first real run must fix the two already-stale compiled `disclaimers.tex` files, not just prevent future drift | `reviews/COMPLETENESS_CRITIC.md` §4 |
| `schema/common.defs.json` enum list updated | Listed tier/independence_class/k_state/bearing/verdict/mc_level/mimcg_role/bilingual_text/genre(12) | Same list, with `verdict_tier` now stated as six values, `review_mode` (six, incl. `INTERNAL_DATA_AUDIT`) and `fetch_status` (one enum) added explicitly, `genre` now 9 + `venue_track` + `companion_of` | Chair ruling C1/C3/C4/C5/B1 |

## Not yet on disk (repeated for emphasis)

Two distinct working trees are in play, and this pass keeps them explicitly separate:

1. **This design round's own working tree**, `research/rigour-without-infrastructure/` inside
   `cpg_research_journal` — this directory keeps its original name; it is the design workspace, not
   the target repo, and is never renamed to `glosa`. `git status`/`ls -la` here as of this
   synthesis pass shows only `design/`, `reviews/`, `sources/`, `surveys/`, and this repo's own
   root `HANDOFF_*`/`PLAN_*` files.
2. **The target repo, `~/ANSE.ASIA/glosa`** — already created (founder decision, request 34; local
   Forgejo commit `74ebde8` on `main`, no public remote yet), but still only a bare shell. Every
   path in the tree above — including every renamed/added path — remains a design-time
   specification only until P-A bootstrap builds it for real: no `paper/`, `methodology/`,
   `schema/`, `kernel/`, `cli/`, `mcp/`, `records/`, `kg/`, `ledgers/`, `cases/`, `incidents/`,
   `lineage/`, `plugins/`, or `scripts/` directory exists there yet.

Founder ratification of the remaining 17-item open-decision list and TH/EN direction
(`FOUNDATION_v0.4.md` §11) must happen before P-A bootstrap builds the rest of `~/ANSE.ASIA/glosa`
for real. Repo name (item 1) and license (item 3) are no longer open — both are DECIDED (v0.3).
The six open S14 §12 items (review_mode/search_mode collision — DECIDED this pass, §7.9;
concentration threshold; spot-check n%; the research-library export adapter; the venue-quality
index source; genre-DAG rewrite scope) are additional open items this v0.4 does not resolve beyond
the one vocabulary decision it makes.

## Open (not resolved by this spec — see `FOUNDATION_v0.4.md` §10/§11, and `design/S14_literature-review-system.md` §12 items 2-6)

- The exact section/format content of `venue_track: thai_tci` (which sections it adds to each of
  the 9 genres, beyond the general requirement list in `FOUNDATION_v0.3.md` §6.2) is not yet
  written — stays generic `Dr` until a Thai TCI journal is named (`FOUNDATION_v0.3.md` §11,
  unchanged from v0.1/v0.2).
- Whether `templates/knowledge/dialogue_card.yaml` is still a distinct artifact from a Blackbox
  Note line with `kind: reply`, or whether it should be retired in favour of the Blackbox Note
  schema alone, is not resolved in this pass (see the `templates/knowledge/` tree note above).
- `ai-native-scholarship` stays cited-as-dependency only (chair ruling B3); this tree assumes no
  `plugins/ai-native-scholarship/` directory is ever created, but B3 remains a founder veto point.
