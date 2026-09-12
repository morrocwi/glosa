# NPSC v2 — frozen encoding (founder 2026-09-13 17:5x); no run until the box-1 pilot validates semantics
Object: address set S (negation-closed, orbit rep), amplitudes u_m = x_m e1(m) + y_m e2(m) with the sweep's exact
perp_basis (generator basis reused verbatim), full convolution over unordered pairs, F_k = NET forcing at every
target k (aggregated over all contributing pairs) — inside and outside S alike.
Per aggregated target k (registered or not):
  selector s_k ∈ {0,1}:              s_k (s_k − 1) = 0
  s_k = 0 ⇒ F_k = 0:                 (1 − s_k) F_{k,j} = 0   for j = 1..3
  s_k = 1 ⇒ u_k ≠ 0 (k registered):  s_k (Σ_j λ_{k,j} u_{k,j} − 1) = 0   (Rabinowitsch on a linear witness; no ‖u‖²)
  k NOT registered ⇒ s_k = 0 forced (an unregistered forced address is FORGOTTEN_INSIDE/TED: excluded from a
     zero-novelty/zero-exit closure test) — i.e. all unregistered targets must have F_k = 0.
Productivity (founder 18:4x): at least one registered k with s_k = 1 AND F_k ≠ 0 — encoded with a PER-ADDRESS linear
  witness: selector r_k ∈ {0,1}, Σ_k r_k − 1 = 0 (at least one productive address), r_k (Σ_j μ_{k,j} F_{k,j} − 1) = 0,
  r_k (1 − s_k) = 0; no sum of squares in either lane. Real lane: UNSAT over the algebraic closure is a valid
  exclusion; any SAT must pass a separate real-feasibility certification before being reported as real SAT.
Isotropic guard: for every target with symbolic k, saturate k·k ≠ 0 (u_iso (k·k) − 1 = 0); for integer targets skip.
Outputs per S: UNSAT (no accounting-complete productive zero-novelty configuration) / SAT with an exact point and the
  per-address state table from rg_forced_address_audit.audit (must show 0 FORGOTTEN_* — a consistency assertion) /
  TIMEOUT. Verdict labels: NPSC_V2_NOT_SELF_CLOSED / NPSC_V2_SELF_CLOSED_CANDIDATE (→ realization audit) / TIMEOUT.
Pilot: box [-1,1]^3 sizes 2,3,4 (85 reps). Full: box [-2,2]^3 sizes 3,4 (26,411 reps) only after the pilot report.
Status wording rule: the old box-2 hit interpretation is RETRACTED; NPSC v2 is a NEW sweep, not a re-labeling.
