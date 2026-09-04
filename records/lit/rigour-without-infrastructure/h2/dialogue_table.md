# Dialogue table — lit-review default output (S14, founder 35c, coordinator addition)
#
# The lit review is a CONVERSATION WITH THE PROBLEM, not a chronology or a priority ranking.
# Every source is placed by how it talks to OUR problem/hypothesis — never by who came first,
# never "seminal"/"pioneering". Date is metadata only (put it in a `date` column if wanted, but
# it must never set row order — order rows by relevance-to-H or leave unordered/alphabetical).
# One dialogue_table per hypothesis (one LRS run = one table). Rows feed neighbour_table.md and
# the litreview_manifest.yaml. Every row needs a citation_card id; a row for a NOT_FETCHED source
# is still legal (mark it honestly) but may not be used to claim the source "agrees" or
# "disagrees" — a stance can only be recorded once claim_match_verified is true.

## Hypothesis this table belongs to
- hypothesis_id (claim_card.claim_id / r2_hypothesis_ref): H2
- hypothesis_world (verbatim R2 text):
- falsifier:

## Table

| source | how it sees the problem | what it separates | what it assumes | agrees with H | disagrees with H | what it would say against us | citation_card | verified |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

Column notes:
- **how it sees the problem** — the source's own framing of the phenomenon, in the source's terms,
  not ours (this is where a genuinely different lens shows up, before we judge it).
- **what it separates** — the distinctions the source's own method licenses (its own Q2, applied to
  its own access source) — may be coarser or finer than ours; state which.
- **what it assumes** — the source's own unexamined premises, as best we can tell from the fetched
  text (never invented; "not determinable from fetched text" is a legal answer).
- **agrees with H / disagrees with H** — `YES | NO | ORTHOGONAL | UNDETERMINED` — orthogonal means
  the source neither supports nor challenges H (different question entirely); undetermined means
  the passage was ambiguous or not fully read (must not be silently rounded to a stance).
- **what it would say against us** — the source's strongest available objection to H, stated in
  its own logic, even if we think we can answer it (this is the Falsifier/Hostile-Reviewer move
  applied per-source, not just once for the whole hypothesis).
- **citation_card** — id of the `citation_card.yaml` this row rests on (§ mandatory, S8).
- **verified** — `metadata_verified` + `claim_match_verified` booleans from that card, copied here
  for at-a-glance reading; the card itself remains the one fact one home for the actual values.

## Forbidden in this table
- Ordering rows by publication date, "who came first," or foundational-rank language (see the priority-language list enforced by scripts/check_forbidden_words.sh).
- Writing a stance (agrees/disagrees) for a row whose citation_card is not `claim_match_verified`.
- Collapsing ORTHOGONAL into either agrees or disagrees to make the table look more decisive.
- A table where every populated row's stance is YES (agrees) with no ORTHOGONAL/UNDETERMINED and
  no attempt to search a challenge family (§2, search_log.yaml `queries.challenge`) — this is the
  bidirectional-search discipline applied at table level; flag with `D-LIT-CONCENTRATED` (stance
  dimension) if it happens honestly despite a real challenge search.
