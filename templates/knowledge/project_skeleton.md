# Project skeleton — RWI S8 template (Dr, unreviewed)

> "One problem = one project" (หนึ่งปัญหาหนึ่งโปรเจ็กต์). Every declared research problem
> (S1 intake output) gets exactly one directory below; every directory answers exactly one
> problem. See `S8_knowledge-infrastructure.md` §4 for the split test and rationale.

```
<problem-slug>/
├── README.md
│     # What problem, from what standpoint (social-enterprise practitioner / citizen / etc.),
│     # and current status at a glance. First thing a human or AI reads to orient.
│
├── CLAIM_BOUNDARY.md
│     # What this project does and does NOT claim to establish. Must be statable without
│     # using the word "and" — if it needs "and," the project should split (§4.3).
│
├── ASSUMPTIONS.md
│     # A1, A2, A3, ... — named, numbered assumptions this project's claims depend on.
│     # Paired 1:1 in spirit with NON_CLAIMS.md (re-derived from an internal repo pattern).
│
├── NON_CLAIMS.md
│     # NC1, NC2, NC3, ... — explicit statements of what this project does NOT claim,
│     # even though a reader might assume it from the results shown.
│
├── claims/
│   └── claim-<nnn>.yaml
│         # One claim_card.yaml per claim (S4 schema). Q1-Q5 (seen/separates/ai_filled/
│         # assumed/tested), tier, standpoint, evidence_relations[] pointing at citation cards.
│
├── sources/
│   └── citation_card_<slug>-<nnn>.yaml
│         # One citation_card.yaml per citation USE (S8 §1). Never inline free-text citations
│         # in claims/ or paper/ — always point here by id.
│
├── kg/
│   ├── nodes.jsonl
│   │     # This project's own knowledge-graph nodes (claim/source/equation/project/
│   │     # person_role/concept), generated from the card files above, not hand-maintained.
│   └── edges.jsonl
│         # This project's own typed relations (supports/challenges/derives_from/borrows/
│         # supersedes/cites) between nodes above and, via borrows/derives_from only,
│         # nodes in other projects.
│
├── paper/
│   ├── main.md          # manuscript, Thai source-of-truth per repo language convention (TBD, §9 open q)
│   ├── main_en.md        # English version — rewritten, not translated, per workspace rule
│   └── CLAIM_MATRIX.md   # prose claim <-> backing claim_card/citation_card id, one row per claim
│
└── reviews/
    └── YYYY-MM-DD_<reviewer-role>.md
          # Dated independent adversarial review reports — the MIMCG evidence bundle for this
          # project (maker != checker != approver; same-model self-review does not count).
```

## Splitting checklist (from S8_knowledge-infrastructure.md §4.3)

A project must split into two when ANY of the following becomes true:

- [ ] `CLAIM_BOUNDARY.md` needs "and" to state its scope.
- [ ] Two claims in `claims/` have contradictory `ASSUMPTIONS.md` entries.
- [ ] The evidence search (`search_log.yaml`) had to freeze two unrelated `frozen_scope`
      concept sets because one search couldn't honestly cover both.
- [ ] A reviewer cannot restate the project's thesis in one sentence without using "also."
