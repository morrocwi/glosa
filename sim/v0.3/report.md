# K4-report — glosa sim/v0.3 prototype evaluation

Tier of every number in this report: **finite_diagnostic** — an exact tally over one fixed,
printed 180-card synthetic corpus, this run, these files as they exist on disk today. Not a
general claim about kernel or prototype quality on any other corpus, on real-world claim cards,
or on differently-worded injections of the same defects. Readout, not truth.

Executed for this report (all commands run from the `glosa` repo root, no kernel/schema/cli/design
files touched — writes confined to `sim/v0.3/`):

- `python3 sim/v0.3/combined.py` — new harness written for this task, printed the combined table
  reproduced in §4 and wrote `sim/v0.3/combined.json`.
- Read (not re-executed) the eight `sim/v0.3/prototypes/*.result.json` files, each of which
  itself records the exact command that produced it (e.g. `python3 sim/v0.3/prototypes/
  kernel_gate_rules_taxonomy_i_z.py`, `python3 sim/v0.3/prototypes/_eval_s7_9.py`) — those runs
  are the S4 prototype step that preceded this report step and are not re-run here, only read
  and cross-checked against `sim/v0.3/baseline.json`.
- Read `sim/v0.3/baseline.json` and `sim/v0.3/baseline.py` (the baseline generation script) and
  `sim/v0.3/gen_corpus.py` (the corpus generator) directly, to confirm how labels were assigned.

## 1. Corpus description and how labels were assigned

`sim/v0.3/corpus/` holds 180 claim_card / citation_card pairs, generated once by
`sim/v0.3/gen_corpus.py` from `schema/examples/claim_card.example.json` and
`schema/examples/citation_card.example.json`:

- **60 VALID cards** — legally varied tier / claim_type / genre / k_state / evidence-relation /
  responsibility-ownership combinations, each built to satisfy every kernel-checked rule. Each
  card's `disclaimers_emitted` block is filled in by calling the kernel's own
  `compute_disclaimers()` rather than hand-guessed, so a valid card is valid by construction, not
  by luck.
- **120 ADVERSARIAL cards** — 14 defect ids, 8 or 9 fixture cards per id (never two defects
  stacked on one card, so per-defect caught/missed counts are never confounded by a second
  violation): `hidden_ai_fill`, `inflated_bearing`, `missing_locator`, `composite_quote`,
  `k_state_rounded_up`, `stub_public`, `signature_missing`, `injected_infinity` (9 each);
  `verifiable_no_procedure`, `premature_category`, `tier_overclaim`, `disclaimer_missing`,
  `ownership_ai`, `same_vendor_review` (8 each).
- Ground truth lives in `sim/v0.3/corpus/labels.json` — `{cards: [{id, claim_file, citation_file,
  kind, defect|null, ...}]}` — written by the generator at construction time, not inferred after
  the fact.
- This report's four "task-brief" defects of interest (`composite_quote`, `hidden_ai_fill`,
  `inflated_bearing`, `injected_infinity`) are exactly the four `baseline.json` already reports
  as 0/9 caught — see §2.

**Limits of the labeling itself**, carried into §5: single generator, single date-stamp
(`GLOSA-CC-20260905-…`), one fixture family per defect (near-identical repeats of the same
injected string per id) — recall numbers below measure catching *this exact phrasing*, not
robustness to paraphrase.

## 2. Baseline table (kernel only, unmodified) — from `sim/v0.3/baseline.json`

Method: every card run through `k.validate_claim_card(card, citation_cards=[citation])`,
`k.validate_citation_card(citation)`, and `k.compute_disclaimers(card)` diffed against the card's
own declared `disclaimers_emitted`. "Caught" = kernel raised an error/warning on that card, or the
disclaimer-diff signal fired for the two defects designated that way
(`verifiable_no_procedure`→`D-DVP-NOT-K2`, `disclaimer_missing`→`D-INDEPENDENCE`).

| defect | n | caught | missed |
|---|---:|---:|---:|
| hidden_ai_fill | 9 | 0 | 9 |
| inflated_bearing | 9 | 0 | 9 |
| missing_locator | 9 | 9 | 0 |
| composite_quote | 9 | 0 | 9 |
| k_state_rounded_up | 9 | 9 | 0 |
| stub_public | 9 | 9 | 0 |
| signature_missing | 9 | 9 | 0 |
| injected_infinity | 9 | 0 | 9 |
| verifiable_no_procedure | 8 | 8 | 0 |
| premature_category | 8 | 8 | 0 |
| tier_overclaim | 8 | 8 | 0 |
| disclaimer_missing | 8 | 8 | 0 |
| ownership_ai | 8 | 8 | 0 |
| same_vendor_review | 8 | 8 | 0 |
| **TOTAL adversarial** | **120** | **84** | **36** |

