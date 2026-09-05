# K4-report — glosa tests/sim prototype evaluation

Tier of every number in this report: **finite_diagnostic** — an exact tally over one fixed,
printed 180-card synthetic corpus, this run, these files as they exist on disk today. Not a
general claim about kernel or prototype quality on any other corpus, on real-world claim cards,
or on differently-worded injections of the same defects. Readout, not truth.

Executed for this report (all commands run from the `glosa` repo root, no kernel/schema/cli/design
files touched — writes confined to `tests/sim/`):

- `python3 tests/sim/combined.py` — new harness written for this task, printed the combined table
  reproduced in §4 and wrote `tests/sim/combined.json`.
- Read (not re-executed) the eight `tests/sim/prototypes/*.result.json` files, each of which
  itself records the exact command that produced it (e.g. `python3 tests/sim/prototypes/
  kernel_gate_rules_taxonomy_i_z.py`, `python3 tests/sim/prototypes/_eval_s7_9.py`) — those runs
  are the S4 prototype step that preceded this report step and are not re-run here, only read
  and cross-checked against `tests/sim/baseline.json`.
- Read `tests/sim/baseline.json` and `tests/sim/baseline.py` (the baseline generation script) and
  `tests/sim/gen_corpus.py` (the corpus generator) directly, to confirm how labels were assigned.

## 1. Corpus description and how labels were assigned

`tests/sim/corpus/` holds 180 claim_card / citation_card pairs, generated once by
`tests/sim/gen_corpus.py` from `schema/examples/claim_card.example.json` and
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
- Ground truth lives in `tests/sim/corpus/labels.json` — `{cards: [{id, claim_file, citation_file,
  kind, defect|null, ...}]}` — written by the generator at construction time, not inferred after
  the fact.
- This report's four "task-brief" defects of interest (`composite_quote`, `hidden_ai_fill`,
  `inflated_bearing`, `injected_infinity`) are exactly the four `baseline.json` already reports
  as 0/9 caught — see §2.

**Limits of the labeling itself**, carried into §5: single generator, single date-stamp
(`GLOSA-CC-20260905-…`), one fixture family per defect (near-identical repeats of the same
injected string per id) — recall numbers below measure catching *this exact phrasing*, not
robustness to paraphrase.

## 2. Baseline table (kernel only, unmodified) — from `tests/sim/baseline.json`

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

