tier: Dr (specified; independently unreviewed)

# readout_universe license leak — 2026-08-03

## Source
the internal survey (local, not public) §D, `PUB-ADVERSARIAL-REVIEW` origin note in the ANSE.ASIA gate files (also
carried in `~/.claude/CLAUDE.md`'s `PUB-ADVERSARIAL-REVIEW` node, reproduced here as the founder
ruling that the standing rule cites): "a real pre-publication adversarial gate on
`readout_universe` caught, on the FIRST such gate ever run, code the repo's own `LICENSE` had
already declared proprietary/must-be-removed sitting live on public GitHub for **two weeks**,
undetected — plus multiple local-filesystem-path/username leaks in 'public' docs, a
license-vs-README file-coverage gap, and self-contradicting claims in the README's own citation
block."

## What happened [tier: finite_diagnostic (documented)]
`readout_universe` is a public repository (MIT, with a stated set of `ap/` files excepted per
the internal survey (local, not public) §A). On 2026-08-03, the first pre-publication review that was explicitly
framed as **adversarial** ("we are about to let a stranger see this," not a quality/coherence
polish pass) found that code the repo's own `LICENSE` file had already declared proprietary — and
therefore required to be removed from the public tree — had in fact been sitting live on public
GitHub for approximately two weeks, unnoticed. The same gate run also found, in the same pass:
local filesystem paths and a username leaking into documents presented as public; a coverage gap
between what the `LICENSE` file declared and what the `README` actually described; and
self-contradicting claims inside the `README`'s own citation block. None of this had been caught by
the several prior polish/audit passes that had already run over the same files — those passes were
not framed as adversarial, and this class of finding did not surface under a quality-only lens.

## What rule it produced [tier: Dr]
This incident is the origin case for `PUB-ADVERSARIAL-REVIEW` as a standing, mandatory gate before
any public-facing publish, on every channel — not only `git push`. In glosa terms, it is the direct
ancestor of the **release state machine**'s seven-dimension review (§7.4, `design/
FOUNDATION_v0.5.md`): R1 leak scan, R2 license coverage, R3 tier fidelity, R4 citation accuracy, R5
anchor-preservation audit, R6 overclaim/register scan, R7 completeness — run by an independent
pass, never the maker, with verdict `PASS | PASS_WITH_LIMITS | FAIL | HUMAN_REVIEW`. The specific
lesson this incident forces onto glosa's own release gate: **R1 (leak scan) and R2 (license
coverage) are separate checks from R3–R7's content-quality checks**, because this incident showed a
repo can pass every content/quality check repeatedly while still failing both R1 and R2 for two
weeks — a quality pass is not a substitute for a leak/license pass, and a release gate that only
checks tier fidelity and completeness (R3, R7) without also running R1/R2 would have shipped the
same failure again.

## What would have caught it earlier
Running `PUB-ADVERSARIAL-REVIEW`'s R1/R2 dimensions — a leak scan (local usernames, home
directories, internal paths, internal IDs) and a license-coverage check (every file's declared
license status cross-checked against the repo's own `LICENSE` file) — as the **first** gate on any
new public repo, before the first public push, rather than as a pass added only after two weeks of
exposure. This is now `glosa`'s own S6 release-state-machine precondition (§7.4) and is why the
`AGENTS.md` gate (item 8) states publish authority as conditional on "PR + adversarial review + leak
scan" rather than on ordinary review alone.

## Non-collapse pairs this incident illustrates
- No single Appendix A pair captures this directly; it is the empirical grounding for the
  *procedural* rule (R1–R7 as seven separate, non-substitutable checks) rather than for a
  conceptual non-collapse pair. It is cross-referenced from `D-K-STATE`/`D-CANDIDATE-STATUS` in the
  disclaimer catalogue (§5) as the reason those disclaimers are mandatory on every public surface,
  always on, rather than conditional on a reviewer remembering to check.
