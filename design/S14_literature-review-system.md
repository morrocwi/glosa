# RWI Stage S14 — Literature Review System (LRS)

> Status: **Dr** (design synthesis, unreviewed) · 2026-09-04 · standalone design pass for
> Rigour Without Infrastructure, requested directly by the founder as request 35 (HANDOFF §8,
> mandatory): *"บังคับก่อนทบทวนวรรณกรรม: ต้องแยกทำระบบทบทวนวรรณกรรมเป็นอีกหนึ่งระบบ ต้องใช้ระบบ
> research ที่มีเต็มรูปแบบ และทำร่วมกับระบบ cite ที่ดีที่สุดที่มนุษย์จะทำได้ เพื่อความแม่นยำสูงสุด."*
> Pipeline context: this stage sits **inside** the spine (§0 below), not after it — S8's citation/
> search-log/kg subsystems are the machinery LRS calls; S14 is the pipeline that sequences them
> for one specific purpose (turning a lens-out hypothesis into a verified, honestly-labeled
> literature conversation) and the SEPARATE gate the founder asked for.
> Author of direction: Yaoharee Lahtee. This document: AI-drafted synthesis, not new philosophy.
> readout-not-truth: every factual claim is tagged with where it was read; nothing here is
> settled until an independent reviewer checks it (`maker-checker-gate`/MIMCG) and the founder
> rules on §9's open questions. Knowledge-validation stance: horizontal only — the mechanical
> checks in this stage (Crossref/OpenAlex/PubMed/DataCite, retraction registries) are existence/
> metadata checks, never an authority that confers truth or legitimacy on a claim
> (`EPIS-KNOWLEDGE-VALIDATION`).

---

## 0. Why the founder made this a SEPARATE system, and where it sits in the spine

S8 already names a citation-accuracy subsystem and a search-protocol subsystem (`design/
S8_knowledge-infrastructure.md` §1–§2). Request 35 does not ask for a new citation mechanism —
it asks for the **pipeline that sequences the existing mechanisms into one gated system**, so
that "I reviewed the literature" is never a sentence a paper gets to say without a frozen,
inspectable object behind it. Three founder refinements fix exactly where and how this pipeline
runs (mid-run additions, all binding on this design):

- **35b — trigger and multiplicity.** The LRS is triggered by the lens-out hypothesis (R2), one
  run per hypothesis. Several hypotheses from one lens-in/lens-out pass mean several LRS runs,
  each with its **own** `search_log.yaml` and its own `litreview_manifest.yaml` — never one
  merged search covering several hypotheses at once (this would silently blur which evidence
  backs which falsifier, the same class of leak the identification ladder exists to catch).
- **35c — form.** The lit review is organised as a **conversation with the problem**: every
  source is placed by how it talks to *our* problem/hypothesis (what it sees, what it separates,
  what it assumes, where it agrees/disagrees, what it would say against us) — never by
  chronology or "seminal/pioneering" rank. This is the same descriptive, no-priority stance
  already ruled for market-neighbour comparison (request 31d–31i); S14 applies it at
  source-granularity via a new `dialogue_table.md` template (§3.4).
- **35d — hypothesis selection.** Because 35b produces *n* LRS runs for *n* candidate
  hypotheses, something has to choose which hypothesis(es) actually proceed to method design.
  That choice is a **human** decision (§6), recorded, never silently defaulted to "whichever had
  the most sources."
- **35e/35f — accuracy and diversity are coupled, but as two separate gates.** A manifest can be
  citation-accurate and still be a monoculture (one database, one language, one AI route, sources
  that all happen to agree). §5.5–§5.6 make diversity a required, disclosed audit — never a
  silent property of "we searched a lot."

