# P22 — Reproduction Ledger: a hash-frozen, re-runnable check against a declared oracle

tier: Dr (specified from the founder ruling and the design spec below; independently unreviewed)

> readout-not-truth applies to this card itself. Founder ruling `BBL-2026-09-07-229` (Toledo
> overnight handoff, "Resistance ladder + Reproduction Ledger",
> `toledo/ops/HANDOFF_OVERNIGHT_2026-09-06.md`'s 2026-09-08 entry): reproducible computation with
> an oracle OUTSIDE our loop counts as AI-off world-side resistance; the programme's scoring must
> show which resistance steps are present. Field-by-field reference:
> `design/RESISTANCE_LADDER_v0_1.md` §2 (this card's own specification pair, the way
> `toledo/registry/SCHEMA.md` is the reference for `CANONICAL.json`). AI drafted this card.
> Comparison language is same/different/cited only.

## id

`P22`

## Rule

A **Reproduction Card** (`schema/reproduction_card.schema.json`, one JSON file per card under
`cases/repro/`) is how this repository holds R3/R4/R6 of the Resistance Ladder (`P23`) for a
reader other than the maker — never by a prose paragraph claiming a run happened, always by a
file that exists.

The binding order, enforced by the tooling, never by convention alone:

1. **Pre-register first.** `glosa repro new` writes `preregistered_prediction.{statement,
   tolerance, declared_at}` together with `run: null` and `result.status: PENDING` in the same
   file, in the same act — a card can never exist with a filled `run`/`result` and no prior
   `preregistered_prediction`. Refuses (exit 1, no file written) if `--statement` or `--tolerance`
   is empty, the same fail-closed shape `glosa session close --retention-note` already uses for a
   different mandatory human-authored field.
2. **Run second, once, immutably.** `glosa repro run <card>` executes the declared `command` via
   `subprocess` in the runner's own stdlib-only process, SHA-256-hashes every declared
   `--input`/`--output` file, and writes `run{}` + `result{}` back — but refuses if `run` is
   already filled (a filled card is immutable; re-checking it is `repro verify`'s job, never an
   overwrite) or if `preregistered_prediction.declared_at` is missing.
3. **Verify third, by someone else.** `glosa repro verify <card> --reviewer-identity <id>`
   re-executes `run.command` fresh, in a clean temporary directory, under a **different** identity
   than whoever ran it first (maker ≠ checker, `P10` NC-28/29), recomputes the hashes, and confirms
   they equal the ones already recorded. On match it scaffolds a `review_report.yaml`
   (`role: SourceAuditor`) rather than mutating the card — this file, not `repro run`'s own first
   execution, is what actually **holds** R3 for anyone but the maker.
4. **Feed the provenance graph, honestly typed.** `glosa repro to-ret <card> --claim <id>` converts
   an external-oracle card into one `RET-Check` provenance row (`P21`), per the mapping in
   `design/RESISTANCE_LADDER_v0_1.md` §4 — and **refuses** for `oracle.kind == "coq_kernel"`,
   because Coq closure is machine-side resistance (R2), never a world-side/reviewer-side row.

**Why `oracle.kind` has exactly five values and no "none".** Every card in the Ledger names the
closest thing its own run's output is being checked against, even when that comparison is trivial
— `published_value`, `independent_implementation`, `public_dataset`, `coq_kernel`, `human_review`.
A genuinely oracle-free run belongs in the project's own test suite, not this Ledger, because this
Ledger's one job is to show which *external* resistance step was actually exercised, never merely
"the script ran" (`design/RESISTANCE_LADDER_v0_1.md` §2).

**Toledo mapping is a citation, never a copy** (`P19`/`P0` one-fact-one-home). A card naming a
Toledo code is not duplicated into Toledo — `toledo_codes[]` may be empty only when
`status: "pending_toledo_code"` is also set, and it is never populated by inventing a code.
Correction (2026-09-08 — an earlier draft of this card, and of
`design/RESISTANCE_LADDER_v0_1.md` §2/§3, specified a `glosa repro run --register-toledo` flag
that was never implemented in `cli/glosa` — `glosa repro run`'s own options are only `--command`/
`--input`/`--output`/`--reference`, confirmed live: `--register-toledo` is rejected as an
unrecognized argument. Toledo's own `registry/SCHEMA.md` addendum already documented the actual
mechanism on its side; this card is corrected here to match, rather than leaving glosa's own
methodology describing a capability that does not exist): the citation index is instead populated
from the **Toledo side**, by that repo's own `scripts/register_reproduction_evidence.py
[--glosa-repo PATH]`, which reads glosa's `cases/repro/*.json` cards and `reviews/routes/**/
review_report.{yaml,json}` files directly and regenerates
`registry/reproduction_card_index.json` / `registry/review_report_index.json` wholesale (never
appends — a full projection of glosa's current on-disk state, rerun whenever a card or review
changes). There is no glosa-side flag or command that writes into Toledo's registry; a card is
made citable simply by existing under `cases/repro/` with a real `toledo_codes[]` entry.

## Why / incident

The founder's own worked case (`design/RESISTANCE_LADDER_v0_1.md` §6, Card 1) is `EQ-068`: Genesis
already discloses a Higgs-mass prediction that fails a 5% PDG band by 74.13%. Before this card
type existed, that disclosed FAIL sat as prose inside `genesis_root.json`, re-readable but not
re-runnable, hash-frozen, or independently re-checkable by anyone who had not read the source file
themselves. The Reproduction Card exists so a disclosed FAIL becomes exactly as strong a piece of
filed evidence as a PASS would be (`P0`'s design principle, restated at `P23` §0): the ladder's own
proof that its external-oracle rungs (R4/R6) can genuinely fail, not a mechanism engineered to
always confirm.

## Inputs → outputs

- **Inputs:** a claim (free text or a `claim_card.claim_id`), the Toledo code(s) it backs (or an
  honest `pending_toledo_code` status), a declared oracle, a pre-registered prediction and
  tolerance written before any run, and — once run — a command, its declared input/output files,
  and the identity that ran it.
- **Outputs:** `cases/repro/<ID>.json`, self-checked against `schema/reproduction_card.schema.json`
  on write; a `review_report.yaml` from `repro verify`; a Toledo `reproduction_card_index.json` /
  `review_report_index.json` row, populated Toledo-side by that repo's own
  `scripts/register_reproduction_evidence.py` (never a glosa-side flag — see the Rule section's
  2026-09-08 correction); a RET-Check provenance row from `repro to-ret`.

## Gate

`glosa repro new` is fail-closed on the pre-registration fields (§Rule item 1). `glosa repro run`
is fail-closed on re-execution of an already-filled card and on a missing `declared_at`. Neither
command ever fabricates a `PASS` — `scripts/repro_check.py`'s comparator returns `ERROR`, honestly,
whenever it cannot mechanically parse `preregistered_prediction.tolerance` against the run's own
output well enough to compute a real `PASS`/`FAIL` (never a guessed verdict). A `FAIL` result is
never retried, re-tuned, or silently converted to `ERROR` to avoid reporting it — the same
"do not retune after seeing output" discipline `P21`'s preregistration already states for the RET
RISK formula, applied here to individual reproduction runs.

## Human / AI split

Founder/human: decides which claims get a Reproduction Card and what tolerance genuinely could
count against the claim (the AOWC non-vacuity condition, `P23` R6); confirms a `repro verify`
identity is genuinely independent of the run's own maker. AI: scaffolds cards, runs the declared
command, computes hashes, reads back the comparator's own output, never asserts a result the
comparator itself did not compute.

## Disclaimers

A Reproduction Card audits **declared, filed evidence of a run**, never the underlying truth of
the claim it backs (`P19`'s own disclaimer, restated) — a card whose `result.status` is `PASS`
still leaves the claim's own `tier`/`k_state` exactly where `P6`/`P10` already put it. `oracle.kind
== "human_review"`/`root_independent` declarations a card feeds into RET-Check remain **input
declarations**, never facts the tooling verified (`P21`'s own disclaimer, inherited unchanged).

## NC pairs

Pre-registered ≠ run · run ≠ verified (`repro run` ≠ `repro verify`, maker ≠ checker) · held ≠
passed (R3/R4 hold on a disclosed `FAIL` too, `P23` §0) · registered in Toledo ≠ copied into
Toledo (`P19`) · declared-independent root ≠ independent root (`P21`, inherited unchanged by every
card converted through `repro to-ret`).

## Not-do

- Do not write `run`/`result` before `preregistered_prediction` exists in the same file.
- Do not overwrite an already-filled `run{}` — start a fresh card, or run `repro verify` instead.
- Do not invent a Toledo code to make `toledo_codes[]` non-empty; use
  `status: "pending_toledo_code"` and leave it honestly empty.
- Do not present a disclosed `FAIL` as a defect to explain away — it is filed evidence the ladder's
  external-oracle rungs are non-tautological.
- Do not feed a `coq_kernel`-oracle card into RET-Check — `repro to-ret` refuses this mechanically;
  never work around the refusal by hand-authoring the row instead.
- Do not import `mpmath`/`numpy` (or anything else) into `scripts/repro_check.py`'s own driver
  process — a card's own oracle computation that needs them runs as a separately declared
  subprocess, per `environment.packages`.

## Tier

Dr — specified from the founder ruling and `design/RESISTANCE_LADDER_v0_1.md` §2/§3; independently
unreviewed. `tests/test_reproduction_card.py` gives `finite_diagnostic` grounding for the schema
and kernel checks themselves — run it and read the output, do not take this card's word for it.
