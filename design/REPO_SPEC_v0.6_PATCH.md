# glosa Repo Spec v0.6 patch — file/dir changes for S3/S4/S5 closure

> **Tier: Dr, specified not applied.** Companion to `design/FOUNDATION_v0.6_PATCH.md`. States the
> exact file/directory diffs against `design/REPO_SPEC_v0.5.md` needed to carry the S3 DAG (26
> nodes), the S4 sim corpus, and the S1 knowledge harvest into the repo's permanent, tracked
> structure. Does not itself move any file — per this task's scope (`design/` only). Format
> follows `REPO_SPEC_v0.5.md`'s own precedent: flat relative-path lists, one path per line,
> `[planned]` prefix for anything not yet on disk. Readout, not truth; no novel/first/prior-art
> language; comparisons stay same/different/cited.

---

## 1. `sim/` → tracked test corpus under `tests/sim/`

**Why:** `sim/v0.3/` currently holds the S4 prototype harness, the 180-card synthetic corpus, and
`report.md` — a real, checkable evaluation artifact — but it sits outside `tests/`, which
`REPO_SPEC_v0.5.md` §9 names as the repo's actual test suite location (`tests/test_kernel.py`,
`tests/test_registry.py`, `tests/test_install.py` already there, 84-test suite per
`ARCHITECTURE_REVIEW_v1.md`). A finite, printed, regenerable corpus that measures kernel behavior
belongs in the test suite's own directory, not in a versioned `sim/vX.Y/` scratch area that a
future minor version would otherwise leave orphaned once `v0.4` scratch work starts.

**Diff:**
```
tests/sim/                          # NEW — was sim/v0.3/, moved+renamed, version-stripped
tests/sim/corpus/                   # 180 claim_card/citation_card pairs + labels.json (ground truth)
tests/sim/gen_corpus.py             # corpus generator, unchanged
tests/sim/baseline.py               # baseline harness (kernel-only pass), unchanged
tests/sim/baseline.json             # baseline run output, unchanged
tests/sim/combined.py               # combined ("if ship set X") harness, unchanged
tests/sim/combined.json             # combined run output, unchanged
tests/sim/prototypes/               # 8 S4 prototype scripts + *.result.json, unchanged
tests/sim/report.md                 # this v0.3 K4-report, moved as historical record — new
                                     # reports for future passes are tests/sim/report_vX.Y.md,
                                     # never overwriting a prior pass's report (append-only history,
                                     # same discipline as XENON_LEDGER.md, §7.8)
tests/test_sim_regression.py        # NEW — a pytest wrapper that runs baseline.py + the ship-set
                                     # from combined.py against tests/sim/corpus/ and asserts
                                     # recall/false_alarm do not regress below the last-recorded
                                     # report.md numbers; this is what makes the sim corpus part of
                                     # the actual CI-run test suite rather than a one-off script
[planned] tests/sim/corpus_v2/      # the held-out, differently-worded fixture batch
                                     # FOUNDATION_v0.6_PATCH.md §3/§6/K-C1-3 acceptance tests call
                                     # for — not built this pass, named here as the next corpus
                                     # generation's home once it exists
```

**One-fact-one-home note:** `tests/sim/corpus/labels.json` remains the one ground-truth home (per
`REPO_SPEC_v0.5.md`'s own discipline) — `report.md`/`combined.json`/`baseline.json` all read it,
none re-derives or duplicates label assignment.

**Migration note (mechanical, not yet run):** `git mv sim tests/sim` preserves history; update the
three hard-coded `sim/v0.3/...` path references inside `tests/sim/report.md`'s own prose (it
narrates its own file locations) to `tests/sim/...` at move time, and add a redirect note at the
old `sim/` location's former path in `CHANGELOG.md` (not a stub file — `sim/` is deleted outright,
per the DAG's own no-novelty/no-duplication discipline; a stale directory left behind would violate
one-fact-one-home).

---

## 2. `knowledge/harvest_v0.3/` → public knowledge base with `INDEX`

