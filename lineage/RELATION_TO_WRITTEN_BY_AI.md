# Relation to "Written by AI. Still True." (Yaoharee Lahtee, Aug 2026)

> **Tier: Dr.** Single reading, not independently cross-checked (I0/I1 only). Source: `sources/
> WRITTEN_BY_AI_STILL_TRUE_v6.txt` / `.pdf`; Zenodo DOI `10.5281/zenodo.22301202` (concept DOI
> `10.5281/zenodo.22301201`), CC BY 4.0, deposited 2026-09-04. Citation card:
> `sources/citation_cards/CIT-written-by-ai-v6.yaml`. Full expansion of each row:
> `design/S15_pillars-ontology-epistemology-methodology.md`. Non-collapse rows drawn from this
> paper: `NC-65`..`NC-73`, `design/S9_non-collapse-table.md`.

This paper is the founder's own general epistemology of AI-mediated knowledge production. glosa
cites it as a philosophical grounding text for mechanisms glosa already needed or was already
building (`FOUNDATION_v0.4.md`'s claim card, disclaimer catalogue, and independence ladder), and
in a small number of cases adds a mechanism the paper's vocabulary named more precisely than
glosa's prior schema did (marked `EXPAND` below). No mechanism in this ledger is claimed as
originating from this paper alone where an existing lineage (Readout Universe/Genesis, Standalone
Scholar, grr-epistemic-foundation, MIMCG) already supplied it — those rows are marked
`PRESERVE_FUNCTION` with the prior lineage noted, and the comparison is *same*, never *adopted
from*, per the founder's wording rule (HANDOFF §6 request 31i: "adopted" is used only when a human
explicitly instructed adoption of that specific thing from that specific source; no such
instruction exists for this paper as of this pass).

