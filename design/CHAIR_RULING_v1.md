# Chair ruling v1 — the AI assistant, 2026-09-04 (binding input for FOUNDATION_v0.2)

> Tier: Dr. These are the orchestrator's rulings on the disputes the synthesis left open and on the
> review findings for S8–S13 (which FOUNDATION_v0.1 never read). Every ruling is subject to the
> founder's override; founder decisions that only the founder can make stay in §11 of the foundation.
> Inputs read: FOUNDATION_v0.1 (full), REPO_SPEC_v0.1 (outline), COMPLETENESS_CRITIC, all 28 reviews'
> verdicts + must-fix headlines, S3/S5 FAIL must-fix sections, HANDOFF requests 1–32.

## A. Founder rulings that arrived after/during synthesis — now binding on v0.2
A1. **Blackbox Note (บันทึกกล่องดำ)** replaces "Register Zero / R0 / เสียงสด" everywhere as the name of the raw-voice record (request 32). R0/R1/R2 survive only as internal stage labels. Renames: `templates/knowledge/blackbox_note.yaml` (ids `BB-YYYY-MM-DD-NN`), claim-card field `origin_blackbox_ref` (replaces both `origin_r0_ref` and `origin_dialogue_ref` — one field, one home), disclaimer `D-BLACKBOX-NOTE` (replaces `D-ORIGIN-DIALOGUE`), citation identifier kind `BLACKBOX_NOTE` (replaces the S8 gap / "DIALOGUE_RECORD"), mandatory appendix title **"Blackbox Note: how this work was made"**. The note has two parts: raw verbatim lines + the `cooking:` log (every transformation, by whom, which lines in, what distinction changed) — published with the work, never sealed.
A2. **No novelty/priority language anywhere** (request 31): remove "novelty", "novel", "first", "unprecedented", "prior art", "residual claim", "concession" from every design, the paper, and **the compiled LaTeX** (`disclaimers.tex` still says "D12 Novelty discipline" — regenerate both PDFs). Paper answers exactly three questions: which problem · by which method · how neighbours do it the same/differently (31d). The three-question form is also the literature-review scaffold (31e); wording same/different/cited; "adopted from" only when a human instructed it and a Blackbox line or decision id exists (31i).
A3. **Human–AI co-production** (request 24) visible per claim (`produced_by`, `responsible: human`) — already in v0.1 §3.2; keep. Human experience preserved (25); human-language question kept in the work (25b); important human proposals recorded with `became:` links (29); appendix curated, concise (30b).

