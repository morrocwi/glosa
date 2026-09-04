# glosa CLI

tier: finite_diagnostic (tests executed: `cli/glosa self-test`, `cli/glosa demo`, and
`cli/glosa check <path>` run against every file in `schema/examples/*.example.json` (20/20 PASS)
and `schema/examples/fail/*.json` (6/6 correctly REJECTED) -- exact commands and recorded output
are reproduced at the bottom of this file. Every dispatch/scaffolding decision this tool makes
beyond what those runs actually exercised is Dr-tier, unreviewed, same as the rest of this repo.

`cli/glosa` is a single stdlib-only Python 3 script (`argparse`) that imports
`kernel/glosa_kernel.py` by relative path (this file's own directory's sibling `kernel/`), never
as an installed package. It implements FOUNDATION_v0.5.md §9's "Callable layer" (CLI skin) plus
`design/S14_literature-review-system.md`'s five-command `lit` subset the task named. It never
makes a network call (same floor as the kernel).

Run it as `./cli/glosa <command> ...` (executable bit set) or `python3 cli/glosa <command> ...`
from anywhere -- the kernel import and every default output path resolve relative to this file's
own location (`kernel/`, `schema/`, `templates/knowledge/` all found via `Path(__file__)`), not
relative to your current directory. **Every command's own output paths are absolute
(`~/ANSE.ASIA/glosa/records/...` etc.) unless you pass `--out-dir`.**

**Optional dependency:** `PyYAML`. When importable, every "new"/scaffold command writes a
human-fillable `.yaml` file; when it is not, the same command writes `.json` instead and says so
plainly in its own JSON result (`"format": "json", "pyyaml_available": false`) -- never silently.
`jsonschema==3.2.0` is the kernel's own optional dependency (see `kernel/glosa_kernel.py`'s
header); when it is not importable, every schema check falls back to a coarse required-field
presence check and every result's `warnings` says so.

