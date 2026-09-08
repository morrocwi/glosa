# P23 — Resistance Ladder: the score is a set of rungs held, never one number

tier: Dr (specified from the founder ruling and the design spec below; independently unreviewed)

> readout-not-truth applies to this card itself. Founder ruling `BBL-2026-09-07-229`. Field-by-
> field reference: `design/RESISTANCE_LADDER_v0_1.md` §0–§1 (this card's own specification, the
> way `toledo/registry/SCHEMA.md` is the reference for `CANONICAL.json`). Narrated against
> `The_Recursive_Epistemic_Tunnel_GENESIS_FIRST_FULL_v2_1.md` §27–31 (Historical Invariance, the
> AI-Independent Consequence Requirement RET-N16, AI-Off World-Closure RET-N17/N18, RET-N19, and
> Appendix E's Minimal AOWC Checklist) for the R6 rung. AI drafted this card. Comparison language
> is same/different/cited only.

## id

`P23`

## Rule

**Design principle (binding, restated verbatim):** the score is a SET of rungs held, each with an
evidence pointer — never a single number that hides a missing rung. A rung is held only by a file
that exists (a Coq report, a Reproduction Card, a review report). `glosa score <artifact>` and
Toledo's own per-entry `resistance` block (`design/RESISTANCE_LADDER_v0_1.md` §5, built by a
sibling stream) never emit a scalar; both emit a per-rung `{rung, held, evidence[], reason}` row.

| Rung | Held by | Does **NOT** certify |
|---|---|---|
| **R0 — Stated** | The artifact's own `statement` field is non-empty. | Anything beyond "this was written down." |
| **R1 — Pre-registered falsifier / claim boundary** | A `claim_card.five_questions.tested.falsifier` (non-TODO) *or* a linked `reproduction_card.preregistered_prediction.declared_at` predating its own `run.date`. | That the falsifier is a good one, or that anyone has tried to defeat the claim yet. |
| **R2 — Coq-closed (kernel outside our loop)** | Toledo's `coq_status == "closed"` for the code. | Empirical truth — Coq closure certifies internal consistency of a finite formal model, never that the model matches the world. |
| **R3 — Reproducible run, hash-frozen, AI = 0** | A `reproduction_card` with a filled `run{}` (`command`, `input_hash`/`output_hash`, `ai_at_runtime: 0`, `date`). | That the run's result matched anything — a card holds R3 with `result.status: FAIL` or `ERROR` too. |
| **R4 — External oracle** | The same card's `oracle` names `published_value`/`independent_implementation`/`public_dataset`, pinned, with a filled `result` (PASS or FAIL). | That the result was a PASS — a disclosed FAIL, honestly run, is exactly what R4 certifies. |
| **R5 — Independent reviewer or interactional-expert record** | A `review_report.yaml` at independence class ≥ I2, or a documented `X_p^int` (`P20`), naming the artifact. | That the review reached a favorable verdict. |
| **R6 — AOWC world record** | An R4-holding card additionally passing the AOWC gate (frozen before the run, `ai_at_runtime: 0`, a tolerance that could genuinely count against the claim). | That the outcome not producible by the recursion loop was the desired one. |

R0–R2 are checkable from Toledo's own files alone. R3–R6 require a Reproduction Card or a review
report; R6 additionally requires the AOWC gate check (`kernel.aowc_gate_check`, one shared function
between `glosa score` and Toledo's own `scripts/compute_resistance.py`, one-fact-one-home between
the CLI and the Toledo build). **Machine-side vs. world-side, kept explicitly separate** (the
founder's own phrase): R2 is resistance from a kernel outside the authoring loop, but still a
formal check, never a world check. A card whose `oracle.kind == "coq_kernel"` feeds `glosa score`'s
R2 row directly and is never converted into a RET-Check provenance row (`P21`, `P22`) — R2's
machine-side count and RET's `N_P^ind` world/reviewer-side count never blend into one number.

**`glosa score <artifact>`** (`--kind toledo-code|claim_card|release_manifest`, auto-detected the
same way `glosa check` infers a schema stem for a file path; a bare string is treated as a Toledo
code): scans, in order, Toledo's own `coq_status` (R2, when a Toledo registry is reachable and a
code is given or inferable), every `cases/repro/*.json` Reproduction Card whose `toledo_codes[]`/
`claim` matches (R1/R3/R4/R6, per the table above), and every `reviews/routes/**/review_report.yaml`
naming the artifact (R5). Prints the R0–R6 table with `held`/`evidence`/`reason` filled per
artifact; `--json` for the structured form. **There is no `--score` flag** — this command is built
to refuse collapsing the table to one number, on purpose.

