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
