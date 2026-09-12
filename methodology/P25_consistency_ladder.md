# P25 — Internal-Consistency Ladder: agreeing with itself is not the same axis as evidence against the world

tier: Dr (specified from the founder instruction and the design spec below; independently unreviewed)

> readout-not-truth applies to this card itself. Founder instruction (2026-09-08, verbatim):
> "ultracode ตั้งทีมชำระสมการด้วย เพื่อให้ telodo เป็นระบบสมการที่แข็งแกร่ง และแยกความแม่นยำในตัวเองอย่างน้อยที่สุดต้องสอดคล้อง
> ภายในในตัวเองอย่างเป็นระบบ" — set up an equation-clearing team so Toledo is a strong equation
> system, and separate its internal precision: at minimum it must be systematically
> self-consistent. Field-by-field reference: `toledo/docs/CONSISTENCY_SPEC_v0_1.md` (this card's
> own specification, the way `design/RESISTANCE_LADDER_v0_1.md` is `P23`'s). AI drafted this card.
> Comparison language is same/different/cited only.

## id

`P25`

## Rule

**Internal consistency (IC) is the registry agreeing with itself — never evidence against the
world.** It is a second, orthogonal axis to `P23`'s Resistance ladder R0–R6: an entry can be IC-3
and R0 (fully self-consistent, no evidence yet), or R4 and IC-0 (an external-oracle result exists,
but the entry's own fields still disagree with the schema or with its own Coq file). Neither ladder
collapses into the other and neither is ever rendered as one number (the same "never a single
number that hides a missing rung" design principle `P23` restates).

| Grade | Meaning | Who can award it |
|---|---|---|
| **IC-0** | Not checked, or the grader's record is older than the entry's last LINEAGE event. | nobody |
| **IC-1 shape-consistent** | Every mechanical structural cell passes: `schema`, `structure`, `tier` (mechanical half), `lineage` (mechanical half). | grader (a deterministic script) |
| **IC-2 text-consistent** | IC-1 plus every deterministic text cell passes: `symbols` (mechanical half), `coq` (mechanical half), `duplicates` (mechanical half, including the structural fingerprint; an `unparsed` entry cannot hold IC-2). | grader |
| **IC-3 reader-cleared** | IC-2 plus every reader cell of the entry cleared by an independent reader **and** countersigned by a second reader of a different role. | readers; the grader only verifies the clearance rows |
| **IC-F** (flag, not a rung) | Checked; at least one finding open. Grade stays at the highest rung whose cells all pass. | grader or reader |

Seven audit dimensions, one auditor each, each with mechanical (`M`) cells a script can check and
reader (`R`) cells a human/agent must judge: `schema` (documentation ⇄ data agreement), `structure`
(referential/structural integrity — parents resolve, children inverse, Coq file present, etc.),
`tier` (tier/status/coq_status honesty against a documented compatibility table), `symbols`
(spelling, sense, reserved-symbol kind/arity, dimensional consistency), `coq` (statement ⇄ Coq file
agreement), `duplicates` (hidden duplicates via a structural fingerprint — renaming/positive-scale/
constant-substitution equivalence, never auto-merged across roots), `lineage` (every declared edge's
derivation actually holds under a shape test). A `needs_reader` cell is an honest state — unchecked
by a reader, not a failing grade, and never silently promoted to `pass`.

Every finding a dimension raises carries `{id, codes, severity (block|warn|info), evidence
{command, observed, expected}, proposed_fix {class A|B|C|D}, mechanical: bool, status}` — a
deterministic id (`sha256` of the cell + codes + observed), so a fixed finding disappears from the
diff rather than needing manual closing. Fix class discipline: **A** (documentation/computed,
touches no content field), **B** (content-neutral edits — symbol-spelling unification, wrapper
header fixes, a SCHEMA-prescribed status move), **C** (identity/lineage — merges, new/retyped
edges), **D** (founder-only — the meaning of any ladder word, raising any tier, any root-layer
`parents` change). Exactly one script may touch `CANONICAL.json`/`LINEAGE.jsonl` for this pass, and
it applies only confirmed findings marked mechanical, never a class C/D finding without a ruling
reference. The grade itself is **never** written into the registry's own content files — it lives
in a sidecar the grader alone writes (`registry/consistency/<mangled code>.json` +
`INDEX.json`), same discipline `P23`'s `resistance` block and Toledo's `executable{}` block already
follow.

## Why / incident

The equation-clearing pass that produced this card's own spec ran seven independent audits over
Toledo's ~1,900-row registry on one day and found the registry disagreeing with its own documented
rules in every dimension at once: 767 root-layer parent edges with no documented edge-kind
vocabulary; a `derived_via` value (`refines`) used 29 times with no semantics defined anywhere; 277+
entries marked `coq_status: closed` with no matching PASS row in the last recorded verification
report; 125 Coq wrapper files whose own header comment named a different tier than the registry's
tier field for the same code; three exact-duplicate statement groups and a same-lemma renamed
across three different root files, none linked by a `same_object` edge; a build script that
computed every root row's rendered tier by a free-text heuristic instead of reading the row's own
already-normalised `tier` field when one existed — silently overriding 188 rows' worth of already-
correct data with a guess. None of this is evidence the registry's mathematics is wrong; it is
evidence the registry had never been checked for agreeing with **itself**, which is a precondition
for a reader trusting any single field of it. Toledo already had a strong evidence-against-the-
world axis (`P23`'s Resistance ladder) with no equivalent axis for internal agreement — this card
names that second axis so the two are never confused going forward.

## Who does what

Founder/human: rules on class-D findings (the meaning of a ladder word, any tier raise, any
root-layer edge change) via a named ruling id — the clearing team never accepts a class-D finding on
its own authority. AI/registrar: runs the seven dimension audits and the grader, applies only
confirmed mechanical findings through the one permitted fix script, and surfaces every remaining
finding to `ops/clearing/RULINGS_REQUESTED.md` rather than resolving it by inference.

## Disclaimers

IC audits **the registry's agreement with its own documented rules**, never the truth of the
underlying mathematics (same disclaimer shape as `P19`/`P23`) — an entry holding IC-3 still carries
exactly the tier/resistance rungs it held before; IC only says the fields describing that entry no
longer contradict each other or the schema. A `pass` on a mechanical cell is not a claim that the
statement is correct, only that the specific structural/referential/textual rule that cell checks
was not violated.

## NC pairs

Self-consistent ≠ true (IC and resistance are orthogonal axes) · `needs_reader` ≠ failing (unchecked
by a reader, not a finding) · `checked, finding open` (IC-F) ≠ `not checked` (IC-0) · mechanical
pass ≠ reader-cleared (IC-2 ceiling for a script; IC-3 needs a clearance row and a countersign from
a *different* role — same-role self-approval is not a check) · a fixed finding ≠ a ruled finding
(class A/B needs no ruling; class C/D needs a named ruling id before the fix script may touch
anything) · a stale clearance (its commit predates the entry's last `revised`/`split`/`merged`/
`status_changed` LINEAGE event) ≠ a current one — staleness drops the cell back to `needs_reader`,
the row is kept, never deleted.

## Not-do

- Do not collapse the seven-dimension table, or the IC-0..IC-3 ladder, to a single number anywhere
  — grader output, site page, `/v1/` JSON, or a summary sentence in a handoff.
- Do not merge IC with the Resistance ladder R0–R6 into one combined score.
- Do not let the one permitted fix script apply a class C/D finding without a named ruling
  reference, or touch any file outside `registry/CANONICAL.json`/`registry/LINEAGE.jsonl` (never
  `registry/genesis_root.json`, never a deposited source).
- Do not treat `needs_reader` as `pass`, or let a rung be earned by a cell that did not actually run
  (`not_checked`).
- Do not auto-merge a cross-root structural-fingerprint match — list it, route it to a reader/
  founder ruling instead.

## Tier

Dr — specified from the founder instruction and `toledo/docs/CONSISTENCY_SPEC_v0_1.md`;
independently unreviewed. Every count that spec itself cites was read by a command run while
drafting it (reported, not asserted from memory); the grader's own counts get a second-role
re-derivation before being cited in Toledo's README, per the spec's own maker-checker clause.
`toledo/tests/test_consistency.py` gives the executable grounding for the grader's own
rung-computation logic — run it and read the output.
