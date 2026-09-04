# P14 — Project Advisor (a third role)

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction (request 22); AI
> drafted this card, narrating `FOUNDATION_v0.5.md` §7.7 in full. Comparison language is
> same/different/cited only. Knowledge base is cited as a dependency, never merged
> (`FOUNDATION_v0.5.md` §1.2, chair ruling B3): `ai-native-scholarship v1.0.0` (Zenodo record) is
> named by version+DOI, not copied into this repo.

## id

`P14`

## Rule

The Project Advisor is a **third role**, distinct from Maker, Checker, and Approver on the same
artifact — it never certifies what it advises on, and it never activates before that artifact has
already cleared release. Specifically:

- **Activation condition:** the advisor role activates **only** after `gate_release` returns
  `PASS`/`PASS_WITH_LIMITS` on an L3+ artifact (`P10`) — never on unreleased/`Draft`/`Pending
  Review` work. Advising on unreleased work would let the advisor's forward-looking framing
  quietly substitute for the independent check the artifact has not yet passed.
- **Reads, never writes**, the release manifest, the linked claim/evidence/citation cards, the
  project's kg, and the existing K1→K2 conversion ledger.
- **Produces one `conversion_plan.yaml` per release**, containing: the K-state now; a
  Global route and a Thai/local route (per the GDA six questions); the next three *addressed*
  conversion actions (not a wishlist — actions the plan itself names as already actionable); a
  rejection budget/survival buffer; a fixed "what NOT to do" list; and a **candidate, never
  confirmed**, K1→K2 ledger row.
- **Tier is always `Dr`** — the plan is a declared bridge/narrative synthesis, never a
  mechanically-checked artifact, regardless of how well-evidenced the underlying release is.
- **Governed by two gates, not universal laws:**
  - Mint–convert coupling: `new_flagship_recommended ⇒ mint_count ≤ λ·conversion_count` (`λ`
    never a shipped constant; cold-start default is zero new flagships, conversion-only).
  - Reactivity License: `increase_mint_rate ⇒ integrity_clean ∧ xenon_below_threshold ∧
    conversion_log_operational`.
- **SCRAM (refuses to advise, `status: BLOCKED`) on:** an unverified citation in scope; K1
  misrepresented as K2/K3 anywhere in the release; a venue disclosure gap; the advisor's own
  identity conflict (the same identity as Maker/Checker/Approver on this artifact); an open
  Xenon-ledger item above threshold. **None of these predicates is yet mechanically checkable as
  specified** — a future revision must either state each predicate exactly or mark it
  human-judgment-only; this card does not silently claim otherwise.

## Why / incident

Founder request 22 asked for a role distinct from the release-gate roles specifically because
conversion advice (what should this release do next, toward K2, toward a wider audience) is a
different question from release certification (is this release honest about its own evidence),
and collapsing the two lets a certifying identity's own forward-looking optimism quietly stand in
for an independent check it never actually ran. The hardest open case this card names rather than
hides: a founder who is both the Maker of most releases and, for now, the only available human —
the advisor's independence claim is untested against exactly this case
(`FOUNDATION_v0.5.md` §11 item 8, §12's carried-forward S12 must-fix).

## Inputs → outputs

- **Inputs:** a release manifest already at `PASS`/`PASS_WITH_LIMITS`; the artifact's linked
  claim/evidence/citation cards; the project's kg; the existing K1→K2 ledger (`P6`, §7.6, ten
  reused columns).
- **Outputs:** one `conversion_plan.yaml`, tier `Dr`, carrying the fields listed above; a
  candidate (unconfirmed) K1→K2 ledger row, which becomes a real ledger row only when a separate
  I5-backed check confirms it (`P6` §4.2 — the advisor's own read never substitutes for that
  check).

## Gate

A `conversion_plan.yaml` may not name a K-state advancement as already achieved — only as a
candidate route. `D-ADVISOR-NOT-K2` fires on any plan referencing a K-state, restating that the
plan itself grants nothing. A plan expires (`D-ADVISOR-EXPIRED`) when the artifact it advises on
is revised or its own `expires_at` passes; a stale plan may not be cited as current advice.

## Human / AI split

Human: is the required distinct identity whenever the advisor role and the artifact's own Maker/
Checker/Approver would otherwise collapse into one person — this is the SCRAM condition this card
names as still unresolved for the single-founder case, so it is flagged to the human explicitly
rather than silently permitted. AI: may perform the mechanical read (release manifest, kg, ledger)
and draft the `conversion_plan.yaml` fields, always tiered `Dr`, always citing
`ai-native-scholarship` as a dependency by version+DOI rather than restating its content.

## Disclaimers

`D-ADVISOR` (every `conversion_plan.yaml`; wording cites `D-NO-VERTICAL-AUTHORITY` rather than
restating it), `D-ADVISOR-NOT-K2` (any plan referencing a K-state), `D-ADVISOR-EXPIRED` (a stale
plan), `D-NO-VERTICAL-AUTHORITY` (the plan's Global/Thai routes never frame a venue's acceptance
as what makes the work legitimate).

## NC pairs

`NC-28` maker ≠ checker ≠ approver (the advisor is a fourth, non-overlapping identity requirement
on the same artifact) · `NC-32` DVP ≠ K2 · `NC-33` K1 ≠ Certification · `NC-38` Credit ≠
EpistemicValue · `NC-40` Friction ≠ Fellowship · `NC-42` Production-supercritical ≠ Credit-
supercritical.

## Not-do

- Do not activate the advisor role on an artifact that has not yet cleared `gate_release`.
- Do not let the advisor's plan write to the claim card, kg, or ledger it read from — read-only.
- Do not confirm a candidate K1→K2 ledger row from the plan alone; it requires its own I5-backed
  check.
- Do not let the same identity serve as advisor and as Maker/Checker/Approver on the same
  artifact without flagging the conflict (the unresolved SCRAM case above).
- Do not merge `ai-native-scholarship`'s content into this repo's `plugins/` — cite it as a
  dependency by name+version+DOI.
- Do not treat "getting external/venue acceptance" as itself a conversion action — the plan's
  routes describe *this repo's own* next steps, never outside validation as the goal
  (`EPIS-KNOWLEDGE-VALIDATION`).

## Tier

Dr (specified; independently unreviewed). The SCRAM predicates are named, not yet reduced to a
mechanically-checkable form.
