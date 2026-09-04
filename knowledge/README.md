# knowledge/ — the harvest, its statuses, and the citation discipline it follows

This directory holds the raw evidence base glosa's own `design/FOUNDATION_v0.6_PATCH.md`
and DAG nodes cite. Everything here is a readout of an already-published source (a Zenodo
record, a repo file, a text file) — not a claim in its own right, and not an independent
re-derivation of what that source argued. Tier discipline (`Th_coqc` / `finite_diagnostic` /
`Dr` / `Open`, defined in `design/FOUNDATION_v0.6_PATCH.md` §4.1) applies to every card in
this directory exactly as it applies to the rest of the corpus.

## What is in `harvest_v0.3/`

- One folder per **hub**: `base/` (the readout_universe / readout_genesis root texts — the
  lens the rest of the corpus is judged against) plus eight subject hubs (`ai`, `aihp`, `ep`,
  `he`, `islam`, `ph`, `se`, `tourism`), each a cluster of sources sharing a Zenodo hub DOI or
  a common origin document.
- Inside each hub folder: one `kc-<hub>-NNN.yaml` **knowledge card** per source (or, where a
  single source yields more than one distinct extractable point, more than one card citing
  the same source), plus a per-hub `INDEX.md` table.
- `knowledge/harvest_v0.3/INDEX.md` — the flat, all-hub index (id / kind / title /
  base_relation / glosa_use / source for every card), generated from the cards themselves,
  never hand-edited. Regenerate it and the knowledge-graph render together — see
  `docs/gen_kg_svg.py`.
- `KNOWLEDGE_STATUS_v0.3.md` — the narrative rollup discussing each hub's cards in prose;
  this README does not duplicate that discussion.
- `kg_edges_v0.3.jsonl` — one JSON line per edge (`{"from": <card id>, "to": <card id, or
  "base", or "FOUNDATION">, "relation": ...}`) recording how a card relates to a base card,
  to the base hub in general, or to a target section of `FOUNDATION`. Rendered (with the
  cards above, as nodes) by `docs/gen_kg_svg.py` into `docs/kg_v0.3.svg` / `docs/kg_v0.3.json`.
- `SPOTCHECK.md` — a targeted independent-review pass over a sample of cards, not a claim
  that every card in the harvest has been independently re-checked.

## Card statuses

Every card carries two independent judgments, kept as separate fields (one fact, one home —
neither is inferred from the other):

- **`base_relation`** — how the card's claim stands against the `base` hub's own texts:
  - `holds` — consistent with / restates the base lens, no tension found.
  - `refined_by_later_work` — an earlier position the corpus's own later material narrows or
    updates; not wrong, superseded in scope.
  - `superseded` — a later base-hub statement replaces this one; kept in the harvest for
    lineage, not for citation as current.
  - `outdated` — no longer an accurate description of the corpus's current position.
  - `open` — the source itself marks the claim `[Open]` or leaves it without a worked case;
    tiered accordingly, not silently upgraded.
- **`glosa_use`** — what, if anything, glosa's own `FOUNDATION`/DAG should do with the card:
  `adopt` (cite or use as-is) · `adapt` (use with reformulation) · `already_in_glosa` (the
  point is already present in glosa's own text, cited here for lineage) · `skip` (not used
  this pass).

A card's `tier` field (`Th_coqc` / `finite_diagnostic` / `Dr` / `Open`, per FOUNDATION §4.1)
is set independently of both of the above — a card can `hold` against the base lens while
still being tiered `Open` if its own source gives no worked case, and the reverse.

## Rule 17 — source-first citation, verbatim

Every card's `source`, `fetched_from_url`, `locator`, and `verbatim` fields exist to satisfy
one standing kernel rule, defined once in `design/FOUNDATION_v0.6_PATCH.md` and enforced in
`kernel/glosa_kernel.py` (`_citation_source_first_errors`, `rule17`/`rule17w`) — restated here
only as a pointer, per the corpus's own one-fact-one-home rule; the rule body lives in
`FOUNDATION`, not here:

> Rule 17 (source-first citation): once a citation card leaves `CANDIDATE` status, its
> `fetched_from_url`, `page_or_locator` (this harvest's `locator` field), `line_or_paragraph`,
> and `exact_passage` (this harvest's `verbatim` field) must be values taken from the actually
> opened source — never reconstructed from memory, never left blank and filled in later from
> recollection. A card missing one of these while still `CANDIDATE` gets a warning
> (`rule17w`); a card past `CANDIDATE` missing one is a hard error (`rule17`).

Practically, for every `kc-*.yaml` card in this harvest that means: the `verbatim` field is a
direct quotation copied from the file/URL named in `source`/`fetched_from_url`, at the
`locator` given — not a paraphrase, and not a passage reconstructed after the fact. The `text`
field is this repo's own restatement for readability; `verbatim` is the check on that
restatement, and is what an independent reviewer re-opens the source to confirm against.

## Public-ness

This directory is already public — the whole repository is CC BY 4.0 (see root `LICENSE`).
Nothing here changes that; this file only documents what is already published. As with any
public-facing file in this corpus, `PUB-ADVERSARIAL-REVIEW`'s leak scan (local usernames,
home-directory paths, private research-stack identifiers such as a Zotero item key or a
Paperless document id) still applies before any regenerated index or render is pushed — see
`design/REPO_SPEC_v0.6_PATCH.md` §2's own note on this point.
