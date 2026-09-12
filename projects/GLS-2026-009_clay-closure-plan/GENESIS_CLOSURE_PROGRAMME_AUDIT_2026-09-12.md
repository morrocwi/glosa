# Audit of the founder's Genesis-native closure programme (CTX 260912-1019 / 1028 / 1036 / 1046 / 5th msg)
tier: Dr (AI audit of founder sketches; every "forced" line below is checked against a named existing fixture,
everything else is analysis). Language: Readout Genesis only. Founder's four/five messages are the source
(verbatim in the session transcript; boxed statements copied in FOUNDER_LINES_2026-09-12_GENESIS_CHAIN.md).

## 0. What the founder proposed (compressed, his names kept)
GBRC (bounded-depth readout closure: TERMINAL ∨ ROUTE ∨ DEFECT within m) →
Genesis-1..4 (RS retained sufficiency / RNO / NC bounded-depth novelty closure / defect floor + retained-load
covariance) → Lemma A prefix compactness, Lemma B recurrent extraction, Lemma C RNO, GNG novelty generation →
two closure engines: FRCC (packing, needs frozen ε_O > 0) and NRC (Noetherian closure-ledger rank) →
chain RS + GNG + FRCC/NRC + RC ⇒ retained contraction ⇒ vanishing critical readout ⇒ domain report.
Founder's own key finding: compactness alone is not enough; need ε_O > 0 or Noetherian rank.

## 1. Verdict per piece (Genesis codes)

| piece | verdict | reason (one line) |
|---|---|---|
| Clay = domain leaf, not root; δ_R ⇏ regularity | PASS (already in GENESIS_FORMULATION §0) | matches commuting-square doctrine |
| RNO (Lemma C) | PASS as a DEFINITIONAL IDENTITY, zero domain content | see §2 — it is the contrapositive of reader equivalence; needs *joint* novelty, not per-step |
| GNG per step (P∩T̄∩Ē∩D̄ ⇒ N) | REFUTED per-step at W1, W2, W3 (existing exact fixtures) | each source step is individually novel, the block response at the target is exactly 0 — per-step N does not give block N |
| GNG block form (∃r ≤ m₀ : N∨T∨E∨D) | OPEN — this IS the P3 question in Genesis clothing | the missing piece is Block-Joint Novelty (BJN), §3 |
| Lemma A prefix compactness | PASS (standard, needs 𝔛 compact + ℬ closed) | closedness of ℬ is not free: "productive" is an open condition; must use ℬ̄ and then decide the boundary |
| Lemma B recurrent extraction ⇒ CR₀ core | PASS conditional on RS | this is the existing CR₀(Q̄) ⊆ P∪D object (PROP-P2-CR0-CORE-INCLUSION-OPEN-01) |
| FRCC (packing engine) | INSUFFICIENT as stated — needs pairwise separation, GNG gives only consecutive | see §4; fix = monotone ledger + BJN |
| NRC (Noetherian engine) | PASS mechanism (this is §114.1 generative constraint accumulation); m_* is N-dependent unless the ideal chain is uniform | uniformity = RS again; the running M2 agent is its first fixture (W3 ledger rank per generation) |
| RC retained-load covariance with one exponent κ | REFUTED for amplitude-only reanchor by the existing fixture T/D = 20√E/n² | loss channel and generation channel have different homogeneity degree; covariance holds only under the JOINT reanchor (amplitude ⊗ address), i.e. the dimensionless critical reader — §5 |
| ε_n ≤ Cθ^n from the frozen tape | OPEN watch point (EPSC decay), unchanged | no fixture yet |
| ℬ = "productive + zero-defect + no-novelty + no-exit + nonterminal" | GOOD definition; adopt as the canonical forbidden relation | it is the Genesis name of a free recurrent core |

## 2. RNO is an identity, and what that means
Future-separating is defined relative to Z^ξ (ξ removed). The sketch compares Z_m with Z_0. The two coincide only if
Z_m ∖ Ξ ~ Z_0 where Ξ = all novelties of the block. With lineage preservation (nothing dropped free) Z_m = Z_0 ⊕ Ξ, so
   q(Z_0 ⊕ Ξ) = q(Z_0)  ⇒  O_future(Z_0 ⊕ Ξ) = O_future(Z_0)  ⇒  Ξ is NOT jointly future-separating.
That is the whole of RNO: "what the declared future reader cannot see is, by definition, not novelty". Forced, no
domain content. Consequence: the load-bearing object is Ξ *as a set*, relative to the block origin — not ξ_i one at a
time relative to its predecessor.