Eight prototypes were run in the prior S4 step (`tests/sim/prototypes/*.py`, each with its own
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
`python3 tests/sim/combined.py` (new harness written for this task; imports the kernel and the two
ship-recommended prototype modules unmodified, OR's their findings with the kernel's own
per-card verdict using `baseline.py`'s own `run_card`/`defect_caught` logic for the kernel half).
Output written to `tests/sim/combined.json`; console table reproduced verbatim:

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
  (`tests/sim/gen_corpus.py`) run once on one date-stamp. Every "recall" and "false_alarm" number
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

---

## v0.4 — SESSION_ARCH_v0.4_SPEC.md §5 defect classes + S4b hidden_ai_fill fix

Tier of every number below: **finite_diagnostic** for the main 180-card corpus counts (an exact
tally over `tests/sim/corpus/`, this run), **Dr** for the five new session-architecture defect
classes (see §v0.4.3 below — measured by a sim-local prototype checker, not the shipped
kernel/schema). Readout, not truth.

### v0.4.1 — S4b fix: `hidden_ai_fill` now actually exercises rule27

Prior to this pass, `tests/sim/gen_corpus.py`'s `hidden_ai_fill` injector wrote AI-drafted prose
into `five_questions.seen.access_model` but never populated
`five_questions.seen.ai_assisted_fields` — the structural marker
`kernel/glosa_kernel.py:881` (`_hidden_ai_fill_error`, kernel rule27, K-C2) actually reads. Rule27
is a **marker-vs-marker** check (`ai_assisted_fields` naming a field vs. `ai_filled` disclosing
it), not a prose scan, so with no marker set the rule structurally could not fire — the card
validated clean regardless of the hidden AI-drafted content. This was an S4b gap: the corpus
*labelled* a card `hidden_ai_fill` and *expected* it to be a meaningful adversarial fixture, but
the one field the kernel's own rule27 inspects was never set, so the label and the mechanism were
never actually connected.

Fix, this pass: `hidden_ai_fill` now sets `seen.ai_assisted_fields: ["access_model"]` alongside
the AI-drafted `access_model` text, while `ai_filled.retained_record_route` stays a not-applicable
placeholder — the exact contradiction rule27 is built to catch. Re-running `baseline.py`:

| defect | n | caught | missed | (before this pass) |
|---|---|---|---|---|
| `hidden_ai_fill` | 8 | **8** | 0 | 0/8 caught (rule27 never exercised) |

The old marker-less injection is **kept**, not deleted, as its own separate labelled class
`hidden_ai_fill_unmarked` (8 fixtures) — so the real, still-open gap ("a hidden AI fill with zero
self-disclosed marker at all slips past rule27, by design of what a structural marker check can
see") stays visible in the corpus rather than being silently erased by fixing the other variant:

| defect | n | caught | missed |
|---|---|---|---|
| `hidden_ai_fill_unmarked` | 8 | 0 | **8** (expected — rule27 has no marker to read; not a bug, disclosed as a scan-scope limit, `finite_diagnostic`) |

Total corpus size is unchanged at the valid/adversarial split (60 valid, still 15 defect ids ×
8 fixtures = 120 adversarial, 180 total) since `hidden_ai_fill_unmarked` was added by re-purposing
one defect id's worth of fixtures, not by growing the corpus. Overall v0.3-corpus recall this run:
**112/120 = 0.933**, valid-corpus false alarms: **0/60** — no regression on any of the other 13
v0.3 defect classes (`tests/test_sim_regression.py::test_sim_corpus_recall_and_false_alarms_do_not_regress`
compares this run's recall against the freshly-regenerated `tests/sim/baseline.json` and passes).

### v0.4.2 — corpus regeneration commands run for this pass

```
python3 tests/sim/gen_corpus.py     # regenerates tests/sim/corpus/ (180 cards) AND
                                     # tests/sim/corpus/v04/ (60 fixtures, see v0.4.3)
python3 tests/sim/baseline.py       # re-runs the CURRENT kernel over both corpora, writes
                                     # tests/sim/baseline.json + tests/sim/baseline_v04.json
python3 -m pytest -q tests          # 183 passed, 1 skipped (kernel-import skip guard, unrelated)
```

### v0.4.3 — five new session-architecture defect classes (design/SESSION_ARCH_v0.4_SPEC.md §5)

These five classes target artifacts §5's own proposals name — `hypothesis_selection.yaml` rows,
`blackbox_note` pairs sharing a `session_id`, a session's Problem Card sequence, and free
prose/code — none of which are `claim_card`/`citation_card` shapes, so they live in a **separate**
corpus tree, `tests/sim/corpus/v04/{hsel,blackbox,session,momentum}/`, with its own
`tests/sim/corpus/v04/labels.json` (one-fact-one-home: a different artifact shape is a different
corpus, not more rows squeezed into the existing `claim_card` labels list).

**TODO(schema.retention-direction-field, SA-1, kernel.reciprocal-lineage-diagnostic, SA-3):**
confirmed by direct grep of `schema/*.json` and `kernel/glosa_kernel.py` (2026-09-05) — none of
`hypothesis_selection.schema.json`'s `retained_direction`/`chooser_reaffirmations[]`,
`blackbox_note.schema.json`'s `ai_state_at_boundary`, or any session-level
`chi_recip`/question-drift validator exist yet. These are the four still-open v0.4 schema/kernel
proposals landing in parallel with this sim task (per §3's `build_now` rows). Because the real
mechanism does not exist yet, "caught" below is measured by a **sim-local prototype reference
checker** in `tests/sim/baseline.py` (`_check_*_v04` functions, one per class) — a hand-written
reading of each proposal's own `failing_control` clause from §5/§4, tier **Dr**, explicitly *not*
a claim about the shipped kernel or schema's behaviour. `tests/test_sim_regression.py::
test_v04_prototype_checkers_match_fixture_labels` asserts these prototype checkers agree with
their own fixtures' declared kind (adversarial → flagged, valid → not flagged) — a
self-consistency test of the sim's own prototype, never a kernel regression claim. Once each
proposal's real schema/kernel change ships, `main_v04()`/this test should be repointed at the real
`kernel.glosa_kernel`/`jsonschema` call and this TODO removed.

Per-class fixture counts and this run's prototype-checker readout (6 adversarial + 6 valid
controls per class, `tests/sim/baseline.py`'s `main_v04()`, written to `tests/sim/baseline_v04.json`):

| defect class | source proposal | n_adv | caught | missed | n_valid | false_alarm |
|---|---|---|---|---|---|---|
| `tunnel_unflagged` | `schema.retention-direction-field`, SA-2 | 6 | 6 | 0 | 6 | 0 |
| `retention_undeclared` | SA-1 | 6 | 6 | 0 | 6 | 0 |
| `chooser_forgotten` | `schema.retention-direction-field` (`chooser_reaffirmations[]`) | 6 | 6 | 0 | 6 | 0 |
| `question_drift_unlogged` | SA-3 (`question_trace[]`) | 6 | 6 | 0 | 6 | 0 |
| `momentum_overclaimed` | `kernel.reciprocal-lineage-diagnostic`, SA-4 | 6 | 6 | 0 | 6 | 0 |

Prototype-checker recall across all five classes this run: **30/30 = 1.000** (n_adv=30),
false-alarm total: **0/30** valid controls. Reiterated: this is a readout of the **prototype**,
not the kernel — it says the fixtures and the spec-reading prototype are mutually consistent, not
that glosa's shipped software catches these five defect classes today. It does not catch, and is
not built to catch: a hidden violation of any of these five rules that does not match the
specific field-shapes this generator constructed (e.g. a `retained_direction` overclaim expressed
in free prose rather than the structured field, or a `momentum_overclaimed` sentence phrased
outside this checker's gate/warrant keyword list — the same evadable-by-omission caveat rule27/28
already carry, disclosed here rather than hidden).

**Fixture sketch per class** (mirrors §5's own table):

- `tunnel_unflagged` — `hypothesis_selection`-shaped rows, `selection_status: chosen` spanning
  `session_ids` across ≥2 sessions, no `evidence_relation` resolving to an independent-check
  verdict → adversarial fixtures bare-assert `retained_direction: expansion|tunnel`; valid
  controls either default to `retained_direction: unknown` or carry an `evidence_relation` whose
  `resolves_to_checker_verdict: true` supplies the sign instead.
- `retention_undeclared` — pairs of Blackbox-Note stubs sharing one `session_id` across a
  `process_restart_after: true` boundary; adversarial fixtures leave one side's
  `ai_state_at_boundary` missing or not the literal `"reset"`; valid controls have both sides
  correctly `"reset"`, or use different `session_id` values (rule does not apply).
- `chooser_forgotten` — `hypothesis_selection`-shaped rows with `reopened_in_session` set;
  adversarial fixtures carry an empty `chooser_reaffirmations: []`; valid controls carry a
  reaffirmation entry naming that same reopening session, or were never reopened at all.
- `question_drift_unlogged` — a session record with `declared_q1_issue` plus
  `problem_cards_opened[]`; adversarial fixtures have a card whose `q1_issue` diverges from the
  declared one with `new_problem_card_opened_for_drift: false`; valid controls either show no
  divergence or set that flag `true`.
- `momentum_overclaimed` — free-text doc/code snippets; adversarial fixtures read
  `chi_recip`/`m^H`/`m^AI`/momentum language as a release gate, warrant, proof, or certification;
  valid controls state the same terms as an Open-tier diagnostic, explicitly disclaiming
  gate/warrant/certification status (the prototype checker is negation-aware at the sentence
  level, per its own `_NEGATION_NEAR_RE` — matched, e.g., against "not a release gate").

### v0.4.4 — what this pass did NOT do (disclosed gaps, not silently dropped)

- Did not touch `kernel/`, `schema/`, or `design/` — per this task's ownership boundary, the four
  schema/kernel proposals these five fixture classes target are a different worker's scope; this
  pass only builds the sim fixtures + a disclosed prototype reference checker.
- `main_v04()`'s and `test_v04_prototype_checkers_match_fixture_labels`'s numbers must be
  **re-read, not reused**, once `schema.retention-direction-field`, `SA-1`,
  `kernel.reciprocal-lineage-diagnostic`, and `SA-3` land — that re-run (against the real
  kernel/schema, not the prototype) is the "again in integrate" pass named in this task.
- Did not add the eleven separate `lrs-defeaters`/`human-uplift` fixture classes from §12
  (`question_trace_gap`, `candidate_forgotten_unrecorded`, `chooser_reaffirmation_missing`,
  `candidate_set_drop_unexplained`, `dialogue_table_stance_without_defeater`,
  `defeater_log_untyped_entry`, `strength_of_claim_defeater`, `defeater_class_style_mismatch`,
  `mastery_gate_unlinked`, `entry_anchor_change_condition_missing`,
  `completeness_prompt_outside_bounded_set`) — this task named exactly five classes by id
  (`tunnel_unflagged`, `retention_undeclared`, `chooser_forgotten`, `question_drift_unlogged`,
  `momentum_overclaimed`), which match §5's table verbatim, not §12's; §12's eleven are a distinct,
  larger fixture set (several targeting `dialogue_table.md`/`claim_card.provenance_dag`/
  `human_mastery_gate.yaml`, artifacts this task's ownership list does not cover) left for a
  separate task rather than folded in here under an approximate name match.