## Why / incident

The founder's own worked case is `EQ-068`: Genesis discloses a Higgs-mass prediction that fails a
5% PDG band by 74.13%. A single aggregate "resistance score" would have to choose between hiding
that FAIL (dishonest) or tanking a number that says nothing about which specific rung is actually
missing (uninformative either way). Per-rung reporting makes both failure modes structurally
impossible: R4 reads `held: true` with the FAIL result attached as its own evidence, and every
other rung reads independently of it.

## Inputs → outputs

- **Inputs:** an artifact identifier (Toledo code / `claim_card` path / `release_manifest` path),
  the Reproduction Cards and review reports that name it, and — for R2 — a reachable Toledo
  registry.
- **Outputs:** the R0–R6 table (plain-text or `--json`), each row citing the file(s) that hold it
  or the reason none does; never a scalar.

## Gate

`glosa score` never blocks a release by itself — it is a readout, the way `glosa ret check` is
(`P21`). A missing rung is reported, not silently omitted; `P10`'s publish gate is what decides
what a given missing rung means for a specific artifact's publication, never this command.

## Human / AI split

Founder/human: decides which rungs a given artifact needs before it may be presented at a given
`tier`/`k_state` — this card names what a rung certifies, never what is "enough". AI: runs the
scan, reads the evidence files it finds, reports exactly what it found, never upgrades a `reason:
"no ... found"` row into `held: true` on inference alone.

## Disclaimers

This ladder audits **declared, filed evidence of resistance**, never the underlying truth of a
claim (`P19`'s own disclaimer, restated) — a full R0–R6 row of `held: true` still leaves the
claim's own `tier`/`k_state` exactly where `P6`/`P10` already put it; passing every rung licenses
nothing beyond "every named check was actually run and filed."

## NC pairs

Held ≠ passed (R3/R4 hold on FAIL too) · registered ≠ verified (`repro run` ≠ `repro verify`,
maker ≠ checker) · machine-side (R2) ≠ world-side (R3–R6) · declared-independent ≠ independent
(`P21`, inherited unchanged by every card converted through `repro to-ret`) · one rung held ≠
artifact certified.

## Not-do

- Do not collapse the seven-rung table to a single number anywhere — CLI, Toledo page, `/v1/` JSON,
  or a summary sentence in a handoff.
- Do not mark a rung `held` without a concrete evidence pointer to a file that exists.
- Do not feed a `coq_kernel`-oracle card into RET-Check's `N_P`/`N_P^ind`.
- Do not present a disclosed FAIL on an R4/R6-holding card as a defect to be hidden or explained
  away in the reported row.

## Tier

Dr — specified from the founder ruling and `design/RESISTANCE_LADDER_v0_1.md` §0/§1/§3;
independently unreviewed. Every Toledo count/quote that design document itself cites was read by a
command run while drafting it (reported, not asserted from memory) — the design decisions
themselves await this build's own test suite before any part of it is `finite_diagnostic` in the
fuller "tests executed" sense. `tests/test_score.py` gives that grounding for `glosa score`'s own
rung-computation logic — run it and read the output.


### Addendum 2026-09-08 — the Equation River codes in Toledo
The strengthening model behind this ladder is registered in Toledo (v1.7): rung set S_n(q) = weld/M.33.v1; strengthening law S_{n+1} = (S_n ∪ A_n) \ W_n = weld/M.34.v1; strength readout σ(q) = S_n (the held set, never a scalar warrant) = weld/M.35.v1; return map q^{(v+1)} = Φ(q^{(v)}, δ) with a LINEAGE 'revised' event = EQ-015/H.50.v1; stage non-collapse (thought ≠ registered ≠ closed ≠ reproduced ≠ oracle-checked ≠ reviewed ≠ world-recorded; PASS ≠ proven) = weld/M.36.v1; stages 3–4 computed on ℚ with an oracle outside the loop = EQ-015/M.17.v1. Founder instruction BBL-2026-09-08-238.
