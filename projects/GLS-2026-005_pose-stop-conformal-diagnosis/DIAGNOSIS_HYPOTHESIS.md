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

## P08 discipline 2 (test the prediction) — APPLIED, 2026-09-09, prediction REFUTED

The third real-data cycle authorized above was run:
`task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run3/` (frozen predeclaration
commit `681c710`, evaluator invocation 2026-09-09T14:32:49+07:00, result commit `a9a9a6a`). New
code path `lab/multicheckpoint.py` + `cqts/safety.py`'s `safe_multi_checkpoint_quantiles` /
`bonferroni_feasible_max_checkpoints` / `bonferroni_checkpoint_alpha`, additive alongside the
unmodified whole-trajectory construction used by runs 1-2. Predeclared K'=4, checkpoints=
`{4, 8, 12, 15}` (the largest feasible value per the arithmetic above), reusing run2's identical
BOP-LMO data/split/ICP backend and TRAIN-derived tolerances unchanged, isolating the
certificate-construction method as the only varied factor.

**Outcome: the falsifiable prediction is REFUTED.** Per-checkpoint quantiles came out LARGER, not
smaller, than the joint `q≈2.0008`:

| checkpoint k | q_{alpha/K'} | vs joint q≈2.0008 |
|---:|---:|---|
| 4  | 2.0854 | +4.3% |
| 8  | 2.1715 | +8.5% |
| 12 | 2.1636 | +8.1% |
| 15 | 2.2000 | +10.0% |

Certificate rate stayed at exactly 0.0 for all three declared tasks (100% HOLD), identical in kind
to runs 1-2. Held-out coverage did not miss its target — all-checkpoints-covered rate 97.5%
(Wilson 95% CI 87.1-99.6%) against the 90% nominal target — so the union-bound argument's own
guarantee was not violated; what is refuted is the more specific quantitative prediction that
restricting aggregation to K'=4 checkpoints would be numerically CHEAPER than the joint
whole-trajectory construction at this sample size (n=40).

**Revised understanding (Dr tier, mechanically consistent with the observed numbers but not yet
independently re-verified — discipline 4 below):** at n=40 calibration episodes, splitting `alpha`
four ways (`alpha/K'=0.025` per checkpoint) forces every checkpoint's Bonferroni-corrected rank to
`ceil(41*0.975)=40` — the single LARGEST of only 40 calibration scores, the most extreme order
statistic short of the fail-closed `+infinity` boundary. The joint whole-trajectory construction's
rank was comfortably inside the sample at `37/40`. The per-checkpoint Bonferroni penalty (needing
the top-of-sample score at every one of 4 checkpoints) outweighed the stage-aggregation penalty it
was designed to remove, at this specific sample size. This points to calibration sample size
(n=40 is small relative to K'=4 checkpoints each needing near-extremal order statistics) as the
more precisely located next lever, not the aggregation scheme's correctness.

**Discipline 2 (test the prediction): now APPLIED.** The prediction from the revision above was
tested on real data and refuted, not merely reasoned about analytically.

**Discipline 4 (re-verification by a different identity): still NOT YET APPLIED** to this new
result — same caveat as before; this record was authored by the same chair session that ran the
evaluation. It may not back a claim card or advance any status until a materially separate pass
re-derives the per-checkpoint rank arithmetic (`ceil(41*(1-0.025))=40`) and the reported q values
independently, and checks whether the "sample-size-limited" reading above has an alternative
explanation this session did not consider.

**Tier for this revision: `Dr`** (plausible, numerically grounded in the run's own committed
`lab_results.json`, mechanically consistent with the Bonferroni-rank arithmetic) — the underlying
`q` values and rank=40/40 figures themselves are `finite_diagnostic` (reproduced directly from
`task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run3/lab_results.json`).

## Fourth cycle, 2026-09-09: spectrally-derived decay predictor (PROP-DECAY-01), refuted on two fronts

A different lever was tried: instead of changing the certificate-CONSTRUCTION (C7-C9 vs C9b, the
subject of the diagnosis above), this cycle replaced the error-SCALE PREDICTOR itself (C6, a fitted
log-linear model) with a closed-form decay law derived from the ICP normal-equations Hessian
`H_k=J^T J`'s own condition number, combined with the (unchanged) whole-trajectory C7-C9
construction (chosen because run3 above found it gives a smaller `q` than the Bonferroni
per-checkpoint construction). Toledo proposal `PROP-DECAY-01`
(`~/ANSE.ASIA/toledo/registry/proposals/spectral_decay_predictor.json`) parented this to a proposed
identification of `H_k` with the graph-Laplacian family `L_R`, so that `q_formal/M.07`'s diameter
floor `lambda_2>=4/(nD)` could bound `H_k`'s conditioning.

**Front 1 (structural): the H_k~L_R analogy is refuted, both by a companion Coq-proof attempt and
by inspecting the real H_k.** The companion attempt (paired Toledo-repo task, `q_formal/M.07`
itself) to Coq-prove `lambda_2>=4/(nD)` did not close: the classical Mohar 1991 proof needs the full
min-max/Courant-Fischer characterization of `lambda_2` over the whole space orthogonal to the
constant vector, materially stronger than the single-Rayleigh-pair idiom this workspace's existing
spectral Coq files use, and was not completed in the time given. Independently, exposing the real
`H_k` this backend computes (`task-conditioned-6d-pose-stop/lab/bop_icp_backend.py:normal_equations_H`)
shows the analogy does not hold structurally regardless: `H_k` is a fixed 6x6 SPD matrix (one
row/column per pose degree of freedom), with no vertex/edge structure and no dependence of its size
on the correspondence count — a graph "diameter D" is undefined for it. Confirmed numerically: a
real k-NN correspondence graph built separately from one ICP stage has `n=400`, `diameter=16`,
`4/(nD)=0.000625` — an unrelated number to that same stage's `H_k` `lambda_min=0.1235`.

**Front 2 (empirical): the closed-form predictor does not tighten calibration; it widens it.**
Using the CORRECT quantity for `H_k` instead (ordinary matrix condition number
`kappa=lambda_max/lambda_min`, feeding the classical cited Kantorovich contraction bound
`rho<=(kappa-1)/(kappa+1)`, no graph object needed), the resulting predictor's calibrated `q=3.298`
(~27x envelope inflation) is LARGER than both the original C6 joint `q≈2.0008` (runs 1-2) and every
run3 Bonferroni per-checkpoint `q` (2.085-2.200). Certificate rate remains exactly 0.0 for all
three tasks (100% HOLD) — the fourth cycle in a row landing on this same qualitative outcome, now
under a materially different (non-regression) predictor family. Held-out coverage: 95.0% (Wilson
83.5-98.6%).

**Disclosed, not yet independently re-verified diagnosis for Front 2:** measured `rho_k` across the
40 TRAIN episodes' stages clusters tightly near 1 (median 0.9991, range [0.9964, 0.9997]), likely
because `H_k`'s rotation columns (`-skew(R p_i)`, scaled by point-coordinate magnitude, ~0.05-0.26m
for these two objects) and translation columns (identity-scaled) mix units in the `[omega, t]`
parameterization, so `kappa_k` is dominated by this coordinate-scaling artifact rather than by the
correspondence set's true geometric conditioning. Not yet tested against an alternative
parameterization (e.g. non-dimensionalizing the rotation columns by a characteristic length scale).

Full accounting: `task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run4/RESULT.md`.

**Tier for this update: `Dr`** for the diagnosis narrative above (mechanically consistent with the
committed `lab_results.json` and the separately-computed graph diagnostic, not yet independently
re-verified — discipline 4 still not applied to this record, same caveat as the run3 entry above).
The `q`, coverage, and n/D/kappa/lambda_min numbers themselves are `finite_diagnostic`, reproduced
directly from that run's committed files.
