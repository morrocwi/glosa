# FOUNDATION v0.5 patch note — "Written by AI. Still True." pillars integration

> **Tier: Dr, specified not applied.** This file states the exact text to insert into
> `FOUNDATION_v0.4.md` to produce v0.5. It does not itself edit `FOUNDATION_v0.4.md` — per this
> task's scope (design/, lineage/, sources/, docs/ only; other agents own the live FOUNDATION
> file). the AI assistant or the next synthesis pass applies this patch. Source:
> `sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt` (Zenodo DOI `10.5281/zenodo.22301202`, CC BY 4.0);
> full derivation: `design/S15_pillars-ontology-epistemology-methodology.md`,
> `design/S9_non-collapse-table.md` `NC-65`..`NC-73`, `lineage/RELATION_TO_WRITTEN_BY_AI.md`.

---

## 1. Insert into `FOUNDATION_v0.4.md` §1, as new subsection "1.0 Pillars — ontology / epistemology / methodology" (≤ 60 lines)

Insert immediately after §1's heading, before the existing "1.1 What glosa is" — exact text:

```markdown
### 1.0 Pillars — ontology / epistemology / methodology

glosa's schema rests on three pillars, each independently traceable to a named glosa mechanism
(full derivation: `design/S15_pillars-ontology-epistemology-methodology.md`; source: "Written by
AI. Still True.," Yaoharee Lahtee, Aug 2026, Zenodo DOI `10.5281/zenodo.22301202`, CC BY 4.0 —
cited as *same*, never *adopted from*, per gate rule 6; the lineage of glosa's own readout-not-
truth stance stays with Readout Universe/Genesis, `lens_used.display`).

**Ontology — pre-subjective constraint structure.** What a claim card reports on was already
capable of making that report right or wrong before the card existed (`RA = OA(W;ΠA) ≠ W`); a
record is an operator-conditioned readout, never the world itself, whether the operator is human
or not. Embodied in: `tested.falsifier` (must name an independent observation), `five_questions.
seen` (record vs. world kept structurally distinct).

**Epistemology — Role Separation, against the Possession–Constitution Collapse.** Ten epistemic
roles (truth, constraint, evidence, reliability, provenance, credibility, accountability,
legitimacy, authorship, possession) are never identical merely because one agent occupies several
at once. glosa names this failure — treating a knower's identity as itself epistemic value — as a
design reason internal to its own schema, never as an accusation against a named party. Embodied
in: the ten-role crosswalk (§3.1's Five-Questions table + `responsible`/`produced_by`/
`independent_check` split); the deliberate absence of any "truth" or "possession" field.

**Methodology — named channels, friction not magic.** No source-metadata fact (`produced_by`,
`ai_filled.*`, a citation's tier) may move a card's standing without naming the specific channel
(reliability, independence, access, assurance, accountability, calibration, error correlation) it
bears on (Bridge Burden) — an unnamed residual must be named or dropped (Residual Provenance
Effect, `rpe_check`, §3.3). Institutions and gates alike are friction machines: cheap to enter
(`shape: stub`, near-zero authoring cost), expensive to survive (independence-class floors on
tier/`k_state` advancement, §3.3 rules 1–4, 9) — never a stamp that raises standing by itself
(`D-NO-VERTICAL-AUTHORITY`).

Non-collapse rows from this reading: `NC-65` Possession≠Constitution · `NC-66` m(A)≠ρ(A) · `NC-67`
Credibility≠Legitimacy · `NC-68` Co-location≠Identity · `NC-69` Two interfaces≠two routes ·
`NC-70` Address of responsibility≠address of truth · `NC-71` RA≠W · `NC-72` Constraint≠
evidence-for-us · `NC-73` Certification≠Warrant (full rows: `design/S9_non-collapse-table.md`).
```

(58 lines including the blank separators and code fence — under the 60-line ceiling.)

---

## 2. Non-collapse table additions

