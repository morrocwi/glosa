# Architecture-First Comparative Review — Proposal v0.2

> tier: Dr (specified; reviewed during drafting — review notes are not part of this repository;
> not independently re-verified here; framework ratified, checker stays WARN-only). Readout-not-truth
> applies to this file.
> **Status: RATIFIED by the founder 2026-09-23 and integrated into the binding methodology this
> same pass.** v0.1's five open conflicts (§8) were resolutions (R1–R5) chosen on the founder's
> behalf under an explicit founder delegation ("choose for me — world-class but actually
> practical", 2026-09-23); the framework itself — architecture map as frozen L2 scope,
> node-grain `SUPPORTS/CHALLENGES/EXTENDS` relations, the WARN-only non-collapse guard, the
> mandatory CHALLENGES pass with `node_status`/`n_open_nodes`, and the six-criteria qualitative
> yardstick — was separately ratified by the founder the same day and is now integrated into:
> `design/S14_literature-review-system.md` §3.5 (binding summary), `methodology/
> P13_literature_review.md` (additive note), `plugins/glosa/skills/glosa-literature-review/
> SKILL.md` (drives the mode), `templates/knowledge/architecture_map.md` and
> `templates/knowledge/architecture_dialogue_table.md` (new), and an optional `node_refs:` /
> `node_status`+`n_open_nodes` addition to `templates/knowledge/neighbour_table.md` +
> `schema/neighbour_table_row.schema.json` and `templates/knowledge/litreview_manifest.yaml` +
> `schema/litreview_manifest.schema.json`. Tier stays honest: the *framework* is ratified and
> binding; `scripts/check_non_collapse.py` remains WARN-only per R4 — it was never proposed as an
> auto-failing gate and ratification does not change that.
>
> **Provenance:** the founder reviewed a general-purpose "world-class literature review" of one of
> their own works and withdrew its framing. That review had asked, component by component,
> whether each piece had already appeared elsewhere in the literature — reducing an architecture
> to a sum of prior publications and using words this repo's own gate already forbids (`novel`,
> `novelty`; AGENTS.md rule 6). The founder's
> correction, paraphrased (2026-09-23, no personal names beyond "the founder", no local paths,
> usernames, session ids, or private-repo names): the work's own architecture is primary; outside
> literature enters only as an *intellectual ally* that helps read, challenge, extend, or lend
> language to a part of the architecture — never as the owner of a mechanism the architecture
> already has. The founder asked that this principle be built as a **general** review framework
> for any work produced through glosa, not tied to the one work that triggered it.

---

## 1. Problem — why novelty-subtraction mis-measures architecture-type work

A "novelty-subtraction" review treats a work as `Architecture = Σ Literature_i` — it asks, for
every component, "who did this first / has this already been done", subtracts whatever prior
literature seems to cover, and reports what remains as the work's contribution. Three failure
modes follow directly, and this repo's own gate already forbids the vocabulary that names them
(`AGENTS.md` rule 6; `scripts/check_forbidden_words.sh`: `novel`, `novelty`, `unprecedented`,
`prior art`, `concession`, `seminal`, `pioneering`):

1. **It makes a literature strand the owner of a mechanism.** If tradition T already uses word W
   for something resembling one node of the architecture, novelty-subtraction concludes the node
   "is" T's concept, minus whatever the work adds on top. But owning a word is not owning a
   mechanism — a node can use the same word as an established tradition and still sit inside a
   different chain of transitions that tradition never specifies (`§3` below).
2. **It measures the wrong quantity.** Summing "components not already published elsewhere" scores
   how much of the work is unprecedented, not whether the *whole* — the specific arrangement,
   the transitions between nodes, what the arrangement as a system can do that no single node can
   do alone — coheres, covers its own claimed ground, resists collapsing into an existing single
   theory, composes with adjacent work, reaches further than any one input, and can be tested.
   Architectures are not judged well by summing their parts' publication histories.
3. **It forecloses dialogue with a subtraction instead of a conversation.** "X covered this first"
   ends the comparison at ownership. It never asks what X's own lens sees when pointed at the
   work's actual node, what X would still object to, or what the work's arrangement sees when it
   holds several such lenses at once that no single lens saw on its own.

