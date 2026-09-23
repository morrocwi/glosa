# Architecture map — frozen before search (S14 §3.5, architecture-first comparative review)
#
# Provenance: design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md §3a/§5.1, ratified 2026-09-23.
# Optional, additive companion to L1/L2 for a hypothesis whose own work is an ARCHITECTURE —
# multiple named nodes (mechanisms/stages/constructs) with transitions between them — not a
# single-claim hypothesis. A single-claim hypothesis with nothing multi-node worth mapping skips
# this file entirely and uses L1-L6 unchanged.
#
# This map IS how L2's frozen_scope locks for an architecture-shaped hypothesis: freeze it BEFORE
# any literature search begins. A map changed after search begins is a scope violation of the same
# kind S14 already treats as a hard L2 exit-gate failure — literature search may never
# retroactively reshape which nodes the architecture is said to have.
#
# No literature reference belongs on this map. It is the work's own object, stated in its own
# vocabulary, before any external lens is pointed at it.

## Hypothesis / work this map belongs to
- hypothesis_id (claim_card.claim_id / r2_hypothesis_ref):
- frozen_at (date the map was locked, before search opened):

## Nodes

| node_id | node_name (work's own term) | mechanism (one sentence, work's own vocabulary) | upstream_nodes | downstream_nodes |
|---|---|---|---|---|
|  |  |  |  |  |

Column notes:
- **node_id** — a short stable id (e.g. `N1`, `N2`) referenced by
  `architecture_dialogue_table.md` rows and by `neighbour_table.md`'s optional `node_refs:` field.
- **node_name** — the work's own term for the mechanism/stage/construct, never a term borrowed
  from a literature strand to name the node.
- **mechanism** — one sentence, in the work's own vocabulary, stating what this node does.
- **upstream_nodes / downstream_nodes** — the transitions in/out, by `node_id`, in the work's own
  terms (how one node's output becomes another's input).

## Forbidden in this map

- Naming a node after a literature strand's own term ("the CSC node") before the work's own
  vocabulary has named it.
- Adding, removing, or renaming a node after literature search has opened (`frozen_at` set) — this
  is a scope violation; a genuine correction requires a new, dated version, not an in-place edit.
- Any literature citation on this map — citations belong only on
  `architecture_dialogue_table.md` rows, never here.