Append `NC-65`..`NC-73` (Family I — Possession / Constitution) to Appendix A's compact index in
`FOUNDATION_v0.4.md`, in the same one-line-per-family style as the existing families, pointing at
the full rows now living in `design/S9_non-collapse-table.md` (which this pass also
reconstructed/created — see that file's own header note on the recovery status of `NC-01`..`64`):

```markdown
### Family I — Possession / Constitution (new this pass)
`NC-65` Possession≠Constitution · `NC-66` m(A)≠ρ(A) (source metadata≠reliability) · `NC-67`
Credibility≠Legitimacy · `NC-68` Co-location≠Identity (of roles) · `NC-69` Two interfaces≠two
routes · `NC-70` Address of responsibility≠address of truth · `NC-71` RA≠W · `NC-72` Constraint≠
evidence-for-us · `NC-73` Certification≠Warrant. *Enforced by: §3.1 role crosswalk,
`evidence_relation.channel` (new, §3 below), `rpe_check` (new, §4 below), `D-NO-VERTICAL-
AUTHORITY`. Full rows: `design/S9_non-collapse-table.md`.*
```

Also update Appendix A's opening line ("64 rows across seven families") to "73 rows across eight
families."

---

## 3. New field: `evidence_relation.channel`

**Where:** `FOUNDATION_v0.4.md` §3.2, inside `tested.evidence_relations[]`'s object shape.
**Why:** Principle 2 (Bridge Burden) — no source-metadata effect may move standing without naming
its channel; the current shape (`evidence_id, bearing, independence_class, strength,
citation_ref`) has no field for this. `design/S15...` Pillar 2 §2.3.

```
tested: { evidence_relations: [ { evidence_id, bearing: SUPPORTS|CHALLENGES|NEUTRAL|UNRESOLVED,
            independence_class: <I0..I5, §4.2>, strength, citation_ref,
            channel: reliability | independence | access | assurance | accountability |
                     calibration | error_correlation | other(named)   # NEW — Bridge Burden field
                     # required whenever this entry is claimed to change a card's tier/k_state;
                     # `other(named)` requires the specific relation named inline, never bare
                     # "other". Kernel rule: an entry with no `channel` may still exist (a raw,
                     # unprocessed evidence log line) but may NOT be cited as the reason `tier` or
                     # `k_state` advanced (new §3.3 rule, see below).
          } ],
          falsifier: string (required, non-empty, must name an observation/check outcome),
          dissent_records: [ { by, date, content, resolved: bool } ] }
```

Also, on `citation_card.yaml` (`templates/knowledge/citation_card.yaml`), add a parallel note
field (not a new boolean, since the card's existing tuple already covers the mechanism — see
`design/S15...` Pillar 2 §2.3's crosswalk table):

```yaml
credibility_channel: ""   # NEW — one line naming which of verification_method / identifier.kind /
                          # metadata_verified / claim_match_verified / evidence_tier / scope /
                          # who_verified is doing the work when this card's status is cited as a
                          # reason to raise or lower confidence in the claim it backs. Optional but
                          # recommended; required whenever the card is cited in a `D-COMPARISON` or
                          # `D-AIFILL` context (Bridge Burden applied to citation use specifically).
```

**New kernel rule (append to §3.3):**

> 13. An `evidence_relations[]` entry with no `channel` (or `channel: other` with no named
>     relation) may be logged, but may never be cited in `disclaimers_emitted`, a review report,
>     or public prose as the reason a card's `tier` or `k_state` advanced (Bridge Burden,
>     `NC-66`/`NC-70`).

---

## 4. RPE reviewer check

**Where:** `FOUNDATION_v0.4.md` §7.1 (MIMCG gate table) — add a required `rpe_check` block to
`review_report`. Source: Definition 4 (Residual Provenance Effect), Principle 4 (Provenance
Relevance Constraint). `design/S15...` Pillar 2 §2.4.

```
review_report:
  ...
  rpe_check:                              # NEW, required whenever produced_by ≠ single fixed value
                                          # across the route being reviewed (i.e. whenever the
                                          # reviewer could, in principle, imagine swapping
                                          # human/ai/joint with everything else held fixed)
    credence_before_channel_fix: string   # the reviewer's verdict/confidence before naming channels
    credence_after_channel_fix: string    # the reviewer's verdict/confidence after every relevant
                                          # channel (reliability, independence, access, assurance,
                                          # accountability, calibration, error correlation) is made
                                          # explicit and held fixed
    residual_named: string | null         # if the verdict still differs, name the specific channel
    residual_dropped: bool                # OR: the reviewer determined no channel justifies the
                                          # residual and dropped it from the verdict
```

**Kernel rule (append to §3.3 or §7.1):**

> `rpe_check.residual_named` and `rpe_check.residual_dropped` cannot both be empty/false when
> `credence_before_channel_fix ≠ credence_after_channel_fix` — a hard validation error, not a
> disclaimer-and-proceed (same enforcement pattern as existing rule 12's `D-LENS-UNSIGNED`).

**Binding companion rule (§5 disclaimer catalogue, `D-AIFILL` entry):** `D-AIFILL` discloses a
route property; it is never itself a tier/independence penalty. Any tier or independence effect
attributed to an `ai_filled.*` sub-field must be justified by that specific sub-field, named, not
by `ai_filled.used: true` alone (Objection 7 / Objection 6 concession, paper lines 795–805,
871–879).

---

## 5. Evidence-list hard rule (Objection 7 / `NC-72`)

**Where:** `FOUNDATION_v0.4.md` §3.3, new numbered rule (append after existing rule 13 above, as
rule 14):

> 14. An `evidence_relations[]` entry with `bearing: CHALLENGES` requires a non-empty
>     `evidence_id`. An unnamed, unrepresented possible failure mode is not a defeater — it is an
>     open item, and belongs in `identification_ladder`'s `unidentified` value or `non_claims`,
>     never in the evidence list disguised as a challenge (Objection 7, `NC-72`).

---

## 6. AI-disclosure sentence template

**Where:** `FOUNDATION_v0.4.md` §5 or a new front-matter boilerplate section, for reuse in any
glosa document's own AI-assistance disclosure (paper front matter, README, claim card
`ai_filled.note`). Source: the paper's own disclosure-challenge sentence (lines 43–46).
`design/S15...` Pillar 3 §3.4.

```markdown
**glosa AI-disclosure template:** "AI assisted with `<name the roles: drafting / literature
search / mechanical checking / language editing / route comparison>` in this work. The human
owner (`human_owner`) selected, checked, and endorses the final claim; `responsible: human`. If a
specific `ai_filled.*` field changes your assessment of this claim, name the reliability,
independence, or evidential channel it affects (`rpe_check`, §4 above) rather than the fact of AI
involvement alone — an unnamed channel is a residual, and this document requires residuals to be
named or dropped, never left silent."
```

---

## 7. `lens_used.display` extension — cite the pillar paper alongside, not instead

**Where:** `templates/knowledge/blackbox_note.yaml`, `lens_used.references` list — additive, no
change to `lens_used.display`'s wording (which stays exactly `"Readout Universe — Yaoharee
Lahtee"`, per founder requests 38/38b, unchanged).

```yaml
lens_used:
  display: "Readout Universe — Yaoharee Lahtee"     # UNCHANGED
  ...
  references:
    - "10.5281/zenodo.21529456"   # Readout Genesis Standalone Synthesis
    - "10.5281/zenodo.21665100"   # What a Zero Readout Certifies
    - "10.5281/zenodo.22301318"   # The Readout Condition (Aug 2026) — NEW, now published,
                                  # concept DOI 10.5281/zenodo.22301317
    - "10.5281/zenodo.22301202"   # NEW — "Written by AI. Still True." (Aug 2026), cited
                                  # alongside as the pillars source for the Role Separation /
                                  # Possession-Constitution Collapse / Bridge Burden mechanisms
                                  # this pass adds — NOT a change of lens attribution, an
                                  # additional cited reference (design/S15..., §7 of this patch)
    - "github.com/morrocwi/readout_universe"
```

Both DOIs above were confirmed published (CC BY 4.0) by the coordinator during this session
(2026-09-04) — `sources/citation_cards/CIT-written-by-ai-v6.yaml` for the second; a parallel
citation card for the Readout Condition is not part of this task's scope and should be created
separately (open item, see below).

---

## Open items for the AI assistant / the next synthesis pass

1. Apply §1–§7 above to `FOUNDATION_v0.4.md`, bump `schema_version` per its own convention (this
   patch touches the claim card's `tested.evidence_relations[]` shape additively — a new optional
   field — and `review_report`'s shape with a new required block; classify as additive/breaking
   per FOUNDATION's own versioning rule before choosing the next version number).
2. Create a citation card for the Readout Condition (`10.5281/zenodo.22301318`) parallel to
   `sources/citation_cards/CIT-written-by-ai-v6.yaml` — out of this task's named scope, flagged
   here as a clear next step.
3. `sources/README.md` PENDING_COPY rows (Readout Condition text, Standalone Scholar text,
   ai-native-scholarship skill) — decide whether to physically copy these into the public repo.
4. An I2+ (cross-vendor or human) check of this entire patch has not run — every mapping above is
   Dr, single-pass.
