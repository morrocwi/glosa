# RELEASE_CHECKLIST.md

> Tier: Dr. This is a procedure, not a claim. Every box on this list is a
> readout of a check someone actually ran — never check a box because it
> "should" pass.

Public push of any part of this repo (a `git push` to the public GitHub
remote, a Zenodo deposit, an Artifact publish, or handing a file to anyone
outside this workstation) is gated on this checklist. **No independent
check, no release** (`AGENTS.md` rule 8, `maker-checker-gate`).

K-state at a release is whatever the kernel's independence math allows — **today K0 (public working release, no independent check)**; K1 requires a cross-vendor I3 route, K2 an external human (I5).
Say so explicitly in the release notes, the Zenodo description, and any
announcement: *"K0 public working release (not peer reviewed; no independent check yet). Not peer reviewed. No I5
(reproduced-by-an-independent-outside-party) check exists yet for this
material."* Never round the K-state up to a stronger-sounding state to make a
release sound more finished than it is.

---

## R1 — Restate the thesis before judging

Before reviewing anything, the reviewer (maker ≠ checker, `AGENTS.md` rule 3)
writes one paragraph, in their own words, of what this release claims and
does not claim. If they cannot do this from reading the release material
alone, the release is not ready — fix the material, not the reviewer's
understanding of it via a side conversation.

- [ ] Reviewer's restatement written down (in the PR description or a
      `reviews/` note).
- [ ] Restatement checked against `CLAIM_BOUNDARY.md` and `NON_CLAIMS.md` —
      does it match, or does the release imply more?

## R2 — Mechanical gates (CI, must be green)

- [ ] `scripts/check_repo.sh` — PASS (required files, no tracked LaTeX
      build artifacts, JSON parses, `.glosa/secrets.env` and
      `.glosa/author_profile.json` not tracked).
- [ ] `scripts/check_version.py` — PASS (git tag == `CITATION.cff` ==
      `.zenodo.json` == `codemeta.json` == `plugin.json`, wherever each
      exists).
