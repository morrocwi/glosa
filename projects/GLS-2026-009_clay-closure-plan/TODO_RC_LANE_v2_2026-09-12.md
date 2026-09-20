# TODO v2 — Readout–Clay lane, ordered by LEVERAGE (not by arrival order of proposals)
tier: Dr. Supersedes the ordering of TODO_RC_LANE_2026-09-12.md (that file stays as the intake log U1–U14; this one is
the execution order). Rule from the founder (CTX ~13:00): "เราจะสแปมข้อเสนอ นายเอาไปจัดเรียงเอง เน้นประสิทธิภาพ".
Placement principle: an item ranks by (decisiveness × cheapness) and by whether it can KILL a route early.

## Standing frame (do not re-derive)
Frontier = RS (G4, joint-normalized) · NPSC/SCWR (G6 interior) · R3-joint + EPSC (reanchor not free, ε_j ≤ Cθ^j) ·
∂₊ (no reader yet). Strategy: exclude exact zero-defect FIRST (equality rigidity), quantitative δ only via compactness
AFTER. Certificates, not solver trust: every UNSAT must ship an exact identity −1 = Σ a_j F_j + Σ_G (Nullstellensatz /
Positivstellensatz), every SAT an exact algebraic point checked by substitution. Cancellation amount ≠ defect; the
accounting residual D^acc is what must vanish. RNO/GCD/Lemma A-B are forced-but-content-free: never count them as
progress. All numbers finite_diagnostic unless a Coq file says otherwise.

## RANK 1 — decisive and cheap (this week)
R1-a  NPSC/SCWR m=1 populated, box [-2,2]³ (RUNNING, agent). Output per set: NOT_SELF_CLOSED / SELF_CLOSED_PRODUCTIVE /
      TIMEOUT. Box-1 done: no fully-populated self-closed productive web (12 apparent hits = 2-address seed-expansion).
R1-b  [DONE for W3: rg_cert_w3_nullstellensatz.json, checker rg_cert_check.py PASS] Turn R1-a's GB=[1] results into EXACT CERTIFICATES: extract cofactors a_j with Σ a_j F_j = 1 by Macaulay-matrix
      linear algebra over ℚ up to a degree bound (no Singular/M2/msolve on this machine; sympy 1.14 has no lift) and
      ship a checker that only expands the identity. Script: rg_cert_nullstellensatz.py. This is the founder's
      UNSAT_CERTIFIED and the first Track-A certificate of the lane.
R1-c  m=2 (𝒮_ω for two-step words): populated support S, state after ONE exact step must still have support ⊆ S with
      all outside forcing zero at both instants (time-invariance of self-closure), productivity via P·s²−1=0,
      nondegeneracy via N·t²−1=0, gauge: 𝒱=1 + declared reanchor gauge H=0. Same box, same tool. Expect heavier
      Gröbner; use the box-1 sets first. RAM cap 3 GB, one process.
R1-d  RS readout (T4): when rg_run1 d∞ K=125 finishes, read A_{N,η} across d=3,4,∞ and the α split
      (sel/off/cancel/total); code RS = PASS / INSUFFICIENT_RESOLUTION for the frozen question Q(i)(ii)(iii).

## RANK 2 — the gate that decides whether cycle enumeration is even finite
R2-a  RC-TYPE probe: after canonical (joint) reanchor, do the descendants of W1/W2/W3 and of the orthogonal-turn chain
      fall into finitely many reader-sufficient types? Concrete test: enumerate gen-1/gen-2 descendant addresses of
      each fixture, reanchor to the √5 cell, and count distinct (direction, polarization, phase-relation, cancellation-
      rank, ancestry-depth) signatures — does the count stabilise across generations? If it grows, RC-TYPE fails as
      stated and the simple-cycle reduction is not finite; report that plainly.
R2-b  REANCHOR edge charge: define g(REANCHOR) on the joint-normalized quotient and test it on the budget fixture
      (ratio 101) and the orthogonal-turn tax 17/25 — is the cross-cell cycle G(C)=0 or >0 once exits are accounted
      into the next cell's 𝒱? Without this, LOSSLESS_CYCLE_CANDIDATE stands at cell level regardless of R1.

## RANK 3 — soundness layer
R3-0  RC-FRPA/APC (U15): specify the resolve map K → K_active ⊕ K_terminal and test the four founder conditions on
      W1–W3 inside the M3 checker; the cone algebra itself needs no work. (needed before any R1/R2 result is quotable as a theorem)
R3-a  M3 checker (W1–W3 → D_RETAINED / D_ADMISSIBILITY / E_REGISTERED / PATTERN with certificate), with the D^acc
      residual rule (not C_k = 0) and the U5 rule (ledger stalls + future readout changes ⇒ LOST_INFORMATION).
R3-b  Σ-sufficiency test (U2): perturb a coordinate outside Σ and check the future readout.
R3-c  Extend RG_GCD_RNO.v with RG-MONODROMY-DETECTION (ledger-map form). Small; Coq.

## RANK 4 — structural holes with no fixture yet
R4-a  ∂₊ aggregate reader ℛ₊ (reader-invariant, reanchor-covariant, cancellation-aware): design only.
R4-b  EPSC decay ε_j ≤ Cθ^j from tape: no candidate proof; fixture retention-gap (fails full-shell, holds cube-surface).

## PARKED — governance / bookkeeping (do when a human gate opens)
P-1  Vault: workflow wf_c25e22de-442 (13 cards written, assembling). After it returns: add cards RG-MONODROMY-
     DETECTION, RC-IMR, RC-NPSC/SCWR (with R1 results), RC-ER, RC-SCWR-CERT; validator + DAG; adversarial findings.
P-2  Push/PR NS branch research/p2-retention-gap-2026-09-12 and Toledo branch (need founder go + review).
P-3  Repo rename (name unconfirmed). Volume 7 check_volume7.py.

## Intake log pointer
Founder proposals U1–U14 (incl. U14 = SCWR as semialgebraic feasibility with Positivstellensatz certificates,
algebraization rules v²=1, c²+s²=1, r²=g·g, productivity P·s²−1=0) live in TODO_RC_LANE_2026-09-12.md. New
proposals get a U-number there and a rank here; nothing is executed from the intake file directly.
