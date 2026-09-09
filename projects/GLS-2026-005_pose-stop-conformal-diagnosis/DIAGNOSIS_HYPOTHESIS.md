# P8 diagnosis record — why the coverage-qualified certificate never fired on real data

Project: GLS-2026-005. External repo: https://github.com/morrocwi/task-conditioned-6d-pose-stop
(commits fd65d27, c9a1dc8). Recorded per `methodology/P08_diagnosis.md`'s five disciplines.
tier for this whole record: **Dr** (a plausible, internally-consistent diagnosis; disciplines 2
and 4 below are explicitly NOT yet applied — do not read this as `finite_diagnostic`).

## Symptom

Two independent real-sensor runs (BOP LM-O, real ICP backend, adversarially reviewed, both
released) found `certificate_rate = 0.0` — `k_C < k_E` on 0/40 held-out episodes, every task, in
both runs. Run 2 changed task tolerances (re-derived from TRAIN, 2.6–2.8× wider on translation)
and this raised the *estimator's own* completion rate substantially but left the certificate's
completion rate at exactly 0.0 in both runs — ruling out "tolerances too tight" as the cause.

## Discipline 1 — a second instrument agrees

The calibrated conformal quantile is recorded in two independently-produced places that agree:
`lab/results/real-bop-lmo-2026-09-09-run2/lab_results.json` (`"q": 2.0007944062384855`,
`"calibration_quantile_rank": 37`) and `RESULT.md`'s own prose (`q ≈ 2.0008`). A third,
independent hand-computation done in this session (`python3 -c "import math;
print(math.exp(2.0007944062384855))"` → `7.3949...`) confirms the multiplicative reading:
`exp(q) ≈ 7.4`. `calibration_quantile_rank = 37` also matches the formula in
`theory/FORMALIZATION_v1.md` C8 exactly: `r_α = ceil((n+1)(1−α)) = ceil(41×0.9) = ceil(36.9) = 37`
for `n=40`, `α=0.1`. Three independently-obtained numbers agree. **Discipline 1: applied.**

## The named mechanism (hypothesis, not yet a finding)

`b_{k,i} = exp(log s_{k,i} + q_α) − δ_i` (C9): the conformal correction `q_α` acts as a
**multiplicative inflation of ~7.4×** on whatever error-scale the observable-feature predictor
`s_{k,i}` (C6) outputs, before the envelope is compared against any task tolerance. Because
`q_α`'s magnitude comes from `r_α = ceil((n+1)(1−α)) = 37` of `n=40` — near the *top* of the
calibration-episode ranking — and because the nonconformity score `A_j` (C7) is a **max over 15
stages × 6 coordinates** for each calibration episode, the calibration set is effectively being
asked for simultaneous coverage across 90 (stage, coordinate) cells per episode, not one. This is
the textbook conservativeness of max-aggregated (Bonferroni-like) simultaneous coverage in split
conformal prediction, not a bug in the arithmetic — but its *magnitude* here (7.4×) is large enough
that no realistic per-task tolerance loosening moves the certificate, which is exactly what run 2
observed.

**Falsifiable prediction:** if the whole-trajectory max-aggregation (C7) is the dominant driver of
envelope width — rather than the observable-feature predictor `s_{k,i}` itself being
uninformative — then re-deriving `q_α` from a **less conservative aggregation** (e.g. per-stage
calibration using only calibration episodes' scores at the *specific* stage being evaluated,
instead of the max across all 15 stages, or a stage-indexed conformal band) on the SAME
calibration data should shrink `q_α` substantially, and the certificate rate should rise above 0%
on the SAME test episodes without touching task tolerances again.

**Discipline 2 (test the prediction) — NOT YET APPLIED.** No experiment has been run with an
alternative aggregation. This is the concrete next step, not a completed diagnosis.

**Discipline 3 (real conditions, not a proxy) — partially applies to what exists so far.** Both
runs used the real BOP-LMO depth data and the real ICP backend end to end; the diagnosis above is
computed from those runs' own real committed numbers, not a synthetic re-creation. The *proposed*
next experiment (discipline 2) would need to reuse the identical real calibration/test episodes to
count as the same access event.

**Discipline 4 (re-verification by a different identity) — NOT YET APPLIED.** This diagnosis was
authored by the same chair session that read the run 2 results; per P08's gate, it may not back a
claim card or advance any status until a materially separate pass re-derives `exp(q)≈7.4` and the
`r_α=37/40` arithmetic independently and checks the aggregation argument for a hole (e.g. whether
per-stage calibration would itself require a different, and non-trivial, correction for testing
multiple stages sequentially — the "peeking" problem in sequential/anytime-valid conformal
prediction is a real, known difficulty this hypothesis does not yet address).

**Discipline 5 (tier per number) — applied above and here:** the `q≈2.0008`/`exp(q)≈7.4`/`r_α=37`
numbers are `finite_diagnostic` (reproduced from a named, committed source, cross-checked by hand).
The causal story ("max-aggregation is the dominant driver, not the feature predictor") is `Dr` —
plausible, mechanically consistent with the numbers, but not yet tested against its own prediction.

## What "elevating the work" means from here, honestly

