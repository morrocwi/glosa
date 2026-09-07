#!/usr/bin/env python3
"""cases/repro/run_EQ-045_gauge_dim.py -- runner for the EQ-045_gauge_dim reproduction card.

tier: Dr (specified from design/RESISTANCE_LADDER_v0_1.md Section 6, Card 1, secondary/positive
control; independently unreviewed).

Standard library only. `AI = 0` at runtime: no model is called; this is a from-scratch,
closed-form arithmetic re-derivation, independent of Toledo code EQ-045's own statement text or
any Genesis/Toledo file -- it never reads registry/genesis_root.json or imports any project code.

WHAT THIS REPRODUCES. Toledo code EQ-045 (registry/genesis_root.json in the Toledo repo) states,
verbatim: "dim Z(g) = 1; g = u(1) (+) su(2) (+) su(3); dim = 1+3+8 = 12" (the Standard Model gauge
algebra's total dimension). This is the "independent_implementation" oracle candidate the design
doc calls a positive control: it uses the general closed-form Lie-algebra dimension formulas
    dim(u(n)) = n**2
    dim(su(n)) = n**2 - 1
(both standard results, not derived from this repository's own construction) with n=1,2,3, and
sums them, WITHOUT ever reading EQ-045's own "1+3+8=12" arithmetic. Agreement with the Genesis
statement is the actual test; it is not assumed.
"""
from __future__ import annotations

import json


def dim_u(n: int) -> int:
    """dim(u(n)) = n**2 (standard result: u(n) is the Lie algebra of n x n anti-Hermitian
    matrices, a real vector space of dimension n**2)."""
    return n ** 2


def dim_su(n: int) -> int:
    """dim(su(n)) = n**2 - 1 (standard result: su(n) is u(n)'s traceless subalgebra, removing
    exactly one real dimension, the trace)."""
    return n ** 2 - 1


def run() -> dict:
    d_u1 = dim_u(1)
    d_su2 = dim_su(2)
    d_su3 = dim_su(3)
    total = d_u1 + d_su2 + d_su3
    return {
        "formula": "dim(u(1)) + dim(su(2)) + dim(su(3)), n**2 for u(n) and n**2-1 for su(n)",
        "dim_u1": d_u1,
        "dim_su2": d_su2,
        "dim_su3": d_su3,
        "dim_total": total,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
