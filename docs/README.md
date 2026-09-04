# docs/ — rendered views, not a new source of truth

Tier: Dr. Readout, not truth. Every file here is a **rendered view** of a source file that lives
elsewhere in this repo — regenerate, never hand-edit, and never treat a file in this directory as
the one home of the fact it displays (one-fact-one-home; the generator script comment on each file
below names its real source).

## What's here

- **`dag_v0.3.dot` / `dag_v0.3.svg`** — the v0.3 improvement DAG (26 nodes, 25 edges), rendered by
  `gen_dag_svg.py` from `design/DAG_v0.3.yaml` (prose companion: `design/DAG_v0.3.md`). Border
  color/opacity encodes node status (`done` / `proposed` / `deferred`); the `⚑H` badge marks a
  `human_decision_needed: true` founder-decision node; edge style encodes `requires` (solid) /
  `informs` (dashed grey) / `conflicts` (red). Regenerate: `python3 docs/gen_dag_svg.py`.
- **`kg_v0.3.json` / `kg_v0.3.svg`** — the knowledge graph over every `kc-*.yaml` card under
  `knowledge/harvest_v0.3/` (324 nodes, 578 edges), rendered by `gen_kg_svg.py`. The same run also
  regenerates `knowledge/harvest_v0.3/INDEX.md` — the flat, generated, one-row-per-card table this
  graph is drawn from; that file, not this SVG, is the readable index. Regenerate:
  `python3 docs/gen_kg_svg.py`.
- **`DEBATE_KIT.md`** — the S15 ontology/epistemology/methodology pillars
  (`design/S15_pillars-ontology-epistemology-methodology.md`) recast as a debate reference (attack
  → principle → reply → counter-question → glosa artifact). Prose companion, not a generated file;
  edit it directly, but keep it consistent with S15 if S15 changes.
- **`OBSIDIAN.md`** — notes on browsing this repo's knowledge cards as an Obsidian vault.
- **`RESEARCH_MAP.md`** / **`research_map.svg`** / **`research_map.html`** — a rendered map of this
  repo's own research artifacts; see the file's own header for its generator, if any.

## Reading order for a new arrival

1. `README.md` (repo root) — what glosa is, one paragraph, and the pointers below.
2. `design/FOUNDATION_v0.6.md` + `design/REPO_SPEC_v0.6.md` (canonical pair, named in
   `design/CURRENT_SPEC.txt`) — the whole system.
3. `dag_v0.3.svg` here — what changed and what's still pending a founder decision.
4. `../knowledge/harvest_v0.3/INDEX.md` — the evidence base the DAG cites, one row per card.
5. `DEBATE_KIT.md` — if the question is "why this design instead of the obvious alternative."

## What this directory is not

Not a second copy of FOUNDATION, the DAG, or the knowledge cards — every number and claim shown
here is generated from, or directly cites, its one real home elsewhere in the repo. If a rendered
file here and its source disagree, the source wins and the rendered file is stale — regenerate it,
do not edit the render to match by hand.
