# glosa PROMPT_PACKET — vendor-neutral

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file. This
> packet lets **any** AI assistant — Codex, Gemini, a local model, or a human alone — run one
> glosa stage from files on disk, with no Claude Code plugin/skill machinery required. It is the
> non-Claude-Code equivalent of `plugins/glosa/skills/*/SKILL.md`; both point at the same
> `methodology/`/`schema/`/`templates/` files and must never fork the protocol between the two.

## Before anything: read the gate

Read `AGENTS.md` (repo root) in full — identical content in `CLAUDE.md`/`GEMINI.md`. Its eight
rules bind every AI session regardless of vendor:

1. Everything here is a readout, not truth. Tag your tier
   (`Th_coqc`/`finite_diagnostic`/`fit_calibrated`/`Dr`/`definition`/`Open`) on every verdict.
2. Read `design/FOUNDATION_v0.6.md` §2 (spine) and §3 (claim card) before editing anything.
3. Maker ≠ checker ≠ approver. Never certify what you produced. Same-model self-review has no
   standing.
4. If pointed at `reviews/routes/*/PACKET.md` you are ONE route: read only your packet, write
   `review_report.yaml`, tier your verdict, do not touch the claim card.
5. Human holds standpoint, falsifier judgment, ethics, and public commitment. AI drafts, routes,
   checks mechanically, logs. AI is never an author.
6. Never propose external/institutional validation as what makes a claim legitimate. Never write
   "novel/first/prior art". Comparison = same / different / cited.
7. Human raw lines (Blackbox Note) are verbatim, never edited or translated in place; the cooking
   log is append-only.
8. No independent check ⇒ no release. Public push only through the publish gate (PR + adversarial
   review + leak scan).

## Pick your stage

Each row: the protocol card that owns the rule (read it in full before acting), the schema that
owns the exact field list, and the template to copy and fill in. Do not restate the protocol card's
text elsewhere — cite it.

| Stage | Protocol card | Schema | Template |
|---|---|---|---|
| Lens translation | `methodology/P00_lens.md` | — | — |
| Standpoint | `methodology/P01_standpoint.md` | — | — |
| Intake / Problem Card | `methodology/P02_intake.md` | `schema/problem_card.schema.json` | — |
| Claim card | `methodology/P03_claim_card.md` | `schema/claim_card.schema.json` | — |
| Assumption check | `methodology/P04_assumption_check.md` | — | — |
| Evidence challenge | `methodology/P05_evidence_challenge.md` | `schema/evidence_relation.schema.json` | — |
| Independent check | `methodology/P06_independent_check.md` | `schema/review_report.schema.json` | `templates/knowledge/cross_vendor_review_packet.md` |
| AI-fill disclosure | `methodology/P07_ai_fill_disclosure.md` | — | — |
| Diagnosis | `methodology/P08_diagnosis.md` | — | — |
| Vet external input | `methodology/P09_vet_external_input.md` | — | — |
| Publish gate | `methodology/P10_publish_gate.md` | `schema/release_manifest.schema.json` | — |
| Log and decision | `methodology/P11_log_and_decision.md` | — | — |
| Readiness | `methodology/P12_readiness.md` | `schema/readiness_report.schema.json` | — |
| Literature review (LRS, L1-L6) | `methodology/P13_literature_review.md` + `design/S14_literature-review-system.md` | `schema/search_log.schema.json`, `source_acquisition_log.schema.json`, `citation_card.schema.json`, `dialogue_table_row.schema.json`, `neighbour_table_row.schema.json`, `litreview_manifest.schema.json`, `hypothesis_selection.schema.json` | `templates/knowledge/search_log.yaml`, `source_acquisition_log.yaml`, `citation_card.yaml`, `dialogue_table.md`, `neighbour_table.md`, `litreview_manifest.yaml`, `hypothesis_selection.yaml`, `sr_protocol_prisma_lite.md` |
| Project advisor | `methodology/P14_project_advisor.md` | `schema/conversion_plan.schema.json` | `templates/knowledge/conversion_plan.yaml`, `advisor_prompt_packet.md` |
| Blackbox Note | *pending* — `methodology/P15_blackbox_note.md` not yet written; use `P00_lens.md` + `P02_intake.md` + `design/FOUNDATION_v0.6.md` §2.3 meanwhile | `schema/blackbox_note.schema.json` | `templates/knowledge/blackbox_note.yaml` |

## Blackbox Note attribution (binding, every dialogue record)

Every Blackbox Note carries a required `lens_used` block. The display string is exactly:

```
Readout Universe — Yaoharee Lahtee
```

cite the lens's DOI(s) via a `VERIFIED` citation card and its repo URL wherever the lens is named,
or the document hard-fails `D-LENS-UNCITED` (`design/FOUNDATION_v0.6.md` §5). Every hypothesis
statement carries a signature line naming the lens `lens_ref` points at, or the document hard-fails
`D-LENS-UNSIGNED`. Full rule: `design/FOUNDATION_v0.6.md` §2.3, §3.2, §3.3 rule 12.

## New this pass (v0.6) — pointer only, rule bodies stay in FOUNDATION

Kernel rules 18–28 (`design/FOUNDATION_v0.6.md` §3.3): injected-infinity/zero taxonomy, the
Fail-Able Gate Law, forbidden-word-list rejection on `comparison.basis`, the genre-router layer-mismatch
diagnostic, the LRS claim-tier intake flag, `verdict_class`, the PCS red-flag, the discovery-
routing extension, and the composite-quote / hidden-AI-fill / inflated-bearing detectors. Several
of these (§3.3 rules 21, 22, 24, 25) are `PENDING FOUNDER DECISION` — read the FOUNDATION section
directly before treating them as binding. New claim-card fields (`comparison`, `evidence_strength`,
`verdict_class`, `gate_fail_taxonomy`, `gate_construction_status`,
`five_questions.seen.ai_assisted_fields`) are additive/optional, `schema/claim_card.schema.json`
target `0.7.0` — not yet applied to the schema file on disk.

## Output discipline

- Tag every output's `tier` and, if released, its `k_state`. This repo's own current release
  state is **K0** (public working release: timestamped, citable, not peer reviewed, no
  independent check yet). K1 would require a cross-vendor I3 route; K2 would require an external
  human (I5) — neither has run. Never claim or imply K1/K2/K3.
- Comparison to any other tool/method is **same / different / cited** only — no priority language
  (see the priority-language list enforced by scripts/check_forbidden_words.sh) and no "we borrow/take from them".
- Do not propose external/institutional validation (peer review, an outside expert's say-so) as
  what would make a glosa claim more legitimate.
- Before anything reaches a stranger (a push to a public remote, a public artifact, a deposit, an
  external message), run the publish gate (`methodology/P10_publish_gate.md`) with a checker
  identity distinct from whoever drafted the content.

## Where the Claude Code plugin equivalent lives

`plugins/glosa/skills/*/SKILL.md` — same files, same rules, wrapped as Claude Code skills with
frontmatter triggers. Read either; never let the two drift into different protocol text.
