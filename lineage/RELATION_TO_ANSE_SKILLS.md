tier: Dr (specified; independently unreviewed)

# Relation to ANSE.ASIA skills

> Readout, not truth. Each row states what glosa re-derives from the named skill (pattern, not
> literal text — no private text is copied; per-skill visibility is stated because it changes what
> "cite" can legally mean), and where the re-derived mechanism now lives in glosa
> (`design/FOUNDATION_v0.3.md` section, or a `design/REPO_SPEC_v0.3.md` path not yet built).
> Visibility key: **public** = the source itself is a public repo/plugin a stranger can open;
> **private_local** = an internal ANSE.ASIA workspace skill under `~/.claude/skills/`, not
> published — glosa re-derives its *pattern* only, names it, never quotes or vendors its text.

## Summary table

| Skill | Visibility | What glosa re-derives | Status | Where it lives in glosa |
|---|---|---|---|---|
| maker-checker-gate (MIMCG) | private_local | L0–L5 consequence table, MC-01..05, the release state machine | `PRESERVE_FUNCTION` | `FOUNDATION_v0.3.md` §7.1–§7.4 |
| rigorous-diagnosis | private_local | "Don't trust one instrument," plausible-vs-verified register discipline | `PRESERVE_FUNCTION` | `methodology/P8_diagnosis.md` (REPO_SPEC path) |
| skillme | private_local | Two-question intake gate; retained-difference issue framing; `INTERNAL_DATA_AUDIT` review mode | `PRESERVE_FUNCTION` / `EXPAND` | `FOUNDATION_v0.3.md` §2.2 (S1), §7.8 (`review_mode`); `methodology/P2_intake.md` (REPO_SPEC path) |
| doc-ecosystem | private_local | Which documents a project needs and who writes/reads each; decision→outcome→lesson→rule loop | `PRESERVE_FUNCTION` | `design/REPO_SPEC_v0.3.md` root-file tree (`README.md`, `AGENTS.md`, `DECISIONS.md`, `CHANGELOG.md`, `incidents/`) |
| project-onboard | private_local | Mandatory pre-work readiness report, fail-closed | `PRESERVE_FUNCTION` | `FOUNDATION_v0.3.md` §9 (`validate_readiness`); `methodology/P12_readiness.md`, `schema/readiness.schema.json` (REPO_SPEC paths) |
| skill-library (vetting) | private_local | "Any outside source is untrusted until read in full"; lazy-catalog + vet-on-demand discipline | `PRESERVE_FUNCTION` | `methodology/P9_vet_external_input.md` (REPO_SPEC path) |
| academic-presentation | private_local | Claim-ceiling discipline; plain-language register per audience | `PRESERVE_FUNCTION` | `FOUNDATION_v0.3.md` §6.2 (per-genre "Claim ceiling" column); `methodology/P13_genre_router.md` (REPO_SPEC path) |
| grr-epistemic-foundation | private_local (upstream text CC BY 4.0) | Claim Object / Evidence Relation / Warrant Profile *vocabulary pattern* — not literal enum strings | `PRESERVE_FUNCTION` | `FOUNDATION_v0.3.md` §1.2, §3.2 (`claim_type`, `evidence_relation`, `independent_check` field groups) |
| readout_genesis | public (GitHub) | 6-tier ladder (never collapsed); forced/borrowed/Open ledger | `PRESERVE_EXACT` (tier ladder) / `PRESERVE_FUNCTION` (ledger) | `FOUNDATION_v0.3.md` §4.1 (tier table); §3.2 `claim_card.ledger` |
| readout_universe | public (GitHub, MIT) | Lens Law (declare Q/X/R/Φ before touching evidence); "1 claim / 1 row / 1 command / 1 falsifier"; "We do NOT claim" ledger | `PRESERVE_FUNCTION` | `FOUNDATION_v0.3.md` §2.1 (spine lens-in); §3.2 `lens_translation` block, `tested.falsifier` (required, non-empty), `non_claims` |
| information-discrete-math | public (plugin marketplace) | Readout-not-truth as the universal reading stance underlying every glosa artifact — no direct field, a worldview commitment | `PRESERVE_FUNCTION` (underlies, not a schema mechanism) | Every glosa file's own header line (this repo's mandatory `tier: ...` line, per this task's binding rules) |
| zero-readout-certifies (incl. `label_inflation_guard.py`) | public (GitHub, DOI-carrying Coq companion) | Six-way HOLD-discipline boundary pattern; `CLAIM_MATRIX.md`; `check_repo.sh`/`check_version.py`; CITATION/.zenodo/codemeta triple-equality check; AI-assistance disclosure section; the tier-inflation lint pattern | `PRESERVE_EXACT` / `EXPAND` (chair ruling C7) | `FOUNDATION_v0.3.md` §1.2, §3.3 kernel rules 2–3 (Th_coqc/finite_diagnostic require I4/I5 evidence, never I3 alone); `paper/CLAIM_MATRIX.md`, `scripts/check_repo.sh`, `scripts/check_version.py` (REPO_SPEC paths) |

