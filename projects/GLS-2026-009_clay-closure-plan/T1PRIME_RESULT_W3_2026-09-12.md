# T1′ result — Retained Extension Fiber readout, W3, generation 0→1 (exact; finite_diagnostic)
Script: p3_attack_2026-09-11/rg_type_graph.py → rg_type_graph_w3.json. Independent of the rg_m2 agent's code path
for the fiber counts (reuses only its mode/target construction); Gröbner over ℚ(√3), no floats. Datum F(k)=0 kept in
every convention (first run without it reproduced the rg_m2 run1 "dim 6" artefact — that family is not the W3 datum).

| convention | f (new live addresses) | r_forced independent | multi-source targets | rank-1 cancellation channels | r_sound | g = r_sound − f_extra | code | productive class after |
|---|---|---|---|---|---|---|---|---|
| A full closure | 68 | 41 | 14 | 0 | 41 | +41 | DROP | ∅ (collapses) |
| B exits |t|²≥3 | 38 | 26 | 14 | 0 | 26 | +26 | DROP | ∅ |
| B2 exits + seed feedback free | 24 | 18 | 12 | 0 | 18 | +18 | DROP | ∅ |

Reading (Genesis): every productive W3 seed class pays ≥18 independent sound constraints at its first extension under
the most permissive convention; no zero-novelty productive extension exists; no multi-source target has a rank-1
cancellation channel (all rank 2 in t⊥), so r_sound = r_raw here — the M3 ambiguity does not arise for this fixture.
Same conclusion as the rg_m2 agent (M_1 ∩ {C≠0} = ∅ under all semantics; minimal certificate = pairs (p_i−q_j, p_i−p_j)).
Type graph: S (productive equal-shell seed) → X (novel/exited) is a DROP edge; the return edge X → S is the REANCHOR
edge whose weight is UNDECLARED → cycle verdict LOSSLESS_CYCLE_CANDIDATE stands until REANCHOR is charged (the
cross-cell budget fixture ratio 101 ∀ j is the existing G(C)=0 witness). Scope: one witness, generation 1, interior;
says nothing about ∂₊ or about RC-G6 in general. Not W1/W2/orthogonal-turn yet.
