Tier: Dr (synthesis) over finite_diagnostic-heavy inputs. Not a fresh audit — a synthesis of six
lens reviews (`reviews/ARCH_structure.md`, `ARCH_sustainability.md`, `ARCH_usability.md`,
`ARCH_integrity.md`, `ARCH_efficiency.md`, `ARCH_lifecycle.md`) plus one cross-check adversarial
pass (`reviews/ARCH_CROSSCHECK.md`, every vote verbatim). No command in this document was
re-executed by the synthesizer; all `finite_diagnostic` claims below are inherited from the lenses
or the cross-check votes, cited by source. No forbidden words used. No external/institutional
validation is proposed anywhere below as what would make this repo's architecture legitimate —
every claim is checked against the repo's own files, commands, and its own stated rules, nothing
else (`EPIS-KNOWLEDGE-VALIDATION`).

# ARCHITECTURE_REVIEW_v1 — glosa architecture review synthesis

> Repo: `glosa`, branch `design/v0.3`. Six lenses reviewed commit `233b0ca`; this synthesis was
> written after HEAD advanced one commit to `043225f` (an unrelated Blackbox Log feature commit) —
> nothing below was re-verified against `043225f`; see §8.
> Founder question (verbatim): *"ตรวจสอบว่าสถาปัตย์วางดีหรือยัง ตรงไหนต้องปรับ ให้มีประสิทธิภาพและยั่งยืน"*
> — is the architecture well laid, what must change, for efficiency and sustainability (a solo
> scholar must be able to maintain this for years).

---

## 1. Verdict — is the architecture well laid?

The callable layer glosa actually ships — the kernel, CLI, MCP server, 20 JSON schemas, and the
84-test suite — is genuinely well laid: it runs clean end to end (`python3 -m unittest discover -s
tests` → 84/84 OK; `./cli/glosa self-test` and `./cli/glosa demo` → PASS; the load-bearing gate
machinery imports only Python stdlib), and every one of the ~35 gaps six independent lenses found
is a cheap, mechanical fix, not a redesign — which is itself evidence the underlying design is
sound. But the paper trail a solo scholar actually depends on to navigate that mechanism is not
well laid as shipped: four documents (the mandatory onboarding gate, `methodology/README.md`,
`design/REPO_SPEC_v0.4.md`, and the disk itself) each claim to be the map and disagree with each
other, one specified "hard validation error" (kernel gate rule 12) has zero code presence yet is
reported as *passing* in both the repo's own release-prep review and the public paper draft, and
the single most safety-critical rule in the whole design — a human must be the Approver before a
claim reaches `Approved-for-Live`/K2/L5 — has no mechanical check anywhere, so an all-AI chain can
reach the system's highest trust tier today with zero human involvement and zero warning emitted.
**Verdict (Dr):** well laid at the mechanism layer, not yet well laid at the discipline-over-itself
layer — every lens converged on the same root cause (four unarchived FOUNDATION generations with no
single canonical pointer, and two release gates the repo built but never wired into its own
checklist), so closing the MUST list below — dependency-ordered, mechanical, no new infrastructure
— is what turns "well laid in principle" into "well laid as shipped," using only the horizontal,
self-checking discipline the repo already asks of its own users, applied to itself.

---

## 2. MUST — before public release

Deduplicated from 23 cross-checked MUST recommendations across six lenses (see
`reviews/ARCH_CROSSCHECK.md` for every vote verbatim) down to 13 distinct fixes, ordered so that
each item's prerequisites are closed by an earlier item. `who` follows this repo's own division of
labor (`AGENTS.md` rule 5): **ai** = mechanical, no judgment call; **joint** = AI drafts, founder
must rule on the content or authorize an irreversible/public action; **human** = only the founder
can make this call.

### MUST-1 — One canonical FOUNDATION spec; archive the rest; make the CLI discoverable from the same files
*(cross-check: items #1, #4, #6, #7, #9, #14, #15(split), #19 in ARCH_CROSSCHECK.md — 5 of 6
lenses independently found this; the single most-corroborated finding in the whole review)*

- **Files:** `design/FOUNDATION_v0.4.md`, `design/FOUNDATION_v0.5_PATCH.md`,
  `design/CURRENT_SPEC.txt` (new), `design/archive/` (new dir), `README.md:10,22`, `AGENTS.md:5`,
  `CLAUDE.md:5`, `GEMINI.md:5`, `llms.txt`, `methodology/README.md:11,63`, `schema/README.md:4,49,135,138`,
  `cli/README.md:11`, `scripts/check_repo.sh`
- **Exact change:**
  1. Founder ratifies `design/FOUNDATION_v0.5_PATCH.md`'s content (it is fully specified — exact
     insertion text already written); AI applies it to `design/FOUNDATION_v0.4.md` mechanically.
  2. `git mv design/FOUNDATION_v0.2.md design/FOUNDATION_v0.3.md design/REPO_SPEC_v0.2.md
     design/REPO_SPEC_v0.3.md design/archive/`, each stamped with a one-line "SUPERSEDED, see
     v0.4" banner (record the supersession — do not delete history).
  3. Write `design/CURRENT_SPEC.txt` containing exactly `FOUNDATION_v0.4.md`.
  4. Repoint every **entry-point/instructional** doc (`README.md`, `AGENTS.md`, `CLAUDE.md`,
     `GEMINI.md`, `methodology/README.md`, `schema/README.md`, `cli/README.md`) at the current
     spec — *and*, in the same edit pass, add one short paragraph + one example command
     (`./cli/glosa intake new --project <name> --human-owner <you>`) to `README.md`, the
     `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` gate block, and `llms.txt`, so the one tool proven to
     produce valid artifacts on the first try (ARCH_usability F5) is discoverable from the same
     files being repointed.
  5. Add a two-tier mechanical check to `scripts/check_repo.sh`: entry/instructional docs must
     cite exactly the string in `design/CURRENT_SPEC.txt`; implementation docstrings
     (`kernel/glosa_kernel.py`, `tests/test_kernel.py`, `cli/glosa`) may honestly lag behind
     (they should cite the version they actually implement) but must be flagged as "behind
     current," never silently pass as if current.
- **Cost:** ~7h (2h merge+ratify, 1h archive, 1.5h repoint 7 docs + CLI paragraph, 2.5h build the
  two-tier check_repo.sh check). One cross-check vote estimated the narrower repoint-only slice at
  0.5–1h; another estimated the full-scope version (all 20 schema headers + 14 methodology cards
  too) at 6h. 7h is this synthesis's Dr-tier consolidated estimate across the overlapping work.
