# glosa ↔ Obsidian bridge

tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this document and to
everything the bridge generates.

Founder rule, verbatim (2026-09-04): *"เชื่อมกับระบบ Obsidian ได้เลย มีก็เชื่อม ไม่มีก็ไม่เชื่อม"*
— connect to Obsidian if a vault exists; if not, do nothing. **This is OPTIONAL infrastructure.**
Nothing in glosa's kernel, CLI, MCP, or CI depends on Obsidian being installed, configured, or
even known about. The tool is `tools/obsidian_bridge.py`.

## What "connect" means here

The bridge reads files that already exist in this repo (claim cards, Blackbox Notes, the kg,
`records/lit/<hypothesis>/` literature-review folders, the registry, incidents, methodology cards)
and writes a **view** of them as Markdown notes with frontmatter and `[[wikilinks]]`, into
`<vault>/glosa/`. It never changes a source file's content, tier, or status. Every generated note
says so in its first line and names the exact source file to edit instead.

## Three ways glosa finds a vault (`detect`)

Run `python3 tools/obsidian_bridge.py detect` any time to see which one applies right now.

1. **`GLOSA_OBSIDIAN_VAULT`** environment variable — a path to an existing folder. Set it to `none`
   (or leave it empty) to disable the bridge outright, no matter what else is configured.
2. **`~/.config/glosa/author_profile.json` → `defaults.obsidian_vault`** — a durable, per-machine
   default, so you don't have to export an env var every session. Only used if the path exists.
3. **Self mode** — if neither of the above is set, the bridge treats the glosa repo's own working
   tree as the vault, writing to `<repo>/obsidian/`. Obsidian can open *any* folder as a vault, so
   this always works with zero configuration: `open <repo>/obsidian/ as a vault` in Obsidian, or
   point Obsidian at the whole repo root (the generated notes live under `obsidian/glosa/` either
   way). Set `GLOSA_OBSIDIAN_DISABLE=1` to turn even this off.

None of these three ever raises an error or fails a build. "No vault" always means the bridge
prints `no vault — bridge skipped` and exits 0.

## Commands

```
python3 tools/obsidian_bridge.py detect                     # which vault (if any) would be used
python3 tools/obsidian_bridge.py sync [--vault P] [--dry-run]  # create/refresh <vault>/glosa/
python3 tools/obsidian_bridge.py check [--vault P]            # counts + dangling-wikilink report
python3 tools/obsidian_bridge.py harvest [--vault P] [--dry-run]  # read back human tags as candidates
python3 tools/obsidian_bridge.py unlink [--vault P]           # remove only bridge-generated files
```

`sync` is idempotent and safe to re-run: unchanged notes are left alone (byte-identical), stale
notes (source removed) are pruned, and everything is tracked in a per-vault manifest,
`<vault>/glosa/.glosa_bridge_manifest.json`, so `unlink` only ever removes files this tool wrote —
it never touches a human's own vault notes, even ones that happen to live next to `glosa/`.

## What gets synced

- `00_INDEX.md` — links into every section below, plus the research registry
  (`registry/RESEARCH_REGISTRY.yaml` / `RESEARCH_LIBRARY.md`) when present.
- One note per claim card (`paper/claims/*.yaml`, `cases/*.yaml`) — frontmatter `id, tier, k_state,
  spine_stage, genre, produced_by`; body links to the Blackbox Note origin, citations, and the lens.
- One note per Blackbox Note file under `blackbox/` (yaml or the current markdown drafts).
- One note per kg node (`kg/nodes.jsonl`), with its `kg/edges.jsonl` relations rendered as
  wikilinks, so Obsidian's graph view mirrors glosa's own knowledge graph.
- A stub note for the lens, `Readout Universe — Yaoharee Lahtee.md`, so every card's lens link
  resolves to something real instead of a permanent dangling link.

## Obsidian as an analysis surface for the literature review — never a source of truth

Founder addition (HANDOFF 41b, 2026-09-04): once a hypothesis has a literature-review run under
`records/lit/<hypothesis>/` (search log, source-acquisition log, citation cards, dialogue-table
rows — see `templates/knowledge/`), `sync` also writes:

- `records_lit/<hypothesis>/00_hypothesis.md` — the hypothesis's own note, linking to its
  `search_log`, `litreview_manifest` (with both gates' status), `dialogue_table`, and every source.
- `records_lit/<hypothesis>/sources/<citation_card_id>.md` — one note per source, frontmatter
  `{source_id, stance, region, language, source_type, venue_quality_index, verified}` (`stance` is
  read from the matching `dialogue_table.md` row: agree/disagree/orthogonal/undetermined), with
  wikilinks back to the hypothesis and to every other source sharing the same agree/disagree stance.
- `records_lit/00_hypothesis_selection.md` if `records/lit/*.yaml` holds a `hypothesis_selection`
  file — chosen and parked candidates, each parked one keeping its required reason.

**Why this is useful:** once these notes exist, Obsidian's own graph view and backlinks panel — no
plugin, no query language needed — visually clusters agreeing vs. disagreeing sources around a
hypothesis, surfaces **orphan sources** (a source note with no link into any hypothesis is an
exclusion candidate), and lets a human eyeball **concentration** (too many sources sharing one
region/language tag) just by looking at the graph. None of this is computed by the bridge; the
bridge only writes the links, Obsidian renders the graph.

**Obsidian is an analysis surface, never the source of truth.** The `litreview_manifest.yaml`'s own
`gate.accuracy_gate` / `gate.diversity_gate` are the actual, mechanically-checked gate verdicts.
The graph is a way for a human to *see* the shape of the evidence before or after checking the
manifest — it never overrides or substitutes for `claim_match_verified`, the accuracy gate, or the
diversity gate. Nothing about a source's `status` changes because of how it looks in the graph.

### `harvest` — reading tags a human added in Obsidian back into the repo

A human reading the graph in Obsidian may tag a source note directly (e.g. `#disagrees_H1`,
`#region/thai`) while thinking about it — that's exactly what the tool is for. `harvest`:

1. Scans every bridge-generated source note under `<vault>/glosa/records_lit/*/sources/*.md` for
   any `#tag` appearing **after** the "generated by glosa obsidian_bridge" header line (i.e.
   anything a human added, not anything the bridge itself wrote).
2. Writes each hypothesis's findings to `records/lit/<hypothesis>/obsidian_harvest.yaml` in the
   **repo** (not the vault) as `candidate_edits` — never as a direct edit to any
   `citation_card.yaml` or `dialogue_table.md`.
3. Every row starts `confirmed: false`. A human reviews the file and applies confirmed edits to
   the real source by hand. **This tool never writes to a citation card or dialogue table itself.**

Recognized tag shapes: `#agrees_<hyp>` / `#disagrees_<hyp>` → a candidate `dialogue_table_stance`;
`#region/<x>` → a candidate `diversity.geography_or_institution`; `#language/<x>` or `#lang/<x>` →
a candidate `diversity.language`. Any other tag is still recorded, flagged `field: null` — "human
judgement needed" — nothing is silently dropped.

## What this bridge never does

- Never writes, reads, or touches `.obsidian/` (Obsidian's own app config: appearance, installed
  plugins, workspace layout). That directory is the user's, not this tool's.
- Never copies a secret, credential, local username, or absolute path from outside the repo into a
  generated note.
- Never fails a build, a render, a CI check, or any other glosa command because no vault is
  configured — `sync`/`harvest`/`check`/`unlink` all no-op cleanly when `detect()` finds nothing.
- Never edits a source file (`paper/claims/*.yaml`, a citation card, a dialogue table, the kg
  jsonl) to "fix" or "upgrade" anything it finds — it is a read-only renderer of those files, and
  `harvest`'s only write target is a clearly-labelled candidate file the human must confirm.
- Never makes a network call.
- Never changes the tier, `status`, or gate verdict written in a source file.

## How to open the repo as a vault (self mode)

No configuration needed: run `sync` with no `GLOSA_OBSIDIAN_VAULT` set and no
`defaults.obsidian_vault` in your `author_profile.json`. It creates `<repo>/obsidian/glosa/`. In
Obsidian: **Open folder as vault** → pick `~/ANSE.ASIA/glosa/obsidian/` (or the whole repo root —
either works; the generated notes always live at `obsidian/glosa/` relative to the repo).

## How to point at an existing vault instead

```bash
export GLOSA_OBSIDIAN_VAULT=~/vaults/my-research-vault   # example: any existing vault
python3 tools/obsidian_bridge.py sync --dry-run   # see what would be written first
python3 tools/obsidian_bridge.py sync
```

Or set it once, durably, in `~/.config/glosa/author_profile.json`:

```json
{ "defaults": { "obsidian_vault": "~/path/to/your/vault" } }
```

An existing vault with a single entry note (for example `KNOWLEDGE_MAP.md`) is a real Obsidian
vault on this machine — useful as a manual detect-logic test target (point `GLOSA_OBSIDIAN_VAULT`
at it deliberately to confirm detection works against a real `.obsidian/`-bearing folder) — but the
bridge never targets it automatically, and this project's own generated notes are not written into
it unless you explicitly set `GLOSA_OBSIDIAN_VAULT` to that path yourself.
