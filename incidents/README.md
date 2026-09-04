tier: Dr (specified; independently unreviewed)

# Incident library

One incident = one file. Every file exists because it produced a rule that now lives somewhere
else — a claim-card field, a kernel gate, a disclaimer id (`§5` of `design/FOUNDATION_v0.5.md`), a
non-collapse pair (Appendix A), or a protocol card in `methodology/`. This directory is the
**evidence trail for why the rule exists**, not a second home for the rule itself (one-fact-one-
home, `design/FOUNDATION_v0.5.md` §8): if a rule changes, edit its schema/gate/protocol file, not
the incident file that motivated it.

## What is and is not in scope

Every incident below is documented **only** from `cpg_research_journal/research/rigour-without-
infrastructure/surveys/SURVEY_2026-09-04.md`, the companion `HANDOFF_2026-09-04_ultracode-
foundation-meeting.md`, and — where the survey/handoff cite a private-repo memory as their own
source — the operator's own private incident memory named in that citation. No detail below is
invented to fill a gap; where the source material does not carry a fact (an exact date, a
reproducible number, a name), the file says so and marks the field `Open` rather than guessing.
Two of the nine incidents point at **private** repositories (`an internal RAG product repo`,
`arayaweddingplanner.com` deploy tooling); those two are written as **anonymized narratives** —
the mechanism and the rule are stated in full, the private repo path/commit/URL is not, per the
task's own instruction for the tuned-on-test case and per this repo's standing rule that private
ANSE.ASIA repos are re-derived as patterns, never linked or quoted verbatim (`D-DERIVED-PATTERNS`).

## Tier discipline used in every file

Each file separates two different things that must never be collapsed into one tier (`NC-11`,
Appendix A):
- **The event itself** — what was observed happening, on a stated date, in a stated
  system — is tiered `finite_diagnostic (documented)`: a finite, dated, reproducible-from-the-
  record fact, not a machine-checked proof and not a general theory.
- **The lesson/rule extracted from it** — the general claim "this class of failure recurs, so we
  now require X" — is tiered `Dr`: a declared human–AI narrative synthesis, not itself
  independently re-verified across other systems. A rule sitting at `Dr` can still be **mandatory**
  (a gate can require a disclaimer or a check regardless of the rule's own evidentiary tier) —
  tier and bindingness are separate axes, matching `NC-02`/`NC-03`.

## Format every incident file follows

```
tier: Dr (specified; independently unreviewed)   # file-level header, per the repo's binding rule

# <short name> — <date or "date not in source, Open">

## Source
Which of SURVEY_2026-09-04.md / HANDOFF...md / a named private memory this is drawn from.

## What happened  [tier: finite_diagnostic (documented)]
The event, as documented — system, date, mechanism, what was actually observed.

## What rule it produced  [tier: Dr]
The named P-card / NC id / disclaimer id / gate this incident is now the evidence for.

## What would have caught it earlier
The concrete check, gate, or disclaimer — if it existed at the time — that would have surfaced
the problem before it became live/public/repeated.

## Non-collapse pairs this incident illustrates
Appendix A ids, where applicable.
```

## Index

| # | File | Date | System | Rule produced |
|---|---|---|---|---|
| 1 | `2026-08-01_check-docs-silent-pass.md` | 2026-08-01 | doc-ecosystem `check_docs.mjs` | `NC-26` "not checked" ≠ "checked, nothing found"; a gate must fail loud when its own precondition (a baseline) is missing, never print a pass |
| 2 | `2026-07-24_ttfb-single-instrument.md` | 2026-07-24 | arayaweddingplanner.com performance diagnosis | Never trust one instrument for a load-bearing measurement (`rigorous-diagnosis`); first conclusion = hypothesis, not verdict |
| 3 | `2026-06-22_tuned-on-test-internal-eval.md` (anonymized) | 2026-06-22 | private internal-eval audit | `NC-06` correct output ≠ true theory; KPI verbs (`PASS`/`ELITE`/`=0`) tuned on the same data they are scored against are point estimates, not claims |
| 4 | `2026-07-31_toon-format-accuracy-overclaim.md` | 2026-07-31 | `toon-format` skill vetting | `skill-library` VETTING_PROTOCOL: an upstream project's own benchmark number is not evidence until independently re-run; a claim can be `finite_diagnostic` on one axis and `Open` on another |
| 5 | `2026-08-08_rubygems-skillme-rm-rf.md` | 2026-08-08 | rubygems package named `skillme` | External-package name collision + an uninstall hook is an attack surface; vet the artifact, never the name |
| 6 | `2026-08-03_readout-universe-license-leak.md` | 2026-08-03 | `readout_universe` public GitHub repo | `PUB-ADVERSARIAL-REVIEW`'s origin incident: a stack of prior polish/quality passes never caught what the first *adversarially framed* pass caught on its first run |
| 7 | `2026-08-09_hosting-vendor-ip-ban.md` | 2026-08-09 | <hosting-vendor> shared hosting (two client sites) | Never retry live-host auth against unverified credentials; one shared-server ban has a blast radius wider than the one site being touched |
| 8 | `date-not-in-source_atomic-swap-plugin-deploy.md` (anonymized) | not stated in SURVEY/HANDOFF (sourced from a private operational incident memory the founder's own request named) | private WordPress plugin-deploy tooling | Multi-file live deploys need an atomic directory-rename swap, never a direct multi-file mirror onto a live, traffic-serving path |
| 9 | `2026-06-30_ai-overclaim-x6-one-session.md` | 2026-06-30 | AI-authored docs/KPIs in one working session | `NC-06`; write → adversarial review → strip overclaim → commit is not optional even on the AI's own fresh output |

## How this feeds the rest of glosa

An incident file may be cited as `citation_card.identifier.kind: OTHER_STABLE` (pointing at this
file's path) when a `claim_card.assumed[]` entry or a `review_report` needs to explain *why* a
particular check exists. It is never itself cited as evidence *for* a claim under study — it is
evidence for a **methodology rule**, a different claim type (`FORMAL`/`DECISION` about the process,
not `EMPIRICAL` about the world).
