# P21 — RET-Check: an AI-independent recursive provenance auditor

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder order, 2026-09-07 (Blackbox Log
> `BBL-2026-09-07-223`, verbatim): "RET-Check v0.1 — AI-independent recursive provenance auditor:
> โปรแกรมเล็ก Python standard library ไม่มี LLM (AI=0 ตอน runtime) ... ตั้ง pass/fail ก่อนเขียน" (a small,
> standard-library-only Python program, no LLM, `AI = 0` at runtime; declare pass/fail before
> writing the code). AI drafted this card. Comparison language is same/different/cited only.

## id

`P21`

## Rule

Every claim carried across a Human/AI provenance network in this repository — a claim card, a
manuscript's own self-application, a chain of endorsements between agents — may be run through
`./cli/glosa ret check <case.json|case.csv>` (or `python3 scripts/ret_check.py <case>` directly)
before it is treated as corroborated by "several endorsements". The tool computes, from declared
provenance rows `{claim, agent, parent, source_root, root_independent, record_type, evidence_ref}`
grouped by `claim`:

- **N_A(c)** — distinct endorsing agents (`record_type = endorsement`).
- **N_P(c)** — distinct provenance roots, full stop, regardless of declared independence (the
  founder's own Mirror example: 1 shared root S1 → `N_P = 1`, not 0 — corrected 2026-09-08, see
  `cases/ret/PREREGISTRATION_v0_1.md`'s dated note; an earlier draft counted only
  independence-declared roots here, mis-scoring Mirror as `N_P = 0`).
- **N_P^ind(c)** — the narrower, SEPARATE count of those roots additionally declared
  `root_independent = true`. The RET RISK formula uses `N_P^ind(c)`, never the raw `N_P(c)`.
- **Flagship** — `N_A(c) ↑ ⇏ N_P(c) ↑` (the theory's own non-entailment), read against the raw root
  count: endorsement count rising never by itself implies provenance-root count rising, and rising
  provenance-root count never by itself implies independence.
- **Recursive cycle** — any directed cycle in the `parent → agent` graph, and whether it returns to
  an origin node.
- **External interruption** — a `world_record` row, or an independent `review` row, whose own
  ancestry does not pass through a detected recursion cycle.
- **RET RISK** (LOW/MEDIUM/HIGH) by the exact pre-registered rule in
  `cases/ret/PREREGISTRATION_v0_1.md` ("RET RISK formula", computed from `N_P^ind`), never
  re-tuned per case.

The program implements the definitions of `The_Recursive_Epistemic_Tunnel_GENESIS_FIRST_FULL_v2_0.md`
§13–21 and §25–30 (network generalization, Recursive Epistemic Reflection, the Epistemic Mirror
Effect, provenance independence, candidate forgetting, the RET state vector, evidence-driven
convergence vs. tunnel contraction, the AI-Independent Consequence Requirement, AI-Off
World-Closure) — it does not invent new definitions of its own. Every quantity's docstring in
`scripts/ret_check.py` cites the section and working alias (`RET-Nxx`) it implements.

Toledo codes for the `RET-Nxx` objects are not yet registered (`P19`); cite the manuscript's own
working alias until the registrar assigns a code, then update this card, the script's docstring,
and the report text together (one-fact-one-home, `P0`).

## Why / incident

The founder's own order names the motivating risk directly: a recursively co-produced theory (a
human and an AI drafting together, citing their own programme's internal objects) can accumulate
apparent corroboration — many endorsing turns, high mutual confidence — without a corresponding
increase in provenance independent of that same loop. §15's Epistemic Mirror Effect and §21's
Collective Epistemic Hallucination name this exact failure mode. Before RET-Check existed, nothing
in this repository's tooling distinguished "5 agents restated the same root" from "5 independent
roots converged" — both looked like "5 endorsements" to a casual reader. RET-Check makes that
distinction a computed readout instead of a narrative judgment.

## Inputs → outputs

- **Inputs:** provenance rows (JSON list, `{"rows": [...]}` JSON object, or CSV) as specified above
  and in `scripts/ret_check.py`'s module docstring.
- **Outputs:** a "RET SELF-AUDIT" plain-text report per claim (`--json` for the structured form),
  never a silent pass — every report restates the program's own limits (below) in its header.

## Gate

This is a diagnostic tool, not a publish gate: it exits 0 whenever a report was produced,
regardless of the RET RISK label the report carries (exit 2 only on invalid input). A HIGH RET
RISK reading on a claim does not by itself block `P10`'s publish gate — it is evidence a human
reviewer should read before deciding whether the claim is corroborated or merely recirculated. The
one hard case is the self-application run (`cases/ret/self_ret_v2_0.json`, built from this very
manuscript's own Core Epistemic Registration): the preregistration requires it to read HIGH with
the sentence "The RET manuscript itself remains at RET-risk until independent world-side or
reviewer-side resistance is added." — a passing test suite that does not enforce this sentence has
not actually checked the tool.

## Human / AI split

Founder/human: declares `root_independent` and `record_type: world_record`/independent `review` on
every row (these are the program's INPUT DECLARATIONS, never computed facts — see Disclaimers);
decides what a HIGH RET RISK reading means for the claim's status. AI: builds and runs the case
files, reads the computed report, never asserts the report as settled truth about the claim.

## Disclaimers

**The program audits declared structure, never truth.** `root_independent` (is a provenance root
independent) and the world-side status of a record (`world_record`, or a `review` marked
independent) are **input declarations** supplied by the case author — the program has no way to
inspect whether a declared-independent root truly shares no dataset, model, or assumption with
another (§16's own caution), or whether a declared world record truly occurred outside the
recursive network. Every report's header states this plainly, and every case file in this
repository was authored with that limit in mind, not discovered by the tool itself.

## NC pairs

- agreement ≠ provenance — `N_A(c)` rising says nothing about `N_P(c)`.
- root count ≠ independence — `N_P(c)` counts distinct roots regardless of independence; only
  `N_P^ind(c)` counts the ones declared independent, and only the latter feeds RET RISK.
- agents ≠ roots — one root can be echoed by many agents; one agent can cite many roots.
- cycle ≠ tunnel — a recursive cycle is a structural fact (§14); calling it a "tunnel" additionally
  requires the absence of growing external resistance/provenance (§19.2, RET-N10) — see §19.1's
  evidence-driven convergence, which can also show `D^eff ↓` without being a tunnel.
- declared-independent ≠ independent — `root_independent: true` on a row is what the case author
  wrote, never a property the program verified.

## Not-do

- Do not retune the RET RISK formula after seeing a case's output to make a preferred case pass —
  the formula is fixed in `cases/ret/PREREGISTRATION_v0_1.md`, written before the code.
- Do not treat a LOW/MEDIUM RET RISK reading as proof the claim is true — it only says the declared
  provenance structure does not match the tunnel pattern; the claim's truth is a separate question.
- Do not add a special-case exemption so the self-application case reads safe.
- Do not call the tool's own report a certification — it is a readout of the rows it was given.

## Tier

Dr — specified from the founder's verbatim order and the manuscript's own §13–21/§25–30;
`tests/test_ret_check.py` gives `finite_diagnostic` grounding for the computed quantities
themselves (run it and read the output — do not take this card's word for it).