This repo already rejects the priority/novelty framing at the *source* level
(`design/S13_neighbour-table.md`: same/different/cited only, never "we take/reuse/borrow" without an
explicit human instruction; `design/S14_literature-review-system.md` §3.4: a dialogue, never a
chronology or priority ranking). What S13/S14 do not yet fix is the **unit of comparison**: S13/S14
compare *the work as a whole* against one neighbour at a time. The founder's ruling asks for a
second, complementary unit — the work's own **architecture**, node by node, held up against a
**ring** of literature strands at once, each related to specific nodes by one of three fixed
relations, never by ownership.

---

## 2. Principle

**Architecture is primary. Literature strands are allied lenses, not owners.**

Schematic notation only, stated explicitly as **not an equation** — the expression below is a
compact notation for an English sentence, not a mathematical object, and any actual equation
would first need to be registered in the applicable public equation registry before it could be
written or cited as one; nothing here has gone through that process, so nothing here is cited or
treated as an equation:

```
NOT AN EQUATION — schematic notation only:
  Architecture ≠ Σ Literature_i
  Interpret(Work) = A_core | {L_1 .. L_n}
```

Read the second line as: "interpreting a work means reading its core architecture *through* a set
of literature strands used as lenses" — never as: "the work's meaning is computed as a sum, product,
or any formal function of literature terms." No literature strand may become the stated *source* of
a node's mechanism (`"A_core.node ← L_i"` is exactly the forbidden move — see §3d).

**Only three relations are permitted between a literature strand and an architecture node:**

- **SUPPORTS** — the strand, in its own terms, corroborates, replicates, or independently arrives
  at something compatible with what the node claims.
- **CHALLENGES** — the strand, in its own terms, gives a reason to doubt, narrow, or reject what
  the node claims, stated in the strand's own logic (not a straw-man of it).
- **EXTENDS** — the strand adds resolution, mechanism-level detail, an adjacent case, or a
  boundary condition the node does not itself specify, without contradicting it.

A strand may carry more than one relation to the same node (e.g. SUPPORTS the node's outer claim
while CHALLENGES one of its stated boundary conditions) — each relation gets its own row.

**Two questions replace "is it novel":**

- *What does this strand see when the architecture is placed in front of it* — what does it
  support, challenge, or extend?
- *What does the architecture see, holding several strands together, that no single strand sees
  on its own* — the "sees together vs. sees partially" synthesis (§3c).

**Yardstick — architectural contribution, not a novelty count.** Judge the whole by six qualitative
criteria (§3f), never by counting how many components have no prior instance anywhere.

---

## 3. Procedure — an extension of S14 L1–L6, not a parallel system

S14's six stages (`methodology/P13_literature_review.md`) already own: question framing (L1),
search protocol (L2), acquisition (L3), reading/extraction incl. `dialogue_table.md` (L4), citation
verification (L5), neighbour table + manifest freeze (L6). This proposal does not replace any of
that machinery. It adds one upstream artifact (the architecture map, §3a) and one per-node,
per-strand relation layer that sits **alongside** the existing per-source `dialogue_table.md` row,
reusing L4's citation-card discipline rather than inventing a second citation-verification path.

### 3a. Freeze the architecture map first (new, precedes L1)

