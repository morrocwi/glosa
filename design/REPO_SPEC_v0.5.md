# glosa Repo Spec v0.5 — directory tree corrected to what is ACTUALLY on disk

> **Tier: finite_diagnostic** (the path list below) **+ Dr** (one-line purposes/annotations).
> Companion to `design/FOUNDATION_v0.5.md`. Supersedes `REPO_SPEC_v0.4.md`, whose own header
> stated "NOT YET ON DISK, except the bare repo shell" — that statement was already stale by the
> time `ARCHITECTURE_REVIEW_v1.md` ran (2026-09-04): the callable layer (kernel, CLI, MCP server,
> 20 schemas, an 84-test suite) had been built. This document replaces v0.4's design-time ASCII
> tree with a **flat, full-relative-path list, one path per line**, read directly off disk and
> mechanically re-checkable — the ASCII-art connector style (`├──`/`│`/`└──`) v0.1–v0.4 used is
> dropped here specifically so `scripts/check_spec_pointers.sh` can verify every line without
> parsing indentation-based nesting.
>
> **Method (finite_diagnostic, executed, exact commands):** `find . -maxdepth 1 -mindepth 1` at
> repo root, then `ls -1` on every first- and second-level directory named below. Every path in a
> fenced block is either (a) a full relative path that exists on disk, verified this pass, or (b)
> prefixed `[planned]` — named in `FOUNDATION_v0.5.md`/`REPO_SPEC_v0.4.md` or an open item
> elsewhere, not yet built, deliberately listed as a gap rather than silently omitted. No path is
> asserted to exist without having been seen in this pass's own `find`/`ls` output.
> `design/CURRENT_SPEC.txt` names this file (with `FOUNDATION_v0.5.md`) as the canonical pair;
> `scripts/check_spec_pointers.sh` (new this pass) parses every fenced block below and fails if any
> non-`[planned]` path is missing from disk.
>
> **Format of each fenced block:** one path per line, relative to the repo root, optionally
> followed by two-or-more spaces and a `#` comment giving its one-line purpose. A line beginning
> `[planned]` names something documented elsewhere as intended but not on disk — the checker skips
> these by design (they are a disclosed gap, not a claim).
>
> **One-fact-one-home discipline, unchanged from v0.1–v0.4:** a file in `methodology/` states a
> rule in prose. A file in `schema/` states a rule's shape. A file in `methodology/data/` states a
> rule's *content* when machine-read. A file in `kernel/`/`scripts/`/`tools/` enforces or renders a
> rule. A file in `paper/` narrates a rule by citation. A file in `plugins/`/`cli/`/`mcp/` invokes
> a rule. No file may do two of these five jobs for the same rule.

---

## 1. Root

```
README.md                    # L0 thesis (TH-first, then EN pointer). Repo entry point.
AGENTS.md                    # Cross-AI conduct gate (identical block to CLAUDE.md/GEMINI.md); points at design/CURRENT_SPEC.txt.
CLAUDE.md                    # Same gate, the AI coding tool filename.
GEMINI.md                    # Same gate, Gemini filename.
llms.txt                     # Machine index for any LLM reading the repo cold.
CITATION.cff                 # Founder sole author (D-AUTHORSHIP; AI never in this array).
LICENSE                      # CC BY 4.0, whole repository, single license.
CLAIM_BOUNDARY.md            # L0 — glosa's own claim ceiling about itself.
ASSUMPTIONS.md               # Repo-level assumptions.
NON_CLAIMS.md                # Repo-level non-claims.
CHANGELOG.md                 # Append-only; every entry carries a tier label.
DECISIONS.md                 # glosa-local decision log.
CODE_OF_CONDUCT.md           # Short, plain-language conduct standard.
CONTRIBUTING.md              # How to open an issue/PR.
SECURITY.md                  # Security policy/scope.
TOOLCHAIN.md                 # What the write→validate→render→publish cycle needs installed.
RESEARCH_LIBRARY.md          # Rendered by tools/registry.py render from registry/RESEARCH_REGISTRY.yaml — a readout, not a truth ledger.
RELEASE_CHECKLIST.md         # Step-by-step release procedure (MUST-9: wires glosa release-gate + registry.py advance in).
requirements.txt             # pip toolchain pins (rendering/validation).
apt-packages.txt             # Informational only — documents system packages; not executed.
logbook.jsonl                # Append-only tool-call log (a second copy lives at mcp/logbook.jsonl — not yet reconciled, open item).

[planned] .zenodo.json       # Zenodo deposit metadata at repo root — not found; a project-level registry/zenodo_state.json exists instead (§7).
[planned] codemeta.json      # named in v0.2-v0.4 ("kept in lockstep with CITATION.cff") — not on disk.
[planned] AI_START_HERE.md   # named in v0.2-v0.4 as the cold-open read-order file — README.md + llms.txt carry this job today.
[planned] GLOSA_K1_K2_LEDGER.md   # K1->K2 conversion ledger at repo root — not on disk (see MUST list item L11).
```

