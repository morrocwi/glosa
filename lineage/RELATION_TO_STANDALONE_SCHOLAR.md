tier: Dr (specified; independently unreviewed)

# Relation to The Standalone Scholar — anchor-preservation ledger

> Readout, not truth. This file is the ledger `design/FOUNDATION_v0.3.md` §1.3 and §1.2 both point
> to and both say must exist "here." Two honest gaps, stated up front rather than papered over:
> (1) the full 17-row anchor-preservation table is described in `FOUNDATION_v0.3.md` §1.3 as
> "carried forward unchanged... incorporated here by reference" from a file named
> `FOUNDATION_v0.1.md` — that file **does not exist on disk** in this design lineage (only
> `the internal build plan (local file, not public)`, `FOUNDATION_v0.2.md`, `FOUNDATION_v0.3.md` do). The 17 invariants themselves are
> real and locatable — they are the "Semantic invariant checklist" in the ancestor skill's own
> `templates/anchor-preservation-audit.md` (`ai-native-scholarship v1.0.0`, PUB, cited below) —
> but the *specific v0.1 mapping prose* for each row was never captured a second time anywhere
> this design round can point to except row 6, which `FOUNDATION_v0.3.md` §1.3 does restate in
> full. Rows other than 6 below are this file's own first mapping pass, done directly against
> `FOUNDATION_v0.3.md`'s current field list — tier `Dr`, unreviewed, exactly as this file's own
> header says. (2) Every "where it now lives" cell below names either a `FOUNDATION_v0.3.md`
> section (real, on disk today) or a `REPO_SPEC_v0.3.md` path (specified, **not yet built** — see
> that file's own "NOT YET ON DISK" notice). Neither kind of pointer is claimed as built-and-tested.

## 1. The ancestor, cited as a dependency (chair ruling B3)

**The Standalone Scholar: A Dual-Track Architecture for AI-Native Scholarship**
(Yaoharee Lahtee, Zenodo, 2026-08-29, DOI `10.5281/zenodo.22163849`, CC BY 4.0, PUB) ships with
skill `ai-native-scholarship v1.0.0` (protocols: `dual-track`, `dvp-k-states`,
`preservation-contract`, `conversion-first`, `conceptual-paper`; templates: K1→K2 conversion
ledger, peer-review template, anchor-preservation audit).

**Cited by name + version + DOI, never merged into `plugins/`** (chair ruling B3, resolving v0.1
§10 dispute 3 — see `design/FOUNDATION_v0.3.md` §1.2, §7.7). glosa re-derives only the specific
protocol functions it needs; `methodology/data/advisor_knowledge_base.json` (REPO_SPEC path, not
yet built) is specified as "a citation + distillation, never a republish of `anchor-v10.md`."
This remains a founder veto point (`FOUNDATION_v0.3.md` §11 item 4) — B3 is a chair ruling, not a
settled founder fact.

**Grain distinction** (macro vs micro, `the internal build plan (local file, not public)` §1, `FOUNDATION_v0.3.md` §1.2): Standalone
Scholar is the **macro** scholar-career architecture (K0→K3, DVP, conversion, dual-track,
legitimacy). glosa is the **micro** engine for one claim: what licenses believing it. glosa's
claim card is explicitly a K0/K1-internal object — it never claims to *be* K1, K2, K3, or a DVP
run in its own right.

## 2. The 17-invariant anchor-preservation ledger

Source of the checklist itself: `templates/anchor-preservation-audit.md`,
`ai-native-scholarship v1.0.0` ("Semantic invariant checklist," 17 items) — quoted here as a
checklist of invariant *names* (the ancestor skill's own wording), each paired with where glosa's
mechanism for it now lives. Status vocabulary: `PRESERVE_EXACT` (same rule, same force),
`PRESERVE_FUNCTION` (same rule, glosa's own mechanism/field), `EXPAND` (glosa adds something the
ancestor did not have), `SUPERSEDE` (glosa's version replaces the ancestor's, named as such),
`PRESERVE_DIAGNOSTIC` (the rule is specified but the ancestor itself flags it untested, and glosa
carries that same untested status forward honestly rather than upgrading it).

| # | SS invariant (verbatim from ancestor checklist) | Status | Where it now lives in glosa |
|---|---|---|---|
| 1 | Discovery != Justification | `PRESERVE_FUNCTION` | The spine's S2/S3 split — Source Card + Observation Card (discovery, K0, `FOUNDATION_v0.3.md` §2.2 row S2) vs. the Claim Card's `five_questions.tested` + `independent_check` (justification, §2.2 row S3/S4; `schema/claim_card.schema.json`, REPO_SPEC path). |
| 2 | Practice experience != Population evidence | `PRESERVE_FUNCTION` | `claim_card.scope.generalization_claimed ∈ {none, pattern_candidate, population_claim}` (§3.2) — a practice-experience card is never silently read as `population_claim`. |
| 3 | AI exploration != Human commitment | `PRESERVE_FUNCTION` | `claim_card.produced_by ∈ {human, ai, joint}` + `responsible: human` (const, non-delegable, §3.2), gated at release by the Human Mastery Gate (§7.5, unchanged from v0.1). |
| 4 | Intervention creator != Sole evaluator | `PRESERVE_EXACT` | MC-01, Maker ≠ Checker ≠ Approver, pairwise-distinct identities checked on the payload itself (§7.2, kernel rule 5 in §3.3). |
| 5 | Claim scope <= Evidence scope | `PRESERVE_EXACT` | `claim_card.scope.claim_scope` may not exceed `scope.evidence_scope` — kernel rule 6, §3.3. |
| 6 | DVP != K2 | `PRESERVE_EXACT`, mechanized | Independence Ladder I0–I5 (§4.2) + `k_state` gate requiring I5 for K2/K3 (kernel rule 4, §3.3) — **plus the bounded I2+I4 exception for a single-vendor scholar (chair ruling B4), which never opens a K2 door.** This row is restated verbatim from `FOUNDATION_v0.3.md` §1.3's own one-row update; every other row in this table is this file's own first derivation, not a second copy of a v0.1 table that no longer exists on disk. |
| 7 | K1 != Certification | `PRESERVE_EXACT` | K-state ladder: K1 is defined as "Public Provisional (timestamped, citable, **explicitly not peer reviewed**)" (§4.4). |
| 8 | Attention != Credit | `PRESERVE_EXACT` | K1→K2 conversion ledger's "does not count" list — stars, downloads, shares, an uncredited AI citation (§7.6, `GLOSA_K1_K2_LEDGER.md`, REPO_SPEC path). |
| 9 | Legitimacy != Truth | `PRESERVE_EXACT` | `D-NO-VERTICAL-AUTHORITY` disclaimer (§5) + `CLAIM_BOUNDARY.md` (REPO_SPEC path) + the workspace-wide `EPIS-KNOWLEDGE-VALIDATION` stance this repo inherits (kernel rule 8, §3.3, hard-fails any text proposing external validation as a legitimacy lever). |
| 10 | Thai track != PR | `PRESERVE_FUNCTION` | `venue_track: thai_tci` is a cross-cutting genre attribute, not a publicity/announcement channel — it adds section/format/disclosure requirements only, never raises or lowers a tier ceiling (§6.1, §6.2). |
| 11 | Author PCR != external K2 | `PRESERVE_FUNCTION` | The Project Advisor's `conversion_plan.yaml` output is explicitly "a candidate (never confirmed) K1→K2 ledger row" (§7.7) — the advisor's own read of the work is never self-certifying. |
| 12 | Production-supercritical != Credit-supercritical | `PRESERVE_FUNCTION` | The Project Advisor's mint–convert coupling equation, `new_flagship_recommended ⇒ mint_count ≤ λ·conversion_count`, cold-start default zero new flagships (§7.7) — production of new claims is gated separately from credit/conversion activity. |
| 13 | NoHumanAvailable != ResearchStop | `PRESERVE_FUNCTION` | `shape: stub` (§3.2a) lets K0 work proceed at low authoring cost with no full apparatus available; the Project Advisor's cold-start default (conversion-only, no new-flagship pressure) keeps a solo scholar working rather than stalled (§7.7). |
| 14 | No independent check => No K2 claim | `PRESERVE_EXACT` | Independence Ladder: "I5 — the only route to K2" (§4.2); MIMCG L5 requires an `I5` independent human checker for any "verified/K2/certified" surface (§7.1). |
| 15 | Goodhart/PRC active | `PRESERVE_FUNCTION` | `D-PARTIAL-SET` disclaimer for any 3-lane structure with fewer than 3 admissible members (§5); the Project Advisor's Reactivity License gate, `increase_mint_rate ⇒ integrity_clean ∧ xenon_below_threshold ∧ conversion_log_operational` (§7.7). |
| 16 | SCRAM/defeat active | `PRESERVE_DIAGNOSTIC` | The Project Advisor's SCRAM rules (§7.7) are explicitly "specified, `Dr`, untested" (chair ruling D1) — `K_STATE_MISREPRESENTED` in particular is named as not yet mechanically checkable. glosa carries this untested status forward rather than upgrading it; `defeater_route` (kernel function, §9) is the mechanical twin for claim-level provenance defeat, separately grounded in the Readout Condition (see `lineage/RELATION_TO_READOUT_CONDITION.md`). |
| 17 | Survival buffer active | `PRESERVE_FUNCTION` | The Project Advisor's `conversion_plan.yaml` carries "a rejection budget/survival buffer" field alongside the next 3 addressed conversion actions (§7.7). |

**Honest note on rows 1–5 and 7–17:** these are this file's own re-derivation against
`FOUNDATION_v0.3.md`'s current schema, produced because the historical v0.1 mapping document this
ledger is supposed to carry forward "verbatim" does not exist in this repo lineage. A future pass
should independently re-check each row against the ancestor skill's own protocol files
(`protocols/dvp-k-states.md`, `protocols/preservation-contract.md`,
`protocols/conversion-first.md` — read locally from the vetted copy of `ai-native-scholarship
v1.0.0` this design round used, not reproduced here since the skill itself is the citable
dependency, not a thing to duplicate).

## 3. The supersession record for novelty/priority language (founder ruling 31)

**Superseded, not merely renamed.** `design/S13_market-collision-audit.md` stays on disk as the
`Dr`-tier research readout it always was; its content now lives, restated in the required
same/different/cited form, at `design/S13_neighbour-table.md` (chair ruling A2/D4,
`FOUNDATION_v0.3.md` §1.1, §13).

**Founder ruling (request 31, 2026-09-04, binding):** *"เราไม่สนเรื่องใหม่ ... เน้นไปที่เราเสนออะไรก็พอ
เพราะเราไม่ได้แข่งขันใคร โลกผ่านจุดนั้นไปแล้ว — เป็นยุคการผลิตงาน"* — glosa states what it proposes, what
it builds on, and what would make it wrong; it does not claim priority and does not compete with
knowledge-authority. Comparison language throughout every glosa file is *same / different /
cited* — never "took/borrowed/first/novel/unprecedented/prior art/seminal/pioneering."

**Mechanism, not just prose:** `.github/workflows/ci.yml` (REPO_SPEC path, not yet built) is
specified to run a hard grep for "novel/novelty/first/unprecedented/prior art" across `paper/`,
`methodology/`, `README.md` on every PR + tag push (`FOUNDATION_v0.3.md` §11 resolved-from table).
`D-COMPARISON` (§5) is the disclaimer id attached to any market/neighbour comparison, explicitly
named as superseding "the old S5 'D12 Novelty discipline'" wording. `design/FOUNDATION_v0.3.md`
§12 records one still-open instance of the old language not yet fixed: the already-compiled
`design/templates/arxiv-{onecol,twocol}/disclaimers.tex` files still say "D12 — Novelty
discipline" — `scripts/render_disclaimers.py`'s first real run (REPO_SPEC path, not yet built)
must regenerate and recompile both, per the priority note carried in that spec file.

## 4. Dependency statement (repeated, plain, for anyone skimming only this file)

`ai-native-scholarship v1.0.0` (Zenodo DOI `10.5281/zenodo.22163849`) is a **named, versioned,
cited dependency** of glosa — it is never copied, merged, or vendored into this repo's
`plugins/`, `methodology/`, or `schema/` trees. Where glosa needs one of its protocol functions
(conversion-first, dual-track, GDA, K1→K2 ledger, back-catalog activation,
friction-vs-fellowship routing, SCRAM), glosa re-derives that function on its own terms and logs
the row in this ledger with `PRESERVE_FUNCTION` or `EXPAND` — never `PRESERVE_EXACT`-by-copy.
This is chair ruling B3, and it remains a founder veto point (`FOUNDATION_v0.3.md` §11 item 4,
§7.7): the founder may still decide the relationship should be a merge instead, at any time.

## 5. Full list of the founder's own public prior work

`lineage/PRIOR_WORK.md` — 180 Zenodo records by the founder, 11 marked `direct-ancestor` (spot-read),
169 listed-not-interpreted per chair ruling D5. This file is the invariant-by-invariant ledger for
exactly one of those 11 (the Standalone Scholar record); the other ten direct ancestors are
covered by `FOUNDATION_v0.3.md` §1.2's own table and, where a distinct relation warrants its own
file, by `lineage/RELATION_TO_READOUT_CONDITION.md` and `lineage/RELATION_TO_ANSE_SKILLS.md`.
