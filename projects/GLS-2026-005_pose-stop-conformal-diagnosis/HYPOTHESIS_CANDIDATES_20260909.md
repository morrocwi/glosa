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
