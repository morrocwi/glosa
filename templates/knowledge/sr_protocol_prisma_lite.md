# PRISMA-2020-lite protocol — RWI S8 template (Dr, unreviewed)

> Fill this file when `search_log.yaml.review_mode` is any literature mode. Full PRISMA-2020
> flow-diagram counts (§4 below) are REQUIRED only for `review_mode: SYSTEMATIC_REVIEW`; the
> other sections apply to every literature mode as a transparency floor, per skillme's own
> citation (`SKILLME.md` §6.17.1): "transparency/reproducibility principle taken from
> PRISMA 2020 (https://www.bmj.com/content/372/bmj.n71) and systematic-search principle from
> Cochrane Handbook Chapter 4 (https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04),
> but not every evidence challenge is claimed as a full systematic review."

## 0. Honest label — pick exactly one and state why

- [ ] `SYSTEMATIC_REVIEW` — protocol pre-registered, full PRISMA flow counts, ≥1 independent
      screener re-check completed.
- [ ] `TARGETED_SEARCH` — a small, deliberately chosen set of known-relevant sources for one
      named claim. Not exhaustive; state so explicitly.
- [ ] `SCOPING_SEARCH` — broad/exploratory mapping of what exists. No claim may cite this alone
      as sufficient evidence.
- [ ] `RAPID_EVIDENCE_CHALLENGE` — time-boxed bidirectional support+challenge search under a
      stated deadline.
- [ ] `FIELD_OBSERVATION_LOG` — direct sensory/field observation, not literature (use
      `search_log.yaml`'s `field_observation` block instead of the sections below).

**Forbidden claim FC-S8-1**: calling anything below `SYSTEMATIC_REVIEW` a systematic review.

Reason for the chosen label (time/scope constraint, honestly stated):
_______________________________________________________________

## 1. Frozen scope (fill BEFORE opening any search results)

1. Hypothesis / claim / falsifier: _______________
2. Question type (mechanism / effect / diagnosis / prediction / implementation / experience /
   law-policy / descriptive baseline): _______________
3. Concepts, synonyms, controlled vocabulary: _______________
4. Inclusion / exclusion rules: _______________
5. Time window and language strategy: _______________
6. Global source classes to search: _______________
7. Local-context source classes and local language(s): _______________
8. Search date, stopping rule, conflicts of interest, access limits: _______________

## 2. Bidirectional query families

| Support family (mechanism present / effect observed / supports) | Challenge family (contradicts / null effect / boundary / alternative mechanism / failed replication / retraction) |
|---|---|
| | |

Challenge queries must be independently constructed — never merely the negation of a support
query.

## 3. Global + local tracks

- **Global track** — how strong is this internationally, what study designs examined it:
  _______________
- **Local-context track** — does the mechanism appear, hold, or break in the founder's actual
  setting (law, language, infrastructure, population): _______________
- **Transfer verdict** (required if a global result is applied locally):
  `TRANSFERS_DIRECTLY | TRANSFERS_WITH_ADAPTATION | DOES_NOT_TRANSFER | UNASSESSED`

`LOCAL_EVIDENCE_NOT_FOUND` is a search-coverage fact, never treated as
`NO_LOCAL_EVIDENCE_EXISTS`.

## 4. PRISMA-2020 flow counts (REQUIRED only for SYSTEMATIC_REVIEW; leave blank otherwise)

| Stage | Count |
|---|---|
| Records identified through database searching | |
| Additional records identified through other sources | |
| Records after duplicates removed | |
| Records screened | |
| Records excluded | |
| Full-text articles assessed for eligibility | |
| Full-text articles excluded, with reasons | |
| Studies included in qualitative/quantitative synthesis | |

Independent screener sign-off (name/role, required for SYSTEMATIC_REVIEW only): _______________

## 5. Result summary (both directions, stated explicitly)

- What was found supporting the hypothesis: _______________
- What was found challenging / limiting / null / boundary conditions: _______________
- "Found no counter-evidence" is NOT "hypothesis confirmed." "Found supporting work" is NOT
  causal proof. State this explicitly if either applies here.

## 6. Citation cards produced

List every `citation_card.yaml` id this search produced, with current `status`:
_______________
