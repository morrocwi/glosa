# Resistance Ladder + Reproduction Ledger — design v0.1

Status: specification for implementation (S1–S4 below). Authority: founder ruling
`BBL-2026-09-07-229` (Toledo overnight handoff, "Resistance ladder + Reproduction Ledger",
`toledo/ops/HANDOFF_OVERNIGHT_2026-09-06.md`'s 2026-09-08 entry). This document is the field-by-field
reference for `methodology/P22_reproduction_ledger.md`, `methodology/P23_resistance_ladder.md`,
`schema/reproduction_card.schema.json`, the `glosa repro` / `glosa score` CLI verbs, RET-Check v0.3,
and Toledo's per-entry `resistance` block — the way `toledo/registry/SCHEMA.md` is the reference for
`CANONICAL.json`. Narrated against `glosa/methodology/P19_registration.md` (registration homes),
`P20_core_epistemic_structure.md` (who ran a check), `P21_ret_check.md` and
`cases/ret/PREREGISTRATION_v0_1.md` (the provenance auditor this ladder feeds), `P10_publish_gate.md`
(R1–R8), and *The Recursive Epistemic Tunnel* v2.1 §27–31 (Historical Invariance, the AI-Independent
Consequence Requirement RET-N16, AI-Off World-Closure RET-N17/N18, RET-N19, and Appendix E's Minimal
AOWC Checklist) for the AOWC definitions this ladder's R6 rung operationalizes.

Readout-not-truth applies to this document itself: every Toledo code, statement, and count quoted
below (§7) was read directly from `toledo/registry/genesis_root.json` and `toledo/registry/CANONICAL.json`
by a command run while drafting this file (a small `python3 -c` script counting `tier_in_genesis`
matches and grepping numeric literals in `statement` text), not carried over from memory or from
the handoff's own prose. One correction made while writing this spec: the handoff's closing line
("IDM into Toledo... ultracode") reads as if IDM Toledo codes might already exist; a direct listing of
`toledo/registry/proposals/` found no IDM file at drafting time — Card 3 below is written honestly as
PENDING, not as if codes already existed.

tier: Dr (specified from the founder ruling and the cited sources; independently unreviewed).

---

## 0. Design principle (restated, binding)

> The score is a SET of rungs held, each with an evidence pointer — never a single number that hides
> a missing rung. Readout-not-truth. A rung is held only by a file that exists (Coq report,
> reproduction card, review report).

Three consequences that shape every section below:

1. **No aggregation.** `glosa score <artifact>` and Toledo's `resistance` block never emit a scalar
   (no "7/10", no percentage). They emit a per-rung `{rung, held, evidence[], reason}` row. A reader
   who wants a single number is refused one, on purpose — a missing R4 must never be laundered into
   "mostly resistant."
2. **A rung is held by evidence, not by assertion.** Every `held: true` cites a file that exists on
   disk (or a `repo_anchor` pointing at one in another repo, at a commit) — a Coq `.v` file +
   `verify_report.json`, a `reproduction_card` JSON file, a `review_report.yaml` file. No rung is ever
   marked held because a prose paragraph claims it.
3. **Failing a rung's check does not un-hold the rung below it, and does not fail the artifact.**
   R4 "held" means *an oracle comparison happened with a tolerance declared before the run* — PASS or
   FAIL both hold R4 (§7 Card 1's `EQ-068` is the paradigm case: it FAILED against PDG and that FAIL
   is exactly what makes R4/R6 non-tautological evidence of real world-side resistance, not proof the
   claim is true). Tier fidelity (`P10` R3) is a separate axis from rung-holding.

---

## 1. The Resistance Ladder R0–R6

| Rung | Held by (what must exist) | Evidence file type | What it does **NOT** certify |
|---|---|---|---|
| **R0 — Stated** | The claim/entry has a written statement at all. | The claim card / Toledo entry's own `statement` field. | Nothing beyond "this was written down." Every entry in Toledo holds R0 trivially — its only job is to make explicit that a bare stated equation carries **zero** resistance by itself, so a reader never mistakes "coded" for "checked." |
| **R1 — Pre-registered falsifier / claim boundary** | A falsifier or a `reproduction_card.preregistered_prediction` was written **before** the run/observation it constrains, with a `declared_at` timestamp. | `claim_card.five_questions.tested.falsifier` (non-TODO, non-empty) *or* a linked `reproduction_card` whose `preregistered_prediction.declared_at` predates its own `run.date`. | That the falsifier is a *good* one, or that anyone has actually tried to defeat the claim yet — only that a boundary was drawn before evidence could shape it (`P21`'s own "declare pass/fail before writing the code" discipline, generalized). |
| **R2 — Coq-closed (kernel outside our loop)** | A machine-checked proof whose kernel is not part of the AI/human authoring loop — Coq's own kernel accepted the term. | `coq/canonical/<code>.v` + a `verify_report.json`/`verify.sh` line reading exactly `"Closed under the global context"` for at least one Theorem/Lemma/Corollary in that file (`toledo/registry/SCHEMA.md`'s `coq_status == "closed"`). | Empirical truth of the statement — Coq closure certifies internal consistency of a finite formal model, never that the model matches the world (`glosa/methodology/P19`'s own disclaimer, restated). `definition` / `wrapped_related` / `mapped_not_wrapped` / `open_prop` / `not_formalisable` / `axioms` / `root_layer_unwired` `coq_status` values do **not** hold R2 — only `closed` does (the v1.1 honest reclassification this repo already went through). |
| **R3 — Reproducible run, hash-frozen, AI = 0** | A `reproduction_card` with a filled `run{}` block: a declared `command`, `input_hash`/`output_hash` (SHA-256 of the declared input/output files), `ai_at_runtime: 0`, and a `date` — independently re-executable. | The `reproduction_card` JSON file itself, plus (once run) a `glosa repro verify` re-execution matching the recorded hashes. | That the run's *result* matched anything — R3 is about the run being pinned and re-runnable at all, before any comparison. A card can hold R3 with `result.status: FAIL` or even `ERROR`. |
| **R4 — External oracle** | The same card's `oracle` names a `published_value`, `independent_implementation`, or `public_dataset`, with `version`/`doi_or_url` pinned, and `result` was computed against `preregistered_prediction.tolerance`. | The `reproduction_card` file (its `oracle{}` + `result{}` blocks). | That the result was a PASS. `EQ-068` (§7 Card 1) holds R4 with a disclosed FAIL — the oracle comparison itself, honestly run, is what R4 certifies. |
| **R5 — Independent reviewer or interactional-expert record** | A `review_report.yaml` at independence class **I2 or above** (`P6`'s ladder), or a documented interactional-expert reading (`P20`'s `X_p^int`, non-`None`), naming the artifact/code. | `review_report.yaml` (`reviewer_identity` distinct from `maker_id`/`approver_id`, `independence_class ≥ I2`). | That the review reached a favorable verdict — a `HostileReviewer`/`Falsifier` role report with a FAIL verdict still holds R5; the rung is about an independent human/route having looked, not about what they concluded. |
| **R6 — AOWC world record** | A `reproduction_card` of external-oracle kind (`published_value` / `independent_implementation` / `public_dataset`) additionally satisfying the AOWC gate conditions (RET-N18, Tunnel v2.1 §30): frozen before the run, `ai_at_runtime: 0` for both execution *and* evaluation, and a tolerance declared such that the test **could genuinely count against the claim** (not a vacuous always-pass band). | The same `reproduction_card` file, marked in `notes` (or inferable from a non-trivial tolerance) as AOWC-qualifying, cross-referenced against Appendix E's Minimal AOWC Checklist (12 items, Tunnel v2.1). | That the outcome not producible by the recursion loop was *desired* — RET-N18's own final condition is "T is allowed to count against H"; a card engineered so it can only ever confirm the claim never holds R6, however many times it is re-run. |

R0–R2 are checkable from Toledo's own files alone (statement text, `coq_status`). R3–R6 require a
Reproduction Card (§2) or a review report; R6 additionally requires the card to pass the AOWC gate
check (§8, `glosa score`'s own logic — not a new schema field, see §2's note).

**Machine-side vs. world-side, kept explicitly separate (founder's own phrase in the ruling).** R2 is
resistance from a kernel *outside our authoring loop* but still a formal, not a world, check. R3–R6
are resistance whose oracle sits, to varying degrees, *outside the recursive human–AI dialogue
network* RET-Check audits (§5). A card whose `oracle.kind == "coq_kernel"` is Coq resistance
double-counted under a different name — §5 is explicit that such a card feeds `glosa score`'s R2 row
directly and is **never** converted into a RET-Check provenance row, so R2's machine-side count and
RET's `N_P^ind` world/reviewer-side count never blend into one number.

---

## 2. The Reproduction Card (`schema/reproduction_card.schema.json`, methodology home `P22`)

One JSON Schema draft-07 file, `additionalProperties: true`, styled like `review_report.schema.json`
and `core_epistemic_structure.schema.json` (both read directly while drafting this section). Required
top level: `id`, `toledo_codes`, `claim`, `preregistered_prediction`, `oracle`, `environment`, `run`,
`result`, `lineage`.

| Field | Shape | Notes |
|---|---|---|
| `id` | string, e.g. `REPRO-2026-09-08-0001` | Same numbering convention as `GLOSA-CC-<date>-<nnnn>` elsewhere in this CLI. |
| `toledo_codes` | `array<string>` | Toledo codes this card backs (`P19` order: the equation must already be registered in Toledo before a card cites it). **May be empty** only when `status: "pending_toledo_code"` is also set (Card 3, §7) — never populated by inventing a code. |
| `claim` | string | Free text, or a `claim_card.claim_id` reference. What is being tested. |
| `preregistered_prediction` | `{statement, tolerance, declared_at}` | Written **before** `run`/`result` exist (`glosa repro new` enforces this by writing the file with `run: null` and refusing any later edit to this block once `run` is filled — the same "do not retune after seeing output" discipline `cases/ret/PREREGISTRATION_v0_1.md` states for the RET RISK formula, generalized to every reproduction card). `tolerance` is a string, not a number, because it must be human-readable and exact ("±5% of the PDG value", "0 digit mismatch to 50 decimal places") — the runner parses it mechanically per `oracle.kind`, never re-interprets it loosely. |
| `oracle` | `{kind, source, doi_or_url, version}` | `kind ∈ {published_value, independent_implementation, public_dataset, coq_kernel, human_review}`. `source` names the thing (e.g. "Particle Data Group, Review of Particle Physics"); `doi_or_url` and `version` are pinned once known — `null` only pre-run, never left `null` once `result` is filled for an external-oracle kind (R4 requires the pin). |
| `environment` | `{python, packages}` | `python`: the pinned interpreter version string used for `run.command`. `packages`: `{name: version}`, **empty for the runner process itself** (stdlib only, matching `ret_check.py`'s own "no third-party import" self-test) — a non-empty entry here names a package used **only inside the card's own declared oracle computation** (e.g. `{"mpmath": "1.3.0"}` for Card 3, §7), run in a separate, declared subprocess/venv, never imported by `scripts/repro_check.py`'s own driver. `numpy`/`mpmath` are the two named exceptions per the task's own constraint; anything else is a schema violation for this repository's cards. |
| `run` | `{command, input_hash, output_hash, ai_at_runtime, date}` | `ai_at_runtime` is **always the literal `0`** — not a free integer; a card asserting anything else is not a Reproduction Card under this scheme (the founder's own "AI = 0 at runtime" phrase, reused verbatim from `P21`). `input_hash`/`output_hash`: SHA-256 of the declared input/output file(s), computed by the runner, never typed by hand. |
| `result` | `{status, observed, deviation}` | `status ∈ {PASS, FAIL, ERROR, PENDING}`. `PENDING` is the only legal value before `run` exists — a freshly-scaffolded card is `PENDING`, matching the "None is itself epistemic information" convention `P20` already uses for `X_p^int`. |
| `lineage` | `{run_by, ces}` | `run_by`: identity string. `ces`: `$ref: core_epistemic_structure.schema.json` (`P20`'s three roles — respondent / interactional / ai_models) scoped to *who ran this specific reproduction*, not the whole paper it may support — one-fact-one-home: the paper's own CES block is a separate, paper-level fact. |
| `notes` | string | Free text; carries the AOWC-qualification note for R6 (§1) and any retrospective-formalisation disclosure (§7 Card 1 is a retrospective card over an already-disclosed Genesis finding, not a fresh blind prediction — that distinction is stated here, never silently blurred). |

**Why `oracle.kind` has exactly five values and no "none".** A card that only wants R3 (a bare,
re-runnable, hash-frozen computation with no comparison target) still declares an `oracle` — pick the
kind that best names what the run's output is being checked against even when the comparison is
trivial or internal; a genuinely oracle-free run is out of scope for this schema and belongs in the
project's own test suite, not the Reproduction Ledger. This keeps every card in the Ledger doing the
one job the founder asked for: showing which *external* resistance step was exercised, never merely
"the script ran."

**Toledo mapping is a citation, never a copy (`P19`/`P0` one-fact-one-home).** A card that names a
Toledo code is not duplicated into Toledo; Toledo's `resistance` block (§6) cites it by
`{repo: "glosa", commit, path, id}` the same way `origin.repo_anchor` already cites external repos.
Correction (2026-09-08 — this section originally specified a `glosa repro run --register-toledo`
flag; it was never implemented in `cli/glosa`, confirmed live, and Toledo's own `registry/
SCHEMA.md` addendum already documents the mechanism actually built): the citation row is produced
Toledo-side, not glosa-side. Toledo's own `scripts/register_reproduction_evidence.py
[--glosa-repo PATH]` reads glosa's `cases/repro/*.json` cards and `reviews/routes/**/
review_report.{yaml,json}` files directly and regenerates `registry/reproduction_card_index.json`
(and `registry/review_report_index.json`) wholesale — a small, git-tracked index Toledo's own
`scripts/compute_resistance.py` reads; not itself the card's home of record. glosa exposes no flag
or command that writes into that Toledo file.

---

## 3. CLI contracts (`cli/glosa`, methodology home `P22`/`P23`)

Five new verbs, dispatched the same way every existing `glosa <noun> <verb>` pair is (see `cli/glosa`'s
`cmd_*` functions) — `_log()`'d to `logbook.jsonl`, self-checked against the schema on write, never
silently swallowing a bad file.

```
glosa repro new    --id <ID> --claim "<text>" --toledo-codes <code[,code...]>
                    --oracle-kind <kind> --oracle-source "<text>"
                    [--doi-or-url <url>] [--version <v>]
                    --statement "<text>" --tolerance "<text>"
                    --human-owner <id> [--out-dir <dir>]
```
Scaffolds `cases/repro/<ID>.json` (or `--out-dir`), `preregistered_prediction.declared_at = now`,
`run: null`, `result: {"status": "PENDING"}`. **Refuses** (exit 1, no file written) if `--statement`
or `--tolerance` is empty — the pre-registration must exist before any run, the same fail-closed shape
`glosa session close --retention-note` already uses for a different mandatory human-authored field.

```
glosa repro run    <path> [--command "<cmd>"] [--input <file>...] [--output <file>...]
```
Loads the card; refuses if `preregistered_prediction.declared_at` is missing, or if `run` is already
filled (a filled card is immutable — re-checking it is `repro verify`'s job, never an overwrite of
`run`, mirroring `session_close`'s "already closed" refusal). Executes `command` via `subprocess` in
the runner's own stdlib-only process (§2's `environment.packages` note — a card whose oracle needs
`mpmath`/`numpy` spawns *that* computation as a separately declared subprocess, never imported into
this driver), SHA-256-hashes every declared `--input`/`--output` file, fills `run{}`, parses the
command's own stdout/the hashed output against `preregistered_prediction.tolerance` per `oracle.kind`'s
comparison rule, and writes `result{status, observed, deviation}` back to the same file.

```
glosa repro verify <path> [--reviewer-identity <id>]
```
Maker ≠ checker (`P10` NC-28/29): a **different** identity re-executes `run.command` fresh in a clean
temp directory, recomputes the hashes, and confirms they equal the ones already recorded — on match,
scaffolds a `review_report.yaml` (`role: SourceAuditor`, verdict quoting the hash match) rather than
mutating the card itself. This is the file that actually **holds** R3 for a reader other than the
maker; `repro run`'s own first execution is necessary but not sufficient.

```
glosa repro to-ret <path> --claim <claim-id> [--out <case.json>]
```
Emits or appends one RET-Check provenance row per §5's mapping. **Refuses** with an explanatory
message for `oracle.kind == "coq_kernel"` — that resistance is machine-side (R2), never converted into
a RET-Check world/reviewer-side row (§1's "never blend into one number" rule, enforced here
mechanically, not just documented).

```
glosa score <artifact>
```
`<artifact>` = a Toledo code (`--kind toledo-code`), a `claim_card` path, or a `release_manifest`
path (auto-detected the same way `glosa check` infers a schema stem). Scans, in order: Toledo's own
`coq_status` (R2, if a Toledo code was given or is reachable from the claim card); every
`cases/repro/*.json` reproduction card whose `toledo_codes[]`/`claim` matches (R1/R3/R4/R6, per §1's
rules); every `reviews/routes/**/review_report.yaml` naming the artifact (R5). Prints the **R0–R6
table** from §1 with `held`/`evidence`/`reason` filled per artifact — `--json` for the structured form
(the same flag every other `glosa` verb already carries). Never prints, computes, or accepts a
`--score` flag that would collapse the table to one number — that is the one thing this command is
built to refuse.

---

## 4. RET-Check v0.3 (`P21`, `scripts/ret_check.py`)

v0.2 (current) computes `N_A`/`N_P`/`N_P^ind`/cycle/interruption from hand-authored provenance rows.
v0.3 adds exactly one capability: **a converter from Reproduction Cards into provenance rows**
(`glosa repro to-ret`, §3) — the RET RISK formula itself is **unchanged** (`cases/ret/
PREREGISTRATION_v0_1.md`'s own standing rule: never retune the formula to make a case pass; v0.2's
correction note is the precedent for how a v0.3 change must be documented — a dated addendum, no
scenario's expected output moves).

**Mapping (the "external oracle = external interruption" rule stated plainly):**

| Card shape | Emitted row | `record_type` | `root_independent` |
|---|---|---|---|
| `oracle.kind ∈ {published_value, independent_implementation, public_dataset}` | one row, `agent = card.id`, `parent = "-"`, `source_root = oracle.source` (+`version`) | `world_record` | `true` (the oracle is, by construction, outside the claim's own authoring network — flagged in the emitted row's own note as an **input declaration**, same disclaimer RET-Check already carries for every `root_independent` value) |
| `oracle.kind == "human_review"` | one row, `agent = lineage.run_by`, `source_root = reviewer identity` | `review` | `true` only if the reviewer's `independence_class ≥ I2` (`P6`'s ladder) — else the row is refused by `repro to-ret` with an explanation, never silently marked independent |
| `oracle.kind == "coq_kernel"` | **refused** — `repro to-ret` exits 1 with: "Coq closure is machine-side resistance (R2); run `glosa score` for that rung, not `glosa ret check`." | — | — |

A new preregistered scenario, **F — Reproduction interruption** (`cases/ret/F_reproduction_card.json`,
authored by S2), exercises this converter the way A–E already exercise hand-authored rows: take the
Mirror scenario (A) and add one `world_record` row emitted from a real, executed Reproduction Card
(Card 1 below) — expected: `N_P` rises by exactly one root, `N_P^ind` rises by exactly one (the card's
oracle is independent), an external interruption is now present, and rule 2 fires (LOW), same as
scenario C/E's existing pattern. **This is a converter test, not a formula retune** — every existing
scenario A–E's expected output is unchanged.

**Why `coq_kernel` never enters RET-Check.** RET's own §28 (RET-N16) asks for a consequence whose
`CausalAncestry` is not a subset of the recursive human–AI network — a *world*-side or *reviewer*-side
exogenous interrupt. A Coq kernel accepting a proof term is a real, independent check, but it checks
internal consistency of a *formal model*, not a world-side consequence (`P19`'s own disclaimer:
"a Coq 'Closed under the global context' certifies consistency of a finite model, neither certifies
empirical truth"). Feeding it into `N_P^ind` would let a purely formal, no-world-contact result read as
if it were the same kind of resistance as an independent human review or a published measurement —
exactly the collapse §0's design principle forbids. R2 stays its own row in `glosa score`'s table,
always.

---

## 5. Toledo's `resistance` block (build-computed, S3)

**Where it is computed, and by what.** A new script `scripts/compute_resistance.py` (owned by S3,
sibling to `scripts/n4_merge.py`/`scripts/v12_S.py` in pattern) reads `registry/CANONICAL.json`, each
entry's own `coq{}` block, and `registry/reproduction_card_index.json` (§2's citation index —
corrected 2026-09-08: populated Toledo-side by that repo's own
`scripts/register_reproduction_evidence.py`, which reads glosa's `cases/repro/*.json` directly;
never by a `glosa repro run --register-toledo` flag, which was never implemented) plus any
`review_report.yaml` pointers registered the same way, and **writes one `resistance` block per
entry back into `registry/
CANONICAL.json`** — this is the one narrow, explicitly-authorized exception to "do not edit
`CANONICAL.json` content fields except adding a computed `resistance` block via the build (never by
hand)": a dedicated script writes it, no editor ever hand-types it, and `LINEAGE.jsonl` is untouched
(this is a derived/computed field, not a content revision the ledger needs to log — the same status
`children[]` already has). `scripts/toledo_build.py` then simply **propagates** the persisted field
into `TOLEDO.json`, each `registry/entries/<code>.json` JSON-LD document, `site/index.json`, and the
`/v1/` static API — it never recomputes resistance itself, keeping one fact in one home
(`registry/CANONICAL.json`) and every other output a read-only projection of it.

**Entry shape (added to the existing `CANONICAL.json` entry object, `SCHEMA.md` addendum owned by S3):**

```json
"resistance": {
  "computed_at": "YYYY-MM-DD",
  "rungs": {
    "R0": {"held": true,  "evidence": []},
    "R1": {"held": false, "evidence": [], "reason": "no linked reproduction_card.preregistered_prediction or claim_card falsifier"},
    "R2": {"held": true,  "evidence": [{"type": "coq", "path": "coq/canonical/<code>.v"}]},
    "R3": {"held": false, "evidence": [], "reason": "no reproduction_card references this code"},
    "R4": {"held": false, "evidence": [], "reason": "R3 not held"},
    "R5": {"held": false, "evidence": [], "reason": "no review_report at independence_class >= I2 references this code"},
    "R6": {"held": false, "evidence": [], "reason": "R4 not held"}
  }
}
```

**Computation rules** (mirroring §1 exactly, entry-scoped):

- `R0`: always `true` when `statement.latest` is non-empty (every current entry).
- `R1`: `true` iff a linked `reproduction_card.preregistered_prediction.declared_at` exists and
  predates its own `run.date` (or, absent a card, a `claim_card` naming this code carries a non-TODO
  `five_questions.tested.falsifier`).
- `R2`: `true` iff `coq.coq_status == "closed"` — the v1.1 ladder's own honest floor, nothing looser.
- `R3`: `true` iff at least one `reproduction_card_index.json` row for this code has a filled `run{}`
  (regardless of `result.status`).
- `R4`: `true` iff at least one such card additionally has `oracle.kind` in the three external kinds
  **and** a filled `result` (PASS or FAIL both count — §0).
- `R5`: `true` iff at least one indexed `review_report` for this code has `independence_class ≥ I2`.
- `R6`: `true` iff an R4-holding card additionally passes the AOWC gate check — `glosa score`'s own
  logic (§1's R6 row), re-used by `compute_resistance.py` via the same shared function
  (`kernel/glosa_kernel.py::aowc_gate_check`, one fact in one home between the CLI and the Toledo
  build, imported the way `cli/glosa` already imports `ret_check`/`check_core_epistemic_structure` by
  relative path).

**Display.** Entry pages (`site/build_site.py::build_entry_context`) gain a `resistance_badges_html`
row alongside the existing `domain_badge`/`tier_badge`/`status_badge`/`coq_status_badge` row — seven
small badges `R0`…`R6`, held ones in the site's existing "current"-style accent, unheld ones in a
muted outline (never hidden — an unheld rung must be exactly as visible as a held one, per §0's design
principle), each with a `title=` attribute quoting that rung's one-sentence "what it does NOT certify"
from §1's table (the same `_definition_title_attr` glossary mechanism `TIER_DEFINITIONS`/
`COQ_STATUS_DEFINITIONS` already use). `/v1/entries/<mangled-code>.json` (`export_static.py`) carries
the same `resistance` object verbatim from `CANONICAL.json`, so an AI agent reading the static API
sees the identical rung table a human sees on the page — one fact, two renderings, never two
computations.

---

## 6. Three first cards (pre-registered before execution, S4)

### Card 1 — Genesis `finite_diagnostic` readouts vs. CODATA/PDG

**Which Toledo codes hold numeric predictions.** A direct query against `registry/genesis_root.json`
(592 root rows) found 73 rows tagged `finite_diagnostic` in `tier_in_genesis`, of which 25 carry a
numeric literal in their own `statement` text. Most of those 25 are structural/definitional counts
(gauge-group dimensions, calibration residuals against a *declared synthetic* ground truth) rather than
a prediction comparable to a real published external constant. Triaged for this first card:

| Code | Statement (quoted verbatim) | Oracle fit |
|---|---|---|
| **`EQ-068`** | *"(a) fit Λ_RD→GeV = 246/v_native = 88.96060634765863; independent Higgs-mass prediction 218.005 GeV vs real PDG 125.20 GeV — 74.13% error, fails a 5% band. (b) zero-fitted-parameter ratio test — identical 74.13% error. (c) zero-external-input internal consistency ... ratio 0.0612, 94% deviation, not consistent."* | **Primary.** `oracle.kind: published_value`, source = Particle Data Group *Review of Particle Physics* (pin the exact edition/DOI at run time), tolerance = the ±5% band Genesis's own text already declares. |
| **`EQ-045`** | *"dim Z(𝔤) = 1; 𝔤 ≅ u(1)⊕su(2)⊕su(3); dim = 1+3+8 = 12."* | **Secondary / positive control.** `oracle.kind: independent_implementation` — a from-scratch stdlib computation of `dim(u(1)) + dim(su(2)) + dim(su(3))`. Low-risk arithmetic identity; pairs with `EQ-068`'s disclosed FAIL as a companion expected-PASS card, so the first card batch shows both outcomes are genuinely possible (§1's non-tautology requirement for R6). |
| `EQ-063` | *"τ_c = ℏ/(2mc²) ... related check finite_diagnostic, D/M vs QuTiP residual 7.6×10⁻⁴."* | **Deferred.** `independent_implementation` = QuTiP, which is not stdlib and needs its own pinned, isolated environment (§2's `environment.packages` exception is written for exactly this, but S4 must decide whether v0.1 of the Ledger includes a QuTiP-backed card or leaves it PENDING). |
| `EQ-064`, `step42`, and the remaining 20 numeric-bearing rows | (various) | **Not R4 candidates as read.** `EQ-064`'s `M_true = 1` is a *declared synthetic* ground truth internal to the paper, not an external oracle; `step42`'s `v_Higgs = 246.22 GeV` is disclosed as a *measured boundary input*, not a derived prediction. Left untriaged for R4; S4 may re-run the same query (`grep`-style numeric-literal scan over `tier_in_genesis == finite_diagnostic` rows) to find further candidates, but none is asserted here without that direct read. |

**Pre-registration (before the card is run):** `preregistered_prediction.statement` = *"the fit
Λ_RD→GeV = 246/v_native predicts a Higgs boson mass of 218.005 GeV"*; `tolerance` = *"±5% of the PDG
Review of Particle Physics value for the Higgs boson mass"*; `notes` states explicitly that this is a
**retrospective formalisation** of an already-disclosed Genesis finding (the 74.13% error and the FAIL
verdict are already written into `genesis_root.json` today) being converted into a re-runnable,
hash-frozen Reproduction Card — not a fresh blind prediction. **Expected result: FAIL** (74.13% > 5%).
This is deliberately the ladder's paradigm case: a claim that genuinely failed its own declared oracle
check is the strongest available proof that R4/R6 are not rigged to always pass.

### Card 2 — RET-Check on our own ultracode meeting logs

**Source (world record = the logs).** `docs/MEETING_2026-09-06_toledo_design.md` in the Toledo repo:
three independently-drafted design proposals (REGISTRAR, FORMALISER, LIBRARIAN — "each drafted an
independent design"), scored by two independent judge passes ("two judge passes scored... conflicts
and gaps independently"), reconciled into ruled decisions each citing its `Source` proposal(s) and
`Judge consensus`. The committed file, at its git commit hash, is the frozen, causally-outside-any-
live-dialogue anchor RET-Check needs for an `external interruption` (§4's "world record = the logs").

**Provenance case** (`cases/ret/toledo_design_meeting_v1.json`, S4): one claim per ruled decision (or
one aggregate claim for "the meeting's design as a whole" — S4's call once building the real case
file). Rows: the two judge passes as `record_type: endorsement` agents; each decision's cited `Source`
proposal(s) as `source_root` values with `root_independent: true` (an **input declaration** taken
directly from the meeting record's own procedural claim of independent drafting — flagged in the case
file's own notes exactly as RET-Check's disclaimer requires, never asserted as independently verified
by this card); the committed Markdown file itself, at its commit hash, as one `world_record` row with
`parent: "-"`.

**Oracle.** `oracle.kind: independent_implementation` — the frozen RET RISK formula
(`cases/ret/PREREGISTRATION_v0_1.md`, unchanged since 2026-09-08) applied mechanically by
`scripts/ret_check.py` v0.3, a deterministic, non-LLM program whose rules predate this specific
application (satisfying pre-registration in RET-Check's own sense).

**Pre-registration:** *"Running RET-Check v0.3 on the Toledo design meeting's declared provenance graph
(3 independently-drafted proposal roots + 2 judge-pass endorsers, one-shot proposal→judge structure, no
detected cycle) will read `N_P^ind ≥ 3` and `RET RISK: LOW`."* Tolerance: exact categorical match
(LOW/MEDIUM/HIGH — no numeric band). **Result:** run `glosa ret check cases/ret/
toledo_design_meeting_v1.json`, record the actual `N_A`/`N_P`/`N_P^ind`/cycle/risk output, compare to
the categorical prediction, mark PASS/FAIL.

### Card 3 — IDM number-ladder approximants of π, √2, e vs. mpmath (**PENDING**)

A direct listing of `toledo/registry/proposals/` at drafting time found no IDM merge file
(`idm.merged.json` or equivalent) — the handoff's own trailing line ("IDM into Toledo... ultracode")
names work in progress, not a landed result; this card is honestly staged as **PENDING, no
`toledo_codes[]` populated**, per the task's own instruction. Once the IDM root extension lands
(Toledo codes assigned to the D→ℤ→ℚ→ℝ number-ladder objects), the pre-registration to write is:

- **Statement:** for each of π, √2, e — the IDM ladder's own discrete-rational approximant at a
  declared step count reproduces the first *N* decimal digits (S4/whoever executes this picks *N*
  before the run; a reasonable first value is 50).
- **Tolerance:** exact digit match to *N* places (0 discrepancy) — not a numeric error band, since both
  sides are exact rational/decimal expansions computable to arbitrary precision.
- **Oracle:** `independent_implementation`, source = `mpmath`, `version` pinned exactly.
  `environment.packages: {"mpmath": "<pinned>"}` — the one named exception in §2, run in its own
  declared subprocess, never imported by the stdlib runner.

---

## 7. Build streams (file ownership)

| Stream | Owns | Depends on |
|---|---|---|
| **S1** — glosa schema + cards P22/P23 + CLI + runner | `methodology/P22_reproduction_ledger.md`, `methodology/P23_resistance_ladder.md`, `schema/reproduction_card.schema.json`, `templates/knowledge/reproduction_card.yaml`, `cli/glosa` (`repro new/run/verify/to-ret`, `score` verbs + their `cmd_*`/scaffold functions), `scripts/repro_check.py` (stdlib-only run/hash/compare driver, same "no third-party import" self-test convention as `scripts/ret_check.py`), `kernel/glosa_kernel.py` additions (`validate_reproduction_card`, `aowc_gate_check` — the shared function §5/§8 both call), `tests/test_reproduction_card.py`, `tests/test_score.py`. | This document. |
| **S2** — RET-Check v0.3 + tests | `scripts/ret_check.py` (bump to v0.3: the converter path only, formula untouched), `cases/ret/PREREGISTRATION_v0_1.md` (dated v0.3 addendum, no scenario A–E output changes), `cases/ret/F_reproduction_card.json` (new preregistered scenario), `methodology/P21_ret_check.md` (v0.3 addendum), `tests/test_ret_check.py` additions. | S1 (`glosa repro to-ret` calls into `ret_check.py`'s existing `run()`). |
| **S3** — Toledo resistance block (build + site + API + tests) | `toledo/scripts/compute_resistance.py` (new), `toledo/scripts/toledo_build.py` (propagate `resistance` into JSON-LD/`TOLEDO.json`/`site/index.json`), `toledo/site/build_site.py` (badge rendering, `RESISTANCE_DEFINITIONS` glossary), `toledo/mcp/toledo_mcp/export_static.py` (`resistance` in `/v1/entries/<code>.json`), `toledo/registry/SCHEMA.md` (dated addendum for the `resistance` block + `registry/reproduction_card_index.json` shape), `toledo/tests/test_build.py` + `test_site.py` updates. **Never** hand-edits `registry/CANONICAL.json` content fields — only `compute_resistance.py` writes the `resistance` sub-object, and `LINEAGE.jsonl` stays untouched (§5). | S1 (reads `reproduction_card_index.json` rows S1's CLI produces), S2 (R2 rows are Toledo's own `coq_status`, unaffected by S2). |
| **S4** — first two cards executed (Genesis constants; RET-Check meeting logs) | `cases/repro/EQ-068_higgs_pdg.json`, `cases/repro/EQ-045_gauge_dim.json` (Card 1), `cases/ret/toledo_design_meeting_v1.json` (Card 2), plus the actual `glosa repro run`/`glosa repro verify`/`glosa ret check` command transcripts recorded as this stream's own evidence (`P19`'s "every number reported comes from a command you ran"). Card 3 stays a written pre-registration only (§6), no execution, until the IDM merge lands. | S1 (CLI to run the cards), S2 (Card 2's `glosa ret check` run), S3 only for the resulting badges to appear on `EQ-068`/`EQ-045`'s Toledo entry pages after `compute_resistance.py` next runs — S4 does not block on S3 to execute its own cards. |

---

## Not-do

- Do not collapse the seven-rung table to a single number anywhere — CLI, Toledo page, `/v1/` JSON,
  or a summary sentence in a handoff.
- Do not mark a rung `held` without a concrete evidence pointer to a file that exists.
- Do not feed a `coq_kernel`-oracle card into RET-Check's `N_P`/`N_P^ind` — machine-side and world-side
  resistance stay two separate counts, always.
- Do not retune the RET RISK formula (`cases/ret/PREREGISTRATION_v0_1.md`) to accommodate the v0.3
  converter — v0.3 adds an input path, never a rule change.
- Do not hand-edit `registry/CANONICAL.json`'s `resistance` block, or any other content field, outside
  the one script named in S3.
- Do not present Card 1's `EQ-068` FAIL as a defect to be hidden or explained away in the badge —
  it is the ladder's own proof that R4/R6 can genuinely fail.
- Do not populate Card 3's `toledo_codes[]` before the IDM merge actually lands.

## NC pairs

Held ≠ passed (R3/R4 hold on FAIL too) · registered ≠ verified (`repro run` ≠ `repro verify`, maker ≠
checker) · machine-side (R2) ≠ world-side (R3–R6) · declared-independent ≠ independent (same caveat
`P21` already carries, inherited unchanged by every card converted through `repro to-ret`) · one rung
held ≠ artifact certified.

## Disclaimers

This ladder audits **declared, filed evidence of resistance**, never the underlying truth of a claim
(`P19`'s own disclaimer, restated) — a full R0–R6 row of `held: true` still leaves the claim's own
`tier`/`k_state` exactly where `P6`/`P10` already put it; passing every rung licenses nothing beyond
"every named check was actually run and filed," per this document's own §0.

## Tier

Dr — specified from the founder ruling and the cited sources above; independently unreviewed. Every
Toledo count/quote in §6/§7 is `finite_diagnostic` in the narrow sense that it was read by a command
run while drafting this document (reported, not asserted from memory) — the design decisions
themselves (schema shape, CLI contracts, build-ownership split) are Dr, awaiting the S1–S4 build and
an independent review pass before any of it is `finite_diagnostic` in the fuller "tests executed"
sense `cli/glosa`'s own tier line uses.