## B. Rulings on §10 disputes
B1. **Genre taxonomy → 9 core genre rows + two cross-cutting attributes.** `genre ∈ {conceptual, empirical_quant, empirical_qual_practice, case_study, formal_proof, systematic_review, design_science, archival, position_reply}` (S11's 12 minus the three that are tracks) + `venue_track: international | thai_tci` + `companion_of: <artifact id> | null`. บทความวิชาการ = conceptual/systematic_review/position_reply with `venue_track: thai_tci`; บทความวิจัย = empirical_*/case_study with `venue_track: thai_tci`; Thai companion = any genre with `companion_of` set. S11's DAG content for the Thai rows is preserved as **track-specific section requirements** attached to the track, not as separate genre rows (PRESERVE_FUNCTION). Reason: request 21 (one stable system, fewer parallel rows) and the fact that S11's own genre 12 already treats Thai as an attribute.
B2. **Card granularity → two legal shapes, one schema.** `claim_card` with `shape: stub | full`. A **stub** (statement, standpoint, tier ≤ Dr, one falsifier, `non_claims` ≥1, `origin_blackbox_ref`, `ai_filled` as a single yes/no + one line, `produced_by`) is legal for K0 work and for cards NOT foregrounded in a paper. A **full** card is required for any card cited in a CLAIM_MATRIX, any card reaching tier ≥ fit_calibrated, and any card leaving the repo (K1). Kernel rule: a stub cannot be cited publicly and cannot advance past `Draft`. Reason: founder request 1 (ordinary people can start) outranks schema purity; silent lift is guarded by the "stub never leaves" rule.
B3. **ai-native-scholarship → cite as a dependency by name + version + DOI** (S12's recommendation); do not merge into `plugins/`. RWI re-derives only the protocol functions it needs, each with a PRESERVE_FUNCTION/EXPAND row in `lineage/RELATION_TO_STANDALONE_SCHOLAR.md`. (Founder decision item 4 remains a veto point.)
B4. **I3 stays the K1 floor; one bounded exception.** If a scholar can reach only one vendor, a claim may be published at K1 with I2 **plus** an I4 mechanical/original-record check, carrying `D-SAME-VENDOR` and `independent_check.expires_at` ≤ 90 days, after which an I3 route is mandatory or the card drops to K0. I3 is a **minimum, never sufficient** (fix S10's "sufficient" wording).
B5. **Local-model DVP route = best-effort, never mandatory.** It counts as I3 only when its model family is vendor-distinct from every other route; otherwise it is an I2 route in the matrix.
B6. **Ledgers per project, one rendered view.** `DISAGREEMENT_LEDGER.md` and `XENON_LEDGER.md` live in each project (one problem = one project), append-only; `rwi kg merge` renders the repo-wide view. Same pattern as the kg (one home per project, one view).

## C. Vocabulary convergence (request 21) — one definition, one home
C1. `independence_class` is the string ladder `I0..I5` in **every** schema (claim card, evidence relation, review report, citation card, kg edge). S4's 0–5 ordinal and S8's string enum are deleted as fields; the ordinal is a derived mapping in the kernel only.
C2. **One disclaimer catalogue** (`methodology/data/disclaimer_catalogue.json`). Register S8's citation-state disclosures (one id per citation state: `D-CITE-NOT-FETCHED`, `D-CITE-FETCH-FAILED`, `D-CITE-MISMATCH`, `D-CITE-CHALLENGED`, `D-CITE-SCRAMMED`, `D-CITE-SUPERSEDED` — or fold under `D-CITATION-UNVERIFIED` with a `state` parameter, synthesizer picks the simpler and says why), S10's `D-INDEPENDENCE` (must reuse S4's trigger; if S10's trigger differs, it becomes `D-INDEPENDENCE-LEVEL` with the level as parameter), S12's three advisor ids (already in v0.1), `D-BLACKBOX-NOTE`. Free-text `disclosure` fields become id references. Every id: trigger, bilingual wording, placement, mandatory flag.
C3. `fetch_status` enum: one enum (v0.1 §7.8's) reused by S13's neighbour table.
C4. `review_report.verdict_tier` enum = the six tiers of §4.1 (fix the 4-of-6 gap).
C5. `review_mode` enum includes `INTERNAL_DATA_AUDIT` (S8 dropped it from skillme's six; restore or record SUPERSEDE).
C6. Non-collapse table: append `NC-62 stakeholder ≠ agency`, `NC-63 Representationality ≠ Selectivity`, `NC-64 SelfExperience ≠ GeneralEvidence`; ids are append-only forever (S10 cites them by number). Local private skills cited as sources get `source_visibility: private_local` and a public re-derivation note.
C7. Lineage table adds **zero-readout-certifies** (CLAIM_MATRIX, check_repo.sh, check_version.py, CITATION triple, AI-disclosure section → PRESERVE_EXACT/EXPAND) and **readout_genesis `label_inflation_guard.py`** (tier-inflation lint → PRESERVE_FUNCTION into kernel rules 2–3).
C8. `origin_blackbox_ref` is the one origin field (A1). S8's citation card gets `identifier.kind: BLACKBOX_NOTE` with verification method `verbatim_diff_against_note`.

## D. Honesty placement fixes (critic §3, §5)
D1. §3.3 heading "the fixes — these are what final means" → "Kernel gate rules (specified, Dr, untested)". Every rule that is not yet executed says so where it is stated, not 500 lines later.
D2. State in §3.1 (not §12) that Q2 (`separates`) and completeness of Q3/Q4 are **presence-checkable, not correctness-checkable** by the kernel; correctness is exactly what the independent check (Q5) exists for. This is the Mechanical ≠ Semantic validity pair applied to RWI itself.
D3. Review-count sentence: "14 designs, 28 review passes, 1 critic, 1 chair ruling".
D4. S13 rows without a URL → `fetch_status: NOT_FETCHED`, tier Open; rewrite S13 into `neighbour_table.md` format under A2.
D5. FOUNDATION §12 keeps its "not read" list and adds: 169/180 Zenodo records unread (to be listed, not interpreted, in `lineage/PRIOR_WORK.md`).

## E. Structure of FOUNDATION_v0.2 (same 12 sections + appendices; changes)
- §1 adds the three-question positioning sentence and the "era of production / not competing with knowledge-authority" stance (31, 31b) as the paper's positioning paragraph.
- §2 spine diagram relabels R0 box as "Blackbox Note (raw lines)" and adds the cooking log as the trace that runs alongside the whole spine.
- §5 catalogue merged per C2. §6 per B1. §7.8 per C8. Appendix A per C6. Appendix B per A2/D4.
- New §13 "Chair rulings applied" — table: dispute/finding | ruling id | where applied.

## F. What stays open for the founder (unchanged from v0.1 §11, plus)
- B1–B4 are chair rulings the founder may overturn.
- Item 7 (who is I5) is the single most consequential open item: without a named external human, no RWI claim can ever be K2. Chair recommendation: the first I5 candidates are the founder's existing correspondents named in the Standalone Scholar's own K1→K2 ledger.