- **recall = 84/120 = 0.700**
- **precision = 1.000** (flagged-true / (flagged-true + flagged-false); 0 false alarms below)
- **false_alarm = 0/60 valid cards → false_alarm rate = 0.000**

All 36 baseline-missed cards are exactly the four defects named in the K4 task brief:
`composite_quote`, `hidden_ai_fill`, `inflated_bearing`, `injected_infinity` (9 each). Every other
defect id is already 100% caught by the unmodified kernel on this corpus.

## 3. Per-prototype results

Eight prototypes were run in the prior S4 step (`sim/v0.3/prototypes/*.py`, each with its own
`*.result.json`). This section reads those results (not re-executed here) and states delta_recall
/ delta_false_alarm exactly as each file reports, plus the reason for its recommendation. All
deltas below are measured against `baseline.json`'s 120-adversarial / 60-valid corpus unless a
node explicitly scores against a different, smaller defect subset (noted per row) — see each
file's own `defects_targeted` field for what it actually claims to move.

| node | targeted defect(s) | delta_recall | delta_false_alarm | recommendation |
|---|---|---:|---:|---|
| `kernel.gate-rules-taxonomy-i-z` | `injected_infinity` (its own 9-card slice: 0/9→9/9) | **+1.0** (on its 9-card slice) | 0 | **ship** |
| `schema.claim-card-comparison-evidence-field` | `inflated_bearing` only, out of the 4-defect/36-card set it reports against | **+0.25** (9/36 → +9 caught) | 0 | **ship** |
| `cli.genre-router-layer-confusion-check` | all 4 (`composite_quote`, `hidden_ai_fill`, `inflated_bearing`, `injected_infinity`) | **+1.0** (0/36→36/36) | 0 | revise |
| `foundation.s7.9-intake-tier-flag` | all 4 (same set) | **+1.0** (0/36→36/36) | 0 (30/60 flat false-alarm rate is a *pre-existing* kernel warning unrelated to this prototype, verified separately at 0/60 prototype-only) | revise |
| `schema.verdict-class-vocabulary` | all 4 (same set) | **+1.0** (0/36→36/36) | 0 | revise |
| `kernel.pcs-red-flag` | semantic closure-timing red flag (not present in this corpus at all) | **0.0** (real corpus has zero fixtures of this concept) | 0 | revise |
| `kernel.unverified-verifiability-flag` | `verifiable_no_procedure` (already 8/8 via kernel's existing `D-DVP-NOT-K2`) | **0.0** | 0 | drop |
| `schema.prereg-gate-fields` | prereg timestamp/ethics-applicability sequencing (fields absent from all 180 cards) | **0.0** | 0.0 | drop |

**Why the three "all 4 defects, +1.0, revise" rows are not simply shipped:**

- `cli.genre-router-layer-confusion-check` — coverage is real on this corpus but each of its four
  layer-checks is a keyword/phrase match tuned to this corpus's own generator vocabulary. Its own
  notes record a failed first cut (an independence-register signal that produced 9 false alarms on
  valid cards before being narrowed) — a genuine finding, not swept under the rug, but exactly the
  kind of narrow-fit result that should not go straight to "ship" without a held-out phrasing test.
  It also substitutes the existing 180-card corpus for the DAG node's own named N=10 acceptance
  fixture rather than running that literal fixture — flagged as an open gap.
- `foundation.s7.9-intake-tier-flag` — same four detectors, same caveat (reverse-engineered from
  diffing 9 fixtures against 60 valid cards, not from the node's own literature-genre-appraisal
  proposal, which this corpus has no fixtures for); explicitly **not** an implementation of the
  DAG node's actual proposed mechanism (AACODS-style flag-and-request-tier layer with a
  Global-South evidence-genre exemption) — that needs its own fixtures.
- `schema.verdict-class-vocabulary` — same four detectors again, hand-curated from one exemplar
  fixture per defect class and verified over all fixtures + all valid cards with zero false hits,
  but each pattern is individually falsifiable by a counter-fixture the pattern would miss (e.g.
  English-only infinity language phrased outside the pattern list); the node's own literal
  acceptance_test (a schema enum accepting FORCED, rejecting a 7th value) was not run — this
  prototype probes the node's epistemic payoff instead.

These three overlap heavily in mechanism (bilingual keyword/marker regex over the same four
defect classes) and in limitation (same corpus, same narrow fixture family) — carrying all three
into the combined "ship" run would be triple-counting near-identical coverage against a
non-independent corpus. See §6 for the recommended next step on this cluster.

`kernel.pcs-red-flag` additionally ran the DAG node's own literal N=60/3-class synthetic
acceptance test independently of the real corpus and passed it exactly (flags only the intended
class, precision=recall=1.0 on that class) — a real, verified result, but on a same-lexicon
self-test, not on the shipped 180-card corpus, so it is reported as "revise" (needs an
out-of-lexicon holdout + independent adversarial review) rather than "ship" or "drop".