**Spine placement (explicit, per the coordinator's instruction to state the order plainly):**

```
S1 problem (ปัญหา)
  → Blackbox Note (บันทึกกล่องดำ, verbatim raw lines)
    → lens-in (Lens Law: declare Q, X, R, Phi before touching evidence)
      → analysis under E-A-D
        → lens-out: n candidate academic hypotheses (R2_1 .. R2_n), each with a falsifier
          → LRS run #1 (H1: search -> acquire -> extract -> dialogue_table -> cite-check -> manifest)
          → LRS run #2 (H2: ... )
          → LRS run #n (Hn: ... )
            → HYPOTHESIS SELECTION (human; hypothesis_selection.yaml; §6)
              → genre route (S6.1: บทความวิชาการ vs บทความวิจัย vs the other 7 rows)
                → S4 rigorous method
                  → S5 paper (lit-review section drafted ONLY if its manifest gate is PASS/
                    PASS_WITH_LIMITS, §7)
                    → S6 publish (Zenodo + GitHub)
```

LRS sits **between S3 (hypothesis via readout lens) and S4 (rigorous method)** — it is not part
of S3 (S3 owns the lens translation, not the evidence search) and it is not part of S4 (S4's
method design consumes the *selected* hypothesis's evidence base; it does not itself run
searches). It is its own numbered stage with its own gate, exactly as request 35 asked.

---

## 1. Pipeline — stages and gates

Six stages, each with an owning artifact and an exit gate, mirroring the FOUNDATION §2.2 table's
own shape (one stage, one artifact, one gate — no parallel vocabulary per request 21).

| # | Stage | Owns artifact | Exit gate | Human/AI split (request 24) |
|---|---|---|---|---|
| L1 | **Question framing** | `search_log.yaml.frozen_scope` (seeded) | `frozen_scope` fields non-empty and traceable to `lens_translation` + `hypothesis_world` + neighbour_table "our row" | Human: confirms the framing is actually the question being asked, not a convenient proxy. AI: drafts `concepts_synonyms_vocabulary`, `inclusion_exclusion_rules` from the claim card fields. |
| L2 | **Search protocol** | `search_log.yaml` (frozen) + `sr_protocol_prisma_lite.md` | `review_mode` chosen honestly (§2); `frozen_scope` locked **before** `sources_found` is populated (§2.5, unchanged from S8) | Human: names the honest label and the stopping rule. AI: runs/drafts the support+challenge query families across global+local tracks. |
| L3 | **Acquisition** | `source_acquisition_log.yaml` rows, one per attempt | Every candidate has a resolved `acquisition_status ∈ {obtained, abstract_only, not_obtained}`; no local path/Zotero key/rl-internal id anywhere in the row (§4) | Human: holds the private research-library shelf (`rl`) and confirms institutional/paywalled access. AI: attempts open-access resolution, records HTTP status, never self-certifies `obtained`. |
| L4 | **Reading & extraction** | `citation_card.yaml` fields (`exact_passage`, `page_or_locator`, `scope`) + `dialogue_table.md` row | `exact_passage` present for every row carrying a stance; `secondary_citation_ban_audit.violations_found == 0` | Human or a decorrelated I3 route reads the acquired text directly (never a paraphrase-of-a-paraphrase) and fills the dialogue-table columns (§3.4). |
| L5 | **Citation-card verification** | `citation_card.yaml` reaching `status: VERIFIED` | `metadata_verified` (mechanical) AND `claim_match_verified` (I5 human OR decorrelated I3) both true; retraction check clear; version status resolved; spot-check sample passed (§5) | Human: is the I5 route, or confirms the I3 route was genuinely decorrelated (MC-02). AI: proposes candidates, never self-certifies its own `claim_match_verified`. |
| L6 | **Neighbour table + manifest** | `neighbour_table.md` rows + `litreview_manifest.yaml` (frozen) | `gate.accuracy_gate` and `gate.diversity_gate` both computed and non-`PENDING`; manifest `status: FROZEN` | Human: signs the manifest as `human_owner`. AI: assembles the roll-up counts and drafts `strata_table`. |

**Gate into S4/S5 (the founder's actual mandate):** *no lit-review section may be drafted, and no
manifest below `PASS`/`PASS_WITH_LIMITS` may be cited from a paper*, per `lit_review_gate_
checklist.md` (§7). This is the one new hard rule request 35 introduces beyond what S8 already
had: S8 built the parts; S14 is the assembly line **and the padlock at its far end**.

---

## 2. Stage detail

### 2.1 L1 — Question framing

Inputs, read directly, never re-typed by hand into a second vocabulary (one fact, one home):

- `claim_card.lens_translation` (§3.2 of FOUNDATION_v0.2.md): `question_Q`,
  `local_contrast_space_X`, `access_relation_R`, `claim_function_Phi_z0` — the lens-in
  formulation, giving the search its controlled vocabulary and the boundary of what a "same
  question" search result even means.
- `claim_card.statement` / `hypothesis_world` (R2) — the world-language hypothesis and its
  falsifier, which becomes `search_log.frozen_scope.hypothesis_or_falsifier`.
- `neighbour_table.md`'s **"Our own row"** block (already a required first fill per that
  template's own instruction: "fill first, so neighbours are compared against something
  explicit") — `problem`, `method`, and `what would make us wrong` seed the frame the dialogue
  table (§3.4) will place every source against.

Output: `search_log.yaml.frozen_scope` populated but **not yet frozen for real** — L1 drafts it,
L2 freezes it (the freeze is the gate event, not the drafting).

### 2.2 L2 — Search protocol (PRISMA-2020-lite, honest label)

Unchanged machinery from S8 §2, reused here as-is (one fact, one home — S14 does not re-specify
`sr_protocol_prisma_lite.md` or `search_log.yaml`, it sequences them):

- `review_mode ∈ {SYSTEMATIC_REVIEW, SCOPING_SEARCH, TARGETED_SEARCH,
  RAPID_EVIDENCE_CHALLENGE, FIELD_OBSERVATION_LOG, INTERNAL_DATA_AUDIT}`. The sixth value,
  `INTERNAL_DATA_AUDIT`, is chair-ruling-restored (`FOUNDATION_v0.2.md` §7.8, chair ruling C5) —
  it is the mode for a hypothesis whose evidence is the scholar's own already-held records
  (a logbook re-read), distinct from a fresh literature search.
- **Global + local (Thai/frontline) tracks**, bidirectional support+challenge query families,
  never a negated support query standing in for a real challenge family.
- **Frozen before opened**: `frozen_scope` is locked *before* `sources_found` is populated —
  this is what makes the search auditable as a pre-registered object rather than a
  post-hoc-tuned narrative (S8 §2.5, re-used verbatim in function).

**Naming note the founder should resolve (flagged, not silently fixed):** `FOUNDATION_v0.2.md`
§7.8 also introduces a *second*, differently-scoped `review_mode` enum (`MAKER_SELF_CHECK |
DECORRELATED_AI_ROUTE | HUMAN_REVIEW | MECHANICAL_CHECK | SYSTEMATIC_LITERATURE_SEARCH |
INTERNAL_DATA_AUDIT`) attributed to the same chair ruling C5. That second enum reads as a
**verification-route** label (who/what checked a `review_report`), not a search-episode label —
it is a different axis from `search_log.yaml.review_mode` even though it shares a field name and
one enum value (`INTERNAL_DATA_AUDIT`). S14 uses the search-episode sense throughout (matching
S8's `search_log.yaml` and the task that named S14 explicitly with that six-value list). This
name collision should be resolved by renaming one of the two fields before the schemas are
implemented — flagged in §9.4 as an open item, not silently resolved here.

### 2.3 L3 — Acquisition (interface to the private research stack)

**What crosses the public/private boundary, and what never does (§4 has the full boundary
contract):** an acquisition attempt may consult the founder's private Zotero+Calibre+Paperless
shelf via `rl` (per `~/research-library/bin/rl --help`, read-only reference for this design —
`status`, `zotero`, `calibre`, `web`, `consume <file>`, `import [dir]`, `rag` [private export,
not RAG-connected], `creds`). **Nothing from that stack's internals — a local file path, a Zotero
item key, a Paperless document id, a folder name — is ever written into a public RWI file.** The
only thing that crosses is: (a) the public, resolvable `identifier` (DOI/PMID/ISBN/ARXIV/
OFFICIAL_URL), (b) an honest `acquisition_status`, and (c) the passage text itself once quoted
under `exact_passage` (the passage is public because it is being cited, not because the shelf is
public).

`acquisition_status` (request 35's own required vocabulary): `obtained | abstract_only |
not_obtained` — mapped mechanically (never hand-duplicated) onto `citation_card.fetch_status`
by `source_acquisition_log.yaml` (§ template). `not_obtained` is a legal, terminal, honestly
recorded state — a source is never silently dropped from the search log for being unobtainable;
it stays visible with `D-LIT-NOT-OBTAINED` wherever it is mentioned, and it may never receive a
dialogue-table stance.

**Secondary-citation ban** (request 35, restated as a named rule, `FC-S14-1`): *never cite what
was not opened.* A passage quoted from a paper that itself quotes the real source, without RWI
opening the real source directly, is a secondary citation and is forbidden from backing a claim
or a dialogue-table stance — `source_acquisition_log.secondary_citation_check` makes this a
checkable field rather than a matter of memory.

### 2.4 L4 — Reading & extraction

Produces two things from the same reading act, never inferred from each other:

1. `citation_card.exact_passage` + `page_or_locator` + `scope` (`DIRECT_QUOTATION | PARAPHRASE |
   SUPPORTS_GENERAL_CLAIM_ONLY | CONTEXT_ONLY_NOT_EVIDENCE`) — the S8 citation-card fields,
   unchanged.
2. One row in `dialogue_table.md` (§3.4 new template) — "what the source solves / how / same-
   different vs us," in the conversation-with-the-problem form request 35c specified.

### 2.5 L5 — Citation-card verification ("best a human can do")

Full standard in §5 below. Produces `citation_card.status: VERIFIED` (or a terminal non-VERIFIED
state, §1.5 of S8, unchanged) plus the spot-check record required by §5.4.

### 2.6 L6 — Neighbour table + manifest freeze

`neighbour_table.md` rows are populated from the VERIFIED subset of this run's citation cards
(a row may cite a `NOT_FETCHED` source only as `Open` tier, per that template's own tier rule).
`litreview_manifest.yaml` (§ template) is assembled, its two gates computed (§5.5–§5.6), and
frozen. Freezing is the event the checklist (§7) and every downstream gate look for.

---

## 3. Templates this stage adds or reuses

| File | New/reused | Purpose |
|---|---|---|
| `design/templates/knowledge/litreview_manifest.yaml` | **New** | Per-hypothesis frozen ledger: every citation card, its status, the diversity roll-up, the stratified selection table, and the two gates. |
| `design/templates/knowledge/source_acquisition_log.yaml` | **New** | Public-safe bridge between a search result and a citation card's `fetch_status`, recording the `rl`-boundary honestly without leaking local paths. |
| `design/templates/knowledge/lit_review_gate_checklist.md` | **New** | The literal checklist an independent reviewer runs before a lit-review section may be drafted or published. |
| `design/templates/knowledge/dialogue_table.md` | **New** (coordinator addition, 35c) | The "conversation with the problem" table — replaces a chronological survey as the default lit-review output. |
| `design/templates/knowledge/hypothesis_selection.yaml` | **New** (coordinator addition, 35d) | The human's comparison and choice among *n* candidate hypotheses after their *n* LRS runs. |
| `design/templates/knowledge/citation_card.yaml` | Reused, unchanged | S8's Integrity Firewall card — LRS is a consumer, not a re-designer, of this schema. |
| `design/templates/knowledge/search_log.yaml` | Reused, unchanged | S8's frozen search episode object. |
| `design/templates/knowledge/sr_protocol_prisma_lite.md` | Reused, unchanged | S8's PRISMA-2020-lite fill-in form. |
| `design/templates/knowledge/neighbour_table.md` | Reused, unchanged | S13's descriptive comparison table — LRS's dialogue tables feed it, per rule 31e. |

### 3.4 `dialogue_table.md` — the distinctive form (request 35c)

Columns: `source | how it sees the problem | what it separates | what it assumes | agrees with H
| disagrees with H | what it would say against us | citation_card | verified`. Rows are **never**
ordered by date, "who came first," or "seminal/pioneering" language — date is metadata only, kept
(if wanted) in a column that does not set row order. A stance (`agrees`/`disagrees`) may only be
recorded once the row's `citation_card.claim_match_verified == true`; before that, the legal
values are `undetermined` (not yet read at that depth) or the row does not yet exist. Full
template body: `design/templates/knowledge/dialogue_table.md`.

---

## 4. The research-stack interface — what crosses, what never does

Unchanged in principle from S8 §7, restated here because request 35 explicitly asks LRS to "use
the full research system" (`rl`) **together with** the citation subsystem:

**Read from `rl --help` (2026-09-04, read-only, nothing modified):**
```
rl status | start | stop | restart | logs [svc] | zotero | calibre | web | consume <file>
| import [dir] | rag | creds
Components: Zotero 9 (references/BibTeX), Calibre 9 (e-books/textbooks),
Paperless-ngx (OCR + full-text search, http://<lan-host>)
Note: PRIVATE and standalone. `rl rag` writes only to a dedicated folder, NOT connected to the
an internal RAG corpus.
```

**Crosses into the public repo:**
- The public, resolvable `identifier` (DOI/PMID/ISBN/ARXIV/OFFICIAL_URL/`BLACKBOX_NOTE`).
- The exact quoted/paraphrased passage, page/locator, and scope — because it is being cited, a
  normal act of scholarship, not a leak of the shelf itself.
- An honest `acquisition_status`/`acquisition_route` (§2.3) — including `RL_PRIVATE_SHELF` as a
  named route value, without naming *which* collection/key inside it.

**Never crosses:**
- A local filesystem path, a Zotero item key, a Paperless document id, a `rl`-internal
  identifier of any kind, or a folder/collection name from the private shelf.
- Any content from `rl rag`'s dedicated export folder (that folder is explicitly not
  RAG-connected and not part of this interface at all — it is out of scope, mentioned only so a
  future maintainer does not assume it is a citation source).

**Optional export adapter (described, not required, per S8 §7's own stance, restated for LRS):**
a private, out-of-repo adapter *may* let `rl` push a `metadata_verified: true` signal into a
`source_acquisition_log.yaml` row when the founder has already independently confirmed a source
in the private library — but the public mechanical checker (`rwi cite check`) never depends on
this adapter being present and always re-verifies via Crossref/OpenAlex/PubMed/DataCite
independently. The private shelf **informs** acquisition; it never **substitutes** for the public,
reproducible check (§5). Building this adapter at all remains an open founder decision (§9.6,
carried over from S8 §9.6 — LRS does not force the decision either way).

---

## 5. The "best a human can do" citation-accuracy standard

### 5.1 Why this is enumerated, not aspirational

"เพื่อความแม่นยำสูงสุด" (for maximum accuracy) is the founder's own stated purpose for this whole
stage. RWI cannot promise infallibility (readout-not-truth: every check here is itself a finite,
retained readout of a source, not the source's truth handed over). What it can promise is that
**every check a solo scholar with no institution and no paid database access can actually run,
gets run, every time, and is recorded as run** — the ceiling is honest effort, not perfection.

### 5.2 The checklist, with independence class per item

| # | Item | What it checks | Independence class required | Consequence of failure |
|---|---|---|---|---|
| 1 | Identifier resolves | The source exists at all (existence, not support) | I4 (mechanical lookup) | `FETCH_FAILED` — terminal, human review |
| 2 | Metadata matches | Title/author/year/venue as claimed | I4 (Crossref/OpenAlex/PubMed/DataCite) or `UNCHECKED_OFFLINE` honestly | `metadata_verified: false` — blocks `VERIFIED` |
| 3 | Full text obtained (or honestly marked otherwise) | `acquisition_status` resolved, never silently assumed `obtained` | Human (I5) confirms access, or I4 mechanical HTTP check | `not_obtained` — legal, but blocks any stance in the dialogue table |
| 4 | Exact passage located | The claim is backed by a specific locator, not "the paper generally says" | Human (I5) or decorrelated AI route (I3) reads the acquired text directly | Blocks `claim_match_verified` |
| 5 | Claim match verified | The passage, at the claimed scope, actually supports the citing sentence | **I5 human, or I3 decorrelated AI route + mandatory human spot-check sample** (§5.4) | Blocks `status: VERIFIED`; a false positive here is exactly the SS §7 "source existence ≠ claim support" failure |
| 6 | Retraction check | Source has not been retracted/corrected since | I4 (Crossref/Retraction Watch) | `RETRACTED` — hard block, Xenon ledger row |
| 7 | Version check | Preprint vs published-version-of-record distinguished | I4 (mechanical, DOI resolves to a version) or I5 | Ambiguous `version_status` — a paper citing a superseded preprint as if it were the published, peer-reviewed text is a `METADATA_MISMATCH`-class error |
| 8 | Secondary-citation ban | The passage was read from the source itself, not from another paper's quotation of it | I5 or I4 (direct-read confirmation) | Hard block on any dialogue-table stance |
| 9 | Fabrication check | The `exact_passage` genuinely appears in the fetched document | I5, or I4 string-search against the fetched text | `SCRAM` immediately — see §5.3 |

Items 1, 2, 6, 7 are the parts a mechanical lookup can do alone and should always be run first
(cheapest, catches the most common and least ambiguous errors). Items 3–5, 8–9 require a reading
act and are where the human/AI division of labour (§6, §8) actually matters.

### 5.3 SCRAM and Xenon — unchanged from S8, restated for completeness

A citation found to reference a non-existent source, or whose `exact_passage` does not appear
anywhere in the fetched document (a fabricated quotation), becomes `status: SCRAMMED`
immediately; the claim card it backed drops to `Open` tier until re-evidenced; the release gate
hard-blocks any paper containing a `SCRAMMED` citation; a row is appended to that project's
`XENON_LEDGER.md` (never purged, per-project home, `rwi kg merge` renders the repo-wide view —
chair ruling B6). LRS adds no new SCRAM condition beyond S8's; it inherits it.

### 5.4 The spot-check standard — proposed n%, and why

**Proposal (Dr, founder override expected): n = 20%, with two floors.**

- **Small-N floor**: if a manifest cites fewer than 10 sources total, spot-check **100%**
  (`small_n_rule_applied: true`) — at that scale, a 20% sample is 1–2 items, which is not a
  meaningful audit and costs the human almost nothing extra to just check them all.
- **Stakes floor**: any citation backing a claim reaching `tier ≥ fit_calibrated`, or feeding a
  card that will ever reach `k_state: K2`, is spot-checked **100%** regardless of sample math —
  because K2 requires an I5 human leg anyway (§4.2 of FOUNDATION), and a citation under it is
  exactly the kind of load-bearing link the E∧A∧D condition treats as no weaker than its weakest
  verified link.
- **Otherwise, 20% stratified random** across the manifest's citations, drawn *after* the
  citation set is frozen (never cherry-picked to be the easiest to check) and reported with
  `sampled_citation_ids` so the sample itself is auditable, not just its pass/fail summary.

**Why 20% and not some other number (honest reasoning, not a proof):** this is closer to a
convenience convention than a statistically powered estimate — with small manifest sizes typical
of a standalone scholar's per-hypothesis literature conversation (tens, not hundreds, of
sources), no sample size here supports a population-level error-rate confidence interval; the
purpose of the number is to make *some* independent re-check structurally mandatory rather than
optional, not to certify an error rate. This mirrors acceptance-sampling conventions used in
other QA contexts (e.g. ISO 2859-family lot inspection, cited here only as a *shape* analogy —
percentage-of-lot sampling with tighter rules at higher stakes — not as an endorsement that RWI
meets that standard's actual statistical guarantees). **Tag: Dr, not `finite_diagnostic`** — this
number is a proposed policy, not a measured or derived quantity, and must never be cited
downstream as if it carries a proven error-detection rate.

### 5.5 Accuracy gate (per-source)

`litreview_manifest.gate.accuracy_gate == PASS` requires: every listed citation at
`status: VERIFIED`; the spot-check sample at `spot_check_result: PASS`; zero secondary-citation
violations; no `RETRACTED` source in scope. `PASS_WITH_LIMITS` is legal when a small number of
lower-stakes citations remain `PAYWALLED_ABSTRACT_ONLY`/`NOT_FETCHED` and are excluded from
dialogue-table stances (disclosed, not hidden) while the rest of the set clears `PASS`.

### 5.6 Diversity gate (set-level) — request 35e, coupled to but separate from accuracy

Accuracy answers "is each source what we say it is." Diversity answers a different question: "did
we actually look in more than one place, in more than one language, for more than one kind of
answer." A manifest can score perfectly on §5.5 while citing three English-language veterinary
hospital web pages that all happen to agree — accurate, and simultaneously a monoculture.

**Dimensions audited (recorded per source, rolled up in the manifest, §template):**
language (EN/TH/other — matching the GDA global+local track questions already in S8 §2.3),
discipline/tradition, source type (`peer_reviewed | preprint | grey_literature | practitioner |
community | archival | field_observation`), search route/database (never one database, never
one AI route alone), stance toward the hypothesis (`agrees | disagrees | orthogonal |
undetermined` — **zero `disagrees` despite a real challenge-family search having run is a flag,
not a quiet success**), and geography/institution.

**Two rules, stated exactly:**
1. Concentration in one cell of any dimension (default threshold 80% of sources in one cell —
   Dr, founder may set a different default per project) triggers `D-LIT-CONCENTRATED` — never
   silently accepted, never hidden by rounding language ("largely international") that avoids
   stating the count.
2. **Never claim "diverse sources" in prose without pointing at the `diversity_audit.counts`
   block.** This is the same discipline as `D-COMPARISON`'s "no novelty framing without the
   table" — a qualitative diversity claim with no attached counts is exactly the kind of
   unfalsifiable positioning language request 31 already forbade for market comparisons, applied
   here to evidence-base comparisons.

**Gate semantics (deliberately asymmetric):** `diversity_gate: FAIL` (an undisclosed
concentration, or the audit skipped entirely) blocks `overall`. A **disclosed** concentration
downgrades `overall` to `PASS_WITH_LIMITS`, it does not hard-block outright — a standalone
scholar genuinely may not have access to a Thai-language peer-reviewed source on every question,
and forcing a hard block here would either (a) stop real work from proceeding at all, or worse,
(b) create pressure to pad the manifest with weak filler sources just to clear a diversity
count — exactly the failure mode `D-PARTIAL-SET` (structural honesty for under-3-member
structures) already names for the DVP route set, applied here to the evidence set.

### 5.7 Stratified selection (request 35f)

When more candidate sources exist than will be cited (the common case once a search returns
dozens of hits), selection is not "whichever we found first" or "whichever is highest quality
overall" — it is **stratified**:

1. Define strata as the cross of `(quality_tier × region × language × source_type)` — quality
   tier may use a `venue_quality_index` (e.g. a Scopus/SJR quartile) **as metadata only**: it is
   recorded with an index name and a date read, and it is never a substitute for
   `claim_match_verified` (Legitimacy ≠ Truth, Appendix A families A/D — a Q1-journal source that
   fails claim-match verification is still not citable).
2. Within each populated stratum, select the candidate with the strongest verification result
   (already `VERIFIED` beats `CANDIDATE`; a direct quotation beats a paraphrase-scope match).
3. Across strata, **fill empty strata before adding a second source to any stratum that already
   has one** — spread is prioritized over depth in any one cell, up to the manifest's target
   citation count.
4. Even when the whole candidate pool is restricted to top-tier venues (e.g. everything is
   Scopus Q1), spread must still be reported **within** that quality tier across
   region/language/institution — a set of five Q1 papers that are all from the same country and
   language is still a concentration, and `strata_table` must show this explicitly rather than
   letting the quality tier stand in for diversity.
5. An empty stratum is recorded, not omitted — `strata_table` carries a row with
   `selected: null` and a note, matching the `LOCAL_EVIDENCE_NOT_FOUND ≠ NO_LOCAL_EVIDENCE_EXISTS`
   discipline already binding elsewhere (S8 §2.3): a stratum with no candidate found is a
   search-coverage fact, not proof nothing exists there.

---

## 6. Hypothesis selection (request 35d)

After the *n* LRS runs for *n* lens-out hypotheses each freeze their own manifest and dialogue
table, a **human** (never an AI route alone — this is `responsible: human`, non-delegable, same
rule as the claim card's own `human_owner`/`responsible` fields) fills
`hypothesis_selection.yaml` (§3 template), comparing candidates on:

- **Developability** — what the dialogue table's own `orthogonal`/`undetermined`/`disagrees`
  rows leave genuinely open; a hypothesis whose own lit review found nothing left to test is a
  flag, not a reason to prefer it.
- **Access/evidence available** — can new access actually be obtained (e.g. a urinalysis, a new
  observation window) for this hypothesis's falsifier, or does it dead-end at "would need a
  clinician."
- **Falsifier reachable with our resources** — cost/time/equipment/permission realism, not just
  logical falsifiability.
- **Independence routes available** — the honest ceiling on `independence_class` (§4.2 ladder)
  this hypothesis's evidence base can currently reach.
- **Risk and ethics** — human-participant/vulnerable-subject flags, domain-safety disclaimers
  this hypothesis would trigger (e.g. `D-NOT-DIAGNOSTIC`).
- **Genre fit** — which of the nine §6.2 genre rows this hypothesis's evidence shape actually
  supports.

**Outcome:** zero, one, or more than one hypothesis may be selected (parallel tracks are legal).
Every **parked** hypothesis keeps a required, non-empty `reason` and stays fully in the repo
(its manifest and dialogue table are not deleted) — matching the append-only, nothing-silently-
dropped discipline already binding on dissent records and the Xenon/Disagreement ledgers. The
selection event itself is appended to the Blackbox Note's `cooking:` log (request 32's own
requirement that every transformation, by whom, is published, never sealed) — a hypothesis
selection is exactly a "cooking" transformation of the raw material into what the paper will
carry forward.

**Only the selected hypothesis(es) route into the genre router** (`FOUNDATION_v0.2.md` §6.1's
9-row table) and onward into S4 method design and S5 paper drafting.

---

## 7. The gate: no lit-review section without a manifest at PASS

This is request 35's central, non-negotiable mechanism, restated exactly:

> No lit-review section may be **drafted** (not merely published) until its
> `litreview_manifest.yaml` reaches `gate.overall ∈ {PASS, PASS_WITH_LIMITS}`.

This gate lives in three places, all pointing at the same one manifest object (one fact, one
home):

1. **S4 (rigorous method)** — a method design that presupposes a literature position (e.g. "the
   evidence shows X, so we test Y") may not proceed while its hypothesis's manifest is `FAIL` or
   `PENDING`.
2. **S6/§7.4 release gate** — `PUB-ADVERSARIAL-REVIEW`'s R4 (citation accuracy) dimension is
   exactly this stage's own §5.5/§5.6 gates, re-run by an independent reviewer, never the
   manifest's own maker (MC-02) — see `lit_review_gate_checklist.md` §7's own line making this
   explicit.
3. **The genre DAGs (S11/§6)** — every genre row that has a literature-synthesis or
   related-work component (all nine rows carry *some* form of this — even `formal_proof` and
   `case_study` genres cite prior mechanisms) routes that component through this gate rather than
   through free-text "related work" prose. The full checklist a genre's own reviewer runs before
   accepting a lit-review section is `lit_review_gate_checklist.md` in full — S14 does not
   duplicate the checklist text inside S11, S11 references it.

Failure mode this gate is specifically built to close (the trap named in S8 §0, re-applied
here): a paper's "we reviewed the literature" sentence with no frozen object behind it — the
exact "the rule existed in prose, nobody could query it" pattern already caught once in this
workspace's own doc-ecosystem history.

---

## 8. Disclaimers this stage emits

Reusing the FOUNDATION §5 catalogue wherever an existing id already fits (one catalogue, one
home, per chair ruling C2 — S14 does not mint a duplicate vocabulary):

| id | Reused/new | Trigger (in LRS terms) |
|---|---|---|
| `D-CITATION-UNVERIFIED` | Reused | Any cited source with `fetch_status ∈ {NOT_FETCHED, FETCH_FAILED, UNCHECKED_OFFLINE}` or `status` below `VERIFIED` |
| `D-DVP-NOT-K2` | Reused | A dialogue-table stance or manifest verdict is described as "verified/certified" while the underlying `independence_class` tops out below I5 |
| `D-SAME-VENDOR` | Reused | The claim-match verification route for every citation in a manifest is the same AI vendor/model |
| `D-COMPARISON` | Reused | Any neighbour_table.md row this manifest feeds — no novelty framing, same/different/cited only |
| `D-BLACKBOX-NOTE` | Reused | The hypothesis-selection event is logged in the cooking log; the appendix carries it forward |
| `D-NO-VERTICAL-AUTHORITY` | Reused | Any mention of a venue's prestige, impact factor, or peer-review status as if it settled a claim rather than describing a venue |
| `D-LEGAL-NEQ-EPISTEMIC` | Reused | A cited "official/gray literature" source (statute, regulation, official guidance) is treated as settling a factual claim rather than a legal fact |
| **`D-LIT-MODE`** | **New** | The `search_log.review_mode` for this manifest is anything other than `SYSTEMATIC_REVIEW` — states which of the five non-SR labels applies, next to the lit-review section, not once in a methods footnote |
| **`D-LIT-NOT-OBTAINED`** | **New** | A source appears in the search log (`sources_found`) but its `acquisition_status == not_obtained` or `abstract_only` — it may be *mentioned* as a known-but-unread source, never given a dialogue-table stance |
| **`D-LIT-CONCENTRATED`** | **New** | Any `diversity_audit.concentration_flags` entry — states the concentrated dimension and the percentage, next to the dialogue table or neighbour table it affects |

No existing id fit the review-mode-honesty case or the diversity-concentration case cleanly
without collapsing two distinct trigger conditions into one id (the same reasoning the chair
ruling used for `D-CITATION-UNVERIFIED`'s own `state` parameter design) — these three are
proposed as genuinely new, per the task's own suggestion (`D-LIT-MODE`, `D-LIT-NOT-OBTAINED`)
plus one more the diversity requirement (35e) makes necessary (`D-LIT-CONCENTRATED`).

---

## 9. Callable layer

### 9.1 CLI surface

```
glosa lit new       <problem-slug> <hypothesis-ref>   # scaffold search_log.yaml + dialogue_table.md
glosa lit search     <search-log-id>                  # run/record support+challenge query families
glosa lit freeze      <search-log-id>                  # lock frozen_scope before sources_found opens
glosa lit acquire     <citation-card-id>                # attempt acquisition; writes source_acquisition_log row
glosa lit extract     <citation-card-id>                # record exact_passage/page_or_locator/scope + dialogue row
glosa lit cite-check  <citation-card-id> [--all <dir>]  # mechanical Crossref/OpenAlex/PubMed/DataCite + retraction check
glosa lit table       <hypothesis-ref>                  # render/refresh dialogue_table.md + neighbour_table.md rows
glosa lit select      <problem-slug>                    # human-run: compare n manifests, write hypothesis_selection.yaml
glosa lit manifest    <hypothesis-ref> [--freeze]        # assemble/freeze litreview_manifest.yaml, compute both gates
```

`glosa lit select` deliberately has no `--auto` flag: it opens the comparison table and requires
a human `decided_by` before it will write a non-empty `selection.chosen` list — matching the
non-delegable `responsible: human` field already binding on the claim card.

### 9.2 MCP tools

One tool per CLI verb above (`lit_new`, `lit_search`, `lit_freeze`, `lit_acquire`, `lit_extract`,
`lit_cite_check`, `lit_table`, `lit_select`, `lit_manifest`), vendor-neutral per request 13 —
callable identically from Claude Code, Codex, Gemini CLI, or a local model, matching the
cross-vendor review gate's own plain-file contract (`FOUNDATION_v0.2.md` §4.3): a packet-style
prompt (`templates/knowledge/cross_vendor_review_packet.md`'s own pattern, reused rather than
re-invented) can drive `lit_extract`/`lit_cite_check` for a decorrelated I3 route without any
shared session.

### 9.3 Human/AI division of labour, made visible per stage (request 24)

| Stage | Human does | AI does |
|---|---|---|
| L1 framing | Confirms the question is the real one, not a convenient proxy | Drafts vocabulary/inclusion-exclusion from claim-card fields |
| L2 search | Sets the honest label and stopping rule | Runs/drafts query families across tracks |
| L3 acquisition | Holds the private shelf; confirms paywalled/institutional access | Attempts open-access resolution; records HTTP status |
| L4 extraction | Reads the acquired text directly at least for the spot-check sample | Drafts dialogue-table rows from a first read; flags own inferential commitments (`ai_filled`) |
| L5 verification | Is the I5 route, or confirms an I3 route was genuinely decorrelated | Proposes candidates; never self-certifies its own `claim_match_verified` |
| L6 manifest | Signs as `human_owner`; approves the freeze | Assembles roll-up counts, drafts `strata_table` |
| Selection | Decides `hypothesis_selection.chosen`; writes the `reason` | Proposes the comparison table's contents, never the decision |

---

## 10. Worked mini-example — the cat question (request 26), run through the LRS

> This is a **demonstration of the pipeline's discipline**, not a completed literature review.
> Every source below was located via a live web search run for this task (2026-09-04); none of
> the three full texts were opened in this session. Per §2.3's secondary-citation ban and §5's
> "never fabricate a check you did not run," every citation card below is honestly marked
> `NOT_FETCHED` / `claim_match_verified: false`, and the resulting manifest's `accuracy_gate` is
> honestly `FAIL` — the gate is shown *working*, not shown passing.

### 10.1 Problem and candidate hypotheses (35d — 2–3 candidates)

- **Problem (Blackbox Note, verbatim, request 26):** "ทำไมแมวเยี่ยวไม่เป็นที่" (why is the cat's
  urine not staying "in its place") — owner standpoint, n=1, not a vet.
- **Lens-in:** access source = observed urine outside the box (place/count/dates); the readout
  separates in-box/out-of-box but **not** illness/dirty-box/stress/marking (same fiber) —
  `contaminated_concept_hit: "ไม่เป็นที่" hides a human decision policy`.
- **Candidate lens-out hypotheses (n=3):**
  - **H1 — box-condition hypothesis**: location/cleanliness/box-type aversion is driving
    out-of-box elimination. Falsifier: a 14-day box-condition intervention (clean, relocate, or
    change litter type one variable at a time) changes the out-of-box rate.
  - **H2 — medical/periuria hypothesis**: a urinary or systemic medical condition (e.g. urinary
    tract disease, kidney disease) is causing or contributing to the behavior. Falsifier: a vet
    urinalysis/exam is positive or negative for a named condition — **this falsifier requires a
    new access source (a clinician) the owner cannot supply alone**.
  - **H3 — marking-vs-latrine hypothesis**: the behavior is territorial marking (not a toileting
    failure at all) rather than latrine avoidance, plausibly tied to household composition
    (multi-cat, free outside access). Falsifier: pattern/location/posture distinguishes marking
    (vertical surfaces, small volume) from latrine avoidance (horizontal surfaces, full volume) —
    **requires household-composition facts (multi-cat? outside access?) not yet established in
    this case**.

### 10.2 Sources found (one search run, `RAPID_EVIDENCE_CHALLENGE` label — honest, not a systematic review)

`search_log.yaml.review_mode: RAPID_EVIDENCE_CHALLENGE` (a single time-boxed web search for this
worked demonstration — explicitly **not** `SYSTEMATIC_REVIEW`, per FC-S8-1). Three sources
located:

1. **VCA Animal Hospitals**, "Inappropriate Elimination Disorders in Cats" —
   `https://vcahospitals.com/know-your-pet/inappropriate-elimination-disorders-in-cats` —
   `identifier.kind: OFFICIAL_URL`; source_type `practitioner`; language `en`; geography `US`
   (veterinary hospital chain).
2. **ASPCA**, "Litter Box Problems" —
   `https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues/litter-box-problems` —
   `identifier.kind: OFFICIAL_URL`; source_type `community`/animal-welfare organization;
   language `en`; geography `US`.
3. **Peer-reviewed study** — Peer et al. (as indexed), "Common Risk Factors for Urinary House
   Soiling (Periuria) in Cats and Its Differentiation: The Sensitivity and Specificity of Common
   Diagnostic Signs," *Frontiers in Veterinary Science*, 2018 — PubMed listing
   `https://pubmed.ncbi.nlm.nih.gov/29892606/`, DOI-bearing venue `10.3389/fvets.2018.00108`
   (DOI read from the search result, not independently confirmed against Crossref in this
   session — `metadata_verified: false`, honestly). `identifier.kind: DOI`; source_type
   `peer_reviewed`; language `en`; an owner-survey study (n=245).

**What was actually verified in this session:** only that these three pages/records surfaced on
a live web search for the stated query and that their titles/URLs/PMID match what is written
above. **Not verified:** full-text content, exact passage support for any hypothesis, retraction
status, Crossref metadata match. This is why every card below stays `CANDIDATE`, not `VERIFIED`.

### 10.3 Citation cards (honestly `NOT_FETCHED`)

| citation_card | identifier | fetch_status | metadata_verified | claim_match_verified | status |
|---|---|---|---|---|---|
| `cite-cat-001` | OFFICIAL_URL (VCA) | `NOT_FETCHED` | `false` | `false` | `CANDIDATE` |
| `cite-cat-002` | OFFICIAL_URL (ASPCA) | `NOT_FETCHED` | `false` | `false` | `CANDIDATE` |
| `cite-cat-003` | DOI `10.3389/fvets.2018.00108` | `NOT_FETCHED` | `false` | `false` | `CANDIDATE` |

### 10.4 Dialogue table (excerpt, H1 — box-condition hypothesis)

| source | how it sees the problem | what it separates | what it assumes | agrees | disagrees | what it would say against us | citation_card | verified |
|---|---|---|---|---|---|---|---|---|
| VCA (cite-cat-001) | Frames "inappropriate elimination" as a clinical/behavioral disorder category with medical causes named first | Separates medical vs behavioral causes; within behavioral, notes cleanliness/location/box-type as named factors — not fetched, so this is from the search snippet only, **not** a verified read | Assumes a vet visit is the appropriate first step for any case | `UNDETERMINED` (not fetched) | `UNDETERMINED` | Likely: "rule out medical causes before assuming box condition" — directly relevant to H2, a challenge to treating H1 as sufficient on its own | `cite-cat-001` | metadata:false / claim_match:false |
| Frontiers 2018 study (cite-cat-003) | Frames the problem as *periuria* with two behaviorally distinct patterns (marking vs latrine) rather than one undifferentiated "inappropriate elimination" | Separates marking from latrine behavior by risk-factor profile (age, multi-cat household, outside access) — per search-result summary only, not fetched | Owner-survey methodology assumes owner-reported categorization is accurate | `UNDETERMINED` (not fetched) | `UNDETERMINED` | Likely: "litterbox attributes were not found significant in our sample" — a direct challenge to H1 if that finding holds under a full read | `cite-cat-003` | metadata:false / claim_match:false |

(ASPCA row omitted here for length; same `UNDETERMINED`/`UNDETERMINED` honesty applies.) Note
the table's own required column ("what it would say against us") is filled from the search
snippet's stated findings even while the stance columns stay `UNDETERMINED` — this is legal: the
objection can be *stated* from what was read (a search summary) without yet being *verified*
against the primary text.

### 10.5 Diversity audit (honest, and it flags itself)

```
by_language:   { en: 3, th: 0, other: 0 }
by_source_type: { practitioner: 1, community: 1, peer_reviewed: 1 }
by_search_route_or_database: { web_search_general: 3 }   # ONE route used — concentration
by_geography_or_institution: { US: 2, unclear_from_snippet: 1 }
by_stance: { agrees: 0, disagrees: 0, orthogonal: 0, undetermined: 3 }
concentration_flags:
  - { dimension: language, cell: en, percent: 100 }          -> D-LIT-CONCENTRATED
  - { dimension: search_route_or_database, cell: web_search_general, percent: 100 } -> D-LIT-CONCENTRATED
zero_disagree_flag: true   # not because none disagree — because nothing has been claim-match
                            # verified yet to license a stance at all; disclosed as such, not
                            # collapsed into "sources agree"
```

### 10.6 Stratified selection table (35f, illustrative — pool of 3, no real stratification yet possible)

| stratum (quality_tier × region × language × source_type) | candidates considered | selected | reason |
|---|---|---|---|
| peer_reviewed × international-survey × en × journal | cite-cat-003 | cite-cat-003 (candidate only) | Only peer-reviewed candidate found this pass |
| practitioner × US × en × hospital-authored | cite-cat-001 | cite-cat-001 (candidate only) | Only practitioner candidate found this pass |
| community × US × en × welfare-org | cite-cat-002 | cite-cat-002 (candidate only) | Only community candidate found this pass |
| *(empty)* any Thai-language stratum | none found | `null` | `LOCAL_EVIDENCE_NOT_FOUND` — a search-coverage fact this pass, not evidence Thai-language sources on this topic don't exist |

With only three candidates and one search route, this table mostly shows **empty strata**
honestly rather than a real fill-empty-first exercise — exactly what a single `RAPID_EVIDENCE_
CHALLENGE` pass should show before a real `SCOPING_SEARCH`/`SYSTEMATIC_REVIEW` widens the pool.

### 10.7 Manifest verdict (honest FAIL, gate working as designed)

```
gate.accuracy_gate:  FAIL   # zero VERIFIED citations; claim_match_verified false on all three
gate.diversity_gate: FAIL   # both language and search-route concentration at 100%, undisclosed
                             # would be a violation — here it IS disclosed via the flags above,
                             # so this FAIL is the honest "audit ran and found concentration" case,
                             # not the "audit was skipped" case
gate.overall:        FAIL
blocked_reason: "No citation reached VERIFIED (no full text opened this session); single search
                 route and single language; H1's lit-review section may not be drafted from this
                 manifest as-is."
```

### 10.8 Hypothesis selection (35d)

Because none of the three manifests (H1/H2/H3 would each need their own LRS run; only H1's is
shown in detail above) reach `PASS`, a real `hypothesis_selection.yaml` at this point would
legitimately record: `selection.chosen: []`, `reason: "no candidate hypothesis has a manifest
past FAIL yet — return to L2/L3 with a real acquisition attempt via rl before selecting."` **This
is deliberately what the worked example shows**: the LRS gate refusing to let a fabricated or
under-evidenced lit review proceed, exactly the mechanism request 35 asked for. A completed,
real run (with full texts actually opened through the founder's `rl` shelf or open-access
retrieval, and at least one Thai-language or disagreeing source sought) would be required before
H1 could route to the genre router.

---

## 11. How the LRS threads into the genre DAGs and the release gate

- **Genre DAGs (S11/§6.2):** every genre row's structure column that includes a literature/
  related-work component (all nine — even `formal_proof` cites prior lemmas/definitions, even
  `case_study`/`practice report` cites prior practice reports for comparison) now names its
  gate as *"lit-review section: `litreview_manifest.gate.overall ∈ {PASS, PASS_WITH_LIMITS}` for
  every hypothesis cited in this section"* rather than a free-text "cite relevant literature"
  instruction. This closes the same class of gap `reviews/S11_anchor.md` Must-fix 2 already
  found for the human-experience field (a stage named in prose without a place in every genre's
  own structure column).
- **Release gate (§7.4 PUB-ADVERSARIAL-REVIEW):** dimension R4 (citation accuracy) is this
  stage's §5.5 accuracy gate, re-run by an independent reviewer; the leak-scan dimension R1
  additionally re-checks `source_acquisition_log.no_local_leak_check` on every acquisition row
  reachable from the paper — a manifest that passed its own gate at freeze time is re-verified,
  never grandfathered, at publish time (matching PUB-ADVERSARIAL-REVIEW's own fail-closed rule:
  "no adversarial pass run before a public-facing publish ⇒ do not publish").
- **Hypothesis selection → genre route:** the selected hypothesis's `genre_fit` criterion (§6)
  is not a suggestion — the chosen genre must be one that `hypothesis_selection.candidates[].
  criteria.genre_fit.candidate_genres` actually listed for that hypothesis; a mismatch (choosing
  a genre the candidate's own evaluation did not name as a fit) is a reviewer-visible flag at L2+
  of MIMCG, matching the reviewer-check already named for the one-problem-one-project rule
  (`FOUNDATION_v0.2.md` §8.1 table).

---

## 12. Open questions only the founder can decide

1. **The `review_mode` name collision (§2.2)** — `search_log.yaml`'s search-episode label and
   `FOUNDATION_v0.2.md` §7.8's verification-route label share a field name and one enum value.
   Should one be renamed (e.g. `search_mode` for the search-episode sense, keeping `review_mode`
   for the verification-route sense), or is the overlap intentional and this design's reading of
   them as two different axes wrong?
2. **Concentration threshold (§5.6)** — is 80%-in-one-cell the right default trigger for
   `D-LIT-CONCENTRATED`, or should it be lower (e.g. 60%) given how small most per-hypothesis
   manifests will be, where 80% of 3 sources is already the entire set?
3. **Spot-check n% (§5.4)** — is 20% (with the small-N-floor and stakes-floor carve-outs) the
   right default, or should the founder set a different number, or make it project-configurable
   from the start rather than a single repo-wide default?
4. **Research-library export adapter (§4, carried over from S8 §9.6)** — build the optional
   private `rl → source_acquisition_log` push adapter, or keep the boundary fully manual
   (founder copies the identifier and acquisition fact by hand)?
5. **Venue-quality index source (§5.7)** — should RWI name a specific index (Scopus/SJR,
   Journal Impact Factor, or an open alternative like the DOAJ/OpenAlex venue metadata) as the
   canonical `venue_quality_index.index_name`, or leave it genuinely open per-citation (as
   currently specified) since different fields use different indices and RWI does not want to
   privilege one commercial index as if it were epistemic authority (`EPIS-KNOWLEDGE-VALIDATION`
   — a quartile is metadata, never a certification)?
6. **Genre-DAG rewrite scope (§11)** — should this stage's authors directly edit S11's file to
   add the gate reference to all nine rows now, or leave that edit for the S11 owner/a synthesis
   pass, since S11 was produced by a different designer and this task's scope was S14 plus its
   own templates?

---

## 13. Deliverables of this stage

- This file (`design/S14_literature-review-system.md`).
- `design/templates/knowledge/litreview_manifest.yaml`
- `design/templates/knowledge/source_acquisition_log.yaml`
- `design/templates/knowledge/lit_review_gate_checklist.md`
- `design/templates/knowledge/dialogue_table.md`
- `design/templates/knowledge/hypothesis_selection.yaml`

All templates are Dr-tier proposed schemas — unreviewed, machine-validatable in intent, not yet
backed by a validator script (kernel/CLI implementation is S4/S7 build work, out of scope for
this design stage, matching S8's own §10 closing note).
