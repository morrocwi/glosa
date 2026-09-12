# M3 — Readout-to-Defect Soundness (definition draft, Readout Genesis language only)
tier: Dr (definition; AI-drafted, D-AIFILL). Gate served: Zero-Defect Closure (the recurrence-to-saturation step
needs it: a retained core K ⊆ Z_d for all d is only meaningful if every positive witness W_d certifies something).

## Definition (the map that must exist and be sound)
A reader witness is a nonnegative readout W ≥ 0 emitted by the checker on a retained configuration z.
Readout-to-Defect Soundness for a witness family {W} is a map
    Σ : {W > 0}  →  { D_retained , D_admissibility , E_registered }
such that, whenever W(z) > 0, at least one of the following is TRUE of z under grammar A and reader Π:
  D_retained      — a physical loss D(q→q') > 0 is paid by the organization (dispersion, holonomy mismatch,
                    cancellation deficit that is not re-absorbed, relaxation, dead channel) — it is a defect of z.
  D_admissibility — the reader is insufficient: ε_suff/ε_dyn/ε_read/ε_inv/ε_bridge/ε_lineage > 0 — a defect of Π,
                    to be refined, never charged to z.
  E_registered    — the distinction leaves the declared cell/active set: a registered exit, neither loss nor defect.
Unsound witness: a W > 0 that maps to none of the three — a reader PATTERN. A pattern may be reported, never used
as load-bearing information (it cannot enter K ⊆ Z_d).

## Witness families in scope and the obligation for each
| witness W | what the reader sees | must be shown to map to |
|---|---|---|
| dispersion μ = 4c²(1−c²) > 0 (plane turn) | two productive plane normals neither parallel nor orthogonal | D_retained only if the cross interaction is productive AND not exactly cancelled at its target; else pattern |
| cancellation deficit C_k = Σ‖g‖ − ‖Σg‖ > 0 | sources at one target partly cancel | UNDECIDED: is C_k > 0 a paid loss or a constraint F_e = 0 on amplitudes (§114)? — the founder's item C; W1–W3 are the test fixtures (net response 0, C_k > 0) |
| holonomy mismatch around a null-web loop | T_loop(λ) ≠ λ (114.2) | D_retained if the loop is recurrent and productive; E_registered if the loop crosses the cell boundary |
| uncancelled response ‖Σg‖ > 0 at a forced target | novelty generated | E_registered (novelty retained) or D_retained (if dead channel) — never "nothing happened" |
| outward descendant on |s|² = 3L² (§115) | symmetry-breaking descendant | E_registered (leaves the cell) unless suppressed; suppression of both descendants ⇒ parent non-productive (D_dead) — verified on W3 |

## Checker contract (to be implemented after the definition is accepted)
Input: a retained configuration z (modes, polarizations, phases), reader Π (cells, window, depth), grammar A.
Output: for every W > 0 the checker emits, exactly one code from {D_RETAINED, D_ADMISSIBILITY, E_REGISTERED, PATTERN}
with the finite certificate that justifies it (the target, the pair list, the exact forcing, the cell crossed).
Fail-closed: any W > 0 without a code ⇒ the run's saturation claim K ⊆ Z_d is UNRESOLVED.
Fixtures: W1 (two-shell N=2 cancellation), W2 (rank-2 web), W3 (equal-shell N=3, generation 1 both branches),
orthogonal-turn chain generation 1 (mirror target = E_registered? or D_retained? — to be decided by the map).

## What this definition does NOT do
It does not decide the cancellation-deficit question; it makes the decision a required, auditable step.