- **Who:** joint — founder ratifies the v0.5 patch content and the archive decision (a call about
  how the repo's own history should read, not a pure engineering choice); AI performs every
  mechanical edit.
- **Drift test:** `bash scripts/check_repo.sh` exits 0 with the new two-tier version-citation
  check included; `grep -rln "FOUNDATION_v0\.[0-2]\b" README.md AGENTS.md CLAUDE.md GEMINI.md
  llms.txt methodology/README.md schema/README.md cli/README.md` returns zero hits;
  `grep -c "cli/glosa" README.md AGENTS.md llms.txt` each ≥1.
- **Risk if ignored:** every future session (human or AI, including this workspace's own
  fail-closed gate protocol) is told to read a spec two-to-four generations stale before touching
  anything — the exact failure mode `AGENTS.md` rule 2 exists to prevent, happening in the gate
  itself; independently corroborated by all of `ARCH_structure`, `ARCH_sustainability`,
  `ARCH_usability`, `ARCH_efficiency`, and `ARCH_lifecycle`.
- **Dissent on record:** one cross-check vote on the narrower "just merge v0.5 into v0.4" sub-step
  argued this specific piece is SHOULD not MUST, since the unmerged patch is honestly tiered ("Dr,
  specified not applied") rather than silently misleading (ARCH_CROSSCHECK.md item #15, vote 1).
  This synthesis kept the full bundle MUST on the strength of the other five independent
  convergent findings and the second vote's compounding-drift argument, but the dissent is
  preserved — see §5.

---

### MUST-2 — Fix `templates/knowledge/blackbox_note.yaml`'s YAML validity
*(cross-check: item D1 in ARCH_CROSSCHECK.md — see synthesizer override note below)*

- **Files:** `templates/knowledge/blackbox_note.yaml`, `scripts/check_repo.sh`
- **Exact change:** line 63's placeholder text (`what_changed: <one sentence: which distinction was
  added/removed/re-attributed>`) contains a bare `:` that YAML reads as a nested-mapping start —
  quote or reword every placeholder in the file containing a bare colon; scan the rest of the file
  for the same pattern. Add a loop to `scripts/check_repo.sh` that YAML-parses every
  `templates/knowledge/*.yaml` file and fails the build on any parse error.
- **Cost:** 1h.
- **Who:** ai.
- **Drift test:** `for f in templates/knowledge/*.yaml; do python3 -c "import yaml,sys;
  yaml.safe_load(open(sys.argv[1]))" "$f" || echo "BROKEN: $f"; done` reports nothing; the same
  check wired into `scripts/check_repo.sh` and `bash scripts/check_repo.sh` exits 0.
- **Risk if ignored:** every reader following the documented human path hits an unexplained parser
  crash on the very first file they are told to fill in, before writing a single word of content
  (ARCH_usability F1, directly reproduced: `yaml.safe_load` → `PARSE ERROR: mapping values are not
  allowed here`, line 63).
- **Synthesizer override, disclosed:** the cross-check ledger formally marked this item `REFUTED`
  — but with an **empty reasons array**, i.e. zero skeptic argument was recorded against it (see
  `reviews/ARCH_CROSSCHECK.md` §Part 2, D1). Per readout-not-truth, this synthesizer treats an
  empty reasons array as a gap in the adjudication record, not evidence the fix is wrong, and has
  restored it to MUST on the strength of the unrebutted, directly-reproduced lens finding and its
  trivial (1h) cost. This override is flagged for the AI assistant and the founder in §7 below and should be
  confirmed or reversed explicitly, not silently accepted.

---

### MUST-3 — Fix `templates/knowledge/citation_card.yaml`; build a permanent template-vs-schema checker
*(cross-check: item #3 in ARCH_CROSSCHECK.md)*

- **Files:** `templates/knowledge/citation_card.yaml`, `scripts/check_templates_vs_schema.py`
  (new), `scripts/check_repo.sh`
- **Exact change:** add the missing `independence_class` field (schema-required, absent from the
  58-line template including its inline comments) to `templates/knowledge/citation_card.yaml`.
  Write `scripts/check_templates_vs_schema.py`: for every `templates/knowledge/<name>.yaml` with a
  matching `schema/<name>.schema.json`, extract the YAML's top-level keys (or the keys one level
  under a wrapper key, for wrapper-keyed templates like `blackbox_note.yaml`) and diff against the
  schema's `required` array; fail on any gap. Wire it into `scripts/check_repo.sh`.
- **Cost:** 4.5h (1h template fix + 3.5h permanent checker, handling both flat and wrapper-keyed
  YAML, per the cross-check vote's own caveat about the naive top-level-diff false-positiving on
  `blackbox_note.yaml`).
- **Who:** ai.
- **Drift test:** `python3 scripts/check_templates_vs_schema.py` exits 0 across all
  `templates/knowledge/*.yaml`; wired into `scripts/check_repo.sh`, `bash scripts/check_repo.sh`
  exits 0.
- **Risk if ignored:** directly breaks the tool's core promise — a solo scholar fills in the
  template exactly as instructed and gets an unexplained schema-validation failure, while
  `./cli/glosa self-test` stays green because it validates a different, correct internal fixture —
  automated checks pass while the human-facing artifact is silently broken.

---

### MUST-4 — Make `validate_claim_card` fail closed when `jsonschema` is unavailable
*(cross-check: item #12 in ARCH_CROSSCHECK.md)*

- **Files:** `kernel/glosa_kernel.py` (`validate_claim_card`), `cli/glosa` (exit-code surfacing),
  `tests/test_kernel.py`
- **Exact change:** `kernel/glosa_kernel.py:36-43` wraps the `jsonschema`/`RefResolver` import in a
  bare `try/except Exception`; when it fails, `validate_claim_card` silently degrades to a
  presence-only check and returns `ok: True` for the same illegitimate payload the real validator
  would reject (reproduced live: an F1-style card with invalid enums, a malformed `claim_id`, and
  wrong-typed `five_questions` returns `ok: True, verdict: PASS_WITH_LIMITS` the moment
  `jsonschema` import is blocked — and this workstation's installed `jsonschema==3.2.0` is already
  outside `requirements.txt`'s pinned `>=4.0` range). Minimum viable fix (both cross-check votes
  converged on this as cheaper and equally effective vs. hand-duplicating all 8 schema-only rules):
  make `validate_claim_card` return `ok: False` — not merely append a `warnings` string — whenever
  schema validation silently fell back to the presence-only checker for a card at/above the
  tier/k_state/status thresholds rules 1,2,3,4/9,10,11 gate. Reuse the kernel's own existing
  kernel-only helpers (`silent_lift_check()`, the stub-shape and provenance checks already inside
  `gate_release`, `_max_independence_class`) rather than duplicating schema logic by hand. Add one
  fallback-mode adversarial test to `tests/test_kernel.py`.
- **Cost:** 5h.
- **Who:** ai.
- **Drift test:** the new `tests/test_kernel.py` fallback-mode test — simulate `jsonschema`
  unavailable via an import hook, feed the F1-style illegitimate payload, assert
  `validate_claim_card(card)["ok"] is False`. `python3 -m unittest discover -s tests` includes and
  passes this test.
- **Risk if ignored:** confirmed live on this very workstation (`pip3 show jsonschema` → `3.2.0`,
  outside the pinned range) — every claim-card gate rule this system is built around can already
  silently stop running today, with no error and exit code 0, on a `pip install -r requirements.txt`
  that lands a newer or older `jsonschema`.

---

### MUST-5 — Fix the CI `schema-validate` job (RefResolver + directory-layout mismatch)
*(cross-check: item #13 in ARCH_CROSSCHECK.md)*

- **Files:** `.github/workflows/ci.yml`
- **Exact change:** the job's bare `jsonschema.validate(instance, schema)` call tries to resolve
  cross-file `$ref`s against the placeholder `$id` `https://glosa.example/...` over the real
  network, raising an uncaught `RefResolutionError` the job's `except jsonschema.ValidationError`
  clause does not catch. **Independently confirmed worse than first reported:** the job's own
  directory-walk expects a `schema/examples/<name>/pass|fail/*.json` layout that does not exist on
  disk (the real layout is flat `schema/examples/<name>.example.json` files plus one
  `schema/examples/fail/` dir) — so the job currently reports "checked 0 example file(s)" and
  exits 0 green, a silent false-pass masking the `RefResolutionError` bug rather than crashing red.
  Fix: route the job through `kernel.validate_*`'s own `RefResolver`+store pattern (or call the
  kernel functions directly) instead of reimplementing validation inline, and correct the
  directory-walk to the real flat layout. Add a second CI job that runs
  `python3 -m unittest discover -s tests` with `jsonschema` intentionally uninstalled, to catch
  regressions of MUST-4.
- **Cost:** 2.5h (1.5–2h original estimate + the layout-mismatch fix surfaced by the second
  skeptic vote).
- **Who:** ai.
- **Drift test:** locally reproduce the CI script's exact logic post-fix; confirm it reports
  "checked N example file(s)" with N > 0 (currently N = 0) and passes/fails each fixture
  correctly, not silently. The new `jsonschema`-uninstalled job exits non-zero if MUST-4 is ever
  regressed.
- **Risk if ignored:** the one CI job whose entire purpose is proving the fail-fixtures correctly
  reject invalid data per rules 1–11 currently gives **zero real coverage while reporting
  success** — worse than "crashes on first push," since a green check mark actively lies about
  what was verified.

---

### MUST-6 — Kernel gate rule 12 (`D-LENS-UNSIGNED`): implement, or stop claiming it passed
*(cross-check: items #2, #11 in ARCH_CROSSCHECK.md — corroborated independently by two lenses)*

- **Files:** `schema/claim_card.schema.json`, `kernel/glosa_kernel.py`, `tests/test_kernel.py`,
  `schema/examples/fail/fail_lens_unsigned.json` (new), `reviews/RELEASE_PREP_CHECK.md:217-218`,
  `paper/main_en.md:115`, `paper/main_th.md:114`
- **Exact change (two-phase, the cheap phase is release-blocking on its own):**
  1. **Immediate (≤1h):** `design/FOUNDATION_v0.4.md:593-600` specifies rule 12 as a hard
     validation error; `reviews/RELEASE_PREP_CHECK.md:217-218` and `paper/main_en.md:115` /
     `paper/main_th.md:114` currently state "satisfying §3.3 rule 12" / "kernel rule 12
     compliance" for a rule with **zero** code, schema, or test presence anywhere (confirmed:
     `hypothesis_world`/`lens_translation` declare no `signature`/`lens_ref` property; the
     `allOf` block has 10 clauses covering rules 1,2,3,4,9,11,7,10 and none for rule 12; no
     `fail_lens_unsigned.json` fixture exists). The underlying data is honest today (all 10 real
     claim cards in `paper/claims/` do carry a correctly non-empty `signature`), but the claim of
     *mechanical* compliance is false. Correct the three lines to state plainly: manually
     eyeball-verified, not kernel-enforced.
  2. **Full close (~2.5–3h):** declare `lens_ref`/`signature` as validated schema properties, add
     the `allOf` cross-field clause (same pattern as clauses 2–7), add
     `fail_lens_unsigned.json` + a `tests/test_kernel.py` case.
- **Cost:** ~1h (phase 1, before release) + ~2.5–3h (phase 2, complete the rule).
- **Who:** joint — phase 1 (doc correction) is ai; phase 2 (adding a new hard-enforcement rule to
  the epistemic-integrity gate) is joint, since it changes what the kernel actually blocks and one
  cross-check vote flagged that registering it as a catalogue *disclaimer* (rather than a hard
  `allOf` clause) would misrepresent the spec's own stated intent — the implementation route is a
  founder-reviewable design choice, not a pure mechanical port.
- **Drift test:** `grep -c "kernel rule 12\|satisfying §3.3 rule 12" reviews/RELEASE_PREP_CHECK.md
  paper/main_en.md paper/main_th.md` returns 0 once phase 1 lands (or, once phase 2 lands, the new
  `tests/test_kernel.py::test_rule12_lens_unsigned_fails` case using the fail fixture asserts
  `ok: False`).
- **Risk if ignored:** a specified "hard validation error" gate is reported as passing in both the
  repo's own release-readiness record and its public-facing paper draft while having zero
  enforcement — precisely the overclaim class this methodology exists to prevent, visible on the
  methodology's own flagship artifact.

---

### MUST-7 — Human-identity check on the Approver (MC-01/`independent_check`)
*(cross-check: item #10 in ARCH_CROSSCHECK.md)*

- **Files:** `kernel/glosa_kernel.py` (`mc01_check`, `_mc01_errors_for_card`, `gate_release`),
  `schema/claim_card.schema.json` (`independent_check` properties),
  `schema/evidence_relation.schema.json`, `tests/test_kernel.py`,
  `schema/examples/fail/fail_no_human_approver.json` (new)
- **Exact change:** `mc01_check` today enforces only pairwise **string inequality** of
  `maker_id`/`checker_id`/`approver_id` — a card with `maker_id: "ai-session-A"`, `checker_id:
  "gemini-session-B"`, `approver_id: "codex-session-C"` (three different AI vendors, zero humans)
  reaches `tier: Th_coqc, k_state: K2, status: Approved-for-Live` with `ok: True` and no disclaimer
  naming the missing human, using the real (not degraded) `jsonschema` validator. This is exactly
  the scenario `design/FOUNDATION_v0.4.md:544-546` names as the reason §3.3 exists — worse, since
  the reproduced case is cross-vendor-AI collusion, not solo-AI. Add a human-identity check: the
  cheapest route (surfaced independently in cross-check) requires
  `independent_check.approver_id == card.human_owner` once status advances past `Pending Review`
  — this is already latent in the existing `human_owner` required field and needs no new registry
  file. Add a `fail_no_human_approver.json` fixture and test.
- **Cost:** 5h.
- **Who:** joint — founder must pick the identity mechanism (the `approver_id == human_owner`
  cross-check vs. a fuller `human_registry.json`/`role: human` tag convention — see §7 founder
  decisions); AI implements whichever is chosen.
- **Drift test:** `tests/test_kernel.py::test_no_human_approver_fails` using the new fixture
  asserts `validate_claim_card`/`gate_release` returns `ok: False` for a card whose
  `independent_check.approver_id` does not match a human identity once status ≥ `Pending Review`.
- **Risk if ignored:** the single most safety-critical requirement in the whole design (a human,
  specifically the founder, must be the Approver before `Approved-for-Live`/K2/L5) is enforced
  **nowhere, in any mode** — an all-AI chain can mechanically reach the system's highest trust tier
  today with zero human involvement and zero warning.

---

### MUST-8 — Fix the worked example's stub claim card so it actually validates
*(cross-check: item #8 in ARCH_CROSSCHECK.md)*

- **Files:** `cases/worked-example-cat.md` (~lines 366–400)
- **Exact change:** the Step 7 stub claim card is missing `five_questions` **entirely** (not just
  one sub-field, as an earlier internal review reported) — `tested`/`ai_filled` sit at the top
  level next to `standpoint`/`tier`, not nested inside a `five_questions` wrapper, and
  `claim_type`, `responsible`, `human_owner`, `status` are also absent. `cli/glosa claim validate`
  on the extracted block returns `FAIL` with 5 missing required properties. Replace the block with
  the output of `cli/glosa claim new --shape stub`'s own correct scaffold shape (already
  independently confirmed to `PASS`), adapted with the worked example's own narrative content.
- **Cost:** 1h.
- **Who:** ai.
- **Drift test:** extract the corrected block and run `cli/glosa claim validate <extracted>` —
  confirm `ok: true, verdict: PASS`. Ideally wired as a standing `tests/test_kernel.py` or a small
  `tests/test_docs.py` case that extracts and validates the worked example automatically, so this
  cannot silently re-break on a future doc edit.
- **Risk if ignored:** the one document meant to teach a reader "here is what a real filled card
  looks like" is the one artifact in the whole repo that is actually broken — a reader who copies
  it gets a failing file on their first hands-on attempt and loses trust in the system immediately.

---

### MUST-9 — Wire `glosa release-gate` and `registry.py advance` into `RELEASE_CHECKLIST.md`
*(cross-check: item #20 in ARCH_CROSSCHECK.md)*

- **Files:** `RELEASE_CHECKLIST.md`
- **Exact change:** `RELEASE_CHECKLIST.md`'s R2 "mechanical gates" list and R7 "Tag, publish,
  Zenodo" section never mention `glosa release-gate <manifest>` (the mechanized implementation of
  the release manifest's own adversarial-review dimensions, `kernel.gate_release()`, tested,
  exposed as a CLI subcommand and an MCP tool) or `registry.py advance <id> <stage>` (the
  registry's own lifecycle-state transition, including the terminal `released` stage). Add both as
  explicit, numbered steps in R2 and R7 respectively.
- **Cost:** 1h.
- **Who:** ai.
- **Drift test:** `grep -c "release-gate\|registry.py advance" RELEASE_CHECKLIST.md` ≥ 2.
- **Risk if ignored:** two pieces of machinery this repo built specifically to gate/track a release
  exist, pass their own tests, and are never invoked by the document a solo maintainer is supposed
  to follow step-by-step — already proven to cause real drift, see MUST-10.

---

### MUST-10 — Fix the registry's own state-machine violation; add a permanent invariant check
*(cross-check: item #21 in ARCH_CROSSCHECK.md)*

- **Files:** `registry/RESEARCH_REGISTRY.yaml`, `tools/registry.py`, `scripts/check_repo.sh`
- **Exact change:** `GLS-2026-001` (glosa's own registry entry) sits at `spine_stage: paper_draft`
  with `litreview_manifest_ref: null` and a single history row with no `stub: true` marker — a
  state `registry.py advance` itself refuses to produce (reproduced live: the same command against
  a scratch copy of the same file refuses with `"refusing to advance ... without a
  litreview_manifest_ref"`, and `cmd_new` only ever creates entries starting at `spine_stage:
  problem`). This entry was hand-edited around the tool, bypassing the one mechanism meant to
  enforce the invariant, and nothing currently notices — `check_repo.sh` never parses
  `RESEARCH_REGISTRY.yaml`. Fix: either supply a real `litreview_manifest_ref` or re-log the entry
  honestly via `registry.py advance ... --stub` (which logs `stub: true`). Add a `check_repo.sh`
  step that YAML-parses `RESEARCH_REGISTRY.yaml` and re-validates every entry's `spine_stage`
  against `STAGES_REQUIRING_LITREVIEW`, failing if any entry in a gated stage lacks either a
  non-null ref or a `stub: true` marker.
- **Cost:** 3h.
- **Who:** joint — deciding whether to supply a real litreview reference (needs an actual
  literature-review artifact to point at) or log the gap honestly as `stub: true` (an admission
  about the paper's own state) is a founder call; AI performs the mechanical fix and builds the
  check.
- **Drift test:** the new `scripts/check_repo.sh` step exits 0 across `RESEARCH_REGISTRY.yaml`;
  `python3 tools/registry.py advance GLS-2026-001 review --by ai` (on a scratch copy) no longer
  needs `--stub` to explain the entry's own prior state, or the entry's `stub: true` flag is
  present and check_repo.sh accepts it as such.
- **Risk if ignored:** the registry's own state machine has already been silently bypassed once,
  undetected, in this repo's own data — a public repo whose entire premise is process rigor should
  not ship with its own audit trail already inconsistent with its own tool's stated invariant.

---

### MUST-11 — Add a founder-approval gate to `zenodo_publish_file.py`
*(cross-check: item #23 in ARCH_CROSSCHECK.md)*

- **Files:** `scripts/zenodo_publish_file.py`
- **Exact change:** `scripts/zenodo_deposit.py`'s `publish` subcommand is guarded — it hard-refuses
  without both `--i-have-founder-approval` and a `registry/RELEASE_APPROVAL.txt` containing
  `APPROVED`. `scripts/zenodo_publish_file.py` implements the same class of irreversible action
  (POST a new deposition, then `actions/publish`) with **no such check anywhere** — its only guard
  is a duplicate-title search, and default invocation (no `--draft`) publishes immediately. This
  script has already published four other ANSE.ASIA projects' Zenodo records (T-PHE, Referral
  Governance, SOMA-READ, MOCA) from inside this repo with no independent-check gate — a live,
  already-exercised violation of `AGENTS.md` rule 8 ("No independent check ⇒ no release"), not a
  hypothetical one. Add the identical flag+file gate.
- **Cost:** 2h.
- **Who:** ai (the gate itself is mechanical; it exists precisely so future *use* of the script
  requires a human/joint decision, which is the point of the fix).
- **Drift test:** `python3 scripts/zenodo_publish_file.py <args>` without
  `--i-have-founder-approval` and without `registry/RELEASE_APPROVAL.txt` containing `APPROVED`
  exits non-zero and refuses to publish.
- **Risk if ignored:** an irreversible, externally-visible action (a permanent public DOI record)
  is already reachable with zero independent check, under the founder's own name, from inside a
  public methodology repo.

---

### MUST-12 — Build the Xenon Ledger for real, or demote its hard-fail to advisory
*(cross-check: item #17 in ARCH_CROSSCHECK.md)*

- **Files:** `kernel/glosa_kernel.py:466-467`, `cli/glosa`, `ledgers/`
- **Exact change:** `validate_citation_card()` hard-fails when `status == "SCRAMMED"` and
  `xenon_ledger_ref` is null — but there is no `schema/xenon_ledger.schema.json`, no
  `ledgers/XENON_LEDGER.md` (the directory is not even git-tracked), and no `glosa ledger` CLI
  verb; `cli/glosa:1140` already honestly states in its own output text that the related checks
  are "NOT implemented ... always reported CLEAR." A `SCRAMMED` citation can only satisfy the hard
  requirement by hand-typing an arbitrary non-null string, which defeats the check. Cheap fix:
  demote the requirement to `Open`/advisory at the point of enforcement, with a one-line comment
  explaining why, until the ledger exists for real.
- **Cost:** 1h (demote) or 4h (build the ledger read/write path for real).
- **Who:** joint — loosening a stated "hard validation error" to advisory is a scope/rigor
  decision the founder should ratify, even though the code change is cheap; committing to build
  the ledger instead is a larger scope call belonging in §7.
- **Drift test:** a `citation_card` with `status: SCRAMMED` and `xenon_ledger_ref: null` now
  either (a) passes with an explicit `Open`-tier warning rather than a hard error, or (b) round-trips
  through a real `glosa ledger` read/write path in a new test.
- **Risk if ignored:** a kernel-level MUST-pass condition cites a mechanism that provably does not
  exist anywhere in the repo — self-undermining in a repo whose whole pitch is rigor without
  phantom infrastructure.

---

### MUST-13 — Close the leak-scan and forbidden-words failures before any public push
*(cross-check: items #5, #18, #22 in ARCH_CROSSCHECK.md — three independent lenses, all
corroborating and all finding the live count higher than first reported; do this LAST)*

- **Files:** every file named in the current `[FOUND]` output of both scripts — as of the
  cross-check pass this included, at minimum, `mcp/README.md`, `mcp/logbook.jsonl`,
  `design/HANDOFF_2026-09-04_founding-meeting.md`, `registry/zenodo_state.json`,
  `design/REPO_SPEC_v0.2/0.3/0.4.md`, `design/S14_literature-review-system.md`, `incidents/*`,
  `.glosa/secrets.env.EXAMPLE`, `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` (self-quoting the forbidden
  words as rule text), `sources/CPRMH_v12.txt`, `templates/knowledge/*.md`,
  `scripts/forbidden_words_allowlist.txt`, and — self-reinforcingly — the `reviews/ARCH_*.md`
  files this very review meeting produced (they quote the leaking paths as evidence).
- **Exact change:** `bash scripts/check_leak.sh` and `bash scripts/check_forbidden_words.sh`
  currently exit 1 with 34 and 162 un-allowlisted hits respectively (both counts higher than the
  29/156 an earlier same-day internal review already flagged `[BLOCKING]` — the surface grew, not
  shrank, because new content kept landing without those pre-existing blocking items being
  closed). One cross-check vote flagged the real scope as larger than a simple redact-4-files fix:
  hits split into (a) genuine local-path/UUID/hostname leaks needing redaction, (b) real
  forbidden-word prose needing rewriting, and (c) legitimate false positives —
  `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` quoting the forbidden words *as the rule itself*, and quoted
  external source material (`sources/CPRMH_v12.txt`) — that the current allowlist
  (`scripts/forbidden_words_allowlist.txt`, scoped only to `design/`+`lineage/` by its own stated
  policy) cannot cover without a policy extension. Redact/generalize the real leaks; rewrite the
  real forbidden-word prose; extend the allowlist's policy to explicitly cover self-referential
  rule-text and quoted-source classes, separately from genuine authorial overclaims; decide
  whether `reviews/` ships publicly at all or is excluded/allowlisted as an internal process
  record. Re-run both scripts to exit 0, or leave every remaining hit individually triaged with a
  stated reason per `RELEASE_CHECKLIST.md` R3.
- **Cost:** 4h stated by most votes; one skeptic vote flagged the true scope (given the growing,
  self-referential-reviews problem and the needed `reviews/`-publication policy call) as closer to
  1–2 days. This synthesis carries the higher estimate forward as the realistic number.
- **Who:** joint — AI performs the mechanical redaction/rewriting/allowlisting; the founder must
  approve each specific redaction (per `RELEASE_CHECKLIST.md` R3's own triage step) and rule on
  the `reviews/`-publication policy question, since this is exactly the incident class
  (`PUB-ADVERSARIAL-REVIEW`) that requires an independent, human-visible review before anything
  public-facing ships.
- **Drift test:** `bash scripts/check_leak.sh && bash scripts/check_forbidden_words.sh` both exit
  0 immediately before the actual public push (re-run fresh, not cached from an earlier pass,
  since content keeps growing between now and push time); the SHOULD-tier GitHub branch-protection
  item below turns this into a structural gate rather than a manual step to remember.
- **Risk if ignored:** this is the exact incident shape `PUB-ADVERSARIAL-REVIEW` exists to catch —
  a real 2-week undetected public leak already happened on a sibling ANSE.ASIA repo. Doing this
  last (not first) matters: every other MUST above adds new content that could itself trip these
  scanners, so re-running MUST-13 fresh right before the actual push is the only way to guarantee
  the number really is zero at push time, not merely at review time.

---

## 3. SHOULD — before v0.2

Items already absorbed into a MUST fix above (archiving `v0.2`/`v0.3`, repointing the gate docs,
merging the v0.5 patch) are not repeated here even though some lenses filed them individually at
SHOULD priority — see MUST-1.

| id | change | files | cost (h) |
|---|---|---|---|
| S1 | Append the 9 missing NC-65..NC-73 rows (already fully written in `design/S9_non-collapse-table.md:92-282`) to `methodology/data/non_collapse_table.json` | `methodology/data/non_collapse_table.json`, `design/S9_non-collapse-table.md` | 1.5 |
| S2 | Update `methodology/README.md`'s card index to match `REPO_SPEC_v0.4.md`'s P13/P16 resolution; write the two missing protocol cards `methodology/P16_genre_router.md` and `methodology/P15_blackbox_note.md` (both mechanisms already fully callable, zero prose card) | `methodology/README.md`, `methodology/P16_genre_router.md` (new), `methodology/P15_blackbox_note.md` (new) | 5 |
| S3 | Fix `design/REPO_SPEC_v0.4.md:109-141`'s repo-tree diagram to show real two-digit filenames (`P00_lens.md`…) instead of single-digit | `design/REPO_SPEC_v0.4.md` | 0.5 |
| S4 | Fix `cases/worked-example-cat.md:506,533`'s `D-INDEPENDENCE(level=I0)` param mismatch — catalogue declares `params: []` | `cases/worked-example-cat.md` | 0.5 |
| S5 | Turn on GitHub branch protection requiring `check_leak.sh`/`check_forbidden_words.sh`/`check_repo.sh`/unit-tests to pass before merge to `main` (CI already runs them; nothing currently blocks a merge on failure) | GitHub repo settings | 0.5 |
| S6 | Make `route_genre()` assert its output is a member of `schema/common.defs.json`'s `genre` enum instead of hand-duplicating the genre list | `kernel/glosa_kernel.py:766-900`, `tests/test_kernel.py` | 2 |
| S7 | Add `tests/test_cli.py` invoking every `cmd_*` handler at least once, especially the file-writing `... new` scaffold commands (`self-test`/`demo` never exercise the argparse dispatch layer) | `tests/test_cli.py` (new), `cli/glosa` | 5 |
| S8 | Split FOUNDATION's monotonically-growing history sections (§10 disputes, §13 chair rulings, part of §12) out into an append-only `design/DECISION_LOG.md`, leaving FOUNDATION as only the living spec | `design/FOUNDATION_v0.4.md`, `design/DECISION_LOG.md` (new) | 3 |
| S9 | Write a `MAINTENANCE.md` monthly checklist (re-verify `TOOLCHAIN.md`'s dated claims, run the full test+demo+gate suite, re-grep the MUST-1 drift test, scan `design/` for anything still "specified not applied") | `MAINTENANCE.md` (new) | 2.5 (write) + 0.5/month (run) |
| S10 | Change the CLI's default `--out-dir` to resolve relative to the caller's cwd, or print a loud one-line warning the first time a write lands outside cwd | `cli/glosa`, `cli/README.md` | 2 |
| S11 | Author a one-page Thai-language quickstart (founder-written or founder-reviewed, not machine-translated — this workspace's own rewrite-not-translate rule) walking one household-problem example to a first stub claim card | `README.md` (linked new file, e.g. `QUICKSTART_TH.md`) | 4 |
| S12 | Link `cases/worked-example-cat.md` from `README.md`/`llms.txt`; fix the `the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518)` → `founding-meeting.md` filename citation in the worked example's `session_ref` and in `cases/README.md`'s index | `README.md`, `llms.txt`, `cases/worked-example-cat.md`, `cases/README.md` | 0.5 |
| S13 | Add an optional repo-local `pre-push` git hook running unit tests + the 3 check scripts, documented in `TOOLCHAIN.md` | `scripts/install_hooks.sh` (new), `.githooks/pre-push` (new), `TOOLCHAIN.md` | 2 |
| S14 | Deduplicate the two overlapping Zenodo registry snapshots; keep one canonical file, state which in `registry/README.md` | `registry/zenodo_all_records.json`, `registry/zenodo_all_records_2026-09-04.json`, `registry/README.md` | 0.5 |
| S15 | Document explicitly, in `registry/README.md`, whether glosa is a per-project template (forked once per new problem) or the founder's permanent multi-project hub; if the latter, key `registry/zenodo_state.json` by project id | `registry/README.md`, `scripts/zenodo_deposit.py`, `registry/zenodo_state.json` | 3 |
| S16 | Move `scripts/zenodo_cluster.py` and the whole-bibliography `registry/zenodo_all_records*.json`/`zenodo_clusters.json` out of the public glosa repo into a private/sibling personal-ops tool; keep only `zenodo_deposit.py` (glosa's own deposit) here | `scripts/zenodo_cluster.py`, `registry/zenodo_all_records*.json`, `registry/zenodo_clusters.json`, `registry/downloads_scan_2026-09-04.json` | 3 |
| S17 | Add a `check_version.py` mode (or CI job) that compares `CITATION.cff` and `plugin.json` versions even with no git tag present | `scripts/check_version.py`, `.github/workflows/ci.yml` | 1.5 |
| S18 | Extend `check_leak.sh`'s scan path to cover `obsidian/glosa/blackbox/*` the same way `blackbox/*_DRAFT.md` is already covered; note in `RELEASE_CHECKLIST.md` R3 | `scripts/check_leak.sh`, `tools/obsidian_bridge.py`, `RELEASE_CHECKLIST.md` | 1.5 |
| S19 | *(downgraded from MUST by cross-check — both votes agreed, see §5/D3)* Fix `methodology/README.md`'s stale `REPO_SPEC_v0.3.md` citation and `P13_genre_router.md` mislabel (the file at that path is `P13_literature_review.md`). **Not** the original recommendation's "build or strike `records/`/ledger/xenon-schema" framing — `REPO_SPEC_v0.4.md` self-labels as a design-time spec ("NOT YET ON DISK... a design-time specification"), so that framing is a category error against a doc that already discloses its own forward-looking status | `methodology/README.md:3,5,30,34,41,44` | 1 |
| S20 | *(downgraded from MUST by cross-check — see §5/D2)* Add a `glosa blackbox new` CLI scaffold command mirroring `intake new`/`claim new` — real ergonomic gap, but not release-blocking since `schema/examples/blackbox_note.example.json` already provides a working, tested example and MUST-2 restores the hand-editable template path | `cli/glosa`, `kernel/glosa_kernel.py` (optional scaffold helper), `cli/README.md` | 3 |
| S21 | Independently audit §7.3 Bounded-Judge Law enforcement (`review_report.verdict_tier` must be one of the 6 tiers) the same way this pass audited §3.3 rules 1–12 — not yet checked this pass, could share MUST-4's fail-open risk class or could already be fine | `kernel/glosa_kernel.py`, `schema/review_report.schema.json`, `tests/test_kernel.py` | 2 |

---

## 4. LATER

| id | change | files | cost (h) |
|---|---|---|---|
| L1 | Add a `tests/test_kernel.py` assertion that `_TIER_STRENGTH`/`_INDEPENDENCE_ORDER` key-sets equal `schema/common.defs.json`'s enum value-sets (low urgency — in sync today, nothing would catch future desync) | `tests/test_kernel.py`, `kernel/glosa_kernel.py` | 1 |
| L2 | Correct `design/FOUNDATION_v0.4.md`/`REPO_SPEC_v0.4.md`'s repeated reference to a standalone `paper/BLACKBOX_NOTE_APPENDIX.md` that was never built that way (it's inline in `paper/main_en.md:159`) | `design/FOUNDATION_v0.4.md`, `design/REPO_SPEC_v0.4.md`, `paper/main_en.md`, `paper/main_th.md` | 0.5 |
| L3 | Name the LibreOffice-only-verified-Thai-rendering single point of failure explicitly in `TOOLCHAIN.md` with a stated fallback/repair plan | `TOOLCHAIN.md` | 0.5 |
| L4 | Comment `mcp/glosa_mcp_server.py:50`'s pinned `PROTOCOL_VERSION` with where to check for the next MCP spec revision | `mcp/glosa_mcp_server.py:50` | 0.5 |
| L5 | Add a documented minimal 4-command path (`intake new` → `claim new --shape stub` → `claim validate` → `lit new`) ahead of the full `--help` listing | `cli/glosa`, `cli/README.md` | 3 |
| L6 | State explicitly in `README.md`/`plugins/glosa/README.md` that the intended non-coder mode is to talk to an AI with the glosa plugin installed (which drives the CLI on their behalf), not to open a terminal | `README.md`, `plugins/glosa/README.md` | 1 |
| L7 | Independently audit whatever §7.3 audit (S21) finds; not yet scoped | `kernel/glosa_kernel.py`, `schema/review_report.schema.json` | 2 |
| L8 | Stop tracking compiled binary output (`paper/latex/main.pdf`) and duplicate-format PDF+txt source pairs; regenerate on demand, keep PDFs as external references | `.gitignore`, `paper/latex/main.pdf`, `sources/*.pdf` | 1 |
| L9 | Fold the unused `disagreement_ledger_entry.schema.json` and the never-built Xenon Ledger split into one schema with a `kind` discriminator until real usage justifies two | `schema/disagreement_ledger_entry.schema.json`, `design/REPO_SPEC_v0.4.md` | 3 |
| L10 | Rename `dist/manifest.json` (render.py `deliver-manifest` output) to `delivery_index.json`, or add explicit cross-references distinguishing it from `release_manifest` in every doc/skill mentioning either | `tools/render.py`, `plugins/glosa/skills/glosa-deliver/SKILL.md`, `cli/README.md` | 1 |
| L11 | Implement `kernel.advise()` (both `cli/glosa`'s `cmd_advise` and `mcp/glosa_mcp_server.py`'s dead `glosa_advise` tool currently diverge — one works, one always errors) or mark the MCP tool not-yet-implemented; decide whether `GLOSA_K1_K2_LEDGER.md` gets built (aggregating `records/advisory/*`) or the spec is corrected to say the ledger is manual-only | `kernel/glosa_kernel.py`, `cli/glosa`, `mcp/glosa_mcp_server.py`, `design/REPO_SPEC_v0.4.md` | 4 |

---

## 5. DROPPED — with the skeptics' reasons (kept for the record, dissent never erased)

### D1 — Was this actually dropped? (anomaly, disclosed)

**Usability R1** ("Fix `templates/knowledge/blackbox_note.yaml` so it is valid YAML + add a
YAML-parse check") was formally marked `REFUTED` by the cross-check pass — **with an empty
reasons array**, i.e. no skeptic vote text was recorded against it at all
(`reviews/ARCH_CROSSCHECK.md`, Part 2, item D1). This synthesizer does not treat an empty vote as
a substantive rebuttal: the underlying lens finding (`ARCH_usability.md` F1) is
`finite_diagnostic`, directly reproduced, unrebutted by any other vote or lens in the record, and
costs 1h to fix. It has been **restored and kept as MUST-2** in §2 above. This is a synthesizer
override of the cross-check's formal disposition, disclosed here rather than silently applied —
the AI assistant/the founder should confirm or reverse it explicitly (see §7).

### D2 — Downgraded to SHOULD: `glosa blackbox new` CLI scaffold command

**Usability R2.** Both cross-check votes agreed the underlying gap is real (no `blackbox`
subcommand exists in `cli/glosa`) but refuted the MUST-priority risk framing: a real, tested
worked example already exists (`schema/examples/blackbox_note.example.json`, exercised by both
`./cli/glosa demo` and `tests/test_kernel.py`'s `BlackboxNoteTest`), so "no working example to
copy" is false — and combined with MUST-2 restoring the hand-editable template path, a solo
maintainer has two working, non-CLI routes to a valid Blackbox Note before this scaffold is ever
built. A dedicated authoring skill (`plugins/glosa/skills/glosa-blackbox-note/SKILL.md`) is also
already the documented production path for this specific artifact type, which — unlike
`problem_card`/`claim_card` — is an append-only verbatim transcript, not a one-shot form a
scaffold naturally fits. Both votes: "the 3h feature is still worth doing... downgraded rather
than dropped." Carried forward as **S20**.

### D3 — Downgraded to SHOULD: "reconcile `REPO_SPEC_v0.4.md` against disk"

**Efficiency R4.** Both cross-check votes agreed on the underlying facts (`AI_START_HERE.md`,
`codemeta.json`, `GLOSA_K1_K2_LEDGER.md`, `records/`, several named schema files all absent from
disk; `methodology/README.md` cites the superseded `REPO_SPEC_v0.3.md` and mislabels the
`P13`/`P16` card split) but both refuted the "build or strike" MUST framing: `design/
REPO_SPEC_v0.4.md:29-30` explicitly self-labels as "NOT YET ON DISK... a design-time
specification" — it is a forward roadmap, not a build-status document, so there is nothing to
"reconcile" in the release-blocking sense; spending hours building `records/` trees or
`schema/xenon_ledger.schema.json` to match a doc that already discloses it describes unbuilt
future work would itself be the premature-infrastructure move this methodology's own "rigour
without infrastructure" ethos argues against. The narrower, real, cheap fix (the
`methodology/README.md` citation + P13/P16 label correction) survives and is carried forward as
**S19**.

### D4 — Split vote, folded into MUST-1: "merge `FOUNDATION_v0.5_PATCH.md` into `v0.4.md`"

**Efficiency R2.** One cross-check vote refuted MUST priority for this specific narrow action:
"nothing in README.md/RELEASE_CHECKLIST.md/kernel/CLI reads FOUNDATION_v0.4.md at runtime — it's
human-consulted prose... an unmerged patch with an honest 'Dr, specified not applied' tier is a
correctly-tiered readout, not a release-blocking defect" (adjusted: SHOULD). The other vote kept
MUST, citing the compounding single-point-of-truth hazard of two live foundation documents with no
merge commit. This synthesizer folded the action into MUST-1's bundle (which five other,
unanimous, independent votes across five lenses established as MUST on stronger and broader
grounds — the citation-drift chain, not just the unmerged-patch question) rather than resolving
the tie unilaterally. The dissent is preserved here for whoever sequences MUST-1's sub-steps: if
time-boxed, the patch-merge could reasonably be sequenced after the higher-agreement repoint/archive
steps rather than gating them.

---

## 6. Sustainability contract — one page, for a solo maintainer

**Monthly ritual (~1–2h/month; formalize as `MAINTENANCE.md`, item S9):**
1. Run, in order, and read the real exit codes (not through `tail`): `python3 -m unittest discover
   -s tests`, `./cli/glosa self-test`, `./cli/glosa demo`, `bash scripts/check_repo.sh`,
   `bash scripts/check_leak.sh`, `bash scripts/check_forbidden_words.sh`,
   `python3 tools/render.py check`. Everything green, or every `FAIL` individually triaged, before
   doing anything else that session.
2. Re-run MUST-1's drift-test grep (canonical-spec-pointer check) — confirm no file has drifted
   onto a stale `FOUNDATION_v0.\d` string since last month.
3. Re-check `TOOLCHAIN.md`'s dated "verified" claims by actually re-running the probes
   (LibreOffice/`xelatex`/`lualatex`), not by trusting the date on the page.
4. Scan `design/` for any file still saying "specified, not applied" / "Dr, unmerged" — if a
   patch has sat unmerged for more than one review cycle, merge it or explicitly mark it
   abandoned; never let a third patch stack up.
5. Once MUST-10 lands, re-run its `check_repo.sh` registry-invariant step against
   `RESEARCH_REGISTRY.yaml`.

**What never to touch without an independent check (this repo's own maker-checker discipline,
`AGENTS.md` rule 3):**
- `schema/*.schema.json` — a change here ripples to kernel, CLI, MCP, templates, and paper at
  once; one-fact-one-home means one silent edit here breaks everything downstream.
- `kernel/glosa_kernel.py`'s `validate_*`/`gate_release`/`mc01_check` functions — the same AI
  session that drafts an edit here has no standing to certify it; a second, independent pass is
  required before it merges, exactly like every claim card the kernel itself gates.
- The FOUNDATION spec's §3.3 kernel gate rules — this is the epistemic-integrity backbone; a rule
  change needs a recorded chair ruling, not a quiet edit during an unrelated task.
- `registry/RELEASE_APPROVAL.txt` — only the founder writes `APPROVED` into this file.

**Freeze rules for `design/`:**
- Exactly **one** FOUNDATION file is "current" at a time. The moment a new synthesis pass starts,
  the prior version moves to `design/archive/` in the **same commit** that introduces the new one
  — never let two live simultaneously (this is the single root cause behind the most-corroborated
  finding in this whole review, MUST-1).
- A `_PATCH.md` file may exist for **at most one review cycle** before it is merged or explicitly
  abandoned — no patch carries forward past a second synthesis pass.
- History sections (chair rulings, disputes resolved, "honest edges — what was NOT read") move out
  of the living FOUNDATION file into `design/DECISION_LOG.md` (append-only) once FOUNDATION
  crosses ~1,200 lines (S8) — the point is to keep the file a solo scholar can hold in their head
  during ordinary editing, not to hide history.

**Size limits (mechanically enforceable, not aspirational):**
- `design/` (excluding `archive/`) holds at most 2 live FOUNDATION-class documents at any time:
  the current spec, and at most one in-flight patch.
- No single spec file exceeds ~1,800 lines before its history must split out —
  `FOUNDATION_v0.4.md` is already at 1,623 lines and has grown ~260–360 lines every synthesis
  pass; left unchecked, this compounds every future reader's "read the entire prior version in
  full" cost, which is each version's own stated synthesis method.
- `registry/` holds exactly one canonical Zenodo full-corpus snapshot file; a dated snapshot may
  coexist for at most one release cycle before deletion or archival (S14).
- No compiled binary artifact is tracked in git if the source it compiles from is also tracked —
  pick one form per document, regenerate the other on demand (L8).

---

## 7. Founder decisions required

These cannot be resolved by an AI session alone — each is either a content/legitimacy call about
the FOUNDATION spec itself, an irreversible/public action, or a scope decision about how much
infrastructure this "rigour without infrastructure" methodology actually wants to carry:

1. **Ratify `design/FOUNDATION_v0.5_PATCH.md`'s content** before it is merged into v0.4 as
   canonical (MUST-1) — the patch text is fully specified; what's needed is the founder's sign-off
   as chair, recorded as a chair ruling, not a silent AI merge.
2. **Confirm or reverse this synthesis's override** of the cross-check's `REFUTED`-with-empty-reasons
   disposition on the `blackbox_note.yaml` YAML fix (MUST-2/D1, §5). The evidence favors keeping
   it as MUST; the formal record shows a data gap, not a rebuttal — the founder should see this
   flagged explicitly rather than have it pass silently either way.
3. **Pick the human-identity mechanism** for MC-01 (MUST-7): the cheap
   `independent_check.approver_id == card.human_owner` cross-check, vs. a fuller
   `human_registry.json` allowlist, vs. a lighter `role: human` self-asserted tag on every
   identity string. Different rigor/cost tradeoffs; the founder is the human this rule exists to
   name, so the founder should choose how it names them.
4. **Decide kernel rule 12's timeline** (MUST-6): full implementation before v1, or the honest
   caveat-only fix now with full implementation deferred to v0.2 — affects the release date.
5. **Decide glosa's own identity** (S15): a per-project template forked once per research problem,
   or the founder's permanent multi-project hub. This also determines whether `zenodo_cluster.py`
   and the whole-bibliography registry files (S16) belong in this *public* repo at all, or should
   move to a private sibling tool — a visibility decision, not just an engineering one.
6. **Approve each specific redaction** in MUST-13's leak/forbidden-words triage, and rule on
   whether `reviews/` (this very review folder) ships publicly at all, given it is now itself a
   repeat source of leak-scan hits by quoting the paths it's reporting on.
7. **Rule on the Xenon Ledger** (MUST-12): demote the hard-fail to advisory now, or commit to
   building the real ledger — a scope decision about how much of the spec's aspirational
   infrastructure this release actually carries.
8. **Approve the archive mechanics** for `FOUNDATION_v0.2.md`/`v0.3.md` and
   `REPO_SPEC_v0.2.md`/`v0.3.md` (git-mv to `design/archive/` vs. an in-place SUPERSEDED banner) —
   a call about how the repo's own history should read to a future visitor.

---

## 8. Tier tags and honest edges — what no lens executed

- Every `finite_diagnostic` claim in this synthesis is **inherited**, not re-run — this document
  itself is `Dr`-tier synthesis over six lens reports and one cross-check ledger; no command in
  this file was independently re-executed by the synthesizer against the repo.
- Six lenses reviewed commit `233b0ca`; by the time this synthesis was written, HEAD had advanced
  one commit to `043225f` (an unrelated Blackbox Log feature). Nothing above was re-verified
  against `043225f` — the hit counts, line numbers, and file states cited throughout are as of
  `233b0ca`/the cross-check pass's own re-runs (mostly on `043225f`, per several votes'
  disclosures), not a fresh check by this synthesizer.
- `.github/workflows/ci.yml` has **never actually executed** against this content — the repo has
  not been pushed to a remote where Actions runs. Every claim about CI behavior in MUST-5 is from
  reproducing the job's exact commands locally, not from an observed Actions run. This is a real,
  disclosed gap: the fix's actual correctness on GitHub's own runners is unverified.
- No lens attempted a literal second, blind AI-vendor session cloning this repo cold — the
  usability lens's "fresh AI" framing is `Dr`-extrapolated from one session's own walkthrough
  (with genuine timed commands), not an independently replicated cold start by a different vendor.
- §7.3 Bounded-Judge Law enforcement (`review_report.verdict_tier`) was explicitly flagged as
  **not audited this pass** by the integrity lens — carried forward as S21/L7. Whether it shares
  MUST-4's fail-open risk class is genuinely unknown, not merely unstated.
- No lens read `mcp/test_mcp_stdio.py`'s actual coverage depth, or `blackbox/`'s / `.glosa/`'s few
  tracked files, line-by-line — named in the efficiency lens's directory census but not audited.
- The lifecycle lens's Obsidian-bridge finding (F10) is from `--dry-run` output and `.gitignore`'s
  stated intent only — no lens ran a real, vault-configured sync to observe actual behavior.
- Every cost estimate throughout is `Dr`-tier solo-maintainer-hour judgment from the reviewing AI
  sessions, not measured against an actual timed fix. Several cross-check votes explicitly flagged
  specific estimates as likely low (MUST-1 closer to 4h than 3h once two-tier design is accounted
  for, per one vote; MUST-13 closer to 1–2 days than 4h once the self-referential-reviews problem
  is counted, per another) — this synthesis carried the higher of any disputed estimate forward
  where a vote flagged it, but none of these were independently re-timed.
- This document's own §5/§7 override of the cross-check's `REFUTED`-with-empty-reasons item (D1)
  is itself a `Dr`-tier judgment call by the synthesizer, disclosed rather than smoothed over —
  see item 2 in §7.

---

*Synthesized from `reviews/ARCH_structure.md`, `ARCH_sustainability.md`, `ARCH_usability.md`,
`ARCH_integrity.md`, `ARCH_efficiency.md`, `ARCH_lifecycle.md`, and `reviews/ARCH_CROSSCHECK.md`.
No forbidden words used. No external/institutional validation proposed anywhere as what would
make this repo's architecture, or this review, legitimate.*
