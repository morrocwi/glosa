# RET-Check v0.1 — Preregistration

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this document itself. Written BEFORE `scripts/ret_check.py` per
> founder order (Blackbox Log `BBL-2026-09-07-223`): "ตั้ง pass/fail ก่อนเขียน" (declare pass/fail
> before writing the code). If the finished program cannot separate scenario A from scenario B, or
> reports the self-application case (item 4 below) as safe, **the artifact FAILS by this document**
> — the rule set is not to be re-tuned after the fact to make a failing case pass.

> **Correction, 2026-09-08 (before any case was tuned to match this document):** the operator
> definition of `N_P(c)` below was corrected to match the paper/founder text. The founder's own
> Mirror example is 1 shared root S1 → `N_P = 1`, not 0, even though that root is not independent
> — a first implementation of `scripts/ret_check.py` had counted only independence-declared roots
> as `N_P`, which mis-scored Mirror as `N_P = 0`. `N_P(c)` is now the raw count of distinct
> provenance roots regardless of declared independence; the independence-only count is its own
> separate, explicitly labelled readout, `N_P^ind(c)`, which the RET RISK formula uses (unchanged
> — every rule below always operated on the independence-only count; only its name and the
> flagship line's raw-count reading changed). No pre-registered RET RISK verdict changed because of
> this correction; every `N_A`/`N_P` value quoted below for scenarios A/C/D/E and the
> self-application case is updated to the corrected `N_P`, with `N_P^ind` given alongside.

## What this document is

A preregistration of the pass/fail scenarios for RET-Check v0.1, an AI-independent (stdlib-only,
no network, no LLM call, `AI_runtime = 0`) auditor of the **declared structure** of a provenance
graph, built from `The_Recursive_Epistemic_Tunnel_GENESIS_FIRST_FULL_v2_0.md` §13–21 and §25–30
(network generalization, Recursive Epistemic Reflection, the Epistemic Mirror Effect, provenance
independence, candidate forgetting, the RET state vector, evidence-driven convergence vs. tunnel
contraction, the AI-Independent Consequence Requirement, AI-Off World-Closure). The program is a
structural auditor of a declared graph, not a truth-oracle over the world the graph describes — see
"What this program can NOT verify" below, which is binding on every report the program ever emits.

## Inputs and computed quantities (definitions, cited to the theory)

Given rows `{claim, agent, parent, source_root, root_independent, record_type, evidence_ref}`
(JSON or CSV; `record_type ∈ {endorsement, world_record, review}`; optional per-row
`effective_alternatives_before`, `effective_alternatives_after`, `self_application`), grouped by
`claim`:

- **N_A(c)** — number of *distinct* agents with `record_type = endorsement` for claim `c`
  (§15, the Epistemic Mirror Effect's `N_A(c) = number of endorsing agents`).
- **N_P(c)** — number of *distinct* `source_root` values for `c`, **regardless of whether any of
  them is declared independent** (§15's literal `N_P(c)` as a raw root count; corrected 2026-09-08,
  see the note above). A single shared, non-independent root still counts once.
- **N_P^ind(c)** — the narrower count of those roots **additionally** declared
  `root_independent = true` (§16's typed provenance structure `Π(c) = (V_c, E_c, τ_c)`, RET-N07).
  **`root_independent` is an input declaration, not a computed fact — see the disclaimer below.**
  The RET RISK formula below is computed from `N_P^ind(c)`, never the raw `N_P(c)`.
- **Recursive cycle** — any directed cycle in the graph of `parent → agent` edges for `c` (§14,
  RET-N04, "a minimal cycle is `a_i → a_j → a_i`"; a multi-agent cycle generalizes this). The
  program also reports whether the cycle returns to an *origin* node (a row whose `parent = "-"`)
  — "any return-to-origin path".
- **External interruption** — a `world_record` row, or a `review` row declared
  `root_independent = true`, whose own ancestry (walked backward through `parent` edges) does not
  intersect any node of a detected recursion cycle. This operationalizes §28's AI-Independent
  Consequence Requirement (RET-N16: `CausalAncestry(y) ⊄ 𝒢^recursive_{≤τ}`) and §29–30's
  AI-Off World-Closure (RET-N17/RET-N18) as a graph-lineage test the program can actually run.
- **Effective-alternatives delta** (optional) — `effective_alternatives_after −
  effective_alternatives_before`, when both are supplied on at least one row of the claim. Used
  only to label a **regime** (§19): `evidence_driven_convergence` (RET-N09: delta < 0 *and* an
  external interruption is present) vs. `tunnel_contraction_risk` (RET-N10: delta < 0, a cycle is
  present, and no external interruption is present). The regime label is a report annotation; it
  does **not** feed the RET RISK formula below (which the founder specified in terms of N_A,
  N_P^ind, cycle, and interruption only).
- **Flagship readout** — §15's non-entailment, RET-N06: `N_A(c) ↑ ⇏ N_P(c) ↑`. The report always
  states the `N_A` vs the raw `N_P` comparison for the claim under this heading, never a bare
  pass/fail.

Toledo codes for RET-N04/05/06/07/09/10/16/17/18 are not yet registered (`methodology/P19`); the
program's docstring and every report cite them by the manuscript's own working aliases
(`RET-Nxx`) and will be updated to Toledo codes once the registrar assigns them.

## RET RISK formula (pre-registered, exact — do not retune after seeing case output)

Evaluated in this order, first match wins, using `N_P^ind(c)` (the independence-declared root
count), never the raw root count `N_P(c)`:

1. **LOW** if `N_P^ind(c) ≥ N_A(c)` (independent provenance keeps pace with or exceeds endorsement).
2. **LOW** if an external interruption is present **and** `N_P^ind(c) ≥ 1`.
3. **HIGH** if `N_A(c) > N_P^ind(c)` **and** a recursive cycle is detected **and** no external
   interruption is present.
4. **MEDIUM** — the remaining case: `N_A(c) > N_P^ind(c)` and either no cycle was detected, or an
   interruption is present but `N_P^ind(c) = 0`.

## The five pre-registered scenarios (declared BEFORE `scripts/ret_check.py` exists)

### A — Mirror (`cases/ret/A_mirror.json`)
5 agents endorse the same claim, all citing one shared, **not** independent (`root_independent:
false`) provenance root, arranged so the endorsement returns to its own origin agent (a recursive
cycle, §14/§15's Epistemic Mirror Effect). **Expected:** `N_A = 5`, `N_P = 1` (the one shared root,
counted; corrected 2026-09-08 — see the note above), `N_P^ind = 0` (that root is not independent),
cycle detected, no external interruption ⇒ **RET RISK: HIGH**. The report must **not** read the 5
endorsements as 5 pieces of independent evidence — the flagship line must show `N_A(5) > N_P(1)`,
and `N_P^ind(0)` is what actually drives the HIGH verdict via rule 3.

### B — Independent convergence (`cases/ret/B_independent.json`)
5 agents each endorse the same claim from 5 **distinct**, independently declared provenance roots,
no shared lineage, no cycle. **Expected:** `N_A = 5`, `N_P = 5`, `N_P^ind = 5`, no cycle ⇒ **RET
RISK: LOW**. Must **not** be flagged the way A is — same `N_A` as A, different `N_P`/`N_P^ind` and
structure, different verdict.

### C — Evidence-driven convergence (`cases/ret/C_evidence_driven.json`)
3 agents endorse from one shared, non-independent root (declining number of live rival
hypotheses — `effective_alternatives_before/after` supplied showing a decrease), and one
`world_record` row is added whose lineage does not pass through the endorsement chain.
**Expected:** `N_A = 3`, `N_P = 2` (the shared root plus the world-record's own root, both
counted), `N_P^ind = 1` (only the world-record's root is independent), an external interruption
present ⇒ rule 2 fires (on `N_P^ind`) ⇒ **RET RISK: LOW** (rule 3's HIGH is pre-empted by the
interruption). Regime label: `evidence_driven_convergence` (RET-N09), explicitly **not**
`tunnel_contraction_risk` — the report must say why: alternatives contracted *because* an
independent world record entered, not because recursion alone dominated.

### D — Recursive return (`cases/ret/D_recursive_return.json`)
Three agents `H → AI1 → AI2 → H` (§14's multi-agent cycle), one shared non-independent root, no
external interruption. **Expected:** cycle detected = true, the cycle's node set includes `H`
(return-to-origin = true), `N_A = 3`, `N_P = 1` (the one shared root, counted), `N_P^ind = 0` ⇒
`N_A(3) > N_P^ind(0)` ⇒ **RET RISK: HIGH** by the same rule 3 as A — D is pre-registered
specifically to exercise cycle detection on a genuine return path (distinct from A's purpose,
which is the `N_A` vs `N_P^ind` mismatch), not to test a new risk bucket.

### E — External interruption present/absent (`cases/ret/E_interruption.json`)
One file, two claims sharing the same endorsement structure (`N_A = 3`, one shared non-independent
root, a cycle present) — claim `e-with-interruption` additionally carries an independent `review`
row outside the cycle; claim `e-without-interruption` does not. **Expected:**
`e-with-interruption` ⇒ `N_P = 2` (the shared root plus the reviewer's own root), `N_P^ind = 1`
(only the reviewer's root) ⇒ rule 2 fires (external interruption present, `N_P^ind ≥ 1`) ⇒ **LOW**;
`e-without-interruption` ⇒ `N_P = 1`, `N_P^ind = 0` ⇒ rule 3 fires ⇒ **HIGH**. This isolates the
interruption variable from everything else held constant.

## Self-application (item 4 of the founder's order, not a pass/fail scenario in the A–E sense)

`cases/ret/self_ret_v2_0.json` is built from the RET manuscript's own Core Epistemic Registration
(the manuscript's own header, quoted verbatim in `BBL-2026-09-07-223`'s source chat and the
manuscript file itself): Human author — Yaoharee Lahtee; AI Model — GPT-5.6 Sol; Interactional
Expert — None; Genesis and Toledo cited as the manuscript's own internal programme sources (same
root as the manuscript itself, not independent); Independent Human Review — None; AOWC empirical
record — None. Modeled as a 2-agent recursive dialogue (`Yaoharee → GPT-5.6 Sol → Yaoharee`, a
minimal §14 RET-N04 cycle) over one shared, non-independent internal-programme root, with **no**
`world_record` or `review` row (matching "Independent Human Review: None" / "AOWC empirical record:
None").

**Expected:** `N_A = 2`, `N_P = 1` (the single shared internal-programme root, counted; corrected
2026-09-08), `N_P^ind = 0` (that root is not independent), cycle detected ⇒ **RET RISK: HIGH**, and
the report for this case must carry, verbatim, the sentence:

> The RET manuscript itself remains at RET-risk until independent world-side or reviewer-side
> resistance is added.

**If the program instead reports this case as safe (LOW/MEDIUM, or omits the sentence), the
artifact FAILS this preregistration.** The rule set in "RET RISK formula" above is not to be
loosened, and no special-case exemption for the self-application claim is to be added, to make
this case pass — a failure here is reported honestly as a failure, and the theory/operator is what
gets revisited, never the test.

## What the program can NOT verify (binding disclaimer, must appear in every report header)

- **Independence of a provenance root** (`root_independent: true/false` on a row) is an **input
  declaration** supplied by the case author, not a fact the program derives or checks. The program
  has no way to inspect whether two declared-independent roots actually share a dataset, a model,
  an institutional pipeline, or an assumption (§16's own caution: "a simple root count is useful
  for audit but insufficient as a universal measure of evidence independence").
- **World-side status of a record** (`record_type: world_record`, or `review` marked
  `root_independent: true`) is likewise an **input declaration**. The program never fetches,
  scores, or verifies that a named record actually occurred in the world, was decisive, or was
  produced outside the recursive network — it only checks whether the *declared* lineage of that
  row, as given in the input rows, intersects a detected cycle.
- The program audits **declared graph structure** (who is declared to have endorsed what, whose
  parent is whom, which roots and records are declared independent) — never the underlying truth
  of the claim, the competence of any agent, or whether a human or AI actually behaved as the rows
  say. This is the same readout-not-truth floor as the rest of this repository (`AGENTS.md` rule 1)
  applied to provenance-graph auditing specifically.

## Tier

Dr — specified from the founder's verbatim order (`BBL-2026-09-07-223`) and the manuscript's own
§13–21/§25–30; independently unreviewed. `finite_diagnostic` will apply once `tests/test_ret_check.py`
is executed and its output recorded (see `methodology/P21_ret_check.md`).
