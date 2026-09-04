# glosa (Claude Code plugin)

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file itself.

Packages the `glosa` methodology — **Rigour Without Infrastructure: a standalone scholar
methodology for human-AI knowledge co-production** (founder Yaoharee Lahtee, ORCID
0009-0005-3861-0626, Open Civil Science Initiative) — as a set of Claude Code skills. AI assists
(drafting, structuring, mechanical checks); it is disclosed in the work and is never an author.

## What this is

Seven skills, each a thin pointer into `methodology/P*.md`, `schema/*.json`, and
`templates/knowledge/` — no skill restates the protocol body (one fact, one home; see
`AGENTS.md` rule and `design/REPO_SPEC_v0.5.md`):

| Skill | Loads for |
|---|---|
| `glosa` | Master entry — orientation, the spine, which of the other six skills to load next |
| `glosa-claim-card` | The five-questions claim card (stub vs full) |
| `glosa-blackbox-note` | Raw verbatim dialogue lines, the append-only cooking log, `lens_used`, hypothesis signatures |
| `glosa-independent-check` | Maker/checker/approver separation, independence ladder I0-I5, DVP packets |
| `glosa-literature-review` | The six-stage Literature Review System (LRS), dialogue table, two exit gates |
| `glosa-publish-gate` | The R1-R7 publish gate (leak scan, tier fidelity, overclaim scan, ...) and K-state semantics (K0 today; K1 needs I3; K2 needs I5) |
| `glosa-project-advisor` | The Project Advisor third role (post-release only) |

## Source form

`.claude-plugin/marketplace.json` declares the plugin's source as
`{"source": "github", "repo": "morrocwi/glosa"}` — **no `path:` key**, so `claude plugin install`
clones the whole repository rather than a subtree rooted at `plugins/glosa/`. This was chosen (and
validated with `claude plugin validate`, which rejects a bare git-URL string for this field —
`github`+`repo` is the accepted shape) because every `SKILL.md` in this plugin cites
methodology/schema/template files by a path relative to the repo root (e.g.
`../../../../methodology/P03_claim_card.md`); a `path:`-scoped subtree checkout would silently
break every one of those pointers by dropping the sibling directories they resolve into.
`design/FOUNDATION_v0.5.md` §9 and `design/REPO_SPEC_v0.5.md` (marketplace.json comment, line
~380: "source clones the WHOLE repo, no `path:` into a subtree") both specify this form.

## Status

K0 public working release (not peer reviewed; no independent check yet). Not peer reviewed. No I5 (independent external human) check has run on this
plugin or the methodology it packages. Every artifact this layer produces before the Accuracy gate
(`FOUNDATION_v0.5.md` §9) passes carries `tier: Dr` and `D-CANDIDATE-STATUS`.

## Vendor-neutral equivalent

Codex, Gemini, or a local model that cannot load Claude Code skills can run the same protocol from
`plugins/glosa/PROMPT_PACKET.md` plus the same `methodology/`/`schema/`/`templates/` files — no
plugin machinery required.