**Why:** `KNOWLEDGE_STATUS_v0.3.md` (838 lines) is currently the only entry point into 324+
knowledge cards spread across `knowledge/harvest_v0.3/{ai,aihp,base,ep,he,islam,ph}/` — a reader
has to open the status file and cross-reference card ids by hand. `REPO_SPEC_v0.5.md` §10 already
lists `knowledge/` as a top-level directory; this patch adds the missing navigation layer without
moving any card file (each card's file path is already its one home; a card's *content* does not
move).

**Diff:**
```
knowledge/harvest_v0.3/INDEX.md     # NEW — one row per card id (all ~324+ cards across
                                     # ai/aihp/base/ep/he/islam/ph), columns: card_id, hub,
                                     # status (holds/refined_by_later_work/superseded/outdated/
                                     # open), adopted_by (DAG node id if any, per DAG_v0.3.yaml's
                                     # own `evidence:` lists — computed by a script, never
                                     # hand-typed, so it cannot drift from the DAG), locator.
                                     # Generated, not authored: see tools/gen_knowledge_index.py
                                     # below — one fact (which node adopted which card), one home
                                     # (DAG_v0.3.yaml's evidence lists), one render (this INDEX).
knowledge/harvest_v0.3/ai/          # unchanged, existing card files
knowledge/harvest_v0.3/aihp/        # unchanged
knowledge/harvest_v0.3/base/        # unchanged
knowledge/harvest_v0.3/ep/          # unchanged
knowledge/harvest_v0.3/he/          # unchanged
knowledge/harvest_v0.3/islam/       # unchanged
knowledge/harvest_v0.3/ph/          # unchanged
knowledge/harvest_v0.3/kg_edges_v0.3.jsonl   # unchanged — existing knowledge-graph edge file
knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md  # unchanged — retained as the narrative/prose
                                     # companion to INDEX.md's machine-generated table; INDEX.md
                                     # does not replace it, since KNOWLEDGE_STATUS carries the §4
                                     # Adopt/Adapt discussion prose INDEX.md's flat table cannot
                                     # (one-fact-one-home: table = INDEX.md, discussion = STATUS.md)
knowledge/harvest_v0.3/SPOTCHECK.md # unchanged
tools/gen_knowledge_index.py        # NEW — reads DAG_v0.3.yaml's evidence[] lists + every card
                                     # file's own status field, writes INDEX.md; re-run after any
                                     # DAG edit or new harvest card, never hand-edited
```

