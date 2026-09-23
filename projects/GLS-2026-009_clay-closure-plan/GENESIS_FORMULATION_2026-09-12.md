# GLS-2026-009 — the whole NS closure problem written in Readout Genesis language only
tier: Dr (lens-in formulation; AI-drafted, disclosed D-AIFILL). Every world-language word appears only in the
lens-out dictionary at the end. Sources: readout_genesis CORE (E00.1–E00.7, II.1–II.3, II.8/IV.4, V.4, VI-A B.1–B.2,
Steps 1–8, 16, 18, 31–32), INFORMATION_DNA RD1–RD9, standalone vNext §46–66, §69–89, §109–118, FINAL-EQUIV.

## 0. Root and grammar
- Root: δ_R = (a ♯ b), a retained distinction. RD1 a start exists; RD2 every retained state steps; RD3 no step
  erases to null; RD4 distinct histories stay distinct; RD5 what holds at the start and survives every step holds
  everywhere. Δθ > 0 and τ_c > 0 are axioms; Δθ = 0, +∞, completed limits are NON-READOUTS (E00.6).
- Structure forced by the root: L_R = D_W − W on the finite causal graph (Th_coqc). Here the graph is the finite
  wavevector lattice with triad edges p + q = k; L_R's diagonal readout is |k|².
- Grammar A: the stepper F. At the NS leaf the spine reads with no inertial term (M = 0), damping D = ν·L_R
  (per-mode relaxation), nonlinear generation ∇V = the quadratic triad coupling 𝓑_{p,q}(a,b) = P_k[(a·q)b + (b·p)a],
  no external source J, residual η = whatever the chosen reader cannot represent. Step 16 (nonlinear generation of
  new distinctions) is the only place novelty is created; Layer 3 (LP-NS audit) is the CHECKER that watches it.

## 1. Retained state, readers, datum
- Retained multimode state X[n]: the finite set of (wavevector, polarization, phase) distinctions kept at tick n.
  Scalar reduction of X to one number per scale is the Scalar-Eigenmode Reduction Error (Step 18) — forbidden as
  a state, allowed as a readout.
- Reader Π = (atlas of scale cells, window ℋ, resolution/budget 𝒦). A scale readout is a quotient q_j. The square
  q_{j+1}∘F = F♯_j∘q_j either commutes or its defects ε_dyn, ε_read are DECLARED before the run (B.2 step 8).
  A reader that does not commute with the seed's own scale action (Steps 31–32) produces a reader defect, not a
  fact about F (this is what happened with dyadic cells vs a 5^j self-similar seed).
- Datum 𝔡₀ = 𝔓_RD = (Γ₀ initial history, δ_R kept, 𝔃^cand, F, Adm, ℬ, 𝒯 tape, 𝒬 question, O readout, ℋ, 𝒦).
  Nothing from the future of the tape may enter 𝔡₀ (Maker–Checker: the answer never leaks back).
- Lineage (Trace): every productive distinction at tick n has a certified source path from 𝔡₀ or a named defect
  ε_lineage > 0. A seed mode placed by hand at a high scale is a datum, not a generated distinction.

## 2. Defects and the balance
- Admissibility defects ε = (suff, dyn, read, inv, bridge, lineage): the reader's language is insufficient — reject/
  refine, never "physics".
- Physical loss D = D_disp + D_hol + D_cancel + D_visc + D_dead: the price a productive organization pays.
- Balance (B): 𝒱(q') + D(q→q') ≤ 𝒱(q) + ε_br, with 𝒱 the escape potential (everything still able to produce
  future critical readout). Consequence: Σ_j D_j ≤ 𝒱₀ + Σ ε_br < ∞ always; a zero-defect transition keeps 𝒱.
- Cancellation at a target is not disappearance: it is constraint information F_e = 0 tying source amplitudes
  together (§114). Attempted perfect retention across a hand-off ⇒ accumulating constraints M₀ ⊇ M₁ ⊇ … (§114.1).

## 3. The question, in lens language (this IS the problem)
  Can a genuinely three-dimensional, productive organization of retained distinctions reproduce zero-defect
  critical escape indefinitely under grammar A_NSE — i.e. is there a Productive Information Circuit?
  Target: CR₀(Q̄^sc_P2) ⊆ P ∪ D  (the only zero-defect recurrent cores are the planar kernel-side class P or the
  degenerate class D). Equivalently K∞ = ∅. The critical-normalized readout S_N = K_N²/Λ_N^{α_p} must not hold at
  the critical barrier S ≡ 1 forever.
  Non-readouts that must not enter the core: "singularity", ‖u‖→∞, sup over the future inside a premise.

