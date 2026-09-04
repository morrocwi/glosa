# sources/ — supporting papers, not truth

> **Tier: Dr.** These files are supporting sources glosa cites and reads from. Readout-not-truth
> applies to them exactly as it applies to any other input glosa processes (CLAUDE.md gate rule
> 1): a source being kept here, cited, or even DOI-verified does not make its content true — it
> makes the citation traceable. `NC-18` Source existence ≠ Claim support and `NC-73` Certification
> ≠ Warrant (`design/S9_non-collapse-table.md`) both apply directly to this directory's own
> contents.

## What is here

| File | Supports | DOI | License | Status |
|---|---|---|---|---|
| `WRITTEN_BY_AI_STILL_TRUE_v6.txt` / `.pdf` | The three pillars (ontology/epistemology/methodology), the non-collapse table rows `NC-65`..`NC-73`, the RPE reviewer check, the disclosure-challenge wording template — `design/S15_pillars-ontology-epistemology-methodology.md`, `design/S9_non-collapse-table.md` | `10.5281/zenodo.22301202` (concept DOI `10.5281/zenodo.22301201`), https://zenodo.org/record/22301202 | CC BY 4.0 (per `citation_cards/ZENODO_written-by-ai-v6.json`) | **PRESENT** — `sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt`, `sources/Written_by_AI_Still_True_v6.pdf`; citation card `citation_cards/CIT-written-by-ai-v6.yaml` |
| `READOUT_CONDITION_2026-08.txt` / `The_Readout_Condition_Full_Paper_Elevated.pdf` | The core epistemic engine glosa's claim card operationalizes: Existence–Attribution–Disclosure (E-A-D), the typed provenance DAG, the identification ladder, defeater routing, the silent-lift check (`FOUNDATION_v0.5.md` §3.1's Five-Questions crosswalk cites this paper directly) | `10.5281/zenodo.22301318` (concept DOI `10.5281/zenodo.22301317`), https://zenodo.org/record/22301318 | CC BY 4.0 (per `citation_cards/ZENODO_readout-condition.json`) | **PRESENT** — `sources/READOUT_CONDITION_2026-08.txt`, `sources/The_Readout_Condition_Full_Paper_Elevated.pdf` |
| `CPRMH_v12` (Coordinated Plaque Remodeling Modalities) | Health-domain supporting source, kept for lineage only — not cited as a glosa mechanism source, not a clinical recommendation | `10.5281/zenodo.22301361` (concept DOI `10.5281/zenodo.22301360`) | CC BY 4.0 (per `citation_cards/ZENODO_cprmh-v12.json`) | **PRESENT** — `sources/CPRMH_arxiv_twocolumn_v12_core_collapse.pdf`, `sources/CPRMH_v12.txt`; founder-authored |
| `STANDALONE_SCHOLAR_v3.txt` | The macro scholar-career architecture glosa's K-state ladder, DVP mechanics, Human Mastery Gate, and SCRAM condition are cited from as a dependency (`lineage/RELATION_TO_STANDALONE_SCHOLAR.md`) | `10.5281/zenodo.22163849` (per `FOUNDATION_v0.5.md` §1.2's existing citation — not independently re-verified in this pass) | Open — no `ZENODO_*.json` record for this source sits in `citation_cards/`, so the license is not independently confirmed here; carried forward from `FOUNDATION_v0.5.md`'s existing citation only | **NOT_PRESENT** (referenced by DOI/URL only) — no file under this path in this repo; working copy lives at `cpg_research_journal/research/rigour-without-infrastructure/sources/STANDALONE_SCHOLAR_v3.txt` |
| `ai-native-scholarship-skill-v1.0.0/` | The shipped skill implementing Standalone Scholar's invariants (anchor-preservation contract, conversion-first strategy) — cited by the Project Advisor role design (S12) | No DOI — a skill package, not a paper | Open — no DOI and no `ZENODO_*.json` record exists for this source, so no license claim is made here | **NOT_PRESENT** (referenced by DOI/URL only — no DOI exists at all; cited by name/path only) — no directory under this path in this repo; working copy lives at `cpg_research_journal/research/rigour-without-infrastructure/sources/ai-native-scholarship-skill-v1.0.0/` |

## The rule

Every file in this directory, present or not, is a **supporting source**, never the ground of
truth for any glosa claim. A claim card that cites one of these sources still carries its own
`tier`, `independence_class`, and `tested.falsifier` — the source's own DOI, license, or presence
status never substitutes for glosa's own independent-check gate (`FOUNDATION_v0.5.md` §7.1,
`NC-34` No independent check⇒No K2 / No independent check⇒No release).

**Status words used in the table above:**
- **PRESENT** — the file (or directory) physically sits under this path in this repo, verified by
  `git ls-files sources/` and a filesystem listing at the time this row was last checked.
- **NOT_PRESENT (referenced by DOI/URL only)** — no copy of the file sits in this repo; the source
  is cited only via its DOI/URL (or, for the skill package, by name/path) and its working copy, if
  any, lives elsewhere (`cpg_research_journal`). A `NOT_PRESENT` row is not a blocker on any glosa
  release gate by itself — it only means this specific public copy has not been placed under this
  path. The DOI/URL citation remains valid regardless of whether the file itself sits here.

## Open questions for the founder

1. Should `STANDALONE_SCHOLAR_v3.txt` and the `ai-native-scholarship-skill-v1.0.0/` package be
   physically copied into this public repo's `sources/`, or should glosa continue to cite them
   only by DOI/URL (Standalone Scholar) or name/path (the skill package) and keep the working
   copies private to `cpg_research_journal`?
2. `STANDALONE_SCHOLAR_v3.txt`'s license has not been independently re-confirmed against a live
   Zenodo record — worth a direct re-check the same way the DOIs for the `PRESENT` rows above were
   confirmed (each now has a `citation_cards/ZENODO_*.json` record).