## Per-skill detail

### maker-checker-gate (MIMCG) — private_local

glosa's release discipline is, by explicit design, "the same maker-checker discipline" as this
skill (`design/AGENTS.md` rule 3; `FOUNDATION_v0.3.md` §7.1 "incorporated by reference from the
MIMCG skill for full detail"). glosa re-derives: the L0–L5 consequence-level table mapped onto
glosa's own artifact types (`FOUNDATION_v0.3.md` §7.1, with L3/L5 reconciled this pass against two
independent reviews' finding of an internal contradiction); MC-01 (maker/checker/approver
pairwise-distinct identities, §7.2, kernel rule 5); the Bounded-Judge Law (an untiered verdict is
invalid, §7.3); the canonical release state machine name set
(`Draft → Pending Review → (Revise) → Approved-for-Test → Approved-for-Live → Monitor`, `Rollback`
reachable from any live state, §7.4). No text is quoted from the skill itself; the table shape and
rule names are re-implemented against glosa's own claim-card fields.

### rigorous-diagnosis — private_local

Informs `methodology/P8_diagnosis.md` (not yet built): "don't trust one instrument," and the
discipline of stating plausible-vs-verified language rather than collapsing an observed result
into settled fact. This is a general debugging/diagnosis discipline the skill states is
domain-independent; glosa applies it specifically to claim-card evidence review (a `review_report`
must state its tier explicitly, never imply confidence it does not carry).

### skillme — private_local

Two contributions. (1) The mandatory two-question intake gate before any analysis starts is the
direct pattern behind glosa's S1 stage gate (`FOUNDATION_v0.3.md` §2.2: "Two-question intake
complete" before `READY_FOR_S2`). (2) `review_mode`'s `INTERNAL_DATA_AUDIT` value is explicitly
named in `FOUNDATION_v0.3.md` §7.8 as "skillme's own sixth mode... restored here rather than left
superseded" — the one place this lineage relationship is already stated directly in the design
document itself, reproduced here for the lineage ledger's own completeness.

### doc-ecosystem — private_local

Informs the shape of glosa's own root-file tree (`README.md`, `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`,
`llms.txt`, `DECISIONS.md`, `CHANGELOG.md`, `incidents/INDEX.md` — `design/REPO_SPEC_v0.3.md`
root listing) and the general discipline that a documentation ecosystem must close the loop
decision → outcome → lesson → rule, rather than let any of those four silently go stale. glosa's
`incidents/` directory (append-only, "why this rule exists") and `DECISIONS.md` (mirroring cpg's
`DECISIONS.yaml` lifecycle) are glosa's own instances of this pattern.

### project-onboard — private_local

The mandatory pre-work readiness report, fail-closed, before touching any repo — re-derived as
glosa's own S1-adjacent gate: `methodology/P12_readiness.md` + `schema/readiness.schema.json` +
kernel function `validate_readiness` (`FOUNDATION_v0.3.md` §9). Not yet built (REPO_SPEC path).

### skill-library (vetting) — private_local

"Any outside source is untrusted until read in full" is re-derived as `methodology/P9_vet_
external_input.md` — the same lazy-catalog-then-vet-on-demand posture this skill uses for
external the AI assistant skills, generalized by glosa to any external evidence source a claim card cites.
`glosa-cite-check` (plugin skill, REPO_SPEC path) is the tool-level twin of this discipline.

### academic-presentation — private_local