## 2. `paper/` — narrates `methodology/*`, never restates

```
paper/README.md            # How the paper is built/compiled.
paper/main_th.md           # TH, source of truth.
paper/main_en.md           # EN, rewritten (not translated) companion.
paper/CLAIM_MATRIX.md      # Every numbered claim <-> claim_id.
paper/claims/              # Per-claim card files backing the matrix (10 real claim cards).
paper/latex/                # LaTeX build (main.pdf tracked — flagged L8 in ARCHITECTURE_REVIEW_v1 as a candidate to stop tracking).

[planned] paper/main.tex    # v0.4 described main.tex/main.bib directly under paper/ — the real build lives under paper/latex/ instead (layout differs, not merely absent).
[planned] paper/BLACKBOX_NOTE_APPENDIX.md   # the Blackbox Note appendix content currently lives inline in paper/main_en.md instead of as a standalone file.
[planned] paper/LIT_REVIEW_SCAFFOLD.md
[planned] paper/thai-tci/   # venue_track: thai_tci format variant.
```

## 3. `methodology/` — L1 protocol cards, prose only

```
methodology/README.md
methodology/P00_lens.md
methodology/P01_standpoint.md
methodology/P02_intake.md
methodology/P03_claim_card.md
methodology/P04_assumption_check.md
methodology/P05_evidence_challenge.md
methodology/P06_independent_check.md
methodology/P07_ai_fill_disclosure.md
methodology/P08_diagnosis.md
methodology/P09_vet_external_input.md
methodology/P10_publish_gate.md
methodology/P11_log_and_decision.md
methodology/P12_readiness.md
methodology/P13_literature_review.md
methodology/P14_project_advisor.md   # 15 cards, two-digit filenames P00-P14 — v0.4's own tree diagram showed single-digit `P0_...md`; the real convention is two-digit.
methodology/data/README.md
methodology/data/contaminated_concept_table.json
methodology/data/disclaimer_catalogue.json
methodology/data/genre_router_table.json
methodology/data/independence_ladder.json
methodology/data/non_collapse_table.json   # 64 rows on disk as of this pass — the 9 new NC-65..NC-73 rows FOUNDATION_v0.5.md §1.0 documents are not yet appended here (S1, still open).

[planned] methodology/P15_blackbox_note.md   # mechanism already callable (blackbox_note.schema.json) but carries no prose card yet (S2).
[planned] methodology/P16_genre_router.md    # mechanism already callable (route_genre() in the kernel) but carries no prose card yet (S2). methodology/README.md's own card index still cites the superseded REPO_SPEC_v0.3.md naming (S19).
```

## 4. `schema/` — L2, the only place a field name is defined

