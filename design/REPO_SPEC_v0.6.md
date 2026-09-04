# glosa Repo Spec v0.6 — directory tree, v0.5 base + v0.6 patch diffs (mostly `[planned]`)

> **Tier: Dr** (this pass's own additions — none of them executed; see below) **+
> finite_diagnostic** (the v0.5 path list this document carries forward, itself read directly off
> disk at that pass). Sixth-pass update — folds every READY diff from `design/
> REPO_SPEC_v0.6_PATCH.md` (sim/ → tests/sim/, knowledge/harvest_v0.3/INDEX.md, docs/dag + kg
> render, README sections, tests/ additions for kernel rules 18–28, schema files touched) into
> this document as the target tree. **This pass does not itself move, rename, or create any file**
> (design/-only scope, matching `REPO_SPEC_v0.6_PATCH.md`'s own header) — every new or moved path
> below is marked `[planned]` unless it was already on disk as of v0.5. See "Changelog v0.5 → v0.6"
> immediately below.

## Changelog v0.5 → v0.6

- **§8 (was §9 in the patch's own draft, corrected):** tests/sim/ is targeted to move to
  tests/sim/ (version-stripped) — `git mv sim tests/sim` is named as a mechanical, not-yet-run
  step; `sim/` still exists at its v0.5 location on disk as of this pass.
- **§knowledge/:** `knowledge/harvest_v0.3/INDEX.md` (a generated, one-row-per-card-id navigation
  table) and `tools/gen_knowledge_index.py` (the generator) are named `[planned]` — not built this
  pass.
- **§docs/:** `docs/kg_v0.3.svg` + `tools/gen_kg_svg.py` (the roadmap's own S6 deliverable) named
  `[planned]`; `docs/dag_v0.4.svg` named `[planned]`, pending the 3 `K-C` nodes folding into a
  `DAG_v0.4.yaml` (also not yet built).
- **§README.md:** two new bilingual sections named (dev-map + knowledge-base pointers) — not yet
  applied to the live `README.md` file, which is outside this task's ownership list.
- **§schema/:** `schema/claim_card.schema.json`, `schema/litreview_manifest.schema.json` (NEW this
  pass), and `templates/knowledge/litreview_manifest.yaml` each gain additive fields per
  `design/FOUNDATION_v0.6.md` §3.2/§7.9 — named here for the schema-owning fixer, not edited by
  this pass.
- **§tests/:** `tests/test_kernel.py` gains one test function per new kernel rule (18–28);
  `tests/test_sim_regression.py` is named `[planned]` as the new pytest wrapper asserting
  recall/false_alarm does not regress against `tests/sim/report.md`'s recorded numbers.
- **Open items carried forward verbatim from `design/REPO_SPEC_v0.6_PATCH.md`'s own "Open items"
  list** (§ below, at the end of this document) — none resolved by this pass.

---

> **Fifth-pass header, carried forward below for lineage (v0.5's own front matter):**

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
schema/claim_card.schema.json        # this pass (v0.6): gains additive comparison, evidence_strength, verdict_class, gate_fail_taxonomy, gate_construction_status, five_questions.seen.ai_assisted_fields — not yet applied, spec only. See FOUNDATION_v0.6.md §3.2, schema_version target "0.7.0".
schema/evidence_relation.schema.json
schema/review_report.schema.json
schema/problem_card.schema.json            # = v0.4's planned intake.schema.json, different filename on disk.
schema/readiness_report.schema.json        # = v0.4's planned readiness.schema.json.
schema/release_manifest.schema.json
schema/citation_card.schema.json     # this pass (v0.6): NO field change — the K-C1/K-C3 kernel-closure checks (rule 26/28) are cross-object reads of existing fields (exact_passage, scope), not new schema fields; the earlier draft's `locators` field was dropped, see FOUNDATION_v0.6.md §7.8 correction.
schema/search_log.schema.json
schema/litreview_manifest.schema.json   # this pass (v0.6): gains additive citations[].intake_tier / intake_tier_reason / global_south_exempt, + discovery_routing block (both additive) — not yet applied, spec only. See FOUNDATION_v0.6.md §7.9.
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

## 6. `records/`, `kg/`, `ledgers/` — self-application artifacts  [planned]

```
kg/          # exists, EMPTY (no nodes.jsonl/edges.jsonl on disk yet).  [planned]
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
tests/test_kernel.py         # 84 tests as of v0.5 (stale figure not re-counted this pass, flagged not fixed — REPO_SPEC_v0.6_PATCH.md's own Review response leaves this SHOULD item open). EXTENDED this pass (not yet applied) — one new test function per rule 18-28: test_rule18_taxonomy_untyped, test_rule19_gate_type_unstated, test_rule20_novelty_word_rejected, test_rule21_layer_mismatch, test_rule22_intake_tier_untiered, test_rule23_verdict_class_unlisted, test_rule24_pcs_joint_condition, test_rule25_discovery_candidate_ungated, test_rule26_composite_quote, test_rule27_hidden_ai_fill, test_rule28_inflated_bearing.
 tests/sim/                 # was tests/sim/ (see below) — moved+renamed, version-stripped; `git mv sim tests/sim` not yet run.
 tests/sim/corpus/          # 180 claim_card/citation_card pairs + labels.json (ground truth) — unchanged content, moved location only.
 tests/sim/gen_corpus.py    # corpus generator, unchanged.
 tests/sim/baseline.py      # baseline harness (kernel-only pass), unchanged.
 tests/sim/combined.py      # combined ("if ship set X") harness, unchanged.
 tests/sim/prototypes/      # 8 S4 prototype scripts + *.result.json, unchanged.
 tests/sim/report.md        # this v0.3 K4-report, moved as historical record; future reports are tests/sim/report_vX.Y.md, append-only (never overwriting a prior pass's report).
[planned] tests/sim/corpus_v2/       # the held-out, differently-worded fixture batch the v0.6 acceptance tests call for — not built.
 tests/test_sim_regression.py   # NEW — pytest wrapper running baseline.py + the ship-set from combined.py against tests/sim/corpus/, asserting recall/false_alarm do not regress below report.md's recorded numbers; makes the sim corpus part of the actual CI-run suite.
tests/sim/                    # STILL AT THIS LOCATION as of this pass — the  tests/sim/ move above has not been executed; both paths named here rather than silently treating the move as done.
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
docs/dag_v0.3.svg            # NOT named anywhere in REPO_SPEC_v0.5.md's own tree (a gap between that document and design/DAG_v0.3.md's own header note, which says this file already exists) — named here per design/FOUNDATION_v0.6_PATCH.md/REPO_SPEC_v0.6_PATCH.md §3, unchanged this pass (no DAG_v0.3.yaml edit yet).
docs/dag_v0.3.dot            # same gap/correction as above.
docs/gen_dag_svg.py          # same gap/correction as above — reused, not forked, for any future DAG render.
[planned] docs/dag_v0.4.svg  # regenerate once DAG_v0.3.yaml + the 3 K-C nodes merge into a DAG_v0.4.yaml (open item, not this pass's scope).
[planned] docs/kg_v0.3.svg   # render of knowledge/harvest_v0.3/kg_edges_v0.3.jsonl (roadmap's own S6 step) — not yet built.
[planned] tools/gen_kg_svg.py   # reads kg_edges_v0.3.jsonl, writes docs/kg_v0.3.svg, same no-graphviz-dependency pattern as gen_dag_svg.py — not yet built.
.glosa/README.md             # NOT in REPO_SPEC_v0.4 — real, on disk.
dist/                        # exists, EMPTY (render.py's deliver-manifest output target, nothing generated into it yet this pass).
```

## 11. `knowledge/` — S1 knowledge harvest, public (new section this pass, v0.6)

**Why:** real, on disk, not named anywhere in `REPO_SPEC_v0.5.md`'s own tree — a gap this pass
closes by naming what already exists plus the missing navigation layer
`design/REPO_SPEC_v0.6_PATCH.md` §2 specifies.

```
knowledge/harvest_v0.3/ai/          # existing card files, unchanged.
knowledge/harvest_v0.3/aihp/        # unchanged.
knowledge/harvest_v0.3/base/        # unchanged.
knowledge/harvest_v0.3/ep/          # unchanged.
knowledge/harvest_v0.3/he/          # unchanged.
knowledge/harvest_v0.3/islam/       # unchanged.
knowledge/harvest_v0.3/ph/          # unchanged.
knowledge/harvest_v0.3/kg_edges_v0.3.jsonl        # existing knowledge-graph edge file, unchanged.
knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md   # 838 lines, existing narrative entry point, unchanged — retained as the prose companion to INDEX.md's machine-generated table (one-fact-one-home: table = INDEX.md, discussion = STATUS.md).
knowledge/harvest_v0.3/SPOTCHECK.md               # unchanged.
[planned] knowledge/harvest_v0.3/INDEX.md   # NEW — one row per card id (~324+ cards), columns: card_id, hub, status, adopted_by (DAG node id, computed from DAG_v0.3.yaml's own evidence[] lists — never hand-typed), locator. Generated by tools/gen_knowledge_index.py, not authored.
[planned] tools/gen_knowledge_index.py      # NEW — reads DAG_v0.3.yaml's evidence[] lists + every card file's own status field, writes INDEX.md; re-run after any DAG edit or new harvest card, never hand-edited.
```

**Public-ness note:** already public (CC BY 4.0, per `README.md`'s license line). `PUB-ADVERSARIAL-
REVIEW` (leak scan, privacy/security scan) still applies before `INDEX.md` itself is pushed — the
generator script must not surface any private `rl` stack path (per FOUNDATION §7.9's own
public/private boundary rule) — not run this pass, open item.

---

## Drift test (MUST-1)

`scripts/check_spec_pointers.sh` (new this pass) fails the build if:
1. Any tracked `.md`/`.json`/`.yaml`/`.yml` file, outside `design/` and `lineage/`, references
   `FOUNDATION_v0.[2345]` or `REPO_SPEC_v0.[2345]` (updated this pass, v0.6, to include the now
   -superseded v0.5 pair, since `design/CURRENT_SPEC.txt` now names v0.6 as canonical).
2. Any non-`[planned]` path listed in a fenced block of this document is missing from disk.

Run `bash scripts/check_spec_pointers.sh` before treating this document as current — see the
task's own K6-foundation run output for this pass's exact result.

---

## Open items carried forward from `design/REPO_SPEC_v0.6_PATCH.md` (none resolved by this pass)

1. Execute `git mv sim tests/sim` and update the three internal path references inside the moved
   `report.md`.
2. Fold the 3 `K-C` nodes into a `DAG_v0.4.yaml` with their own `requires`/`informs` edges (K-C1/
   K-C2/K-C3 have no stated dependency on any existing node — flagged, not guessed) and re-render
   `docs/dag_v0.4.svg`.
3. Build `tools/gen_knowledge_index.py` and run it once to produce
   `knowledge/harvest_v0.3/INDEX.md` — not built this pass.
4. Build `tools/gen_kg_svg.py` and `docs/kg_v0.3.svg` — the roadmap's own S6 deliverable, not yet
   built.
5. Run `PUB-ADVERSARIAL-REVIEW`'s leak scan on `knowledge/harvest_v0.3/INDEX.md` once generated,
   before any push — confirm no `rl` private-stack path is surfaced by the generator.
6. An I2+ (cross-vendor or human) check of this repo-spec pass has not run — Dr, single-pass,
   same-model, per this session's own maker-checker-gate finding.
7. Apply the README.md dev-map/knowledge-base sections named in the changelog above to the actual
   `README.md` file — outside this task's ownership list, named here as a pointer for whichever
   fixer owns that file.
