# GLS-2026-006 — P02 intake: A Readout Problem for Fefferman's Navier-Stokes Equation

tier: Dr (specified; independently unreviewed at this intake stage — see maker-checker-gate for
the pending independent check before release/deposit)

## Two-question intake (P02)

**Q1 — what is the retained difference this issue names?**
Two founder-authored mathematical notes state and prove a small, self-contained finite fact
(exact commuting domain-translation + exact reader-factorization does NOT imply a finite-horizon
reader can decide an arbitrary domain question — Theorem 1 / Theorem 3.1, an 8-state witness) and
pose, without answering, a structurally analogous dichotomy for Fefferman's Navier-Stokes
breakdown predicate. The fuller companion additionally proves a genuinely new (to these notes)
global finite-interval continuation theorem for an already-Toledo-registered retained-turbulence
ODE (Theorem 6.1). The retained difference: these are currently two disconnected PDFs on a local
disk, unregistered in Toledo, unpublished, and not brought into this workspace's own equation
lineage or public-repo/release/Zenodo pipeline — that is the gap this intake closes.

**Q2 — who is affected versus who holds power?**
Affected: the founder (author, sole intellectual credit), and any future reader of the public
Fefferman/Navier-Stokes readout-problem literature who might otherwise not see this framing.
Power: the founder holds full authorial and release authority (Yaoharee Lahtee is the sole author;
no external co-author, no institutional gate). No third party's interests are affected by
registering or publishing this note — it names, but does not claim to resolve, the Clay Millennium
Problem, and cites only Fefferman's own official problem statement.

`zero_vs_bottom`: Toledo was checked (not skipped) for existing related work on both the finite-witness
theorem and the continuation theorem before either was registered as new — see
`toledo/registry/proposals/fefferman_readout_note.json`'s `origin`/`honest_caveats` fields. The
retained-turbulence equation itself was found already registered (`weld/P.05.v1`) and is cited
directly, not re-registered.

## What this intake does

1. Toledo-first check and registration (see `toledo/registry/proposals/fefferman_readout_note.json`
   and `toledo/docs/HANDOFF_fefferman_readout_problem_2026-09-09.md`).
2. This blackbox_note.yaml + this intake doc (P02 only — see `scope_decision_disclosed` in the
   blackbox note for why the full spine is not run).
3. A single merged arXiv-style LaTeX paper in the new repo
   a local working copy of the `readout-problem-navier-stokes` repository (not yet pushed to any remote).
4. A CLAIMS.md in that repo stating exactly what is and is not claimed, mirroring the source note's
   own Remark 2 non-claim boundary.

## What this intake explicitly does NOT do

- Does not run S1-S13 of the full glosa spine (no litreview manifest, no genre_decision, no
  claim_card, no dialogue_table).
- Does not claim any progress on the Clay Millennium Navier-Stokes problem itself. Both source
  documents and the merged paper state this explicitly and repeatedly (Remark 2 of the short note;
  Theorem 8.1/Corollary 8.2 framing of the fuller companion).
- Does not push to any git remote, cut a release, or deposit on Zenodo — those steps require the
  mandatory independent adversarial review (PUB-ADVERSARIAL-REVIEW) and maker-checker gate first,
  neither of which this intake session performed. See the handoff file for the exact next steps.