**Public-ness note:** `knowledge/harvest_v0.3/` is already public (this repo is CC BY 4.0 per
`README.md`'s license line); this patch only adds a navigable index, it does not change any
existing publication-gate status. `PUB-ADVERSARIAL-REVIEW` (leak scan, privacy/security scan)
still applies before `INDEX.md` itself is pushed — the generator script must not surface any
private `rl` stack path (per FOUNDATION §7.9's own public/private boundary rule), and this patch
does not run that scan; it is listed as an open item below.

---

## 3. `docs/dag` + kg render

**Why:** `docs/dag_v0.3.svg`/`docs/dag_v0.3.dot` already exist (per `design/DAG_v0.3.md`'s own
header note, drawn by `docs/gen_dag_svg.py` since graphviz was unavailable on this workstation).
This patch names the v0.6 update path for when the DAG gains the 3 `K-C` nodes from
`FOUNDATION_v0.6_PATCH.md`, and adds the missing knowledge-graph (kg) render `REPO_SPEC_v0.5.md`
§6 names `kg/` for but does not yet connect to a rendered output.

**Diff:**
```
docs/dag_v0.3.svg                   # unchanged this pass (no DAG_v0.3.yaml edit; the 3 K-C nodes
                                     # are new FOUNDATION_v0.6_PATCH.md content, not yet folded
                                     # into DAG_v0.3.yaml itself — see open item 2 below)
docs/dag_v0.3.dot                   # unchanged
[planned] docs/dag_v0.4.svg         # regenerate once DAG_v0.3.yaml + the 3 K-C nodes merge into
                                     # a DAG_v0.4.yaml (open item, not this pass's scope)
docs/gen_dag_svg.py                 # unchanged — reused, not forked, for any future DAG render
[planned] docs/kg_v0.3.svg          # NEW — render of knowledge/harvest_v0.3/kg_edges_v0.3.jsonl,
                                     # the knowledge-graph companion to dag_v0.3.svg the roadmap's
                                     # own S6 step names ("README with DAG + knowledge graph (kg)
                                     # render", ROADMAP_v0.3.md step S6) — not yet built
[planned] tools/gen_kg_svg.py       # NEW — reads kg_edges_v0.3.jsonl, writes docs/kg_v0.3.svg,
                                     # same no-graphviz-dependency pattern as gen_dag_svg.py
docs/DEBATE_KIT.md                  # unchanged
docs/OBSIDIAN.md                    # unchanged
docs/RESEARCH_MAP.md                # unchanged
docs/research_map.html              # unchanged
docs/research_map.svg               # unchanged
```

---

## 4. README sections

**Why:** `ROADMAP_v0.3.md` step S6 names "README with DAG + knowledge graph (kg) render" as a
build-step deliverable. `README.md` (root) currently has no pointer to `design/DAG_v0.3.md`,
`docs/dag_v0.3.svg`, or `knowledge/harvest_v0.3/INDEX.md` (new, §2 above).

**Diff (README.md, additive sections only, both TH and EN halves per §2.5's bilingual rule — TH
source of truth, EN rewritten not translated):**
```markdown
## แผนที่การพัฒนา (S3 improvement DAG)
`design/DAG_v0.3.md` — 26 nodes (proposed/done/deferred), แต่ละ node มี acceptance test +
evidence card id; render: `docs/dag_v0.3.svg`. สถานะ ship/revise/drop จาก S4 simulation:
`sim/v0.3/report.md` (ย้ายเป็น `tests/sim/report.md` ตาม `design/REPO_SPEC_v0.6_PATCH.md` §1).

## ฐานความรู้ (S1 knowledge harvest)
`knowledge/harvest_v0.3/INDEX.md` — ดัชนีการ์ดความรู้ทั้งหมด (~324+ ใบ), เชื่อมกับ DAG node
ที่ใช้การ์ดนั้นเป็นหลักฐาน; อภิปรายเต็ม: `knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md`.

## Development map (S3 improvement DAG)
`design/DAG_v0.3.md` — 26 nodes (proposed/done/deferred), each with an acceptance test and
evidence card ids; render: `docs/dag_v0.3.svg`. Ship/revise/drop status from the S4 simulation:
`sim/v0.3/report.md` (moved to `tests/sim/report.md` per `design/REPO_SPEC_v0.6_PATCH.md` §1).

## Knowledge base (S1 harvest)
`knowledge/harvest_v0.3/INDEX.md` — index of all knowledge cards (~324+), cross-linked to the DAG
node that cites each as evidence; full discussion: `knowledge/harvest_v0.3/KNOWLEDGE_STATUS_v0.3.md`.
```

**Placement:** immediately after the existing "หาคำสั่งได้จากไหน (CLI discoverability)" section,
before "ผู้ทำ" — matching the existing README's own section order (entry points, then commands,
then knowledge/dev-map additions here, then authorship/license).

---

## 5. `tests/` additions for the new kernel rules (18–28)

**Why:** `FOUNDATION_v0.6_PATCH.md` §1–§23 and K-C1–K-C3 each name a new kernel rule (18–28,
detailed in that document's Rule numbering table). `REPO_SPEC_v0.5.md` §9 names
`tests/test_kernel.py` as the existing kernel test file; this patch does not fork a new test file
per rule (one-fact-one-home: kernel behavior tests live in one file, matching rules 1–17's own
existing placement) — it names the additions to the existing file plus the corpus wiring from §1
above.

**Diff:**
```
tests/test_kernel.py                # EXTENDED, not replaced — add one test function per new rule
                                     # (test_rule18_taxonomy_untyped, test_rule19_gate_type_unstated,
                                     # test_rule20_novelty_word_rejected, test_rule21_layer_mismatch,
                                     # test_rule22_intake_tier_untiered, test_rule23_verdict_class_
                                     # unlisted, test_rule24_pcs_joint_condition, test_rule25_
                                     # discovery_candidate_ungated, test_rule26_composite_quote,
                                     # test_rule27_hidden_ai_fill, test_rule28_inflated_bearing) —
                                     # matching the file's existing one-function-per-rule convention
tests/test_sim_regression.py        # NEW (also listed in §1) — asserts K-C1/K-C2/K-C3 (rules
                                     # 26-28) reach 9/9 caught on their respective
                                     # tests/sim/corpus/ fixture slices, per
                                     # FOUNDATION_v0.6_PATCH.md's own acceptance tests
```

---

## 6. Schema files touched (additive only, no breaking change this pass)

Per `FOUNDATION_v0.6_PATCH.md`'s own "Open items" §1 (schema_version bump pending confirmation),
the following schema files gain additive fields once this patch is applied — named here for the
schema-owning fixer, not edited by this patch itself:

```
schema/claim_card.schema.json       # + comparison, evidence_strength, verdict_class,
                                     # gate_fail_taxonomy (all additive/optional)
schema/citation_card.schema.json    # no field change this pass (K-C1/K-C3 are kernel-only
                                     # cross-object checks reading existing fields)
templates/knowledge/litreview_manifest.yaml   # + sources_found[].intake_tier /
                                     # intake_tier_reason / global_south_exempt,
                                     # + discovery_routing block (both additive)
```

---

## 7. What this patch does NOT change

- No file under `kernel/`, `schema/`, `templates/`, or `cli/` is edited by this patch — it is a
  `design/`-only specification, matching this task's own scope restriction.
- `sources/`, `blackbox/`, `registry/`, `ledgers/`, `lineage/`, `cases/`, `incidents/`, `reviews/`,
  `paper/`, `methodology/`, `mcp/`, `plugins/`, `logbook.jsonl`, `llms.txt`, `CHANGELOG.md`,
  `CITATION.cff`, and every root governance file (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`,
  `CLAIM_BOUNDARY.md`, `NON_CLAIMS.md`, etc.) are unchanged by this patch.
- `design/DAG_v0.3.yaml`/`design/DAG_v0.3.md` are read, not edited — the 3 `K-C` nodes named in
  `FOUNDATION_v0.6_PATCH.md` are new content in that document only; folding them into a
  `DAG_v0.4.yaml` (with their own edges/topological order) is named as an open item below, not
  done by this patch.

## Open items for the AI assistant / next synthesis pass

1. Execute `git mv sim tests/sim` (§1) and update the three internal path references inside the
   moved `report.md`.
2. Fold the 3 `K-C` nodes (`FOUNDATION_v0.6_PATCH.md`'s "New nodes" section) into a `DAG_v0.4.yaml`
   with their own `requires`/`informs` edges (K-C1/K-C2/K-C3 have no stated dependency on any
   existing node in this patch — flagged here rather than guessed) and re-render `docs/dag_v0.4.svg`.
3. Build `tools/gen_knowledge_index.py` and run it once to produce `knowledge/harvest_v0.3/
   INDEX.md` (§2) — not built this pass.
4. Build `tools/gen_kg_svg.py` and `docs/kg_v0.3.svg` (§3) — the roadmap's own S6 deliverable, not
   yet built.
5. Run `PUB-ADVERSARIAL-REVIEW`'s leak scan on `knowledge/harvest_v0.3/INDEX.md` once generated,
   before any push — confirm no `rl` private-stack path (Zotero item key, Paperless doc id, local
   file path) is surfaced by the generator (FOUNDATION §7.9's public/private boundary rule).
6. An I2+ (cross-vendor or human) check of this repo-spec patch has not run — Dr, single-pass,
   same-model, per this session's own maker-checker-gate finding.
