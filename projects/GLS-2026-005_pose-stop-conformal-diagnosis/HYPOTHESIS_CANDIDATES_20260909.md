# Candidate next hypotheses for GLS-2026-005 (problem card GLOSA-PC-20260909-0005)

AI-drafted comparison table. Per glosa's own rule (hypothesis_selection.schema.json: "an AI route
may PROPOSE the comparison table, never make the selection"), **the founder chooses** which
candidate(s) carry forward into a fifth real-data cycle. Nothing below is a decision.

Founder's own redirect (verbatim, 2026-09-09) that produced candidate H3: "ต้องตั้งคำถามก่อนว่า
error คืออะไรในปรัชญาของเรา และวางโมเดลขึ้นมาใหม่จากรากของ Toledo เอง" -- the classical error
definition `e_k = Log(That_k^-1 T*)` used by all four prior cycles requires the unobserved true
pose `T*`, a non-readout under this workspace's own information-discrete-math discipline. H3
redefines error natively, from Toledo's own root primitives, with no `T*` anywhere.

## H1 -- graph-structured correspondence-residual feature
Build an observable feature from the ICP correspondence set's OWN graph structure (which, unlike
the normal-equations Hessian `H_k` refuted in run 4, genuinely has vertices/edges/a diameter), and
apply Toledo's L_R ceiling/floor method to THAT object.
- developability: real correspondence graphs already exist inside the ICP backend; needs new
  feature-extraction code, not a new backend.
- falsifier reachable with our resources: yes -- same BOP-LMO data, same lab harness.
- risk: the correspondence graph's spectral properties may still carry little information about
  true pose error (an empirical question run 1-4's pattern suggests could go either way).
- relation to the founder's redirect: partial -- still calibrates against T* offline (same as
  runs 1-4), does not yet address the deeper "what IS error" question.

## H2 -- replace classical ICP with a learned/neural pose backend
Matches the original adversarial review's own stated requirement (R8: an empirical robotics
contribution needs a real iterative learned backend, e.g. FoundationPose-class).
- developability: substantial -- needs integrating an external pretrained model, likely GPU,
  different licensing/dependency footprint than the from-scratch numpy+scipy backend used so far.
