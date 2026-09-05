# Publish gate v1 — public summary (glosa v0.1.0, 2026-09-04)

Route: independent multi-agent adversarial gate (R1 leak · R2 license · R3 tier fidelity ·
R4 citation · R5 anchor consistency · R6 register/overclaim · R7 completeness), each finding
challenged by skeptics; then a second independent re-verify pass on the fixes. Maker ≠ checker.
Tier of every verdict: finite_diagnostic. K-state of the release: K0.

| id | class | finding (sanitized) | status |
|----|-------|---------------------|--------|
| B-1 | leak | session drafts and a session-id fragment tracked | fixed: drafts untracked, fragment redacted, denylist extended (local) |
| B-2 | leak | internal survey/plan/review files named private repositories | fixed: files untracked; remaining names generalized; private-name patterns moved to a git-ignored local denylist |
| B-3 | leak | local file inventory tracked | fixed: untracked |
| B-4 | accuracy | sources/ status table overstated what is present | fixed: PRESENT / NOT_PRESENT stated per file |
| B-5 | consistency | K-state asserted as K1 without an I3 route | fixed: K0 everywhere; K1 requires I3 |
| B-6 | self-consistency | paper said it could not clear its own lens-citation gate | fixed: VERIFIED I3 lens citation cards; EN/TH/LaTeX aligned |
| B-7 | citation | reserved DOI resolves only after publish | disclosed; published at push time |
| B-8 | citation | no VERIFIED citation card for the lens DOIs | fixed: cross-vendor (I3) claim-match, record in registry/verification/ |
| B-9 | metadata | invalid Zenodo relation | fixed |
| B-10 | provenance | Blackbox Log pre-release history had a removal + restore | disclosed as append-only correction entry; rule text qualified |
| B-11 | release | stale draft archive on Zenodo | fixed: HEAD archive + PDFs uploaded before publish |

Warnings (non-blocking) were fixed where mechanical (CHANGELOG, README pointers, duplicated
wording) and otherwise carried in RELEASE_CHECKLIST.md. The verbatim packets exist locally and
can be shown to any reviewer on request; they are not public because of what they quote.

## v0.3.0 (2026-09-05) — gate v3 summary
17 BLOCKs upheld by skeptics and fixed (private-name leak ×12, one vendor-credit field, one tier over-statement, one stale spec status, one scanner class, one changelog status); verdict PASS_WITH_LIMITS (K0; six founder decisions pending; rule 27 open on the tracked corpus).

## v0.4.0 (2026-09-05) — gate v4 summary
4 BLOCKs upheld and fixed (one private path fragment, one rule-10 completeness failure, two stale protocol-card status sections); 6 WARNs fixed, 1 open (column-boundary re-verification of citations into two-column source text); verdict PASS_WITH_LIMITS (K0; founder decisions pending; hidden_ai_fill_unmarked declared open).

## v0.4.1 (2026-09-05) — gate v4.1 summary
Scope: the founder-delegated decision build (rules 22/24/25, D-SCOPE-CONTEXT, H3 falsifier proxy sim, decided text blocks). One independent adversarial review pass by a different AI agent (I1: same operator, different agent) over the diff, 7 dimensions. 5 BLOCKs upheld and fixed: two stale "not yet built" claims against code shipped in the same diff (DAG yaml rule 24, P13 rule 22); CHANGELOG self-contradiction on which founder items remain pending (now the 4 Part-2 items only); a real kernel divergence (compute_disclaimers did not scan statement.translation.text while the scope-context check did — fixed, regression test added); a schema description promising suppression behaviour no code implements (global_south_exempt now labelled reserved/inert). 3 SHOULDs applied (rule 24 holdout caveat carried into CHANGELOG; route A 0/40 disclosed as guaranteed by corpus construction; NC-77 spec item clarified). Verdict PASS_WITH_LIMITS (K0; H3 stays Open — proxy only; rule 24 ERROR branch still owes an out-of-lexicon holdout; 4 Part-2 founder items pending).
