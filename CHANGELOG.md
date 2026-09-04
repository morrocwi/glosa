# CHANGELOG
## 0.3.0 — 2026-09-05
- FOUNDATION_v0.6.md / REPO_SPEC_v0.6.md: assembled from FOUNDATION_v0.5.md/REPO_SPEC_v0.5.md +
  every READY section of `design/FOUNDATION_v0.6_PATCH.md`/`design/REPO_SPEC_v0.6_PATCH.md`.
  `design/CURRENT_SPEC.txt` now names this pair. Design-docs-only pass — no schema/kernel/template
  file this document describes was itself edited by the FOUNDATION/REPO_SPEC merge (templates
  updated separately, see below).
- **Shipped without a founder gate (kernel-closure rules, closing named K4 sim-confirmed defect-
  detection gaps):** rule 26 composite-quote detector, rule 27 hidden-AI-fill detector, rule 28
  inflated-bearing detector (§7.8). Rules 15–17 (responsibility arrow/ownership, empirical-
  extension warning, source-first citation — already shipped in `kernel/glosa_kernel.py` before
  this pass) folded into FOUNDATION §3.3's numbered prose for the first time. New schema fields
  (additive/optional, target `schema_version: "0.7.0"`): `comparison`, `evidence_strength`,
  `verdict_class`, `gate_fail_taxonomy`, `gate_construction_status`,
  `five_questions.seen.ai_assisted_fields` — spec only, not yet applied to `schema/
  claim_card.schema.json` on disk. `templates/knowledge/litreview_manifest.yaml` gains
  `citations[].intake_tier`/`intake_tier_reason`/`global_south_exempt` and a `discovery_routing`
  block. Appendix A gains Family J (`NC-74`..`NC-76`; 76 rows across nine families).
- **Pending founder decision (recommended text specified, not ratified):** genre-router
  layer-mismatch diagnostic promotion (`promote-from-revise-to-ship-gate`, this patch's own
  proposal, not DAG-mandated), LRS claim-tier intake flag (`thin-layer-scope-confirmation`), PCS
  red-flag (`PCS-scoping-confirmation`), partial theology-neutral ontology analogue
  (`partial-analogue-adoption`), per-instance vs. standardized non-clinical/legal scope clause
  (`per-instance-vs-standardized-disclaimer`), LRS discovery-routing extension
  (`discovery-routing-stage-adoption`). None of these six is committed to `DECISIONS.yaml` or
  built until the founder rules (`EPIS-KNOWLEDGE-VALIDATION` — no external validation lever, the
  founder is the internal decision owner).
- **Tooling gaps this run found, not fixed this pass:**
  - **I3 route fixes:** rule 18's original draft mis-scanned for a match against kernel rule 8's
    unrelated `EXTERNAL_VALIDATION_PROPOSED` scan before a review response corrected it to a
    standalone new scan; the injected-infinity/zero taxonomy itself was also corrected from an
    invented epistemic/rhetorical vocabulary to `kc-base-016`'s real, verbatim physics/math
    continuum-injection taxonomy (I1–I4/Z1–Z4) — both flagged as I3-cross-vendor-caught corrections
    in `design/FOUNDATION_v0.6_PATCH.md`'s own review-response table, not as clean first drafts.
  - **Leak-scan rewrite:** `scripts/check_leak.sh` (34 un-allowlisted hits) and
    `scripts/check_forbidden_words.sh` (162 un-allowlisted hits) both still exit non-zero against
    the pre-existing corpus (`design/REPO_SPEC_v0.5.md` §9) — this pass is design/-only scope and
    does not touch either script; a leak-scan rewrite is named here as an open gap, not silently
    treated as fixed.
  - **Spot-check:** no independent (I2+) check has run on this synthesis pass, on the K-C1/K-C2/
    K-C3 kernel-closure rules, or on the six pending-founder recommended-text blocks — every one
    of them is K0/Dr, single-pass, same-model (this session's own maker-checker-gate finding
    applies, per `PUB-ADVERSARIAL-REVIEW`'s fail-closed rule: no independent check ⇒ no release).
    A held-out, differently-worded fixture batch (`tests/sim/corpus_v2/`, `[planned]`) is required
    before several of these rules' acceptance tests can be honestly re-run (§6's layer-confusion
    diagnostic, §5's verdict-class literal enum test, §23's discovery-routing precision/recall
    comparison).