## 3. Block-Joint Novelty (BJN) — the real gate, and it already has fixtures
BJN(m): for every productive block Z_n → … → Z_{n+m} with zero defect, no exit, nonterminal, the set Ξ of retained
novelties of the block is jointly future-separating from Z_n above ε_O.
W1 (two sources, N=2), W2 (rank-2 web), W3 (three equal-shell sources, θ = 0, 2π/3, 4π/3): each single step generates a
distinction; the joint response at the shared target is exactly 0 (verified, finite_diagnostic). So per-step N holds
and block N fails — unless the checker records the cancellation as D (paid loss) or T (terminal class) or as a
constraint c_n that strictly advances the closure ledger (NRC). This is exactly the founder's item C (cancellation
deficit C_k > 0: loss or constraint?) and the M3 Readout-to-Defect Soundness map. So: BJN ⇔ P3 (multi-source
cancellation compatibility) in Genesis language. Nothing new is proved by the abstraction; what is gained is that the
gate is now stated without any domain word, and its fixtures are already exact.

## 4. FRCC needs pairwise separation, not consecutive
Packing bounds the number of PAIRWISE ε-separated states. GNG (even in block form) gives d(Z_{i}, Z_{i+1}) ≥ ε for
consecutive states; a stream can return within ε of an earlier state while every consecutive step is ε-separated.
Repair: (i) closure ledger is monotone under ⊕ (never drops a represented novelty — lineage preservation), and
(ii) the future-reader metric is monotone along ⊕: d(Z_i, Z_i ⊕ Ξ) ≥ ε whenever Ξ is jointly novel. (ii) is BJN again.
So FRCC = compactness + ε_O + monotone ledger + BJN. Same gate as §3.

## 5. Retained-Load Covariance fails for amplitude-only reanchor (exact, existing)
check_ns_p2_uniform_scale_loss_audit.py §2 (exact, sympy): on the coherent triad state, loss/generation ratio =
20·√E / n²; i.e. generation scales as λ^{3/2} in amplitude and loss as λ¹ (rates), and the address rescale n → λn
enters as λ⁻². There is no single κ with 𝔇(λZ) = λ^κ 𝔇(Z) and 𝒱(λZ) = λ^κ 𝒱(Z) for amplitude-only λ. Covariance is
exact only along the joint orbit (amplitude λ, address λ⁻¹) — which is precisely the dimensionless critical reader
R = (K²)^r/Λ already in the chain. Hence: δ_* must be the minimum over the JOINT-normalized compact slice, and the
compactness of that slice is RS (G4) — not a separate gate. This removes RC as an independent frontier item and folds
it into RS: the honest list shrinks.

## 6. Resulting honest frontier (Genesis, no domain words)
   RS   frozen tape ⇒ compact JOINT-normalized retained region, uniform in the cutoff (sup_N A_{N,η} < ∞ and tightness)
   BJN  every productive zero-defect block is jointly novel above ε_O, or pays D / reaches T / registers E
        (fixtures: W1–W3 at gen 1 — currently block-N FAILS there, so the checker must classify: D, T, or ledger-progress)
   NRC-u  Noetherian ledger chain length m_* uniform in the cutoff (fixture: M2 W3 rank per generation, running)
   EPSC   ε_n ≤ Cθ^n from tape only
RNO: forced identity (no work). RC: folded into RS. GBRC/NC: consequences of RS + BJN + NRC-u via Lemma A/B.

## 7. Where the running agents sit in this list
rg_run1 (TRANSFORM/SOLVE on frozen input, √5 cells): measures A_{N,η} and α-split → RS evidence, and the α cancel-share is
the first direct BJN readout. rg_m2 (W3 gen-2 exact): dimension of the constraint variety per generation → NRC ledger
rank; if rank stalls with response still 0 and no D, that is a live ℬ-witness at depth 2 (the forbidden fifth outcome)
and the translation must return NO_CLOSURE for that block, not PASS.

## 8. Addendum — ERCP / R1 R2 R3 / GCD / update-class table (founder CTX 260912-1055)
Founder's correction accepted: Noetherian stabilisation is per-chain; uniform m_* needs an effective capacity rank
𝔠_ret with a bound from the frozen tape only (R3). This is the correct name for the uniformity that was hidden.

