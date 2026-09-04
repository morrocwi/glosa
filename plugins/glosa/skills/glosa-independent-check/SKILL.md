---
name: glosa-independent-check
description: Route or verify an independent check on any glosa artifact before it advances past Draft/Pending Review - maker/checker/approver separation, the I0-I5 independence ladder with its tier/K-state ceilings, DVP roles, Resolve-or-Declare, Query Stop. Triggers - "independent check", "who checks this", "maker checker approver", "I0/I1/I2/I3/I4/I5", "cross-vendor review", "DVP", "can I release this", "self-review", "review packet".
---

# glosa-independent-check

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../methodology/P06_independent_check.md` — the full protocol: maker≠checker≠approver,
  the I0-I5 ladder text, tier/K-state ceilings per level, DVP roles, Resolve-or-Declare, Query
  Stop. Read this before routing any check — do not re-derive the ladder from memory.
- `../../../../schema/review_report.schema.json` — what a checker actually writes back.
- `../../../../schema/readiness_report.schema.json` — the readiness object an approver reads.
- `../../../../methodology/data/independence_ladder.json` — the machine-readable I0-I5 enum and
  ceilings, the single source `kernel/` validates against.

## One-line rule (pointer only)

No independent check ⇒ no release. Maker, checker, approver are three pairwise-distinct
identities past `Pending Review`; the independence *class* (I0-I5) caps the maximum tier/K-state
regardless of how many same-level routes stack (`NC-31 ManyModels⇏Independence`,
`NC-32 DVP≠K2` — both in `P06_independent_check.md`).

## If you were handed a review route packet

`../../../../AGENTS.md` rule 4: if pointed at `reviews/routes/*/PACKET.md`, you are **one route**
— read only your packet, write `review_report.yaml` against the schema above, tier your verdict,
never touch the claim card itself.

## Related

- `../../../../methodology/P10_publish_gate.md` (`glosa-publish-gate`) — R1-R7 gate that a release
  cannot pass without a completed independent check on the artifacts it covers.
- `../../../../methodology/P14_project_advisor.md` (`glosa-project-advisor`) — activates only
  after `gate_release` returns PASS, never before.
- Cross-vendor packet template: `../../../../templates/knowledge/cross_vendor_review_packet.md`.
- This workspace's own `maker-checker-gate` skill (`~/.claude/skills/maker-checker-gate/SKILL.md`)
  states the same MIMCG invariant org-wide; `P06_independent_check.md` is glosa's own
  domain-specific instance of it, not a separate rule.