## 4. Relations (every edge with its tier)
  [RD5 shape]      φ(0) = datum bound  ;  φ(x)→φ(σx) = hand-off contraction  ⇒  ∀x  — the proof grammar (Ax/Th)
  G4  compact exact scale-covariant quotient Q̄^sc from 𝔡₀ alone              ⟵ Retain sufficiency (B.2 step 5)
                                                                             + tightness of ancestry reader A_{N,η}
                                                                             + coherent normalization (108.3)   [OPEN]
  G6  no zero-defect productive recurrence:  interior IRR ⟵ Recurrence-to-Saturation + Witness Soundness
                                                              + (OWR/FNW or OCSR)                                [OPEN]
                                             lower corridor ∂₋ ⟵ FAR-a/b/c attenuation (107.1)   [CONDITIONALLY CLOSED]
                                             upper boundary ∂₊ ⟵ UBRR (diffuse residue reader)   [OPEN]
  G7  positive homogeneous floor: Σ_{r<m} D ≥ δ 𝒱_j  ⟵ compact m-block path space + l.s.c. + scale covariance
                                                          (79.1) ; bridge decay ε_j ≤ Cθ^j ⟵ certified tape       [OPEN]
  G7 ⇒ 𝒱_{j+m} ≤ (1−δ)𝒱_j + ε_j ⇒ S_N ≲ Λ_N^{−σ} ⇒ R_N = S_N^{r_p} → 0                                  [DERIVED]
  R_N → 0 ⇒ finite modal gate ⇒ regularity on [0,T] ∀T                                        [DERIVED, FINAL-EQUIV B]
  regularity ⇒ R_N → 0 (so R_N → 0 is the target in another name; nothing equivalent to it may sit upstream) [DERIVED, A]
  Known finite facts (PASS): single-target cancellation generic (rank = dim k⊥) except equal-source-shell N=2
  (direction lock ∥ p×q, corollary of §14); W3 is not a zero-defect web at depth 1 (c≠0: outward suppression kills
  the parent; c=0: 36 forced novelty targets); orthogonal-turn chain pays mirror tax 17/25 every scale; energy-only
  remainder refuted by Bernstein-saturating full-shell data (ratio ∝ √λ), not by few-mode data; critical budget
  ∫T/∫D = 1 + 1/(2ν).
  Refuted routes (0, not ⊥): universal δ from energy/accounting; pointwise T ≤ (1−δ)D + Cρ^j; K_N-criterion or
  SC(T) or "retention gap with solution-dependent constants" as a NEW bridge (all regularity-equivalent → HOLD).
  Hidden-target watch points (where the answer could leak upstream): G4 compactness; G7 homogeneity; EPSC decay.

## 5. Zero vs ⊥ ledger
  0 (no relevant difference under the declared reader): "cancellation at one target is impossible" (refuted);
  "energy accounting gives δ" (refuted); "the selected tree is privileged" (refuted: off-tree ≥ selected).
  ⊥ (undecided): G4, G6 (OCSR, WS, UBRR), G7 homogeneity, hand-off cost α_j under a commuting reader (v2 HOLD),
  A_{N,η} ≤ B(𝔡₀) (never measured), Clay itself.

## 6. Solving order (RD5-shaped, smallest reversible step first)
  0. Reader honesty: Π commuting with the seed's scale action; ℋ, 𝒦, ε_read declared; lineage from 𝔡₀ only.
  1. Measure on that reader (finite_diagnostic): α_j^{sel/off/cancel/total} and A_{N,η}/B(𝔡₀) vs active-set depth d.
     Kill rules: α stable & <1−e^{−c} in d → G6/G7 supported on this seed; α→1 with honest lineage → Track B witness
     candidate; A_{N,η} unbounded → refine the state (Q), not the theorem.
  2. OCSR at generation 2, exact: dimension of the constraint variety M_d must drop per productive generation.
  3. Witness Soundness as a definition + checker (W1–W3 as fixtures): witness → physical defect ∨ admissibility
     defect ∨ registered exit.
  4. G7 homogeneity from scale covariance on a compact m-block path space (no sup over the future).
  5. UBRR: the diffuse ∂₊ reader; the hardest and last.

## 7. Lens-out dictionary (world language, used only here)
  retained distinction ↔ Fourier mode with polarization/phase · grammar A_NSE ↔ periodic 3D Navier–Stokes ·
  L_R ↔ −Δ on the lattice · nonlinear generation ↔ (u·∇)u triads · reader q_j ↔ dyadic/packet shell readout ·
  ℋ ↔ time window τ_j = c/(νλ²) · 𝒦 ↔ cutoff N_G / RAM · datum 𝔡₀ ↔ (u₀, ν, Ω, BC) · escape potential 𝒱 ↔ critical-
  normalized readout S_N and its retained companions · physical loss D ↔ dissipation + cancellation deficit + …
  · P ↔ planar/2D3C flows · D ↔ degenerate/nonproductive · CR₀ ⊆ P∪D ↔ no self-sustaining critical cascade ·
  R_N → 0 ↔ subcritical finite-observation gate ↔ (FINAL-EQUIV) global regularity · non-readout "singularity"
  ↔ Fefferman's finite-time blow-up (periodic case).
