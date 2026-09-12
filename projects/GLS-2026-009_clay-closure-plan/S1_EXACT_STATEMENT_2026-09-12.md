# S1 — Finite reader completeness / no-silent-ancestry, written through the Readout Genesis lens

Status: **NEW DERIVATION / PROPOSAL — not yet in Toledo.** Tier of every claim below is stated per line (Definition /
Th_coqc / finite_diagnostic / Dr / Open). Ontology through Readout Genesis, mathematics through Toledo, per
`EQUATION_SOURCE_POLICY.md`. Reuse pipeline run before writing (Toledo lookup → Genesis compatibility → reuse →
derive only the missing piece → mark PROPOSAL) — parents cited inline, no object below is invented where an existing
weld/proposal already covers it.

## 0. Where S1 sits

Parent route (U47, `TODO_RC_LANE_2026-09-12.md`): Clay (B) ⇒ assume first blowup `T` ⇒ **S1** ⇒ S2 ⇒ S3 ⇒ extend past
`T` ⇒ ⊥. S1's job: before anything is said about *progress* (S2) or *continuation* (S3), the finite object we read
near `T` must not have silently discarded an influence that could change the answer. This is a **completeness**
obligation, not a smallness or decay obligation — S1 does not shrink anything, it only forbids silent loss.

## 1. Genesis objects reused (step 1–3 of the pipeline)