Before any literature search begins, freeze a map of the work's own architecture: nodes (the
work's own mechanisms, stages, or constructs — named in the work's own vocabulary) and transitions
(how one node's output becomes another's input, in the work's own terms). This is the direct
analogue of S14 L1/L2's `frozen_scope` locked **before** `sources_found` is populated
(`P13_literature_review.md` L2 exit gate) — the architecture must be stated in its own right before
any external lens is pointed at it, so that literature search cannot retroactively reshape which
nodes the architecture is said to have. A map changed after search begins is a scope violation of
the same kind S14 already treats as a hard L2 exit-gate failure.

Minimal fields per node: `node_id`, `node_name` (work's own term), `mechanism` (one sentence, in
the work's own vocabulary), `upstream_nodes` (transitions in), `downstream_nodes` (transitions
out). No literature reference belongs on this map — it is the work's own object, frozen before
dialogue starts.

### 3b. Per-strand, per-node relation rows

For each literature strand admitted through S14 L2/L3 (same search-protocol and acquisition
discipline — a strand is a real, acquired, citation-carded source, never a memory-cited one), add
one row per `(node, strand, relation)` triple actually found, using the **same citation-card
backing** L4 already requires (`exact_passage`, `citation_card` id, `metadata_verified` +
`claim_match_verified`). Table template in §5.

Columns, per row: `node_id`, `strand` (citation), `relation` (`SUPPORTS | CHALLENGES | EXTENDS`),
`what the strand sees` (the strand's own framing, pointed at this node, in the strand's own terms
— structurally identical to `dialogue_table.md`'s "how it sees the problem" column, applied at
node grain instead of whole-hypothesis grain), `what the strand does not see` (what the node's
architecture specifies that this strand's own method/scope cannot reach — the node-level analogue
of "what it assumes"), `citation_card`, `verified`.

### 3c. "Sees together / sees partially" synthesis

After every node has its relation rows (or is honestly marked `no strand found` — an empty ring
around a node is disclosed, not hidden), write one synthesis sentence per node: what the
architecture's own arrangement of this node inside the whole system reveals that no single strand,
read alone, reveals — and, symmetrically, what any one strand still sees that the others miss (this
is the genuine content of "each strand sees only partially"). This is a **qualitative synthesis
statement**, not a score, and it must name which strands it is drawing the partial/together
contrast from — never asserted as an unattributed claim.

### 3d. Non-collapse guard (gate) <!-- non-collapse:meta -->

**A row or sentence anywhere in this review that makes a strand the owner or source of a node's
mechanism is a finding to be read and disposed of by a human** — v0.2/R4 (§8): unlike
`scripts/check_forbidden_words.sh`'s hard, auto-failing gate on banned vocabulary, this is
deliberately WARN-only, never an auto-fail, per the founder's delegated resolution.
`scripts/check_non_collapse.py` (built by this v0.2 pass, §8 R4) flags candidate constructions of the shape
`<Architecture node> ← <Literature strand>` or `<node> is <strand>'s concept`, alongside the
existing forbidden-word list, for human review — never auto-failing on its own.

| Forbidden phrasing (ownership move) | Correct phrasing (ally move) |
|---|---|
| "The work's semantic-transformation node is Controlled Semantic Cognition." | "CSC gives detailed representation/control mechanisms inside semantic cognition; the work's architecture places semantic transformation inside a longer chain of stages that CSC does not itself specify. CSC is used here as an ally to elaborate some transitions, without reducing the node to CSC." |
| "The work's meaning-node comes from Derrida." | "The work's meaning-node stands in critical dialogue with Derrida — Derrida CHALLENGES the node's assumption of stable reference; the node's own architecture answers by [X], which is not itself a Derridean move." |
| "Since Capability Approach already has 'capability', this node isn't new." | "Capability Approach elaborates one input condition of this node in detail (EXTENDS); the architecture connects that condition to [upstream/downstream nodes] Capability Approach's own framework does not address." |
| "X already did this, so we retreat / must shift the claim elsewhere." | "X SUPPORTS / CHALLENGES / EXTENDS this specific node; the node's claim stands as stated, refined by what X adds, unless X's CHALLENGES row is actually unanswered (§3e)." |

A strand may be cited as the historical or terminological origin of a *word* the work also uses —
that is a factual, citable statement (same/different/cited, per S13) — but it must never be written
as if the strand supplied the *mechanism*, i.e. the node's actual chain of transitions in the
architecture map (§3a). "Same word, different chain" is not a defect to fix; it is a fact to state
plainly, as in the examples above.

### 3e. Mandatory CHALLENGES pass

Carrying S14's existing rule forward at node grain: a review whose every populated relation is
SUPPORTS, with no CHALLENGES row anywhere and no disclosed attempt to search for one, is a flag —
the direct analogue of S14's `D-LIT-CONCENTRATED` condition ("every populated row's stance is YES
... with no attempt to search a challenge family", `templates/knowledge/dialogue_table.md`
"Forbidden in this table"). Allies are not cheerleaders by default; a search for a strand that
would CHALLENGE each node is a required step, and its absence — or its honest zero-result outcome —
must be disclosed, not silently omitted.

### 3f. Six-criteria yardstick (qualitative rubric, not a sum)

Judge the architecture, holding all relation rows together, against six criteria. **Each is a
qualitative test question, answered in prose with the specific rows that ground the answer — never
summed into a single score, and never used to declare "N unprecedented components" as the
verdict.**

