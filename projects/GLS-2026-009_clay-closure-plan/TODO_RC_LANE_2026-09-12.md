# TODO — Readout–Clay / NS lane (two proposals run side by side)
tier: Dr. TaskCreate tool unavailable in this session → this file is the todolist of record (mirrored in handoff).
Proposal 1 (AI): M3 Readout-to-Defect map + BJN checker on W1–W3.   Proposal 2 (founder, CTX 260912-1055+): region-split
RCAP_int / RCAP_- / RCAP_+ with RC-SIG/RC-FRESH as the first shot. Both are tested against the SAME fixtures.

## Extracted from the founder's message — what is useful and checkable
U1. Three-region split 𝒬_RC = int ∪ ∂₋ ∪ ∂₊ with separate capacity theorems. USEFUL: it stops one ERCP from being
    asked to cover the diffuse upper boundary, where algebraic rank is the wrong reader. Adopt.
U2. Interior signature Σ(Z) = (direction, polarization, phase relation, cancellation, ancestry address, invariant
    allocation) and the translation gate q_RC(Z) = Q(Σ(Z)). USEFUL: this is a concrete sufficiency test, decidable
    on fixtures (does the future readout of W3 gen-2 depend on anything outside Σ?).
U3. RC-GNG-int: productive zero-defect generation ⇒ I_{d+1} ⊋ I_d ∨ T ∨ E. This is OCSR in ledger form — same object
    the M2 agent computes (dim of constraint variety per generation). Adopt as the M2 pass criterion.
U4. Bounded Readout Signature Theorem (n_*, D_* fixed, not growing with generation) ⇒ m_int ≤ 1 + C(n_*+D_*, D_*).
    USEFUL but must be checked immediately (see T1): in seed coordinates the degree DOUBLES per generation
    (each step is quadratic; descendant amplitudes are quadratic in ancestors ⇒ deg 2^d); in local coordinates the
    degree stays 2 but the variable count grows (W3 depth-1: 3 seeds → 36 nonzero targets). So n_*, D_* both fixed
    is possible ONLY per declared cell with everything outside the cell registered as E — which is the reanchor
    problem (audit §8 case 3) again. Not a refutation, a scoping: RC-SIG is a per-cell statement.
U5. Track-D falsifier as a checker rule: J_{d+1} = J_d while the future readout changes ⇒ LOST_INFORMATION (Σ
    insufficient), not a geometry counterexample; only with Σ sufficient does a stalled ledger + productive + D=0 +
    E=0 become an RC-G6 counterexample candidate. USEFUL: this is exactly the fail-closed rule M3 needs. Adopt.
U6. ∂₋ (remote ancestry): capacity = 𝒜_{N,η} ≤ A_*(𝒯₀), then FAR reader G_M ≲ A_*^{1/2} 2^{-M(β−η)} ⇒ CONTRACT ∨
    REANCHOR ∨ LOCAL ∨ BACK. This is the rg_run1 readout (A_{N,η} measured). No new work; wait for the run.
U7. ∂₊ (diffuse): needs an aggregate reader ℛ₊ that is reader-invariant, reanchor-covariant, cancellation-aware.
    OPEN, no fixture, no candidate reader yet. Honest status: this is the largest unreduced hole; do not let any
    interior result be reported as RC-G6.
U8. RC-G7 as written still uses single-κ covariance — REFUTED for amplitude-only reanchor (audit §5); must read
    "joint reanchor". Founder's chain otherwise unchanged.

## Todolist (ordered; each item names its fixture and its pass/fail code)
T1  [P2, immediate, exact] RC-SIG scoping on W3: from rg_m2 output extract per generation d=0,1,2 — number of active
    addresses n_d inside the √5 cell, degree of the constraint generators in local vs seed coordinates, dim J_d.
    PASS if n_d, deg bounded per cell; LOST_INFORMATION if future readout differs with J_{d+1}=J_d (U5);
    NO_CLOSURE if J stalls with response 0, D=0, E=0. Owner: this session, after rg_m2 returns.
T2  [P1+P2 joint] M3 checker: W1, W2, W3 gen-1 → each W>0 gets D_RETAINED / D_ADMISSIBILITY / E_REGISTERED / PATTERN
    with certificate; add the U5 rule and the REANCHOR update class (audit §8). Fixture: `verify_w3_gen1.py`,
    `check_ns_p2_multisource_cancellation.py`. Output: `rg_m3_check.py`.
T3  [P2] Σ-sufficiency test (U2): perturb W3 gen-2 state in a coordinate NOT in Σ (e.g. an invariant-allocation-
    neutral phase shift) and test whether the future readout at gen-3 targets changes. If yes → add coordinate.
T4  [P2] ∂₋: read A_{N,η} and α-split from rg_run1; code RS PASS / INSUFFICIENT_RESOLUTION.
T5  [P2, open] ∂₊ aggregate reader ℛ₊ — design only; no computation until a candidate reader is declared and frozen.
T6  [both] RC-G7 statement rewrite with joint reanchor; check that δ_RC from the joint-normalized slice matches the
    existing critical reader R (no new object; Toledo lookup PROP-P3-RETENTION-GAP-RECURRENCE-01 first).
T7  [governance] Push/PR of NS branch research/p2-retention-gap-2026-09-12 and Toledo branch — still waiting on
    founder go + adversarial review. Repo rename — name unconfirmed.
Standing constraints: Genesis language only until a way out; RAM cap 3 GB/process, no grid > 64³; no new Toledo
entries for objects already in the chain; keep the handoff current.

## Addendum (founder CTX 260912-1104 RC-FIBER, 260912-1114 RC-TYPE / RC-CYCLE)
U9.  Retained Extension Fiber, Δc_d = f_d − r_d^sound, output alphabet DROP/NEUTRAL/EXPAND. USEFUL and directly
     computable on W3 gen 1→2 from the rg_m2 data. One precision (Genesis, not domain): in a deterministic stepper
     every new descendant address comes with its own defining relation, so r_d ≥ f_d ALWAYS; the whole content of
     g(e) = r^sound − f is the number of EXTRA relations — forced-zero targets (cancellation) and forced-zero outward
     descendants — that constrain the PARENT class. W3 gen-1 fixture: 44 targets, 36 nonzero, 8 exactly zero;
     outward descendants forced to 0 ⇒ parent C_i = 0. Whether those count as constraints (DROP) or as registered
     exits E (NEUTRAL + load leaving the cell) is precisely the M3 row still undecided. So g(e) is undefined until
     M3 chooses per witness; the checker must output BOTH conventions and never pick silently.