| Toledo code | tier | statement (canonical, cited not restated) | role in S1 |
|---|---|---|---|
| `weld/M.02.v1` | Definition | `q_{D,n+1}∘F_n = F#_{D,n}∘q_{D,n}` — a domain translation either commutes with the root dynamics exactly, or the square's defect must be declared | S1's finite projection `P_N` is exactly this `q_D`; S1's whole content is what happens to the defect term |
| `weld/M.03.v1` | Definition | `z ~_{Q,O,c,L} z' ⟺ O(F^k z)=O(F^k z') ∀k≤L` — equivalence is only ever relative to a declared question/observable/context/horizon | licenses reading a *finite window* `I_j` instead of the whole future; the horizon `L` is declared, not discovered |
| `weld/E.05.v1` | Definition | `χ_G ∈ {1,0,⊥}` = ADMITTED/OBSTRUCTED/UNRESOLVED; `χ_t(d) ∈ {FORCED,DERIVED,POSITED,BORROWED,OPEN}` per-distinction provenance | every defect term gets exactly one of these labels — UNRESOLVED (⊥) is a real, distinct outcome, never silently folded into ADMITTED |
| `weld/E.06.v1` | Definition | `Suff_{E,L}(Z^cand;Q,O,c,T)∈{1,0,⊥}`; a quotient may not merge states differing on a required future invariant | states the exact obligation S1 does **not yet discharge**: is `P_N u` sufficient to decide the continuation question `Q` = "does `u` extend past `T`?" |
| `weld/E.08.v1` | Definition | local knowledge is presented as global only through a declared, tolerance-bounded commuting-square transport, `ε_bridge = d(T^Y∘K_i, K_j∘T^C)` | governs transporting a per-window ledger statement across the whole shrinking family `{I_j}_j` — S1 must be a family statement, not one window in isolation |
| `EQ-015/M.04.v1` | Definition | `Retention→Structure→Translation→Readout→Meaning→Report` (pipeline order) | organizes §2 below; S1 lives at the Translation/Readout boundary |
| `EQ-001/C.16.v1` | untagged | a marked quotient stores structural occupation **separately** from an append-only **lineage sidecar**; equal structural projections need not identify marked histories | this IS the forced-address ledger `Λ` already built (NS PR #66/#67, `rg_forced_address_audit.py`) — reused verbatim as the sidecar, not reinvented |
| `PROP-P3-RECENT-RETENTION-BOUND-ENERGY-ONLY-REFUTED` | Dr | `¬[∃α<1-e^{-c},σ>0,B=B(E_0,ν,T) ∀u_0,∀j: 𝒩_{j+1}≤αR_j+C2^{-σj}B]` — an energy-only, datum-independent remainder bound is REFUTED (Bernstein-saturating witness, unbounded ratio) | tells S1 exactly what NOT to attempt: the ledger `Λ` below must carry datum-dependent, per-address entries — never a single universal scalar bound `B(E_0,ν,T)` |

Not yet in Toledo (cited as PROPOSAL, reused as-is, not re-derived): the forced-address accounting rule itself
(`F(a)=0 ∨ a ∈ Λ`, NS PR #66) and its per-address audit (`rg_forced_address_audit.py`, PR #67).

## 2. S1, stated through the EQ-015/M.04 pipeline

**Retention.** `δ_R` = the frozen datum: periodic NSE, `f≡0`, `ν>0`, `u_0` smooth divergence-free (Clay B). Assume
(for contradiction, per the S1→S2→S3 route) a first blowup time `T<∞`; before `T`, `u` is smooth.

**Structure.** Translate to the discrete Fourier interaction network on `ℤ³` — reused verbatim from the T0-02/M2
stepper (triads `{p,q,t=p+q}`, pair-sum coupling `B_{p,q}`); this Translation step is already exact (T0-02 admits
triads to `1e-8` relative energy identity, measured).

**Candidate state.** For scale `λ_j = λ_0ρ^j` and shrinking window `I_j = [T - c/(νλ_{j+1}²), T)`, the candidate
state is `z_j := q_D(u|_{I_j}) = P_{≤λ_j}u|_{I_j}` — the finite Fourier truncation, i.e. `q_D` of `weld/M.02`.

**Domain dynamics — the M.02 commuting square, made explicit (not assumed).** Writing the finite projection of the
NSE step:

```
∂_t P_N u + P_N B(P_N u, P_N u) = ν Δ P_N u + R_N,        R_N := -P_N[ B(u,u) - B(P_N u, P_N u) ]
```

This is an **identity**, true by construction for any `N`; `weld/M.02`'s square commutes exactly **iff `R_N ≡ 0`**.
S1 is not the claim that it commutes — S1 is the claim that whatever fails to commute is **accounted for**, never
silently dropped by the truncation.

**Sufficiency (the open half, `weld/E.06`).** `Suff_{E,L}(z_j; Q,O,c,T)` — is `z_j` sufficient to decide `Q` =
"does `u` extend past `T`?" — is **not** established by S1 alone; S1 only prepares the state on which S3 will later
try to certify sufficiency (via the `H^3` bridge). S1's contribution is narrower: it does not let `Suff` fail
*silently* through an unaccounted `R_N`.

**Readout / Meaning — the completeness statement (S1's actual new content).** For every `j`, every Fourier address
`k` with `|k| ~ λ_{j+1}` carrying a nonzero component of `R_N` on `I_j` (i.e. every mode the truncation's own
nonlinear term fails to generate correctly) must resolve to exactly one label, via `weld/E.05` read together with
the lineage sidecar `Λ` of `EQ-001/C.16`:

$$
\boxed{
\forall j,\ \forall k:\quad
R_N(k)\big|_{I_j}=0
\quad\vee\quad
(k,\ \text{source pair},\ \text{magnitude})\in\Lambda_j
\quad\vee\quad
\chi = \bot\ (\texttt{UNRESOLVED}).
}
$$

Per `PROP-P3-RECENT-RETENTION-BOUND-ENERGY-ONLY-REFUTED`: the ledger entry in the middle branch must be a
**per-address, datum-dependent** record (source triad, exact or floating-point-with-declared-tolerance magnitude,
window `I_j`) — never a single scalar `B(E_0,ν,T)` standing in for the whole tail. This is the one substantive
change S1 makes to the reused rule: the *existing* forced-address rule (PR #66/#67) is stated per address at a
**fixed** resolution; S1 additionally requires it to hold **uniformly across the whole shrinking family `{I_j}`** as
`j→∞`, i.e. transported across scales via a declared-tolerance bridge (`weld/E.08`) rather than re-proved from
scratch at each `j`.

**Report.** The reader's verdict for the family `{I_j}_{j≤J}` is:

* **PASS** iff every `j≤J` resolves every forced address to the first two branches (zero or ledgered) — ledger
  completeness holds up to `J`.
* **UNRESOLVED** iff any `j≤J` has an address that resolves to `⊥` — S1 halts the chain at that `j`; S2/S3 may not
  proceed past an UNRESOLVED window (fail-closed, per the R0 gate discipline).
* S1 never returns OBSTRUCTED/FAIL on its own — a genuine unaccounted address is definitionally UNRESOLVED, not a
  disproof of anything; only a *positive*, checked counterexample (an address that provably cannot be ledgered)
  would obstruct the route, and none is known.

## 3. What is and is not established (honest status)

* **DONE (reused, not re-derived):** the commuting-square identity itself (§2, exact by construction); the
  per-address forced-address rule and its checker at a fixed resolution (PR #66/#67, box-1/box-2 audits); the
  triad-table completeness check at fixed `N` (T0-02: 0 partner-consistency failures, energy conservation to
  `1e-8`–`1e-15` relative, measured).
* **ITEM 1 — CLOSED 2026-09-12 (exact + finite_diagnostic).** `rg_s1_ledger_completeness_check.py` cross-checks the
     fast key-based pair-table construction against a brute-force double loop over the SAME finite active set, at
     `d=1,2,3`, both points A/B. The only discrepancy at every `d` tested is the self-pair (`p=q`) address, excluded
     by construction (`keep = ip_ < iq_`). This is proved, not merely observed, to be harmless: the self-pair forcing
     term is `g_self = -2i(u_p·p)u_p`, and `rg_s1_selfpair_check.py` confirms `u_k·k = 0` (transversality) holds to
     floating roundoff (`~1e-16` relative) throughout an actual 50-step run at both points — an exact invariant of
     the projected stepper (every increment is Leray-projected transverse to its own target), not merely a seed
     property. So the excluded self-pair resolves to `weld/E.05`'s **ADMITTED, `F(a)=0`** branch, never `⊥`. Because
     the pair-table search is an exact, collision-free integer-key lookup (not sampled or truncated — `assert
     (np.diff(skey)>0).all()`), this exhaustiveness holds for **every finite `d`**, not only the three tested: it is
     an architectural fact about the search algorithm, not a numerical coincidence that could fail at larger `d`.
     **Conclusion: the pair-table/ledger construction has zero silent omission at any fixed resolution — S1 item 1
     is CLOSED.**
  2. **OPEN — the `weld/E.08` transport bridge itself.** No `ε_bridge` tolerance has been computed for going from a
     per-window (fixed-`d`) ledger-completeness statement to the whole shrinking family `{I_j}_{j→∞}` — i.e. item 1
     closes "no address is silently dropped at any one fixed active-set depth," but does NOT by itself say the
     active-set depth `d(j)` needed to represent `I_j` stays achievable/finite as `j→∞`, or that consecutive `d(j)`
     bridge with a declared, summable tolerance. This is a genuinely new obligation belonging to S1/S2's boundary,
     not present in any existing weld or proposal, and it is NOT closed by item 1's code-correctness argument.
  3. **Sufficiency (`weld/E.06`)** is explicitly deferred to S3, not claimed here.
* S1 is therefore **still not a completed theorem**, but is now narrower and more precise than at first writing:
  the "does the accounting machinery ever silently drop an address" half is CLOSED (item 1, exact); the remaining
  content of S1 is entirely the `weld/E.08` cross-window bridge (item 2) — a single, well-posed open obligation
  rather than two entangled ones.

## 4. Next concrete step (does it advance S1/S2/S3? — yes, closes S1 to a single open item)

Item 1 is now closed (§3). The only remaining S1 obligation is item 2: derive the `weld/E.08` bridge tolerance
`ε_bridge` across the family `{I_j}` — i.e. state and check a concrete recursion for how the active-set depth `d(j)`
required to represent window `I_j` grows with `j`, and whether the ledger statement transports across `j→j+1` with a
summable defect. This is naturally the same object S2 needs (the scale-recursion `R_{j+1} ≤ qR_j + β_j`), so item 2
should be attacked jointly with S2 rather than as a separate S1 task — it does not need its own new machinery.

Parent registration: this document itself is `NEW DERIVATION / PROPOSAL`, not yet in Toledo; register after
independent review, parented to `weld/M.02.v1`, `weld/E.05.v1`, `weld/E.06.v1`, `weld/E.08.v1`, `EQ-015/M.04.v1`,
`EQ-001/C.16.v1`, and `PROP-P3-RECENT-RETENTION-BOUND-ENERGY-ONLY-REFUTED` (derived_via: `refines` — restates the
refuted universal-bound claim as a per-address, cross-scale ledger-completeness claim instead).