| Criterion | Test question |
|---|---|
| Coherence | Do the nodes and transitions fit together as one system without an internal contradiction the relation rows expose? |
| Coverage | Does the architecture's own claimed ground actually get addressed by its nodes, or are there gaps a CHALLENGES/EXTENDS row reveals? |
| Non-collapse | Can the architecture be fully reduced to any single literature strand without loss — or does at least one node do something no single strand's own framework does? |
| Composability | Do the nodes connect to each other (and, where relevant, to allied strands' own frameworks) without requiring an unstated bridge? |
| Explanatory reach | What does the arrangement explain, together, that the individual strands do not explain on their own (the §3c synthesis, restated as a yardstick question)? |
| Testability | For each node with a real claim attached, is there a stated falsifier — something a CHALLENGES row, or a future one, could actually defeat? |

---

## 4. Mapping the three relations onto S14's existing `agrees/disagrees/undetermined` vocabulary

This is the central compatibility question and is answered here explicitly, not left implicit,
per this proposal's instruction to map onto existing fields wherever possible rather than
duplicate them.

- **These are not the same field at the same grain, and this proposal does not merge them.** S14's
  `dialogue_table.md` records one stance **per source, per whole hypothesis**
  (`agrees with H | disagrees with H | ORTHOGONAL | UNDETERMINED`). This proposal's relation rows record a relation
  **per source, per architecture node** — a finer grain, since one hypothesis/work typically
  contains several nodes, and one strand can SUPPORT one node while CHALLENGING another.
- **Partial semantic overlap, stated plainly:**
  - `SUPPORTS` ≈ `agrees with H = YES`, narrowed to one node instead of the whole hypothesis.
  - `CHALLENGES` ≈ `disagrees with H = YES`, and reuses the *existing* "what it would say against
    us" column directly — no new field is needed for a challenge's content, only the node-level
    address for which claim it challenges.
  - `EXTENDS` has **no equivalent in S14's four-value stance enum**
    (`YES|NO|ORTHOGONAL|UNDETERMINED`). This is the one genuine gap this proposal adds, not a relabeling of
    `ORTHOGONAL` — `ORTHOGONAL` means the source neither supports nor challenges because it
    addresses a different question entirely (`templates/knowledge/dialogue_table.md`); `EXTENDS`
    means the strand *does* bear on the same node but adds detail/an adjacent case/a boundary
    condition without contradicting it. Collapsing EXTENDS into ORTHOGONAL would misclassify every
    ally-elaboration case the founder's ruling is specifically about (CSC on semantic cognition,
    Capability Approach on the capability node).
  - `UNDETERMINED` carries over unchanged at node grain (a row not yet read to this depth, or
    ambiguous) — this proposal adds no new value here.
- **Resolved by R1 (§8):** reuse `dialogue_table.md`'s existing
  `defeater_class`/`legitimate_defeater`/`citation_card`/`verified` columns unchanged on the new
  node-relation rows (they are already source-grain, not hypothesis-grain, so they transfer
  cleanly); add exactly one new enum value's worth of vocabulary (`EXTENDS`) rather than a new
  four-way system; keep the existing `agrees/disagrees/ORTHOGONAL/UNDETERMINED` table as the
  **whole-hypothesis** record it already is, and treat architecture-node rows as an **additive,
  finer-grained companion table** for reviews that name an explicit architecture map (§3a) — never
  a required replacement for hypotheses too small to have a multi-node architecture worth mapping.
  This is the option this proposal recommended in v0.1 (option (a) below); R1 chooses it, subject
  to the founder's separate ratification of the framework as a whole (§8's "what ratification
  would change" list is unaffected — S14's own files are still untouched by this proposal itself).

---

## 5. Proposed table template

### 5.1 Architecture map (frozen before search, §3a)