This diagnosis converts an unexplained double-negative result into one concrete, falsifiable next
experiment (stage-restricted or sequentially-valid conformal calibration on the identical BOP-LMO
data) rather than a vaguer "try tuning something." It does **not** itself constitute progress
toward H2–H4 in `RESEARCH_QUESTION.md` — those remain unsupported until the next experiment (or a
different one) is actually run and, per this project's own culture, independently reviewed before
any release claims it.

## Founder-visible next step (not yet authorized to run)

Build and run a per-stage (or sequentially-valid) conformal variant of C7–C9 on the same TRAIN/
CALIBRATION/TEST split used in both prior runs, predeclare it the same way run 2 did (frozen
config committed before final test is opened), and report the result — support, refutation, or a
new failure mode — with the same honesty as both runs so far. This is scoped as a THIRD real-data
cycle, not a retroactive edit of runs 1–2.

## Revision, 2026-09-09 — discipline 2 applied analytically, naive fix refuted before running it

Founder instruction: "ใช้ glosa หาปัญหาให้เจอแล้วออกแบบการแก้ปัญหา ด้วยสายธาร toledo สร้างนวัตกรรมให้สำเร็จ"
(use glosa to find the problem, design the fix via the Toledo river, make the innovation succeed).

Before spending a third real-data cycle on the naive "per-stage calibration instead of a joint max
over 15 stages" idea proposed above, its validity was checked analytically first (P08 discipline 2,
applied as a computed prediction, not a code run): a per-stage fix that still gives a valid
whole-trajectory guarantee needs a Bonferroni correction (union bound) across the K checkpoint
stages, i.e. each stage calibrated at level `alpha/K`, not `alpha`. With the SAME `n=40` calibration
episodes used in both prior runs:

```
r_{alpha/K} = ceil((n+1)(1-alpha/K))   for n=40, alpha=0.1
K=15 (every ICP iteration):  r = 41 > n=40  ->  q = +infinity at EVERY stage, immediately.
K=4  (4 checkpoints):        r = 40 = n     ->  feasible (q = worst calibration score).
K=5  (5 checkpoints):        r = 41 > n=40  ->  infeasible again.
```

**Finding: the original per-stage idea, applied naively at every one of the 15 ICP iterations, is
provably infeasible with only 40 calibration episodes** — it does not need to be run to know it
would fail-close to `+infinity` everywhere, which is a DIFFERENT and more mechanical failure mode
than either prior run's, not a fix. This refutes the naive form of the hypothesis before spending a
third real-data cycle on it — exactly what P08 discipline 2 is for.

**Revised, feasible hypothesis:** restrict certificate checks to a small number of predeclared
checkpoint stages (`K' <= 4` with this calibration sample size, e.g. stages `{4, 8, 12, 15}` or
similar, chosen before seeing any final-test result), each independently calibrated at
`alpha/K'` via the same split-conformal construction (C7–C9) but with the nonconformity score
maxed over the 6 pose coordinates ONLY, not over stages. By the union bound (Boole's inequality),
this keeps the same overall whole-trajectory coverage guarantee `>= 1-alpha`, while removing the
15-way stage-aggregation term that produced the ~7.4x inflation on both prior runs. Whether the
resulting `q_{alpha/K'}` values are actually smaller than the joint `q~2.0008` in practice is now a
genuinely open, feasible, and worth-running empirical question — unlike the un-restricted version.

This equation family (base split-conformal quantile C7-C9, and the new Bonferroni-corrected
multi-checkpoint variant) is being registered in Toledo (`~/ANSE.ASIA/toledo`,
`registry/proposals/conformal_stopping_family.json`) per the workspace's standing Toledo-first
rule, before being implemented in the pose-stop repo's code — this closes a retroactive gap (the
original C7-C9 machinery was implemented and used in that repo before ever being registered).

## Toledo registration status, 2026-09-09

`registry/proposals/conformal_stopping_family.json` (3 objects) written in Toledo, per the
Toledo-first rule: PROP-CONF-01 (base split-conformal quantile, retroactive), PROP-CONF-02 (the
whole-trajectory max-aggregated nonconformity score, retroactive), PROP-CONF-03 (the new
Bonferroni-corrected multi-checkpoint variant). PROP-CONF-03's core union-bound argument is
machine-checked: `coq/canonical/PROP_CONF_03_union_bound.v`, two theorems
(`finite_union_bound`, `bonferroni_checkpoints`), both `Print Assumptions` = "Closed under the
global context" (axiom-free, over Q).

**Merge into CANONICAL.json blocked, correctly, by Toledo's own orphan check**: PROP-CONF-01 is a
genuinely new mathematical primitive (split-conformal prediction) with no honest parent anywhere
in Toledo's existing roots (D/Z/Q/R number ladder, L_R spectral family, A2 fold engine,
causal-memory family, Theta/CMC) — forcing a parent link would be dishonest. This is the same
situation CMC was in before its founder ruling made it a standalone root-extension. Filed for the
founder: "FOUNDER: rule on whether split-conformal prediction becomes a new Toledo root" (workspace
todolist). The proposal file and the Coq witness remain staged, correct, and ready to merge the moment
this is settled — nothing was forced into the registry to work around the block.