| Principle (paper) | Status | Where in glosa | What glosa does NOT take |
|---|---|---|---|
| Definition 1, pre-subjective constraint structure (lines 159–166) | `PRESERVE_FUNCTION` — same underlying realism as glosa's existing `tested.falsifier`/`scope` design, independently arrived at via Readout Universe/Genesis lineage, not this paper | `design/S15...` Pillar 1 §1.1; `tested.falsifier`, `scope.evidence_scope` | glosa does not adopt the paper's specific vocabulary ("pre-subjective constraint structure") as a schema field name; it names the same distinction using its own existing field names. |
| RA = OA(W;ΠA) ≠ W (lines 251–269) | `PRESERVE_FUNCTION` — same distinction as readout-not-truth, cited as *same*, lineage stays with Readout Universe/Genesis (`lens_used.display`) | `design/S15...` Pillar 1 §1.2; `NC-71`; `five_questions.seen` | glosa does not switch its `lens_used.display` attribution to this paper — the Lens Law and readout-not-truth remain attributed to Readout Universe/Genesis (Yaoharee Lahtee), per the existing `blackbox_note.yaml` block. This paper is cited *alongside*, in `lens_used.references`, not *instead of*. |
| Principle 1, Role Separation + Table 1's ten roles (lines 276–360) | `PRESERVE_FUNCTION` — every role maps onto an existing, distinct glosa field (see full crosswalk, S15 Pillar 2 §2.1) | `design/S15...` Pillar 2 §2.1 | glosa does not add a "Possession" or "Truth" field — the paper's own diagnosis is exactly why those two roles are deliberately absent from the schema. |
| Definition 2, Possession–Constitution Collapse; Definition 3, knower fetishism (lines 247–249, 540–544) | `PRESERVE_FUNCTION`, restated as glosa's own internal design diagnosis, not a claim about any named party | `design/S15...` Pillar 2 §2.2; `NC-65`; existing `NC-38`, `NC-58` | glosa does not name any specific person, tool, or institution as having committed this collapse — `feedback-no-negative-unverified-org-content` forbids an identified accusation without a verifiable source, and the paper itself argues in general philosophical terms, not about named parties. |
| Principle 2, Bridge Burden (lines 302–306) | `EXPAND` — genuine schema gap this pass identifies and patches | `design/S15...` Pillar 2 §2.3; `design/FOUNDATION_v0.5_PATCH.md` §3 (new `evidence_relation.channel` field) | glosa does not retroactively invalidate any existing `evidence_relations[]` entry written before this field existed — the patch is additive; a missing `channel` on a pre-existing entry is `Open`, not `FAIL`, until the schema version bumps and a migration pass runs. |
| Principle 3, No Bare Pedigree (lines 390–396) | `PRESERVE_FUNCTION` — the seven-element tuple already maps one-to-one onto existing `citation_card.yaml` fields | `design/S15...` Pillar 2 §2.3 crosswalk table | glosa does not rename any existing citation-card field to match the paper's exact tuple vocabulary — the mapping is stated as a crosswalk, not a schema change. |
| Principle 4, Provenance Relevance Constraint; Definition 4, Residual Provenance Effect (lines 567–603) | `EXPAND` — new `rpe_check` reviewer step, genuinely absent before this pass | `design/S15...` Pillar 2 §2.4; `design/FOUNDATION_v0.5_PATCH.md` §4 | glosa does not make the RPE check retroactive on already-completed `review_report`s — it applies to reviews conducted after the patch lands. glosa does not treat a passed RPE check as raising `tier`/`k_state` by itself; it only prevents an unnamed residual from silently doing so. |
| Principle 5, Friction not magic; the Verification Paradox (lines 688–691, 725–751) | `PRESERVE_FUNCTION` — glosa's K-state/independence-ladder architecture already has this shape | `design/S15...` Pillar 2 §2.5; `EPIS-KNOWLEDGE-VALIDATION` (horizontal authority, prior lineage) | glosa does not adopt an institutional-friction requirement as a literal gate condition — its friction is independence-class routes (I0–I5), not institutional review specifically; institutions remain one possible *source* of an I5 route, never a required one. |
| Objection 11, equal liability to epistemic testing, not equal credibility (lines 891–894) | `PRESERVE_FUNCTION` — already true by omission (no `produced_by`-conditional kernel branch) | `design/S15...` Pillar 2 §2.6 | glosa does not level every card to one tier — cards reaching different independence-class routes legitimately reach different `tier`/`k_state` ceilings; only the *test applied* is uniform. |
| Objection 8, two buttons ≠ two checks (lines 826–835) | `PRESERVE_FUNCTION` — same conclusion as glosa's existing single `I0..I5` ladder + Route Dependence Matrix, independently arrived at | `design/S15...` Pillar 3 §3.1; `NC-69`; existing `NC-31` | glosa does not adopt the paper's specific "route wearing two interfaces" phrase as a field name — it is cited as the same conclusion, reached from a different route (chair ruling C1 predates this reading). |
| Objection 9, accountability human / generation-verification may be AI (lines 848–851) | `PRESERVE_FUNCTION` — `responsible: human` (const) already separate from `produced_by` | `design/S15...` Pillar 3 §3.2 | No change; the paper's wording is cited as confirming an existing design choice, not motivating a new one. |
| Objection 7, unknown-unknowns are uncertainty, never evidence (lines 795–805) | `EXPAND` — new kernel rule on `evidence_relations[].bearing: CHALLENGES` requiring a non-empty `evidence_id` | `design/S15...` Pillar 3 §3.3; `NC-72`; `design/FOUNDATION_v0.5_PATCH.md` §5 | glosa does not claim this closes every unknown-unknowns worry about AI reliability in general — it only prevents an unnamed worry from entering the evidence list disguised as a defeater; the underlying uncertainty is still allowed to be recorded, honestly, as uncertainty. |
| Disclosure challenge, front-matter sentence (lines 43–46) | `EXPAND` — a reusable wording template, not previously stated in glosa's own words | `design/S15...` Pillar 3 §3.4; `design/FOUNDATION_v0.5_PATCH.md` §6 | glosa does not reproduce the paper's exact sentence verbatim as its own front-matter boilerplate (that would be an uncredited restatement) — it adapts the *move* (name the channel, don't just report discomfort) into glosa's own field-referencing wording. |

## What glosa does not take from this paper, in general

- **No claim that AI knows, believes, testifies, understands, or possesses moral standing** — the
  paper itself explicitly grants the skeptic all of this (lines 593–597); glosa's schema already
  had no such field before this reading and adds none now.
- **No metaphysics beyond the realist minimum** the paper itself states (line 171) — glosa does
  not adopt Popper's World 3, Dretske's information theory, Baird's "thing knowledge," or any of
  the paper's cited philosophical positions (Williamson, Frege, Giere, Humphreys) as glosa
  commitments; it cites only the paper's own synthesis, at the grain the paper itself states is
  sufficient (Definition 1's "deliberately weaker notion").
- **No novelty or priority claim inherited** — the paper itself makes limited claims to originate
  the diagnosis of the Possession–Constitution Collapse (paper §12 item 8, "does not claim novelty
  for anti-anthropocentrism as such"); glosa inherits that same restraint per its own gate rule 6
  (never "novel/first/prior art") independently of whether the source paper used such language
  elsewhere.
- **No change to glosa's existing lens attribution** (`lens_used.display: "Readout Universe —
  Yaoharee Lahtee"`) — this paper is added to `lens_used.references` as a supporting citation
  where relevant (per `design/FOUNDATION_v0.5_PATCH.md` §7), not substituted as the lens itself.

## Open questions for the founder

1. This ledger was built from a single AI reading (I0/I1) of the paper text. An independent
   cross-vendor or human check (I2+) of the S15/S9/patch mappings has not run.
2. Whether any additional principle from the paper (beyond the fourteen objections and five named
   principles covered here) should be extracted into its own S15 section or NC row.
3. Whether `design/FOUNDATION_v0.5_PATCH.md`'s proposed `evidence_relation.channel` field and
   `rpe_check` block should be scoped narrower or wider before Fable applies the patch.
