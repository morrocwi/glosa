tier: Dr (specified; independently unreviewed)

# Tuned-on-test internal eval — 2026-06-22 (anonymized narrative)

## Source
the internal survey (local, not public) §C, cited as `an internal RAG product repo docs/AUDIT_2026-06-22_internal-
eval.md (PRIVATE local git only)`: "tuned-on-test — abstention thresholds calibrated on the same
25 labeled queries then scored; scorer vocabulary edited to whitelist a failing probe; 'KPI verbs
PASS/ELITE/=0 are tuned-on-test point estimates.'" **The source repo and audit file are private**;
per this repo's own rule (private ANSE.ASIA repos are re-derived as patterns, never linked or
quoted, `D-DERIVED-PATTERNS`) and per the task's own instruction, this entry is written as an
anonymized narrative with no repository link, path, or internal identifier reproduced.

## What happened [tier: finite_diagnostic (documented)]
An internal evaluation of a retrieval/answering system produced KPI numbers presented with strong
verbs — `PASS`, `ELITE`, a headline metric reported as exactly `0`. A self-audit of the same
evaluation found two mechanisms behind those numbers: (1) the system's own abstention thresholds
had been calibrated using the same small labeled query set (25 queries) that was then used to
*score* the system — the test set and the tuning set were the same data, so the reported pass rate
measured how well the thresholds had been fit to that data, not general performance; (2) the
scorer's own vocabulary list had been edited, during development, to explicitly whitelist a probe
that had previously been failing — meaning the "PASS" partly reflected a change to the pass
criterion, not only a change to the system. The self-audit's own conclusion, tiered honestly, was
that the KPI verbs were "tuned-on-test point estimates," not general claims.

## What rule it produced [tier: Dr]
`NC-06` correct output ≠ true theory, applied to KPI reporting specifically: a threshold or
scoring rule fit on the same data used to evaluate it cannot license the strong verbs (`PASS`,
`ELITE`, an exact `=0`) that imply the result would hold on unseen data. Generalized glosa rule,
tying into `overclaim-tendency-review`'s own fix (below): a `claim_card.tier` of anything above
`Dr` for a quantitative result requires that the calibration set and the scoring set be disjoint,
and `scope.evidence_scope` must name which set was used for which purpose — a card that cannot
answer "was the threshold fit on data disjoint from the scored set?" defaults to `Dr` regardless of
how confident the wording elsewhere reads. Editing a scorer's pass criteria after seeing a specific
failure, without re-running the full set under the new criteria and disclosing the change, is a
`silent_lift` in the sense of `NC-15` — the represented dependency set ("this passes the standing
scorer") silently diverged from the actual one ("this passes a scorer edited to accommodate it").

## What would have caught it earlier
Two separate, mechanically-checkable preconditions before any KPI verb (`PASS`/`ELITE`/`=0`) is
emitted: (1) a recorded, timestamped split between the tuning/calibration set and the scored set,
with the kernel refusing to emit anything above `Dr` when they overlap; (2) a diff/version record
of the scorer's own pass-criteria across the evaluation's runs, so a criteria edit made mid-stream
is visible in the same report as the KPI it produced, rather than only visible to whoever reads the
scorer's source code directly. Both are instances of the general independent-check requirement
(§7.1–7.2): an evaluation that both defines its own passing criteria and reports its own pass rate,
with no independent route checking either, is a maker self-certifying (`NC-30`).

## Non-collapse pairs this incident illustrates
- `NC-06` correct output ≠ true theory.
- `NC-15` represented ≠ actual essential dependency set (Silent Lift), applied to a scorer's own
  criteria as a dependency of the reported KPI.
- `NC-30` same-model/same-team self-approval ≠ review — the same effort defined, tuned, and scored
  its own success criterion with no independent route.