Contributes the claim-ceiling discipline (never state a stronger conclusion than the evidence in
hand supports) and register-matching for a named audience — re-derived directly into glosa's
per-genre "Claim ceiling" column (`FOUNDATION_v0.3.md` §6.2, e.g. `conceptual`'s ceiling of `Dr`
on propositions, `formal_proof`'s `Th_coqc` only with `independent_check.status==PASSED`).

### grr-epistemic-foundation — private_local skill, upstream text CC BY 4.0

Already named directly in `FOUNDATION_v0.3.md` §1.2's ancestor table: "the *pattern* (typed claim,
typed evidence relation, warrant is multi-axis) — **not** its literal enum strings, independently
re-derived (`claim_type`, §3.2)." Reproduced here because this skill sits at the boundary of
private-local and public: the skill file itself lives under `~/.claude/skills/`, but its content
adapts an upstream GRR-EF (Claim/Evidence/Warrant/Status) structure that is itself CC BY 4.0. glosa
treats it as private_local for citation purposes (no direct link/quote), re-deriving only the
pattern.

### readout_genesis — public

`FOUNDATION_v0.3.md` §1.2 names this ancestor directly: the 6-tier ladder
(`Th_coqc/finite_diagnostic/fit_calibrated/Dr/definition/Open`, never collapsed), the Lens Law "as
the mandatory `lens_translation` block before any Five Question is answered," and (added chair
ruling C7) `label_inflation_guard.py`'s tier-inflation lint pattern, folded into `FOUNDATION_v0.3.md`
§3.3 kernel rules 2–3 rather than kept as a separate check — those two rules already forbid `I3`
alone from licensing `Th_coqc`/`finite_diagnostic`, which is exactly what a tier-inflation lint
would otherwise have to catch after the fact.

### readout_universe — public, MIT

`FOUNDATION_v0.3.md` §1.2: "The 6-tier ladder... Lens Law..." — readout_universe specifically
contributes the `definition`/`fit_calibrated` tier additions and the "1 claim / 1 row / 1
command / 1 falsifier" discipline, re-derived as `claim_card.tested.falsifier` being required and
non-empty, and the "We do NOT claim" ledger pattern re-derived as `claim_card.non_claims`
(required, `minItems 1`).

### information-discrete-math — public (plugin)

Not a schema mechanism — a standing worldview. Readout-not-truth is the default reading stance for
*everything* glosa reads (a benchmark, a user's claim, a tool's output, glosa's own prior output),
per the workspace-wide `EPIS-UNIVERSAL-LENS` rule this repo inherits. Its concrete floor-level
expression inside glosa is mechanical, not narrative: every glosa file, this one included, carries
the mandatory `tier: ...` header line this task's binding rules require, and `FOUNDATION_v0.3.md`
itself opens every section with "readout-not-truth applies to every line below."

### zero-readout-certifies (incl. `label_inflation_guard.py`) — public, DOI-carrying Coq companion

Added this synthesis pass specifically to close a gap: `reviews/COMPLETENESS_CRITIC.md` §2 found
this ancestor's own artifacts (`CLAIM_MATRIX.md`, `scripts/check_repo.sh`, `check_version.py`, the
CITATION.cff/.zenodo.json/codemeta.json triple-consistency check, and an "AI-assistance
disclosure" section) were reused near-verbatim in an earlier draft with **zero lineage tag**
(`FOUNDATION_v0.3.md` §1.2, chair ruling C7). Fixed here and in the design document itself: these
five mechanisms are named `PRESERVE_EXACT`/`EXPAND` — the release/citation-hygiene mechanism is
reused, glosa's own mathematical claims and Coq theorems (glosa has none) are not. `paper/
CLAIM_MATRIX.md`, `scripts/check_repo.sh`, `scripts/check_version.py` (REPO_SPEC paths, not yet
built) are the direct file-level continuations of this lineage; `label_inflation_guard.py`'s
tier-inflation-lint pattern folds into kernel rules 2–3 (§3.3), as noted under readout_genesis
above since the guard itself targets the same tier ladder that repo also contributes.

## What is NOT here

Five private ANSE.ASIA repos are explicitly out of scope for citation or pattern-borrowing under
this task's binding rules: five internal ANSE.ASIA repositories (not named in this public file;
the list lives in a git-ignored local registry). Nothing in this file, or in glosa generally, names, links, or
patterns from those five beyond what is already public knowledge independent of them. Where a
skill above (e.g. `grr-epistemic-foundation`) sits at a private/public boundary, this file states
that explicitly rather than treating "cited in an internal skill" as equivalent to "safe to quote
publicly."
