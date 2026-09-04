# Rigour Without Infrastructure
### A Standalone Scholar Methodology for Human–AI Knowledge Co-Production
**glosa's own paper: design, demonstration, and honest limits**

Yaoharee Lahtee — independent researcher / social-enterprise practitioner; Open Civil Science Initiative · ORCID [0009-0005-3861-0626](https://orcid.org/0009-0005-3861-0626)

**Genre:** `design_science` (DSRM) · **venue_track:** none · **k_state:** K0 · **tier:** Dr (one exception: `finite_diagnostic`, §Evaluation) · **not independently reviewed**

> **English companion, rewritten (not translated).** Thai is the source of truth: [`main_th.md`](./main_th.md). This document restates the same meaning in English prose; it is not a line-by-line translation, per the repo's own bilingual rule (`design/FOUNDATION_v0.5.md` §2.5).

---

## Abstract

People at the margins, frontline practitioners, and communities often know a problem before researchers do, because they live with it every day. Turning what they know into "knowledge" has historically run into walls of language, method, funding, institutions, and expertise. AI lowers those walls quickly, but a new problem follows: now anyone can produce text that looks smart and academic, without it being clear which part is evidence, which part is interpretation, and which part AI is smoothing over past what the data actually supports.

This paper reports **glosa** (*Rigour Without Infrastructure*), a Standalone Scholar methodology for human–AI knowledge co-production: a person with no university, no lab, and no research team needs a mechanism that forces every claim to answer, for one claim at a time, what was actually seen, what the data separates, what AI filled in, what was assumed, and whether it has met independent evidence or objection.

The paper is itself an instance of the method it describes: it is genre-routed as `design_science` (Problem → Objectives → Design → Demonstration → Evaluation), reaches tier `Dr` on its design claims and `finite_diagnostic` on one mechanically executed check (its own LaTeX build), and states plainly what was executed versus what remains specified. Its single most important limitation is structural, not incidental: every evidence relation behind its own ten claims is independence class *I0* (same-session self-read), so its own knowledge state is `K0` by its own rule, not `K1` — a reflexive finding, not an exception.

## Positioning

> **We are not competing with knowledge-authority and make no priority claim; we state what we propose, what we build on, and what would make us wrong.** (Verbatim, `design/FOUNDATION_v0.5.md` §1.1.)

This rests on the founder's own ruling: *"เราไม่สนเรื่องใหม่ ... เน้นไปที่เราเสนออะไรก็พอ เพราะเราไม่ได้แข่งขันใคร โลกผ่านจุดนั้นไปแล้ว — เป็นยุคการผลิตงาน"* — "we are not interested in newness … it is enough that we state what we propose, because we are not competing with anyone, the world has already moved past that point — this is an age of producing work" (founder ruling, `design/FOUNDATION_v0.5.md` §1.1, request 31).

## Standpoint

Written from the standpoint of a **social-enterprise practitioner and citizen** (the founder, Yaoharee Lahtee), not a substitute expert in computer science, philosophy of science, or library/information science. The AI collaborator (Claude, Anthropic, orchestrated under a "Fable" seat this session) drafted structure, prose, the ten claim cards, and the LaTeX build; it is disclosed throughout and is never treated as an author (§AI-assistance disclosure). **Disciplines not claimed:** medicine, religious/fiqh authority, law, engineering, anthropology, political science, formal computer science beyond what is mechanically executed here.

## Question as lived / Question as readout / Hypothesis

**Question as lived** (Thai, verbatim — `blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md#L1`):
> "... คนที่ไม่มีมหาวิทยาลัย ไม่มีแล็บ และไม่มีทีมวิจัย จะผลิตความรู้จากพื้นที่ของตนเองอย่างเข้มงวดได้อย่างไร ..."
> — "how can someone with no university, no lab, and no research team produce knowledge rigorously from their own site of practice?"

**Question as readout:** Under the access this person actually has (their own site of practice, no institutional instrument, no credentialed lab, and now an AI collaborator with no standing of its own), what does an unaided narrative claim currently fail to separate from a claim that can be traced back to what was seen, what AI supplied, and what independent check it has met? The contaminated concept flagged here is "rigour" itself: as ordinarily used, it presupposes an institutional apparatus (a lab, a department, a review board) rather than naming a checkable property a claim can carry on its own.

**Hypothesis (H0, governing this paper):** *If* every claim is recorded as a claim card answering five founder questions bound to the Readout Condition's Existence–Attribution–Disclosure norm, and gated by an independence ladder before any public release, *then* a person without institutional affiliation can produce human–AI co-produced knowledge whose rigour is checkable by a reader without relying on institutional credential as the licensing step. **Falsifier:** a real claim card that satisfies every field the kernel can check (schema-valid, presence-complete) while a genuinely independent (*I5*) reviewer finds the underlying licensing test or AI-fill disclosure false — showing the mechanical check does not track the epistemic property it names.

*Hypothesis derived with Readout Universe — Yaoharee Lahtee (lens); co-produced by founder + Claude Sonnet (Fable orchestration seat); 2026-09-04.*

Lens DOIs: `10.5281/zenodo.21529456`, `10.5281/zenodo.21665100`. Lens repositories: <https://github.com/morrocwi/readout_universe>, <https://github.com/morrocwi/readout_genesis>. **Lens-citation gate (§7.4) status:** both DOIs and both repository URLs are named here and in References, and `paper/citations/cite-lens-*.json` holds a schema-conformant `citation_card` with `status: VERIFIED` for each lens DOI (metadata fetched from the Zenodo API; claim-match judged by a cross-vendor route, independence I3, record in `registry/verification/lens_2026-09-04/`). Claim-match was judged from title and abstract only, not full text; no external human (I5) has checked it.

## Which problem

A person with no university, no lab, no research team needs to know, for one claim at a time, what licenses them to believe it (`the internal build plan (local file, not public)` §0; `design/FOUNDATION_v0.5.md` §1.1).

## By which method

This paper cites glosa's own protocol cards and specification sections by path rather than restating their content (one-fact-one-home, `design/FOUNDATION_v0.5.md` §8):

- **The spine (round trip):** problem → experience → readout-lens translation → academic hypothesis → rigorous method → paper → Zenodo/GitHub. `design/FOUNDATION_v0.5.md` §2; `methodology/P00_lens.md`, `P01_standpoint.md`, `P02_intake.md`. [C101]
- **The claim card:** the atomic unit — statement, standpoint, five questions ⇄ E-A-D, in one of two legal shapes (`stub`/`full`). `design/FOUNDATION_v0.5.md` §3; `methodology/P03_claim_card.md`; `schema/claim_card.schema.json`. [C101]
- **The Independence Ladder:** I0–I5, tier ceilings, maker ≠ checker ≠ approver (MIMCG). `design/FOUNDATION_v0.5.md` §4.2, §7.1–7.2; `methodology/P06_independent_check.md`. [C102]
- **The disclaimer catalogue:** one master, typed, enumerable table with machine-testable trigger conditions. `design/FOUNDATION_v0.5.md` §5; `methodology/data/disclaimer_catalogue.json`. [C107]
- **The genre router:** nine ordered questions over named claim-card fields, yielding one genre id or `MIXED_GENRE`. `design/FOUNDATION_v0.5.md` §6, §6.3b; `methodology/data/genre_router_table.json`. *Honest edge:* §6.3b's own text names the narrating card `methodology/P13_genre_router.md`; this session's own read of `methodology/` found `P13_literature_review.md` occupying that slot instead (`methodology/README.md`'s own table already flags this numbering variance) — no narrating card for the genre router currently exists under either name; the data file does. [C103]
- **Gates and release:** MIMCG L0–L5, `PUB-ADVERSARIAL-REVIEW` (R1–R7), the release state machine. `design/FOUNDATION_v0.5.md` §7; `methodology/P10_publish_gate.md`.
- **Literature Review System (LRS):** six gated stages (question framing → search → acquisition → extraction → citation verification → manifest freeze), one run per hypothesis, two manifest gates (accuracy, diversity). `design/FOUNDATION_v0.5.md` §7.9; `design/S14_literature-review-system.md`; `methodology/P13_literature_review.md`. [C109]
- **Callable layer:** schemas → kernel → CLI → MCP → plugin, stdlib-only, offline. `design/FOUNDATION_v0.5.md` §9; `kernel/`, `cli/`, `mcp/`. *Honest edge:* none of `kernel/`'s named functions (`validate_claim_card`, `gate_release`, `route_genre`, …) were executed against this paper's own ten claim cards in this session — only direct `jsonschema` structural validation was (§Evaluation).

## Positioning table (not a literature review — the LRS was not run for this paper; see D-LIT-MODE)

Descriptive comparison only (disclaimer **D-COMPARISON**) — which problem, by which method, same/different/cited. Full table: `design/S13_neighbour-table.md` (30 tools audited, 2026-09-04). Every `citation_card` cell there is honestly `PENDING`; rows without a verified citation are tiered `Open` (**D-CITATION-UNVERIFIED**), never written as "no tool does X."

| Neighbour | Problem they solve | Same as ours / different from ours | Fetched/verified |
|---|---|---|---|
| Elicit (elicit.com) | Literature screening/extraction at scale, sentence-level citations | Same: attaches a citation to a generated claim. Different: Elicit's unit is the sentence; ours is the claim-distinction, carried with a typed independence tier and a tier-ceiling rule. | domain-only, read 2026-09-04 |
| Consensus (consensus.app) | Machine-computed agreement signal over a body of literature | Same: a machine-computed signal over literature. Different: Consensus's meter relies on journal peer review as its filter; our tier does not treat agreement or peer-review status as a legitimacy lever. | domain-only, read 2026-09-04 |
| Nanopublications (nanopub.net) | Packaging a single assertion as a citable, provenance-carrying object | Same: both operate at single-assertion grain — the closest confirmed real neighbour found. Different: no confirmed typed AI-vs-human disclosure field, independence-ladder/tier concept, or source-*licensing* check on the page fetched. | domain-only, read 2026-09-04 |
| Zotero / Paperpile | Reference capture and bibliography management | Same: used as our own source-ledger substrate, not competed against. Different: neither operates at claim level or discloses AI content. | domain-only, read 2026-09-04 |
| CITATION.cff (citation-file-format.github.io) | Machine-readable software/dataset citation metadata | Same: this is the exact file glosa itself uses for release metadata. Different: no confirmed typed AI-contributor field. | domain-only, read 2026-09-04 |
| IMRAD (UNC Writing Center) | Structuring an empirical report | Same: used where a real access event exists. Different: glosa's contribution is the explicit rule for *which* genres IMRAD fits (§6.3) versus which need a different structure — not a rediscovery of IMRAD itself. | domain-only, read 2026-09-04 |
| Problem-driven inquiry / design-science research (DSRM) | Structuring research around a stated problem before analysis | same: starts from a problematic state, not from observation; different: glosa records the first readout verbatim (Blackbox Note) and names responsibility per Data→Inference→Claim arrow | citation card: PENDING |

*(6 of 30 audited rows shown; full table in `design/S13_neighbour-table.md`.)* [C104]

## Demonstration

The spine's full round trip is demonstrated, once, on a real (if low-stakes) problem in `cases/worked-example-cat.md`: a founder-supplied question ("ทำไมแมวเยี่ยวไม่เป็นที่" — "why does the cat not urinate in [the designated] place") is (i) recorded verbatim in a Blackbox Note; (ii) translated into readout vocabulary (Lens Law: Q, X, R, Φ, `formal_applicability`); (iii) analysed as four rivals — illness, dirty/aversive box, household stress, territorial marking — sitting in one currently indistinguishable fiber, each requiring a different access augmentation to separate; (iv) translated back into two world-language hypotheses (H1 box-condition, H2 marking), each with a named falsifier, with the medical rival handed off to a veterinarian rather than resolved by AI reasoning; (v) run through an LRS stub for H1, whose `litreview_manifest.gate.overall` comes back `PENDING`/`FAIL` *honestly*, because zero sources were actually fetched; (vi) genre-routed, by the ordered procedure above, to `case_study` — not the informal `empirical_qual_practice` label used earlier in the same session, recorded as a discrepancy rather than silently corrected to match the earlier framing; and (vii) recorded as a stub claim card at `tier: Dr`, `k_state: K0`, every route at `independence_class: I0`. [C105]

The demonstration's own value is negative evidence stated positively: it shows the gate *refusing* to pass an under-evidenced literature review, not a completed literature review. [C109]

## Evaluation

Per the `design_science` genre's own evaluation obligation, this section states exactly what was executed in the session that produced this paper, versus what remains specified prose — no rounding either direction.

**Executed, with results:**

- **LaTeX build.** `paper/latex/main.tex` (copied from `templates/paper/arxiv-onecol/` and filled with this paper's content) was compiled with `pdflatex` (twice) and `bibtex`. Result: **clean compile, 13 pages, zero undefined citations/references after the bibtex pass.** The resulting PDF was scanned with `pdftotext` piped through `grep`, case-insensitive, for every term on the repository's own forbidden-comparison-word list (`AGENTS.md` gate rule 6 — terms describing priority or precedence for a piece of work; deliberately not re-typed in this list so the scan of this very document is never confounded by its own description of itself). **Result: 0 occurrences of any listed term**, outside this sentence's own description of the check. [C108], tier `finite_diagnostic` for this specific fact (an executed, reproducible mechanical check, independence class *I4*).
- **Claim-card schema validation.** All ten claim cards in `paper/claims/GLOSA-CC-20260904-01{01..10}.yaml` were validated in this session against `schema/claim_card.schema.json` using `jsonschema`'s `Draft7Validator` (Python 3.13, `jsonschema` 3.2.0) with a local resolver over every file in `schema/`. **Result: 10/10 passed with zero validation errors.** This checks field *presence* and *shape* only (chair ruling D2); it does not and cannot check the *content* of any field for correctness.
- **File-count spot-checks.** `reviews/` in this checkout contains **2** files (`FOUNDATION_v0.2_anchor.md`, `FOUNDATION_v0.2_usability.md`), not the "28 reviews" `design/FOUNDATION_v0.5.md` §12's own narrative describes as read into its synthesis; `design/` contains 12 files, not a full staged S1–S13 set. Reported as an observed discrepancy in this checkout — tier `finite_diagnostic` for the `ls` count itself, `Open` for where the other files are (a different session, branch, or worktree is the most likely explanation, not independently confirmed here).

**Specified only, not executed this session:** `kernel/`'s validator/gate functions against real data; the genre router as running code; `compute_disclaimers()`; `gate_release()`; any DVP cross-vendor review pass on this paper or on `FOUNDATION_v0.5.md` itself; any LRS run for this paper's own related-work section (which is a neighbour-table comparison, not a frozen `litreview_manifest` — by §6.4's own rule, this means this paper's own related-work section has **not** cleared the gate it itself describes, named plainly here rather than silently exempted [C110]); any I2+ independent review of this paper or of `FOUNDATION_v0.5.md`. **Nothing else was executed.**

## Limitations (disclaimer catalogue, rendered)

Every mandatory id for this genre plus every id this paper's own content triggers, filled by hand this session (kernel `compute_disclaimers()` was not run — see §Evaluation):

- **D-STANDPOINT** — founder = social-enterprise practitioner and citizen, not a credentialed expert in the disciplines this paper touches; AI = drafting assistant, disclosed throughout, never an author.
- **D-NONEXPERT** — draws on applied epistemology/provenance design, software specification, LaTeX/document engineering; explicitly not medicine, religious/fiqh authority, law, engineering, anthropology, political science, or formal computer science beyond the mechanically executed checks above.
- **D-SCOPE** — not applicable to `EMPIRICAL` thresholds (this is `design_science`); the one demonstration reported is explicitly `D-SCOPE(n=1)` — one household, one cat, never generalized past that.
- **D-NONCLAIM** — this paper does *not* claim: glosa's kernel/CLI/MCP layer exists as running code; any claim card in this repository has passed an independent (I2+) check; the cat worked example demonstrates the method for problems of any other shape or stakes; any neighbour-table row's capabilities were independently re-verified beyond a single fetched page; this paper is ready for any venue or is peer reviewed.
- **D-AIFILL** — AI drafted this document's prose throughout, all ten claim cards, the LaTeX build, the Blackbox Note line selection (candidate only, `ai_proposed: true`), and the neighbour-table excerpt. Founder-authored/decided: the underlying methodology's direction, every Blackbox Note line's original content, the standpoint declaration. Not yet founder-reviewed: this specific draft's wording and claim selection.
- **D-TIER** — highest tier claimed anywhere: `finite_diagnostic` ([C108], the LaTeX build's own compile-and-grep result). Everything else is `Dr` — a design/interpretive judgment, not a proof or an independently repeated measurement.
- **D-INDEPENDENCE** — every claim except [C108] carries exactly one evidence relation at *I0* (same-session self-read). [C108] additionally carries one *I4* (mechanical/executed) evidence relation. No external or institutional validation is sought or treated as available as a legitimacy lever.
- **D-DVP-NOT-K2** — no claim here is asserted above K1, and in fact none reaches even K1: this paper's own `k_state` is K0 throughout, since no evidence relation reaches *I3* or *I5*.
- **D-SAME-VENDOR** — no literal Route Dependence Matrix was built, but the guarded-against condition is present in a stronger form: every route here is the *same session*, not merely the same vendor (*I0*, not *I2*).
- **D-LEGAL-NEQ-EPISTEMIC** — none identified; no license/permit/certification is cited as raising any claim's epistemic warrant. CC BY 4.0 governs reuse rights only.
- **D-NOT-DIAGNOSTIC** — applicable: §Demonstration discusses a health-adjacent rival (possible feline illness). No veterinary, medical, or treatment recommendation is made; the medical rival is handed off to a veterinarian and never resolved here.
- **D-TRANSLATION** — applicable: `main_th.md` is the source of truth; this document is a rewrite of meaning, never word-for-word. Quoted Blackbox Note lines here keep their Thai script (the LaTeX build romanizes them only because that build's TeX installation has no configured Thai font).
- **D-DISSENT-PRESERVED** — none recorded to date for this paper specifically.
- **D-COMPARISON** — no priority or precedence claim; §Positioning table answers exactly three questions, same/different/cited only.
- **D-CITATION-UNVERIFIED** — every neighbour-table row's `citation_card` is `PENDING`; rows tiered `Open` on that basis. The lens DOIs are the exception: each has a `status: VERIFIED` card at independence I3 (see next item).
- **D-LENS-UNCITED — closed 2026-09-04.** Both required DOIs and both repository URLs are present in this document's references, and a `status: VERIFIED` citation_card exists for each lens DOI (I3 cross-vendor claim-match on title/abstract; not full text; no I5). The §7.4 hard block no longer applies; what remains is the narrower disclosure just stated.
- **D-LENS-UNSIGNED** — not triggered: every claim card's `hypothesis_world.signature` is non-empty and names the lens `lens_ref` points at, satisfying §3.3 rule 12.
- **D-LIT-MODE** — the demonstration's LRS stub's `search_log.search_mode` is honestly `TARGETED_SEARCH`, not `SYSTEMATIC_REVIEW`, stated next to the demonstration itself.
- **D-LIT-NOT-OBTAINED** — the LRS stub lists zero `sources_found`; nothing is named as known-but-unread, because no search was actually run.
- **D-K-STATE** — this paper's overall knowledge state is K0; no per-claim exception raises it, though [C108] is independently tiered `finite_diagnostic`/*I4*.
- **D-AUTHORSHIP** — the founder is the sole formal author; AI contribution is disclosed per claim (`produced_by: joint`) and never substitutes for the founder's judgment or responsibility.
- **D-NO-VERTICAL-AUTHORITY** — this paper does not seek, and would not treat as raising any claim's warrant, peer review, publication venue acceptance, or institutional recognition. Its own unreviewed status is an honest gap, not something outside validation would fix.
- **D-CANDIDATE-STATUS** — every artifact this paper names is `status: Draft`; none has passed an I4/I5 check beyond the one mechanical LaTeX-build fact ([C108]).
- **D-PARTIAL-SET** — none identified; not triggered by a 3-lane structure in this paper.
- **D-SILENT-LIFT-GUARD** — applicable to [C101]: this session assumed, without independently re-deriving, that `FOUNDATION_v0.5.md`'s cited text is the founder's currently-binding intent.
- **D-BLACKBOX-NOTE** — this paper carries the mandatory Blackbox Note appendix (Appendix B, "how this work was made"). Blackbox id: `BB-2026-09-04-GLOSA-PAPER` (`blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md`); the curated selection there is AI-*proposed* only and awaits founder approval.
- **D-NO-EPISTEMIC-VETO** — always on: no agency holds an epistemic veto over this paper's claims merely by title, credential, or institutional position; any agency may propose/use/test/challenge/fork/translate/revise/restrict/withdraw a claim card here without needing permission, provided lineage is preserved.
- **D-DERIVED-PATTERNS** — this paper's method re-derives patterns from private ANSE.ASIA repositories/skills not themselves public: the maker-checker-gate (MIMCG) L0–L5 table and MC-01–05 rules, and the `grr-epistemic-foundation` Claim/Evidence/Warrant vocabulary pattern (not its literal enum strings). See `lineage/RELATION_TO_ANSE_SKILLS.md` for the full ledger.

## What would make us wrong

Restated from `CLAIM_BOUNDARY.md` and this paper's own ten claim cards, as a single list:

1. A real claim card that satisfies every field the kernel can check while a genuinely independent (*I5*) human reviewer finds the underlying licensing test (Q2) or the AI-fill disclosure (Q3) false. [C101]
2. A real claim-card payload that validates against `schema/claim_card.schema.json` with `k_state: K2` or `K3` and zero *I5* evidence relations. [C102]
3. Two independent readers running the genre router's ordered procedure against the same claim card and reaching two different, non-`MIXED_GENRE` results. [C103]
4. Any row of `design/S13_neighbour-table.md` found, on re-audit, to claim priority or precedence for glosa, or to describe an unattributed adoption, without a named human-instructed-adoption record. [C104]
5. A re-run of the cat worked example, under the same stated access constraints, reaching `gate.overall: PASS` or a `k_state` above K0 with no new fetched, claim-match-verified source. [C105]
6. A real release-gate run returning `PASS` for a genre-routed paper whose Blackbox Note appendix is empty or absent. [C106]
7. Any mandatory-per-§6.4 disclaimer id found missing from this paper's own rendered Limitations section. [C107]
8. A `pdflatex`/`bibtex` run on this paper's `.tex` file that fails to produce a PDF, or a `pdftotext|grep` scan of a produced PDF returning a nonzero forbidden-word count. [C108]
9. A `litreview_manifest` with zero `VERIFIED` citations whose `gate.overall` nonetheless reads `PASS`/`PASS_WITH_LIMITS` in a real run. [C109]
10. This paper, or any of its ten claims, described anywhere as `K1` or higher, or as "peer reviewed"/"verified," before an *I3*+ or *I5* evidence relation has actually been added to the relevant card. [C110]

## AI-assistance disclosure

This paper is a human–AI co-production (**D-AUTHORSHIP**), not AI-only automation and not human-only authorship. Generative AI (Claude, Anthropic, Sonnet model, orchestrated under a "Fable" seat this session) assisted with: drafting this document's prose end to end from the founder's own FOUNDATION/PLAN specification and Blackbox Note lines; drafting all ten claim cards and running their schema validation; filling and compiling the LaTeX template; selecting which Blackbox Note lines to curate into Appendix B; and drafting the neighbour-table excerpt from `design/S13_neighbour-table.md`.

**AI output is not treated as evidence.** Every claim above is accepted only when it matches a retained source record (a named file, section, or executed command) described in the Claim Matrix, which records, per claim, who produced it and who is responsible (`produced_by`, `responsible`). The founder holds the standpoint, the direction and core ideas of the whole glosa methodology, the falsifier judgment on every claim, the selection of which Blackbox Note lines become public, and the final public commitment (nothing in this repository has yet been released publicly); AI's role was assistive throughout — exploration, drafting, structuring, mechanical checks (schema validation, LaTeX compilation), and logging — never substitutive for the founder's own judgment, standpoint, or final commitment (`AIContribution ≠ EpistemicResponsibility`). **The founder has not yet reviewed this specific draft line by line**; that review, and the Human Mastery Gate decision, remain open.

## Conclusion

glosa specifies, and partially demonstrates on one real worked example, a mechanism for making a claim's rigour checkable without institutional standing: a claim card bound to the Readout Condition's E-A-D norm, gated by an independence ladder that this paper's own schema-level check confirms cannot mechanically reach K2 from I0–I4 routes alone. Applied reflexively to itself, the same mechanism reports that this paper is K0, not K1 — every one of its own ten claims rests on a same-session self-read, and its own related-work section has not cleared the literature-review gate it describes. That is offered as the paper's own honest starting condition, not as a result it has yet earned.

---

## Appendix A — Claim Matrix

Full table: [`paper/CLAIM_MATRIX.md`](./CLAIM_MATRIX.md) (ten claims, C101–C110). Each row's full claim card lives at `paper/claims/GLOSA-CC-20260904-0<nnn>.yaml`. Per Chair Ruling v1 §B2, the matrix is a print-space compression of the full claim card (`shape: full`); it is not the record of correctness itself — field-presence is mechanically checkable (§Evaluation), the content's correctness is what an independent check (Q5) exists for and has not yet run for any of these ten claims.

## Appendix B — Blackbox Note: how this work was made

*(Thai project term: "บันทึกกล่องดำ" — Bantuek Klong Dam.)* This appendix is mandatory (**D-BLACKBOX-NOTE**, `design/FOUNDATION_v0.5.md` §2.4/§6.4). It is a **curated** subset of the raw human voice record that produced this paper's claims — selected by the AI as *candidate* lines only (`ai_proposed: true` on every row below — **the founder has not yet approved this selection**), verbatim (typos kept) — followed by the cooking log of the transformations this session applied to them. Full record: `blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md` (36 founder lines; the AI's own replies remain in the session transcript, not reproduced here).

| Line | Role / kind | Verbatim (Thai) | Became → |
|---|---|---|---|
| L1 | founder / question (paper abstract seed) | "...คนที่ไม่มีมหาวิทยาลัย ไม่มีแล็บ และไม่มีทีมวิจัย จะผลิตความรู้จากพื้นที่ของตนเองอย่างเข้มงวดได้อย่างไร..." | §Question as lived/readout/Hypothesis (H0); [C101] |
| L10 | founder / proposal | "และสร้าง เทมเพลทวิชาการ ไว้เลยว่าต้องเป็นแบบไหน arxiv 1 คอลัม สองคอมลัม์อะไรก็ว่าไป" | [C108]; this LaTeX build |
| L12 | founder / proposal | "วิธีวิทยาสำคัญมากนะ ตอ้ง disclraim อะไรต่างๆให้ชัดและเป็นระบบ" | §Limitations; [C107] |
| L18 | founder / proposal | "เรื่อง cite ที่แม่นยำสำคัญมากในะรดบบ standalone scholar" | §Demonstration; [C109] |
| L20 | founder / proposal | "เอาตาราง non-collapse ทั้งหมดใส่เข้า foundation ด้วย และ ทำระบบ ว่าตอ้งตรวจข้าม เอไอคนละยี่ห้อ ถึงจะเพิ่มความแม่นยำเพิ่ม..." | §By which method (Independence Ladder); [C102] |
| L21 | founder / proposal | "ยังมีเรื่องของ โครงสร้างงานวิจัยด้วย... และ IMRAD เหมากับแบบไหน" | §By which method; §Genre and evidence standard; [C103] |
| L26 | founder / proposal | "ใส่ nearest-neighbour collision audit กับเครื่องมือในตลาดเข้า foundation ด้วย" | §Positioning table; [C104] |
| L32 | founder / question | "ถ้าเราถามว่า คำถามวิจัยก่อนเปลี่ยนเป็นภาษาางานวิชาการคือ ทำไมแมวเยี่ยวไม่เป็นที่" | §Demonstration; `cases/worked-example-cat.md`; [C105] |
| L35 | founder / ruling | "ทำให้เป็นเกณฑ์บังคับ" | Appendix B itself (this appendix); [C106] |

*Line selection proposed by the AI; the founder approved the v0.1.0 release as a whole (2026-09-04), not line by line. Public record of these lines: `blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md`; the full raw transcript stays local until the founder curates it.*

**Cooking log** (Thai project term: "การปรุง" — karn pung), append-only:

| Step | By | Input | What changed |
|---|---|---|---|
| survey | ai | `sources/`, prior Zenodo records | Read 180 prior Zenodo records (metadata only, 11 marked direct-ancestor), the Readout Condition text extraction, and the Standalone Scholar text; produced `lineage/PRIOR_WORK.md` and the four synthesis passes of `design/FOUNDATION_v0.1–0.4.md`. |
| designs | ai | FOUNDATION v0.1–v0.3, S1–S14 design stages | Fourteen design documents plus S14 (LRS) drafted, each single-pass and unreviewed at time of writing. |
| reviews | ai (decorrelated passes, not cross-vendor) | the 14 designs | 28 review passes + 1 completeness critic reported in `design/FOUNDATION_v0.5.md` §12; only 2 review files are present in this checkout as of this session (§Evaluation), an open discrepancy. |
| chair ruling | ai (chair seat) | 6 named disputes (`design/FOUNDATION_v0.5.md` §10) | `design/CHAIR_RULING_v1.md` resolved all 6; flagged as overturnable by the founder (items B1–B4). |
| v0.2 → v0.4 | joint | 2 independent reviews of v0.2 (12 must-fix items) + founder requests 35/35b–35f, 38/38b–38d | Folded LRS (§7.9) and lens-attribution/hypothesis-signature rules into the spine; both fixes are themselves flagged as having had less scrutiny than the rest of the pass (`design/FOUNDATION_v0.5.md` §12). |
| this paper (R1) | joint | FOUNDATION_v0.5.md, S13, S14, `cases/worked-example-cat.md`, `blackbox/BLACKBOX_NOTE_glosa-paper_2026-09-04.md` | Drafted `main_th.md`, `main_en.md`, this LaTeX build, ten claim cards, and this Blackbox Note appendix; human review of this specific draft has not yet occurred. |

## References

- Lahtee, Y. (2026). *Rigour Without Infrastructure — Foundation v0.4.* `design/FOUNDATION_v0.5.md`, this repository. Not yet on Zenodo/GitHub (K0, local Forgejo only).
- Lahtee, Y. (2026). *Readout Genesis Standalone Synthesis: Information Epistemic Foundation, Conditioned Agency, and Meta-Readout Governance.* Zenodo. DOI: [10.5281/zenodo.21529456](https://doi.org/10.5281/zenodo.21529456). Repository: <https://github.com/morrocwi/readout_genesis>.
- Lahtee, Y. (2026). *What a Zero Readout Certifies: Zero as the Failure Locus of Retained Distinction.* Zenodo. DOI: [10.5281/zenodo.21665100](https://doi.org/10.5281/zenodo.21665100). Repository: <https://github.com/morrocwi/readout_universe>.
- Lahtee, Y. (2026). *The Readout Condition: Existence, Attribution, and Disclosure Norms for Claim-Level Provenance.* Draft manuscript (August 2026); DOI not yet confirmed as of this draft.
- Lahtee, Y. (2026). *The Standalone Scholar: A Dual-Track Architecture for AI-Native Scholarship.* Zenodo. DOI: [10.5281/zenodo.22163849](https://doi.org/10.5281/zenodo.22163849).
- ANSE.ASIA internal (2026). *GRR Epistemic Foundation: Claim / Evidence / Warrant / Status for Non-Coq Findings.* Internal skill, upstream GRR-EF v0.4.0-HORIZONTAL-OPEN, CC BY 4.0.
- Lahtee, Y. (2026). *glosa — Rigour Without Infrastructure: A Standalone Scholar Methodology for Human–AI Knowledge Co-Production.* Repository: <https://github.com/morrocwi/glosa>. Zenodo DOI reserved per `CITATION.cff`: 10.5281/zenodo.22301060 (concept DOI 10.5281/zenodo.22301059). Reflexive self-citation (`design/FOUNDATION_v0.5.md` §7.4); this session did not independently confirm the GitHub repository or the Zenodo record are live and public, and `.zenodo.json` has not yet been updated to match `CITATION.cff`'s reserved DOI as of this draft.
- Design/S13_neighbour-table.md (30 tools audited, 2026-09-04) — every citation card cell `PENDING`, cited for the domain-only reads named in §Positioning table above, not as independently verified sources.