```
schema/README.md
schema/common.defs.json
schema/claim_card.schema.json
schema/evidence_relation.schema.json
schema/review_report.schema.json
schema/problem_card.schema.json            # = v0.4's planned intake.schema.json, different filename on disk.
schema/readiness_report.schema.json        # = v0.4's planned readiness.schema.json.
schema/release_manifest.schema.json
schema/citation_card.schema.json
schema/search_log.schema.json
schema/litreview_manifest.schema.json
schema/source_acquisition_log.schema.json
schema/dialogue_table_row.schema.json      # = v0.4's planned dialogue_table.schema.json.
schema/hypothesis_selection.schema.json
schema/kg_node.schema.json
schema/kg_edge.schema.json
schema/equation_registry_row.schema.json
schema/blackbox_note.schema.json
schema/conversion_plan.schema.json
schema/route_dependence_matrix.schema.json
schema/neighbour_table_row.schema.json     # not named in REPO_SPEC_v0.4 — real, on disk.
schema/disagreement_ledger_entry.schema.json   # = v0.4's planned disagreement_ledger.schema.json (per-entry, not per-ledger, shape).
schema/examples/blackbox_note.example.json
schema/examples/citation_card.example.json
schema/examples/claim_card.example.json
schema/examples/conversion_plan.example.json
schema/examples/dialogue_table_row.example.json
schema/examples/disagreement_ledger_entry.example.json
schema/examples/equation_registry_row.example.json
schema/examples/evidence_relation.example.json
schema/examples/hypothesis_selection.example.json
schema/examples/kg_edge.example.json
schema/examples/kg_node.example.json
schema/examples/litreview_manifest.example.json
schema/examples/neighbour_table_row.example.json
schema/examples/problem_card.example.json
schema/examples/readiness_report.example.json
schema/examples/release_manifest.example.json
schema/examples/review_report.example.json
schema/examples/route_dependence_matrix.example.json
schema/examples/search_log.example.json
schema/examples/source_acquisition_log.example.json   # flat layout, NOT the pass/fail/ nested layout REPO_SPEC_v0.4/the CI job assumed — the layout-mismatch MUST-5 names.
schema/examples/fail/fail_k2_without_i5.json
schema/examples/fail/fail_missing_disclaimer.json
schema/examples/fail/fail_no_independent_check.json
schema/examples/fail/fail_same_model_review.json
schema/examples/fail/fail_stub_public.json
schema/examples/fail/fail_th_coqc_no_witness.json

[planned] schema/xenon_ledger.schema.json   # confirms MUST-12's finding — no schema exists for the Xenon Ledger the kernel's own validate_citation_card() hard-fail cites.
[planned] schema/examples/fail/fail_lens_unsigned.json      # kernel rule 12, MUST-6.
[planned] schema/examples/fail/fail_no_human_approver.json  # MUST-7.
```

## 5. `templates/` — human-fillable instances of the schema shapes

```
templates/knowledge/advisor_prompt_packet.md
templates/knowledge/blackbox_note.yaml       # YAML-validity fix pending, MUST-2 (a bare `:` in a placeholder, line 63).
templates/knowledge/citation_card.yaml       # `independence_class` field missing, MUST-3.
templates/knowledge/conversion_plan.yaml
templates/knowledge/cross_vendor_review_packet.md
templates/knowledge/dialogue_table.md
templates/knowledge/equation_registry_row.yaml
templates/knowledge/hypothesis_selection.yaml
templates/knowledge/kg_edge.yaml
templates/knowledge/kg_node.yaml
templates/knowledge/library_spinout_checklist.md
templates/knowledge/lit_review_gate_checklist.md
templates/knowledge/litreview_manifest.yaml
templates/knowledge/neighbour_table.md
templates/knowledge/project_skeleton.md
templates/knowledge/route_dependence_matrix.yaml
templates/knowledge/search_log.yaml
templates/knowledge/sr_protocol_prisma_lite.md
templates/paper/arxiv-onecol/
templates/paper/arxiv-twocol/

[planned] templates/knowledge/dialogue_card.yaml   # still explicitly flagged open by v0.4 itself.
[planned] templates/claim_card.yaml
[planned] templates/evidence_relation.yaml
[planned] templates/assumptions.md
[planned] templates/non_claims.md
[planned] templates/ai_fill_ledger.md
[planned] templates/review_report.md
[planned] templates/readiness_report.md
[planned] templates/logbook.jsonl
[planned] templates/paper-outline/   # a flat top-level templates/ tier v0.4 described alongside knowledge/ and paper/ is not on disk; only those two subdirectories exist.
```

## 6. `records/`, `kg/`, `ledgers/` — self-application artifacts

```
kg/          # exists, EMPTY (no nodes.jsonl/edges.jsonl on disk yet).
ledgers/     # exists, EMPTY (no DISAGREEMENT_LEDGER.md/XENON_LEDGER.md on disk yet).

[planned] records/   # the whole per-project problems/sources/observations/claims/blackbox/lit/hypothesis_selection/logbook.jsonl tree named in REPO_SPEC_v0.4 does not exist under this name. Real self-application artifacts that DO exist instead: paper/claims/ (10 real claim cards) and registry/RESEARCH_REGISTRY.yaml (the project's own registry entry, GLS-2026-001 — see MUST-10, its own state-machine violation).
```