## 0.2.0 — 2026-09-05
- Published: repository DOI 10.5281/zenodo.22307843 (archive tree = commit e6f9642; the tagged commit adds only the DOI pointers in CITATION.cff/README/CHANGELOG and the registry `released` row) (concept 10.5281/zenodo.22301059); concept paper DOI 10.5281/zenodo.22307841; GitHub tag v0.2.0.
- glosa applied to itself: concept paper (English, arXiv two-column) produced through the full spine — problem card, Blackbox Note, lens translation, three hypotheses selected by the founder, literature review system with 48 citation cards VERIFIED by a cross-vendor route under rule 17 (link + page + line + verbatim), own-lineage collision rows, claim cards reviewed by nine cross-vendor routes and revised (dissent preserved), publish gate v2.
- New rules from the run: rule 15/16 (responsibility per arrow, ownership of problem/question/hypothesis-selection, empirical extension), rule 17 (source-first citation), gate rule 9 (no AI attribution without permission); lit manifest fails closed on non-conformant cards; CLI writes repo-relative refs; pre-commit leak hook; install.sh / doctor / CI install test.
- Vendor names removed from all attribution surfaces; public git history rewritten to strip AI co-author trailers (founder ruling 2026-09-05).
- Zenodo: Bounded Knower series (Papers I–III) published and cross-linked; Blackbox Log updated through v15+.
## 0.1.0 — 2026-09-04
- Published: Zenodo DOI 10.5281/zenodo.22301060 (concept 10.5281/zenodo.22301059); GitHub morrocwi/glosa tag v0.1.0.
- Registry self-report: GLS-2026-001 stays at stage `genre_routed` — the registry state machine refuses `method…released` without a literature-review manifest, and this paper was released with a positioning table, not an LRS run (D-LIT-MODE). The system reports the gap on itself; closing it = run the LRS for this paper in 0.2.
- First public working release (K0: timestamped, citable, not peer reviewed, no independent check yet). Kernel 134 tests green, CLI/MCP/plugin, 20 schemas, methodology cards P00–P14, paper (design-science, Dr), Blackbox Log (concept DOI 10.5281/zenodo.22302518), 7 Zenodo programme hubs, research map. Publish gate v1 ran: 11 BLOCKs fixed before push (see reviews/PUBLISH_GATE_v1.md). All content tier Dr unless a test says otherwise.
- Adopted (founder instruction 2026-09-04, BBL-086/087): ownership criterion — problem, question, and the selection of the hypothesis stay human (BBL-088 wording) (FOUNDATION §2.1c, responsibility.ownership, kernel rule 15).
- Adopted (founder instruction 2026-09-04, BBL-083/084): problem-first spine wording, responsibility per Data→Inference→Claim arrow (rule 15), optional empirical_extension (operationalization, study design, bias register, robustness), P15 card.
- Paper: EN and TH texts and the LaTeX source (`paper/main_en.md`, `paper/main_th.md`, `paper/latex/`) were aligned on the D-LENS-UNCITED lens-citation status and on the "Positioning table" section naming.
## 0.0.1-draft — 2026-09-04
- Bootstrap: FOUNDATION_v0.5 (Dr), REPO_SPEC_v0.5, chair ruling, 14 knowledge templates, 2 compiled LaTeX templates, lineage (180 Zenodo rows), Blackbox Note drafts (not curated, not public).
- Nothing executable yet. Tier of everything: Dr.
