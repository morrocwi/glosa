tier: Dr (specified; independently unreviewed)

# check_docs silent-pass — 2026-08-01

## Source
the internal survey (local, not public) §A, `doc-ecosystem / human-ai-doc-ecosystem / uia-doc-ecosystem-bridge`
entry: "Incident: `check_docs.mjs` printed 'OK — all hashes match' with no baseline (2026-08-01)."

## What happened [tier: finite_diagnostic (documented)]
A documentation-consistency checker (`check_docs.mjs`, in the `doc-ecosystem` family of repos)
printed a success message — "OK — all hashes match" — on a run where no baseline hash file existed
yet to compare against. The check had nothing to compare, so there was nothing that could actually
fail; it printed the same success wording it would print on a genuine match. The failure was
discovered only later, when the doc-ecosystem's own four-layer discipline (PHILOSOPHY → RULES →
MECHANISM → LOG) was applied to the checker itself and the gap between "checked, found no
difference" and "had nothing to check against" was named explicitly (`A2` in that system's own
axiom set, reused here as `NC-26`).

## What rule it produced [tier: Dr]
`NC-26` — **"not checked" ≠ "checked, nothing found"** (Appendix A, Family B, `design/
FOUNDATION_v0.5.md`). Generalized rule for glosa: any kernel validator or gate function
(`gate_release`, `cite_check`, `kg_validate`, and every future `validate_*`) must distinguish, in
its own output, between (a) the check ran and found no problem, and (b) the check's precondition
data (a baseline, a prior version, a populated field) was absent, so the check did not actually run.
A validator that cannot tell these apart must default to state (b) and refuse to emit a bare
"PASS" — it must emit something that names the missing precondition. This is the same shape as
`provenance_dag.status: not_run | run` and `silent_lift_check.status: not_run | run` in the claim
card (`design/FOUNDATION_v0.5.md` §3.2, must-fix 12) — both fields exist specifically so a card
cannot present an unrun check as a passed one.

## What would have caught it earlier
A one-line self-test on the checker itself: run it once against a repo state with **no** baseline
file present and assert the output is NOT the same string as a genuine pass. This is exactly the
kind of check `kernel/glosa_kernel.py`'s own `self_test` function (`design/FOUNDATION_v0.5.md` §9)
is required to run against every `validate_*`/`gate_*` function before it ships — a gate that has
never been exercised against its own "nothing to check yet" case is untested in the one direction
that matters most for false confidence.

## Non-collapse pairs this incident illustrates
- `NC-26` "not checked" ≠ "checked, nothing found" (the direct hit).
- `NC-34` No independent check ⇒ No release — a checker that cannot fail is not an independent
  check at all; it is decoration that looks like one.
