# P26 — Claim–Evidence–Theory matrix: the citation record for theory-building papers

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder instruction 2026-09-25 (*"วางระบบบันทึกเข้า
> GLOSA หน่อย ให้เชื่อมกับการทำงานด้าน CITE"* — set up a recording system in glosa that connects to the
> citation work), with the founder's own analytical notes on citation method for theory-building
> papers as input. An AI assistant drafted this card; nothing in it has had an independent check
> yet. Comparison language is same/different/cited only. Knowledge-validation stance: horizontal only
> — no venue, index, or reviewer is what makes a claim hold (`EPIS-KNOWLEDGE-VALIDATION`).

## id

`P26`

## Rule

A theory-building or conceptual paper may not cite anything that is not recorded in one chain:
**search → synthesis → claim×source row → chained source → audited sentence → proposition row**.
Every sentence in the manuscript that leans on a source must be traceable to a row that says what
the source supports, what it does **not** support, and who checked that the sentence stays inside
that support. Every theoretical proposition must be traceable to a row that states its mechanism
in the author's own words before any citation is attached.

P26 is **layered on `P13`** (literature review, L1–L6), never a replacement: the search, the
acquisition, the citation cards and the manifest gates are P13's. P26 adds the manuscript-facing
records a theory-building paper needs on top of them. Eight items, (a)–(h):

| Item | What | Home of record (one fact, one home) | New in this pass? |
|---|---|---|---|
| (a) | Structured search log | `schema/search_log.schema.json` (P13 L1–L2, P05) | no — reused unchanged |
| (b) | Integrative, theory-oriented synthesis (not a declared systematic review) | `search_log.search_mode` + `D-LIT-MODE`; `templates/knowledge/sr_protocol_prisma_lite.md` only when a declared review applies | no new field |
| (c) | Claim–Evidence–Theory matrix (claim × source) | `schema/claim_evidence_matrix_row.schema.json`; `templates/knowledge/claim_evidence_matrix.csv` (+ `.md`) | yes |
| (d) | Backward + forward citation chaining | `citation_card.chaining` (optional block) | yes, additive |
| (e) | Claim-level citation audit | `citation_card.audit` (optional block) | yes, additive |
| (f) | Theory–Evidence–Falsifier matrix (per proposition) | `schema/theory_evidence_falsifier_row.schema.json`; `templates/knowledge/theory_evidence_falsifier_matrix.yaml` | yes |
| (g) | Three-tier citation rule per construct | `claim_evidence_matrix_row.construct_tier_role` | yes (one field) |
| (h) | No argument by citation | `theory_evidence_falsifier_row.logical_basis` (mechanism + premises) | yes (one field group) |

Field names are defined only in the schema files named above; this card narrates them and never
redeclares a shape.

### (a) Structured search log

- **Purpose.** A paper's "we searched the literature" sentence has an inspectable object behind it:
  databases/indexes, query strings (support **and** challenge families), dates, inclusion rules,
  stopping rule — frozen before results are opened.
- **Fields.** `search_log` as it already stands (`frozen_scope`, `queries.support`,
  `queries.challenge`, `sources_found`, `search_mode`, `summary_disclaimer`). Nothing added.
- **Who fills.** AI may draft vocabulary and query families; the human sets the honest
  `search_mode` and the stopping rule (P13 L2).
- **Gate.** P13 L2 exit gate (scope frozen before `sources_found`); P10 R4 re-reads the linked
  manifest. The `rival_search_ref` / `contradictory_search_ref` fields in (c) and (f) point back to
  this object, so an empty "rival evidence" cell is only legal when a challenge search is named.
- **Tier.** Dr for the method; the log itself is a record (`finite_diagnostic` for what it records,
  never for the world it searched).
- **Readout-not-truth.** A search log records what one search returned on one date through one
  route. An empty result is a fact about the search (NC-27), not about the literature.

### (b) Integrative, theory-oriented synthesis — and when a declared review applies instead

- **Purpose.** Separate two layers the founder's notes keep apart: the *internal evidence control*
  that every theory-building paper needs (items c–h), and a *review-article method*, which applies
  only when the review is itself the contribution.
- **Default for a theory-building paper.** The literature is synthesised around the theory's
  constructs and mechanisms, not surveyed in date order. `search_mode` is `TARGETED_SEARCH` or
  `SCOPING_SEARCH`, and `D-LIT-MODE` is stated next to the section. The paper does **not** call its
  literature work a systematic review (FC-S8-1, NC-46), and does not attach a PRISMA flow diagram
  it has no counts for.
