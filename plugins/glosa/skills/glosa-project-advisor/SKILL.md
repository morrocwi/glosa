---
name: glosa-project-advisor
description: Advise on a project's next conversion step after (never before) an artifact has cleared the publish gate - a third role, distinct from maker/checker/approver, that reads a released manifest and produces one conversion_plan.yaml (K-state now, Global + Thai/local route, next addressed actions, rejection budget, what-NOT-to-do list, candidate-never-certified). Triggers - "project advisor", "what's next for this project", "conversion plan", "K1 to K2 path", "advise on this release".
---

# glosa-project-advisor

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../methodology/P14_project_advisor.md` — the full role definition, activation
  condition, and `conversion_plan.yaml` output spec.
- `../../../../schema/conversion_plan.schema.json` — authoritative field list.
- `../../../../templates/knowledge/conversion_plan.yaml` and
  `../../../../templates/knowledge/advisor_prompt_packet.md` — fill-in templates.
- `../../../../design/FOUNDATION_v0.5.md` §7.7 and §1.2 (chair ruling B3) — why
  `ai-native-scholarship` is cited by name+version+DOI here, never merged into `plugins/`.

## One-line rule (pointer only)

Third role, distinct from Maker/Checker/Approver on the same artifact. Activates **only** after
`gate_release` (`glosa-publish-gate`) returns `PASS`/`PASS_WITH_LIMITS` on an L3+ artifact — never
on `Draft`/`Pending Review` work. Reads the release manifest, linked cards, project kg, and
existing K1→K2 conversion ledger; never writes to them. Produces one `conversion_plan.yaml`.

## Related

- `../../../../methodology/P10_publish_gate.md` (`glosa-publish-gate`) — the gate that must return
  PASS before this role may activate at all.
- `../../../../lineage/PRIOR_WORK.md` — the founder's public prior Zenodo records this advisor may
  point at as a route precedent, listed not interpreted.
- `ai-native-scholarship v1.0.0` (Zenodo 10.5281/zenodo.22163849) — cited as a dependency by
  name+version+DOI only; not present in this repo's `plugins/` tree.
