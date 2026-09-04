<!--
cross_vendor_review_packet.md — RWI S10 template (Dr, unreviewed proposed format)

WHAT THIS FILE IS: the vendor-neutral unit of work for ONE route in a cross-vendor
Decorrelated Verification Protocol (S10 §6). It is dropped at
reviews/routes/<claim_id>/<route_id>/PACKET.md and picked up by ANY agent — Claude Code, Codex,
Gemini CLI, or a local model runner — from the repository alone. No shared session, no
orchestration tool, and no prior conversation are required to act on it.

VENDOR-NEUTRALITY RULE: this packet must contain no mention of which vendor/model is being asked
to fill it in. The same file is handed to every route unchanged except for the fields inside the
"ROUTE ASSIGNMENT" block below. Do not add vendor-specific phrasing anywhere else in this file.

GATE BLOCK THIS FILE ASSUMES: whichever agent opens this file has already read the identical
short block that appears in this repo's CLAUDE.md / AGENTS.md / GEMINI.md (S10 §6):

  ## RWI cross-vendor review gate
  If you were pointed at a file under reviews/routes/*/PACKET.md: you are one route in a
  Decorrelated Verification Protocol. Read ONLY the packet in your assigned directory — do not
  read other routes' review_report.yaml files, and do not read the claim's authorship history
  beyond what the packet includes. Fill in review_report.yaml per
  schema/review_report.schema.json exactly. State your verdict's tier
  (Th_coqc/finite_diagnostic/fit_calibrated/Dr/definition/Open — the six-value ladder, chair ruling C4) explicitly — an untiered verdict is invalid
  (Bounded-Judge Law, S9 NC-06). Do not edit the claim card itself. Do not re-run your assigned
  role a second time on the same claim without a new PACKET version (Query Stop Rule, S10 §3.4).

If that gate block is missing from the repo you are working in, treat this packet as invalid and
stop — do not proceed on trust.
-->

# Cross-Vendor Review Packet

## 0. Route assignment (the only section that varies between routes)

- `claim_id`: `<claim-id>`
- `route_id`: `<R1 | R2 | R3 | …>` — use this id in your output, never your own vendor/model name
- `role`: one of `Advocate | NearestConceptProsecutor | Falsifier | SourceAuditor | HostileReviewer | TranslationReviewer | MethodEmpiricalDesigner`
  (definitions: `design/S10_cross-vendor-independence-ladder.md` §5 — do not improvise a different role)
- `evidence_base_you_may_consult`: `<claim card only | claim card + named files | live web search | none>`
- `acceptance_criteria_ref`: `reviews/routes/<claim_id>/ACCEPTANCE_CRITERIA.md` (frozen before any route started — read it, do not propose changes to it)

## 1. The claim under review

> Paste the claim card's exact `seen: / separates: / ai_filled: / assumed: / tested:` fields
> here, verbatim. Do not paraphrase — paraphrasing at this step is itself a silent-lift risk
> (S9 NC-15).

```
<claim card fields, verbatim>
```

## 2. What you are being asked to do

Perform the job of your assigned `role` (§0) against the claim in §1, using only the evidence
base named in §0. Specifically:

- **Advocate** — argue the claim's strongest form using only what the evidence in §1 actually
  supports. Note whether a stronger, still-supportable version exists.
- **NearestConceptProsecutor** — find the closest existing concept/prior result and argue the
  claim is not meaningfully different from it. State the explanatory delta if one survives.
- **Falsifier** — actively search for the observation/record that would defeat this claim. A
  report with no attempted defeat is not a Falsifier report.
- **SourceAuditor** — run the Integrity Firewall on every citation named in §1: does the source
  exist, does its metadata match, does it actually support the specific scope claimed (source
  existence ≠ claim support, S9 NC-18)?
- **HostileReviewer** — adopt an adversarial stance toward the whole artifact, not one claim.
  Also: if you can see the Route Dependence Matrix for this claim, fill in the `shared_with`
  field honestly for your own route — this is the one field an operator has an incentive to
  under-report, so this role is specifically tasked with catching it.
- **TranslationReviewer** — check any Thai/English pair in §1 for translation drift (meaning,
  not just fluency); Thai is source-of-truth content, rewritten not translated, per this
  workspace's own rule — verify that discipline was followed, don't just check grammar.
- **MethodEmpiricalDesigner** — propose the observation/test that would discriminate between
  this claim and its nearest rival. Feed this into the claim's `tested:`/falsifier field.

## 3. What you must NOT do

- Do not read `reviews/routes/<claim_id>/<other_route_id>/` — you are blind to other routes by
  design (Operator-Decorrelation Control, S10 §3.2).
- Do not edit the claim card itself. Your output is a `review_report.yaml`, not a revision.
- Do not re-run yourself on this same claim a second time to get a different answer. One
  documented re-ask with a logged reason is allowed if your first answer was genuinely ambiguous
  or mis-scoped; a third attempt requires a Disagreement Ledger entry instead (Query Stop Rule,
  S10 §3.4 — repeated re-asking is answer-shopping/model-shopping, a SCRAM condition, S10 §9).
- Do not soften an untiered verdict into a tiered-sounding sentence. If you cannot tier it, say
  `Open` and say why.

## 4. Required output — `review_report.yaml`

Write this file to `reviews/routes/<claim_id>/<route_id>/review_report.yaml` (schema:
`schema/review_report.schema.json`, extended per `design/S10_cross-vendor-independence-ladder.md`
§7):

```yaml
review_report:
  claim_ref: <claim_id>
  route_id: <route_id>
  independence_level: <I0|I1|I2|I3|I4|I5>   # your honest self-assessment; a synthesizing role or
                                              # Hostile Reviewer may later revise this after
                                              # checking the Route Dependence Matrix's shared_with
                                              # field — do not inflate this yourself
  role: <role from §0>
  verdict: "<your actual verdict, in your own words>"
  verdict_tier: <Th_coqc|finite_diagnostic|fit_calibrated|Dr|definition|Open>   # REQUIRED, SIX values (chair ruling C4) — Bounded-Judge Law (S9 NC-06):
                                                        # your verdict is itself a bounded claim
  evidence_consulted:
    - "<list what you actually looked at>"
  shared_dependency_disclosure: >
    <your own honest statement of what you might share with other routes on this claim: same
    vendor as another route you're aware of, same operator, same prompt ancestry, or "none known
    to me" — this feeds the Route Dependence Matrix's shared_with field>
  date: <ISO 8601 date>
```

## 5. If you disagree with another route (only if you can see that you do)

If your evidence base includes another route's already-written `review_report.yaml` (this only
happens for a role explicitly tasked with synthesis, not for a fresh blind route — see §3), and
your verdict differs from theirs, do not average the two verdicts and do not silently prefer one.
Instead, propose a `disagreement_ledger` entry per
`design/S10_cross-vendor-independence-ladder.md` §4: classify the disagreement's `nature`
(construct/source/mechanism/boundary/venue/epistemic_tier), state both `positions` verbatim, and
either point to a `decisive_record` that resolves it (outcome `RESOLVED`) or declare it open and
tier the disputed point `Open` (outcome `DECLARED`). Both outcomes are valid; a laundered
consensus is not.
