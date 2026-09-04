---
name: glosa-publish-gate
description: Run the glosa publish gate before anything leaves this repo's hands toward a stranger - a public git push, a public artifact, a Zenodo deposit, an external message. Seven dimensions R1-R7 (leak scan, license coverage, tier fidelity, citation accuracy, anchor-preservation, overclaim/register scan, completeness), run by an identity distinct from the maker, plus K1 release semantics. Triggers - "publish gate", "can we push this public", "leak scan", "is this ready to release", "K1 status", "overclaim scan", "PUB-ADVERSARIAL-REVIEW".
---

# glosa-publish-gate

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../methodology/P10_publish_gate.md` — the full R1-R7 rule, run by an identity distinct
  from whoever produced the content (never a same-model self-check).
- `../../../../schema/release_manifest.schema.json` — what a passed gate produces.
- `../../../../design/FOUNDATION_v0.6.md` §7.4/§6.4 — the reflexive glosa-cites-glosa rule and the
  K-state semantics this gate certifies into.
- This workspace's own `PUB-ADVERSARIAL-REVIEW` standing rule (`~/.claude/CLAUDE.md`) — the
  org-wide version of the same invariant; `P10_publish_gate.md` is glosa's domain instance of it.

## The seven dimensions (pointer only — full text in P10_publish_gate.md)

R1 leak scan · R2 license coverage · R3 tier fidelity · R4 citation accuracy (re-runs the LRS
accuracy gate independently) · R5 anchor-preservation audit (`lineage/` `PRESERVE_EXACT`/
`PRESERVE_FUNCTION` rows) · R6 overclaim/register scan (contaminated-concept table + priority-word
list) · R7 completeness (every reference/field resolves).

## New this pass (v0.6) — pointer only, rule bodies stay in FOUNDATION

`../../../../design/FOUNDATION_v0.6.md` §7.8 adds three kernel-closure checks feeding R4/R6:
composite-quote detector (rule 26), hidden-AI-fill detector (rule 27), inflated-bearing detector
(rule 28) — none founder-gated, all shipped this pass. §3.3 rule 19 (Fail-Able Gate Law) also
applies to this gate itself: a gate documented here as Type-P must cite a machine-derived failing
control it correctly rejected, or it stays Type-U.

## K-state semantics at release

This repo's own release-time K-state is **K0** (public working release: timestamped, citable,
not peer reviewed, no independent check yet). K1 requires a cross-vendor I3 route; K2 requires an
external human (I5) — neither has run for this repo. Never state or imply K1/K2/K3 without the
required route actually completed (`glosa-independent-check`) — `NC-32 DVP≠K2` applies here as
everywhere else in glosa.

## Related

- `../../../../methodology/P06_independent_check.md` (`glosa-independent-check`) — the check this
  gate cannot substitute for; a passed publish gate still needs the underlying artifacts to have
  cleared their own independent check first.
- `../../../../methodology/data/contaminated_concept_table.json` and the forbidden-word list in
  `../../../../AGENTS.md` rule 6 — the R6 scan target.
- `../../../../methodology/P14_project_advisor.md` (`glosa-project-advisor`) — activates only
  after this gate returns PASS/PASS_WITH_LIMITS.