## 7. `cases/`, `incidents/`, `lineage/`, `reviews/` — narrative/process record

```
cases/README.md
cases/worked-example-cat.md         # Step 7 stub claim card fails validation, MUST-8.
incidents/README.md
incidents/2026-06-22_tuned-on-test-internal-eval.md
incidents/2026-06-30_ai-overclaim-x6-one-session.md
incidents/2026-07-24_ttfb-single-instrument.md
incidents/2026-07-31_toon-format-accuracy-overclaim.md
incidents/2026-08-01_check-docs-silent-pass.md
incidents/2026-08-03_readout-universe-license-leak.md
incidents/2026-08-08_rubygems-skillme-rm-rf.md
incidents/2026-08-09_hosting-vendor-ip-ban.md
incidents/date-not-in-source_atomic-swap-plugin-deploy.md   # 9 incident files — different filenames than REPO_SPEC_v0.4's illustrative example list. No INDEX.md; README.md fills that job.
lineage/README.md
lineage/PRIOR_WORK.md
lineage/RELATION_TO_ANSE_SKILLS.md
lineage/RELATION_TO_READOUT_CONDITION.md
lineage/RELATION_TO_STANDALONE_SCHOLAR.md
lineage/RELATION_TO_WRITTEN_BY_AI.md   # not named in REPO_SPEC_v0.4 — real, on disk (backs FOUNDATION_v0.5.md §1.0's pillars citation).
reviews/ARCH_CROSSCHECK.md
reviews/ARCH_efficiency.md
reviews/ARCH_integrity.md
reviews/ARCH_lifecycle.md
reviews/ARCH_structure.md
reviews/ARCH_sustainability.md
reviews/ARCH_usability.md
reviews/BUILD_V1_mechanical.md
reviews/BUILD_V2_consistency.md
reviews/FOUNDATION_v0.2_anchor.md
reviews/FOUNDATION_v0.2_usability.md
reviews/RELEASE_PREP_CHECK.md   # NOT the YYYY-MM-DD_<stage>_<route>.md + routes/<claim_id>/<route_id>/{PACKET.md,review_report.yaml} layout REPO_SPEC_v0.4 specified — real files are named by review subject, no routes/ subdirectory exists yet. reviews/ publication policy is itself an open founder decision (MUST-13, §7 decision 6).
```

## 8. Callable layer — schemas → kernel → CLI → MCP → plugin

```
kernel/glosa_kernel.py       # validate_*, gate_release, mc01_check, route_genre, kg_merge, cite_check, demo_run, self_test, and more — one file, not a package (REPO_SPEC_v0.4 showed kernel/tests/ nested here; the real test suite lives at top-level tests/, see below).
tests/test_kernel.py         # 84 tests, `python3 -m unittest discover -s tests` -> 84/84 OK. One file, not the per-concern split (test_schemas_valid.py, test_gate_release.py, ...) or the fixtures/ directory REPO_SPEC_v0.4 described.
cli/README.md                # Full command list — `./cli/glosa --help` is the live source.
cli/glosa                    # Console entry point.
mcp/README.md
mcp/glosa_mcp_server.py      # One tool per kernel function.
mcp/logbook.jsonl            # Second copy of the root logbook — open item, not reconciled.
mcp/test_mcp_stdio.py        # Not named in REPO_SPEC_v0.4 — real, on disk; coverage depth not independently audited this pass.
.claude-plugin/marketplace.json
plugins/glosa/README.md
plugins/glosa/PROMPT_PACKET.md
plugins/glosa/.claude-plugin/plugin.json
plugins/glosa/skills/glosa/SKILL.md
plugins/glosa/skills/glosa-blackbox-note/SKILL.md
plugins/glosa/skills/glosa-claim-card/SKILL.md
plugins/glosa/skills/glosa-deliver/SKILL.md
plugins/glosa/skills/glosa-independent-check/SKILL.md
plugins/glosa/skills/glosa-literature-review/SKILL.md
plugins/glosa/skills/glosa-obsidian/SKILL.md
plugins/glosa/skills/glosa-project-advisor/SKILL.md
plugins/glosa/skills/glosa-publish-gate/SKILL.md
plugins/glosa/skills/glosa-render/SKILL.md   # 10 skills — different set than REPO_SPEC_v0.4's list (no glosa-intake/glosa-evidence-challenge/glosa-disclaimer-system/glosa-genre-router/glosa-cite-check skills on disk; glosa-deliver/glosa-obsidian/glosa-render/the umbrella glosa/SKILL.md are real and not in v0.4's list).

[planned] tests/test_cli.py   # S7, ARCHITECTURE_REVIEW_v1 — argparse dispatch layer for cmd_* handlers is not exercised.
```

