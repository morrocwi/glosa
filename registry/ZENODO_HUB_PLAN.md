# Zenodo hub classification plan

Readout, not truth: this is a classification READOUT over 229 concepts (latest version per work) fetched from the public Zenodo API. No write to Zenodo has happened as part of this plan. See `registry/zenodo_all_records.json` for the fetched data and `methodology/P19_registration.md` for where new work registers.

## Source data

- `registry/zenodo_all_records.json` — all records by the author, all pages fetched, versions collapsed to one row per concept (Zenodo's own "latest version" determination, cross-checked against a second all-versions fetch: 342 total record-versions, 229 concepts).
- `registry/zenodo_hub_plan.json` — this plan in machine-readable form: one entry per concept id, each `{title, hub, rule_or_evidence, confidence, current_relations, proposed_new_isPartOf}`.
- Existing cluster/hub definitions and rules: `scripts/zenodo_cluster.py` (PRIMARY/TAGS regexes, OVERRIDE_PRIMARY/OVERRIDE_TAGS_ADD/REMOVE manual overrides, HUBS hub records); prior linked state: `registry/zenodo_clusters.json`.

## Method

1. **Rule pass** — applied `zenodo_cluster.py`'s own PRIMARY regex scoring (ep/he/ph, exclusive primary cluster) and TAGS regex matching (ai/islam/tourism/se; aihp/jps are curated-only series, no regex) verbatim, plus its OVERRIDE_PRIMARY / OVERRIDE_TAGS_ADD / OVERRIDE_TAGS_REMOVE manual override tables (resolved by concept id, since an override sometimes names an older version id of a concept than the one now "latest"). Hub index records themselves (title = a programme-index title, or containing "programme index") are marked `hub`, not a member.
2. **Evidence pass** — every concept where the rule pass produced a tie or a thin, wrong-leaning margin between two PRIMARY clusters (ep/he/ph score gap <=1, or top score <=2) was re-read by title and abstract; 5 of 229 needed a correction this way (table below) — all were ep/ph or ep/he close calls resolved by the paper's own stated subject, quoted verbatim in `zenodo_hub_plan.json`.
3. **needs_founder** — none. Every one of the 229 concepts resolved to at least one existing hub via rule or evidence; no concept was left with an empty hub list.
4. **New clusters** — none proposed. A concept always found a home among the 9 existing hubs (ep/he/ph/ai/islam/tourism/se/aihp/jps); no theme with >=8 concepts was left uncovered by them.

## Confidence tiers (229 concepts)

| confidence | count | meaning |
|---|---|---|
| rule | 224 | tool's own regex score or manual override table placed it (verbatim `zenodo_cluster.py` logic) |
| evidence | 5 | rule pass tied/ambiguous; resolved by quoting the record's own title/abstract |
| needs_founder | 0 | none — see Method §3 |

## Counts per hub (a concept may carry a primary hub plus tag-hubs, so columns sum to more than 229)

| hub | name | members | new `isPartOf` relations this plan would add (not yet applied) |
|---|---|---|---|
| `ep` | Epistemology programme | 73 | 11 |
| `he` | Health & mind programme | 18 | 0 |
| `ph` | Physics & information programme | 115 | 0 |
| `ai` | AI & knowledge programme | 46 | 10 |
| `islam` | Islam, Muslim society & knowledge authority programme | 13 | 0 |
| `tourism` | Muslim-friendly tourism & service programme | 6 | 0 |
| `se` | Social enterprise programme | 6 | 0 |
| `aihp` | When AI Expands Human Potential series | 37 | 2 |
| `jps` | Society, Justice, Peace & Violence series | 13 | 0 |

## Programme-index (hub) records themselves — 9

| concept id | title |
|---|---|
| 22301551 | Readout Universe — Artificial intelligence & knowledge programme index (Yaoharee Lahtee, 2026) |
| 22301458 | Readout Universe — Epistemology programme index (Yaoharee Lahtee, 2026) |
| 22301464 | Readout Universe — Health & mind programme index (Yaoharee Lahtee, 2026) |
| 22301553 | Readout Universe — Islam, Muslim society & knowledge authority programme index (Yaoharee Lahtee, 202 |
| 22301561 | Readout Universe — Muslim-friendly tourism & service programme index (Yaoharee Lahtee, 2026) |
| 22301468 | Readout Universe — Physics & information programme index (Yaoharee Lahtee, 2026) |
| 22301565 | Readout Universe — Social enterprise programme index (Yaoharee Lahtee, 2026) |
| 22342042 | Society, Justice, Peace & Violence — series index: structured coexistence, causal ethics, conflict a |
| 22308200 | When AI Expands Human Potential — series index: human–AI epistemic fusion, standalone scholarship, a |

## Evidence-pass corrections (5) — rule tied/leaned wrong, resolved by title/abstract

| concept id | title | final hub(s) | why (see `zenodo_hub_plan.json` for the full quote) |
|---|---|---|---|
| 20473229 | The Explanatory Insufficiency of Randomness | ep | title "The Explanatory Insufficiency of Randomness"; abstract argues objective chance cannot be a terminal explanans without a prior space of possibilities and a measure over it — … |
| 18772139 | Invariance and the Identity of a World A Minimal Structural  | ep | title "Invariance and the Identity of a World: A Minimal Structural Necessity Thesis"; abstract: "When distinct descriptions are said to concern the same world, what makes this cla… |
| 18133009 | Constructible Ordering from Distinguishable Steps | ep | title "Constructible Ordering from Distinguishable Steps"; abstract states the construction is made "without presupposing time, dynamics, probability, or physical structure" — the … |
| 17335198 | Epistemic Coherence_Yaoharee_proposal | ep | title itself is "Epistemic Coherence_Yaoharee_proposal" and the abstract opens "The Epistemic Coherence Equation (ECE)..." — the record's own title names its subject as epistemic. … |
| 19640360 | Mind as Information Horizon: From Primordial Difference to E | aihp, ep | title "Mind as Information Horizon: From Primordial Difference to Expertise Formation"; abstract: "What must reality minimally be if knowing—and therefore expertise—are to be possi… |

## needs_founder — none

No concept is listed here: every one of the 229 latest-version concept records resolved to at least one of the 9 existing hubs via the tool's own rule/override logic or, for 5 close calls between ep/he/ph, by quoting the record's own title/abstract (table above). If the founder disagrees with any assignment — rule-based or evidence-based — `registry/zenodo_hub_plan.json` records the exact reasoning per concept so any single entry can be corrected without redoing the pass.

## Checker corrections (2026-09-07, independent adversarial pass, no Zenodo write)

Two mechanical defects found in this plan file by a 40-concept sample check against live Zenodo titles/keywords/descriptions; both fixed in `registry/zenodo_hub_plan.json` directly (no reclassification judgment involved):

1. **Empty quoted-evidence artifact (92 `ph` entries).** `PRIMARY['ph']`'s own regex contains a capturing group (`informational (pixel|field|diffusivity)`), so Python's `re.findall()` silently returns the captured group instead of the full match — for every other `ph` alternative that fired, this produced the empty string `''`, rendered as `matched ['']`. The classification itself was independently re-checked against live title/keywords/description for every affected concept and is correct (genuine physics vocabulary each time — `physic`, `gravit`, `quantum`, `energy`, `mass`, `cosmolog`, etc.); only the displayed evidence quote was corrupted. Re-derived with a non-capturing group and recorded verbatim in each entry's `rule_or_evidence`.
2. **False-positive `islam`+`se` tags on 2 concepts (22302409, 22301885 — both versions of the same NIDA 2026-08-29 AI slide deck).** The `islam` and `se` TAGS regexes matched only on the author-affiliation boilerplate line in the record's own description ("ARAYA Nikah Social Enterprise"), not on the paper's actual subject (AI and the civilization of knowledge — no Islam or social-enterprise content). Removed both tags from `hub` in the plan file; `ai`/`aihp`/`ep` on these two records are genuine (confirmed against live title/keywords/description) and unchanged. Counts above updated (`islam` 15→13, `se` 8→6).
   - **Not fixed here (out of scope, needs founder-approved follow-up):** the *live* Zenodo metadata for both concepts already carries `isPartOf` to the islam hub (10.5281/zenodo.22301554) and se hub (10.5281/zenodo.22301566) — inherited by Zenodo's version-copy behavior from an earlier (2026-09-04) linking pass on a prior version of the same concept (record ids 22302410 / 22301886, see `registry/zenodo_clusters.json` `linked` state). Removing a wrong relation is not something `scripts/zenodo_add_relation.py` does (add-only) and was not attempted by this read-only checker pass.

No other concept in the 40-sample was found misclassified. Total concept count (229) re-verified against the live public API on 2026-09-07.

## Not done

- No write to Zenodo. This plan is a proposal only.
- No title, description, or file content was changed — read only, for classification.
- The Apply phase (adding `isPartOf` relations via `scripts/zenodo_add_relation.py` with `--founder-instructed "BBL-2026-09-07-232" --i-have-founder-approval`, metadata-only, on existing records) is a separate, later step, not run here.
