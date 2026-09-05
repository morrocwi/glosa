> tier: Dr (specified; independently unreviewed)

# methodology/ — protocol card index (P0–P14)

One card = one file, one rule, prose only (`design/REPO_SPEC_v0.6.md` §"methodology/", L1). A
protocol card narrates a rule; it never redeclares a field name — every field a card mentions is
defined once, in the matching `schema/*.schema.json` file (one-fact-one-home, request 21). Machine-
read rule *content* (disclaimer wording, genre-router tables, contaminated-concept table) lives
under `methodology/data/`, cited by these cards, never restated inline.

Full spine and schema: `design/FOUNDATION_v0.6.md` §2 (the round trip), §3 (the claim card), §4
(tier/independence/K-state), §5 (disclaimer catalogue), §6 (genre router), §7 (gates/MIMCG/
citation), §8 (one-fact-one-home layout), §9 (callable layer).

**CLI discoverability:** a protocol card narrates *why* a rule exists; it is not where you find
the command that runs it. The full, current command list lives at `cli/README.md`, and
`./cli/glosa --help` is the live source of truth (it reads the actual argparse dispatch, so it
cannot drift the way a card's prose can). A frontline user's fastest path into any card above is
usually one CLI verb, e.g. `./cli/glosa intake new --project <name> --human-owner <you>` for P2.

## This batch (task B4) — P0–P7

| Card | File | One-line rule |
|---|---|---|
| P0 | `P00_lens.md` | Readout-not-truth as default reading stance; lens-in/lens-out round trip before any analysis. |
| P1 | `P01_standpoint.md` | Declare who speaks, from what base, and what disciplines are explicitly not claimed. |
| P2 | `P02_intake.md` | Two-question gate before any analysis starts; issue = retained difference; 0≠⊥; stakeholder≠agency. |
| P3 | `P03_claim_card.md` | The atomic unit — five questions ⇄ E-A-D, in one of two legal shapes (`stub`/`full`). |
| P4 | `P04_assumption_check.md` | Typed augmentation naming + contaminated-concept scan + identification ladder. |
| P5 | `P05_evidence_challenge.md` | Bidirectional support+challenge search, global+local tracks, per hypothesis. |
| P6 | `P06_independent_check.md` | Maker≠checker≠approver; MIMCG L0–L5; independence ladder I0–I5 with tier/K ceilings. |
| P7 | `P07_ai_fill_disclosure.md` | What AI added, route-level, six-way audit, never silently merged into the source. |

## Owned by the other builder (not written in this batch)

Per `design/REPO_SPEC_v0.6.md`'s methodology tree, cards P8–P14 (and the separately-tracked P15)
are owned by the other builder working this task in parallel. Listed here only as an index pointer
— their content, rationale, and citations belong in their own files, not restated here:

| Card | File | One-line rule (per `REPO_SPEC_v0.5.md`) |
|---|---|---|
| P8 | `P8_diagnosis.md` | Don't trust one instrument; plausible vs. verified language. |
| P9 | `P9_vet_external_input.md` | Any outside source is untrusted until read in full. |
| P10 | `P10_publish_gate.md` | Adversarial review + leak scan before public-facing. |
| P11 | `P11_log_and_decision.md` | Append-only logbook + DECISIONS row; dissent never erased. |
| P12 | `P12_readiness.md` | Pre-work readiness report, fail-closed. |
| P13 | `P13_genre_router.md` | Narrates FOUNDATION §6's 9-genre table + `venue_track`/`companion_of`; cites `methodology/data/genre_router_table.json`. |
| P14 | `P14_project_advisor.md` | The third role (FOUNDATION §7.7) — activation trigger, reads/writes, SCRAM conditions (specified, Dr, untested). |

(For completeness, `REPO_SPEC_v0.5.md` also names `P15_blackbox_note.md` — added after the P0–P14
set, per chair ruling A1/A2's request-32 rename — as the raw-voice + cooking-log discipline card;
not part of the original P0–P14 numbering and not this batch's responsibility either.)

## P15 — problem-first spine + responsibility per arrow (founder instruction, 2026-09-04)

| Card | File | One-line rule |
|---|---|---|
| P15 | `P15_problem_first_and_responsibility.md` | Problem state precedes "observation" (a verb, not a node); every spine arrow names who performed it, Inference→Claim always human; operationalization/study-design/bias-register/robustness for `EMPIRICAL` cards (optional; warns if absent). |

**Naming note:** `REPO_SPEC_v0.5.md` names a *different* `P15_blackbox_note.md` (the raw-voice +
cooking-log discipline card, chair ruling A1/A2). `P15_problem_first_and_responsibility.md` is a
distinct file added this pass (founder instruction 2026-09-04, BBL-2026-09-04-083/084) — a second
numbering collision at P15, alongside the P0–P7 two-digit-vs-one-digit variance already flagged
above. Not silently reconciled here; a future pass should renumber one of the two.

## P17, P18 — session-architecture review cards (2026-09-05, `design/SESSION_ARCH_v0.4_SPEC.md`)

| Card | File | One-line rule |
|---|---|---|
| P17 | `P17_human_mastery_gate.md` | Ten-question live unaided-defense checklist, generalized past the arXiv-paper genre and wired to publish-gate R8 (HU-1, build_now). |
| P18 | `P18_session_architecture.md` | The Session object as a logical join across Blackbox Note + `hypothesis_selection.yaml` + Problem Card + `kg_edge.yaml`, one-fact-one-home; retention≠direction (NC-77); momentum diagnostics Open, diagnostic-only. |

**Naming note (third numbering collision, disclosed rather than reconciled, same pattern as
P0–P7 and P15 above):** `design/SESSION_ARCH_v0.4_SPEC.md` §11.1 names the Human Mastery Gate card
`P16_human_mastery_gate.md`. It ships here as **P17** because a concurrent task in this same build
pass claimed the P16 slot for a different card; P18 (session architecture) is not assigned any
number by the spec at all — it is the next free slot in this file's own sequence. A future pass
should reconcile P15, P16 (whatever it becomes), P17, and P18 into one clean sequence rather than
layering a fourth disclosed collision on top of these three.

## Flagged, not silently reconciled: filename numbering variance

This batch's task instruction named files `P00_lens.md` … `P07_ai_fill_disclosure.md` (two-digit
`P0`), while `design/REPO_SPEC_v0.6.md`'s methodology tree and the plugin `SKILL.md` pointers it
lists (e.g. `glosa-intake/SKILL.md → cites methodology/P2_intake.md`) use single-digit names
(`P2_intake.md`, not `P02_intake.md`) for cards P0–P9. This batch follows the task instruction's
exact filenames (`P00`–`P07`) as given. The two conventions do not yet resolve to the same file
path for P0–P7; a future pass should either rename this batch's files to match `REPO_SPEC_v0.5.md`
exactly or update `REPO_SPEC_v0.5.md`'s own tree and every `SKILL.md` pointer it lists — this is
named here rather than picked silently, per the one-fact-one-home discipline this same batch is
built under.

## Cross-card invariants (apply to every card above, this batch included)

- Every card's "why" cites a real founder ruling or reviewer finding from
  `design/FOUNDATION_v0.6.md` or `design/HANDOFF_2026-09-04_founding-meeting.md` — never an
  invented incident.
- No card redeclares a schema field name — a card that needs to mention a field cites
  `schema/<name>.schema.json`, one home.
- No card proposes external/institutional validation as what makes a claim legitimate
  (`EPIS-KNOWLEDGE-VALIDATION`; `AGENTS.md` gate rule 6).
- Comparison language throughout every card is same/different/cited — never novel/first/
  unprecedented/prior art/seminal/pioneering, and never "we borrow/take from."
- Every card is tier `Dr` until an independent I2+ check actually runs against it — none of this
  batch has been independently reviewed yet (`AGENTS.md` gate rule 8: no independent check ⇒ no
  release).