## 9. `scripts/`, `tools/` — repo maintenance and rendering

```
scripts/check_repo.sh
scripts/check_forbidden_words.sh    # currently exits 1, 162 un-allowlisted hits (MUST-13).
scripts/check_leak.sh               # currently exits 1, 34 un-allowlisted hits (MUST-13).
scripts/check_toolchain.sh
scripts/check_version.py
scripts/forbidden_words_allowlist.txt
scripts/leak_denylist.txt
scripts/load_secrets.sh
scripts/validate_examples.py
scripts/zenodo_cluster.py
scripts/zenodo_deposit.py           # has the founder-approval gate (--i-have-founder-approval + RELEASE_APPROVAL.txt).
scripts/zenodo_publish_file.py      # does NOT have that gate yet (MUST-11).
scripts/check_spec_pointers.sh      # NEW this pass — this document's own drift test.
tools/blackbox_log.py               # NOT in REPO_SPEC_v0.4 at all — real, on disk.
tools/obsidian_bridge.py
tools/registry.py                   # `advance <id> <stage>` — the registry lifecycle tool MUST-9 wires into RELEASE_CHECKLIST.md.
tools/render.py
tools/research_map.py
```

## 10. `.github/`, `registry/`, `sources/`, `blackbox/`, `docs/`, `.glosa/`, `dist/`

```
.github/workflows/ci.yml     # schema-validate job has both a RefResolver bug and a directory-layout mismatch against the real flat schema/examples/ layout above (MUST-5). Never actually run against this content — no push to a remote where Actions runs.
registry/README.md           # NOT in REPO_SPEC_v0.4 at all — real, on disk.
registry/RELEASE_APPROVAL.txt.EXAMPLE
registry/RESEARCH_REGISTRY.yaml     # GLS-2026-001's own state-machine violation, MUST-10.
registry/blackbox_log_zenodo.json
registry/downloads_scan_2026-09-04.json
registry/zenodo_all_records.json
registry/zenodo_all_records_2026-09-04.json   # duplicate snapshot pair, S14.
registry/zenodo_clusters.json
registry/zenodo_state.json
registry/zenodo_uploads/
sources/README.md            # NOT in REPO_SPEC_v0.4 — real, on disk: primary-source PDFs/text extracts (CPRMH v12, the Readout Condition, "Written by AI. Still True.") + citation_cards/ backing them.
sources/citation_cards/
blackbox/README.md           # NOT records/blackbox/<id>.yaml as REPO_SPEC_v0.4 envisioned — real layout is flat DIALOGUE_*_DRAFT.md files plus a log/ subdirectory.
blackbox/log/
docs/DEBATE_KIT.md           # NOT in REPO_SPEC_v0.4 — real, on disk.
docs/OBSIDIAN.md
docs/RESEARCH_MAP.md
.glosa/README.md             # NOT in REPO_SPEC_v0.4 — real, on disk.
dist/                        # exists, EMPTY (render.py's deliver-manifest output target, nothing generated into it yet this pass).
```

---

## Drift test (MUST-1)

`scripts/check_spec_pointers.sh` (new this pass) fails the build if:
1. Any tracked `.md`/`.json`/`.yaml`/`.yml` file, outside `design/` and `lineage/`, references
   `FOUNDATION_v0.[234]` or `REPO_SPEC_v0.[234]`.
2. Any non-`[planned]` path listed in a fenced block of this document is missing from disk.

Executed this pass — see the fixer's own report for exact output.
