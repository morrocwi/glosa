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

## The 20 schemas, one line each

| Schema | FOUNDATION_v0.5.md section | Notes |
|---|---|---|
| `claim_card.schema.json` | §3 (whole section) | The canonical schema. Two legal shapes (`stub`\|`full`, §3.2a). Carries the largest share of schema-enforced kernel rules (see table below). Also carries two OPTIONAL top-level blocks added per founder instruction 2026-09-04 (BBL-2026-09-04-083/084, FOUNDATION_v0.5.md §2.1b): `responsibility` (`data_to_inference: human\|ai\|joint`, `inference_to_claim` const `"human"`, kernel rule 15 — see fail fixture table below) and `empirical_extension` (`operationalization[]`, `study_design`, `bias_register[]`, `robustness`; kernel rule16w warns when absent on an `EMPIRICAL` claim). |
| `evidence_relation.schema.json` | §3.2 `five_questions.tested.evidence_relations[]` | Standalone so `claim_card` can `$ref` it (one-fact-one-home) and so review/DVP tooling can validate one evidence relation in isolation. |
| `review_report.schema.json` | §4.3, §7.3 (Bounded-Judge Law) | `verdict_tier` required, six values (chair ruling C4). Field renamed `independence_level` → `independence_class` to match chair ruling C1's "one string ladder, every schema." |
| `citation_card.schema.json` | §7.8 | Integrity Firewall's two independently-flaggable booleans. `status` uses FOUNDATION's newer six-value enum, not the broader draft enum in `templates/knowledge/citation_card.yaml`. |
| `blackbox_note.schema.json` | §2.3, §2.4 | Renamed from the design-era `r0_record.schema.json` (chair ruling A1). |
| `problem_card.schema.json` | §2.2 stage S1 | The two-question intake gate. This is the object `REPO_SPEC_v0.5.md` calls `intake.schema.json` — filed under `problem_card` per this task's naming. |
| `readiness_report.schema.json` | §9 (`validate_readiness`) | General pre-work project-readiness self-check — distinct from `problem_card.readiness`, which is S1's own narrower gate. |
| `release_manifest.schema.json` | §7.4 | PUB-ADVERSARIAL-REVIEW's seven dimensions (R1–R7) plus the mandatory Blackbox Note appendix precondition. |
| `route_dependence_matrix.schema.json` | §4.3 | DVP mechanics — makes route correlation visible, never zeroes it out. |
| `disagreement_ledger_entry.schema.json` | §4.3, §8.1 | Resolve-or-Declare, per-project home + merged view (chair ruling B6). |
| `kg_node.schema.json` | §8.1 | Graph-view pointer only; canonical content lives at `ref`. |
| `kg_edge.schema.json` | §8.1 | `derives_from` vs `borrows` kept deliberately non-collapsible. |
| `equation_registry_row.schema.json` | §8.1 | Registered once, at first use; Buckingham-trap guard. |
| `conversion_plan.schema.json` | §7.7 | Project Advisor output. `tier` is fixed `"Dr"`. |
| `search_log.schema.json` | S8 template + S14 §12 | Field renamed `review_mode` → **`search_mode`** (this task's explicit instruction), resolving the name collision `S14_literature-review-system.md` §12 open-question-1 flagged against §7.8's `review_mode`. |
| `source_acquisition_log.schema.json` | S14 | Public-repo-safe by construction — never a local path/Zotero key. |
| `litreview_manifest.schema.json` | S14 | Frozen per LRS run; two separate gates (`accuracy_gate`, `diversity_gate`). |
| `hypothesis_selection.schema.json` | S14, HANDOFF 35d | Human-only selection among candidate hypotheses; AI may propose, never select. |
| `dialogue_table_row.schema.json` | S14, `templates/knowledge/dialogue_table.md` | One row per source; a stance may only be recorded once `claim_match_verified`. |
| `neighbour_table_row.schema.json` | `design/S13_neighbour-table.md`, chair ruling A2 | `relation: adopted_from` requires an authorization pointer (never AI-inferred). |

Plus `common.defs.json` (not one of the 20; shared definitions — see above).

## Examples

`schema/examples/<name>.example.json` — one valid instance per schema (20 files). The
`claim_card`, `problem_card`, and `blackbox_note` examples form one linked worked example around
the founder's own cat question ("ทำไมแมวเยี่ยวไม่เป็นที่"), cross-referencing each other by id
(`BB-2026-09-04-01` → `GLOSA-PC-20260904-0001` → `GLOSA-CC-20260904-0001`) exactly as the spine
(§2.1) describes. The other 17 examples build out the same worked example's downstream artifacts
(a citation card, a review report, a route-dependence matrix, a lit-review manifest, ...) so the
whole example set is one coherent case rather than 20 unrelated fragments. Two schemas needed a
source that is not the household's own Blackbox Note (`source_acquisition_log`,
`neighbour_table_row`); those use an explicitly labeled `SYNTHETIC`/placeholder identifier
(`cite-example-ext-001`, `https://example.org/synthetic-example-source`) rather than inventing a
realistic-looking fake citation.

`schema/examples/fail/*.json` — six deliberate-FAIL fixtures, each a `claim_card`-shaped instance
that is schema-valid everywhere **except** the one violation named in its own `_fail_reason` field
(a documentation-only field the validation script strips before validating — it is not part of the
schema). Each is built by minimally mutating the valid `claim_card.example.json`, so a diff against
that file shows exactly what was changed to trigger the failure:

| Fixture | Violates | §3.3 rule |
|---|---|---|
| `fail_same_model_review.json` | `independent_check.status: PASSED` with `independence_class: I1` | rule 1 (MC-02) |
| `fail_no_independent_check.json` | `k_state: K1` with no I3+ evidence, no bounded-exception markers | rule 9 |
| `fail_missing_disclaimer.json` | strongest evidence is I2 (no I3+) but `D-INDEPENDENCE` absent | §5 catalogue, schema-approximated |
| `fail_th_coqc_no_witness.json` | `tier: Th_coqc` with only an I3 (cross-vendor AI) witness, no I4/I5 | rule 2 |
| `fail_stub_public.json` | `shape: stub` with `status: Approved-for-Live` (past Draft) | rule 10 |
| `fail_k2_without_i5.json` | `k_state: K2` with only an I4 witness, no I5 | rule 4 |
| `fail_ai_signs_claim.json` | `responsibility.inference_to_claim: "ai"` instead of the required `"human"` | task-scoped kernel rule 15, §2.1b (founder instruction 2026-09-04, BBL-2026-09-04-083/084) — also fails the schema's own `const: "human"` on the same field, so this fixture is rejected at both layers |

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