- falsifier reachable with our resources: partial -- depends on what pretrained backends are
  actually runnable on this workstation (no GPU confirmed available for this repo's own use).
- risk: highest-effort option; if it also fails to certify, the wasted cost is largest.
- relation to the founder's redirect: none directly -- also still calibrates against T*.

## H3 -- native readout-not-truth error redefinition + retained-sensitivity admissibility (NEW, this session)
`PROP-NATIVE-01`/`PROP-NATIVE-02` in `~/ANSE.ASIA/toledo/registry/proposals/
native_retained_sensitivity.json`. Redefines "error" as the retained difference `Delta_k` between
consecutive readouts (never `T*`), and redefines the ACT criterion as: the task verdict must be
invariant under perturbing the current pose estimate along the correspondence Hessian `H_k`'s own
low-eigenvalue (data-justified-uncertain) directions, by a magnitude the data itself justifies
(inverse eigenvalue, bounded by the already-proven `weld/M.40.v1` ceiling). No `T*` is used even
for calibration -- only as an external check, after the fact, the same way any falsifiable
prediction is checked.
- developability: moderate -- reuses run 4's own already-built `H_k` eigen-extraction code; the
  new part is the perturb-and-recheck-the-task-verdict loop, which is a smaller build than a new
  backend.
- falsifier reachable with our resources: yes -- same BOP-LMO data, same lab harness, same 3
  declared tasks.
- risk: a genuinely new construction (Dr tier), no coverage-style guarantee proven yet -- "small
  eigenvalue direction correlates with large true error" is itself an assumption to test.
- relation to the founder's redirect: direct and complete -- this IS the founder's own redirect,
  formalized and Toledo-registered.
- an added benefit: sidesteps run 4's EXACT refutation (H_k has no graph diameter) by using H_k's
  own eigenvalues directly, never needing a diameter at all.

## AI's own honest read (not a recommendation to override the founder's choice)
H3 is the only candidate that actually answers the question the founder asked this session,
rather than being one more variation on runs 1-4's calibration-against-T* pattern. H1 and H2 are
legitimate independent options if the founder wants to keep the classical error definition and
attack a different part of the pipeline instead. All three could also be run in sequence or
combined (e.g. H3's native criterion tested on H1's graph-structured feature).

## Outcome, 2026-09-09: H3 tested, refuted (unsafely, not safely)

Founder selected and authorized H3 ("เราสร้างโมเดลมา แก้ปัญหาให้ certificate ทำงาน"). Executed as
`task-conditioned-6d-pose-stop/lab/native_sensitivity.py` +
`lab/run_native_sensitivity.py`, on the identical BOP-LMO data/split as cycles 1-4
(`lab/results/real-bop-lmo-2026-09-09-run5/`).

**This is the first of the five real-data cycles (H3's cycle plus cycles 1-4) to license ACT at
all.** It is not the success this candidate's write-up hoped for: ACT fired on 100% of test
episodes across all three tasks, always at the very first ICP stage, and was WRONG (unsafe) on
92.5-100% of them. The exact risk this candidate's own write-up flagged in advance --
"'small eigenvalue direction correlates with large true error' is itself an assumption to test" --
is the assumption this run refutes. `H_k`'s spectral floor alone, without an absolute
residual/noise-scale term, is not a safe proxy for pose uncertainty on this backend.

H1 (graph-structured correspondence-residual feature) and H2 (learned/neural backend) remain
untested, available candidates if a sixth real-data cycle is authorized. A natural next design
(not yet built, not authorized) combining H3's ground-truth-free ACT framing with an absolute
residual-scale term (as the fourth cycle's own decay predictor already carried, for a different
purpose) would directly address this run's own diagnosed root cause, rather than abandoning the
native-error framing PROP-NATIVE-01 argued for.

Full accounting: `task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run5/RESULT.md`.

## Outcome, 2026-09-09, sixth cycle: PROP-NATIVE-03 (memory/persistence) tested, refuted

Founder authorized a sixth cycle ("เอาเลยรอบที่หก") to test whether Toledo's already-registered
`PROP-NATIVE-03` (a persistence/memory streak gate on top of H3's own per-stage check) recovers
safety. Executed as `task-conditioned-6d-pose-stop/lab/native_persistence.py` +
`lab/run_native_persistence.py`, identical data/split as cycles 1-5
(`lab/results/real-bop-lmo-2026-09-09-run6/`), two variants: (a) persistence gate only; (b) also a
residual-scaled perturbation magnitude, directly targeting this document's own suggestion above
("a natural next design ... combining H3's ground-truth-free ACT framing with an absolute
residual-scale term").

**Both variants refuted.** A TRAIN-only diagnostic disclosed before test.jsonl was opened predicted
the outcome: H3's per-stage check never toggles on TRAIN (True at all 640 readings), so the streak
accumulator has nothing to filter. Confirmed on test: ACT fires deterministically at the fixed
stage `k=3` on 100% of test episodes, unsafe on 80.0-87.5% of them (a modest improvement over run5's
92.5-100%, attributable only to 3 extra ICP iterations, not to persistence itself). Variant (b)'s
residual-scale term (this document's own suggested next design) also did not help: its dynamic
range (~1.15-1.8x) is roughly two orders of magnitude too small relative to the gap between the
perturbation cap and the real coarse-detector initial-pose error.

H1 (graph-structured correspondence-residual feature) and H2 (learned/neural backend) remain
untested. The concrete lesson for any further iteration on this line: neither `H_k`'s eigenstructure
nor the ICP correspondence residual RMSE carries the ABSOLUTE scale of the coarse detector's real
initial-pose error on this backend -- a future construction needs either a genuinely
large-dynamic-range observable tied to absolute error scale (not yet identified here), or a
different framing that reasons about the coarse initial estimate's own error distribution directly.

Full accounting: `task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run6/RESULT.md`.

## Team meeting, 2026-09-09: PROP-NATIVE-04 registered as the run-7 candidate

Founder instruction after run 6's refutation: convene an ultracode team meeting reading the six-run
history through the Toledo, readout_genesis, readout_universe, and glosa-methodology lenses, and find
the answer. Four independent lens agents converged, from four directions, on the same diagnosis:
runs 4-6 (PROP-DECAY-01, PROP-NATIVE-01/02/03) each read only a LOCAL, single-instant or
boolean-folded quantity (H_k's own eigenstructure or a streak of pass/fail checks) and never an
absolute, calibrated SCALE term -- which is exactly the ingredient PROP-NATIVE-02's own honest_caveats
and run 6's own diagnostic named as missing. The one already-registered, already-validated
(CONTINUUM_AUDIT_20260909.md rates its marginal-coverage machinery LOW RISK) absolute-scale observable
in the whole project is the split-conformal quantile from runs 1-3 (PROP-CONF-01/02/03) -- never once
combined with a native/local check across six cycles (methodological gap #2 identified by the
glosa-methodology lens read of this project's own ledger).

**Registered candidate: `PROP-NATIVE-04`** (Toledo:
`toledo/registry/proposals/native_retained_sensitivity.json`, tier Dr, status unverified -- design
only, not yet run). Three concrete changes on top of PROP-NATIVE-02/03, one per diagnosed defect:
1. Perturbation magnitude `eps_{k,j} := min(q_k/lambda_j, weld/M.40.v1 ceiling)`, where `q_k` is
   PROP-CONF-03's per-checkpoint Bonferroni conformal quantile (calibrated OFFLINE on the n=40
   calibration set only, never online) -- replaces run 5's undersized, TRAIN-population-borrowed CAP.
2. Per-stage signal is `Gamma_k := sum_j lambda_j * eps_{k,j}^2`, Toledo's proven Keystone quadratic-form
   energy (`Phi^T L_R Phi`, specialized `L_R -> H_k`) -- a real magnitude, not run 6's degenerate
   boolean indicator.
3. Accumulator is a DECAYED real-valued running sum `m_k := rho*m_{k-1} + iota_k*Gamma_k` (Toledo root
   A2/FOLD, generalized to a real carrier) rather than run 6's hard reset-to-zero streak.
   ACT iff `m_{k_m} >= theta` AND `q_{k_m} <= tau_i` (the calibrated envelope already fits the task
   tolerance, C11).

This is a design record only -- P08's full four-discipline diagnosis was not re-run for this entry
(the standing methodological gaps it identified, same-split reuse and the either/or hypothesis-class
gap, are carried forward as open risks in the Toledo entry's `honest_caveats`, not resolved here).
Full reasoning, parents, and open risks: `toledo/registry/proposals/native_retained_sensitivity.json`
entry `PROP-NATIVE-04`. Implementation and execution (run 7) is a separate, not-yet-authorized-by-this-
document Execute-phase step.

## Run 7 executed, 2026-09-09: PROP-NATIVE-04 refuted, over-conservative direction

Execute-phase result: `task-conditioned-6d-pose-stop/lab/results/real-bop-lmo-2026-09-09-run7/RESULT.md`,
Toledo status updated to `refuted_over_conservative`
(`toledo/registry/proposals/native_retained_sensitivity.json`, entry `PROP-NATIVE-04`).

A TRAIN+CALIBRATION-only diagnostic, disclosed BEFORE `test.jsonl` was opened, predicted the exact
failure mode that FINAL TEST then confirmed: (1) `eps_{k,j}=min(q_k/lambda_j, CEILING)` saturates at
the reused CEILING (byte-identical to runs 5-6's own CAP) on 100% of TRAIN stage-checkpoint pairs --
`q_k` is uniformly larger than the ceiling on this backend, so the conformal-quantile term never
actually influences the perturbation magnitude; (2) the checkpoint certificate gate (a disclosed
reading of the registered `q_{k_m}<=tau_i` as PROP-CONF-03's own physically well-typed certificate
condition, since the literal scalar comparison mixes a dimensionless log-quantile with a physical
tolerance) is TRUE on 0/40 TRAIN episodes at every predeclared checkpoint -- reproducing run 3's
already-known `certificate_rate=0.0` finding.

**Test-time result: ACT rate 0% (100% HOLD) on all 40 test episodes, all three tasks. Unsafe-ACT
rate 0% -- but only because ACT never fires at all.** Non-inferiority fails in the OPPOSITE
direction from runs 5-6 (LCB -23.7% to -49.1%, vs the estimator's own 10.0-32.5% completion rate).
Checkpoint diagnostics: the Keystone/decay accumulator alone (`m_k>=theta`) held on 45% of
checkpoint readings per task -- not itself vacuous -- but the certificate gate held on 0/160
readings per task throughout, making it the sole binding constraint.

**Methodological note for this project's own ledger:** this is the THIRD independently-designed
construction (after PROP-CONF-03's own standalone certificate in run 3, and now this conjunctive
gate) to find the same per-checkpoint Bonferroni conformal envelope vacuous on this exact
backend/dataset -- a within-project stability finding about that specific calibration construction
itself, not an artifact of any one run's tuning. Standing methodological gaps (same-split reuse
across all seven cycles; the honest_caveats' Open risk 3 second-calibration-split falsifier) remain
open and were NOT closed by this run -- flagged here, not silently dropped, per this project's own
predeclaration/disclosure discipline.