- [ ] `scripts/check_forbidden_words.sh` — PASS (no un-allowlisted
       (any word on the priority-language list enforced by scripts/check_forbidden_words.sh).
- [ ] `scripts/check_leak.sh` — PASS, or every `[FOUND]` line individually
      triaged (see R3).
- [ ] `scripts/check_spec_pointers.sh` — PASS (no tracked doc points at a
      stale `FOUNDATION_v0.[234]`/`REPO_SPEC_v0.[234]` outside `design/`
      and `lineage/`; every non-`[planned]` path in
      `design/REPO_SPEC_v0.5.md` still exists on disk).
- [ ] `scripts/check_toolchain.sh` — PASS (the rendering/validation
      toolchain `TOOLCHAIN.md` claims is actually installed/enabled).
- [ ] `python3 -m unittest discover -s tests` — PASS, if `tests/` exists.
- [ ] `python3 scripts/validate_examples.py` — PASS (every
      `schema/examples/*.json` validates against its schema; every
      `schema/examples/fail/*.json` correctly fails).
- [ ] `./cli/glosa self-test` and `./cli/glosa demo` — both PASS.
- [ ] `python3 tools/registry.py check` — PASS (every
      `registry/RESEARCH_REGISTRY.yaml` entry's `spine_stage` is consistent
      with the state-machine invariants `registry.py advance` itself
      enforces — catches a hand-edited entry that bypassed the tool, see
      `ARCHITECTURE_REVIEW_v1.md` MUST-10).
- [ ] `./cli/glosa release-gate <release_manifest.json>` — exit 0
      (PASS/PASS_WITH_LIMITS). This is the mechanized implementation of
      this checklist's own adversarial-review dimensions
      (`kernel.gate_release()`); a non-zero exit (1 FAIL, 2 HUMAN_REVIEW, 3
      ROLLBACK) means this checklist is not actually satisfied yet,
      whatever the boxes above say — fix the underlying finding, do not
      re-run the manifest until it happens to pass.
- [ ] LaTeX build job green, if `paper/latex/main.tex` exists.

CI green is necessary, never sufficient — it is a mechanical readout of a
fixed pattern list, not a review.

## R3 — Privacy / security leak triage (mandatory, own step even if R2 was green)

`check_leak.sh` finding zero hits is not proof of no leak — only proof the
current denylist found none. Before every public push:

- [ ] Re-read every file touched since the last release with fresh eyes,
      specifically hunting for: local usernames/home paths, internal IPs,
      session/PR/ticket IDs, internal org/vendor names, private-repo path
      fragments, anything that reads like an internal working note pasted
      into a public-facing file.
- [ ] Every `[FOUND]` line from `check_leak.sh` is individually resolved:
      redacted, generalized, or (rarely) confirmed a false positive with a
      one-line reason recorded in the PR.
- [ ] Every `[EMAIL]` line from `check_leak.sh` is checked: is it the
      author's own intended public line, or something else that must come
      out?
- [ ] `blackbox/` DRAFT dialogue files are NOT pushed as-is unless they have
      gone through the Blackbox Note curation step (`methodology/P15_*`) —
      a DRAFT is a working record, not a public artifact.

## R4 — Content review (independent of the maker)

- [ ] Tier tags present and honest on every claim (`Th_coqc` /
      `finite_diagnostic` / `fit_calibrated` / `Dr` / `definition` / `Open`)
      — nothing stated as executed unless the reviewer can see the actual
      run output, not a description of a run.
- [ ] No forbidden words outside an allowlisted historical mention
      (`scripts/forbidden_words_allowlist.txt`, `design/`/`lineage/` only).
- [ ] Every comparison to other work is same/different/cited — never framed
      as a priority or legitimacy claim.
- [ ] No external/institutional validation framed as a legitimacy lever
      (`EPIS-KNOWLEDGE-VALIDATION`) — internal Th_coqc/independent-review
      discipline is the standard, not outside recognition.
- [ ] Every Blackbox Note in the release carries: verbatim founder lines
      (unedited, untranslated in place), a `lens_used` block with display
      string `"Readout Universe — Yaoharee Lahtee"`, the lens DOI and repo
      URL cited in the surrounding document, and a hypothesis signature
      line under every hypothesis.
- [ ] People referred to by role, not name, throughout (founder's own name
      is the sole allowed exception, as author).
- [ ] Thai content is rewritten for the release, not machine-translated
      from the English draft (or vice versa).

## R5 — Independence Ladder check

- [ ] The reviewer running R1–R4 is not the same session/agent that
      authored the changed content (maker ≠ checker, `AGENTS.md` rule 3).
- [ ] The independence class actually achieved (I0–I5) is recorded honestly
      — do not round up. At K0/K1, an I5 (reproduced by an independent outside
      party) check almost certainly does not exist yet; say so rather than
      implying it does.
- [ ] Any bounded I2+I4 exception in use is named explicitly, not silently
      substituted for a fuller check.

## R6 — Founder approval (human gate, cannot be delegated to AI)

- [ ] Founder (Yaoharee Lahtee) has read the actual diff/release content
      being pushed — not a summary of it — and approved it explicitly.
- [ ] Any open dissent or unresolved reviewer finding is either fixed or
      explicitly accepted by the founder in writing (PR comment, DECISIONS
      row) before merge — never silently dropped.
- [ ] `DECISIONS.md` / `cpg/research/coordination/DECISIONS.yaml` (if this
      release constitutes a decision) has a row for this release.

## R7 — Tag, publish, Zenodo

- [ ] Version bumped consistently in `CITATION.cff`, `.zenodo.json`,
      `codemeta.json`, and `plugin.json` (wherever each exists) — verify
      with `scripts/check_version.py` BEFORE tagging, not after.
- [ ] `CHANGELOG.md` entry added, tier-labeled, describing what actually
      changed (no forward-looking claims about what the release "enables").
- [ ] `python3 tools/registry.py advance <id> <stage> --by human|ai|joint
      [--stub] [--litreview-manifest-ref REF]` — this release's registry
      entry (`registry/RESEARCH_REGISTRY.yaml`) is advanced to the stage
      this release actually reaches, through the tool (never hand-edited —
      that is exactly the MUST-10 state-machine violation this checklist
      exists to prevent going forward). Use `--stub` and record why,
      explicitly, if the real prerequisite (e.g. a litreview manifest ref)
      is not yet available — an honest `stub: true` row beats a silent
      hand-edit.
- [ ] Git tag `vX.Y.Z` created on the exact commit reviewed in R1–R6 (no
      drift between the reviewed commit and the tagged commit).
- [ ] Push to the public GitHub remote.
- [ ] Zenodo deposit created via the **GitHub-integration route** (preferred
      — Zenodo watches the GitHub repo and mints a DOI automatically on a
      new GitHub Release; this keeps the deposit's metadata in lockstep
      with `.zenodo.json` without a separate manual upload step). Manual
      fallback only if the GitHub integration is unavailable:
      `python3 scripts/zenodo_deposit.py publish --i-have-founder-approval`
      — refuses without both that flag AND `registry/RELEASE_APPROVAL.txt`
      containing `APPROVED` (the founder-approval gate, `AGENTS.md` rule
      8/MUST-11). If used, its metadata must be hand-verified against
      `.zenodo.json` before finalizing. **`scripts/zenodo_publish_file.py`
      is a different, more general script (used for other ANSE.ASIA
      projects' deposits) — it does NOT carry this same founder-approval
      gate as of this pass; do not use it for a glosa release until MUST-11
      closes that gap.**
- [ ] Deposit description / GitHub Release notes explicitly state the K-state (K0 today)
      public-provisional status (see wording above) and link
      `CLAIM_BOUNDARY.md`.
- [ ] `related_identifiers` in `.zenodo.json` still correctly list every
      direct ancestor DOI (verify, do not assume the file is current).

---

## After release

- [ ] Confirm the DOI resolves and the Zenodo record's rendered metadata
      matches `.zenodo.json` (Zenodo sometimes re-derives fields — check the
      live record, not just the file that was pushed).
- [ ] Add the minted DOI to `CITATION.cff` in the NEXT working commit
      (never edit a tagged release's `CITATION.cff` in place after the tag
      — that would break the tag==file version-lock this checklist just
      verified).
- [ ] If any R3/R4 finding was accepted-with-limits rather than fixed,
      confirm it is visible in `CLAIM_BOUNDARY.md` or `NON_CLAIMS.md`, not
      buried only in a PR comment.
