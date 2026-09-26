# claim_evidence_matrix.csv — how to fill the Claim–Evidence–Theory matrix

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this file. The rule this template serves is narrated in
> `methodology/P26_claim_evidence_theory_matrix.md` (item c). Field names and allowed values are
> defined once, in `schema/claim_evidence_matrix_row.schema.json`; this file only explains how to
> fill the spreadsheet form of those rows.

## One row = one claim × one source use

A row joins three objects that already exist and adds only what none of them holds:

| Column | Home of the fact | Filled by |
|---|---|---|
| `claim_id`, `claim_label` | claim card (`claim_card.statement.text` is canonical; the label is a display copy that loses on any disagreement) | author |
| `source` | citation card (`citation_card.id`: passage, locator, `claim_match_verified`, `audit`) | author / AI drafts, checker verifies |
| `search_log_ref`, `rival_search_ref` | search log (`search_log.id`, with its support and challenge query families) | author / AI |
| `construct`, `source_type`, `construct_tier_role`, `supports`, `does_not_support`, `rival_evidence`, `used_in_section`, `mechanism_ref` | **this row, and nowhere else** | author; AI may draft, never sign |

## Rules while filling

1. Fill `does_not_support` on every row. If you cannot say what the source does not support, you
   have not read it closely enough to cite it.
2. `rival_evidence` may be empty only when `rival_search_ref` names the search whose challenge
   family came back empty. "Not found" is a fact about the search, not about the world (NC-27).
3. `supports` is never wider than the citation card's `exact_passage`. If the sentence in the
   draft says more, the claim-level audit (`citation_card.audit.status`) is `OVERREACH`.
4. For each distinct `construct`, the rows together should cover `originating_source`,
   `current_synthesis` and `critical_or_contradictory` (P26 item g). A missing tier is disclosed
   in the manuscript, not silently left out.
5. List fields (`rival_evidence`, `used_in_section`) use `;` as the separator inside one cell.
6. A row carries its own `tier`, normally `Dr` until the linked citation card's `audit.status` is
   `VERIFIED` by a checker who is not the maker.

## Validating a row

`cli/glosa check` validates JSON/YAML instances. To check CSV rows, convert each row to a JSON
object (split the list columns on `;`, keep empty cells as empty lists or `null`), add
`"$schema": "claim_evidence_matrix_row.schema.json"`, and run `./cli/glosa check <row>.json`.
A worked example is `schema/examples/claim_evidence_matrix_row.example.json`. No CSV-native
checker exists yet (open item in P26).
