# TOURISM knowledge cards — K1-hub tourism (registry/zenodo_clusters.json hubs.tourism)

Hub anchor DOI: 10.5281/zenodo.22301562. 6 member records, all distinct concept DOIs (no version
dedup needed). Only one record (19059720, "Beyond Halal Labels") had local full text
(`~/Downloads/Beyond Halal Labels.pdf`, 33pp, read pages 1-6 only per RAM-slice rule); the other 5
are carried at Zenodo-abstract depth via `https://zenodo.org/api/records/<id>`. All 7 cards are
tiered **Open** — every source is either an explicit "preprint — not peer reviewed" conceptual
paper, or a compiled dataset whose own author disclaims interpretive analysis; none carries a
Th_coqc/finite_diagnostic/Dr result to elevate it past Open.

Extraction focus per task: the method/epistemic layer of each tourism paper (scope-disclosure,
data/inference separation, gap-naming, claim-typing), not the domain tourism findings themselves.

| id | kind | title | source doi | tier | base_relation | glosa_use |
|---|---|---|---|---|---|---|
| kc-tourism-001 | claim | PCS generalized as scale-invariant mechanism, own limits named | 10.5281/zenodo.19115417 | Open | holds | skip |
| kc-tourism-002 | claim | Premature category stabilization — provider-side mechanism, not certification sufficiency | 10.5281/zenodo.19059720 | Open | open | skip |
| kc-tourism-003 | method | 'Proves vs. still cannot explain' gap statement before advancing a new mechanism | 10.5281/zenodo.19059720 | Open | holds | adapt |
| kc-tourism-004 | method | Behavioral dataset compiled with interpretation deliberately excluded | 10.5281/zenodo.17305576 | Open | holds | already_in_glosa |
| kc-tourism-005 | method | Statistical dataset from named institutions, analysis explicitly withheld | 10.5281/zenodo.17305534 | Open | holds | already_in_glosa |
| kc-tourism-006 | claim | Cultural-Based Practitioner framework from cross-national case studies | 10.5281/zenodo.17281646 | Open | open | skip |
| kc-tourism-007 | rule | Contribution explicitly typed theoretical/analytical, empirical findings disclaimed | 10.5281/zenodo.18258377 | Open | holds | already_in_glosa |

## Records covered (6/6, all members)

1. 10.5281/zenodo.19115417 — From Intercultural Marriage to State Policy: PCS as a Scale-Invariant
   Mechanism of Cultural Failure (2026-03-20) → kc-tourism-001
2. 10.5281/zenodo.19059720 — Beyond Halal Labels: Premature Category Stabilization in
   Muslim-Friendly Tourism (2026-03-17, hub anchor) → kc-tourism-002, kc-tourism-003
3. 10.5281/zenodo.17305576 — Behavioral Dataset of Muslim Tourists in Thailand (2024–2025)
   (2025-10-09) → kc-tourism-004
4. 10.5281/zenodo.17305534 — Statistical Dataset of Muslim and Malaysia-Origin Tourists Visiting
   Thailand (2024–2025) (2025-10-09) → kc-tourism-005
5. 10.5281/zenodo.17281646 — Faith in Service Systems: Dynamics of Cultural-Based Practitioners
   (2025-10-06) → kc-tourism-006
6. 10.5281/zenodo.18258377 — From Ritual Compliance to Predictable Cultural Experience: A
   Conceptual Framework for Cross-Cultural Tourism (2025-01-15, hub anchor) → kc-tourism-007

## base_relation counts

holds: 5 (kc-tourism-001, 003, 004, 005, 007) · refined_by_later_work: 0 · superseded: 0 ·
outdated: 0 · open: 2 (kc-tourism-002, 006)

## Notes on outdated/superseded

None of the 6 records is judged outdated or superseded against the base cards — these are all
2025-2026 conceptual/dataset papers in an unrelated domain (Muslim-friendly tourism), none of
which uses vocabulary the base later replaced (no continuum-math, angle, or infinity/zero language
at stake). All "open" or "holds" only.

## adopt/adapt candidates for glosa's own kernel

- kc-tourism-003 (adapt) → FOUNDATION §7.9 Literature Review System / §12 Honest edges: adapt the
  paper's explicit "proves X / still cannot explain Y" two-part split as a required sub-field of a
  glosa literature-review entry.
- kc-tourism-004, kc-tourism-005, kc-tourism-007 (already_in_glosa) → concrete real-world instances
  confirming FOUNDATION §2.1b (Data→Inference→Claim separation) and §3.2b (claim-type disclosure)
  are not just internal aspiration — external authors in this domain already practice the same
  discipline independently.