- **When a declared review applies instead.** When the paper's contribution **is** the review —
  its claims are about the body of literature itself — switch to a declared systematic, scoping or
  integrative review: named databases, a frozen search string, inclusion/exclusion rules, screening
  with an independent screener, and a flow diagram. Then `search_mode: SYSTEMATIC_REVIEW` with
  fully populated `prisma_counts`, and `templates/knowledge/sr_protocol_prisma_lite.md` is filled in
  full. The genre router's `systematic_review` row (`FOUNDATION_v0.6.md` §6) governs the manuscript
  structure in that case, not this card.
- **Relayed, not verified.** The founder's notes relay a reading of how particular journals and
  reporting guidelines treat review typologies and citation practice (management-theory and
  machine-intelligence journals, PRISMA). That reading is recorded here only as **the founder's
  relayed reading — NEEDS_VERIFICATION**. No journal's editorial policy is stated as fact by this
  card, and no venue is named as a target or as a guarantee of anything.
- **Who fills.** Human decides which case applies and signs the `search_mode` label.
- **Gate.** FC-S8-1 (schema hard block on a `SYSTEMATIC_REVIEW` label without counts); P10 R6
  treats "systematic review" wording in a paper whose `search_mode` is not `SYSTEMATIC_REVIEW` as an
  overclaim.
- **Tier.** Dr. **Readout-not-truth:** the label describes what was done, never how complete the
  coverage is.

### (c) Claim–Evidence–Theory matrix

- **Purpose.** Bind every claim the paper makes to every source it uses for that claim, with the
  source's boundary stated. This is the paper's internal evidence control.
