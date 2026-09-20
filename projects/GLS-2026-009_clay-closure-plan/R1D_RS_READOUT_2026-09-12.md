# R1-d — INVARIANT+DEFECT readout of the frozen-input run (rg_run1 series), Genesis codes
tier: finite_diagnostic (floating-point integrator with declared tolerances; energy-identity residual ≤ 6.6e-9 on all
four runs; sparse=dense validated 1e-16; brute-force convolution 9e-16). Frozen record T0-2026-09-12-01, η=1/2,
cells Λ_m = 5^(m/2+θ), B(T0) = 10.944 (seed retained load).  Script rg_run1_analyze.py; data rg_run1_{d3,d4,d4_phaseB,dinf_K125}.npz.

| run | cutoff | cells | A/B per cell (0..4) | max A/B | d-vs-next cutoff agreement |
|---|---|---|---|---|---|
| d3 | 144 modes | 0–2 | .352 .479 1.13 | 1.13 | cell1 19%, cell2 30%, cell3 absent |
| d4 | 544 | 0–3 | .352 .477 1.00 .755 | 1.00 | vs d∞: cell1 1.4%, cell2 5.4%, cell3 10%, cell4 absent |
| d4 phaseB (q0 phase i) | 544 | 0–3 | identical to 4 digits | 1.00 | phase of q0 irrelevant at this resolution |
| d∞ K=125 | 15,812 | 0–4 | .31 .477 1.00 .759 .38 | 1.00 | top cell max load 0.033 (2.6e-3 of seed) |

Hand-off readouts α (sup over trailing window of hand-off load / R_m):
  0→1: total 20.5–23.7, sel 0, off = total, cancel 25.6–102 (cancel share > net; d3 value 102 is cutoff-polluted)
  1→2: total 7.93, sel 4.97, off 7.26–7.29, cancel 24.0   (the selected pair carries 63% of the net; cancellation deficit = 3× net)
  2→3: total 16.2–16.4 (d4, d∞; d3 = 0 = cutoff), sel 0, cancel 20.5
  3→4: 0.41 (d∞ only; d4 = 0 = cutoff), cancel 0.53
Lineage: energized modes per generation 4,4,8,16,32,64,24,0 (d∞) — doubling per generation, k_y ∈ {−4,0,4} only
(the seed's planar sub-lattice is respected: no ε_lineage events). Exits: line boundary energized at d3/d4 (registered
E at the active-set edge), not at d∞ (K=125 contains the whole energized set within T=10).

## Codes against the frozen question Q
Q(i)  sup_N A_{N,η} ≤ B(T0)?  — max A/B = 1.13 (d3), 1.00 (d4, d∞): bounded by 1.13·B across three cutoffs, and
      decreasing with cutoff.  Code: **INSUFFICIENT_RESOLUTION** for a uniform statement (three cutoffs, one seed,
      strongly dissipative regime ν = 1/200 where load dies by t≈5; cell-0 window incomplete). Not LOST_INFORMATION:
      no lineage defect. Positive evidence only.
Q(ii) α-split: cancellation deficit exceeds the net hand-off load at every populated hand-off (cancel/total = 1.1–3.0)
      — the multi-source cancellation channel is the dominant reader at hand-offs, and the selected pair carries the
      majority of the net only at 1→2.  Code: **PASS (readout obtained)**; interpretation stays with M3 (cancel ≠ defect).
Q(iii) exits/EPSC: top-cell load ratio 2.6e-3 at K=125; cutoff sensitivity 19%→1.4% (cell 1), 30%→5% (cell 2) as the
      cutoff grows.  Code: **PASS at this resolution**, no evidence of unregistered exit; ε_j ≤ Cθ^j not testable
      from one seed (needs the retention-gap datum family).
Overall for RS: evidence consistent, not a certificate. Next: second seed family (non-planar) and a less dissipative ν
before any RS card moves from OPEN.

## Addendum from the run agent's final report (arrived after the table above)
STRUCTURAL: from the frozen T0 alone, grammar A generates only the planar sublattice spanned by the two seeds; with
seed polarizations (in-plane, out-of-plane) the entire lineage is in TERMINAL CLASS P (2D3C): the in-plane retained
state stays exactly ±p0 for all time, all generated load sits on the line |k_y| = 4 advected linearly by p0. The chain
objects q1, p2 are NOT reachable from T0 (the earlier v2_ot runs had hand-placed q1 — those are not readouts of this
record). Consequence: this frozen input is a TYPE+SUFFICIENCY defect for the G6/NPSC question — the seed lies in the
terminal class the theorem excludes, so the run can support RS/EPSC readouts only, never a recurrence probe.
Agent's codes: (i) A bounded PASS_FINITE_DIAGNOSTIC (A/B ≤ 1.13, decreasing above cell 2); (ii) α_total < 1−e⁻¹ and
stable d3→d4: NO_CLOSURE (α = 8–24 ≫ 0.632; d4→d∞ converged 1–2 %); (iii) recurrent load with zero registered defect:
none (all envelopes decay 7e-5…3e-4). ε_lineage = 0; peak RSS 0.71 GB; no process left.
My coding stands as the conservative one for (i) (INSUFFICIENT_RESOLUTION for a uniform claim); (ii) I adopt the
agent's NO_CLOSURE for the α<0.632 sub-question (the reader normalisation α/R_m is itself flagged as candidate ε_read).
NEXT FROZEN INPUT (T0-02): non-planar seed outside class P (e.g. W3 datum or the orthogonal-turn pair with a third,
non-coplanar address), same reader family, so that RS and NPSC are probed on a productive class. Freeze before running.