U10. RC-TYPE / RC-CYCLE (finite type alphabet 𝔗 after reanchor, cycle surplus G(C) = Σ g(e), min cycle mean μ_*,
     potential Φ_d = c_d + h(τ_d), Φ_{d+1} ≤ Φ_d − μ ⇒ depth ≤ (Φ_0 − Φ_min)/μ). USEFUL — replaces "DROP every
     generation" by "no free cycle", which is the correct Genesis form (Karp min-cycle-mean is exact on a finite
     weighted digraph; all weights are integers, so μ_* > 0 iff every cycle has G > 0). Hidden gates named by the
     founder and confirmed: (a) 𝔗 finite ⇐ reanchor equivalence 𝔉_d/Q ≅ 𝔉_1 — this is audit §8 case 3; the REANCHOR
     edge must be IN the graph with its own g, otherwise the cross-cell budget fixture (ratio 101 ∀ j, each cell
     rebuilt from zero) is already a NEUTRAL cycle G(C) = 0 → LOSSLESS_CYCLE_CANDIDATE at the cell level; (b) type
     sufficiency q_type(Z)=q_type(Z') ⇒ same future readouts, else LOST_INFORMATION and enlarge 𝔗 (= U5 rule).
T1' [replaces T1; run when rg_m2 returns] Edge catalogue for W3 (and W1, W2, orthogonal-turn chain) gen 1→2:
     per fixture compute f (new nonzero descendant addresses inside the √5 cell), r^raw (defining relations +
     forced-zero relations), r^sound under convention A (outward = constraint) and B (outward = E), report
     g_A, g_B ∈ {DROP, NEUTRAL, EXPAND}. Then build the first type graph with the REANCHOR edge included and run
     an exact min-cycle-mean (integer weights). Codes: INTERIOR_RIGID / LOSSLESS_CYCLE_CANDIDATE /
     EXPANDING_CYCLE_CANDIDATE, never Clay-D. Script: `rg_type_graph.py` (to write).

## Addendum (founder CTX ~11:55 RC-ACYCLIC, ~12:10 monodromy split)
U11. RC-ACYCLIC: kill zero-cost cycles logically first (𝒢₀ = productive ∩ exact ∩ D=0 ∩ nonterminal ∩ no-exit edges;
     finite alphabet + acyclic ⇒ m_int ≤ M−1), quantitative δ only afterwards via G4 + l.s.c. ACCEPTED as the cleaner
     form; RC-CYCLE (positive weights) demoted to fallback. Load moves entirely to RC-TYPE (finite reader-sufficient
     alphabet — a quotient claim = RS) and RC-PROD-NOV. REANCHOR edge must still be in 𝒢₀'s edge set.
U12. RC-PROD-NOV = RG-MONODROMY-DETECTION (𝔐_C ≠ Id + sufficiency ⇒ NOVELTY ∨ LOST_INFORMATION; abstract, same
     shape as the RNO Coq lemma with add Z ξ replaced by 𝔐_C — content-free, extend RG_GCD_RNO.v) +
     RC-IMR Identity-Monodromy Rigidity (𝔐_C = Id ∧ D=0 ∧ E=0 ∧ productive ⇒ TERMINAL/DEGENERATE; = §114.1 generative
     constraint accumulation / CR₀ ⊆ P∪D in monodromy form; Clay-load-bearing). FIRST EXACT INSTANCE ALREADY EXISTS:
     T1′/rg_m2 on W3 — the 1-step identity-monodromy system (all in-cell sources cancel, Ξ=0) has productive solution
     set ∅ under all three conventions, i.e. 𝓜_C⁰ ⊆ 𝒟 for one-generation W3-type cycles. Not yet: multi-generation
     cycles, other seed types, ∂₊.
T8  Extend RG_GCD_RNO.v with RG-MONODROMY-DETECTION (ledger map form). Small.
T9  Add vault cards RG-MONODROMY-DETECTION (OPEN/abstract, likely provable) and RC-IMR (OPEN, Clay-load-bearing,
     first exact instance = T1′ W3 gen 1) AFTER workflow wf_c25e22de-442 completes (cards not in its prompts).
T10 IMR depth-2 on W3: propagate a concrete productive W3 seed one generation (actual descendants, not the zero-
     novelty variety), then ask whether a 2-generation cycle can return Ξ=0 with D=0: compute V(I_2) ∩ {productive}.
     RAM: sympy only, expected < 1 GB; cap 3 GB.

## Addendum (founder ~12:20–12:35: GLOBAL-MONODROMY-CLOSURE, FPR/NPSC, IRM/ESC/UCR/ER chain)
U13. Chain ER ⇒ UCR ⇒ IRM ⇒ NPSC ⇒ FPR ⇒ IMR ⇒ interior G6, with RG-MON for the 𝔐≠Id branch. Accepted as the
     working spine. Cautions recorded: (a) the annihilating-polynomial / spectrum step treats 𝒩_Z as linear on the
     module; the generator is quadratic, so UCR is only meaningful for the linearised generation about a populated
     state — say so on the card; (b) the closed 3-mode truncation has an exact periodic productive orbit at D=0
     (validated Taylor integration, first return t*∈(1.82,1.84)) — a unit-circle orbit — excluded from 𝒢₀ only because
     E≠0 (it forces 6 outside addresses). So UCR/ER content = E=0 self-closure = NPSC; nothing extra; (c) T1′/M2 kill
     SEED-EXPANSION identity cycles (formal-time: order-dt novelty cannot be cancelled by order-dt²), NOT populated
     cycles; populated self-closure is what the NPSC sweep tests.
DONE rg_imr_structural.py: structural NPSC/IMR — a finite negation-closed address set that is self-closed for ALL
     amplitudes is collinear (⇒ degenerate). 3-line proof (p,q non-parallel ⇒ p+q, 2p+q, … ∈ S, infinite) + exhaustive
     PASS on 597,618 sets in [-2,2]³ up to 8 addresses. Tier: finite_diagnostic (exhaustive) + Dr (general proof).
RUNNING NPSC populated sweep (agent): all small address sets |S|∈{4,6,8} in [-1,1]³ (then [-2,2]³), generic ⊥
     amplitudes, variety {all outside forcing = 0} ∩ productive — this IS the depth-1 RC-EQUALITY-RIGIDITY probe.
     Verdicts per set: SELF_CLOSED_PRODUCTIVE (falsifier candidate) / NOT_SELF_CLOSED / TIMEOUT.
T11 If any SELF_CLOSED_PRODUCTIVE appears: realization audit (is the point a genuine state of the exact stepper for
     all time, i.e. invariant, not just instantaneous?) before calling it a falsifier. If none: state
     NPSC-depth-1-small-box as finite_diagnostic and plan depth-2 (time-invariance of the closure, not just instant).

U14. (founder ~12:55) RC-SCWR as finite certified attack: fix simple cycle word ω, algebraize all equalities
     F_ω(x)=0, inequalities G_ω≥0, productivity P·s²−1=0, nondegeneracy N·t²−1=0, gauge 𝒱=1 + H=0; ask 𝒮_ω = ∅?
     with exact certificates (UNSAT_CERTIFIED / SAT_CERTIFIED / UNRESOLVED); RC-TYPE finite ⇒ finitely many simple
     words ⇒ interior G6. ACCEPTED as the execution form of NPSC; NPSC m=1 sweep = 𝒮_ω for m=1 already; missing piece
     = cofactor certificates (R1-b) and m=2 time-invariance (R1-c). Ordering now in TODO_RC_LANE_v2_2026-09-12.md.

U15. (founder ~13:10) RC-APC / RC-FRPA: source-lifted ordered ledger with pointed cone K; APC1–4; FRPA
     A_r + S_r = A_{r+1} + T_r + E_r + D_r all in positive cones; identity monodromy ⇒ Σ U ξ_r = 0 in pointed cone ⇒
     all ξ_r = 0 ⇒ nonproductive — kills identity cycles of every length at once. AUDIT: the cone algebra is correct
     and content-free; ALL content sits in (i) APC4 / resolve-map soundness — a cancelled pair may be terminalized
     ONLY if it has no future relevance; W3 shows the gen-0 cancelled target k is NOT terminal (it feeds the gen-1
     constraint ideal), so resolve cannot terminalize it and the active ledger grows — which is the forbidden
     time-counter trick unless "active" = future-separating, i.e. reader sufficiency (RS) again; (ii) transport
     positivity U K ⊆ K under REANCHOR is unproven (cross-cell budget fixture). Verdict: FRPA is a proof SHAPE for
     IMR; it does not replace the m=1,2 computations, it says what M3 must certify per witness (the four tests the
     founder listed). Ranked R3 (soundness layer) in TODO v2, not R1.
DONE R1-b: rg_cert_w3_nullstellensatz.py + rg_cert_check.py — exact certificate 1 = u²·Σa_j f_j − (uC₁−1)(uC₁+1)
     with 6 generators (2 in-cell targets p1−q2, p1−p2 + datum C₀=C₁=C₂), cofactors in ℚ(√3), degree ≤ 2, found by
     Macaulay-matrix linear algebra (1890×1092 over ℚ); checker only expands. First UNSAT_CERTIFIED of the lane:
     W3 has no productive zero-novelty gen-1 extension under ANY exit convention.
NPSC box-2 size-3 (agent, partial): 20 SELF_CLOSED_PRODUCTIVE all degenerate 2-address support; pair-kernel
     nonempty exactly for the 24 equal-norm pairs, never for 97 unequal-norm pairs (= rank-1 iff |p|=|q| lock).

U16. (founder ~13:25) FRPA hole fixed by the founder: nonterminal ⇏ T_r = 0; identity cycle gives Balanced Turnover
     Σ U S_r = Σ U T_r, not S_r = 0. Terminal tokens need a finite resolution certificate (Resolve = PASS) else
     UNRESOLVED. Recurrence ⇒ nonzero positive circulation on a turnover graph 𝒢_turn; DAG ⇒ none; a cycle needs
     an admissible positive fixed vector M_C x = x, x ∈ K∖{0} (RC-POSITIVE-CIRCULATION-RIGIDITY, PCR). AUDIT: correct
     self-correction (this is exactly the objection in U15); PCR is the Perron–Frobenius form of the type graph with
     positive weights — same object as T1′'s type graph + REANCHOR edge; M_C is again a linearisation (caveat U13a).
     Concrete first 𝒢_turn: the rg_run1 lineage/hand-off data already give per-generation birth counts (4,4,8,16,32,64)
     and cancel/net ratios per hand-off — a weighted generation graph. Ranked R2-a′ (merge with RC-TYPE probe).
DONE R1-d: RS readout — see R1D_RS_READOUT_2026-09-12.md. Q(i) INSUFFICIENT_RESOLUTION (A/B ≤ 1.13, decreasing with
     cutoff), Q(ii) PASS (cancel share dominates hand-offs), Q(iii) PASS at this resolution.
LESSON: a background waiter that greps its own pattern (`pgrep -f rg_run1_driver.sh` inside a command containing that
     string) never exits / gets killed (exit 144). Use a pid file or `pgrep -x`.
DONE R2-a′ (first 𝒢_turn, W3 gen 0→1; rg_turn_graph_w3.py/.json): nodes {P,Q,K,SEED,IN[3/4],IN[7/4],IN[9/4],EXIT};
     edges K+P→EXIT×6/SEED×6, K+Q→EXIT×6/SEED×6, P+P→IN[7/4]×6/IN[9/4]×6, Q+Q same, P+Q→EXIT×18/IN[3/4]×12/SEED×6.
     Every directed cycle passes SEED (feedback needs the k class). Zero-birth circulation would need all IN[*] = 0
     on a productive seed → refuted by the certificate ⇒ PCR holds at depth 1 for W3 (certified). Depth ≥2 needs
     the populated-state graph (R1-c), not the seed catalogue.

U17. (founder ~14:20) RC-DUAL-DESCENT / RC-DUAL-SEPARATION: instead of hunting cycles, find y_v ∈ K_v*, η>0 with
     ⟨y_w, M_e x⟩ ≤ ⟨y_v, x⟩ − η ℓ_e(x) on every productive edge; chaining around any cycle with M_C x = x forces
     Σ ℓ = 0 ⇒ degenerate/terminal/exit ⇒ PCR for all lengths at once; primal–dual (SAT witness vs UNSAT dual
     certificate); Farkas/Gordan alternative in the polyhedral case; per-cell piecewise potentials glued at
     registered transitions; potentials must be built from declared readers/lineage/grammar only (no R_j→0, no H¹).
     AUDIT: (a) correct Lyapunov/dual shape; content = existence of ℓ_e with ℓ_e = 0 ⇔ no independent future-relevant
     consequence — this is NPSC in local form (same gate, now stated as a functional). (b) M_e is bilinear in
     amplitudes, so the cone/linearity needed for Farkas holds only on the SOURCE-LIFTED COUNT LEDGER (births per
     address), not on amplitudes; on that finite type graph the dual potential IS the Karp/Bellman-Ford potential h of
     U10 (RC-CYCLE): a potential exists ⇔ no cycle of nonpositive weight — so DUAL-DESCENT and RC-CYCLE are the same
     theorem in two languages (primal = negative/zero cycle, dual = feasible potential). Computable now on
     𝒢_turn(W3) once the REANCHOR edge weight is declared (R2-b) — without it the alternative returns "primal" via
     the budget fixture (G(C) = 0 at cell level). (c) The exact fixture T/D = 20 (generation ≫ loss at a productive
     state) shows no energy-type Φ can descend per step; any admissible Φ must be ledger/lineage-based — consistent
     with the founder's ban on H¹/regularity inputs, and a useful negative filter for candidate potentials.
     Ranked: R2-b′ (compute the Bellman-Ford dual potential on the weighted type graph after REANCHOR weight;
     output CERTIFICATE (potential table) or PRIMAL (nonpositive cycle) — both exact integers). Vault card:
     RC-DUAL-DESCENT (OPEN, alias RC-DUAL-SEPARATION, see_also RC-CYCLE, RC-PCR) — to add at next vault pass.

U18. (founder ~14:35) Two-attack lock: PRIMAL (exact positive recurrent circulation M_C x = x) vs DUAL (globally
     glued descent certificate, CERT-e: y_v − M_eᵀ y_w − η c_e = A_vᵀ λ_e, λ_e ≥ 0; polynomial cells via
     Positivstellensatz; GLUE condition Φ_β(h x) ≤ Φ_α(x); dual holonomy obstruction on chart cycles; theorem of
     alternatives RECURRENT WITNESS ⊕ DESCENT CERTIFICATE; "no certificate at degree d ≠ counterexample → UNRESOLVED").
     AUDIT (one substantive point beyond U17): a per-EDGE weighted graph is the WRONG primal object. In 𝒢_turn(W3) the
     feedback edges K+P→SEED, K+Q→SEED, P+Q→SEED have zero births, so Bellman-Ford on per-edge weights would report a
     zero-weight cycle SEED→{P,Q,K}→SEED — yet T1′ certifies that any productive seed step ALSO forces ≥18 in-cell
     births in the same step. Edges of one generation are not independent choices; the transition is the whole step.
     Hence: (i) the finite-graph Farkas alternative is valid only when a NODE = whole-state type and an EDGE = one
     full generation step (the RC-TYPE alphabet, not the target-class graph); (ii) below that aggregation the honest
     primal is the cycle-word system 𝒮_ω of U14 (semialgebraic) and the honest dual is the Positivstellensatz
     certificate — exactly what rg_cert_w3_nullstellensatz.json already is for ω = one W3 step (a degree-2
     Nullstellensatz certificate = a dual certificate with η-term absent). So the founder's engine is already
     running at m = 1; the missing piece for m ≥ 2 is the populated-state step (T0-02 run, R1-c), and GLUE =
     REANCHOR weight (R2-b) remains the open input. No new rank; folded into R1-c / R2-b / R2-b′.
     Vault: add RC-DUAL-DESCENT with note "per-edge graph insufficient; state-type aggregation required" and the
     duality principle PRIMAL MONODROMY ⊕ DUAL HOLONOMY as RG-DUALITY-PRINCIPLE (OPEN, domain-neutral).

U19. (founder ~14:50) Occupation-flow primal/dual + fail-closed outer relaxation (RC Certified Primal–Dual
     Refinement, CEGAR-style): event lift (K_e, P_e, Q_e, p_e); primal (P): z_e ∈ K_e⁰, Bz = 0, p(z) = 1; recurrence ⇒
     occupation flow via Cesàro/S_N→∞ or ZPR (p = 0 ⇒ T∪D∪E); dual (D): ⟨y_t,P_e z⟩ − ⟨y_h,Q_e z⟩ ≥ η p_e(z) on K_e⁰ ⇒
     0 ≥ η contradiction; polyhedral CERT with λ_e ≥ 0; outer relaxations K^exact ⊆ K^(r) refined by cuts from
     W-fixtures; DUAL on a superset is a proof, PRIMAL on a relaxation must pass exact realization; nontermination ⇒
     UNRESOLVED; RC-TYPE may be replaced by a finite SOUND outer event grammar (inclusion proof only).
     AUDIT: (a) This is the correct fail-closed engine and it absorbs U14/U17/U18 (LP relaxation + cutting planes;
     dual on an over-approximation is sound). ACCEPT as the execution architecture for G6-interior. (b) Every cut
     H_r ≥ 0 must be PROVEN for all exact events, not read off one fixture — a fixture-only cut breaks the inclusion
     and silently turns the "proof" into a heuristic; the vault must carry an inclusion certificate per cut.
     (c) ZPR as stated is definition-level: p(Z) = 0 ⇔ every pair interaction vanishes, which is how class D is
     defined; it carries content only if 𝒟 is defined independently (e.g. collinear/rank-1-locked polarizations) —
     the structural lemma rg_imr_structural.py + the rank-1-iff-equal-shell fact are the independent definition.
     (d) The Cesàro step needs G4 (bounded normalized states) explicitly — recorded as the dependency.
     (e) The first outer relaxation cannot be built from gen-1 data alone: at the type level the IN-classes are pure
     sinks until gen-2 event types exist, so (P) is trivially infeasible = INSUFFICIENT_RESOLUTION, not a G6 result.
     Hence the event lift waits for the populated T0-02 run (event types observed at gen ≥ 2), then: K^(0) =
     polyhedral cone on event counts with balance B, p = births; exact rational LP (small; fractions simplex);
     DUAL_CERTIFIED / PRIMAL → realization check against 𝒮_ω / SPURIOUS → cut with inclusion proof.
     Ranked: R1-e (after T0-02). Vault: RC-OCCUPATION-FLOW-PD (OPEN, engine) + RC-ZPR (definition-level, note).

U20. (founder ~15:10) Global event automaton over strata I/L/U with ONE occupation-flow primal (P-global: Bz=0,
     d=0, x=0, p=1) and ONE global dual (GD); lower-boundary estimate encoded as edge inequalities; W1–W3 as cuts;
     UBRR reduced to "refine only the upper states that obstruct the dual"; theorem of alternatives on rational
     polyhedral K^(r); dual may give finite horizon m_* ≤ Φ_max/(η p_*)+1 once p_* > 0 from compactness + ZPR.
     AUDIT: (a) consistent extension of U19; adopt as the engine spec (event lift z_e = (Z⁻, Z⁺, Ξ, R, Γ)).
     (b) U-stratum: "sound outer abstraction" is the whole hole in new clothes — a sound K_U^outer with only sign/
     ledger constraints will almost certainly admit a fake U→U flow; every cut that kills it needs an inclusion
     proof for ALL diffuse states, which is UBRR content. The reduction is real only in that it tells us WHICH
     diffuse facts are needed (those that obstruct the dual) — strategic, not a shortcut. Keep RC-UBRR OPEN.
     (c) The L-edge inequality G_M ≲ A^{1/2} 2^{-M(β−η)} presupposes A bounded (RS/G4): the lower certificate is
     conditional on RS; record the dependency edge in the vault.
     (d) In P-global, x(z)=0 excludes registered exits; the cross-cell REANCHOR must therefore be an I→I edge with
     x=0 and d>0 (paid) or an explicit exit — either way the budget-fixture cycle is NOT a zero-defect circulation,
     consistent with audit §8 case 3. This finally fixes the REANCHOR convention question inside the engine:
     REANCHOR = transport edge with declared d_e (payable) — so answer (c)/(b) of my earlier ask, not (a).
     (e) Finite horizon from the dual needs p_* > 0 — founder's own caveat; unchanged.
     Ranked: R1-e spec updated to GLOBAL (strata as vertex classes; U edges start with the coarse sound cone and
     are refined only by proven cuts). Vault: RC-GLOBAL-EVENT-AUTOMATON (OPEN, engine), edge RC-G6-LOWER → RC-G4.

U21. (founder ~15:25) RC-OCC-SOUND (exact recurrent core ⇒ outer primal feasible; contrapositive: outer primal
     UNSAT ⇒ no exact recurrence), obligations G4 + ZPR + event commutation (COMM) + outer soundness; layered cuts
     C^(0) ⊂ … (W1, W2, W3, lineage, FAR, diffuse); record supp(z) and dual slack σ_e per round; primal SAT needs
     REALIZATION (occupation mixture ≠ trajectory); "design the abstraction so DUAL wins". AUDIT: correct; the
     asymmetry (dual = proof, primal = candidate) is the right reading; OCC-SOUND's proof needs the Cesàro limit to
     stay inside a CLOSED outer cone — closedness of C^(r) must be part of the inclusion certificate.
DONE R1-e round 0 (rg_occ_c0_w3.py/.json): coarse C^(0) on the count ledger with W3 gen-1 exact counts
     (E_S: 1 SEED → 14 SEED + 24 IN + 30 EXIT) and the unknown gen-2 IN-step outer-free. Zero-exit forces z_S = 0;
     the relaxed primal is feasible with support {E_IN: IN→IN self-loop}, p = 1 — SPURIOUS BY CONSTRUCTION. The
     primal "runs away" exactly into the unknown gen-2 events; first required cut H_gen2 = exact gen-2 event
     catalogue on a populated W3 state (T0-02 run). No dual possible before that cut.

U22. (founder ~16:20) C0 re-based on old core only: Z=(S,μ,C,A,B,Ω,I) from P2 Standalone; admissible transition =
     weld/M.02 (T1,T2) + Genesis ε_dyn=ε_read=ε_inv=0 (T3) + weld/E.06 sufficiency (T4); NS exact constraints
     NS-CANCEL (DERIVED) and NS-SELF (DERIVED EXACT) as cuts; dead shortcuts (orthogonal-turn ⇒ contraction;
     productive two-step ⇒ preselected cross pair nonzero) excluded; C0 = weld ∩ reader ∩ invariant ∩ lineage ∩ cancel ∩
     exact-local, and G4/G6/G7/UBRR/uniform-ancestry NOT encoded; sectors 𝒯 = ℒ_M ∪ ℱ_M ∪ ℬ_M; occupation/Farkas parked
     as PROPOSAL; next = LOCAL: assemble NS-CANCEL + NS-SELF + full local convolution into a minimal OCSR obligation
     and find the single missing lemma. AUDIT: agreed; the LOCAL assembly already exists in executed form — T1′ /
     rg_m2 / rg_cert_w3_nullstellensatz (full local convolution on W3 gen 1: no productive zero-novelty extension, any
     exit convention) — so the "single missing lemma" for LOCAL is the populated-state closure at depth ≥ 2 (NPSC
     sweep box-2 s4 running; T0-02 gen-2 events pending). Rule REUSE-PIPELINE installed in CLAUDE.md / codex / gemini /
     the command-center AGENTS.md (that edit uncommitted).

U23. (founder ~16:35) TG-RFG-01 placed in Toledo by the founder (PRs #27/#120/#3/#54/#128 — founder-reported, not
     verified by this session). Focus locked on ONE missing piece: PROP-RC-LOCAL-WS-01 (WS-local):
     Z ∈ C0^old ∧ ProdLocal(Z) > 0 ⇒ FutureReadoutResponse(Z) > 0 ∨ RegisteredCancellation(Z) > 0 ∨ EXIT ∨ DEGENERATE.
     AUDIT + EVIDENCE: (a) first exact instance already holds — W3 gen-1: every productive seed (C≠0) has nonzero net
     response at an in-cell target under every exit convention (rg_cert_w3_nullstellensatz.json, UNSAT of the zero-
     response system); all 14 multi-source targets are rank 2 in t⊥ ⇒ RegisteredCancellation cannot absorb the
     response; the in-cell address carries load ≥ τ_res, so the declared cell reader (weld/M.03 horizon L ≥ 1) sees
     it ⇒ FutureReadoutResponse > 0. WS-local(W3, gen 1) = ADMITTED. (b) What the GENERAL statement still needs:
     (i) the same for every productive class in C0^old, not only the equal-shell three-triad datum — the NPSC sweep
     (box-2, |S| ≤ 8) is the enumeration of small productive classes and so far returns only degenerate hits;
     (ii) "future-relevant" beyond horizon 1: that the response is not resolved (T-channel) within the declared window
     — needs the Resolve certifier (R coordinate), currently UNRESOLVED in C0. So WS-local general = (NPSC small-class
     coverage) + (Resolve certifier). No new theorem opened.
DONE  Toledo local branch f06c39b8: 2 malformed proposal JSONs repaired (syntax only) + 3 NEW DERIVATION / PROPOSAL
     entries (26 proposals). NOT pushed. Command-center repo PR #116 opened (private repo) for the REUSE PIPELINE
     rule; that repo has an unrelated dirty DECISIONS.yaml (hook-written) so the checkout stays on the rules branch
     until the founder merges.
     Internal dir initialised as a local-only git repo (no remote), commit 2c58fb7; vault pass 2 agent running
     (DEFINITION status, 10 new cards, cancellation-parent correction, commit).

U24. (founder ~17:10) NS PR #55 (branch research/p2-witness-soundness-w123, MERGEABLE): three exact results —
     PROP-P3-CANCEL-CONSTRAINT-LIVE-W123-01 (W1 16/18, W2 42/44, W3 36/44 nonzero targets; cancel at k ≠ web
     disappears), PROP-P3-ANTIPODAL-CANCEL-OUTWARD-01 (k=(K,0,0), p=(0,P,0), q=(K,∓P,0): B_{p,q}=KPx e3,
     B_{−p,q'}=−KPx e3 cancel at k; cross pairs (K,±2P,0) carry ±KPx e3, outward), PROP-P3-ANTIPODAL-CANCEL-LADDER-01
     (q_j=(K,(2j+1)P,0), b_j=(−(2j+1)P c_j/K, c_j, z_j): B_{p,q_j}=+P c_j e3 to s_{j+1}, B_{−p,q_j}=−P c_j e3 to s_j ⇒
     interior cancellation forces c_j = c_{j−1}; finite strip ⇒ two boundary descendants; bi-infinite ⇒ |q_j|→∞).
     INDEPENDENT VERIFICATION (this session): all three checkers run PASS in a temp worktree; the four identities
     re-derived with sympy from the single coupling formula — exact match. Verdict on the mathematics: CONFIRMED.
     CAVEAT (must enter the claim boundary before merge): every wavevector of the antipodal family has k_z = 0 and
     the generated polarization is e3 only ⇒ the whole family is 2D3C = TERMINAL CLASS P (the same class as T0-01).
     So "boundary novelty ∨ scale escape" is proven INSIDE the class the G6 theorem excludes; it demonstrates the
     constraint-propagation mechanism exactly but is not evidence about the productive non-planar sector. The
     founder's next target (strip boundary + arbitrary external cancelling triad) must require k_z ≠ 0 for at least
     one external address, otherwise it stays in 𝒫. Recommend: add "family ⊂ class P (2D3C)" to the two papers'
     claim boundaries and to the three proposal cards; then merge.

U25. (founder ~18:20) PROP-P3-CROSS-FAMILY-BOUNDARY-CANCEL-01 (PR #55 extended, CI green per founder): null-locus rule
     (R): B_{p,r}(e3,u)=0, u≠0 ⇒ z=0 ∨ |r|=|p| (anchor p=(0,P,0), a=e3); det L_r = z²(|r|²−|p|²)/|p+r|²; external
     triad r+t=s cancelling the e3 boundary source with z≠0 forces |r|=|t|=|p| ⇒ equal-shell direction lock
     B_{r,t} ∥ r×t, horizontal part z²(K²+L²)>0 ⇒ not ∥ e3 ⇒ contradiction ⇒ PLANAR recruitment ∨ OFF-PLANE novelty
     at p+r or p+t; rational non-vacuity s=(1,2,0), r=(1,0,1), t=(0,2,−1).
     INDEPENDENT CHECK (sympy, this session): null locus of L_r CONFIRMED exactly (det ∝ z²(|r|²−P²)); the exact
     determinant differs from the stated formula by a normalisation: with orthonormal bases on r⊥ and (p+r)⊥ the
     area ratio is z²(|r|²−P²)/(|r|·|p+r|), not /|p+r|² — convention-dependent (matrix in non-orthonormal bases), the
     zero locus is unaffected; flag for PR #55 wording only. The rational example was not re-verified here (CI
     checker reported success). Dichotomy logic CONFIRMED.
     SIGNIFICANCE: iterating (R) sends every 3D recruit to the anchor shell |r|=|p| — equal-shell constraint
     accumulation on a compact sphere — which is exactly the W3-type configuration (three equal-shell triads at one
     target) whose gen-1 closure is already certified empty (rg_cert_w3_nullstellensatz.json). So the founder's next
     iteration lands on the object we have: the populated equal-shell web at depth ≥ 2 (NPSC / T0-02). No new object.

U26. (founder ~19:10) PROP-P3-RANK2-SELFCLOSURE-PLANARITY-01: for a=α(n×p), b=β(n×q): n·B_{p,q}(a,b) =
     2αβ[n·(p+q)][n·(p×q)]²/|p+q|²; n·(p×q)=0 ⇒ B=0 (nonproductive, not a loophole); productive output in W=n⊥ ⇒
     n·(p+q)=0; reuse of self-closure (DERIVED EXACT) then forces p,q,k ∈ W or an escape from W ⇒ dichotomy ESCAPE W ∨
     PLANAR ∨ DEGENERATE; rational witness p=(1,0,1), q=(0,2,−1), B=(−12/5, 6/5, 0). INDEPENDENT CHECK: identity
     CONFIRMED symbolically; "n·(p×q)=0 ⇒ B=0" CONFIRMED on 39 random rational cases with q ∈ span(n,p) (a first test with a WRONG parametrisation q = sp + t(n×p), which does not satisfy n·(p×q)=0, produced a spurious counterexample — corrected; symbolic simplify does not close, numeric exact does);
     rational witness reproduced exactly. Next founder target = plane-switching loop W_0→…→W_m=W_0 with zero defect =
     the populated-web recurrence question again (NPSC/T0-02 object).

U27. (founder ~19:30) "YOU ARE HERE" map: local rigidity chain closed up to rank-2 self-closure planarity; current gate =
     plane-switching compatibility (W_j → forced novelty outside W_j → ? → W_{j+1}: can a compact, productive,
     zero-defect, lineage-compatible web switch rank-2 planes forever while cancelling every novelty?); then global
     cancellation compatibility + WS, FNW/OCSR, G4, G6, G7, R_N→0, adapter, Clay. AGREED with one alignment note: the
     plane-switching loop IS the populated-web recurrence object (NPSC / T0-02 / occupation primal) — the same gate
     seen from the polarization side; no new machinery, the next computation is the depth-≥2 populated closure on a
     web that is allowed to switch W, which the T0-02 stepper produces automatically (it does not fix a plane).

U28. (founder ~20:40) PR #56 (research/p2-plane-switch-capacity, 17/17 CI pass, MERGEABLE): PROP-P3-PLANE-SWITCH-
     CAPACITY-01 (three retained novelties in a rank-2 plane ⇒ det[c1 c2 c3]=0; W_{j+1} locked by two independent
     lineages ⇒ a genuine switch must replace/resolve a basis lineage or exit) and normal/lineage reconstruction
     n_j × n_{j+1} = det[c_j,c_{j+1},c_{j+2}] c_{j+1} (★) ⇒ [c_{j+1}] = [n_j × n_{j+1}] ⇒ the normal loop determines
     the lineage loop; FNW entrance: T_loop must fix [n_j × n_{j+1}] at every step, else holonomy obstruction.
     INDEPENDENT CHECK: (★) CONFIRMED symbolically (it is the standard (a×b)×(c×d) = [a,b,d]c − [a,b,c]d identity
     with b = c); the det = 0 statement is elementary. Value = reformulation only (no new content), correctly labelled
     PROPOSAL. Next founder target: projective normal-loop holonomy — this is §114.2 in the vNext (T_loop(λ) = λ),
     already carded (FW / holonomy); reuse its statement, do not re-derive. Suggest merging #56 after the Toledo
     lookup line for "§114.2 projective transport" is added to both papers.

U29. (founder ~22:30) Big map v2 + CURRENT ATTACK VECTOR locked (NORMAL LOOP → HOLONOMY → FNW/OCSR → G6). Recorded in
     MAP_v2_CURRENT_ATTACK_VECTOR_2026-09-12.md. Toledo: PR #29 (11 proposals) MERGED, review fixes PR #30 MERGED
     (process slip disclosed: #29 merged before fixes; corrected within the hour). NS #56 MERGED.

U30. (founder ~23:00) Type split H_P (projective polarization/lineage holonomy, §114) vs H_Φ (scalar phase-incidence
     holonomy, phase tax/packing) — no theorem links them; type guard PR #57 (MERGED by this session, 18/18 CI).
     Three-line projective rigidity (PGL(2,ℝ) fixing 3 distinct lines ⇒ identity) = PROP-P3-PROJECTIVE-THREE-LINE-
     RIGIDITY-01 — standard (PGL(2) is sharply 3-transitive), label correct. FNW split: A (M ≠ I ⇒ ≤ 2 returned
     classes ⇒ third returned lineage contradiction) / B (M = I hard equality branch). Phase side reuses packing
     tax Σ T_e ≤ Σ A_e − c₀P and the window charge; conflict-poor branch = response/cancellation ancestry.
     EXECUTED (rg_typeP_loop_transport.py, exact, §114.1 zero-cross transport T_e([a]) = [b], b ∈ ker of
     B_{k1,k2}(a,·) on k2⊥):
     (1) GENERIC EDGES CARRY NO TRANSPORT: on 40 random integer mode loops every edge had trivial kernel — consistent
         with the general-anchor nullity theorem (kernel iff a·k2 = 0 or |k1| = |k2|). So a Type-P loop is confined
         to ONE SHELL (or uses rank-0 edges a ⊥ k2 that collapse every class to [k1 × k2]). The Type-P recurrence
         question therefore lives on the equal-shell web — the same object as W3/NPSC.
     (2) EQUAL-SHELL LOOPS (m = 3..5, random samples): |k|²=9: 45 loops with 2 fixed lines, 2 with 0, 1 with M ~ I;
         |k|²=6: 43 / 9 / 0; |k|²=5: 40 / 11 / 1. Identity-monodromy loops EXIST: shell 9 symmetric 4-cycle
         [(2,−2,1),(2,−2,−1),(−2,−2,1),(−2,−2,−1)] (reflection-symmetric rectangle) and shell 5 planar 3-cycle
         [(−1,−2,0),(−2,1,0),(2,1,0)] (z = 0, class P). So branch B (M = I) is NOT empty: symmetric webs realise
         identity Type-P monodromy; branch A (≤ 2 fixed lines) is the generic case. Files: rg_typeP_loop_transport*.json.
     Decision on the Toledo "AI-vendor" leak-scan hits: the 4 hits in readout_ns_series_vol2-6.json cite an external
     organisation's publicly stated hypotheses as a SOURCE (third-party claim), not an author/credit of our work ⇒
     PUB-NO-AI-ATTRIBUTION does not apply; no cleanup PR. Recorded.

RESULT NPSC depth-1 populated (R1-a) COMPLETE: box [-1,1]³ (85 reps) + box [-2,2]³ sizes 3 (1,848 reps, 164 s) and 4
     (24,563 reps, 11,285 s): SELF_CLOSED_PRODUCTIVE hits 12 + 20 + 590 = 622, EVERY one with partial support
     (seed-expansion); fully-populated check: NOT_SELF_CLOSED for all 610 tested (12 + 20 + 590 - none skipped);
     TIMEOUT 0; NO_INSIDE_TARGET 23,045 + 1,807 + 67 (cannot be productive). Verdict: NO finite address set of ≤ 8
     addresses in [-2,2]³ admits a fully populated productive amplitude configuration whose outside forcing vanishes.
     Tier finite_diagnostic. This is NPSC / SCWR at depth 1 on that box; depth ≥ 2 and larger boxes not covered.
     Genesis code for Q-NPSC-depth1-box2: ADMITTED (weld/E.05). Files rg_npsc_results*.json; REPORT pending (agent).

U31. (founder 23:5x) Rulings on the four items: 1 GO (paper NS_P2_TYPEP_LOOP_TRANSPORT_FIXTURES.md, checker
     check_ns_p2_typeP_loop_transport.py, status split DERIVED/EXACT vs FINITE_DIAGNOSTIC vs EXACT FIXTURE / PROPOSAL,
     "identity branch non-empty" = DERIVED from exact fixtures, A3 NOT closed; boxed reduction non-rank-0 Type-P
     transport ⇒ |k1|=|k2|; rank-0 edge = projective collapse to [k1×k2], separate branch; no vendor-name cleanup).
     2 GO with wording: "third re-entered lineage candidate" [ℓ]_ret with (i) real full-convolution lineage path,
     (ii) joint reanchor back to the base fiber of M, (iii) reader-relevant after reanchor, (iv) [ℓ]_ret ∉ Fix(M);
     A1 obstruction: M≠I ∧ [ℓ]_ret ∉ Fix(M) ∧ D=E=T=0 ⇒ recurrence incompatibility. 3 GO: A3 Gröbner on the rectangle
     in two layers (symmetry-constrained → symmetry-released), full system (productivity + full-convolution closure +
     all D = 0 + E = 0); UNSAT kills the fixture only; SAT = algebraic candidate, not a trajectory. 4 GO-FREEZE /
     HOLD-RUN with the full freeze list (nu, u0, normalization, q, reader, M, tau_0, ancestry horizon, tolerances,
     seed, commit SHA) — done in FROZEN_INPUT_RECORD_T0-03. NPSC-depth1-box[-2,2]³ = ADMITTED / FINITE_DIAGNOSTIC with
     claim boundary (no depth ≥ 2, no larger box, not a theorem); founder's reading: most loopholes come from
     "forgotten descendants", consistent with full-convolution / no-silent-loss.
     Applied: PR agent re-briefed with the naming/labels; A3 script now two-layer; T0-03 freeze list completed.

U32. (founder ~00:30) PR #58 (research/p2-a1-two-line-escape, 19/19 CI): nonidentity Type-P classification by
     Δ_P = (tr A)² − 4 det A (0/1/2 real fixed lines); with plane-switch capacity (rank-2 recurrence needs ≥ 2
     independent classes): Δ_P<0 ⇒ no exact Type-P recurrence; Δ_P=0 ⇒ rank drop/degenerate; Δ_P>0 ⇒ two-line
     skeleton RetReturn(M) ⊆ {[ℓ+],[ℓ−]}. Shared-mode trichotomy (same plane / orthogonal turn / positive
     dispersion) reused; nonplanar orthogonal-turn patch ⇒ positive dispersion within ≤ 2 closure generations
     (s×t = (QR,−PR,−PQ)) unless the generated channel is suppressed ⇒ A1 hard residue = recursive suppression
     charging (= OCSR + global cancellation compatibility + WS), with the suppression alphabet ORTHOGONALITY ∨
     EQUAL-SHELL NULLITY ∨ EXACT MULTISOURCE CANCELLATION ∨ T/E/D (the anchor-cross nullity theorem shows a single
     cross silence needs a·q=0 ∨ |q|=|p|).
     INDEPENDENT CHECK: discriminant classification agrees with this session's exact fixed-line counts on 152/152
     equal-shell loops (Δ<0: 22, Δ=0: 2, Δ>0: 128) — so 22 of 152 sampled loops are excluded outright (elliptic),
     2 are rank-drop, 128 are two-line skeletons. MERGED #58 (delegated decision; mathematics standard + verified,
     all global items kept OPEN). Alignment: the suppression alphabet IS the M3 readout-to-defect map (S1) —
     build the M3 checker with exactly these four labels; the "third re-entered lineage" test stays as a
     certificate (sufficient, not necessary).

U33. (founder 00:4x) Rulings: 1 M3 GO now (multi-label bitmask, UNRESOLVED fail-closed, MSCANCEL = accounting not
     loss); 2 Toledo PR after #59 merges, pinned by merge SHA, ids PROP-P3-TYPEP-FIXEDLINE-CLASSIFICATION-01,
     PROP-P3-ORTHOGONAL-TURN-FULLCLOSURE-ESCAPE-01, PROP-P3-A1-TWO-LINE-ESCAPE-REDUCTION-01 + Type-P fixtures
     (statistics as FINITE_DIAGNOSTIC / EXACT_FIXTURE metadata); 3 card PROP-P3-RECURSIVE-SUPPRESSION-CHARGING-01 with
     the founder's statement and dependencies (§114.1, nullity, direction lock, cancellation ledger, A1 two-line, M3
     soundness); NPSC only as supporting evidence / falsification control. Order: M3 → card → T0-02 evidence → A3 ∥ G4.
DONE M3 checker (rg_m3_check.py/.json): W1 26 targets (10 suppressed: ORTH 8, EQSHELL 8, TED 8, MSCANCEL 2), W2 56
     (14 suppressed: 12/12/12/2), W3 point A 82 (26 suppressed: ORTH 16, EQSHELL 26, TED 16, MSCANCEL 2); UNRESOLVED 0;
     asserted: W1's k target is MSCANCEL without EQSHELL (two-shell), W3's k target is MSCANCEL ∧ EQSHELL.
OBJECTIONS raised by this session (founder invited objections):
  O1  The real 3-way Δ_P classification is a fixture-convention artefact: the physical Fourier coefficients are
      complex and §114.1 allows the complex fiber. Over ℂ, PGL(2,ℂ) has NO elliptic case — every M ≠ I has 1 or 2
      fixed points — so "Δ_P < 0 ⇒ no exact Type-P recurrence" does not survive once phases are retained; only
      "M ≠ I ⇒ ≤ 2 returned classes" (two-line skeleton) and the parabolic rank-drop case survive. The papers should
      state the field explicitly and not present the elliptic exclusion as a theorem about NSE.
  O2  Type-P transport is defined only on pairwise-null edges (ORTH/EQSHELL). MSCANCEL suppression (the W1/W2/W3 k
      targets: individually nonzero, net zero) defines NO T_e, so the whole holonomy machinery is blind to exactly
      the channel that carries the residue. A1 therefore cannot be closed through Type-P alone — consistent with the
      founder's own "recursive suppression charging" residue, but it should be said that the residue is the MSCANCEL
      channel specifically, and that its measure is D_acc/cancellation-ledger accounting, not holonomy.
  O3  "nonplanar orthogonal-turn ⇒ positive dispersion within ≤ 2 generations unless suppressed" is a dichotomy,
      not an exclusion; its content is again the suppression charge — do not count it as progress on G6 twice.

U34. (founder ~01:10) PR #60: PROP-P3-RECURSIVE-SUPPRESSION-CHARGING-01 (OPEN THEOREM CANDIDATE) + RSC-O two-anchor
     planarity: two anchors (p_i,a_i) with a1×a2≠0, one recruit (q,b) suppressing both via ORTH (a_i·q=0) ⇒
     B_{p_i,q}(a_i,b) = (b·p_i)a_i ⇒ b ⊥ p1,p2,q ⇒ det[p1,p2,q]=0 (wavevector planarity) and q ∥ a1×a2 = W⊥.
     Gap stated by the founder: single-O alternation (ℓ+,ℓ−,ℓ+,…) never producing a double-O. CHECK: elementary and
     correct (Leray projection fixes a_i because a_i ⊥ p_i+q). MERGED #60 (19/19). #59 conflict (ACK) resolved by
     merging main; MERGED #59 (5 commits, asserted on head). Toledo registration agent launched for #58/#59/#60
     (merge-gated per U33) with the O1 complex-field caveat written into the fixed-line entry.
     Note on the lemma's reach: it bites only at double-O events; the M3 data can count double-O vs single-O events
     per fixture — add to the M3 output (next M3 revision) so the alternation gap becomes measurable.

U35. (founder ~02:40) PR #63 RSC-O alternation transfer: (ALT-1) a genuine nonparallel single-O event copies the anchor
     projective line ([b]=[a]); (ALT-2) for an alternating pair, individual nullity of the cross descendant ⇒ |q|=|r|
     (E), since b ∥ a_+ and a_+·r ≠ 0 by genuine alternation; (ALT-3) O_+→O_− ⇒ novelty ∨ E ∨ C ∨ T ∨ parallel
     degeneracy; (ALT-4) infinite genuine alternation ⇒ E or C infinitely often — transfers the alternation
     sub-branch of RSC-O into RSC-E / RSC-C. CHECK: ALT-1/2 elementary and correct (needs p×q≠0, declared);
     checker PASS locally; claim boundary honest (RSC-O not closed; residues listed). MERGED #63 (after ACK merge with
     #61/#62). MERGED #62 (M3 checker in NS; W1 N_{O,1}=8/N_{O,≥2}=0, W2 12/0, W3 14/2 — the two double-O targets of
     W3 are ±k, rank 2 from the three horizontal anchors; committed __pycache__ removed before merge).
     Consequence for the queued single-O Gröbner (m=2,3): by ALT-1/ALT-3 its SAT set is expected to be forced into
     E or C at the cross target; the run now serves as an exact confirmation of ALT-3 on the fixed skeleton rather
     than an open falsifier — keep it queued, downgrade expectation.

U36. (founder ~03:00) Narrative of #63 (merged, U35) + RSC-O residue table: A double-O → planarity; B switching single-O →
     RSC-E/RSC-C; C one-sided single-O persistence (NEXT); D parallel degeneracy (separate). SESSION CONTRIBUTION to C
     (exact, 2-line): under one-sided O_+ persistence every recruit has q_j ∈ a_+^⊥ and [b_j] = [a_+] (ALT-1); for
     any two such recruits (b_i·q_j) = (b_j·q_i) = 0 (polarization along the plane normal, wavevectors in the plane)
     ⇒ B_{q_i,q_j}(b_i,b_j) ≡ 0 — verified symbolically. So the one-sided recruit set is MUTUALLY SILENT: its members
     never interact with each other; all productivity must pass through anchor–recruit or anchor–anchor channels,
     and anchor–recruit channels on the O_+ line are suppressed by construction. Hence branch C reduces to: the
     productive core is the anchor pair + O_−-side descendants only, and the recruit cloud is a passive, non-
     interacting layer (the 2D3C-like structure: wavevectors in a plane, polarization normal to it). Proposal name
     suggested: PROP-P3-RSC-O-ONE-SIDED-SILENT-LAYER-01 (for the founder's next PR; not registered here).

U37. (founder 03:1x) Rulings: 1 three-line rigidity → Toledo GO; 2 tier Dr accepted + evidence_kind metadata
     (EXACT_FIXTURE / FINITE_DIAGNOSTIC), Dr ≠ global theorem; 3 Toledo pass GO: #61 = caveat append only, #62 = M3 as
     checker/interface, #63 = alternation transfer, all pinned to merge SHAs; 4 queue CONFIRMED with silent-layer
     paper/checker done now (no compute): A3 → silent-layer → single-O m=2,3 → M2; 5 orthogonal-turn amplitudes into
     M3 GO with assertions (k·u=0, exact field, same Fourier–Leray operator, provenance commit), status EXACT FIXTURE /
     FINITE DIAGNOSTIC; 6 silent-layer lemma PR GO by this team, id PROP-P3-RSC-O-ONE-SIDED-SILENT-LAYER-01, wording
     "2D3C-like passive layer with respect to internal recruit–recruit interactions", reduction "all persistent
     productivity must cross the layer/core interface", next box: passive O_+ layer + active O_- core ⇒ double-O ∨ E ∨
     C ∨ novelty/exit (OPEN). T0-02 over cap ⇒ UNRESOLVED per record.
     LAUNCHED: agent A (NS PR silent-layer + NS PR orthogonal-turn M3 fixture), agent B (Toledo pass for #57 three-line,
     #61 caveat, #62 M3, #63 alternation, evidence_kind). T0-02: A d2 485 s, A d3 4732 s, B d2 466 s all rc=0; B d3
     running; system swap 9.9 GB used (not our process) — no parallel compute.

CHECKPOINT T0-02 (rg_t0_02_REPORT.md, all finite_diagnostic): all four runs completed within cap (A d2 483 s, A d3 79 min,
     B d2 464 s, B d3 84.5 min — B d3 stopped by maxwall exactly at the declared horizon T=3.21, so it is NOT
     UNRESOLVED; correction to the earlier note). Validation: datum forcing 0 exactly; gen-1 address set = catalogue
     82/82, live 68/68; pair-sum vs brute force 1.6e-15; energy identity 1.4e-11 at dt 1e-3 (d2 production 1e-11 OK;
     d3 production 1e-8 — registered defect, tolerance 1e-10 not met at d3).
     Readouts: A/B(T0) rises along the cascade 0.77 → 6.8 (d2) → 10.2–10.6 (d3), cell 2 ×2 from d2→d3 (not converged);
     retained load 14 → 250 while energy 7 → 5.2 (forward cascade emptying cell 0 in 1–3 time units); point B = point A
     within 5–10 % (no phase dependence); α_total 14–26 everywhere (≫ 0.632); D_acc = 0 to 4e-15 (accounting closes);
     cancellation-deficit fraction 0.91–0.97 at every hand-off (source ledger 10–30× net); turnover: S>0 only in
     window 0 (inventory saturates by t=0.025), Dropped = T = U = 0, E_r/B up to 315, no E=D=0 window ⇒ no PCR
     falsifier. Codes: (i) INSUFFICIENT_RESOLUTION, (ii) D_acc PASS_fd / α NO_CLOSURE, (iii) NONE_OBSERVED.
     Anomaly screen: no contradiction, no exact counterexample. Two WATCH items (not stop): (a) cancellation deficit
     ≈ 0.95 — nearly all source activity cancels; structural cause unknown (readout only); (b) non-convergence in d —
     the depth-2 exit is not small after t≈0.3, so the gen-2 catalogue is d-dependent; M2 round 1 must carry d as a
     declared parameter, not average over it. Proceeding automatically: A3 → single-O → one-sided → M2.

RESULTS A3 / single-O / one-sided (exact Gröbner, fixed skeleton p+=(1,0,0), a+=(0,1,0); p−=(0,1,0), a−=(0,0,1);
     core k = p+ + p− = (1,1,0) with free c ⊥ k; denominator-cleared projection; all saturations as ruled):
  A3 shell-9 rectangle ±{(2,−2,±1),(−2,−2,±1)}: NO_INSIDE_TARGET — no pair sum lands on a registered address, so the
     identity-monodromy web has no internal productivity at all; every interaction is a registered exit ⇒ it cannot
     be a zero-exit productive recurrent web as it stands (branch-B fixture resolved by structural openness, not by
     UNSAT of the intended system; adding the exits changes the web and its loop).
  single-O alternation m=2,3: with the core address allowed EMPTY → SAT (the forgotten-descendant loophole: the
     productive core triad forces k but k carries no load); with the core POPULATED (c ≠ 0 saturated) → UNSAT for
     m = 2 and m = 3 — exact confirmation of ALT-3 on this skeleton.
  one-sided O+ layer + active O− core m=1,2: same pattern — SAT unpopulated (witness q=(0,0,±1), c=0), UNSAT once
     the core is populated ⇒ the founder's next box (passive O+ layer + active core ⇒ double-O ∨ E ∨ C ∨ novelty)
     holds on this fixture for m ≤ 2.
  Slip: the queued waiters self-matched their own pgrep pattern (same bug as 2026-09-12) and never fired; killed by
     PID and the chain run directly (seconds). Lesson re-logged: never `pgrep -f` a string present in the waiter.
  M2 round 1 agent launched on the T0-02 catalogue (d as declared parameter).

RESULT A3-closed (rg_a3_rectangle_closed.py, exact): rectangle + one sum layer = 26 addresses; NO_CLOSURE_THROUGH_DEPTH_2
     (110 sums still leave the web); INVARIANT M_old = I confirmed; new equal-shell loops in the enlarged web: shell 9
     m=3 → 24 loops with 1 fixed line, m=4 → 78 (1 line) / 102 (2 lines) / 24 identity; shell 16 m=4 → 2 identity;
     shell 20 m=3 → 24 elliptic / 24 hyperbolic / 16 identity, m=4 → 78 / 102 / 24 identity; shell 32 → 2 identity.
     Populated (all-active) productive zero-outside-novelty on the enlarged web: UNSAT (System A only — the
     accounting-complete disjunction over 13 half addresses is 2^13 systems, not run). Reading: identity loops are
     abundant inside the enlarged web (they come from the reflection symmetry), so branch B is NOT resolved by
     enlargement; what is resolved: the enlarged web still cannot be an all-active zero-exit productive web at
     depth 2. NS PR #66 (forced-address accounting rule + 3 fixtures, System A/B) MERGED (20/20).

RETRACTION (from the PR #66 independent review, verified by the maker agent and recorded in the merged paper):
  R1  My claim "single-O m=2,3 SAT when the core is empty = forgotten-descendant loophole" was WRONG: the Gröbner
      basis of that SAT system contains z0²+1, q0_2 + z0 — the only solutions are COMPLEX isotropic recruits
      q0 = (0,0,±i) with k·k = 0 where the denominator-cleared projection degenerates. With t·t ≠ 0 saturated the
      single-O ansatz is UNSAT in System A, System B and the forgotten system for m = 2, 3. The real witness
      q = (0,0,±1), c = 0 belongs to the ONE-SIDED fixture m = 1 only.
  R2  My claim "the founder's next box (passive O+ layer + active O− core ⇒ …) holds on this fixture for m ≤ 2" was
      WRONG: System A is already refuted at m = 0 — the anchor–core pairs (p+,k), (p−,k) exit to (2,1,0), (1,2,0)
      (Gröbner [c1, c3]) — so every UNSAT column is skeleton-level, not recruit-dependent. The next box remains OPEN;
      the fixture must be redesigned so that the anchor–core products are inside the web (closed core) before it can
      test anything about recruits.
  What stands: the forced-address accounting rule (founder wording), A3 rectangle NO_INSIDE_TARGET, the isotropic
  degeneration remark (v ↦ −(v·k)k on k·k = 0), and the merged paper's own claim boundary. NS #66 MERGED with these
  corrections already in it.

U40. (founder 16:36) Layered rulings: 1 GO redesign / HOLD "fill shells until closed" — combinatorial sum-closure ≠
     closure under net forcing (a ∉ W allowed iff F(a)=0); Track E (exit accounting/EPSC) and Track R (recruit test on
     W3/T0-02 populated web); hand skeleton retired as evidence, kept as regression test. 2 GO audit / HOLD wording
     "622 INVALID" until rerun; unit = one ADDRESS after aggregation. 3 GO first: mutually exclusive states with
     precedence, per-address aggregation, CERTIFIED_ZERO vs NUMERICAL_ZERO, isotropic guard k·k≠0 (R1 → checker
     invariant). 4 GO after 3: audit at the PRE-THRESHOLD layer (convolution → F(a) → accounting → threshold).
     5 GO retractions now / HOLD final Toledo pass until reruns; dependency audit RETAIN/DOWNGRADE/RETRACT ("correct
     UNSAT ≠ correct interpretation"). Order 3 → 2_audit → 4 → 5_retract → 1_W3 → 5_final. Central invariant:
     ∀ a ∉ W: F(a) = 0 ∨ a enters the ledger — "no empty forced address may disappear from the accounting".
DONE 3 + 2_audit (rg_forced_address_audit.py/.json, exact, per address, sweep's own perp_basis, isotropic guard):
     W1/W2/W3 as SEEDS are (correctly) INVALID closure tests (forgotten inside addresses = their gen-1 births:
     10 / 12 / 18) — calibration that the rule fires on open seeds. NPSC box-2 hits: 610/610 INVALID — every hit has
     ≥ 1 registered address with amplitude 0 and nonzero net forcing (1,260 such addresses in total; 15,186 null by
     geometry; 2,440 active; 0 forgotten-inside, 0 TED in-box). Box-1's 12 hits not re-audited (combined file has a
     different structure) — wording for box-1 stays HOLD. First pass with my own perp basis was WRONG (10 spurious
     "valid" hits) — corrected by importing the sweep's basis; recorded as a checker lesson (point coordinates are
     basis-dependent; always reuse the generator's basis).

U41. (founder 17:5x) Final rulings: Track R GO structural-first + REGISTERED LINEAGE LINK required (recruit = gen-2
     address + registered ancestry/event link to the anchor + structural O-condition; genuine single-O needs
     nonparallel + opposite line not O; one-sided needs persistence of the fixed line in lineage history, not a
     snapshot; dynamic fraction = readout, label 'candidate'). box-1 rerun GO (same pipeline/basis as box-2).
     Toledo 5_final GO after PR audit merge + vault dependency audit (status_note aligned in one pass). NPSC v2 GO
     with encoding review + box-1 pilot first; encoding = per aggregated address k: selector s_k(s_k−1)=0,
     (1−s_k)F_{k,j}=0 ∀j, s_k(Σ_j λ_{k,j}u_{k,j} − 1)=0 (Rabinowitsch on a LINEAR witness, not ‖u‖²≠0 — isotropic-safe,
     complex-safe); F_k = net forcing after aggregation. Queue: M2 → box-1 rerun → freeze NPSC-v2 encoding → NPSC-v2
     box-1 pilot → Track R structural scan → NPSC-v2 box-2 full. STATUS WORDING (R3-prevention rule): "OLD NPSC
     box-2 hit interpretation = RETRACTED" — NOT "NPSC box-2 theorem refuted"; the accounting-rule question has not
     been swept yet.

CORRECTION (founder asked "ขัดกับ Genesis หรือเปล่า", 18:3x): my Track-R item 1 ("lineage link must be a productive
     path, net forcing ≠ 0 at every step") is WRONG under Genesis: lineage preservation / GCD keeps a registered
     path even when a step is EXACT-CANCELLED (cancellation ≠ loss), and future relevance is a separate reader
     gate (weld/M.03 on the declared horizon), not "forcing ≠ 0 now". Corrected definition: recruit = gen-2
     address + registered lineage path in the ledger (any channel) + structural O-condition; future relevance
     tested separately by the declared reader. Items 2 (persistence over every window), 3 (linear witness in both
     lanes), 4 (M2 partial + 60-min certificate cap) reviewed: consistent with Genesis; kept.

U42. (founder 18:4x) Final Track-R / NPSC-v2 / M2 semantics — LOCKED:
  1 lineage link = registered source-pair path with EACH TRAVERSED CHANNEL individually nonzero (edge productivity),
    while every address on the path carries its own outcome {ACTIVE, EXACT-CANCELLED, NULL, TED, UNRESOLVED};
    recruit = gen-2 address + registered productive-channel ancestry + structural O-condition + future-reader
    relevance (weld/M.03, horizon L = 3 windows unless changed). Never "net forcing ≠ 0 at every step".
  2 O_+-persistent ⇔ + ∈ O(q_t) for every window t ∈ {1,2,3}; complement is NOT alternation: outcomes PERSISTENT ∨
    CERTIFIED SWITCH (line change O_+ → O_− seen with registered lineage/event) ∨ MIXED/UNRESOLVED.
  3 Linear Rabinowitsch witness Σ_j λ_{k,j} F_{k,j} − 1 = 0 per address (own λ_k, no shared witness) in both lanes;
    real lane: UNSAT over the algebraic closure kills real solutions; SAT requires a separate real-feasibility
    certification before being reported as real SAT.
  4 M2: two fields per (point,d): primal_verdict and certificate_status; 60-min certificate cap from 18:2x; timeout
    ⇒ CERTIFICATE_UNRESOLVED only (primal retained; proof-grade exclusion HOLD); no retroactive cap change.

U43. (founder 19:1x) Track R GO with three guards: (1) L = 3 is a reader-scoped horizon — wording "future-relevant
     within declared L=3", never "irrelevant"; persistence requires the address ACTIVE in all 3 windows AND
     O_t(q) = {+} ∀t; (2) real-feasibility semantics locked: SAT_REAL = explicit exact point substituted into every
     equation/inequality/witness; SAT_COMPLEX_ONLY needs a certificate that the real locus is empty (e.g. x²+1 ∈ I);
     else SAT_REAL_UNRESOLVED; eliminant real-root isolation = diagnostic only; linear Rabinowitsch stays primary;
     (3) switch-by-readout accepted as readout evidence (not lineage event) with the frame guard: same address, same
     registered/reanchored two-line fiber across the horizon, ACTIVE at adjacent windows, O_t={+}, O_{t+1}={−};
     frame not certified ⇒ MIXED_UNRESOLVED; five branches DOUBLE_O ∨ PERSISTENT_PLUS ∨ PERSISTENT_MINUS ∨
     CERTIFIED_SWITCH ∨ MIXED_UNRESOLVED ({+,−} routes to DOUBLE_O). Scanner written (rg_track_r_scan.py) and queued
     behind the M2 lock; box-1 per-address audit queued first.

U44. (founder 19:5x) Final scanner rulings: 1 retention-gap branch GO push+PR / HOLD merge until review+CI; after
     merge re-pin the 32 cards to the immutable merge SHA (branch-ref is a temporary workaround). 2 τ_O = 1e-12 as a
     SEPARATELY TYPED angular parameter (τ_ret = load, τ_O = angular; same number, two parameters); failing τ_O = not
     classified, never "non-O". 3 numerical DOUBLE_O = CANDIDATE ONLY; rational rounding of float history proves a
     property of a nearby rational point, not of the observed state — DOUBLE_O_EXACT only from registered structural
     line representatives (nullity/kernel formula) checked symbolically. 4 manifest/spec generation GO, automatic
     Gröbner HOLD; fixtures built from candidates are "exact surrogate fixtures derived from candidates", never
     "exactification of the observed trajectory". Core line: keep "numerical run evidence" and "exact algebraic
     fixture" separate. Applied: scanner patched (typed tolerances, candidate-only DOUBLE_O, manifest); review+push
     agent launched for the retention-gap branch (HOLD merge).

RESULT-M2-R1 (20:2x, finite_diagnostic, rg_m2_round1_REPORT.md): all four (point,d) solved inside cap (11 min).
     P_1 alone: primal_verdict SAT at A_d2/A_d3/B_d2/B_d3, every SAT SPURIOUS (no T0-02 window with S>0, E=D=0 and
     inventory return) → C0 failure class LOST_INFORMATION (energy coordinate absent). P_1+H_2 (energy rows
     E⁺−E⁻−LE=0): UNSAT, certificate_status VERIFIED in all four (canonical Farkas y_E=−1, λ_X=1, η>0; checker PASS);
     one tight edge per run, always at the DEEPEST cell (g=d). η: A 3.32e-4 → 6.50e-5, B 2.98e-4 → 5.92e-5 from d=2→3,
     ratio ≈ 5.1 / 5.0 = the scale ratio 5 per step (observation; interpretation OPEN — the raw certificate margin is
     NOT scale-uniform; a scale-normalized η is the reassessment item for T0 question (ii)). The report itself says the
     H_2 certificate is the expected outcome once energy is a coordinate ("E=D=0 stationary ⇒ null state" in LP form);
     the round's content = the load coordinate alone (rounds 0–1) cannot see it. NOT a global charging argument.
     T0-03 DECISION (locked rule): primal SAT/SPURIOUS AND dual tight at the deepest cell ⇒ HOLD / REASSESS. T0-03 and
     T0-04 stay FROZEN / NOT RUN. Reassessment item: scale-normalized energy coordinate before any new run.
RESULT-BOX1-AUDIT (20:2x, exact, sweep basis): old NPSC box-1 12/12 hits INVALID under forced-address accounting
     (states NULL_BY_GEOMETRY 266, FORGOTTEN_REGISTERED 26, ACTIVE 48). Same status as box-2: OLD interpretation
     RETRACTED, theorem not refuted.
RESULT-TRACK-R (20:2x, finite_diagnostic, rg_track_r_scan.log/.json + rg_track_r_manifest.json): 4 runs × 41 anchors ×
     248 recruits × 3 windows. Per run: MIXED_UNRESOLVED 201,306 numerical + 1,461 structural; PERSISTENT_MINUS 334+2;
     PERSISTENT_PLUS 246+4; DOUBLE_O_CANDIDATE(numerical) 7; CERTIFIED_SWITCH 0. Manifest = 2000 entries (CAPPED —
     totals exceed 2000; not silent: noted here), frame_certified = false for every entry, NO margin field emitted
     (gap vs the U44 spec: margins/lineage path/accounting not in the manifest — scanner revision needed before any
     margin ranking). Fixture spec PROPOSAL written (rg_track_r_fixture_spec_PROPOSAL.json): 3 structural PERSISTENT
     candidates, distinct anchor pairs, Gröbner HOLD. Observation: all 24 structural PERSISTENT candidates have the
     axis recruit (0,0,3) with an axis anchor (0,0,2) — an axis-symmetric family; flagged, not interpreted.
DECISIONS (delegated, my defaults — founder may override): Q1 fixtures = 3 (spec above). Q2 DOUBLE_O_EXACT source =
     kernel line of the anchor-cross nullity theorem (equal-shell) ONLY; ORTH case (a ∥ p×q) kept as a separate label
     ORTH_DEGENERATE (branch D, OPEN), not merged. Q3 retention-gap PR #68 CI green (20/20) — HOLD merge for founder go
     (U44 ruling). Q4 NPSC-v2 pilot box-1 = GO (frozen encoding; 85 reps; queued via rg_queue.sh; agent builds runner).

U45. (founder 20:1x) COMMERCIAL LAYER — "ไม่ต้องรอแก้ Clay สำเร็จก็เอาของที่พิสูจน์แล้วไปสร้างมูลค่าได้": four product
     layers (1) Readout CFD / Simulation Integrity Auditor (forced-address accounting on solver output: ACTIVE /
     EXACT-CANCELLED / NULL-BY-GEOMETRY / TED / UNRESOLVED → PASS / WARNING / INVALID CLOSURE / UNRESOLVED) — first to
     build; (2) adaptive spectral refinement by future-relevance of forced descendants; (3) proof-carrying simulation /
     certified digital twin (research/engineering assurance layer, NOT regulatory certification); (4) NS solver torture
     suite (isotropic k·k=0 artefact, basis dependence, forced-address omission, W1–W3 / OT fixtures). Recorded in
     readout-problem-navier-stokes-internal/PRODUCT_IDEAS_2026-09-12.md with tier notes. No compute, no repo work now.

U46. (founder 20:5x) Map corrected (FINAL-EQUIV = REGULARITY-EQUIVALENT/HOLD; switching single-O = fixture-level finite
     diagnostic; silent layer = exact local under ALT-1 only; interface OPEN = primary theorem target). ONE main queue:
     1 M2 round 1 FROZEN as result (P1 = LOST_INFORMATION; P1+H2 = finite UNSAT/VERIFIED; raw η non-uniform; normalized-η
       hypothesis η̃_d = 5^{d-2} η_d OPEN, label FINITE_DIAGNOSTIC / SCALE-NORMALIZATION CANDIDATE); T0-03 HOLD, T0-04 FROZEN.
     2 M2-normalization analysis BEFORE any rerun: is 5η_{d3} ≈ η_{d2} an algebraic consequence of units or empirical?
     3 NPSC-v2 box-1 pilot continues (running).
     4 Track R scanner fix before promote: uncapped aggregates, margin m_O = |a·q|/(‖a‖‖q‖), symmetry-orbit dedupe,
       split STRUCTURAL_GEOMETRY vs NUMERICAL_O_PERSISTENCE (agent launched: rg_track_r_scan_v2.py, queued).
     5 Rerun 4 families, count INEQUIVALENT structural orbits; 1 orbit ⇒ study 1 orbit, never fabricate 3 fixtures.
       (Founder objection accepted: the 3-fixture PROPOSAL is WITHDRAWN as "diverse" — all 24 structural hits are the axis
       family; the file stays as history with this note.)
     6 Exact surrogate fixture spec only after orbit count; Gröbner only after accounting+lineage+frame+L=3 checks.
     7 RSC-O theorem target: passive one-sided layer + active opposite core ⇒ double-O ∨ E ∨ C ∨ novelty/exit.
     8 PR #68: GO merge on head 039bfb7 with CI green → MERGED 20:5x at 295dce4; re-pin cards to 295dce4 (vault agent).
     9 Toledo/vault final pass after NPSC-v2 pilot + Track R v2.
RESULT-M2-NORMALIZATION (21:0x, finite_diagnostic, from rg_m2_round1.json columns_summary, no new run): min LE/p over
     productive interior types grouped by the deepest RECEIVER cell m within ONE run:
       A_d2: m0 8.7e-4, m1 3.3e-4, m2 3.9e-4 | A_d3: m0 1.1e-3, m1 1.7e-4, m2 6.7e-5, m3 6.5e-5
       B_d2: m0 4.0e-4, m1 3.0e-4, m2 3.1e-4 | B_d3: m0 5.9e-4, m1 1.9e-4, m2 5.9e-5, m3 5.9e-5
     (i) The within-run cell profile is NOT ∝ 5^{-m} (multiplying by 5^m makes it grow ~5× per cell), so the factor 5
       between d=2 and d=3 is NOT the |k|²-units of the deepest cell (load-vs-energy units explanation REFUTED at this
       resolution). (ii) Restricting the d=3 run to cells ≤ 2 still gives ≈ η_{d3} (6.7e-5 / 5.9e-5), not η_{d2}: the
       same cell 2 reads 5.9× smaller in the d=3 run. The d=3 runs are read at 5× shorter horizons (snapshots t ≈ 1–3 vs
       5–16; τ_m ∝ Λ_{m+1}^{-2} = factor 5) ⇒ the leading explanation is the READER HORIZON (state read earlier), a
       reader-scoped quantity, not a cell-scale quantity. (iii) η̃ = 5^{d-2}η constant therefore reads as "min LE/p per
       relaxation window" — consistent with BOTH a horizon artefact and a scale-uniform margin; two runs cannot separate
       them. Decisive cheap test (HOLD, needs a new frozen record since the reader horizon changes): re-step point A at
       d=2 (12k triads, minutes) with the d=3 window schedule and recompute η; equal to 6.5e-5 ⇒ horizon effect; equal to
       3.3e-4 ⇒ genuine cell/depth effect. Status: SCALE-NORMALIZATION CANDIDATE, OPEN; not G7.

U47. (founder 21:2x) MAIN ROUTE LOCKED — S1/S2/S3 skeleton on Clay (B) (periodic, f=0):
  assume first blowup T -> S1 complete finite recent reader -> S2 uniform normalized scale progress/payable charge
  -> sum_j R_j < infty -> S3 H^3 continuation bridge -> extend past T -> bot. Rule: every new task must advance
  S1, S2, or S3, or it is not done. S2 = main bottleneck; G4/G6/G7 subsumed into S1(reader completeness)/S2(rigidity+
  uniform exit). RSC-O program continues but reframed as machinery FOR S2, not a standalone target.
RESULT-INTERFACE-NOVELTY (21:2x, exact, sympy pair-level, rg_interface_novelty_lemma.py): founder's interface-novelty
  lemma for the one-sided RSC-O interface VERIFIED with one wording correction. Setting: independent lines a+,a-;
  opposite-core anchor (p,a-) with a-.p=0; one-sided recruit (q,b), b || a+, a+.q=0, genuine single-O a-.q!=0.
  (1) B_{p,q}(a-,b)=0 under single-O forces equal shell |p|=|q| on the REAL locus (the (p_z+q_z)^2+q_y^2=0 branch is
  a sum of squares, real-forces q_y=0, contradicting single-O); the only surviving branch there is SAT_COMPLEX_ONLY
  (isotropic k.k=0 artefact class, same family as the R1/R2 retraction) -- corrected wording vs the founder's draft:
  NOT "equal shell iff 0", but "equal shell OR isotropic-complex artefact only". (2) a+.p!=0 and B!=0 => output not
  || a+ and not || a- (checked both directions exactly) => third-line novelty CONFIRMED. (3) Escape a+.p=0 (with
  a-.p=0) forces p || a+ x a- CONFIRMED; on this locus output is exactly on line a+ with a+.k=0 (CONFIRMED: output
  is a NEW ALT-1 recruit of the same layer, not a terminal state -- must be tracked as such, not treated as closure).
  (4) Normal-locked web check (core x core silent, layer x layer silent [reuses the existing silent-layer lemma],
  core address receives 0 from every core-layer pair, all outputs on line a+): VERIFIED exact at the symbolic level
  tested. Conclusion CONFIRMED: one-sided interface reduces to double-O v E v C v T v third-line-novelty v
  normal-locked-recursion(new ALT-1 layer) -- "normal-lock" is NOT a sixth terminal branch, it recurses into the
  one-sided case again with a new anchor pair; recurrence/termination of that recursion is OPEN (not yet a theorem).
  Status: NEW DERIVATION / PROPOSAL, not yet in Toledo. First concrete S2 contribution.
RESULT-NPSC-V2-PILOT (21:2x, finite_diagnostic, rg_npsc_v2_pilot_REPORT.md): box-1, 85/85 reps UNSAT under the frozen
  v2 encoding (per-address selector + linear Rabinowitsch witness + isotropic guard); 0 SAT_REAL, 0 SAT_COMPLEX_ONLY,
  0 SAT_REAL_UNRESOLVED -- the real-feasibility certification path is UNTESTED by this run (no SAT case arose). 73/85
  consistent with v1; 12/85 were v1 "hits" (SELF_CLOSED_PRODUCTIVE) that v2's semantics do not reproduce either (a
  new sweep, not a re-labeling -- those 12 are also among the ones already INVALID under forced-address accounting).
  15/85 direct cross-checks timed out (UNSAT stands on primary solve only for those). Box-2 full (26,411 reps) queued
  next per the frozen doc's own gate, but per U47 priority is now S1/S2/S3, not catalogue expansion -- HOLD box-2
  unless it specifically advances S1 or S2.
INCIDENT (21:2x): Track R scanner v2 agent FAILED — API usage-credits exhausted (rate_limit 429), not a task defect.
  Not relaunched pending credit/model availability. rg_track_r_scan_v2.py not yet written; v1 outputs unchanged.
  Session model switched to Sonnet 5 (founder /model sonnet) for remaining work this session.

RESULT-S1-STATEMENT (21:4x, Dr, S1_EXACT_STATEMENT_2026-09-12.md): S1 written through Genesis reuse pipeline —
  q_D = P_N is weld/M.02's commuting square (defect R_N is an IDENTITY, not assumed); reader horizon licensed by
  weld/M.03; the forced-address ledger Λ is EQ-001/C.16's lineage sidecar reused verbatim (not reinvented); every
  unaccounted address gets exactly one weld/E.05 label (0 / ledgered / UNRESOLVED=bot, never silently PASS);
  sufficiency (weld/E.06) explicitly deferred to S3; cross-window transport uses weld/E.08 (bridge tolerance not yet
  computed -- new obligation). Parent PROP-P3-RECENT-RETENTION-BOUND-ENERGY-ONLY-REFUTED tells S1 what NOT to do:
  ledger entries must be per-address/datum-dependent, never a single scalar B(E_0,nu,T) (that form is REFUTED).
  S1 = PARTIAL, two concrete open sub-claims: (1) cross-scale ledger completeness as j->infty [untested by any run
  so far -- everything is at fixed N,d], (2) the E.08 bridge tolerance itself [not computed]. Next step: check
  whether the T0-02 triad enumeration stays complete under refinement (N up / d up) -- single YES/NO, existing
  stepper, no new theory, directly attacks S1 item 1.

RESULT-S1-ITEM1-CLOSED (21:5x, exact + finite_diagnostic, rg_s1_ledger_completeness_check.py +
  rg_s1_selfpair_check.py): S1 item 1 (cross-scale ledger construction exhaustiveness) CLOSED. Brute-force double
  loop vs the fast key-based pair table agrees exactly at d=1,2,3, both points A/B, with the SOLE discrepancy being
  the self-pair (p=q) address, excluded by construction. Proved harmless: self-pair forcing g_self=-2i(u_p.p)u_p is
  identically 0 because u_k.k=0 (transversality) is an exact invariant of the Leray-projected stepper -- confirmed
  numerically to ~1e-16 relative over 50 steps, both points (not merely a seed-time property). Because the pair-table
  search is an exact collision-free integer-key lookup (not sampled/truncated), the exhaustiveness argument holds for
  EVERY finite d, not only the three tested -- an architectural fact, not a numerical coincidence. weld/E.05 reading:
  the excluded self-pair resolves to ADMITTED (F(a)=0), never UNRESOLVED. S1 is now reduced to a SINGLE open item:
  the weld/E.08 cross-window bridge tolerance (item 2), which is the same object S2 needs (R_{j+1}<=qR_j+beta_j) --
  merge item 2 into S2's attack rather than treating it separately. S1_EXACT_STATEMENT_2026-09-12.md updated in place.