GCD (retained ⊕ terminalized ⊕ exited ⊕ defected = input, no "vanished" term): PASS as the Genesis conservation law;
it is manifesto P-line "future-relevant information cannot disappear for free" in ledger form. RNO follows from it
(founder is right that RNO is a corollary). Update-class table: adopt; note CANCEL ≠ D automatically — that is
exactly the M3 map's undecided row.

### The three adversarial cases against ERCP, checked against existing exact fixtures
1. Infinitely refinable novelty — SURVIVES ONLY WITH DECLARED CELLS. In the exact reader the address lattice is
   unbounded: every generation of the ∇V term places a descendant at a farther address (|s|² = 3L², verified on W3).
   Refinement beyond the declared cell is not N, it is E (registered exit). So 𝔠_ret is finite per cell, but the exit
   channel then carries retained load OUT of the cell, and the cell-local balance is only honest if exits are counted.
   Existing fixture: retention-gap checker — full-shell datum, energy-only reader: exit-carried share grows
   0.232 → 0.238 → 0.340 → 0.647 (does not satisfy ε_j ≤ Cθ^j); cube-surface datum: 0.232 → 0.073 → 0.039 (does).
   Verdict: case 1 is the EPSC watch point; ERCP holds per cell, the cross-cell ledger is where the load goes.
2. Dependent-looking novelty independent later — SURVIVES in exact arithmetic (rank over ℚ / ideal membership at
   fixed cutoff is decidable; R2 returns YES/NO), returns U under any floating reader. The M2 agent computes exactly
   this (constraint-variety dimension per generation on W3). No fixture contradicts.
3. Readdress/reanchor cycle resetting rank at zero defect — DOES NOT SURVIVE AS STATED. The joint reanchor
   (amplitude λ, address λ⁻¹) is a symmetry of the stepper; a state exiting cell j re-enters cell j+1 as the same
   joint-normalized state with a fresh ledger (rank reset, E registered, D per cell a fixed fraction). Exact fixture:
   the critical budget — ∫generation/∫loss = 1 + 1/(2ν) = 101 for EVERY cell j (check §3), i.e. each cell is built
   from zero, pays the same relative loss, and the normalized load does not contract. This is the R_j ≡ 1 no-go
   in Genesis language. So ERCP must be amended: 𝔠_ret is defined on the JOINT-normalized quotient, and REANCHOR
   is an eighth update class whose required consequence is "rank carried across the cell (no reset) ∨ D ≥ δ𝒱 ∨ E with
   load accounted into the next cell's 𝒱". Without that row, ERCP is refuted by the budget fixture.

### Net effect on the frontier (§6 updated)
   RS      frozen tape ⇒ compact joint-normalized region (sup_N A_{N,η} < ∞, tightness)
   BJN     block-joint novelty above ε_O, or D / T / E — fixtures W1–W3 (block-N fails at gen 1; must classify)
   R3-joint  capacity rank bounded on the joint-normalized quotient, i.e. the reanchor cycle is not free
             — fixture: budget ratio 101 (fails energy-only); orthogonal-turn tax 17/25 (one exact per-turn tax)
   EPSC    exit-carried load ε_j ≤ Cθ^j from tape — fixture: retention-gap (fails full-shell, holds cube-surface)
The three heavy items are the same three we had (G4 / G6 / G7) but now each has an exact fixture that a candidate
proof must pass first, and none of them can be discharged by the abstract lemmas (GCD, RNO, Lemma A/B), which are
forced but content-free for these three.

## 9. RETRACTION (2026-09-12 ~11:40) — §1 row "GNG per step REFUTED by W1–W3" was too strong
W1–W3 show exact cancellation at ONE shared target, not zero novelty of the whole step. The rg_m2 exact run
(sympy Gröbner over ℚ(√3), rg_m2_run1.log / run2.log) shows for W3 gen 0→1: seed variety dim 12 (productive, C₀≠0);
requiring all 68 live targets to vanish ⇒ EMPTY; with exits |t|² ≥ 3 declared and seed-mode feedback |t|²=1 left
unconstrained, requiring the interior classes |t|² ∈ {3/4, 7/4, 9/4} to vanish ⇒ still EMPTY (the run1 "dim 6"
variant excluded the wrong class and is superseded by run2). So per-step GNG HOLDS on W3 at gen 1 under both
conventions: every productive seed emits interior novelty. Corrected row: GNG per step — PASS on W3 gen 1 (exact);
block-joint novelty (BJN) remains the gate for deeper blocks and for the cross-cell (reanchor) cycle. §3 wording
"per-step N holds and block N fails" stands only for the single shared target, not for the step.