| node_id | node_name | mechanism (one sentence, work's own terms) | upstream_nodes | downstream_nodes |
|---|---|---|---|---|
|  |  |  |  |  |

### 5.2 Architecture × literature dialogue (per node, per strand)

| node_id | strand (citation) | relation | what the strand sees | what the strand does not see | citation_card | verified |
|---|---|---|---|---|---|---|
|  |  | SUPPORTS \| CHALLENGES \| EXTENDS |  |  |  |  |

### 5.3 Per-node synthesis (§3c)

| node_id | strands drawn on | what the architecture sees together | what each strand still sees alone |
|---|---|---|---|
|  |  |  |  |

### 5.4 Six-criteria yardstick (§3f) — prose per criterion, not a score

- Coherence:
- Coverage:
- Non-collapse:
- Composability:
- Explanatory reach:
- Testability:

---

## 6. Forbidden phrases and allowed rewrites <!-- non-collapse:meta -->

| Forbidden | Why | Allowed rewrite |
|---|---|---|
| "not novel" / "no novelty" | Already banned repo-wide (`AGENTS.md` rule 6, `check_forbidden_words.sh`) | State the specific relation: "SUPPORTS/CHALLENGES/EXTENDS node N" |
| "novelty constraint" | Frames the review as a subtraction target | "architectural-contribution question" (§3f) |
| "X already did this" | Ownership move, forecloses dialogue | "X SUPPORTS/EXTENDS node N by [specific mechanism]; the architecture places N in a chain X's framework does not itself specify" |
| "must shift novelty [elsewhere]" | Assumes novelty is the yardstick and something must retreat from it | "node N's claim stands, refined/challenged by X's row; if X's CHALLENGES row is unanswered, that is stated as an open gap (§3e), not a retreat" |
| "reduces to X" | Exactly the collapse §3d's gate forbids | "node N and X's framework are same/different in [specific respect]; N does not reduce to X because [specific transition/mechanism X's framework does not cover]" |
| "[Node] ← [theory]" / "[node] is [strand]'s concept" | Makes the strand the owner of the mechanism (§3d) | Use the ally-phrasing template in §3d's right-hand column |
| "seminal" / "pioneering" / "prior art" | Already banned repo-wide | Neutral citation only (same/different/cited, per S13) |

---

## 7. Worked example (generic, neutral architecture — not any founder-private work) <!-- non-collapse:meta -->

**Architecture map (fictional, illustrative only):** a toy "Feedback Learning Loop" (FLL) with
three nodes: `N1 Observe` (raw signal capture) → `N2 Adjust` (a rule updates internal state from
the observed signal) → `N3 Act` (the updated state selects the next action, feeding back into
`N1`).

| node_id | node_name | mechanism | upstream | downstream |
|---|---|---|---|---|
| N1 | Observe | Captures a raw signal from the environment before any interpretation is applied | N3 | N2 |
| N2 | Adjust | A fixed update rule maps the observed signal plus current internal state to a new internal state | N1 | N3 |
| N3 | Act | The updated internal state selects the next action, which changes what N1 will observe next | N2 | N1 |

| node_id | strand | relation | what the strand sees | what the strand does not see | citation_card | verified |
|---|---|---|---|---|---|---|
| N2 | Classical control theory (PID-controller literature) | SUPPORTS | A proportional-integral-derivative controller is a mature, well-studied instance of exactly this update-rule pattern: error signal in, corrected control variable out | PID literature treats the update rule as fixed and hand-tuned; it does not address a `N2` that itself changes its own update rule over time | (illustrative — not a real citation) | — |
| N2 | Online/adaptive-learning-rate literature (e.g. stochastic-gradient adaptive-rate methods) | EXTENDS | Gives a detailed mechanism for how an update rule's own parameters can themselves change over time in response to observed signal statistics | Does not address the `N3`→`N1` action-changes-observation feedback path — it is typically studied with a fixed, externally supplied data stream, not a closed action loop | (illustrative) | — |
| N1–N3 loop | Situated-cognition literature (embodied/enactive cognition) | CHALLENGES | Argues that splitting "observe" from "act" as two distinct stages misdescribes real embodied systems, where perception and action are constitutively coupled, not sequential stages | Does not offer a formal update-rule mechanism comparable to `N2`'s — its critique is at the level of framing, not an alternative mechanism for the same job | (illustrative) | — |

**Synthesis (N2):** PID theory and adaptive-learning-rate theory each supply a different, real
piece of N2's mechanism — a stable baseline update law and a way that law's own parameters can
move — but neither, alone, is written for a closed loop where N3's action changes what N1 next
observes. The architecture's contribution at N2 is exactly that closure: an update rule whose
adaptation is read as an internal readout of the whole loop's own history, not an externally
supplied training signal. PID theory alone would not predict this closure; adaptive-rate theory
alone would not predict it either — together, read through the architecture's own transitions,
the loop's self-referential update behavior becomes visible, which is what "sees together, not
partially" means here.

**Non-collapse check:** it would be a gate failure to write "N2 is a PID controller" (ownership
move) or "N2 is just online learning" (ownership move). The correct phrasing: "N2's update
mechanism is SUPPORTED by classical control theory's baseline stability results and EXTENDED by
adaptive-learning-rate theory's parameter-adaptation mechanism; the architecture's own contribution
is placing that update inside a closed observe-adjust-act loop neither tradition specifies on its
own."

**CHALLENGES pass:** the situated-cognition row above is the required challenge-family result —
found by deliberately searching for a framework that objects to the loop's own staging, not only
frameworks that supply mechanism detail. The architecture's answer to it (not shown in full here,
since this is an illustrative sketch, not a real review) would need to state whether `N1`/`N3`'s
formal separation is defended as a modeling convenience or revised in response.

---

## 8. Resolutions

v0.1 listed five open conflicts for the founder to rule on. The founder delegated the choice
("choose for me — world-class but actually practical", 2026-09-23); the choice below was made
on the founder's behalf. These are choices among the options v0.1 already laid out — they resolve how the
framework would work, not whether it is ratified into S14/P13/SKILL.md, which stays a separate,
still-pending founder decision (see "What ratification would change" below, unchanged by this
section).

**R1 — EXTENDS (was open conflict 1).** Do NOT alter S14's hypothesis-grain
`agrees/disagrees/undetermined` enum. Add a separate node-grain field
`relation ∈ {SUPPORTS, CHALLENGES, EXTENDS}`, used only in the architecture×literature table (§5.2), never merged into
`dialogue_table.md`'s own whole-hypothesis stance column. Cross-grain reading, when a node-relation
row needs to be read against the hypothesis-grain enum: SUPPORTS → agrees, CHALLENGES → disagrees,
EXTENDS → no hypothesis-grain analogue (recorded as such — "no S14 stance analogue" — never coerced
to ORTHOGONAL, which means something different: the source addresses a different question
entirely, not that it elaborates the same one). This is option (a) from §4/open-conflict-1;
option (b) (extending `dialogue_table.md`'s own enum workspace-wide) is rejected as unnecessarily
invasive to a file this proposal is explicitly not touching.

**R2 — Grain (was open conflict 2).** An architecture review is **one LRS run** whose frozen scope
(S14 L2) IS the frozen architecture map (§3a) — the map is not a second run-unit alongside the
hypothesis, it *is* how the hypothesis's scope gets frozen for an architecture-shaped hypothesis.
Each node is a named sub-question inside that one run. Exit gates (S14 L1–L6) are evaluated
per-node first (did this node's own dialogue rows pass citation verification, etc.), then rolled
up to the run level the way L6's manifest already aggregates its sources today. A node-level table
is required whenever a hypothesis's own architecture map (§3a) names more than one node; a
single-claim hypothesis with no multi-node architecture worth mapping skips §3a/§5.1–5.2 entirely
and uses S14/P13 unchanged, per §4's existing "never a required replacement" language.

**R3 — Unanswered CHALLENGES (was open conflict 3).** Carrying glosa's own Resolve-or-Declare
discipline down to node grain: a node with an unanswered CHALLENGES row is marked
`node_status: OPEN` with a stated reason (the node's own architecture has not yet answered the
challenge). The run-level `litreview_manifest.yaml` may still freeze with open nodes present — this
is not a whole-run fail — but the manifest's run-level status reports `n_open_nodes` (count) so an
open node is never silently absorbed into an otherwise-green manifest, and an OPEN node's claim may
not be cited as settled by anything downstream until it is closed. This does not weaken S14's
existing `D-LIT-CONCENTRATED` flag (§3e): zero CHALLENGES rows anywhere, after a real search for a
challenging strand was actually attempted and disclosed, still raises that flag regardless of how
many nodes are OPEN or CLOSED.

**R4 — Non-collapse check (was open conflict 4).** Built as `scripts/check_non_collapse.py`: a
lightweight, stdlib-only, WARN-only script that flags candidate ownership/subtraction phrasing
(`<node> ← <strand>` shapes and the EN/TH phrase families listed in §6's forbidden-phrases table,
among others) for a **human** to read and dispose of. It never auto-fails a gate — unlike
`scripts/check_forbidden_words.sh`'s hard fail on an unallowlisted hit, this checker only surfaces
candidates; the human's disposition (kept as a real finding and reworded, or marked a
false-positive) is recorded wherever that human records it, not by the script itself. An opt-in
`--strict` flag exists for a future CI lane that wants a hard gate, but nothing in this proposal
wires it in by default.

**R5 — S13 link (was open conflict 5).** Each whole-work neighbour row in `S13_neighbour-table.md`
may carry an optional `node_refs:` field pointing at zero or more node-grain rows (§5.2) that bear
on that neighbour. S13 stays exactly what it already is — the **whole-work** comparison
(same/different/cited) — and no content is duplicated between the two tables; `node_refs:` is a
pointer, never a copy of a node-relation row's own fields. This is additive and optional: a
neighbour row with no matching node-level table (a single-claim hypothesis, R2) simply carries no
`node_refs:`.

**What ratification changed (done, 2026-09-23, this same pass):**
- `design/S14_literature-review-system.md` — new §3.5 describing the architecture-map freeze step
  and the node-relation companion table, cross-referencing this proposal.
- `methodology/P13_literature_review.md` — an additive note in the L1–L6 text naming the optional
  architecture-map prerequisite.
- `plugins/glosa/skills/glosa-literature-review/SKILL.md` — a full "Architecture-first comparative
  review" section (when to use, steps, the three relations, forbidden phrasings → rewrites, the
  `check_non_collapse.py` run before publish), triggers added to its `description`, and its "New
  this pass" note updated from pending to ratified.
- `templates/knowledge/architecture_map.md` and `templates/knowledge/architecture_dialogue_table.md`
  — the two new template files for §5.1/§5.2's tables (kept as separate markdown templates, not
  merged into `dialogue_table.md`, matching this repo's one-fact-one-home convention for a
  genuinely different grain of table).
