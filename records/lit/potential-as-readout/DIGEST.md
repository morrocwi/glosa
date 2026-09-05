# DIGEST -- potential-as-readout (POT1-integrate)

Task: POT1-integrate. Scope actually owned by this pass: `claims/*.yaml` (reconcile
`five_questions.tested.evidence_relations[].citation_ref` from PLACEHOLDER ids to real,
existing citation card ids only) and this file. Everything else in the three claim
cards -- statements, non_claims, falsifier text, dissent_records, disclaimers -- was
left untouched, per the task's own "keep everything else" instruction. That has one
side effect flagged below (see "Known inconsistency left in place").

Tier on every verdict below: `finite_diagnostic` (mechanical script output, read
directly, this session) unless marked `Dr` (a sketch/judgment call) or `Open`
(genuinely unresolved). Comparison vocabulary only: same/different/cited, never
novel/first/prior art (glosa gate rule 6). AI (this session) drafted this digest;
the founder alone signs claims (glosa gate rule 5, rule 9 -- no AI/vendor attribution).

## 1. Citation cards that actually exist, per hypothesis

| Hyp | citation cards found | status (all) | independence_class |
|---|---|---|---|
| H1 | 6 | METADATA_OK (none VERIFIED) | I1 (same-session; I3 cross-vendor attempt for h1/h3 failed on codex quota, honestly reverted per h1/h3 worker's own report) |
| H2 | 10 | METADATA_OK (none VERIFIED) | I3 (cross-vendor route:codex actually ran for h2; several returned `claim_match_verified: false`) |
| H3 | 7 (+1 non-literature fixture evidence item, not a citation card) | METADATA_OK (none VERIFIED) | I1 |

**None of the 23 citation cards across H1/H2/H3 carry `status: VERIFIED`** (VERIFIED
requires `metadata_verified: true` AND `claim_match_verified: true`, per
`schema/citation_card.schema.json`'s conditional). H2's cards are additionally
honest about a real, executed I3 cross-vendor disagreement (`claim_match_verified:
false` on several), not a placeholder or a script failure.

## 2. Claim cards reconciled (evidence_relations only)

### GLOSA-CC-20260905-0301 (H1 -- witnessed set)
- 3 PLACEHOLDER ids (`cite-potential-h1-001..003`) replaced with the 6 real H1
  citation cards.
- Bearing (mapped from each source dialogue-table row's own `stance`: YES->SUPPORTS,
  NO->CHALLENGES): **3 SUPPORTS** (Aristotle Metaphysics Theta; Chaiklin 2003/
  Vygotsky ZPD; Vygotsky 1978 via Chaiklin) / **3 CHALLENGES** (Robeyns 2017;
  Nussbaum 2011; Sen 1999 via Nussbaum) -- genuinely mixed, not forced.
- `./cli/glosa claim validate` (with `--citation-cards`): **FAIL** -- `rule12b
  D-LENS-UNCITED`: the card's own `lens_translation.lens_ref` (Readout Universe DOI
  10.5281/zenodo.21529456) has no VERIFIED citation card among the supplied set.
  This is a real, pre-existing gap (no citation card for the lens DOI exists in
  either hypothesis's `citations/` folder) -- out of this pass's ownership to fix
  (would require creating a new citation card, not reconciling an id), reported as
  a hard release-gate block, not worked around.

### GLOSA-CC-20260905-0302 (H2 -- two-layer agency)
- 3 PLACEHOLDER ids replaced with all 10 real H2 citation cards.
- Bearing: **all 10 UNRESOLVED**. This is a deliberate, honest deviation from the
  task brief's "mixed SUPPORTS/CHALLENGES" instruction: every one of H2's own
  dialogue-table rows records `stance: UNDETERMINED` (not a scaffolding artifact --
  each row's own `what_it_would_say_against_us` gives a real, specific counter-
  reading, e.g. Causal Agency's own Def.3 may already BE H2's layer-2 claim
  restated in different notation; Kabeer 1999's indivisibility argument may make
  H2's "separable layers" unmeasurable). Forcing these into SUPPORTS/CHALLENGES
  would fabricate a verdict the underlying literature review itself did not reach.
  `bearing: UNRESOLVED` is the schema's own correct value for this state
  (`schema/common.defs.json` bearing enum: SUPPORTS/CHALLENGES/NEUTRAL/UNRESOLVED).
- `./cli/glosa claim validate` (with `--citation-cards`): **FAIL** -- same
  `rule12b D-LENS-UNCITED` gap as H1 (no VERIFIED lens citation card).

### GLOSA-CC-20260905-0303 (H3 -- pseudo-peace numerical signature)
- Kept the one real fixture evidence_relation (`fixture-nogo-2node-run-001`)
  unchanged, per "keep everything else". Replaced 2 PLACEHOLDER literature ids
  with all 7 real H3 citation cards.
- Bearing: **6 SUPPORTS** (Galtung 1969 x2, Galtung 1990, Farmer 2004, Pettit,
  Satha-Anand 2021) / **1 NEUTRAL** (Csaky 2026 -- a formal agency-theory paper the
  lit worker itself flagged as evidentially weak for a peace/violence hypothesis;
  recorded NEUTRAL rather than forced into SUPPORTS or CHALLENGES). No CHALLENGES-
  bearing literature item exists for H3 -- genuinely absent from what the concurrent
  lit worker found, not omitted.
- `./cli/glosa claim validate` (with `--citation-cards`): **FAIL** -- same
  `rule12b D-LENS-UNCITED` gap, PLUS **`rule28 INFLATED-BEARING`** on the kept
  fixture evidence_relation: its `citation_ref` (`cite-potential-h3-fixture-001`)
  does not resolve to any known citation_card_id (it names simulation output, not a
  literature citation) and its `strength` field does not say `"context"`. This is a
  real, pre-existing structural gap in a field this pass was told to leave
  unchanged -- flagged here, not silently fixed and not silently ignored.

## 3. `./cli/glosa claim validate` verdicts (summary)

| Card | verdict (bare) | verdict (with `--citation-cards`) |
|---|---|---|
| 0301 (H1) | PASS_WITH_LIMITS | **FAIL** (D-LENS-UNCITED) |
| 0302 (H2) | PASS_WITH_LIMITS | **FAIL** (D-LENS-UNCITED) |
| 0303 (H3) | PASS_WITH_LIMITS | **FAIL** (D-LENS-UNCITED + INFLATED-BEARING) |

Reported as-run, not forced to PASS. The bare-path run only warns "not checked";
supplying the real citation cards (as this task's own reconciliation now makes
possible) surfaces the two real gates above.

## 4. `./cli/glosa release-gate`

`release-gate` takes a `release_manifest` FILE path (see
`schema/release_manifest.schema.json`, `projects/GLS-2026-001_.../release_manifest.json`
for a worked example), not a project directory. **No `release_manifest.json` exists
yet for `projects/GLS-2026-002_potential-as-readout/`.** Running it against the
project directory itself fails immediately (`IsADirectoryError`). Creating a release
manifest is outside this pass's ownership (claims + DIGEST.md only) -- reported as
NOT RUN, not forced to PASS.

`gate_verdict` for this task: **NOT RUN (no manifest exists to gate)**.

## 5. `sim/battery.py`

Executed once this session. `sim/battery_result.json` exists
(`~/ANSE.ASIA/cpg_research_journal/research/society-justice-peace/sim/battery_result.json`,
44,652 bytes, written 2026-09-05). `overall_verdict`:
```
all_N_all_seeds_pass_P1_P4: true
all_N_false_claim_refuted_every_seed: true
all_N_outside_hypothesis_correctly_flagged: true
tier: "finite_diagnostic (this randomly-instantiated finite spine + these 20 seeds
       per N only; not a theorem about societies)"
```
All P-controls pass with the failing controls refuted, exactly as designed under the
Fail-Able Gate Law. `battery_ok: true` at this tier, on this fixture family, with
this seed count only -- not a general theorem.

## 6. The 5 strongest CHALLENGES (exact passages)

1. **H1 / Nussbaum 2011, Creating Capabilities, Ch. 2, p.18** (CHALLENGES):
   capability opportunities "then may or may not exercise in action: the choice is
   theirs" -- an unexercised, never-witnessed option still counts toward justice
   assessment, the opposite polarity from H1's witnessing requirement.
2. **H1 / Robeyns 2017, Wellbeing, Freedom and Social Justice, Ch. 2** (CHALLENGES):
   capabilities are "a person's real freedoms or opportunities to achieve
   functionings" -- availability, not demonstrated achievement, is the criterion.
3. **H1 / Sen 1999 (quoted in Nussbaum 2011, p.20)** (CHALLENGES): capability is
   "the alternative combinations of functionings that are FEASIBLE for her to
   achieve" -- an analyst-modeled feasible set, not a record of what was executed.
4. **H2 / Causal Agency Def.3 (Zenodo 18897585, p.19)** (UNRESOLVED, counter-reading
   recorded against H2): "A system exhibits agency if its internal dynamics modify
   the constraint structure C ... to increase the expected persistence" -- H2's own
   dialogue-table row flags this may already BE H2's layer-2 claim, restated in
   different notation, adding nothing beyond naming a "recoverable gap".
5. **H2 / Kabeer 1999 abstract** (UNRESOLVED, counter-reading recorded against H2):
   resources, agency, and achievements are argued to be "indivisible in determining
   the meaning of an indicator" -- if the same indivisibility holds for H2's
   layer-1/layer-2 split, a recoverable-gap quantity requiring the layers to be
   SEPARABLE may not be measurable the way H2's framing needs.

(H3 has no CHALLENGES-bearing literature item at all in this pass's citation set --
its one real internal challenge is the fixture's own first-attempt failed control,
already disclosed in the card's `dissent_records`, not a new literature finding.)

## 7. What the paper (v2) must now say differently

1. **Cite the lens itself, or drop the lens-citation claim.** All three claim cards
   FAIL `rule12b D-LENS-UNCITED` because no citation card for
   `10.5281/zenodo.21529456` (Readout Universe) exists with `status: VERIFIED`
   among the hypothesis's own citation set. If the paper's v2 text asserts the lens
   is "cited" in the glosa sense, that assertion is currently false and must either
   be walked back or backed by a real VERIFIED citation card for that DOI.
2. **State H1's capability-theory contrast honestly as a genuine 3-3 split, not a
   one-sided confirmation.** Sen/Nussbaum/Robeyns's own formal definitions of
   capability/feasibility do NOT require witnessing -- they are, on their own terms,
   CHALLENGES to H1's witnessed-set reading, softened only by each source's own
   applied-practice caveat (quoted in the evidence notes above). The paper must not
   present the capability-theory literature as simply confirming the witness rule.
3. **Do not claim H2's layer-1/layer-2 distinction is portable or confirmed by the
   agency/empowerment/capability literature.** Every one of the 10 sources reviewed
   for H2 came back UNDETERMINED, several with a specific reason the two-layer split
   might be either (a) already present in the programme's own prior work under
   different notation (Causal Agency Def.3) or (b) not empirically separable at all
   (Kabeer 1999). v2 should state H2 as an open, not-yet-portable conjecture, not as
   a distinction the wider literature "already draws".
4. **Flag Csaky 2026 as a weak H3 citation, or drop it.** It is a formal
   agency-theory paper unrelated to peace/violence; keeping it as an H3 citation
   without the NEUTRAL/context-only caveat overstates H3's literature grounding.
5. **The fixture evidence_relation in H3 needs its own fix, separate from this
   pass.** `cite-potential-h3-fixture-001` does not resolve to a real citation
   card and its `strength` field is not marked `"context"` -- `rule28
   INFLATED-BEARING` catches this. A follow-up pass (in scope for whoever owns
   `claims/*.yaml`'s non-evidence-id fields, or a schema-aware fixture-evidence
   convention) should either create a minimal citation card for the fixture output
   or mark the relation's strength as `"context"` per the rule's own stated
   exception.
6. **No release manifest exists yet for this project.** v2 (or any public-facing
   next step) cannot go through `release-gate` until
   `projects/GLS-2026-002_potential-as-readout/release_manifest.json` is created,
   following the `GLS-2026-001` precedent, naming all 3 claim ids and all 23
   citation card ids, and until the D-LENS-UNCITED and INFLATED-BEARING findings
   above are actually resolved (not merely disclosed) -- a disclosed FAIL is not a
   release-ready state (glosa gate rule 8: no independent check -> no release).

## Numbers (for the calling task's JSON)

- Citation cards total across H1+H2+H3: **23** (6 + 10 + 7).
- Cards with `status: VERIFIED`: **0**. Cards with `status: METADATA_OK`: **23**.
- `claim validate` (bare path): 3/3 `PASS_WITH_LIMITS`.
- `claim validate` (with real `--citation-cards`): 3/3 **FAIL** (real gates
  surfaced by this pass's own reconciliation, not pre-existing false passes).
- `release-gate`: **NOT RUN** -- no release_manifest.json exists for this project.
- `sim/battery.py`: executed once, `battery_result.json` exists, all P-controls
  PASS, failing controls refuted, tier `finite_diagnostic`.
