tier: Dr (specified; independently unreviewed)

# methodology/data — glosa data tables

Five machine-readable tables that back the glosa gates. Each file's `_meta` block states its own
tier, source documents, and the one-fact-one-home rule that applies to it. **Field names used
inside `trigger`/`enforced_by` expressions are never redefined here — they are defined only in
`schema/*.schema.json`.** These files reference those names; they do not own them.

## Files

- **`disclaimer_catalogue.json`** — every disclaimer id from `design/FOUNDATION_v0.5.md` §5, plus
  the literature-review ids from `design/S14_literature-review-system.md` §8
  (`D-LIT-MODE`, `D-LIT-NOT-OBTAINED`, `D-LIT-CONCENTRATED`) and one new id
  (`D-SELF-EXPERIENCE-NOT-GENERAL-EVIDENCE`, backing `NC-64`). 37 rows. `gate_release` refuses
  release while any `mandatory: true` trigger is active and its id is absent from
  `claim_card.disclaimers_emitted`.
- **`genre_router_table.json`** — the 9 genre rows from FOUNDATION §6.2, each with structure,
  IMRAD status, claim ceiling, mandatory disclaimers (genre-specific, layered on the universal
  floor), section list, and the Blackbox Note requirement. Also carries `venue_track` requirements
  (`international` / `thai_tci` / `none`) — the `thai_tci` block reproduces the บทความวิชาการ vs
  บทความวิจัย section/ethics requirements from
  `cpg_research_journal/.../design/S11_research-structure-dags.md` §10, itself marked `Dr` there
  and unverified against any live TCI journal — and the `companion_of` requirement.
- **`non_collapse_table.json`** — NC-01 through NC-64 (Families A-H), reproduced from
  `design/S9_non-collapse-table.md` (NC-01..NC-61) plus `design/FOUNDATION_v0.5.md` Appendix A
  (NC-62..NC-64, chair ruling C6). **Ids are append-only** — a future pass may add NC-65 onward,
  but no id here is ever renumbered or reused, per the source document's own "ids cited from claim
  cards / gates / disclaimers" contract.
- **`contaminated_concept_table.json`** — generalizes the information-discrete-math
  contaminated-concept-table *pattern* (phrase → what it smuggles → disciplined replacement) to
  glosa's own domain: knowledge-legitimacy phrasing rather than continuum-math phrasing. Covers the
  8 phrases named in the task (`consensus`, `obvious`, `well known`, `proven`, `validated by
  experts`, `peer reviewed therefore true`, `novel`, `first`) plus three more for completeness
  (`gold standard`, `best practice`, `settled science`). Pattern only — no private IDM text copied.
- **`independence_ladder.json`** — the I0-I5 rows from FOUNDATION §4.2 (chair ruling C1): each
  row's `definition`, `can_raise`, `cannot_raise`, `k_ceiling`, `mc_ordinal`. `mc_ordinal` is a
  **derived/informational** field here, matching the source rule that the 0-5 ordinal is computed
  by the kernel only and is never a second schema-level field on the claim card itself — this
  table is data, not schema. Also carries the bounded I2+I4 exception, the local-model DVP rule,
  and the orthogonal (non-ladder) Founder-as-Approver role, all from the same section.

## Trigger mini-grammar

`disclaimer_catalogue.json.trigger` and `non_collapse_table.json`/other tables' condition-shaped
fields are written in one small, deliberately restricted grammar — not a full expression language,
just enough for a human or a validator to read a trigger and know exactly which schema field(s) to
check:

| Form | Meaning |
|---|---|
| `ALWAYS` | Fires on every claim card / every public surface, unconditionally. |
| `<path> <op> <value>` | A direct field comparison, e.g. `claim_card.scope.generalization_claimed != "none"`. `<path>` is a dotted path into a schema field; `<op>` is one of `==`, `!=`, `<`, `<=`, `>`, `>=`, `IN`, `NOT IN`. |
| `EXISTS(<path>)` | The path resolves to a non-null / non-empty value. |
| `LEN(<path>) <op> <n>` | Cardinality check on an array field. |
| `ANY(<path> <cond>)` / `ALL(<path> <cond>)` | Quantifies `<cond>` over every element of an array field at `<path>`. |
| `MAX(<path>)` | The maximum value of an ordinal field across an array (used for independence-class ladders, which sort I0 < I1 < ... < I5). |
| `COUNT(DISTINCT <path>)` | Distinct-value count across an array field. |
| `AND` / `OR` / `NOT` | Standard boolean combinators between the forms above. |
| `TEXT_CONTAINS_ANY({...})` | A prose-scan check over the rendered public text (paper/README/etc.), not a schema field — used only where the disclaimer is about *language actually used*, not a structured field. |
| `HEURISTIC(<description>)` | Marks a trigger that is **not** mechanically computable from a schema field — it requires a human or reviewer judgment call, named in plain language. A validator can flag `HEURISTIC(...)` triggers for manual review but cannot auto-fire them. |

No trigger in these tables invents a second name for a field that already has a home in
`schema/*.schema.json` — where a trigger needs a value not yet in any schema (e.g. a "content
domain" tag for `D-NOT-DIAGNOSTIC`), it is marked `HEURISTIC(...)` rather than silently minting a
new field here.

## Validation

Every file in this directory parses as JSON (`python3 -m json.tool <file>` — run and confirmed
clean at generation time, 2026-09-04). This is a **format** check only (NC-07, Conformance ≠
Truth) — it confirms the file is syntactically valid, not that its content is correct; content
correctness is Dr-tier, specified but independently unreviewed, same as every other file here,
until an I3+ or I4/I5 route checks it (see `independence_ladder.json`).

## One-fact-one-home cross-references

- Disclaimer ids are defined once, in `disclaimer_catalogue.json` — genre rows and NC rows
  *cite* an id by string, they never restate its wording.
- NC ids are defined once, in `non_collapse_table.json` — the disclaimer catalogue and
  contaminated-concept table cite an NC id by string in their own `nc_ref`/`enforced_by` fields
  rather than restating the pair.
- Independence-class values (`I0`..`I5`) are defined once, in `independence_ladder.json` — every
  other table treats the six-value ladder as a closed, ordered enum and never redefines its
  meaning locally.
