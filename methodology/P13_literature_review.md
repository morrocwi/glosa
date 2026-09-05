# P13 — Literature review (LRS)

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction (request 35, HANDOFF
> §8, mandatory); AI drafted this card, narrating `design/S14_literature-review-system.md` in
> full. Comparison language is same/different/cited only. Knowledge-validation stance: horizontal
> only — the mechanical checks named below (Crossref/OpenAlex/PubMed/DataCite, retraction
> registries) are existence/metadata checks, never an authority that confers truth or legitimacy
> on a claim (`EPIS-KNOWLEDGE-VALIDATION`).

> **Naming note, stated plainly rather than silently resolved:** `design/REPO_SPEC_v0.5.md` names
> `methodology/P13_genre_router.md` for `FOUNDATION_v0.5.md` §6's genre router. This task assigns
> the id `P13` to the literature-review system instead, per its own explicit instruction. This is
> a live naming collision between two design documents, not a decision this card makes — a future
> synthesis pass must renumber one of the two (the genre router narration could move to a
> different id, or this card could) before both are built into the callable layer. Flagged here,
> not resolved.

## id

`P13`

## Rule

A paper may never say "we reviewed the literature" without a frozen, inspectable object behind
that sentence. The Literature Review System (LRS) is the pipeline that produces that object, run
**once per lens-out hypothesis** (never one merged search covering several hypotheses — this
would blur which evidence backs which falsifier):

**Six stages (L1–L6), each with one owning artifact and one exit gate** (`S14` §1):

| # | Stage | Owns | Exit gate |
|---|---|---|---|
| L1 | Question framing | `search_log.yaml.frozen_scope` (seeded from `lens_translation`/`hypothesis_world`) | Fields non-empty and traceable to the claim card |
| L2 | Search protocol | `search_log.yaml` (frozen) + `sr_protocol_prisma_lite.md` | Honest `review_mode` chosen; `frozen_scope` locked **before** `sources_found` is populated |
| L3 | Acquisition | `source_acquisition_log.yaml` rows | Every candidate has `acquisition_status ∈ {obtained, abstract_only, not_obtained}`; no local path/Zotero key/`rl`-internal id anywhere |
| L4 | Reading & extraction | `citation_card.yaml` fields + `dialogue_table.md` row | `exact_passage` present for every row carrying a stance; secondary-citation-ban audit clear |
| L5 | Citation verification | `citation_card.status: VERIFIED` | `metadata_verified` (mechanical) **and** `claim_match_verified` (I5 human or decorrelated I3) both true |
| L6 | Neighbour table + manifest | `neighbour_table.md` rows + `litreview_manifest.yaml` (frozen) | Both gates (§ below) computed and non-`PENDING`; manifest `status: FROZEN` |

**Form (request 35c):** the review is a **conversation with the problem**, not a chronological or
priority-ranked survey — every source is placed in `dialogue_table.md` by what it sees, what
it separates, what it assumes, whether it agrees/disagrees/is orthogonal to the hypothesis, and
what it would say against us. Date is metadata only; it never sets row order.

**Two separate gates, not one (request 35e):**
- **Accuracy gate** — every listed citation `VERIFIED`, spot-check sample `PASS`, zero secondary-
  citation violations, no `RETRACTED` source in scope.
- **Diversity gate** — the source *set* actually spans language/discipline/source-type/search-
  route/geography, audited and disclosed (`diversity_audit`), not silently claimed. A disclosed
  concentration downgrades to `PASS_WITH_LIMITS`; an undisclosed one is `FAIL`.

**Stratified selection (request 35f):** when more candidates exist than will be cited, select
across the cross of `(quality_tier × region × language × source_type)`, filling empty strata
before adding a second source to any populated one; an empty stratum is recorded with
`selected: null`, never omitted. A `venue_quality_index` (e.g. Scopus/SJR quartile) is metadata
only — it is never a substitute for `claim_match_verified` (Legitimacy ≠ Truth).

**Never cite what was not opened (`FC-S14-1`, secondary-citation ban):** a passage quoted from a
paper that itself quotes the real source, without this pipeline opening the real source directly,
is forbidden from backing a claim or a dialogue-table stance.

**Hypothesis selection is a human decision (request 35d):** after *n* LRS runs for *n* candidate
hypotheses each freeze their own manifest, a human — never an AI route alone — fills
`hypothesis_selection.yaml`, comparing developability, access/evidence available, falsifier
reachability, independence-route ceiling, risk/ethics, and genre fit. A parked hypothesis keeps a
required non-empty `reason` and stays fully in the repo, never deleted. The selection event itself
is logged in the Blackbox Note's `cooking:` log (`P11`).

