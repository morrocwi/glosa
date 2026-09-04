# ISLAM hub knowledge cards — K1-hub islam (method layer of Islamic-scholarship/social-enterprise preprints)

Hub root: `10.5281/zenodo.22301554`. `registry/zenodo_clusters.json` `hubs["islam"].members` lists 16 DOIs;
one pair (`10.5281/zenodo.22302410` and `10.5281/zenodo.22301886`) is a byte-identical duplicate Zenodo
deposit — same title, same date (2026-08-29), same `desc` field — so it is treated as one concept-record
version per the K1 dedupe instruction, keeping the newer-numbered DOI (`22302410`) and giving it the card.
**15 unique records → 16 cards** (one member, `10.5281/zenodo.22206607`, carries two cards for two distinct
method-layer claims; one member, `10.5281/zenodo.22302161`, is a cross-hub duplicate already fully mined as
`kc-he-003` in the `he` hub and gets a thin pointer card here).

Extraction scope per task: the METHOD layer only (epistemic/methodological/human-AI/evidence/disclosure/
authority content), not the domain (Islamic-scholarship, tourism, health) findings themselves — domain hubs
are mined for how-knowledge-is-made/checked content, per K1-hub-islam instructions.

Source text used: local PDF full text (`pdftotext -l 1-2`, matched by title/abstract against a Zenodo record)
for 7 of the 15 records, found in `~/Downloads` — no matches were found in `sources/`, `~/ANSE.ASIA/readout_universe`,
or `~/ANSE.ASIA/readout_genesis` for any islam-hub title. The cached Zenodo abstract (`desc` field already
present in `registry/zenodo_all_records.json`, itself fetched by the registry harvester from
`https://zenodo.org/api/records/<id>`) was used for the remaining 8 records; `fetched_from_url` on those
cards names that same API URL. One record (`10.5281/zenodo.22302410`) is a 58 MB slide-deck PDF found locally
but not opened — its cached Zenodo abstract was used instead, per the RAM-low rule (no large PDF is loaded
beyond a `pdftotext -l` page-range slice, and this one was skipped rather than partially parsed).

## Cards

| id | kind | title | record DOI | tier | base_relation | glosa_use |
|---|---|---|---|---|---|---|
| kc-islam-001 | rule | Practitioner standpoint paired with cited evidence, no clinical recommendation (islam-hub angle) | 10.5281/zenodo.22302161 | Open | holds | already_in_glosa |
| kc-islam-002 | claim | Revelation is not fallible; the human juristic determination of it is | 10.5281/zenodo.22206607 | Open | holds | adopt |
| kc-islam-003 | claim | Functional sacralization of fiqh — human determinations acquiring practical sacred-normativity | 10.5281/zenodo.22206607 | Open | holds | adopt |
| kc-islam-004 | claim | AI-mediated society risks the human forgetting their own status as chooser and responsibility-bearer | 10.5281/zenodo.22302410 | Open | holds | adopt |
| kc-islam-005 | definition | Epistemic hardening — declining social revisability of human interpretive claims | 10.5281/zenodo.22129490 | Open | holds | adopt |
| kc-islam-006 | method | Every doctrine states the conditions under which it would be defeated | 10.5281/zenodo.21439275 | Open | holds | adopt |
| kc-islam-007 | method | Power-literate satire framework offered as analytical tool, not normative verdict | 10.5281/zenodo.20159825 | Open | holds | adopt |
| kc-islam-008 | claim | Knowledge as the residue of beliefs that survived the world's resistance | 10.5281/zenodo.19951961 | Open | holds | adopt |
| kc-islam-009 | rule | Layer confusion — applying one layer's tools/authority to a question belonging to another layer | 10.5281/zenodo.19124963 | Open | holds | adopt |
| kc-islam-010 | definition | Premature Category Stabilization as scale-invariant mechanism; peace defined by three structural conditions | 10.5281/zenodo.19115417 | Open | holds | adopt |
| kc-islam-011 | claim | Premature category stabilization — provider-defined service templates precede and distort diversity | 10.5281/zenodo.19059720 | Open | holds | adapt |
| kc-islam-012 | tool | Behavioral dataset explicitly withholds interpretive commentary | 10.5281/zenodo.17305576 | Dr | holds | adopt |
| kc-islam-013 | tool | Statistical dataset compiled from named sources, explicitly excludes interpretive analysis | 10.5281/zenodo.17305534 | Dr | holds | adopt |
| kc-islam-014 | claim | Dialogue quality, not the interlocutor's nature, determines whether wisdom or distortion results | 10.5281/zenodo.22308451 | Open | holds | adopt |
| kc-islam-015 | method | Cultural-Based Practitioners framework converts faith/cultural capital into verifiable value | 10.5281/zenodo.17281646 | Open | holds | skip |
| kc-islam-016 | claim | Contribution declared theoretical/analytical, not empirical, up front | 10.5281/zenodo.18258377 | Open | holds | adopt |

## base_relation summary

All 16 cards were judged `holds` against the base cards (`base/INDEX.md`) — every islam-hub record's
method-layer content is either a domain-specific instance of a base epistemic principle (readout-vs-truth,
tier discipline, Fail-Able Gate Law, falsifiable-claims table, Data→Inference→Claim separation) or an
independently-derived analogue that does not contradict one. No islam-hub record uses vocabulary a base card
later replaced, so no card is `superseded`/`outdated`/`refined_by_later_work`; none required an `open`
(unjudgeable-against-base) verdict — each had a clear structural parallel to name.

## adopt_candidates (glosa_use: adopt or adapt)

kc-islam-002, kc-islam-003, kc-islam-004, kc-islam-005, kc-islam-006, kc-islam-007, kc-islam-008,
kc-islam-009, kc-islam-010, kc-islam-011 (adapt), kc-islam-012, kc-islam-013, kc-islam-014, kc-islam-016.

## skip / already_in_glosa

- kc-islam-001 (`already_in_glosa`): same record as `kc-he-003`; no new extraction beyond confirming the
  cross-hub tag.
- kc-islam-015 (`skip`): abstract-level method-layer content too thin (a named framework, no stated
  verification procedure) to adopt without reading the full paper.
