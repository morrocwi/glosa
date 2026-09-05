> tier: Dr (specified; independently unreviewed)

# P17 — Human Mastery Gate

## One-line rule

A claim may not leave `Draft` for an L3+ artifact until the human who owns it can defend it,
unaided by the AI, against a fixed ten-question live checklist — the AI may have drafted the
prose, but the human must be able to stand behind it alone.

## Why

Founder ruling BBL-2026-09-05-119 governs this card: raise the work, never lower the claim. The
live unaided-defense checklist this card narrates already exists, verbatim, at
`templates/paper/arxiv-twocol/main.tex:375-378` (and its onecol twin), and is asserted as an
enforcement mechanism by two non-collapse rows, `methodology/data/non_collapse_table.json:570`
(NC-56) and `:620` (NC-61) — but that assertion was prose-only before this card:
`design/FOUNDATION_v0.6.md` §7.5 (line 1619) reads only `"Unchanged from v0.1 §7.5"` where no
`FOUNDATION_v0.1.md` file exists anywhere in the repo (confirmed by direct read); the checklist was
scoped to the arXiv paper genre alone, invisible to a code-release or dataset-release L3+ artifact;
and `methodology/P10_publish_gate.md`'s actual mechanical R1–R7 dimension list never named the gate
at all — the NC-56/NC-61 enforcement claim sat undischarged. `design/SESSION_ARCH_v0.4_SPEC.md` §6
and §11.1 (HU-1, `build_now`) name this exact gap and its fix; this card is the genre-independent
protocol text that gap requires, plus the §6 five-check self-protocol layered on top of it.

**Naming note, stated plainly:** `design/SESSION_ARCH_v0.4_SPEC.md` §11.1 names this file
`methodology/P16_human_mastery_gate.md`. It ships here as **P17** — a second card (session
architecture, see `P18_session_architecture.md`) claimed the `P16` slot concurrently in this same
build pass, in the same way `methodology/README.md` already discloses a P15 numbering collision
rather than silently reconciling it. Not renumbered here; a future pass should resolve both P15
and P16/P17 into one sequence.

## Inputs → outputs

- Input: the ten-question checklist already stated at
  `templates/paper/arxiv-twocol/main.tex:375-378` (and the onecol twin) — this card does not
  restate the questions themselves (one-fact-one-home); it narrates the rule that applies them
  outside the arXiv-paper genre.
- Output: `human_mastery_gate.yaml` (`schema/human_mastery_gate.schema.json`, **specified this
  pass, not yet applied to disk** — see the "What this card does NOT do" section): a required
  `gate_status` enum `PASS | PASS_WITH_NAMED_GAPS | NOT_READY`, plus the ten answer fields, each
  human-authored — never `ai_filled` (mirrors `standpoint.declared_basis`'s non-delegable rule,
  P01). A linked gate feeds `methodology/P10_publish_gate.md`'s new **R8** dimension.

## Gate

