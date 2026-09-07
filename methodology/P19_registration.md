# P19 — Registration: where new work goes

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction (ruling 2026-09-07, Blackbox Log
> BBL-2026-09-07-205: "ทุกสมการที่เราสร้างให้มาอัพเดท ตรวจสอบจากตรงนี้ก่อน" — every equation we create is checked
> against and updated in Toledo first, and the founder asked that glosa say where new work registers). AI drafted
> this card. Comparison language is same/different/cited only.

## id

`P19`

## Rule

New work is not "done" until it is registered in the one home that owns its kind of fact. One kind, one home;
each home cites the others by id, never restates them (`P0` one-fact-one-home):

| Kind of new work | Home of record (register here first) | How |
|---|---|---|
| An **equation** (new, revised, or reused in a new domain) | **Toledo** — `github.com/morrocwi/toledo`, concept DOI 10.5281/zenodo.22537318 | Look it up in `registry/CANONICAL.json` / `registry/genesis_root.json` under the equivalence criterion (renaming, positive scale, constant substitution). Existing ⇒ cite its code and add an occurrence. New ⇒ register it with a code `<Genesis root>/<D>.<nn>.v<k>`, parents by code to a Readout Genesis root, tier as the source states, origin/status, and a Coq file named by the code — then use the code in the paper. Revised ⇒ bump `.v<k>` with a `LINEAGE.jsonl` event. |
| A **machine check** of an equation (Coq) | Toledo, `coq/canonical/<code>.v` | File name = code; `verify.sh` (Print Assumptions) result recorded on the entry's `coq{}` block. |
| A **paper, note, dataset, software release** | **Zenodo**, as a new version under the work's existing concept DOI (never a new record for the same work), linked `isPartOf` its hub (Human–AI Readout Programme hub 10.5281/zenodo.22308201) | `scripts/zenodo_publish_file.py` (first record) / `scripts/zenodo_new_version.py` (versions); the run is logged under `registry/zenodo_uploads/`; `scripts/zenodo_cluster.py hubs-refresh` and `scripts/zenodo_library_kg.py` afterwards. |
| A **founder ruling or verbatim instruction** | **Blackbox Log** (`blackbox/log/entries.jsonl`, deposited as 10.5281/zenodo.22302518) | `tools/blackbox_log.py add(...)`, `text_verbatim` never paraphrased; private names redacted with a `source_note`. |
| A **decision** (chair, founder, or team) | `DECISIONS.md` / the project's `DECISIONS.yaml` (`P11`) | A row with date, decided_by, statement, refs. |
| An **event** (observation, check, review, publish attempt, dissent) | `logbook.jsonl` (`P11`) | Append-only typed row. |
| A **claim** | a claim card (`P3`) in the project's `cases/` or `records/` | Five questions ⇄ E-A-D; K-state; falsifier. |
| A **literature card** | the project's lit manifest (`P13`) | Rule 17 citation (link + page + line + verbatim). |
| A **method change** (a new rule, gate, or card) | `methodology/` + `CHANGELOG.md` + a `DECISIONS` row | One card = one rule; data tables under `methodology/data/`. |
| A **skill** (reusable AI procedure) | the internal skill library (`~/.claude/skills/`, catalogued) | Internal first; external only after vetting, kept separate. |

Order for a piece of research that carries an equation: Toledo (equation) → claim card (claim) → Zenodo (record) →
Blackbox/DECISIONS/logbook (rulings, decisions, events) → hubs/KG refresh. A paper may cite a Toledo code only after
the code exists; a Toledo entry may cite a paper only by its deposited DOI (rule 17).

## Why / incident

The programme's 40 deposited chapters carried 946 numbered equations; canonicalising them in Toledo (2026-09-06/07)
found the same objects restated many times under different notation, some bundles of unrelated formulas under one
label, and prose propositions typeset as equations. None of that was visible while each paper registered its own
equations locally. The founder's ruling makes Toledo the first stop so an equation is written once, coded once, and
read per domain — the same one-fact-one-home discipline this methodology already applies to decisions (`P11`).

## Inputs → outputs

- **Inputs:** the new artifact and its kind (equation / check / record / ruling / decision / event / claim / card /
  method change / skill).
- **Outputs:** the registration in the home named above, with the id it returns (Toledo code, DOI, BBL id, DECISIONS
  id, logbook row), cited from the artifact itself.

## Gate

Fail-closed, per kind: an equation with no Toledo lookup is not presented as new; a work with no DOI is not cited as
deposited; a ruling with no Blackbox id is not cited as a ruling; a decision with no DECISIONS row is not "done". The
publish gate (`P10`) checks that every equation on a public page carries a Toledo code or an honest "not yet coded".

## Human / AI split

Founder/human: rulings, decisions, publishing approval (`--founder-instructed` on every deposit), root-registry
extensions (a new Genesis-level root is a founder decision, never an AI's). AI: lookups, drafting entries, running the
registration tools, writing the lineage events, reporting counts from the files.

## Disclaimers

Registration is a readout of where a fact is recorded, not a warrant that the fact is true; a Toledo code certifies
identity and lineage of an equation, a Coq "Closed under the global context" certifies consistency of a finite model,
neither certifies empirical truth (tier ledger, `P6`).

## NC pairs

Registered ≠ validated · coded ≠ derived · deposited ≠ reviewed · logged ≠ decided (`P11`).

## Not-do

- Do not register the same equation in a paper's private table and in Toledo with different codes — Toledo's code is
  the one cited; older private registries are superseded for public codes.
- Do not create a new Zenodo record for a new version of an existing work.
- Do not invent a root code, a tier, or a parent to make registration succeed — leave it `untagged` / `unverified` /
  `HRP-X` with a drift note and say so.
- Do not paraphrase a founder ruling into the Blackbox Log.

## Tier

Dr — specified from the founder ruling and the Toledo v1.0.0 build; independently unreviewed.