**The gate into method design and paper (the founder's actual mandate, restated exactly):** *no
lit-review section may be drafted — not merely published — until its `litreview_manifest.yaml`
reaches `gate.overall ∈ {PASS, PASS_WITH_LIMITS}`.*

**Optional S14 discovery-routing stage (decided 2026-09-05, founder, delegated "ทำให้เลย",
BBL-2026-09-05-122; `DECISIONS.md` 2026-09-05 row; `design/FOUNDATION_v0.6.md` §7.9;
`design/FOUNDATION_v0.6_PATCH.md` §23; DAG node `foundation.lrs-discovery-loop-extension`,
status `decided`).** L1–L6 above may optionally be **preceded** by a discovery-routing stage: the
human retains ownership of the question; the AI recursively decomposes it into candidate
sub-questions and gates each candidate before it enters L1, using `k_epi` (the epistemic-
multiplication construct, cited kc-ep-045, kc-ep-046, kc-ep-048, kc-ep-049, kc-aihp-005,
kc-aihp-006, kc-aihp-010, kc-aihp-020) as the gating construct. This is an **extension, never a
replacement** — every candidate that survives the gate still runs the full L1–L6 pipeline
unchanged; a run that skips this stage entirely is equally valid. **Not adopted by this decision:**
the broader agenda-paper claim behind `k_epi` (kc-aihp-008, kc-aihp-009) stays logged `[Open]` —
this stage operationalizes only the already-`holds`/`adapt` cards, not the open agenda claim
itself. `litreview_manifest.yaml` gains an additive `discovery_routing: { used: bool,
candidate_questions: [string], k_epi_gate_log: [{question, gated_out: bool, reason}] }` block;
`used: false` (default) means this section does not apply and no candidate_questions/gate_log is
required. Kernel `rule25` (`DISCOVERY-CANDIDATE-UNGATED`): `discovery_routing.used=true` requires
every `candidate_questions` entry to have a `k_epi_gate_log` row before it may enter L1 — not yet
built (kernel is other workers' ownership this pass). No sim fixtures exist for this mechanism yet;
acceptance test ("S4 finite_diagnostic sim compares LRS precision/recall on the same question set
with and without the discovery-routing stage; ship only if recall improves without a precision
drop") has not been run.

**Claim-tier intake flag (decided 2026-09-05, founder, delegated "ทำให้เลย",
BBL-2026-09-05-122; `DECISIONS.md` 2026-09-05 row; `design/FOUNDATION_v0.6.md` §7.9;
`design/FOUNDATION_v0.6_PATCH.md` §4; DAG node `foundation.s7.9-intake-tier-flag`, status
`decided`) — thin addition to the accuracy gate, not a new mechanism.** At L4 (reading &
extraction), a source is flagged `intake_tier: request_tier` when its own genre would normally
suppress an AACODS-style trace-to-original+appraise pass (e.g. a policy brief, a grey-literature
report, an anecdotal/expert/local-knowledge account) — the flag *requests* a tier assignment
rather than rejecting the source outright. **Explicit exemption:** Global South anecdotal,
expert, and local-knowledge evidence genres are never treated as automatically suspect by this
flag alone; the flag names a gap in the existing checklist's coverage, not a downgrade of the
source's standing. A flagged-and-tiered row is distinct in the manifest from a rejected row.
Fields (additive, per `citations[]` entry, not on `litreview_manifest` top level — the per-source
array is `citations[]` keyed by `citation_card_id`; there is no `sources_found` field on
`litreview_manifest`): `intake_tier: request_tier | not_flagged` (default `not_flagged`),
`intake_tier_reason: string | null` (required non-empty when `intake_tier=request_tier`),
`global_south_exempt: bool`. Kernel `rule22` (`INTAKE-TIER-UNTIERED`): a `citations[]` entry
flagged `intake_tier=request_tier` requires a non-empty `intake_tier_reason`, never merged with a
rejected row — built and shipped in `kernel/glosa_kernel.py` (`_intake_tier_warnings`, WARNING-only, `Rule22IntakeTierTest`). **Sim caveat carried
forward explicitly:** any acceptance test for this mechanism must be run against fixtures built
for the actual AACODS-layer mechanism, not against the existing S4 corpus (which has no such
fixtures) — a prior +1.0 delta measured on this corpus was produced by a different (defect-
detector) proxy and must not be cited as evidence for this mechanism.

## Why / incident

Founder request 35 (2026-09-04, HANDOFF §8, mandatory): *"บังคับก่อนทบทวนวรรณกรรม: ต้องแยกทำระบบ
ทบทวนวรรณกรรมเป็นอีกหนึ่งระบบ ต้องใช้ระบบ research ที่มีเต็มรูปแบบ และทำร่วมกับระบบ cite ที่ดีที่สุดที่
มนุษย์จะทำได้ เพื่อความแม่นยำสูงสุด"* — the founder asked, directly, for a separate, full-strength
system, paired with the best citation-accuracy discipline achievable by a human, for maximum
accuracy. The failure mode this closes: a paper's "we reviewed the literature" sentence with no
queryable object behind it — the same "the rule existed in prose, nobody could query it" pattern
already caught once in this workspace's own documentation history (`doc-ecosystem` skill), applied
here to literature review specifically rather than left as a general prose instruction.

## Inputs → outputs

- **Inputs:** a lens-out hypothesis (`hypothesis_world`, R2) with its falsifier; the "our own row"
  block of `neighbour_table.md`; the private `rl` (Zotero+Calibre+Paperless) shelf as a **read-only
  reference**, never a public citation source in itself.
- **Outputs (per hypothesis):** a frozen `search_log.yaml`, `source_acquisition_log.yaml` rows, a
  `dialogue_table.md`, a set of `citation_card.yaml` entries, `neighbour_table.md` rows, and one
  frozen `litreview_manifest.yaml` carrying both gate results.

## Gate

Threaded through three places, all pointing at the same one manifest (one fact, one home):

1. **S4 (rigorous method)** may not proceed on a hypothesis whose manifest is `FAIL`/`PENDING`.
2. **The publish gate (`P10`, R4)** re-runs the accuracy gate independently at publish time — a
   manifest that passed at freeze time is re-verified, never grandfathered (a citation may have
   been SCRAMMED since).
3. **Every genre's structure column** (`FOUNDATION_v0.5.md` §6.2) that includes a literature/
   related-work component routes it through this gate rather than free-text "cite relevant
   literature" prose.

**The research-stack boundary (never crosses into the public repo):** a local filesystem path, a
Zotero item key, a Paperless document id, an `rl`-internal identifier of any kind, or a folder/
collection name from the private shelf. **Crosses:** the public resolvable identifier (DOI/PMID/
ISBN/ARXIV/OFFICIAL_URL/`BLACKBOX_NOTE`), the exact quoted/paraphrased passage with locator and
scope, and an honest `acquisition_status`/route (including `RL_PRIVATE_SHELF` as a named route
value without naming which collection inside it).

## Human / AI split

Human: sets the honest `review_mode` label and stopping rule (L2); holds the private shelf and
confirms paywalled/institutional access (L3); reads the acquired text directly at least for the
spot-check sample (L4); is the I5 verification route or confirms an I3 route was genuinely
decorrelated (L5); signs the manifest as `human_owner` and approves the freeze (L6); decides
`hypothesis_selection.chosen` and writes the `reason` (selection) — all non-delegable. AI: drafts
vocabulary/inclusion-exclusion from claim-card fields (L1); runs/drafts query families across
tracks (L2); attempts open-access resolution and records HTTP status, never self-certifying
`obtained` (L3); drafts dialogue-table rows and flags its own inferential commitments (L4);
proposes verification candidates, never self-certifying `claim_match_verified` (L5); assembles
roll-up counts and drafts `strata_table` (L6); proposes the hypothesis-comparison table's
contents, never the decision (selection).

## Disclaimers

`D-CITATION-UNVERIFIED`, `D-DVP-NOT-K2`, `D-SAME-VENDOR`, `D-COMPARISON`, `D-BLACKBOX-NOTE`, `D-
NO-VERTICAL-AUTHORITY`, `D-LEGAL-NEQ-EPISTEMIC` (all reused, `S14` §8), plus three new to this
stage: `D-LIT-MODE` (any `review_mode` other than `SYSTEMATIC_REVIEW`, stated next to the section,
not in a footnote), `D-LIT-NOT-OBTAINED` (a source known but unread — mentionable, never given a
dialogue-table stance), `D-LIT-CONCENTRATED` (any undisclosed-risk concentration in the diversity
audit, stated with the dimension and percentage).

## NC pairs

`NC-18` Source existence ≠ Claim support · `NC-27` LOCAL_EVIDENCE_NOT_FOUND ≠ NO_LOCAL_EVIDENCE_
EXISTS (an empty stratum is a search-coverage fact, not proof nothing exists there) · `NC-36`
Reproduction ≠ Replication · `NC-46` Systematic Review ≠ Rapid/Scoping/Targeted evidence challenge
· `NC-63` Representationality ≠ Selectivity (a venue-quality index is metadata, never proof of
population-level representativeness).

## Not-do

- Do not merge several hypotheses' evidence into one search/manifest.
- Do not order or narrate sources by date, "who came first," or priority-ranked language.
- Do not record a dialogue-table stance (`agrees`/`disagrees`) before `claim_match_verified ==
  true` on that row — the legal interim value is `undetermined`.
- Do not claim "diverse sources" in prose without pointing at the `diversity_audit.counts` block.
- Do not write a local file path, Zotero key, Paperless id, or shelf folder/collection name into
  any public file.
- Do not let an AI route self-certify its own `claim_match_verified`.
- Do not draft or publish a lit-review section while its manifest sits below `PASS`/`PASS_WITH_
  LIMITS`.
- Do not treat a venue's prestige, impact factor, or peer-review status as settling a claim rather
  than describing a venue (`D-NO-VERTICAL-AUTHORITY`).

## Tier

Dr (specified; independently unreviewed). None of the six stages' gates has been run through a
validator or tested against a real hypothesis end-to-end; the worked cat-question example in
`S14` §10 demonstrates the pipeline honestly *failing* (accuracy and diversity gates both `FAIL`,
by design), not a completed real run.

## Source-first citation (kernel rule 17, 2026-09-04)

Never cite from memory. Open the source, record the link you read it from, the page/section, the line/paragraph, and one continuous verbatim passage — all four on the card — or leave the card at CANDIDATE. See FOUNDATION §7.8.
