tier: Dr (specified; independently unreviewed)

# TTFB single-instrument — 2026-07-24

## Source
the internal survey (local, not public) §B, `rigorous-diagnosis` entry: "never trust one instrument for a
load-bearing measurement; read/run the actual source; first conclusion = hypothesis; separate
'plausible' vs 'verified' language; adversarial check before 'done'. Incident:
arayaweddingplanner.com TTFB 2026-07-24 (curl 0.3s vs browser 5.8–10s; AI first root-cause wrong)."

## What happened [tier: finite_diagnostic (documented)]
A performance investigation on `arayaweddingplanner.com` measured page load using `curl` alone,
which reported a Time-To-First-Byte of about 0.3 seconds — a healthy number. A real browser
loading the same URL, on the same day, measured 5.8–10 seconds — an order of magnitude slower. The
two instruments disagreed on the same live target because `curl` does not execute the page's
client-side work (scripts, redirects, cookie/session handling, third-party requests) that a real
browser does. The AI's first stated root cause for the slowness — reached before the browser
measurement was taken and treated as settled rather than as a hypothesis — was wrong; only a
second, adversarially-checked pass using the browser as a second instrument found the actual
mechanism.

## What rule it produced [tier: Dr]
Generalized into the `rigorous-diagnosis` discipline, re-derived here as a glosa rule rather than
copied: **a single measurement instrument never backs a load-bearing claim on its own.** In claim
card terms (`design/FOUNDATION_v0.5.md` §3.2), `five_questions.tested.evidence_relations[]`
requires an `independence_class` per entry precisely so a claim resting on one instrument/one
route cannot silently present itself as checked — one `curl` reading is `I0`/self at best, never
enough on its own to raise a `tier` past `Dr`, and the routing procedure that would eventually
route such a claim into `empirical_quant`/`design_science` (§6.3b) requires the access event named
in `five_questions.seen` to be real and dated, not merely the first tool that happened to answer
fast. The wording distinction the incident forced — "plausible" (a hypothesis, `Open`/`Dr`) versus
"verified" (backed by an independent second check) — is the same distinction the Bounded-Judge Law
(§7.3) and `NC-06` (correct output ≠ true theory) already state generally; this incident is the
concrete, dated case that shows what happens when the distinction is skipped under time pressure.

## What would have caught it earlier
A standing rule that any performance/behavior claim about a live system must name **two**
independent measurement routes (e.g. `curl` + a real browser render, or two different browsers)
before the claim's `tier` may be recorded as anything above `Dr`/hypothesis — mirroring the
independence-ladder discipline (§4.2) applied at the instrument level rather than the reviewer
level. A `citation_card`/`evidence_relation` entry whose only backing route is a single
command-line tool is exactly the `D-SAME-VENDOR`-style gap the independence ladder exists to flag,
generalized from "same AI vendor" to "same measurement instrument."

## Non-collapse pairs this incident illustrates
- `NC-06` correct output ≠ true theory (the first curl-based conclusion was internally consistent
  and still wrong about the world).
- `NC-16` doxastic warrant ≠ assertoric disclosure — the AI's confidence in stating the first root
  cause exceeded what one instrument's reading actually warranted.
