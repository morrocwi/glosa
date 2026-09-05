# CLAUDE.md

## glosa gate (identical in CLAUDE.md / AGENTS.md / GEMINI.md)
1. Everything here is a readout, not truth. Tag your tier (Th_coqc / finite_diagnostic / fit_calibrated / Dr / definition / Open) on every verdict.
2. Read design/FOUNDATION_v0.5.md §2 (spine) and §3 (claim card) before editing anything. (One
   canonical spec pair: design/CURRENT_SPEC.txt names FOUNDATION_v0.5.md + REPO_SPEC_v0.5.md.)
3. Maker ≠ checker ≠ approver. Never certify what you produced. Same-model self-review has no standing.
4. If you were pointed at reviews/routes/*/PACKET.md you are ONE route: read only your packet, write review_report.yaml, tier your verdict, do not touch the claim card.
5. Human holds standpoint, falsifier judgment, ethics, and public commitment. AI drafts, routes, checks mechanically, logs. AI is never an author.
6. Never propose external/institutional validation as what makes a claim legitimate. Never write "novel/first/prior art". Comparison = same / different / cited.
7. Human raw lines (Blackbox Note) are verbatim, never edited or translated in place; the cooking log is append-only.
8. No independent check ⇒ no release. Public push only through the publish gate (PR + adversarial review + leak scan).
9. **No AI attribution without explicit permission.** Never add an AI or vendor/model name as author,
   co-author, contributor, or credit anywhere that leaves this repo or is public: git commit trailers
   (`Co-Authored-By`, session links), Zenodo/CITATION metadata, paper bylines, acknowledgements,
   READMEs. Disclosure of AI use is mandatory (cooking log, Blackbox Note, ai_filled) but names the
   role — "AI assistant" — not the vendor, unless the founder explicitly permits it for that artifact.
   Founder ruling 2026-09-05 (Blackbox Log BBL-2026-09-04-104/105).
10. **No finding is ever dropped.** Every finding, proposal, or review item that enters a ledger
    (meeting record, review report, gate output, DAG) must appear in every downstream record either
    carried forward or explicitly closed with a reason; a count mismatch is a gate failure
    (`scripts/check_findings_complete.py`). Hand-offs between AI workers pass file paths, never
    truncated slices. Founder ruling 2026-09-05 (Blackbox Log BBL-2026-09-05-121), after one
    proposal (SA-5) fell out of a re-anchoring pass through a truncated hand-off.
