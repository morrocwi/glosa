tier: Dr (specified; independently unreviewed)

# Cases

Worked examples that demonstrate the spine (`design/FOUNDATION_v0.5.md` §2) and the claim card
(§3) end to end, on a small, concrete problem — so a reader can see every artifact and gate produce
a real, filled row rather than reading the schema in the abstract. A case file is a
**demonstration**, not a claim about the world: everything inside one, unless the case's own text
says otherwise, sits at `tier: Dr`, `k_state: K0` — it shows the *shape* of the round trip, not a
completed, checked result.

## Index

| File | Demonstrates |
|---|---|
| `worked-example-cat.md` | The full round trip: Blackbox Note → lens-in → analysis (rivals in one fiber, augmentation types, identification ladder, medical-rival human handoff) → lens-out (hypotheses + falsifiers) → LRS stub → hypothesis selection (human) → genre route → stub + full claim card → disclaimers → independence ceiling under the AI assistant-only / +Gemini / +external-human. Source: `the founder session record (local handoff, not public; public trace: Blackbox Log, concept DOI 10.5281/zenodo.22302518)` §6, request 26 (founder-supplied). |

## What a case file must show, if another one is added

Per the pattern this first case sets:
1. **Step 0 is always the Blackbox Note** — the raw human line(s) that started the problem,
   verbatim, before any formalization. A case with no Blackbox Note line has skipped the spine's
   own starting point.
2. **Every step is tagged `produced_by: human | ai | joint`** (request 24) — a case that only
   states this once, at the top, has not actually shown the co-production split the methodology
   claims to make visible.
3. **The genre-routing procedure (§6.3b) is actually run against the claim card's own fields**, not
   asserted from an earlier informal description — if the computed result differs from what was
   expected going in, the case says so honestly (see `worked-example-cat.md`'s "Honest edges"
   section) rather than quietly matching the expected answer.
4. **The independence ceiling is stated as a table across at least two route counts** (e.g. AI-only
   vs +a second vendor vs +an external human), per §4.2 — a case that reports only one ceiling
   value has not demonstrated the ladder, only one point on it.
5. **A closing "Honest edges" section** names what in the case is a planned design rather than a
   completed check, and any place where the case's own procedure produced a different answer than
   the case's own informal framing assumed going in.

## Relationship to `incidents/`

`incidents/` records failures that already happened and the rules they produced. `cases/` records a
worked-forward demonstration of the methodology on a problem, whether or not anything went wrong.
A case may cite an incident file (e.g. a case demonstrating the citation-integrity subsystem might
point at `incidents/2026-07-31_toon-format-accuracy-overclaim.md` as the reason a particular check
exists) but the two directories are not interchangeable: an incident is evidence for a rule, a case
is a demonstration of the rule being followed.
