# Architecture x literature dialogue — node grain (S14 §3.5, architecture-first comparative review)
#
# Provenance: design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md §3b/§3c/§5.2-§5.3, ratified
# 2026-09-23. Optional, additive companion to dialogue_table.md for a hypothesis whose
# architecture_map.md (§ sibling template) names two or more nodes. Reuses the same citation-card
# backing L4 already requires (exact_passage, citation_card id, metadata_verified +
# claim_match_verified) — this table does not invent a second citation-verification path.
#
# ARCHITECTURE IS PRIMARY. Literature strands are allied lenses, never owners. A row that makes a
# strand the owner/source of a node's mechanism ("[node] is [strand]'s concept", "[node] <- [strand]")
# is a non-collapse violation (§ "Forbidden in this table" below) — run
# `python3 scripts/check_non_collapse.py <this file>` before publish (WARN-only; a human reads and
# disposes of every hit).

## Hypothesis / architecture this table belongs to
- hypothesis_id (claim_card.claim_id / r2_hypothesis_ref):
- architecture_map_ref (path to the frozen architecture_map.md):

## Relation rows (one per node x strand x relation triple actually found)

| node_id | strand (citation) | relation | what the strand sees | what the strand does not see | citation_card | verified |
|---|---|---|---|---|---|---|
|  |  | SUPPORTS \| CHALLENGES \| EXTENDS |  |  |  |  |

Column notes:
- **node_id** — must match a `node_id` already frozen on `architecture_map.md`; a row may never
  introduce a node not already on that map.
- **relation** — exactly one of `SUPPORTS | CHALLENGES | EXTENDS` per row. A strand may carry more
  than one relation to the same node (e.g. SUPPORTS the node's outer claim while CHALLENGES one of
  its stated boundary conditions) — each relation gets its own row.
  - **SUPPORTS** — the strand, in its own terms, corroborates, replicates, or independently
    arrives at something compatible with what the node claims.
  - **CHALLENGES** — the strand, in its own terms, gives a reason to doubt, narrow, or reject what
    the node claims, stated in the strand's own logic (not a straw-man of it).
  - **EXTENDS** — the strand adds resolution, mechanism-level detail, an adjacent case, or a
    boundary condition the node does not itself specify, without contradicting it. No
    hypothesis-grain analogue in `dialogue_table.md`'s `agrees/disagrees/orthogonal/undetermined`
    enum — never coerced to `orthogonal`, which means the strand addresses a different question
    entirely, not that it elaborates the same one.
- **what the strand sees** — the strand's own framing, pointed at this node, in the strand's own
  terms (structurally identical to `dialogue_table.md`'s "how it sees the problem" column, applied
  at node grain).
- **what the strand does not see** — what the node's architecture specifies that this strand's own
  method/scope cannot reach (node-level analogue of "what it assumes").
- **citation_card / verified** — same fields as `dialogue_table.md`; a stance may only be recorded
  once `claim_match_verified == true` on that card.

## Per-node synthesis (one sentence per node, after its relation rows are filled)

| node_id | strands drawn on | what the architecture sees together | what each strand still sees alone |
|---|---|---|---|
|  |  |  |  |

A node with no strand found is disclosed as `no strand found`, not omitted from this table.

## Six-criteria yardstick (prose per criterion, not a score)

- Coherence:
- Coverage:
- Non-collapse:
- Composability:
- Explanatory reach:
- Testability:

## Mandatory CHALLENGES pass

A search for a strand that would CHALLENGE each node is a required step; its absence, or its
honest zero-result outcome, must be disclosed, not silently omitted. A node whose every populated
relation is SUPPORTS with no disclosed challenge-family search is a flag (the node-grain analogue
of `dialogue_table.md`'s `D-LIT-CONCENTRATED` condition).

- node_status (per node with an unanswered CHALLENGES row): `OPEN`, with a stated reason — the
  node's own architecture has not yet answered the challenge. An OPEN node's claim may not be
  cited as settled by anything downstream until it is closed.
- n_open_nodes (run-level count, rolled up into `litreview_manifest.yaml`):

## Forbidden in this table

- A row or sentence anywhere that makes a strand the owner or source of a node's mechanism
  (`<node> <- <strand>` shapes, `"<node> is <strand>'s concept"`) — see
  `design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md` §3d/§6 for the full forbidden/rewrite table.
- Recording a `relation` for a node not already frozen on `architecture_map.md`.
- Recording SUPPORTS/CHALLENGES for a row whose `citation_card` is not `claim_match_verified`.
- Summing the six-criteria yardstick into a single score, or reporting it as a count of
  components with no prior instance found anywhere.
- Every populated relation in a node being SUPPORTS with no disclosed attempt to search for a
  CHALLENGES strand.
