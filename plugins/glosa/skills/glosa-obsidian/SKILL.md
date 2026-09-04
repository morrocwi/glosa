---
name: glosa-obsidian
description: OPTIONAL Obsidian bridge for glosa — sync claim cards, Blackbox Notes, the kg, and per-hypothesis literature-review folders (records/lit/) into an Obsidian vault as linked notes, so the graph/backlinks surface agree/disagree clusters, orphan sources, and concentration. Triggers - "obsidian", "vault", "graph view", "backlinks", "connect glosa to obsidian", "harvest tags from obsidian".
---

# glosa-obsidian

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../docs/OBSIDIAN.md` — the full contract: vault-detection order, what `sync` writes,
  what `harvest` does, what this bridge never does. Read it before running any command below.
- `../../../../tools/obsidian_bridge.py` — the implementation; stdlib only (pyyaml optional).

## One-line rule (pointer only)

Founder rule, verbatim: *"เชื่อมกับระบบ Obsidian ได้เลย มีก็เชื่อม ไม่มีก็ไม่เชื่อม"* — if a vault
exists, connect; if not, do nothing. Every command below no-ops cleanly (exit 0, "no vault —
bridge skipped") when no vault is configured. This is optional infrastructure; nothing else in
glosa depends on it.

## Commands

```
python3 tools/obsidian_bridge.py detect            # which vault (if any) would be used, and why
python3 tools/obsidian_bridge.py sync [--dry-run]  # create/refresh <vault>/glosa/
python3 tools/obsidian_bridge.py check             # counts + dangling-wikilink report
python3 tools/obsidian_bridge.py harvest [--dry-run]  # read human tags back as CANDIDATE edits
python3 tools/obsidian_bridge.py unlink            # remove only bridge-generated files
```

## Vault resolution (detail: `docs/OBSIDIAN.md`)

`GLOSA_OBSIDIAN_VAULT` env var → `~/.config/glosa/author_profile.json` `defaults.obsidian_vault` →
self mode (`<repo>/obsidian/`, always available, opt out with `GLOSA_OBSIDIAN_DISABLE=1`).

## Obsidian as analysis surface, never source of truth

`sync` renders `records/lit/<hypothesis>/` (search log, citation cards, dialogue table) into one
note per hypothesis and one per source, with wikilinks so the Obsidian graph clusters
agree/disagree sources and exposes orphans/concentration by eye. The actual gate verdicts
(`litreview_manifest.yaml`'s `gate.accuracy_gate`/`gate.diversity_gate`) are the real source of
truth — the graph never overrides them. `harvest` reads back any `#tag` a human adds to a
generated source note and writes it to `records/lit/<hypothesis>/obsidian_harvest.yaml` as a
**candidate** edit only — it never writes to a citation card or dialogue table directly; a human
confirms and applies it by hand.

## What this skill/tool never does

Never touches `.obsidian/` (the vault's own app config). Never edits a source file to "fix" it —
it is a read-only renderer, `harvest` included. Never fails a build/CI check for lack of a vault.
Never makes a network call. Never copies a secret, local username, or absolute path into a note.

## Related

- `../glosa-literature-review/` — owns `records/lit/<hypothesis>/` itself; this skill only reads
  it.
- `../glosa-claim-card/`, `../glosa-blackbox-note/` — own the claim cards / Blackbox Notes this
  bridge renders.
