# K1-hub se — social-enterprise hub knowledge cards

Hub `se` (registry/zenodo_clusters.json `hubs["se"]`, hub DOI `10.5281/zenodo.22301566`).
8 members listed; deduped to 7 unique concept records by dropping `10.5281/zenodo.22301886`
(a same-day, same-title, same-abstract duplicate deposit of `10.5281/zenodo.22302410` — kept
the higher/newer record id). Extraction focus per task: the method layer of each record — how
each paper makes, tiers, bounds, discloses, or checks its own knowledge claims — not its
domain (social-enterprise) findings themselves.

12 cards total.

| id | kind | title | record (doi) | tier | base_relation | glosa_use |
|---|---|---|---|---|---|---|
| kc-se-001 | rule | Descriptive-only comparison table — no outperformance claim | 10.5281/zenodo.22302161 (T-PHE) | Open | holds | adopt |
| kc-se-002 | rule | Adjacent evidence ≠ evidence the intervention works | 10.5281/zenodo.22302161 (T-PHE) | Open | holds | adopt |
| kc-se-003 | rule | Five-tier claim ladder (Th-coqc…NI/Open) | 10.5281/zenodo.22301882 (MOCA) | definition | holds | adopt |
| kc-se-004 | rule | Unidentified values return NI, never zero | 10.5281/zenodo.22301882 (MOCA) | definition | holds | adopt |
| kc-se-005 | definition | Readout non-equivalence, R=K·θ(E)+η in an enterprise data model | 10.5281/zenodo.22301882 (MOCA) | definition | refined_by_later_work | adapt |
| kc-se-006 | rule | Reflexive practitioner-inquiry disclosure (own org as illustration) | 10.5281/zenodo.22227005 (Why We Became an SE) | Open | holds | adopt |
| kc-se-007 | method | Prior-art review: "partially anticipated, not found in formulation" | 10.5281/zenodo.22227005 (Why We Became an SE) | Open | holds | adopt |
| kc-se-008 | claim | Candidate Forgetting | 10.5281/zenodo.22302410 (AI & Knowledge Civilization slides) | Open | holds | adopt |
| kc-se-009 | rule | AI Governance → Epistemic Governance | 10.5281/zenodo.22302410 (AI & Knowledge Civilization slides) | Open | holds | adopt |
| kc-se-010 | method | CBP framework — descriptive, not an outcome claim | 10.5281/zenodo.17281646 (Faith in Service Systems) | Open | outdated | skip |
| kc-se-011 | method | SWSF policy brief — eight dimensions, four mechanisms | 10.5281/zenodo.17280895 (SWSF) | Open | outdated | skip |
| kc-se-012 | method | Simulation-battery evidence, stated as finite_diagnostic | 10.5281/zenodo.18506938 (TTD v3) | finite_diagnostic | refined_by_later_work | adapt |

## Records covered (7 unique, after dedup)

1. `10.5281/zenodo.22302161` — T-PHE (2026-09-02) — local full text (RE_T-PHE repo, private working tree)
2. `10.5281/zenodo.22301882` — MOCA (2026-09-02) — local full text (~/Downloads PDF)
3. `10.5281/zenodo.22227005` — Why We Became a Social Enterprise (2026-09-01) — local full text (~/Downloads PDF)
4. `10.5281/zenodo.22302410` — AI & the Civilization of Knowledge, NIDA slides (2026-08-29, kept; dupe `22301886` dropped) — local full text (~/Downloads PDF)
5. `10.5281/zenodo.17281646` — Faith in Service Systems / CBP (2025-10-06) — Zenodo abstract only
6. `10.5281/zenodo.17280895` — Strong, Warm & Safe Family Ecosystem (2025-10-06) — Zenodo abstract only (cached in registry/zenodo_all_records.json; live API call for this DOI fails validation per `registry/zenodo_clusters.json` "failed" entry)
7. `10.5281/zenodo.18506938` — TTD v3 survival model (2025-02-06) — Zenodo abstract only (truncated at API description length limit)

## base_relation summary

- **holds** (8): kc-se-001, 002, 003, 004, 006, 007, 008, 009 — consistent with, or an independently
  convergent restatement of, the base tier/disclosure/comparison discipline.
- **refined_by_later_work** (2): kc-se-005, kc-se-012 — both are earlier-stage constructs (MOCA's raw
  readout equation; TTD v3's simulation battery) that the same author's own later se-hub paper (MOCA's
  explicit five-tier ladder, kc-se-003) folds in and gives an explicit tier label to.
- **outdated** (2): kc-se-010, kc-se-011 — both 2025-10-06 policy/framework papers with no explicit
  claim-tier language, superseded in vocabulary by this corpus's own later tier-discipline statements
  (kc-base-007, kc-se-003).
- **superseded** (0), **open** (0): none this pass.

## Adopt candidates (glosa_use: adopt or adapt)

- kc-se-001, kc-se-002 — comparison-table and evidence-scope wording templates for FOUNDATION §3.
- kc-se-003, kc-se-004 — tier-ladder and NI-not-zero rule, cross-reference against glosa's own six-tier
  vocabulary (different spelling/granularity — comparison = different, cited, not superseding).
- kc-se-005 (adapt), kc-se-012 (adapt) — worked cross-domain instances of the base mother equation and
  of finite_diagnostic simulation evidence.
- kc-se-006, kc-se-007 — standpoint-disclosure and prior-art-comparison wording templates.
- kc-se-008, kc-se-009 — Candidate Forgetting / Epistemic Governance, independently-worded convergent
  statements of glosa's own readout-not-truth and maker≠checker rules; strong candidates for FOUNDATION
  §1 and §5.

## Notes / gaps

- kc-se-010 and kc-se-011 had no local full text under `sources/` or `~/Downloads`; only the Zenodo
  abstract was available, per task fallback rule. Case-study and dimension-level detail (CBP's three
  country cases; SWSF's eight dimensions/four mechanisms named individually) was not extracted — would
  need the full paper for a closer method-layer read.
- kc-se-012's abstract text is cut off mid-sentence at the Zenodo API's description-length limit; the
  numeric ±30%-shock survival value is not available from this source and is not asserted in the card.