**Logging:** every command -- success, refusal, or error -- appends exactly one
`{"kind": "tool_call", ...}` JSON line to `./logbook.jsonl` **in your current working
directory** (not this file's directory), matching `mcp/glosa_mcp_server.py`'s own logging
contract (CLI and MCP are two callable skins over the same kernel, and log the same way).

**Output convention:** every command prints ONE JSON object to stdout (`json.dumps(..., indent=2)`)
and sets its process exit code as documented below. Nothing else is printed to stdout, so
`cli/glosa <command> ... | python3 -m json.tool` (or `jq`) always works.

---

## Commands and exit codes

Unless a row says otherwise, exit code is **0 = ok/PASS, 1 = FAIL/error**. `check`,
`*  validate` commands, and `lit table`/`kg validate` follow that same 0/1 convention against
their own `result.ok` (or, for `kg validate`, the top-level `ok`).

| Command | What it does | Exit codes |
|---|---|---|
| `glosa intake new --project P --human-owner H [--origin-blackbox-ref R] [--out-dir D]` | Scaffold a fresh `problem_card` (S1 intake gate). Default `--out-dir`: `records/problems/`. | 0 always (scaffold is self-checked, never refuses) |
| `glosa intake validate <path>` | `kernel._schema_validate` against `problem_card.schema.json`. | 0 PASS, 1 FAIL |
| `glosa claim new [--shape stub\|full] --human-owner H [--claim-id ID] [--origin-blackbox-ref R] [--out-dir D]` | Scaffold a fresh `claim_card`. `--shape` default `full`. Default `--out-dir`: `records/claims/`. Populates `disclaimers_emitted` via `kernel.compute_disclaimers` for real (full shape). | 0 always |
| `glosa claim validate <path>` | `kernel.validate_claim_card` (all 11 §3.3 kernel gate rules + schema). | 0 PASS, 1 FAIL |
| `glosa claim disclaimers <path>` | `kernel.compute_disclaimers(card)`, prints the list. | 0 always |
| `glosa check <path>` | Validate ANY glosa instance file. Detects which of the 20 schemas it is by, in order: (1) an in-content `"$schema"` key (bare stem or `<name>.schema.json`), (2) the filename containing a known schema stem, (3) a last-resort field-fingerprint guess (labeled `"detected_by": "field-fingerprint (...) -- NOT $schema/filename, use with caution"` so a caller can tell a guess from a real match). Dispatches to the matching `kernel.validate_*` for the 5 kernel-backed kinds, `kernel.lit_gate` for `litreview_manifest`, and `kernel._schema_validate` (generic) for the other 14. | 0 PASS/PASS_WITH_LIMITS, 1 FAIL/unrecognized |
| `glosa review new --claim REF --route R1 [--reviewer ID] [--out-dir D]` | Scaffold a fresh `review_report`. Default `--out-dir`: `reviews/routes/<claim>/<route>/`. | 0 always |
| `glosa review validate <path>` | `kernel.validate_review_report` (Bounded-Judge Law). | 0 PASS, 1 FAIL |
| `glosa readiness check [path]` | Schema-check a `readiness_report`. If `path` omitted, looks for `./readiness_report.{yaml,json}`. | 0 PASS, 1 FAIL, **2** = no path given and none found |
| `glosa release-gate <manifest> [--cards P...] [--reviews P...]` | `kernel.gate_release(manifest, cards, reviews)`. **`manifest.status == "Rollback"` short-circuits to ROLLBACK without running the gate** (a human rollback decision overrides gate computation -- `gate_release` itself never returns "ROLLBACK", so this CLI-level check is what actually produces exit 3). | **0** PASS/PASS_WITH_LIMITS, **1** FAIL, **2** HUMAN_REVIEW, **3** ROLLBACK |
| `glosa defeater route <card> <node>` | `kernel.defeater_route(card.provenance_dag, node)` (Readout Condition Proposition 3). | 0 = distinction survives, 1 = `distinction_lost: true` |
| `glosa genre route <card> [--search-log] [--target-claim-ref R] [--bounded-case yes\|no] [--mixed]` | `kernel.route_genre(card, context)`. `--mixed` opts into the step-9 `MIXED_GENRE` tie detector. | 0 = a genre was assigned, 1 = none matched (needs a human Approver) |
| `glosa cite check <card> [--offline]` | `kernel.validate_citation_card` (schema + status + `xenon_ledger_ref` completeness). **`--offline` is accepted for the shape the task specified, but this CLI performs the SAME offline-only check whether or not you pass it** -- no live Crossref/OpenAlex/PubMed/DataCite lookup is implemented anywhere in this tool; every result carries an explicit note saying so, and omitting `--offline` prints an extra note rather than silently pretending a live check ran. | 0 PASS, 1 FAIL |
| `glosa lit new <problem-slug> <hypothesis-ref> [--search-mode M]` | Scaffold `search_log.<ext>` + `dialogue_table.md` under `records/lit/<slug>/<hyp-slug>/`. | 0 always |
| `glosa lit freeze <problem-slug> <hypothesis-ref>` | Refuses (exit 1) unless `frozen_scope.hypothesis_or_falsifier` is filled AND `sources_found` is still empty (S14 §2.2: frozen BEFORE opened). On success, appends one line to `FREEZE_LOG.jsonl` in that hypothesis's dir. | 0 FROZEN, 1 refused |
| `glosa lit table <problem-slug> <hypothesis-ref>` | Re-renders `dialogue_table.md`'s `## Table` section from every `dialogue_table_row`-shaped file in `records/lit/<slug>/<hyp>/rows/*.{yaml,json}` that passes `dialogue_table_row.schema.json` (invalid rows are reported, not silently dropped or silently included). | 0 always (invalid rows listed in `rows_invalid`, not an error by themselves) |
| `glosa lit select <problem-slug> --decided-by H --reason R [--chosen "h1,h2"\|"all"] [--park "h:reason" ...] [--cooking-log-ref REF]` | Scans `records/lit/<slug>/*/litreview_manifest.*` for every hypothesis with a manifest, builds the `candidates` array, and writes `hypothesis_selection.<ext>`. **No `--auto`**: every candidate not in `--chosen` MUST have a matching `--park '<hyp>:<reason>'` or the command refuses (a parked hypothesis's reason is never fabricated). | 0 written, 1 refused/no manifests found |
| `glosa lit manifest <problem-slug> <hypothesis-ref> --human-owner H [--freeze]` | Assembles `litreview_manifest.<ext>` from `records/lit/<slug>/<hyp>/citations/*.{yaml,json}` (empty if none exist yet -- an honest `gate.overall: FAIL` with a `blocked_reason`, matching S14 §10's own worked example: "the gate is shown working, not shown passing"). Re-checks internal consistency via `kernel.lit_gate`. `--freeze` sets `status: FROZEN` regardless of the gate verdict (freezing the object and passing its gate are two different events, S14 §2.6). | 0 = internally consistent (`lit_gate_check.ok`), 1 = inconsistent |
| `glosa kg validate [--dir D]` (default `kg/`) | Schema-checks every line of `<D>/nodes.jsonl` + `<D>/edges.jsonl`, flags dangling `from`/`to` refs, and detects cycles among `relation: derives_from` edges only. | 0 clean, 1 any node/edge error, dangling ref, or cycle |
| `glosa kg merge [--projects-glob G] [--out-dir D]` (defaults `cases/*/kg`, `kg/`) | Concatenates every matching project's `nodes.jsonl`/`edges.jsonl` into `--out-dir` (dedup by id, last match wins, duplicates reported). **Pass one glob matching every project you want in the merge at once** -- each invocation fully regenerates `--out-dir` from what the glob matches THAT call, it does not accumulate across separate invocations (matches REPO_SPEC's "repo-root `kg/` is generated output only, never hand-edited"). Zero matches is not an error. | 0 always |
| `glosa advise <release_manifest> [--identity ID] [--cards P...] [--citation-cards P...] [--expires-at D] [--out-dir D]` | Project Advisor (§7.7). **Hard refuses, writing NO file**, when: the manifest itself fails its own schema/kernel check; `gate_verdict` is not `PASS`/`PASS_WITH_LIMITS`; or one of the checkable SCRAM conditions fires -- `ADVISOR_IDENTITY_CONFLICT` (`--identity == manifest.human_owner`), `K_STATE_MISREPRESENTED` (needs `--cards`), `UNVERIFIED_CITATION_IN_SCOPE` (needs `--citation-cards`). **`VENUE_DISCLOSURE_GAP` and `XENON_THRESHOLD` are NOT implemented** (no venue-candidate data / no Xenon ledger reader in this CLI) -- always reported CLEAR, never silently upgraded to a false pass; every successful result's `note` says so and a human must check those two by hand. On success, scaffolds `conversion_plan.<ext>` (`tier` fixed `"Dr"`) under `records/advisory/`. | 0 = plan written, 1 = BLOCKED/refused (no file) |
| `glosa schema summary` | Lists every one of the 20 `schema/*.schema.json` files' own `title` + `required` list (read live, never re-typed), plus row counts from `methodology/data/*.json`. | 0 always |
| `glosa self-test` | `kernel.self_test()` verbatim (every `schema/examples/*.example.json` PASSes its matching `validate_*`; every `schema/examples/fail/*.json` is REJECTED). | 0 PASS, 1 FAIL |
| `glosa demo` | Runs the cat worked example (`schema/examples/*`) end-to-end: `validate_blackbox_note` → `validate_claim_card` → `compute_disclaimers` → `route_genre` → `independence_ceiling` → `silent_lift_check` → `defeater_route` → `validate_citation_card` → `validate_review_report` → `validate_release_manifest` → `gate_release` → `self_test`, and prints every verdict. | 0 = every step with an `ok` field read `!= false`, 1 otherwise |

Every `intake`/`claim`/`review`/`lit`/`advise` "new"/scaffold command writes a file that
**validates cleanly out of the box** as a fresh `Draft`/`DRAFTING` artifact -- enum/const/required
values are chosen to be schema-legal defaults (verified against `schema/*.schema.json`'s own
`required`/`enum` lists while this tool was written and re-confirmed by the runs below), never
placeholder pseudo-syntax like `"A | B | C"`. What still needs a human/AI to fill in is real
*content* (the claim text, the standpoint, the falsifier, ...), not shape.

---

## What this CLI does NOT do (read before trusting a command name alone)

- **No live citation lookup.** `cite check` never calls Crossref/OpenAlex/PubMed/DataCite over
  the network -- there is no network call anywhere in this file or the kernel it wraps. Every
  `fetch_status`/`metadata_verified`/`claim_match_verified` this tool reports is exactly what was
  already written in the file you gave it; the tool never upgrades those fields itself.
- **`advise`'s SCRAM check is partial.** `VENUE_DISCLOSURE_GAP` and `XENON_THRESHOLD` are not
  implemented (no venue-candidate data model, no Xenon ledger reader) -- a human must check those
  two by hand before treating an `advise` "READY_TO_DRAFT" result as covering all five S12 §8
  conditions.
- **`kg merge` fully regenerates its output** from whatever its `--projects-glob` matches in one
  call; it does not incrementally merge across separate invocations (by design, matching
  REPO_SPEC's "generated output only, never hand-edited" rule for the repo-root `kg/`).
- **No git integration.** This CLI reads and writes plain files only; committing/branching/PRs
  are a separate, human-run step (per `AGENTS.md`'s "Always PR workflow").

---

## Reproduced test output (tier basis for this file's own header)

Run from the repo root, `~/ANSE.ASIA/glosa`, with `python3 -m unittest discover -s tests` first
confirming the kernel itself (84 tests, `OK`, unchanged by this task) before exercising the CLI:

```
$ cli/glosa self-test
{
  "action": "self_test",
  "result": {
    "ok": true,
    "verdict": "PASS",
    "errors": [],
    "warnings": [],
    "tier": "finite_diagnostic"
  }
}
$ echo $?
0

$ cli/glosa demo | python3 -c "import json,sys; print(json.load(sys.stdin)['all_ok'])"
True
$ echo $?
0
```

`cli/glosa check <f>` for every `f` in `schema/examples/*.example.json` (20 files): **20/20 exit
0**, each `"detected_by": "filename"` and its matching `validate_*`/`lit_gate` result `"ok": true`.

`cli/glosa check <f>` for every `f` in `schema/examples/fail/*.json` (6 files): **6/6 exit 1**
(`fail_k2_without_i5.json`, `fail_missing_disclaimer.json`, `fail_no_independent_check.json`,
`fail_same_model_review.json`, `fail_stub_public.json`, `fail_th_coqc_no_witness.json`).

Additional command-by-command behavior confirmed in a scratch directory during this build
(not repeated verbatim here for length; see the task's own session transcript for the full
JSON of each): `claim new --shape stub` and `--shape full` both self-check PASS; `review new` +
`review validate` round-trip PASS; `readiness check` with no path and none present exits **2**;
`release-gate` confirmed at all four exit codes (0 on the worked example, 1 on a missing claim
card, 2 on an injected unresolved `dissent_records` entry, 3 on `status: Rollback`); `defeater
route` on the worked example's single-node DAG correctly reports `distinction_lost: true` (exit
1); `genre route --mixed` on a claim mutated to also satisfy `position_reply` correctly returns
`MIXED_GENRE` naming both matched branches; `cite check` with and without `--offline` behave
identically and both say so; the full `lit new` → `lit freeze` (refused before scope filled,
accepted after) → `lit table` (renders a valid `dialogue_table_row`, reports an invalid one
separately) → `lit manifest` (honest `FAIL` with zero citations, `PASS` once a `VERIFIED`
citation is added, `--freeze` sets `status: FROZEN`) → `lit select` (refuses an un-parked
candidate, succeeds with `--chosen all`) pipeline was run end-to-end on a synthetic
"cat-problem"/"H1" case; `kg validate` correctly flags a node missing a required field, the
resulting dangling edge reference, and a manually-injected `derives_from` cycle, then reports
clean once fixed; `kg merge` correctly merges two synthetic per-project `kg/` directories in one
glob and reports duplicate ids when re-run over an overlapping set; `advise` refuses (no file
written) both when `gate_verdict` is not `PASS`/`PASS_WITH_LIMITS` and when `--identity` collides
with `manifest.human_owner`, and writes a schema-valid `conversion_plan` otherwise; `schema
summary` lists all 20 schemas with live-read `required` lists.