- **Fields** (`schema/claim_evidence_matrix_row.schema.json`): `row_id`, `claim_id` (→ claim card),
  `claim_label` (display copy; the claim card's `statement.text` wins), `construct`, `source`
  (→ citation card), `source_type`, `construct_tier_role` (item g), `supports`, `does_not_support`
  (required, non-empty), `rival_evidence` (empty only with `rival_search_ref`), `used_in_section`,
  `mechanism_ref` (→ item f row), `search_log_ref`, `tier`, `produced_by`, `notes`.
- **Grain.** One row per claim × source **use**. This is the same grain as a citation card (one card
  per citation use), so the row never repeats the passage, locator or verification — it points at
  the card.
- **How it differs from existing tables.** `dialogue_table.md` records one source's stance toward
  one whole *hypothesis*; `architecture_dialogue_table.md` records a literature strand's relation to
  one *architecture node*; `neighbour_table.md` compares neighbouring *work* same/different/cited.
  The matrix records one source's bounded use for one *manuscript claim*. A paper using the
  architecture-first route may name the node id in the row's `notes`; no second field is added.
- **Who fills.** Author; AI may draft `supports` / `does_not_support`, never sign them.
- **Gate.** P10 R4: every source cited in the manuscript has a row, and every row's `source` card is
  `VERIFIED` before publish. P10 R7: every pointer (`claim_id`, `source`, `mechanism_ref`,
  `*_search_ref`) resolves. P10 R3: a row's `tier` does not exceed what its card and audit support.
- **Tier.** Dr. **Readout-not-truth:** a row records what a reader took a passage to support; the
  audit in (e) is what checks that reading.

### (d) Backward and forward citation chaining

- **Purpose.** Reach the relevant work a keyword search misses: backward (the source's own
  reference list) and forward (work that cites the source).
- **Fields** (`citation_card.chaining`, optional): `as_of`, `route`, `backward[]`, `forward[]`;
  each link carries `identifier`, `citation_card_ref`, `decision`
  (`INCLUDED | EXCLUDED | NOT_SCREENED`) and `reason`.
- **One home.** A citation card is per *use*, chaining is per *source document*: the block is
  recorded once, on the lowest-id card for that source; other cards for the same source leave it
  absent.
- **Who fills.** AI may run the lookup and draft the links; a human confirms each `INCLUDED` /
  `EXCLUDED` decision that shapes the argument.
- **Gate.** P13 L3 (each `INCLUDED` link enters acquisition and gets its own citation card before it
  can back anything); P13 diversity gate (chaining is a named `search-route` value in the diversity
  audit).
- **Tier.** Dr. **Readout-not-truth:** forward chaining is a readout of one index at one moment —
  hence `as_of` and `route`; a different index or a later date returns a different set.

### (e) Claim-level citation audit

- **Purpose.** Check, sentence by sentence, whether the source really supports what the sentence
  says — separately from whether the source exists (`metadata_verified`) and whether the carded
  passage supports the carded claim (`claim_match_verified`).
- **Fields** (`citation_card.audit`, optional): `status` (`VERIFIED | RELAYED | OVERREACH`),
  `checked_by`, `date`, `sentence_refs[]`, `note`. `VERIFIED` = the checker read the passage and
  the sentence claims no more than it supports; `RELAYED` = the sentence rests on a source the
  checker has not read directly; `OVERREACH` = the passage was read and the sentence claims more.
  Schema rule: `audit.status: VERIFIED` requires `claim_match_verified: true`
  (fail fixture `schema/examples/fail/fail_citation_audit_verified_without_claim_match.json`).
- **Who fills.** A checker who is **not** the sentence's maker (AGENTS.md rule 3, P06). An AI route
  may act as checker only at the independence class it actually has (P06's I0–I5 ceilings).
- **Gate.** P10 R4: any `RELAYED` or `OVERREACH` audit on a sentence in the artifact is a `FAIL`
  (FC-S14-1: a secondary citation may not back a published claim). P10 R6 reads `OVERREACH` as an
  overclaim finding. P06: the audit's `checked_by` is compared against the maker identity.
- **Tier.** Dr. **Readout-not-truth:** `VERIFIED` here means one checker's reading of one passage
  against one sentence, at the independence class recorded — never that the sentence is true.

### (f) Theory–Evidence–Falsifier matrix

- **Purpose.** For each theoretical proposition, lay out the whole chain a reader needs to attack
  it: claim → logical basis → supporting literature → contradictory literature → boundary
  condition → observable implication → falsifier.
- **Fields** (`schema/theory_evidence_falsifier_row.schema.json`): `row_id`, `proposition_id`,
  `claim_ref` (the proposition **is** a claim card), `constructs`, `logical_basis`
  (`mechanism` + `premises[]`, item h), `supporting_literature[]` and `contradictory_literature[]`
  (→ matrix rows; the second empty only with `contradictory_search_ref`), `boundary_conditions[]`
  (at least one), `observable_implication`, `falsifier_on_card`, `falsifier_check`,
  `rival_explanations[]` (each with a `distinguishing_observation`; empty only with
  `rival_search_ref`), `tier`, `status`, `human_owner`.
- **Falsifier home.** The falsifier text lives on the claim card
  (`claim_card.five_questions.tested.falsifier`) and is never copied into the row. The row carries
  `falsifier_on_card`, which a checker sets to `true` only after confirming the card's falsifier
  names an observation at the proposition's grain (not a placeholder, not a strength-of-claim
  sentence, kernel rule29). A row with `falsifier_on_card: false` cannot leave `Draft` (schema rule).
- **Who fills.** Human owns the proposition, the falsifier judgment and the boundary conditions
  (FOUNDATION §2.1b: Inference → Claim is always human). AI may draft rival explanations and
  observable implications for the human to accept or reject.
- **Gate.** P10 R3 (tier fidelity against the linked claim card), R7 (every `cem-` pointer and
  `claim_ref` resolves), R8/P17 (the human can defend the mechanism unaided). P06: `falsifier_check`
  is signed by someone other than the maker.
- **Tier.** Dr. **Readout-not-truth:** a filled row is a map of how the proposition could fail; it
  is not evidence that it did not.

### (g) Three-tier citation rule per construct

- **Purpose.** Each construct is cited through three different kinds of source, so a reader can see
  where it came from, where the field holds it now, and what is known against it.
- **Rule.** For every distinct `construct` in the matrix, the rows together include one
  `originating_source` (read directly — never cited through a review, FC-S14-1), one
  `current_synthesis`, and one `critical_or_contradictory` source. A tier that could not be filled
  is disclosed in the manuscript next to the construct, with the search that looked for it; it is
  never silently left out.
- **Field.** `claim_evidence_matrix_row.construct_tier_role`
  (`originating_source | current_synthesis | critical_or_contradictory | supporting_only`),
  separate from `source_type` (what kind of object the source is).
- **Who fills.** Author; checker confirms the originating source was opened directly.
- **Gate.** P10 R4 reads the per-construct coverage. This is a set-level rule over many rows; no
  schema can enforce it on one row, and no script computes it yet (open item 1).
- **Tier.** Dr. **Readout-not-truth:** "originating source" names the earliest statement this search
  found and read, not a priority judgement about who holds the idea.

### (h) No argument by citation

- **Purpose.** A citation cannot stand in for reasoning. The mechanism is written first, in the
  author's own words; citations then attach to its parts.
- **Field.** `theory_evidence_falsifier_row.logical_basis`: `mechanism` (own words, required) and
  `premises[]` (each with `text`, `cem_refs[]` and `kind`:
  `cited_premise | definition | own_reasoning_step | assumption`). A premise with no citation is
  legal when its `kind` says why.
- **Who fills.** Author. AI may flag sentences of the form "as X showed, therefore …" as candidate
  argument-by-citation; the author rewrites them.
- **Gate.** P10 R6 (a proposition whose mechanism is only a citation is an overclaim finding); P17
  (the author can state the mechanism without the sources in front of them).
- **Tier.** Dr. **Readout-not-truth:** a stated mechanism is a proposal about why; it is tested by
  the falsifier in (f), not by the number of citations attached to its premises.

## Why / incident

Founder instruction 2026-09-25 (quoted above), together with the founder's notes on citation
method for theory-building papers: keep the internal citation/evidence matrix separate from a
review-article method; bind every claim to its sources; chain citations backward and forward;
audit citations sentence by sentence; never let a citation replace reasoning; cite each construct
through an originating source, a current synthesis and critical evidence; and, at the highest
standard, carry every proposition through to its falsifier. The failure this closes is the one P13
already names for literature review in general — a rule that exists in prose and cannot be queried
— applied to the manuscript's own sentences and propositions.

## Inputs → outputs

- **Inputs:** P13's frozen `search_log`, `source_acquisition_log`, `citation_card`s and
  `litreview_manifest`; the paper's claim cards (P03), one per claim and one per proposition.
- **Outputs:** `claim_evidence_matrix.csv` (rows valid against
  `claim_evidence_matrix_row.schema.json`), `theory_evidence_falsifier_matrix.yaml` (rows valid
  against `theory_evidence_falsifier_row.schema.json`), and citation cards carrying `chaining` and
  `audit` where used.

## Gate

The records above are what P10 R3/R4/R6/R7 read for a theory-building paper, and what P06's
maker ≠ checker comparison runs on for the audit and the falsifier check. **Stated plainly:** as of
this card, `kernel/glosa_kernel.py`'s `gate_release` does **not** yet read matrix rows, `audit`, or
`falsifier_on_card`; the consumption above is specified (Dr), not built. What is enforced today is
the schema layer only: `./cli/glosa check <file>` validates each row and card (kind detection is
driven by the `schema/` directory, so the two new kinds are picked up without CLI changes).

## Human / AI split

Human: chooses the synthesis-vs-declared-review case (b); owns every proposition, mechanism,
boundary condition and falsifier (f, h); confirms chaining decisions that shape the argument (d);
signs the matrix. Checker (not the maker): the claim-level audit (e) and `falsifier_check` (f).
AI: drafts queries, chaining lookups, `supports` / `does_not_support` text, candidate rivals and
argument-by-citation flags — never signs an audit or a falsifier check of its own output.

## Disclaimers

Reused: `D-LIT-MODE` (b), `D-CITATION-UNVERIFIED` (any row whose card is not `VERIFIED`),
`D-LIT-NOT-OBTAINED` (a chained link known but unread), `D-TIER`, `D-SCOPE`, `D-AIFILL`,
`D-NO-VERTICAL-AUTHORITY` (no venue or index settles a claim). No new disclaimer id is introduced.

## NC pairs

`NC-18` Source existence ≠ Claim support · `NC-27` not found ≠ does not exist · `NC-46` Systematic
Review ≠ Rapid/Scoping/Targeted evidence challenge · `NC-57` Claim scope ≤ Evidence scope.

## Not-do

- Do not call the literature work of a theory-building paper a systematic review, or attach a
  PRISMA diagram without counts.
- Do not copy a claim's canonical wording or its falsifier into a matrix row; point at the card.
- Do not leave `does_not_support` empty, or `rival_evidence` / `contradictory_literature` empty
  without naming the challenge search.
- Do not cite a construct's originating source through a review of it.
- Do not let the maker of a sentence audit it, or the maker of a proposition sign its falsifier check.
- Do not present a journal's editorial policy, or a venue, as the standard that makes the paper
  right — the founder's relayed reading of venue policy stays `NEEDS_VERIFICATION`.

## Tier

Dr (specified; independently unreviewed). Schema examples and one fail fixture validate under
`./cli/glosa check`; nothing here has been used on a real manuscript yet.

## Open items (named, not resolved)

1. No script computes the set-level checks: three-tier coverage per construct (g), "every cited
   source has a row" (c), pointer resolution across files (R7), and CSV-to-row validation.
2. `gate_release` does not yet consume `audit`, matrix rows, or `falsifier_on_card`.
3. `search_mode` has no value for a declared *integrative* review article; such a paper currently
   uses `SCOPING_SEARCH` or `SYSTEMATIC_REVIEW` according to its protocol. Adding a value is a
   schema decision left to the founder.
4. The founder's relayed reading of venue and reporting-guideline policy is `NEEDS_VERIFICATION`
   and is not carried into any rule here.