1. **Entry:** an L3+ artifact (per `design/FOUNDATION_v0.6.md` §7.1's MIMCG mapping) using the
   arXiv paper genre already carries the checklist inline (`Gate status:` line in the template) —
   no separate file is required for that genre; a genre without the template (code release,
   dataset release, any other L3+ artifact type) must link a `human_mastery_gate.yaml` instance.
2. **R8 (new, `methodology/P10_publish_gate.md`):** `gate_status != NOT_READY` is required for any
   L3+ artifact's release-gate pass. `PASS_WITH_NAMED_GAPS` is a legal, honest outcome — it
   discloses which of the ten questions the human could not answer unaided, rather than silently
   failing or silently rounding up to `PASS`.
3. **Failing control — MUST fire:** a non-Paper-genre L3+ claim card with no `human_mastery_gate.yaml`
   linked, currently passing R1–R7 clean (`grep -rn mastery schema/*.json` returns zero hits on
   the schema as it stands today, confirmed) — R8 must return `BLOCKED: NO_MASTERY_GATE_LINKED`.
   **MUST NOT fire:** an S5 Paper-genre artifact using the arXiv template with `Gate status:`
   already filled `PASS`.
4. **Non-delegable:** every one of the ten answer fields is authored by the human being gated, in
   their own words — an AI may prompt the human through the ten questions (same bound as P01's
   completeness-prompting rule, see HU-5), but may never fill an answer on the human's behalf; a
   filled-but-`ai_filled`-tagged answer is itself a `NOT_READY` condition, not a disclosed pass.

## Human / AI division of labour

Human: answers all ten questions unaided, live, and signs `gate_status` — this is the entire point
of the gate; delegating the answers to the AI that drafted the artifact would collapse exactly the
distinction the gate exists to preserve (does the human, not the AI, understand and can defend
what is being released). AI: may draft the artifact itself, may run the mechanical R1–R7 checks
that sit beside R8, and may hold the ten questions ready to ask — but never answers them, never
scores the answers, and never sets `gate_status`.

## §6 merge — self-check protocol vs. mechanical publish-gate wiring

`design/SESSION_ARCH_v0.4_SPEC.md` §6 states five self-checks for the human/AI pair (entry,
selection, direction, boundary, diagnostic-not-gate) that compose across the Blackbox Note,
`hypothesis_selection.yaml`, Problem Card, and `kg_edge.yaml` — see `P18_session_architecture.md`.
Those five checks are the standing self-check protocol for a session in progress; this card's R8
is the separate, narrower point where that protocol becomes a mechanical publish-gate requirement
for a specific artifact about to leave Draft. Neither duplicates the other: §6 is continuous
(checked throughout a session), R8 is a single gate (checked once, at release). Per
`EPIS-KNOWLEDGE-VALIDATION`, R8 is not a vertical-authority certification layer — it is this
repo's own maker≠checker≠approver discipline (`AGENTS.md` gate rule 3) applied to the human's own
unaided defense of their own claim, not an outside party's approval.

## Disclaimers emitted

`D-STANDPOINT` · `D-AUTHORSHIP` · a dedicated `D-MASTERY-GATE-NAMED-GAPS` row is **not yet added**
to `methodology/data/disclaimer_catalogue.json` in this pass (out of scope for this task's
ownership list) — `PASS_WITH_NAMED_GAPS` should surface via that catalogue in a future pass rather
than only in `human_mastery_gate.yaml`'s own field; named here as the honest gap, not silently
closed.

## Non-collapse pairs enforced

`NC-56` and `NC-61` (`methodology/data/non_collapse_table.json:570`, `:620` — the checklist's own
originating rows) · `NC-58` AIContribution≠EpistemicResponsibility (the human's unaided defense is
exactly the check that keeps responsibility from silently transferring to the tool that drafted
the prose) · `NC-60` Founder=ideas/direction≠AI=assistant.

## What this card does NOT do

The schema `schema/human_mastery_gate.schema.json`, the template, the kernel validator, the R8 warning in `methodology/P10_publish_gate.md` and the §7.5 pointer fix were built in v0.4 (2026-09-05); this card is the protocol text and does not certify that build.
text for that fix, but does not apply it). This card narrates the rule; the DAG node
`hu.mastery-gate-wired` (spec §13) tracks the build. It does not decide *what counts as a correct
answer* to any of the ten questions — the kernel and R8 can only check the field is present and
human-authored, never that the defense given is actually sound (same presence-vs-correctness split
already applied to the bias register in `P15_problem_first_and_responsibility.md`). It does not
retroactively gate already-released L3+ artifacts — forward-only, same default as
`design/SESSION_ARCH_v0.4_SPEC.md` §7's recommended (not yet founder-ratified) answer for SA-3's
retroactivity question.

## TODO(hu.mastery-gate-wired)

Build `schema/human_mastery_gate.schema.json`, add R8 to `methodology/P10_publish_gate.md`, and
fix the `FOUNDATION_v0.6.md` §7.5 pointer — per `design/SESSION_ARCH_v0.4_SPEC.md` §11.1 and
`design/FOUNDATION_v0.7_PATCH.md` §1. `founder_decision_needed: true` per the spec's own DAG node.
