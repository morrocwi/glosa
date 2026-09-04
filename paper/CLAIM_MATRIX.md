# Claim Matrix — `paper/main_th.md` / `paper/main_en.md`

> tier: Dr (specified; independently unreviewed) · k_state: K0 for every row · every
> `evidence_relations` entry in every underlying claim card is `independence_class: I0`
> (same-session self-read — "not a `tested:` entry at all" per `design/FOUNDATION_v0.5.md` §4.2's
> own table; cannot raise `tier` or `k_state`). This table is a print-space compression of the full
> claim card (`shape: full`); it is not the record of correctness itself — field-presence here is
> mechanically checkable (verified in this session, see `paper/README.md` §Evaluation), the
> content's correctness is what an independent check (Q5) exists for and has not yet run.
>
> Format follows `design/FOUNDATION_v0.5.md` §3.2, PRESERVE_EXACT lineage from
> `zero-readout-certifies` (chair ruling C7). Full card: `paper/claims/<ID>.yaml` — every field, not
> just this compression. Ten claims below (C101–C110); every `\claimref{Cnnn}` in
> `paper/latex/main.tex` resolves to exactly one row.

| ID | Informal statement | Evidence / source | Tier | Produced by | Responsible | k_state | Independence |
|---|---|---|---|---|---|---|---|
| **C101** | A claim card answering the five founder questions is a usable claim-level instantiation of the Readout Condition's E-A-D norm. | `design/FOUNDATION_v0.5.md` §3, §3.1; `schema/claim_card.schema.json` | Dr | joint | human | K0 | I0 |
| **C102** | The Independence Ladder I0–I5, bound into the kernel gate rules, prevents a solo AI session from reaching K2 on its own. | `design/FOUNDATION_v0.5.md` §4.2, §3.3 rule 4; `schema/claim_card.schema.json` allOf rule 4 (`jsonschema` Draft7Validator run, this session — see README) | Dr | joint | human | K0 | I0 |
| **C103** | The genre router (§6.3b) is an ordered, computable procedure yielding one genre id (or `MIXED_GENRE`) from named claim-card fields, not free editorial judgment. | `design/FOUNDATION_v0.5.md` §6.3b; `cases/worked-example-cat.md` Step 6 | Dr | joint | human | K0 | I0 |
| **C104** | The neighbour table (~30 tools) compares glosa's claim-card mechanism using same/different/cited language only; no row claims priority. | `design/S13_neighbour-table.md` (full table, every row) | Dr | joint | human | K0 | I0 |
| **C105** | The cat worked example demonstrates the spine's full round trip end to end, arriving at an honest LRS gate FAIL rather than a fabricated PASS. | `cases/worked-example-cat.md` (full document) | Dr | joint | human | K0 | I0 |
| **C106** | The "Blackbox Note: how this work was made" appendix is a mandatory hard gate for every genre, not a suggestion. | `design/FOUNDATION_v0.5.md` §2.4, §6.4 | Dr | joint | human | K0 | I0 |
| **C107** | The disclaimer catalogue (§5) yields a genre-computable mandatory disclaimer set rather than leaving disclosure to an author's memory. | `design/FOUNDATION_v0.5.md` §5, §6.4; `paper/latex/disclaimers.tex` (this paper's own rendering) | Dr | joint | human | K0 | I0 |
| **C108** | glosa's own LaTeX template compiles under `pdflatex`+`bibtex` to a PDF with zero forbidden words. | `templates/paper/arxiv-onecol/`; `paper/latex/main.pdf` (compiled this session — exact log in README) | **finite_diagnostic** (the compile+grep result itself); Dr (the template's suitability) | joint | human | K0 | I0 self-check; **I4** for the mechanical compile/grep result itself |
| **C109** | The LRS gate (S14 §5.5/5.6) refuses to pass a lit-review citing zero fetched-and-verified sources — shown, not just specified, by the cat example. | `design/S14_literature-review-system.md`; `cases/worked-example-cat.md` Step 4 | Dr | joint | human | K0 | I0 |
| **C110** | This paper itself sits at K0, not K1, because no I2+ check has run on `FOUNDATION_v0.5.md` or on this paper — a reflexive application of glosa's own rule to itself. | `design/FOUNDATION_v0.5.md` §4.2, §12 | Dr | joint | human | K0 | I0 |

## Five-questions detail (per claim)

Every row's `seen` / `separates` / `ai_filled` / `assumed` / `tested` detail is written out in full
in its own claim card (`paper/claims/<ID>.yaml`, `five_questions` block) rather than duplicated
here as a second, driftable copy (one-fact-one-home, `design/FOUNDATION_v0.5.md` §8). In summary,
identically across all ten cards: `seen.access_model` = "direct file read within this repository,
same session, 2026-09-04"; `ai_filled` is the full six-key shape, every key non-empty (see
`paper/README.md` for what that discloses in aggregate); `tested.evidence_relations` carries
exactly one entry, `independence_class: I0`, per card — a same-session self-read, which by
`design/FOUNDATION_v0.5.md` §4.2's own table "is not a `tested:` entry at all" for the purpose of
raising tier or k_state, and is recorded honestly as such (`D-INDEPENDENCE` fires on every row).

## What this table does not claim

- Does not claim any row has passed an independent (I2+) check — `independent_check.status: NONE`
  on every underlying card.
- Does not claim `schema/claim_card.schema.json`'s `allOf` rules are the whole of
  `design/FOUNDATION_v0.5.md` §3.3 — the schema's own header names rules 5, 6, 8, and the 90-day
  bounded-exception arithmetic of rules 4/9 as kernel-only, not schema-expressible.
- Does not claim `kernel/`'s `gate_release`/`route_genre`/`compute_disclaimers` functions have been
  run against these cards — only `jsonschema` structural validation was run this session (see
  `paper/README.md` §Evaluation for the exact command and result).
