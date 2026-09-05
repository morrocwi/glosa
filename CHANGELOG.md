# CHANGELOG
## 0.4.0 — in preparation
- Session-architecture review (`design/SESSION_ARCH_v0.4_SPEC.md`, both parts, 25 proposals
  scored under founder ruling BBL-2026-09-05-119: raise the work, never lower a claim to pass —
  count corrected from 24 to 25, `SA-5` restored under gate rule 10, see `design/
  FOUNDATION_v0.7_PATCH.md` §0/§11.8): 13 `build_now`, 8 `with_revision` (exact fix stated), 4
  `still_open` (raise-path stated, no softened claim). **`design/FOUNDATION_v0.7_PATCH.md` states
  the exact diff for every node; what is actually applied to `FOUNDATION_v0.6.md`/schema/kernel
  differs by node, not uniformly "not yet applied"** (MUST fix, ARCH_REVIEW_v0.7.json source-
  fidelity — a prior draft of this line claimed the whole diff unapplied, contradicting this same
  entry's own "Built this pass" section below): `session.boundary-blackbox-note` (SA-1)'s core
  schema fields, `schema.blackbox-question-trace`, `lrs.dialogue-table-claim-type-column`,
  `lrs.defeater-defeated-status-field`, `hu.mastery-gate-wired` (HU-1), and now `schema.entry-
  anchor-full-h0` (HU-2)'s full `intake.entry_anchor` object are already shipped to
  schema/kernel/`FOUNDATION_v0.6.md` (see "Built this pass" below and `FOUNDATION_v0.7_PATCH.md`
  §1/§5/§6, §5 now marked `applied this pass`); the `chi_recip` CLI wiring and every
  `with_revision`/`still_open` node's own stated fix remain genuinely not-yet-applied, per
  `FOUNDATION_v0.7_PATCH.md`'s own per-section status.
- New protocol cards: `methodology/P17_human_mastery_gate.md` (generalizes the ten-question
  live unaided-defense checklist past the arXiv-paper genre, wires it to a new publish-gate R8 —
  HU-1); `methodology/P18_session_architecture.md` (the Session object as a logical join across
  Blackbox Note + `hypothesis_selection.yaml` + Problem Card + `kg_edge.yaml`, one-fact-one-home;
  no fifth `session.yaml` file created). Both disclose a P-number collision with a concurrent
  task rather than silently reconciling it — see `methodology/README.md`.
- `methodology/P01_standpoint.md`: the AI completeness-prompting boundary (HU-5) is now a bounded,
  closed five-item list, replacing the earlier open-ended `(e.g. ...)` example — an AI prompt
  outside the list must be logged `ai_filled.prompt_source: freeform`, extending `NC-58`
  (AIContribution≠EpistemicResponsibility) from AI-*filled answers* to AI-*posed prompts*.
- New non-collapse row specified (not yet in `methodology/data/non_collapse_table.json`):
  **`NC-77` Retention≠Direction** — persistence of a chosen hypothesis across ≥2 sessions is never
  by itself evidence of expansion vs. tunnel; only a linked independent check may set the sign.
  Reservation of the id in the internal command-center's DECISIONS ledger (private) is a pending founder act
  (`design/FOUNDATION_v0.7_PATCH.md` §13, §15.3).
- **Pending founder decision (recommended text specified, not ratified):** 10 decisions carried
  forward from `design/SESSION_ARCH_v0.4_SPEC.md` §7 and its Part-2 additions — see
  `design/FOUNDATION_v0.7_PATCH.md` §15. None is defaulted silently; the session-object
  one-fact-one-home layout, the `SA-1`/duplicate-proposal merge, the `NC-77` reservation, and
  `SA-3`/HU-2 retroactivity (recommended default: forward-only) are the most load-bearing.
- **Built this pass (remaining `build_now` nodes from `design/SESSION_ARCH_v0.4_SPEC.md`):**
  - `schema.blackbox-question-trace`: `schema/blackbox_note.schema.json`'s additive/optional
    top-level `question_trace[]` (`{n, ts, question_text, derived_from_line, note}`) plus a
    mechanical coverage check, `tools/blackbox_log.py`'s `question_trace_coverage()` /
    `blackbox_log.py check-note <path>` (every `lines[].kind==question` line must have a matching
    `question_trace[].n` entry, or an explicit `derived_from_line: null`).
  - `lrs.dialogue-table-claim-type-column`: `schema/dialogue_table_row.schema.json` gains additive/
    optional `defeater_class` (five-way `phenomenological|constitutive|structural_formal|
    diagnostic|empirical`) + `legitimate_defeater`, matching the already-shipped
    `templates/knowledge/dialogue_table.md` columns and `cli/glosa`'s `_dialogue_row_incomplete`
    lint (`rows_incomplete_defeater`) — deliberately schema-optional, not `required` (the template
    documents the stance-without-defeater-columns check as a lint, not a hard gate).
  - `lrs.defeater-defeated-status-field`: kernel rule31 adds a `defeater_status`
    (`untested|tested_survived|tested_defeated`) WARNING — DERIVED from `provenance_dag.
    defeater_log[]`, never a duplicate schema field (the field's real fix, `defeater_log`
    `required: [node, date, outcome]` + `outcome` enum, already shipped) — fires once a card's
    `status` is Pending Review or beyond with `defeater_log` empty.
  - `hu.mastery-gate-wired` (HU-1): new `schema/human_mastery_gate.schema.json` (`gate_status`
    `PASS|PASS_WITH_NAMED_GAPS|NOT_READY`, the ten answer fields from
    `templates/paper/arxiv-twocol/main.tex:375-378`, `named_gaps` required on
    `PASS_WITH_NAMED_GAPS`, any `ai_filled` disclosure forcing `NOT_READY`) +
    `kernel.validate_human_mastery_gate`/`mastery_gate_r8_status`; `methodology/
    P10_publish_gate.md` gains R8; `release_manifest.schema.json`'s additive
    `human_mastery_gate_ref` (absence is a `gate_release` WARNING `NO_MASTERY_GATE_LINKED`, never
    a hard fail — pending founder ratification); `design/FOUNDATION_v0.6.md` §7.5's broken
    "Unchanged from v0.1 §7.5" pointer fixed to cite `methodology/P17_human_mastery_gate.md`.
  - `schema.entry-anchor-full-h0` (HU-2): `schema/problem_card.schema.json`'s `intake` object
    gains the full `entry_anchor: {unresolved, existing_evidence, change_condition,
    verification_intent, resistance_route}` object (all optional, human-authored, never
    AI-backfilled); `resistance_route` is now the single home for the R* fact (one-fact-one-home)
    — the sibling flat `intake.precommitted_resistance_route` field is DEPRECATED (kept read-only
    for already-scaffolded instances; kernel's `_precommit_route_flag` reads `entry_anchor.
    resistance_route` first, falling back to the deprecated path).
  - **SA-1 field-location fix (MUST, ARCH_REVIEW_v0.7.json spec-code-fidelity/one-fact-one-home/
    fail-closed-and-controls/founder-invariants):** `glosa session open|close` (`cli/glosa`'s
    `scaffold_blackbox_note_session`/`cmd_session_open`/`cmd_session_close`) and
    `templates/knowledge/blackbox_note.yaml` previously nested `session_id`/`session_boundary`/
    `entry_anchor`/`retention_note` under a second-level `session:` wrapper key, while
    `schema/blackbox_note.schema.json` and `kernel/glosa_kernel.py`'s `check_session_boundary_
    reset` read them at the TOP level — meaning every note the shipped CLI produced was silently
    invisible to SA-1's own cross-file reset-enforcement mechanism. Fixed: all four artifacts now
    agree on the flat, top-level shape; `tests/test_install.py` updated to match, plus a new
    round-trip regression test (`test_note_produced_by_session_open_is_actually_seen_by_kernel_
    check`) that feeds a real `glosa session open`-produced note straight into
    `check_session_boundary_reset` and asserts it actually fires on a forced violation.
  - **`ai_state_at_boundary` literal fix (MUST, ARCH_REVIEW_v0.7.json founder-invariants/source-
    fidelity):** `scaffold_blackbox_note_session` previously wrote `"carried"` when a
    `carried_from_ref` was given, contradicting the schema enum (`["reset"]` only) and the cited
    architectural-scope definition (an unconditional AI-state reset at every boundary,
    `sources/notes/EPISTEMIC_FUSION_v7.1.txt:331`). Fixed: `ai_state_at_boundary` is now ALWAYS the
    literal `"reset"`; `carried_from_ref` is recorded solely as separate provenance on
    `session_boundary.human_retained_residue_ref` — never conflated with the AI's own state.
  - Verified (no change needed): `NC-77` (`methodology/data/non_collapse_table.json`),
    `D-RETENTION-DIRECTION`, `D-NO-PRECOMMIT-ROUTE` (`methodology/data/disclaimer_catalogue.json`)
    each exist exactly once, no duplicates anywhere in the repo.
  - **Correction to this file's own prior entry:** `session_id`/`session_boundary`/`entry_anchor`
    (R* conjunct only) on `schema/blackbox_note.schema.json`, `retained_direction` on
    `schema/hypothesis_selection.schema.json`, `session_id` on `schema/kg_edge.schema.json`, and
    the `chi_recip_diagnostic` kernel function were already shipped before this pass (confirmed by
    direct read) — this file's prior "Not yet built this pass" line named them in error. **Still
    genuinely not built this pass** (outside this task's ownership): a `chi_recip` **CLI** command
    wiring the existing kernel function into `cli/glosa` (the function itself is not new);
    `candidate_set_deltas[]` on `hypothesis_selection.yaml` (no build_path was ever assigned to it
    — see `schema/hypothesis_selection.schema.json`'s own `$comment`, added this pass as a rule-10
    fix, ARCH_REVIEW_v0.7.json spec-code-fidelity).
## 0.3.0 — 2026-09-05
- Published: repository DOI 10.5281/zenodo.22310837 (concept 10.5281/zenodo.22301059); GitHub tag v0.3.0.
- Publish gate v3 (7 dimensions, skeptic-verified): 17 upheld BLOCKs fixed before release (see reviews/PUBLISH_GATE_v1_public.md); 6 DAG nodes remain pending founder decision, marked in FOUNDATION v0.6.
- FOUNDATION_v0.6.md / REPO_SPEC_v0.6.md: assembled from FOUNDATION_v0.5.md/REPO_SPEC_v0.5.md +
  every READY section of `design/FOUNDATION_v0.6_PATCH.md`/`design/REPO_SPEC_v0.6_PATCH.md`.
  `design/CURRENT_SPEC.txt` now names this pair. Design-docs-only pass — no schema/kernel/template
  file this document describes was itself edited by the FOUNDATION/REPO_SPEC merge (templates
  updated separately, see below).
- **Shipped without a founder gate (kernel-closure rules, closing named K4 sim-confirmed defect-
  detection gaps):** rule 26 composite-quote detector, rule 27 hidden-AI-fill detector, rule 28
  inflated-bearing detector (§7.8). Rules 15–17 (responsibility arrow/ownership, empirical-
  extension warning, source-first citation — already shipped in `kernel/glosa_kernel.py` before
  this pass) folded into FOUNDATION §3.3's numbered prose for the first time. New schema fields
  (additive/optional, target `schema_version: "0.7.0"`): `comparison`, `evidence_strength`,
  `verdict_class`, `gate_fail_taxonomy`, `gate_construction_status`,
  `five_questions.seen.ai_assisted_fields` — applied to `schema/claim_card.schema.json` (schema_version 0.7.0) on disk. `templates/knowledge/litreview_manifest.yaml` gains
  `citations[].intake_tier`/`intake_tier_reason`/`global_south_exempt` and a `discovery_routing`
  block. Appendix A gains Family J (`NC-74`..`NC-76`; 76 rows across nine families).
- **Pending founder decision (recommended text specified, not ratified):** genre-router
  layer-mismatch diagnostic promotion (`promote-from-revise-to-ship-gate`, this patch's own
  proposal, not DAG-mandated), LRS claim-tier intake flag (`thin-layer-scope-confirmation`), PCS
  red-flag (`PCS-scoping-confirmation`), partial theology-neutral ontology analogue
  (`partial-analogue-adoption`), per-instance vs. standardized non-clinical/legal scope clause
  (`per-instance-vs-standardized-disclaimer`), LRS discovery-routing extension
  (`discovery-routing-stage-adoption`). None of these six is committed to `DECISIONS.yaml` or
  built until the founder rules (`EPIS-KNOWLEDGE-VALIDATION` — no external validation lever, the
  founder is the internal decision owner).
- **Tooling gaps this run found, not fixed this pass:**
  - **I3 route fixes:** rule 18's original draft mis-scanned for a match against kernel rule 8's
    unrelated `EXTERNAL_VALIDATION_PROPOSED` scan before a review response corrected it to a
    standalone new scan; the injected-infinity/zero taxonomy itself was also corrected from an
    invented epistemic/rhetorical vocabulary to `kc-base-016`'s real, verbatim physics/math
    continuum-injection taxonomy (I1–I4/Z1–Z4) — both flagged as I3-cross-vendor-caught corrections
    in `design/FOUNDATION_v0.6_PATCH.md`'s own review-response table, not as clean first drafts.
  - **Leak-scan rewrite:** `scripts/check_leak.sh` (34 un-allowlisted hits) and
    `scripts/check_forbidden_words.sh` (162 un-allowlisted hits) both still exit non-zero against
    the pre-existing corpus (`design/REPO_SPEC_v0.5.md` §9) — this pass is design/-only scope and
    does not touch either script; a leak-scan rewrite is named here as an open gap, not silently
    treated as fixed.
  - **Spot-check:** no independent (I2+) check has run on this synthesis pass, on the K-C1/K-C2/
    K-C3 kernel-closure rules, or on the six pending-founder recommended-text blocks — every one
    of them is K0/Dr, single-pass, same-model (this session's own maker-checker-gate finding
    applies, per `PUB-ADVERSARIAL-REVIEW`'s fail-closed rule: no independent check ⇒ no release).
    A held-out, differently-worded fixture batch (`tests/sim/corpus_v2/`, `[planned]`) is required
    before several of these rules' acceptance tests can be honestly re-run (§6's layer-confusion
    diagnostic, §5's verdict-class literal enum test, §23's discovery-routing precision/recall
    comparison).
## 0.2.0 — 2026-09-05
- Published: repository DOI 10.5281/zenodo.22307843 (archive tree = commit e6f9642; the tagged commit adds only the DOI pointers in CITATION.cff/README/CHANGELOG and the registry `released` row) (concept 10.5281/zenodo.22301059); concept paper DOI 10.5281/zenodo.22307841; GitHub tag v0.2.0.
- glosa applied to itself: concept paper (English, arXiv two-column) produced through the full spine — problem card, Blackbox Note, lens translation, three hypotheses selected by the founder, literature review system with 48 citation cards VERIFIED by a cross-vendor route under rule 17 (link + page + line + verbatim), own-lineage collision rows, claim cards reviewed by nine cross-vendor routes and revised (dissent preserved), publish gate v2.
- New rules from the run: rule 15/16 (responsibility per arrow, ownership of problem/question/hypothesis-selection, empirical extension), rule 17 (source-first citation), gate rule 9 (no AI attribution without permission); lit manifest fails closed on non-conformant cards; CLI writes repo-relative refs; pre-commit leak hook; install.sh / doctor / CI install test.
- Vendor names removed from all attribution surfaces; public git history rewritten to strip AI co-author trailers (founder ruling 2026-09-05).
- Zenodo: Bounded Knower series (Papers I–III) published and cross-linked; Blackbox Log updated through v15+.
## 0.1.0 — 2026-09-04
- Published: Zenodo DOI 10.5281/zenodo.22301060 (concept 10.5281/zenodo.22301059); GitHub morrocwi/glosa tag v0.1.0.
- Registry self-report: GLS-2026-001 stays at stage `genre_routed` — the registry state machine refuses `method…released` without a literature-review manifest, and this paper was released with a positioning table, not an LRS run (D-LIT-MODE). The system reports the gap on itself; closing it = run the LRS for this paper in 0.2.
- First public working release (K0: timestamped, citable, not peer reviewed, no independent check yet). Kernel 134 tests green, CLI/MCP/plugin, 20 schemas, methodology cards P00–P14, paper (design-science, Dr), Blackbox Log (concept DOI 10.5281/zenodo.22302518), 7 Zenodo programme hubs, research map. Publish gate v1 ran: 11 BLOCKs fixed before push (see reviews/PUBLISH_GATE_v1.md). All content tier Dr unless a test says otherwise.
- Adopted (founder instruction 2026-09-04, BBL-086/087): ownership criterion — problem, question, and the selection of the hypothesis stay human (BBL-088 wording) (FOUNDATION §2.1c, responsibility.ownership, kernel rule 15).
- Adopted (founder instruction 2026-09-04, BBL-083/084): problem-first spine wording, responsibility per Data→Inference→Claim arrow (rule 15), optional empirical_extension (operationalization, study design, bias register, robustness), P15 card.
- Paper: EN and TH texts and the LaTeX source (`paper/main_en.md`, `paper/main_th.md`, `paper/latex/`) were aligned on the D-LENS-UNCITED lens-citation status and on the "Positioning table" section naming.
## 0.0.1-draft — 2026-09-04
- Bootstrap: FOUNDATION_v0.5 (Dr), REPO_SPEC_v0.5, chair ruling, 14 knowledge templates, 2 compiled LaTeX templates, lineage (180 Zenodo rows), Blackbox Note drafts (not curated, not public).
- Nothing executable yet. Tier of everything: Dr.
