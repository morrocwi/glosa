# glosa/schema — index, namespace, validation

**tier: Dr (specified; independently unreviewed).** This directory is the *only* place a glosa
field name is defined (one-fact-one-home, `FOUNDATION_v0.5.md` §8 / `REPO_SPEC_v0.5.md`'s
one-fact-one-home table: "A file in `schema/` states a rule's shape"). Every other file —
`methodology/`, `templates/`, `paper/`, `kernel/` — references these field names; none of them
may redeclare one. This README is itself Dr-tier, unreviewed prose, produced in the same pass as
the schemas it documents (Task B1).

## Namespace

Every `$id` uses the placeholder namespace `https://glosa.example/schema/<name>.schema.json`.
**`glosa.example` is not a real, resolvable domain.** The repo has no public remote yet
(`REPO_SPEC_v0.5.md`: local Forgejo only, no public GitHub as of this pass). The `$id` values exist
so `$ref` resolution has a stable base URI to resolve relative references against (see
"Cross-file `$ref`" below) — they are not meant to be dereferenced over the network, and the
kernel/validator never fetches them; `scripts/validate_glosa_schemas.py`-style tooling must always
resolve them from a local file store (see `README.md`'s own validation script below), never from
the network. When glosa gets a real public home, every `$id` in this directory should be updated
together, in one pass, to the real namespace — not incrementally, to avoid a mixed-namespace state
where some `$ref`s resolve and others don't.

## Cross-file `$ref` and `common.defs.json`

`common.defs.json` is **not** one of the 20 schemas this task named — it exists because all 20 of
them need the same handful of enums (`tier`, `independence_class`, `k_state`, `mc_level`,
`review_mode`, `fetch_status`, `citation_status`, `genre`, `venue_track`, `gate_verdict`,
`disclaimer_id`/`disclaimer_ref`, `bilingual_text`, ...), and JSON Schema draft-07 has no native
"import" — the only way to share a definition across files without hand-duplicating it (which
would itself be a one-fact-one-home violation, just at the schema layer instead of the
methodology/schema boundary) is a relative `$ref` resolved by a `RefResolver` with a `store` keyed
by `$id`. Every schema file's own `$id` is its resolution base, so `"common.defs.json#/definitions/tier"`
inside `claim_card.schema.json` resolves to `https://glosa.example/schema/common.defs.json#/definitions/tier`.
`claim_card.schema.json`'s `five_questions.tested.evidence_relations[]` items also `$ref`
`evidence_relation.schema.json` directly, rather than redeclaring that shape inline — this is the
one-fact-one-home discipline applied *within* `schema/` itself, not only between `schema/` and the
rest of the repo.

**Consequence for anyone validating these files:** a bare `jsonschema.validate(instance, schema)`
call, or `Draft7Validator(schema).validate(instance)` with no resolver, will throw a
`RefResolutionError` the moment it hits `"common.defs.json#/..."` or `"evidence_relation.schema.json"`,
because it has no way to find those files. You must build a `store` mapping every schema's `$id` to
its loaded JSON and pass a `RefResolver(base_uri=schema["$id"], referrer=schema, store=store)` to
the validator. See "How to validate" below for the exact pattern (and the actual script this task
ran, at the path named there).

## The 21 schemas, one line each

| Schema | FOUNDATION_v0.5.md section | Notes |
|---|---|---|
| `claim_card.schema.json` | §3 (whole section) | The canonical schema. Two legal shapes (`stub`\|`full`, §3.2a). Carries the largest share of schema-enforced kernel rules (see table below). Also carries two OPTIONAL top-level blocks added per founder instruction 2026-09-04 (BBL-2026-09-04-083/084, FOUNDATION_v0.5.md §2.1b): `responsibility` (`data_to_inference: human\|ai\|joint`, `inference_to_claim` const `"human"`, kernel rule 15 — see fail fixture table below) and `empirical_extension` (`operationalization[]`, `study_design`, `bias_register[]`, `robustness`; kernel rule16w warns when absent on an `EMPIRICAL` claim). schema_version 0.8.0 (this pass, `design/SESSION_ARCH_v0.4_SPEC.md` §10): additive optional `five_questions.tested.defeater_class` (rule30) and `provenance_dag.defeater_log[]` now `required: [node, date, outcome]` with an `outcome` enum (rule `lrs.defeater-defeated-status-field`). |
| `evidence_relation.schema.json` | §3.2 `five_questions.tested.evidence_relations[]` | Standalone so `claim_card` can `$ref` it (one-fact-one-home) and so review/DVP tooling can validate one evidence relation in isolation. |
| `review_report.schema.json` | §4.3, §7.3 (Bounded-Judge Law) | `verdict_tier` required, six values (chair ruling C4). Field renamed `independence_level` → `independence_class` to match chair ruling C1's "one string ladder, every schema." |
| `citation_card.schema.json` | §7.8 | Integrity Firewall's two independently-flaggable booleans. `status` uses FOUNDATION's newer six-value enum, not the broader draft enum in `templates/knowledge/citation_card.yaml`. |
| `blackbox_note.schema.json` | §2.3, §2.4 | Renamed from the design-era `r0_record.schema.json` (chair ruling A1). Additive/optional `session_id`, `session_boundary` (`ai_state_at_boundary` literal `"reset"`), `entry_anchor` — `design/SESSION_ARCH_v0.4_SPEC.md` §2.1/§2.2 (SA-1), pending founder ratification of §2.2's logical-join decision. Also additive/optional top-level `question_trace[]` (per-turn question-evolution trace inside ONE note, `schema.blackbox-question-trace`, `design/SESSION_ARCH_v0.4_SPEC.md` §9.1/§9.4) — coverage-checked by `tools/blackbox_log.py`'s `question_trace_coverage()`/`check-note` (distinct from that same file's own Blackbox LOG entries.jsonl functionality). |
| `problem_card.schema.json` | §2.2 stage S1 | The two-question intake gate. This is the object `REPO_SPEC_v0.5.md` calls `intake.schema.json` — filed under `problem_card` per this task's naming. Additive/optional `intake.precommitted_resistance_route` (`design/SESSION_ARCH_v0.4_SPEC.md` §2.1/§2.2, D-NO-PRECOMMIT-ROUTE flag, never a hard block). |
| `readiness_report.schema.json` | §9 (`validate_readiness`) | General pre-work project-readiness self-check — distinct from `problem_card.readiness`, which is S1's own narrower gate. |
| `release_manifest.schema.json` | §7.4 | PUB-ADVERSARIAL-REVIEW's seven dimensions (R1–R7) plus the mandatory Blackbox Note appendix precondition. Additive/optional `human_mastery_gate_ref` (methodology/P10_publish_gate.md R8, `hu.mastery-gate-wired`) — absence is a `kernel.gate_release` WARNING (`NO_MASTERY_GATE_LINKED`), never a hard schema fail, pending founder ratification. |
| `route_dependence_matrix.schema.json` | §4.3 | DVP mechanics — makes route correlation visible, never zeroes it out. |
| `disagreement_ledger_entry.schema.json` | §4.3, §8.1 | Resolve-or-Declare, per-project home + merged view (chair ruling B6). |
| `kg_node.schema.json` | §8.1 | Graph-view pointer only; canonical content lives at `ref`. |
| `kg_edge.schema.json` | §8.1 | `derives_from` vs `borrows` kept deliberately non-collapsible. Additive/optional `session_id` (`design/SESSION_ARCH_v0.4_SPEC.md` §2.2/§8) backs `chi_recip_diagnostic` (`kernel/glosa_kernel.py`, `Open`-tier, never a verdict). |
| `equation_registry_row.schema.json` | §8.1 | Registered once, at first use; Buckingham-trap guard. |
| `conversion_plan.schema.json` | §7.7 | Project Advisor output. `tier` is fixed `"Dr"`. |
| `search_log.schema.json` | S8 template + S14 §12 | Field renamed `review_mode` → **`search_mode`** (this task's explicit instruction), resolving the name collision `S14_literature-review-system.md` §12 open-question-1 flagged against §7.8's `review_mode`. |
| `source_acquisition_log.schema.json` | S14 | Public-repo-safe by construction — never a local path/Zotero key. |
| `litreview_manifest.schema.json` | S14 | Frozen per LRS run; two separate gates (`accuracy_gate`, `diversity_gate`). |
| `hypothesis_selection.schema.json` | S14, HANDOFF 35d | Human-only selection among candidate hypotheses; AI may propose, never select. Additive/optional `session_id`, `chooser_reaffirmations[]`, `retained_direction` (default `unknown`, NC-77), `direction_evidence_relation` — `design/SESSION_ARCH_v0.4_SPEC.md` §2.1/§4. |
| `dialogue_table_row.schema.json` | S14, `templates/knowledge/dialogue_table.md` | One row per source; a stance may only be recorded once `claim_match_verified`. Additive/optional `defeater_class` + `legitimate_defeater` (`lrs.dialogue-table-claim-type-column`, `design/SESSION_ARCH_v0.4_SPEC.md` §10.1) — deliberately schema-optional, not `required`; the stance-without-defeater-columns check is a `cli/glosa` lint (`rows_incomplete_defeater`), not a hard schema gate. |
| `neighbour_table_row.schema.json` | `design/S13_neighbour-table.md`, chair ruling A2 | `relation: adopted_from` requires an authorization pointer (never AI-inferred). |
| `human_mastery_gate.schema.json` | §7.5 (`methodology/P17_human_mastery_gate.md`) | `hu.mastery-gate-wired` (HU-1, `design/SESSION_ARCH_v0.4_SPEC.md` §11.1, build_now). Genre-independent form of the ten-question live unaided-defense checklist already inline in `templates/paper/arxiv-twocol/main.tex:375-378`. Every answer is human-authored only, never `ai_filled` — any `ai_filled` disclosure forces `gate_status: NOT_READY` (schema allOf). Feeds `methodology/P10_publish_gate.md`'s new R8 via `release_manifest.human_mastery_gate_ref`. |

Plus `common.defs.json` (not one of the 21; shared definitions — see above).

## Examples

`schema/examples/<name>.example.json` — one valid instance per schema (21 files). The
`claim_card`, `problem_card`, and `blackbox_note` examples form one linked worked example around
the founder's own cat question ("ทำไมแมวเยี่ยวไม่เป็นที่"), cross-referencing each other by id
(`BB-2026-09-04-01` → `GLOSA-PC-20260904-0001` → `GLOSA-CC-20260904-0001`) exactly as the spine
(§2.1) describes. The other 18 examples build out the same worked example's downstream artifacts
(a citation card, a review report, a route-dependence matrix, a lit-review manifest, a Human
Mastery Gate, ...) so the whole example set is one coherent case rather than 21 unrelated
fragments. Two schemas needed a
source that is not the household's own Blackbox Note (`source_acquisition_log`,
`neighbour_table_row`); those use an explicitly labeled `SYNTHETIC`/placeholder identifier
(`cite-example-ext-001`, `https://example.org/synthetic-example-source`) rather than inventing a
realistic-looking fake citation.

`schema/examples/fail/*.json` — sixteen deliberate-FAIL fixtures, each a `claim_card`- or (rule26
only) `citation_card`-shaped instance that is schema-valid everywhere **except** the one violation
named in its own `_fail_reason` field (a documentation-only field the validation script strips
before validating — it is not part of the schema). Each is built by minimally mutating the valid
`claim_card.example.json` (or, for rule26, `citation_card.example.json`), so a diff against that
file shows exactly what was changed to trigger the failure. `scripts/validate_examples.py` and
`kernel/glosa_kernel.py`'s own `self_test()` route each fixture by shape: a `"shape"` key routes
through `validate_claim_card`, an `"identifier"`+`"claim_ref"` pair (no `"shape"`) routes through
`validate_citation_card` (corrected 2026-09-05 — previously every non-`"shape"` fixture fell
through to `claim_card.schema.json` regardless of its actual object type, which happened to still
reject a citation_card-shaped instance, but for the wrong reason: missing claim_card-required
fields, not the rule the fixture actually names). The nine pre-existing fixtures cover §3.3 rules
1/2/4/9/10/15/(§5 D-INDEPENDENCE) and rule17 (source-first citation); the seven new fixtures below
(this pass, `design/FOUNDATION_v0.6_PATCH.md`) cover rules 18/19/20/23/26/27/28 (see the Rule
numbering table further down — rules 21/22/24/25 have no dedicated fail-fixture file: 21 is a
warning, never a hard fail, so it cannot be represented as a FAIL fixture, and 22/24/25 are
pending-founder, not built this pass):

| Fixture | Violates | §3.3 rule |
|---|---|---|
| `fail_same_model_review.json` | `independent_check.status: PASSED` with `independence_class: I1` | rule 1 (MC-02) |
| `fail_no_independent_check.json` | `k_state: K1` with no I3+ evidence, no bounded-exception markers | rule 9 |
| `fail_missing_disclaimer.json` | strongest evidence is I2 (no I3+) but `D-INDEPENDENCE` absent | §5 catalogue, schema-approximated |
| `fail_th_coqc_no_witness.json` | `tier: Th_coqc` with only an I3 (cross-vendor AI) witness, no I4/I5 | rule 2 |
| `fail_stub_public.json` | `shape: stub` with `status: Approved-for-Live` (past Draft) | rule 10 |
| `fail_k2_without_i5.json` | `k_state: K2` with only an I4 witness, no I5 | rule 4 |
| `fail_ai_signs_claim.json` | `responsibility.inference_to_claim: "ai"` instead of the required `"human"` | task-scoped kernel rule 15, §2.1b (founder instruction 2026-09-04, BBL-2026-09-04-083/084) — also fails the schema's own `const: "human"` on the same field, so this fixture is rejected at both layers |
| `fail_rule18_injected_infinity.json` | `hypothesis_world.text` asserts an actual +infinity (I4) as a reached value | rule18 (TAXONOMY-UNTYPED, kernel-only, `design/FOUNDATION_v0.6_PATCH.md` §1) |
| `fail_rule19_gate_type_unstated.json` | `gate_construction_status.type: "Type-P"` with `failing_control_ref: null` | rule19 (GATE-TYPE-UNSTATED, kernel-only, §1) |
| `fail_rule20_priority_word_rejected.json` | `comparison.basis` contains the word "first" | rule20 (forbidden-word-list rejection, schema-enforced, §2) |
| `fail_rule23_verdict_class_unlisted.json` | `verdict_class: "UNLISTED_SEVENTH_VALUE"`, a seventh value outside the six-value enum | rule23 (VERDICT-CLASS-UNLISTED, schema-enforced, §5) |
| `fail_rule26_composite_quote.json` (citation_card-shaped) | `exact_passage` splices across a boundary via an ellipsis marker | rule26 (COMPOSITE-QUOTE, kernel-only, K-C1) |
| `fail_rule27_hidden_ai_fill.json` | `seen.ai_assisted_fields` names a field, but every `ai_filled` value is a placeholder | rule27 (HIDDEN-AI-FILL, kernel-only, K-C2) |
| `fail_rule28_inflated_bearing.json` | `evidence_relations[0]` bearing=SUPPORTS, own-lineage notes, `strength` not "context" | rule28 (INFLATED-BEARING, kernel-only, K-C3) |
| `fail_rule29_strength_of_claim_defeater.json` | `tested.falsifier` reads "feel intuitively solid" (strength-of-claim, not a defeater) | rule29 (DEFEATER-NOT-COLLAPSE, kernel-only, `design/SESSION_ARCH_v0.4_SPEC.md` §10.3) |
| `fail_rule30_defeater_class_mismatch.json` | `defeater_class: EMPIRICAL` paired with a PHENOMENOLOGICAL-style (absence/misdescription) `falsifier` | rule30 (CLAIM-TYPE-DEFEATER-ENUM, kernel-only, §10.4) |
| `fail_nc77_retained_direction_unforced.json` (hypothesis_selection-shaped) | `retained_direction: expansion` declared on a `chosen` row spanning 2 sessions with no `direction_evidence_relation` | NC-77 (kernel-only, `validate_hypothesis_selection`, `methodology/data/non_collapse_table.json`) |
| `fail_session_boundary_not_reset.json` (blackbox_note-shaped) | `session_boundary.ai_state_at_boundary: "manual_continue"` — not the literal `"reset"` | unnumbered session-boundary rule, schema-enforced within one note; the cross-note case is `check_session_boundary_reset` (kernel-only), exercised in `tests/test_kernel.py`, not a fixture file |

## How to validate

Requires `jsonschema==3.2.0` (the version this task was told to target; the schemas use only
draft-07 features — `if`/`then`/`else`, `contains`, `const`, `additionalProperties` — that 3.2.0
supports in full). Bare `jsonschema.validate()` will NOT work (see "Cross-file `$ref`" above) — you
need a `RefResolver` backed by a `store` of every schema's `$id`:

```python
import json
from pathlib import Path
from jsonschema import Draft7Validator, RefResolver

ROOT = Path("schema")  # this directory
store = {}
for p in list(ROOT.glob("*.schema.json")) + [ROOT / "common.defs.json"]:
    schema = json.loads(p.read_text())
    store[schema["$id"]] = schema

def validator_for(schema_filename):
    schema = store[f"https://glosa.example/schema/{schema_filename}"]
    resolver = RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    return Draft7Validator(schema, resolver=resolver)

instance = json.loads((ROOT / "examples/claim_card.example.json").read_text())
validator_for("claim_card.schema.json").validate(instance)  # raises on failure
```

This exact pattern (plus a meta-schema self-check on every `*.schema.json` file, and an
expect-to-fail pass over `examples/fail/*.json`) is what this task ran to confirm: **all 20 valid
examples PASS their schema; all 6 fail fixtures are correctly REJECTED; all 21 schema files
(20 + `common.defs.json`) are themselves valid draft-07 schemas.** Re-run it after any schema edit.

## Schema-enforced vs kernel-enforced — FOUNDATION_v0.5.md §3.3's 11 rules

**Pure JSON Schema cannot express every cross-field kernel rule** (this is stated as a known limit
in `FOUNDATION_v0.5.md` §3.3's own heading rationale and in the task that produced this
directory). Draft-07's `if`/`then`/`contains` can express a surprising amount of it, but not all of
it — three specific kinds of check are permanently out of reach: (a) **comparing two property
values against each other** (JSON Schema can check a property against a literal/enum, not against
another property's actual value — no `<=` between two strings, no "these three fields must differ
pairwise"); (b) **date/duration arithmetic** (e.g. "expires_at is within 90 days of date" — draft-07
has no date-diff operator); (c) **free-text semantic scanning** (e.g. "does this prose propose
external validation as a legitimacy lever" — a lexical regex would both over- and under-match, so
this is left to the kernel's actual text-processing code, not faked here as a brittle pattern
match). Rows below are honest about which side of that line each of the 11 rules falls on.

| # | Rule (§3.3) | Schema-enforced? | Where / how | What the schema CANNOT check |
|---|---|---|---|---|
| 1 | `independent_check.status == PASSED` requires `independence_class ∉ {I0,I1}` | **Yes, fully** | `claim_card.schema.json` allOf, "Kernel rule 1" | — |
| 2 | `tier: Th_coqc` requires ≥1 evidence_relation at I4 or I5 | **Yes, fully** | allOf, "Kernel rule 2" (uses `contains`) | — |
| 3 | `tier: finite_diagnostic` requires ≥1 evidence_relation at I4/I5 (I3 alone insufficient) | **Yes, presence check** | allOf, "Kernel rule 3" | That the I4/I5 route actually supplied a reproduction command/retrievable original (a content-quality judgment, not a shape check) |
| 4 | `k_state ∈ {K2,K3}` requires ≥1 evidence_relation at I5 | **Yes, for the plain rule; NO for the bounded exception's arithmetic** | allOf, "Kernel rule 4" | The rule's full text also allows a "formal/empirical constraint" alternate path not reduced to a checkable predicate in FOUNDATION itself — left as prose, not schema-enforced |
| 5 | `maker_id`, `checker_id`, `approver_id` pairwise distinct once status advances past Pending Review (MC-01) | **No — kernel-only** | n/a | JSON Schema cannot compare two properties' *values* against each other for inequality; this needs actual code (`kernel/glosa_kernel.py`'s `validate_claim_card`) |
| 6 | `scope.claim_scope` may not exceed `scope.evidence_scope` | **No — kernel-only** | n/a | Same class of limit as rule 5 — a string-containment/human-reviewed comparison between two property values, not expressible via `enum`/`const`/`pattern` alone |
| 7 | `silent_lift_check.flags` non-empty is a hard failure blocking status advancement | **Yes, approximated** | allOf, "Kernel rule 7" — reads as "status stays Draft while any flag is open" | The rule's exact meaning ("blocks advancement", not "resets to Draft") is a simplification for schema purposes; a real advancement state machine belongs in the kernel |
| 8 | Contaminated-concept text scan fires `EXTERNAL_VALIDATION_PROPOSED` as a hard fail | **No — kernel-only** | n/a | Free-text semantic scanning (see (c) above) — deliberately not faked with a brittle regex here |
| 9 | `k_state: K1` requires ≥1 evidence_relation at I3+, OR the bounded I2+I4 exception (D-SAME-VENDOR + non-null `expires_at`) | **Yes, approximated** | allOf, "Kernel rule 9" (anyOf) | The exception's actual 90-day arithmetic (`expires_at ≤ 90 days from date`) — schema only checks `expires_at` is present, not that it is within range; that is kernel-only date math |
| 10 | `shape: stub` cards fail status advancement past Draft | **Yes, fully** | allOf, "shape:stub legal-shape rule" | — |
| 11 | `provenance_dag.status` and `silent_lift_check.status` must both be `run` before `k_state` advances past K0 | **Yes, fully** | allOf, "Kernel rule 11" | — |

**Net: 6 of 11 rules are fully schema-enforced (1, 2, 10, 11, and the plain halves of 4 and 9's
main clause), 2 are enforced as a presence-only approximation (3, 7) that cannot verify content
quality, 1 is enforced except for date arithmetic (9's exception clause), and 3 are permanently
kernel-only (5, 6, 8).** This split is not a shortcut taken to save time — it is the actual
expressive ceiling of JSON Schema draft-07 against a rule set that includes cross-property
comparisons, date arithmetic, and free-text semantics; `kernel/glosa_kernel.py`'s
`validate_claim_card` (named in FOUNDATION §9, not yet built — this task is schema-only) is where
rules 5, 6, 8, and the two arithmetic gaps must actually be checked before any of this is treated
as enforced in practice. Every field in `disclaimers_emitted`/`independent_check`/etc. that the
schema lets through unchecked is still `Dr`-tier by the repo-wide default (`kernel not yet
built ⇒ tier: Dr` + `D-CANDIDATE-STATUS`, FOUNDATION §9) — passing this schema is necessary, never
sufficient, for a claim card to be trustworthy.

One additional disclaimer-catalogue row (`D-INDEPENDENCE`, "tested's strongest entry is I0–I2") is
also schema-approximated in `claim_card.schema.json`'s allOf as a worked example of how a
disclaimer trigger COULD be schema-checked; the other ~35 rows of `methodology/data/
disclaimer_catalogue.json`'s full catalogue (§5) are not individually re-implemented here — that
full compute is `compute_disclaimers()`'s job (FOUNDATION §9), kernel-side, reading the catalogue's
actual trigger conditions rather than having them re-typed once per row into every schema file.


## Rule numbering, rules 12–28 (`design/FOUNDATION_v0.6_PATCH.md`'s own numbering table)

Rules 1–11 above are FOUNDATION_v0.5.md §3.3's original numbered list. Rule 12 (D-LENS-UNSIGNED /
D-LENS-UNCITED) ships in the kernel (`_lens_unsigned_error` / `_lens_uncited_error`). Rules 13–28
below either predate this task (13/14, spec-only; 15–17, kernel-shipped ahead of FOUNDATION's own
prose) or are this task's own K6-kernel additions (18–28, `design/FOUNDATION_v0.6_PATCH.md`).

| # | Rule | Status | Where |
|---|---|---|---|
| 13–14 | `tested.evidence_relations[].channel` (Bridge Burden) / `bearing: CHALLENGES` | **spec-only** — stated in FOUNDATION §3.3 prose, no kernel/schema implementation on disk this pass (`grep -n "channel\|CHALLENGES" kernel/glosa_kernel.py` finds no rule-13/14 implementation) | FOUNDATION_v0.5.md §3.3 rules 13/14 |
| 15 | `responsibility.inference_to_claim` must be `"human"` (hard error); `rule15w` warns when `responsibility` is absent | **shipped in kernel**, not yet folded into FOUNDATION §3.3's numbered prose | `kernel/glosa_kernel.py` `_responsibility_error_for_card` / `_responsibility_warning_for_card` |
| 16 | `rule16w`: EMPIRICAL claim without `empirical_extension` (warning) | **shipped in kernel** | `kernel/glosa_kernel.py` `_empirical_extension_warning_for_card` |
| 17 | Source-first citation (`rule17`/`rule17w`) | **shipped in kernel** | `kernel/glosa_kernel.py` `_citation_source_first_errors` |
| 18 | Injected-infinity/zero I1–I4/Z1–Z4 taxonomy scan (`TAXONOMY-UNTYPED`), ported from `sim/v0.3/prototypes/kernel_gate_rules_taxonomy_i_z.py`, kc-base-016 codes verbatim — its own standalone kernel text-scan rule, NOT rule 8's `EXTERNAL_VALIDATION_PROPOSED` family | **shipped in kernel** | `kernel/glosa_kernel.py` `_scan_for_injected_infinity_zero`, `claim_card.schema.json`'s additive `gate_fail_taxonomy` field |
| 19 | Fail-Able Gate Law (Type-P requires a cited machine-derived failing control; absent that, stays Type-U), kc-base-008 verbatim | **shipped in kernel** | `kernel/glosa_kernel.py` `_gate_construction_status_error`, `claim_card.schema.json`'s additive `gate_construction_status` field |
| 20 | `comparison.basis`/`relation` schema-rejects the forbidden-word-list terms (see scripts/check_forbidden_words.sh), English + Thai (`ใหม่`/`ครั้งแรก`/`ดีที่สุด`/`เหนือกว่า`) | **shipped, fully schema-enforced** (no kernel code needed) | `claim_card.schema.json`'s additive `comparison` field |
| 21 | Genre/register layer-mismatch diagnostic (warning, never auto-corrected) — HONEST LIMIT: keyword-calibrated against one corpus's own vocabulary, `finite_diagnostic` scoped to what was actually run, not a general detection-rate claim | **shipped in kernel, warning-only** | `kernel/glosa_kernel.py` `_layer_mismatch_warning` |
| 22 | `citations[].intake_tier` / `intake_tier_reason` / `global_south_exempt` (INTAKE-TIER-UNTIERED) | **pending-founder** (`thin-layer-scope-confirmation`) — NOT built this pass | TODO(foundation.s7.9-intake-tier-flag) in `schema/litreview_manifest.schema.json`'s `$comment` |
| 23 | `verdict_class` six-value enum (`DERIVED\|FORCED\|DEFINITIONAL-RELABEL\|POSITED\|BORROWED-SCALE\|OPEN`) | **shipped, fully schema-enforced** (no kernel code needed, parallels rule 1/2/10/11) | `claim_card.schema.json`'s additive `verdict_class` field |
| 24 | Premature Category Stabilization (PCS), joint closure-timing + absence-of-adaptation | **pending-founder** (`PCS-scoping-confirmation`) — NOT built this pass | TODO(kernel.pcs-red-flag) in `methodology/data/disclaimer_catalogue.json`'s `_meta._todo_pending_founder`, and in `kernel/glosa_kernel.py`'s `validate_claim_card` body |
| 25 | `discovery_routing{used, candidate_questions, k_epi_gate_log}` (DISCOVERY-CANDIDATE-UNGATED) | **pending-founder** (`discovery-routing-stage-adoption`) — NOT built this pass | TODO(foundation.lrs-discovery-loop-extension) in `schema/litreview_manifest.schema.json`'s `$comment` |
| 26 | Composite-quote detector: `citation_card.exact_passage` may not splice across a boundary via an ellipsis/`" -- "` marker | **shipped in kernel** (structural check on the field's own shape, no lexicon-fragility risk) | `kernel/glosa_kernel.py` `_composite_quote_error`, wired into `validate_citation_card` |
| 27 | Hidden-AI-fill detector: `five_questions.seen.ai_assisted_fields` vs `five_questions.ai_filled` contradiction | **shipped in kernel** | `kernel/glosa_kernel.py` `_hidden_ai_fill_error`, `claim_card.schema.json`'s additive `seen.ai_assisted_fields` field |
| 28 | Inflated-bearing detector: a `bearing: SUPPORTS` evidence_relation without `strength: "context"`, unresolvable/disqualified citation, or same-lineage notes | **shipped in kernel** (the resolvability half is only checked when `citation_cards` is supplied — a warning discloses the gap otherwise, same convention as D-LENS-UNCITED) | `kernel/glosa_kernel.py` `_inflated_bearing_errors`, wired into `validate_claim_card` |
| 29 | `kernel/glosa_kernel.py` rule29 (`lrs.defeater-not-collapse-rule`, `design/SESSION_ARCH_v0.4_SPEC.md` §10.3): a `tested.falsifier` matching strength-of-claim/feels-solid phrasing is never itself a legitimate defeater, regardless of `claim_type`. NOTE: this is a **different, non-colliding sibling** number from `design/FOUNDATION_v0.6.md` §3.3's own prose "flag-rule29" (`kernel.candidate-set-delta-cooking-step`) — always write out `kernel.glosa_kernel.rule29` vs. `FOUNDATION_v0.6.md §3.3 flag-rule29` per SESSION_ARCH_v0.4_SPEC.md §10's own disambiguation note | **shipped in kernel** (tier `Dr`, evadable-by-omission phrase-list guard — the spec's suggested `methodology/data/non_defeater_phrase_table.json` home is not in this task's ownership list, so the pattern is kept inline instead; rule statement/failing control unchanged) | `kernel/glosa_kernel.py` `_rule29_non_defeater_error`, wired into `validate_claim_card` |
| 30 | `five_questions.tested.defeater_class` (additive optional, sibling of `claim_type`) must be paired with a `falsifier` phrasing style matching that class (`lrs.claim-type-defeater-enum`, §10.4) | **shipped in kernel**, EMPIRICAL<->PHENOMENOLOGICAL pairing only this pass — the other three classes' own phrasing styles are an open dependency per §10.4's own disclosure | `kernel/glosa_kernel.py` `_rule30_defeater_class_error`, `claim_card.schema.json`'s additive `five_questions.tested.defeater_class` field |
| 31 | `lrs.defeater-defeated-status-field` (§10.2) tested-status warning: `defeater_status` (`untested\|tested_survived\|tested_defeated`) is DERIVED from `provenance_dag.defeater_log[]`, never a second stored field (§10.2 already named a new top-level status field the "already-refuted idea" its own real fix — `defeater_log` required `[node,date,outcome]` — deliberately did not add). WARNING (never a hard fail) once `status` is Pending Review or beyond with `defeater_log` empty | **shipped in kernel, warning-only** (like rule 21, this has no fail-fixture file — a warning cannot be represented as a schema-level FAIL) | `kernel/glosa_kernel.py` `defeater_status_for_card`, `_rule31_defeater_status_warning` |

Every rule 18–28 row above traces to `design/FOUNDATION_v0.6_PATCH.md`; rules 22/24/25 are
deliberately unbuilt (pending-founder) — their TODO comments name the exact node id a future pass
must resolve before building them, per this task's own instruction not to guess a founder ruling.
Rules 29/30/31 trace to `design/SESSION_ARCH_v0.4_SPEC.md` §10.2/§10.3/§10.4 instead.

## NC-77 (Retention ≠ Direction) and the session-architecture fields — `design/SESSION_ARCH_v0.4_SPEC.md`

- **NC-77** (Family J, `methodology/data/non_collapse_table.json`): persistence/retention of a
  chosen hypothesis across ≥2 sessions is never by itself evidence of expansion vs. tunnel; only a
  linked independent-check artifact may set the sign. Schema default `retained_direction: unknown`
  on `schema/hypothesis_selection.schema.json`; kernel-enforced by `_retained_direction_error` /
  `validate_hypothesis_selection` (`kernel/glosa_kernel.py`). Disclaimer `D-RETENTION-DIRECTION`
  (documentation-only, `methodology/data/disclaimer_catalogue.json`).
- **`session_id` / `session_boundary` / `entry_anchor`** (`schema/blackbox_note.schema.json`,
  additive/optional): the session-boundary + AI-reset fact (SA-1). `ai_state_at_boundary` is
  schema-restricted to the literal `"reset"`; the cross-note agreement across a shared
  `session_id` is kernel-checked (`check_session_boundary_reset`), not schema-checked.
- **`intake.precommitted_resistance_route`** (`schema/problem_card.schema.json`, additive/
  optional): the R* resistance-precommit fact. Absence at `READY_FOR_S2` raises the
  `D-NO-PRECOMMIT-ROUTE` flag (`validate_problem_card`) — a warning, never a hard block.
- **`chi_recip_diagnostic`** (`kernel/glosa_kernel.py`, over `schema/kg_edge.schema.json`'s new
  `session_id` field): an `Open`-tier finite diagnostic, never a verdict — returns
  `{"not_computable": True, ...}` (never a numeric default) when `session_id` is absent.
- The Session object itself (§2.1) is a **logical join** across these four artifacts, not a new
  `session.yaml` file (§2.2's one-fact-one-home decision) — **pending founder ratification**
  (§7 item 1 of the spec); the fields above implement that recommended default, not a founder
  ruling already made. Likewise `hypothesis_selection.schema.json`'s `session_id` field wires
  SA-2's own session-grouping key as the recommended default (§7 item 7), also pending founder
  ratification.

## Remaining `design/SESSION_ARCH_v0.4_SPEC.md` `build_now` nodes closed this pass

- **`schema.blackbox-question-trace`** — `schema/blackbox_note.schema.json`'s additive/optional
  top-level `question_trace[]` (`{n, ts, question_text, derived_from_line, note}`), coverage-checked
  by `tools/blackbox_log.py`'s `question_trace_coverage()` / `blackbox_log.py check-note <path>`.
- **`lrs.defeater-defeated-status-field`** — `provenance_dag.defeater_log[]` `required: [node,
  date, outcome]` with an `outcome` enum was already shipped; this pass adds kernel rule31 (a
  DERIVED `defeater_status` warning, see the rule table above) on top of it, without a duplicate
  schema field.
- **`lrs.dialogue-table-claim-type-column`** — `dialogue_table_row.schema.json`'s additive/optional
  `defeater_class` + `legitimate_defeater`, matching the already-shipped `templates/knowledge/
  dialogue_table.md` columns and `cli/glosa`'s `_dialogue_row_incomplete` lint.
- **`hu.mastery-gate-wired`** (HU-1) — new `schema/human_mastery_gate.schema.json` +
  `kernel.validate_human_mastery_gate`/`mastery_gate_r8_status`, `methodology/P10_publish_gate.md`
  R8, `release_manifest.schema.json`'s additive `human_mastery_gate_ref` (absence is a
  `gate_release` WARNING, never a hard fail — pending founder ratification, per
  `methodology/P17_human_mastery_gate.md`), and the `design/FOUNDATION_v0.6.md` §7.5 broken-pointer
  fix.
- **Verified, not re-fixed:** `NC-77` (`methodology/data/non_collapse_table.json`),
  `D-RETENTION-DIRECTION`, `D-NO-PRECOMMIT-ROUTE` (`methodology/data/disclaimer_catalogue.json`)
  each already exist exactly once in the repo, no duplicates across either data file.