- `templates/knowledge/neighbour_table.md` and `schema/neighbour_table_row.schema.json` — per R5,
  an optional `node_refs:` field on S13's neighbour-table row, wiring it to the node-relation table.
- `templates/knowledge/litreview_manifest.yaml` and `schema/litreview_manifest.schema.json` — per
  R3, an optional `architecture_review` block carrying `node_status` per node and a run-level
  `n_open_nodes` count, absent/empty on an ordinary single-claim run.

`scripts/check_non_collapse.py` (R4) remains what it always was: a standalone, WARN-only script,
not a hard gate — this pass did not change its behavior, only added the binding-methodology text
that points to it.

---

## 9. What this proposal explicitly did and did not do

**Status as of 2026-09-23 (integration pass):** the framework is now ratified and integrated —
§8's "What ratification changed" list above states exactly which files this pass touched. What
follows is this section's original scope statement, corrected in place rather than silently
rewritten, since it described a prior, pre-ratification state:

- Originally: "does not touch any binding file." Corrected: this integration pass DOES touch
  `S14_literature-review-system.md` (§3.5), `P13_literature_review.md`, `plugins/glosa/skills/
  glosa-literature-review/SKILL.md`, `schema/neighbour_table_row.schema.json`,
  `schema/litreview_manifest.schema.json`, `templates/knowledge/neighbour_table.md`, and
  `templates/knowledge/litreview_manifest.yaml`, additively, per the ratified R1–R5 resolutions
  and §8's list. `S13_neighbour-table.md` itself remains untouched — only its sibling schema/
  template gained the optional `node_refs:` field per R5; S13's own text is unchanged.
- Kernel rules, CLI verbs, and validators wired into the binding methodology's own gate machinery
  remain out of scope for this pass — only `scripts/check_non_collapse.py` (R4, standalone,
  WARN-only, unchanged by this pass) exists as runnable code; no hard-gate check was added.
- Does not apply this framework to any real, in-progress review — §7's worked example is a
  deliberately neutral, fictional toy architecture, not any founder-private work; this remains
  true after integration.
- The five v0.1 open conflicts are resolved by delegation (§8, R1–R5) and the framework itself is
  now ratified into the binding methodology (S14/P13/SKILL.md/templates) — no part of this
  proposal's original scope remains pending.
