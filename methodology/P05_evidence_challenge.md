> tier: Dr (specified; independently unreviewed)

# P5 — Evidence Challenge (support AND challenge; global+local; LOCAL_EVIDENCE_NOT_FOUND ≠ NO_LOCAL_EVIDENCE_EXISTS)

## One-line rule

Every evidence search runs bidirectional query families — support **and** challenge, never a
negated support query standing in for a real challenge family — across both a global track and a
local/frontline track, and a search that finds nothing locally is recorded as a search-coverage
fact, never promoted to "no such evidence exists."

## Why

`design/FOUNDATION_v0.5.md` §7.8 names this directly: `LOCAL_EVIDENCE_NOT_FOUND ≠ NO_LOCAL_
EVIDENCE_EXISTS` (`NC-27`) — "a search-coverage fact is never promoted to a universal negative."
`design/S14_literature-review-system.md` §1 (founder request 35, 2026-09-04 —
*"บังคับก่อนทบทวนวรรณกรรม: ต้องแยกทำระบบทบทวนวรรณกรรมเป็นอีกหนึ่งระบบ ... เพื่อความแม่นยำสูงสุด"*) makes
"global + local (Thai/frontline) tracks, bidirectional support+challenge query families" a named,
frozen-before-opened protocol step (S14 §2.2, L2), reused unchanged from S8's own machinery
(one-fact-one-home — this card sequences `search_log.yaml`, it does not re-specify it). The
`frozen_scope` locked **before** `sources_found` is populated is what makes the search auditable
as pre-registered rather than post-hoc-tuned.

## Inputs → outputs

- Input: `claim_card.lens_translation` + `hypothesis_world` (from P0/P3) — one LRS run per
  hypothesis (S14 §0, request 35b: several hypotheses from one lens-out pass mean several separate
  runs, never one merged search blurring which evidence backs which falsifier).
- Output: `templates/knowledge/search_log.yaml` (`frozen_scope`, `sources_found`, `review_mode`),
  `templates/knowledge/source_acquisition_log.yaml`, `templates/knowledge/dialogue_table.md`
  (source-by-source: what it sees, what it separates, what it assumes, where it agrees/disagrees,
  what it would say against us — S14 §0 request 35c, descriptive placement, never chronological or
  "seminal" rank), feeding `claim_card.five_questions.tested.evidence_relations[]`.

## Gate

`review_mode` must be chosen honestly from the six-value enum
(`SYSTEMATIC_REVIEW | TARGETED_SEARCH | SCOPING_SEARCH | RAPID_EVIDENCE_CHALLENGE |
FIELD_OBSERVATION_LOG | INTERNAL_DATA_AUDIT`, S14 §2.2) before `sources_found` is populated —
**FC-S8-1** (hard block, `design/FOUNDATION_v0.5.md` §7.8) refuses calling anything less than a
full SR protocol a "systematic review."

## Human / AI division of labour

Human: names the honest label and the stopping rule (S14 §1, L2 row) and holds the private
research-library shelf (`rl`) for institutional/paywalled access (S14 §2.3, L3 row). AI:
runs/drafts the support+challenge query families across global+local tracks, attempts open-access
resolution, records HTTP status, and **never self-certifies `obtained`** or
`claim_match_verified` on its own read of a source (S14 §1, L3/L5 rows) — a decorrelated I3 route
or a human must confirm claim match.

## Disclaimers emitted

`D-CITATION-UNVERIFIED` (any citation with `fetch_status ∈ {NOT_FETCHED, FETCH_FAILED,
UNCHECKED_OFFLINE}`, or the derived `state` parameter) · `D-COMPARISON` (any same/different/cited
positioning against a neighbour) · `D-PARTIAL-SET` (a 3-lane structure — e.g. DVP routes — with
fewer than 3 admissible members).

## Non-collapse pairs enforced

`NC-18` Source existence≠Claim support · `NC-19` metadata_verification≠scope_verification ·
`NC-27` LOCAL_EVIDENCE_NOT_FOUND≠NO_LOCAL_EVIDENCE_EXISTS · `NC-46` Systematic Review≠Rapid/
Scoping/Targeted evidence challenge · `NC-47` AI output≠Evidence · `NC-48` Global/Anglophone
route≠Local/Thai-language route.

## What this card does NOT do

It does not verify a citation by itself — `metadata_verified` (mechanical) and `claim_match_
verified` (I5 human or decorrelated I3) are both required and are P6's independent-check
territory, not this card's. It does not merge several hypotheses' searches into one manifest
(request 35b forbids this explicitly). It does not treat AI's own reading of a source as evidence
in itself (`NC-47`) — AI output is a candidate for a human or an I3+ route to confirm, never a
citation-ledger entry on its own say-so.
