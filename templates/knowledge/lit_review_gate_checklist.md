# Literature Review gate checklist — RWI S14 template (Dr, unreviewed)

> Run this checklist before drafting ANY lit-review prose, and again before it may be cited from
> a genre DAG's lit-review section (S11) or pass the release gate (S6/§7.4). A `NO` on any
> **hard-gate** item blocks; a `NO` on a **disclose** item requires the named disclaimer, not a
> block.

## 0. Trigger and scope
- [ ] hard-gate — This LRS run is tied to exactly one lens-out hypothesis (`hypothesis_ref`), not
      a whole paper or whole project.
- [ ] hard-gate — `litreview_manifest.yaml.status == FROZEN`.

## 1. Honest label
- [ ] hard-gate — `search_log.yaml.review_mode` is one of `SYSTEMATIC_REVIEW | SCOPING_SEARCH |
      TARGETED_SEARCH | RAPID_EVIDENCE_CHALLENGE | FIELD_OBSERVATION_LOG | INTERNAL_DATA_AUDIT`,
      and matches what was actually done (FC-S8-1: never call anything less than a full protocol
      a systematic review).
- [ ] disclose — `D-LIT-MODE` emitted wherever the lit-review section is read, stating the mode.

## 2. Acquisition and the secondary-citation ban
- [ ] hard-gate — Every citation appearing with a stance (agrees/disagrees/orthogonal) in a
      `dialogue_table.md` row has `acquisition_status: obtained` (or `abstract_only` with `scope`
      restricted to `SUPPORTS_GENERAL_CLAIM_ONLY`/`CONTEXT_ONLY_NOT_EVIDENCE` only — never a direct
      quotation from an abstract-only source).
- [ ] hard-gate — `secondary_citation_ban_audit.violations_found == 0` (never cite what was not
      opened).
- [ ] disclose — Every `not_obtained` candidate still listed in the search log carries `D-LIT-
      NOT-OBTAINED` and is excluded from the dialogue table's stance columns.

## 3. Citation-card verification (the "best a human can do" standard)
For every citation_card reachable from this manifest:
- [ ] hard-gate — `identifier.kind` + `identifier.value` present and not a bare unstable URL.
- [ ] hard-gate — `metadata_verified == true` via Crossref/OpenAlex/PubMed/DataCite (or
      `UNCHECKED_OFFLINE`, honestly labeled, re-run online before this gate is re-checked).
- [ ] hard-gate — `claim_match_verified == true`, verified by a named human (I5) OR a decorrelated
      I3 AI route — never the same route/model that produced the citing sentence (MC-02).
- [ ] hard-gate — `exact_passage` is a verbatim quote or precise locator, not a paraphrase
      standing in for the check.
- [ ] hard-gate — `retraction_check != RETRACTED`.
- [ ] hard-gate — `version_status` resolved (PREPRINT vs PUBLISHED vs BOTH_LINKED) — a preprint
      cited as if it were the peer-reviewed version of record is a `METADATA_MISMATCH`-class
      Xenon-ledger error.
- [ ] hard-gate — Spot-check requirement met: `accuracy.spot_check.spot_check_result == PASS`
      (see S14 §5.4 for the proposed n%), or `spot_check.applicable == false` because every card
      is already `HUMAN_I5`-verified.
- [ ] hard-gate — No citation in scope has `status: SCRAMMED` (immediate hard block + Xenon ledger
      row, per §7.8).

## 4. Diversity audit (accuracy and diversity are two SEPARATE gates)
- [ ] hard-gate — `diversity_audit` block populated (not skipped) — language, discipline,
      source_type, search_route_or_database, geography_or_institution, stance all counted.
- [ ] disclose — Every entry in `concentration_flags` carries `D-LIT-CONCENTRATED`.
- [ ] disclose — `zero_disagree_flag`, if true, is stated explicitly next to the dialogue table,
      not silently left as an apparent unanimous agreement.
- [ ] hard-gate — Prose anywhere citing this manifest never asserts "diverse sources" or
      "comprehensive coverage" without pointing at the `diversity_audit.counts` block.
- [ ] disclose — `strata_table` shows spread reported WITHIN each quality tier, not only overall,
      whenever `venue_quality_index` is used to select or describe sources (request 35f) —
      `venue_quality_index` never substitutes for `claim_match_verified` (Legitimacy ≠ Truth).

## 5. The dialogue table itself (request 35c form)
- [ ] hard-gate — Rows are not ordered by date/priority/"seminal" language; date is metadata only.
- [ ] hard-gate — Every row with agrees/disagrees populated points to a `claim_match_verified:
      true` citation_card (§3 above).
- [ ] hard-gate — At least the "what it would say against us" column is attempted for every row
      (may legitimately read "not determinable from fetched text").

## 6. Neighbour table and wording (rule 31d–31i)
- [ ] hard-gate — Comparison language is same/different/cited only; "adopted from" appears only
      where an R0/Blackbox line or logbook decision id records the human instructing the adoption.
- [ ] hard-gate — No priority language (see the priority-language list enforced by scripts/check_forbidden_words.sh) anywhere in the lit-review
      section (chair ruling A2).

## 7. Manifest freeze and downstream gate
- [ ] hard-gate — `gate.accuracy_gate ∈ {PASS, PASS_WITH_LIMITS}`.
- [ ] hard-gate — `gate.overall ∈ {PASS, PASS_WITH_LIMITS}` before the lit-review section may be
      drafted in `paper/main.md`; `FAIL` blocks drafting entirely, not just publishing.
- [ ] hard-gate — Before publish (S6/§7.4 PUB-ADVERSARIAL-REVIEW), an INDEPENDENT reviewer (not
      the manifest's own maker) re-runs this checklist — a self-check does not count (MC-02).

## 8. Hypothesis-selection linkage (if this manifest fed a selection decision)
- [ ] disclose — `hypothesis_selection.yaml` references this manifest's `gate.overall` value
      honestly at the time of selection, even if selection proceeded despite `PASS_WITH_LIMITS`
      or `FAIL` (a promising, under-evidenced hypothesis may still be chosen — disclosed, not
      hidden).
