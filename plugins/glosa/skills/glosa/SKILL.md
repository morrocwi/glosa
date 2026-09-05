---
name: glosa
description: Master entry point for the glosa methodology (Rigour Without Infrastructure — human-AI knowledge co-production, standalone scholar). Load this FIRST whenever a task involves writing a claim, running a Blackbox Note dialogue, doing a literature review, an independent check, a publish gate, or advising on a project's next conversion step — before jumping straight to one of the other six glosa-* skills. Triggers: "claim card", "blackbox note", "independent check", "literature review", "publish gate", "project advisor", "glosa", "K1/K2 state", "five questions".
---

# glosa — master entry

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file. Founder
> Yaoharee Lahtee = method direction; AI drafted this pointer file. No priority-claim language.

## Read this first

- `../../../../AGENTS.md` — the eight-rule gate, identical in `CLAUDE.md`/`GEMINI.md`. Binding on
  every session before touching anything in this repo.
- `../../../../design/FOUNDATION_v0.6.md` §2 (spine) and §3 (claim card) — the whole system, read
  before editing anything.
- `../../../../methodology/README.md` — index of every `P*.md` protocol card.

## The spine, one paragraph

A human raw line lands in a **Blackbox Note** (`glosa-blackbox-note`) → gets a **lens
translation** (`../../../../methodology/P00_lens.md`) → becomes a **claim card**
(`glosa-claim-card`) answering five questions (seen / separates / AI-filled / assumed / tested) →
evidence for it is gathered, optionally through a full **literature review**
(`glosa-literature-review`) → the artifact only advances past `Pending Review` through an
**independent check** (`glosa-independent-check`, maker ≠ checker ≠ approver) → nothing reaches a
stranger without the **publish gate** (`glosa-publish-gate`, R1-R7) → only after release does the
**project advisor** (`glosa-project-advisor`) suggest a next conversion step.

## Which skill to load next

| Situation | Load |
|---|---|
| Starting from a raw human statement/dialogue | `glosa-blackbox-note` |
| Turning a distinction into a claim (stub or full) | `glosa-claim-card` |
| A claim needs external sources, not just an assertion | `glosa-literature-review` |
| An artifact is about to move past Draft/Pending Review | `glosa-independent-check` |
| Something is about to leave this repo's hands (push, deposit, artifact, message) | `glosa-publish-gate` |
| An artifact already passed the publish gate; what's next | `glosa-project-advisor` |

## Pointers, not restatement

Every rule body lives in exactly one place — do not copy protocol text into this file or any
other `SKILL.md` (`../../../../design/REPO_SPEC_v0.6.md` §"one fact one home"):

- Protocol cards: `../../../../methodology/P00_lens.md` … `P14_project_advisor.md`, plus
  `P17_human_mastery_gate.md` and `P18_session_architecture.md`
  (`../../../../methodology/README.md` is the index; some ids referenced by design docs, e.g.
  `P15_blackbox_note.md`, are not yet written — see `glosa-blackbox-note`'s own pending note; the
  README also discloses the P15/P16/P17/P18 numbering collisions rather than reconciling them).
- Schemas (field-level truth for every card/log/manifest): `../../../../schema/*.schema.json`.
- Fill-in templates: `../../../../templates/knowledge/*.yaml` / `*.md`.
- Paper skeletons with the mandatory Blackbox Note appendix: `../../../../templates/paper/`.
- Chair rulings that resolved every open dispute: `../../../../design/CHAIR_RULING_v1.md`.
- Prior public work, listed not interpreted: `../../../../lineage/PRIOR_WORK.md`.
- Vendor-neutral (non-Claude-Code) equivalent of this whole skill set: `../../PROMPT_PACKET.md`.

## Status

K0 (public working release: timestamped, citable, not peer reviewed, no independent check yet).
K1 would require a cross-vendor I3 route; K2 would require an external human (I5) — neither has
run. Treat every output as `tier: Dr` unless a cited card says otherwise.
