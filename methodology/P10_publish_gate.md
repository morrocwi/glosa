# P10 — Publish gate (PUB-ADVERSARIAL-REVIEW, R1–R7)

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction; AI drafted this card,
> narrating `FOUNDATION_v0.5.md` §7.4 and this workspace's own `PUB-ADVERSARIAL-REVIEW` standing
> rule. Comparison language is same/different/cited only.

## id

`P10`

## Rule

Nothing leaves this repo's hands toward a stranger — a `git push` to a public remote, a public
artifact/page, a Zenodo deposit, a message sent externally — without a `PUB-ADVERSARIAL-REVIEW`
pass run first, by an identity distinct from the one that produced the content, across all seven
dimensions:

- **R1 — Leak scan.** Grep for local usernames/home directories, internal IPs/hostnames, private-
  repo paths, internal session/PR/ticket IDs, any `rl`-shelf internal identifier (Zotero key,
  Paperless doc id, local file path — `S14` §4's boundary contract), and anything reading like an
  internal working note pasted into a public file.
- **R2 — License coverage.** Every file that should carry/inherit the repo's single CC BY 4.0
  license actually does; no file claims a different, unreconciled license silently.
- **R3 — Tier fidelity.** Every `tier`/`k_state`/`independence_class` on the surface matches what
  the underlying evidence actually supports — no quiet upgrade because the prose reads confidently.
- **R4 — Citation accuracy.** Re-runs `P13`'s own accuracy gate (`litreview_manifest.gate.
  accuracy_gate`) independently, never grandfathering a manifest that passed at freeze time — a
  citation may have been SCRAMMED since.
- **R5 — Anchor-preservation audit.** Every `PRESERVE_EXACT`/`PRESERVE_FUNCTION` row this artifact
  touches (`lineage/`) still holds; nothing was silently weakened while drafting.
- **R6 — Overclaim/register scan.** Full-text scan against the contaminated-concept table
  (Appendix C) and this repo's priority-claim word list (the terms this repo's own gate excludes
  under `EPIS-KNOWLEDGE-VALIDATION`'s no-priority-contest stance, and the "we took/borrowed this
  from them" framing barred except where a human explicitly instructed adoption) — any hit is a
  hard fail, not a style note.
- **R7 — Completeness.** Every `\claimref{}`/field the artifact points at actually resolves (no
  dangling reference, no promised appendix missing) — the same discipline `FOUNDATION_v0.5.md`
  §12 applies to its own document, applied here to the artifact being published.
- **R8 — Human Mastery Gate.** (`hu.mastery-gate-wired`, HU-1, `design/SESSION_ARCH_v0.4_SPEC.md`
  §11.1, `methodology/P17_human_mastery_gate.md`.) A linked `human_mastery_gate.yaml`
  (`schema/human_mastery_gate.schema.json`) must have `gate_status != NOT_READY` for any L3+
  artifact — `PASS_WITH_NAMED_GAPS` is a legal, honest outcome. An arXiv-paper-genre artifact
  using `templates/paper/arxiv-twocol/main.tex`'s inline `Gate status:` line satisfies R8 without
  a separate file. **Failing control — MUST fire:** a non-Paper-genre L3+ claim card with no
  `human_mastery_gate.yaml` linked → `BLOCKED: NO_MASTERY_GATE_LINKED`. **MUST NOT fire:** an
  arXiv-paper-genre artifact with `Gate status: PASS` already filled. Per `P17`, R8 is not a
  vertical-authority certification layer (`EPIS-KNOWLEDGE-VALIDATION`) — it is this repo's own
  maker≠checker≠approver discipline applied to the human's own unaided defense of their own
  claim.

## Why / incident

Founder ruling, 2026-08-03: a real pre-publication adversarial gate on a sibling public research
repo in this workspace, run for the first time, caught on its *first* run — after many prior
polish/coherence passes on the same files had missed it — code the repo's own LICENSE had already
declared must-be-removed, sitting live on public GitHub for two weeks undetected, plus local-
filesystem-path/username leaks in files presented as public, a license-vs-file-coverage gap, and
self-contradicting claims inside the README's own citation block. None of the prior passes were
framed as "we are about to let a stranger see this" — that framing, specifically, is what
surfaced the finding; a general quality audit did not. This is why R1–R7 above are a named,
ordered checklist rather than a general "looks good" pass.

## Inputs → outputs

- **Inputs:** the artifact as it would actually appear to the outside party (the rendered page,
  the pushed diff, the deposited files) — not a description of it; the repo's LICENSE and its
  file-coverage expectation; the contaminated-concept table and forbidden-word list; the
  `litreview_manifest.yaml` and `lineage/` files it depends on.
- **Outputs:** a `review_report` with `verdict_tier` and a per-dimension `PASS | PASS_WITH_LIMITS |
  FAIL | HUMAN_REVIEW` result for each of R1–R7; where any dimension is `FAIL`, the publish action
  does not occur until the finding is resolved or explicitly accepted by the human Approver
  (`FOUNDATION_v0.5.md` §7.4).

## Gate

**K1 semantics, stated exactly (per `FOUNDATION_v0.5.md` §7.1's L3/L5 reconciliation):** a card
checked at independence class I3 (or the bounded I2+I4 exception, §4.2) and approved by the human
Approver may sit on public `main`, cited, dated — this is K1, **public-provisional, never K2**.
Nothing in the publish gate substitutes for the I5-human requirement that alone opens K2/K3
(`P6`); passing R1–R7 licenses **publication at the artifact's own honest K-state**, it never
raises that K-state. `PUB-ADVERSARIAL-REVIEW` is required in addition to, not instead of, the
`independent_check`/MIMCG gate (`P6`) the artifact must already have passed to reach its stated
tier — R1–R7 check the *publication act itself* (leak, license, register, completeness), while
`P6` checks the *claim's own evidentiary standing*. Both must clear. **PR-only:** every publish to
the public remote goes through a pull request reviewed by a distinct identity; no direct push to
the public `main` branch, ever, regardless of how small the change looks.

## Human / AI split

Human: is the non-delegable Approver — the sign-off to publish is a release-authority function,
never satisfied by an AI's own "looks clean" (`FOUNDATION_v0.5.md` §7.1 L3 row). AI: may run the
mechanical parts of R1 (grep-based leak scan), R2 (file-coverage check), R6 (contaminated-concept/
forbidden-word scan), and R7 (reference-resolution check) — but the review must be a **different**
session/context from the one that authored the content (`NC-28`/`NC-29`), and R3/R4/R5's semantic
judgments (does this tier match the evidence, does this citation still hold, does this preserve
the anchor) require a route at independence class ≥ I2, with I3+ for anything reaching L3 public.

## Disclaimers

`D-K-STATE` (every public surface states its K-state), `D-DVP-NOT-K2` (public language never
implies K2/K3/"verified/certified" while the review tops out below I5), `D-REVISION-LIVE`
(CHANGELOG/`reviews/` updated), `D-CANDIDATE-STATUS` (anything not yet through an I4/I5 check),
`D-NO-VERTICAL-AUTHORITY` (the gate is an internal independent check, never framed as seeking
outside legitimacy).

## NC pairs

`NC-03` Legitimacy ≠ Truth (horizontal & vertical) · `NC-28`/`NC-29` maker ≠ checker; AI generator
≠ AI reviewer of the same commit · `NC-32` DVP ≠ K2 · `NC-33` K1 ≠ Certification · `NC-34` No
independent check ⇒ No K2 / No independent check ⇒ No release (two distinct gates) · `NC-59`
AI-candidate output ≠ Verified citation.

## Not-do

- Do not push directly to the public `main` branch.
- Do not run the adversarial pass in the same session/context that authored the artifact and call
  it independent.
- Do not treat a manifest's freeze-time `PASS` as still valid at publish time without re-running
  R4.
- Do not let a passing R1–R7 result raise the artifact's `k_state` — publication and K-state
  advancement are separate gates.
- Do not propose "submit for outside review/peer review" as a substitute for R1–R7 or for the I5
  human check K2 actually requires (`EPIS-KNOWLEDGE-VALIDATION`).
- Do not publish while any `mandatory: true` disclaimer trigger is active and its id is absent
  from `disclaimers_emitted`.

## Tier

Dr (specified; independently unreviewed).
