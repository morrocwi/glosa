# P8 — Diagnosis (rigorous-diagnosis, 5 disciplines)

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself: every discipline below is a specified procedure,
> not yet mechanically enforced and not yet independently re-checked. Founder = method direction;
> AI (assistant seat) drafted this card's wording from the pattern already named in this
> workspace's internal `rigorous-diagnosis` skill and the incident that produced it. Comparison
> language in this card is same/different/cited only.

## id

`P8`

## Rule

Before stating a root cause, a fix, or "this is safe now" for any non-trivial observed problem —
in code, in a claim card's `five_questions.separates`, in a measurement, in a reviewer's own
verdict — apply five disciplines, in order, and record which ones were actually run:

1. **No single instrument is truth.** One measurement tool, one log line, one test run is a
   *readout* of the system, not the system. A second, differently-built instrument must agree
   before a number is trusted.
2. **Plausible ≠ verified.** A root-cause story that explains the symptom is a hypothesis, not a
   finding, until it is tested against a prediction the story itself makes (if X is the cause,
   changing X should change the symptom by a stated amount — check that it did).
3. **Reproduce under real conditions, not a simplified proxy.** A synthetic/local/simplified
   reproduction that "looks like" the real failure is not the same access event as the real one
   (`five_questions.seen.access_model` must name which was actually used); a fix verified only
   against the proxy is unverified against the real case.
4. **Re-verify your own conclusion before declaring it closed.** The session that produced a
   root-cause claim is not a check on that claim (`NC-28`/`NC-29`, maker ≠ checker); a second
   pass — ideally by a different route/session/instrument — must confirm the fix before `status`
   advances past `Draft`.
5. **State confidence honestly, per number.** Every diagnostic claim carries a tier
   (`finite_diagnostic` only when reproduced by a named command; `Dr` for a plausible-but-untested
   narrative; never silently upgraded because the story is convincing).

## Why / incident

Extracted from a real 2026-07-24 TTFB (time-to-first-byte) investigation on a production
WordPress site in this workspace's own operating history: a single measurement instrument
(`curl`, no browser-realistic headers/rendering) reported the page as fast; a real browser on the
identical URL was roughly 20× slower. The session's own first root-cause conclusion — reached
before the second instrument was run — was also later found to name the wrong mechanism once
re-verified. Neither the wrong number nor the wrong mechanism survived discipline 1 and discipline
4 once they were actually applied; both had already been asserted, in the same session, as
settled before that. This card exists so the same failure mode is checked for by name rather than
re-discovered per incident.

## Inputs → outputs

- **Inputs:** an observed symptom (a number, an error, a claim needing a root cause); at least one
  measurement instrument or evidence route already run.
- **Outputs:** a diagnosis record naming (a) which of the five disciplines were actually applied,
  (b) the second instrument/route used for discipline 1, (c) the falsifiable prediction discipline
  2 tested and its result, (d) the access model used for discipline 3, (e) who/what performed the
  re-verification in discipline 4, (f) the tier assigned per discipline 5. This record is a
  `logbook.jsonl` entry (`P11`) and, where it backs a claim card, an `evidence_relation` under
  `five_questions.tested`.

## Gate

A diagnosis may not back a claim card's `tested.evidence_relations` entry, and a fix may not
advance `status` past `Draft`, unless disciplines 1 and 4 are both recorded as applied by an
identity distinct from the one that first proposed the root cause (maker ≠ checker, `MC-01`). A
diagnosis missing discipline 5's tier tag is invalid input to any gate (`P6`'s Bounded-Judge Law:
an untiered verdict backs nothing).

## Human / AI split

Human: owns the judgment of which real-world condition (discipline 3) actually matters for this
problem, and is the required second identity for discipline 4's re-verification whenever the
diagnosis will back anything reaching L2+ (`P6`). AI: may run the second instrument (discipline 1),
draft the falsifiable prediction (discipline 2), and propose the tier (discipline 5), but its own
self-report of "verified" carries no standing as the discipline-4 check on its own prior claim
(`NC-29`).

## Disclaimers

`D-TIER` (every diagnostic claim), `D-AIFILL` (any AI-drafted prediction/root-cause text),
`D-INDEPENDENCE` (whenever the strongest check on file is I0–I2), `D-CANDIDATE-STATUS` (any
diagnosis not yet through discipline 4 by a distinct identity).

## NC pairs

`NC-06` correct output ≠ true theory (Bounded-Judge Law — a fix that made the symptom go away is
not proof the named mechanism was the real one) · `NC-10` `finite_diagnostic` ≠ proof · `NC-17`
Mechanical validity ≠ Semantic validity · `NC-28`/`NC-29` maker ≠ checker; AI generator ≠ AI
reviewer of the same commit · `NC-36` Reproduction ≠ Replication.

## Not-do

- Do not state a root cause as settled from one instrument's readout.
- Do not let the session that proposed a fix also certify the fix as verified.
- Do not reuse a synthetic/simplified reproduction as if it were the real access event.
- Do not omit the tier on a diagnostic claim because the mechanism "seems obviously right."
- Do not propose external/institutional review as what would make a diagnosis legitimate — the
  check that matters is a second instrument/route and a distinct identity, both internal disciplines
  (`EPIS-KNOWLEDGE-VALIDATION`).

## Tier

Dr (specified; independently unreviewed). This card has not itself been through discipline 4.