## 4. Combined ("if all ship") numbers

Ship set for this combined run = the two nodes recommended **ship** in §3:
`kernel.gate-rules-taxonomy-i-z` and `schema.claim-card-comparison-evidence-field`. Executed:
`python3 sim/v0.3/combined.py` (new harness written for this task; imports the kernel and the two
ship-recommended prototype modules unmodified, OR's their findings with the kernel's own
per-card verdict using `baseline.py`'s own `run_card`/`defect_caught` logic for the kernel half).
Output written to `sim/v0.3/combined.json`; console table reproduced verbatim:

| defect | n | caught | missed |
|---|---:|---:|---:|
| hidden_ai_fill | 9 | 0 | 9 |
| inflated_bearing | 9 | 9 | 0 |
| missing_locator | 9 | 9 | 0 |
| composite_quote | 9 | 0 | 9 |
| k_state_rounded_up | 9 | 9 | 0 |
| stub_public | 9 | 9 | 0 |
| signature_missing | 9 | 9 | 0 |
| injected_infinity | 9 | 9 | 0 |
| verifiable_no_procedure | 8 | 8 | 0 |
| premature_category | 8 | 8 | 0 |
| tier_overclaim | 8 | 8 | 0 |
| disclaimer_missing | 8 | 8 | 0 |
| ownership_ai | 8 | 8 | 0 |
| same_vendor_review | 8 | 8 | 0 |
| **TOTAL adversarial** | **120** | **102** | **18** |

- **baseline recall = 0.700 → combined recall = 0.850** (+0.150)
- **baseline false_alarm = 0/60 (0.000) → combined false_alarm = 0/60 (0.000)** (unchanged — both
  ship prototypes report, and this harness confirms, zero new false alarms on the 60 valid cards)
- Remaining misses after combining: `composite_quote` (9/9 missed) and `hidden_ai_fill` (9/9
  missed) — neither ship-recommended prototype targets these; they are covered (at +1.0 delta
  each) only by the three "revise" prototypes in §3, which this combined run deliberately excludes
  pending the follow-up in §6.

## 5. Limits (read before trusting any number above)

- **Synthetic corpus, single generator.** All 180 cards come from one generator
  (`sim/v0.3/gen_corpus.py`) run once on one date-stamp. Every "recall" and "false_alarm" number
  above is a readout of catching *this generator's exact phrasing* of each defect, not a
  population-level detection rate. Several prototype notes independently confirm this: a
  synthetic Thai-only probe with no English "verified" loanword defeats the kernel's existing
  regex today (`kernel.unverified-verifiability-flag`'s notes), and every keyword/marker-based
  prototype in §3 states outright that a differently-worded injection of the same defect class
  would likely evade it.
- **No real-world cards beyond the schema examples.** The two seed cards
  (`schema/examples/claim_card.example.json`, `citation_card.example.json`) are the only
  non-synthetic anchor; everything else is a generated variant of them.
- **Single-run, single-model construction.** Every prototype and this report were built and
  scored by the same agent in the same session — this is a maker's finite_diagnostic readout, not
  an independently checked one (`maker-checker-gate`: same-model self-check has no standing on
  its own).
- **Two nodes report zero real-corpus movement by construction, not by weak design**
  (`kernel.pcs-red-flag`, `schema.prereg-gate-fields`) — their target defect classes simply have
  no fixtures in this corpus. Their "drop"/"revise" status reflects that gap, not a demonstrated
  failure of the underlying mechanism.
- **Combined numbers in §4 cover only 2 of 8 evaluated nodes.** The three "revise" nodes that
  each independently close both remaining gaps (`composite_quote`, `hidden_ai_fill`) are excluded
  from §4 specifically because they are non-independent (same corpus, overlapping mechanism) —
  see §6.

## 6. DAG nodes this S4 pass supports shipping, revising, or dropping

- **ship**: `kernel.gate-rules-taxonomy-i-z`, `schema.claim-card-comparison-evidence-field`
- **revise**: `cli.genre-router-layer-confusion-check`, `foundation.s7.9-intake-tier-flag`,
  `schema.verdict-class-vocabulary`, `kernel.pcs-red-flag`
- **drop**: `kernel.unverified-verifiability-flag`, `schema.prereg-gate-fields`

Follow-up implied by this table, out of this task's own scope (sandbox-only, no kernel edits):
the three "revise" nodes overlap almost completely in what they catch (`composite_quote`,
`hidden_ai_fill`, `inflated_bearing`, `injected_infinity`, all via bilingual keyword/marker
matching). Before any of the three goes from "revise" to "ship", the recommended next step is
one held-out, differently-worded synthetic batch per defect (not built from any of the three
prototypes' own marker lists) to see which detector(s) actually generalize, rather than promoting
overlapping near-duplicates independently.
