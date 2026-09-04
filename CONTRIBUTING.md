# Contributing to glosa

Thank you for your interest. Please read this before opening an issue or
pull request — the discipline below is not a formality, it is the
methodology this repo itself is about.

## Before anything else

- Read `AGENTS.md` (also mirrored, identically, in `CLAUDE.md` and
  `GEMINI.md`) and `design/FOUNDATION_v0.5.md` §2–§3. If a contribution does
  not fit the claim-card / tier discipline described there, say so in the
  issue rather than working around it silently.
- Everything in this repo is a readout, not truth. Tag the tier of any
  claim you add or change (`Th_coqc` / `finite_diagnostic` / `fit_calibrated`
  / `Dr` / `definition` / `Open`).

## Authorship

Yaoharee Lahtee (ORCID 0009-0005-3861-0626) is the sole author of the
methodology and its claims — ideas and direction are the founder's. AI
assistance used in drafting is disclosed in the work itself (Blackbox Notes,
`ai_filled` disclosure fields) and is never listed as an author, co-author,
or contributor-with-authorship-standing in `CITATION.cff`, `.zenodo.json`,
or any paper byline. A pull request that adds an AI system, vendor, or
model name to an authorship field will be declined.

## What we accept

- Corrections to schema/methodology inconsistencies, with a specific file
  and line referenced.
- Additional claim cards / case studies that follow the existing schema
  (`schema/claim_card.schema.json`) and carry honest tiers.
- Documentation fixes, translation-as-rewrite (not machine translation) for
  Thai content, typo fixes.
- Bug reports and fixes for `scripts/` and `cli/`.

## What we do not accept

- Language claiming or implying priority (see the priority-language list enforced by scripts/check_forbidden_words.sh)
  outside a clearly
  historical mention in `design/`/`lineage/`. Comparison to other work is
  always same/different/cited, never a priority claim.
- Proposals to seek external/institutional validation (peer review,
  outside-expert sign-off, publication venue prestige) as what makes a
  claim legitimate. That axis is rejected in this repo by design — see
  `CLAIM_BOUNDARY.md`. (Legal/regulatory requirements are a separate axis
  and are not affected by this.)
- Content that names a private individual by name where a role would do,
  or that makes an unverifiable negative/accusatory claim about a named
  person, family, or organization.
- Edits to `blackbox/*_DRAFT.md` files that alter or translate the
  founder's verbatim lines in place. Draft dialogue records are append-only
  and verbatim; curation into a public Blackbox Note appendix is a separate,
  reviewed step (`methodology/P15_blackbox_note.md`).

## How to contribute

1. Open an issue describing the change and which file(s) it touches.
2. Fork, branch, make the change. Run the mechanical gates locally before
   opening a PR:
   ```
   bash scripts/check_repo.sh
   bash scripts/check_forbidden_words.sh
   bash scripts/check_leak.sh
   python3 scripts/check_version.py
   ```
3. Open a PR against `main` (or the active `design/*` branch if the
   maintainers say so). CI must be green.
4. A maintainer who did not author the change reviews it (maker ≠ checker —
   see `AGENTS.md` rule 3 and the `maker-checker-gate` discipline). Do not
   ask the same author to also approve their own PR.
5. Squash or rebase merges only, once approved. No direct pushes to `main`.

## Reporting a security or privacy issue

Do not open a public issue for a suspected leak (a real credential, a real
private path, a real personal detail). See `SECURITY.md`.

## Code of conduct

See `CODE_OF_CONDUCT.md`.
