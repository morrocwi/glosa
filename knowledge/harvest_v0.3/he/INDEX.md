# HE hub knowledge cards — K1-hub he (method layer of health/epistemics preprints)

Hub root: `10.5281/zenodo.22301465`. 18 members listed in `registry/zenodo_clusters.json` `hubs["he"].members`;
all 18 are distinct concept records (no version-dedup needed — each member DOI maps to a distinct `concept` id).
One member (`22302173`→concept `22302172`, "SANA"'s neighbor is unrelated — see table) had a Zenodo API link
failure at cluster-build time (`he.failed["17280895"]`, `metadata.dates` validation error) but its metadata was
still present in `registry/zenodo_all_records.json` and is used here (`kc-he-018`, `fetched_from_url` is the
nominal API URL, not a verified-live fetch — flagged in that card's `notes`).

Extraction scope per task: the METHOD layer only (epistemic/methodological/human-AI/evidence/disclosure/
authority content), not the domain (health) findings themselves — per K1-hub-he instructions, domain hubs are
mined for how-knowledge-is-made/checked content, not their substantive claims.

Source text used: local full text (`sources/CPRMH_v12.txt`) for the one record with a local copy
(`10.5281/zenodo.22301361`, "Coordinated Plaque Remodeling Modalities" — matched by title/content against
`sources/CPRMH_v12.txt`, confirmed via `sources/citation_cards/ZENODO_cprmh-v12.json`); the cached Zenodo
abstract (`desc` field in `registry/zenodo_all_records.json`, itself the `metadata.description` the registry
harvester already fetched from `https://zenodo.org/api/records/<id>`) for the remaining 17 records — no PDF
match was found in `~/Downloads` or in `~/ANSE.ASIA/readout_universe` / `readout_genesis` for any of the other
17 titles (checked by keyword grep against filenames).

## Cards

| id | kind | title | record DOI | tier | base_relation | glosa_use |
|---|---|---|---|---|---|---|
| kc-he-001 | method | Referral governance — separating clinical decision / info transfer / payment | 10.5281/zenodo.22302173 | Open | holds | adopt |
| kc-he-002 | method | SOMA-READ — frozen preregistration before ethics, before data | 10.5281/zenodo.22302190 | Open | open | adopt |
| kc-he-003 | rule | T-PHE — practitioner standpoint paired with cited tier-one evidence dossier | 10.5281/zenodo.22302161 | Open | holds | already_in_glosa |
| kc-he-004 | method | RRHM Open Lab — sealed prediction + independent reproduction | 10.5281/zenodo.22255211 | finite_diagnostic | holds | adopt |
| kc-he-005 | method | RRHM phobia model — pre-registered simulable falsification gates, failures disclosed | 10.5281/zenodo.22227003 | finite_diagnostic | holds | adopt |
| kc-he-006 | method | CPRMH — 17 pre-specified falsifiers locked before outcome access | 10.5281/zenodo.22301361 | Open | holds | adopt |
| kc-he-007 | method | CPRMH — versioned living-evidence object, machine-assisted + mandatory human adjudication | 10.5281/zenodo.22301361 | Open | holds | adopt |
| kc-he-008 | definition | Wellbeing from Informationism — repair-permissive coherence, not symptom absence | 10.5281/zenodo.20283074 | Open | holds | skip |
| kc-he-009 | definition | Health as constraint-admissible trajectory | 10.5281/zenodo.18813886 | Open | holds | skip |
| kc-he-010 | rule | AI-coached endurance training — admissibility-first, no-go before optimization | 10.5281/zenodo.18404721 | finite_diagnostic | holds | adopt |
| kc-he-011 | rule | Autonomic Safety — AI guidance bounded to GO/NO-GO, not clinical decision | 10.5281/zenodo.18281221 | Open | holds | adopt |
| kc-he-012 | definition | High Capability, Low Execution — finite causal capacity, not motivation deficit | 10.5281/zenodo.18264276 | Open | holds | skip |
| kc-he-013 | rule | Cellular Aging — falsifiable constraints without pathway/clinical claims | 10.5281/zenodo.18212478 | Open | holds | adopt |
| kc-he-014 | definition | Causal Psychology — failure as environmental impossibility, not deficiency | 10.5281/zenodo.18175678 | Open | holds | skip |
| kc-he-015 | rule | Life as Hazard Management — nondiagnostic, no new constants/prescriptions | 10.5281/zenodo.18174493 | Open | holds | adopt |
| kc-he-016 | rule | SANA runtime — explicit non-medical/psychiatric/legal scope in-spec | 10.5281/zenodo.17825408 | Open | holds | adopt |
| kc-he-017 | claim | AI-Cognitive Interaction — K0, SSRN-first, no priority claim, provenance disclosed | 10.5281/zenodo.22308448 | Open | holds | adopt |
| kc-he-018 | definition | Strong, Warm & Safe Family Ecosystem — policy brief, no stated falsification mechanism | 10.5281/zenodo.17280895 | Open | open | skip |
| kc-he-019 | rule | Systemic Repair Capacity Theory — novelty scoped to architecture, not mechanism | 10.5281/zenodo.20229203 | Open | holds | adopt |

## Counts

- Records: 18 (all 18 `he` hub members; none dropped)
- Cards: 19 (one extra card for the one record with local full text and a rich falsification-architecture
  section, `10.5281/zenodo.22301361` / CPRMH)
- `base_relation`: holds = 17, open = 2 (`kc-he-002` SOMA-READ — explicitly pre-data/pre-ethics; `kc-he-018`
  SWSF — no stated falsification mechanism in the abstract), refined_by_later_work = 0, superseded = 0,
  outdated = 0. No record in this hub uses vocabulary the base cards have since replaced.

## Adopt candidates (glosa_use: adopt)

kc-he-001, kc-he-002, kc-he-004, kc-he-005, kc-he-006, kc-he-007, kc-he-010, kc-he-011, kc-he-013, kc-he-015,
kc-he-016, kc-he-017, kc-he-019 — mostly targeting FOUNDATION §3.3 Kernel gate rules, §5 disclaimer catalogue,
§7.3 Bounded-Judge Law, and §7.9 Literature Review System. `kc-he-007` (CPRMH's machine-assisted-retrieval +
mandatory-human-adjudication clause) is the single strongest LRS precedent found in this hub.
