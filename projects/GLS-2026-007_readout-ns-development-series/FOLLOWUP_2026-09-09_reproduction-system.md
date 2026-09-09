# GLS-2026-007 — follow-up note, 2026-09-09

**This note is an ADDITION, not a correction.** `INTAKE.md` and `blackbox_note.yaml` stand
as written and describe accurately what had and had not been done at P02-intake time
(2026-09-09, earlier the same day): only Volume 1 read, no Toledo lookup, no duplication
check, no reading of Volumes 2-6. Nothing in those two files is being overwritten.

## What changed since intake

Per founder instruction ("ทำ ระบบ reproduc ระดับโลก" — build a world-class reproduction
system), scoped by the founder's own follow-up to: the Navier-Stokes readout series
(GLS-2026-006 + this project, GLS-2026-007) — one-command verification of every checkable
claim across both, with an auto-regenerated ledger.

1. **Volumes 2-6 have now been read** (previously only Volume 1 was read at intake).
2. **A one-command reproduction system was built** in
   `readout-problem-navier-stokes/reproduction/` (Python check scripts per volume,
   an auto-generated `LEDGER.json`/`LEDGER.md`, `reproduce_all.sh`), tiering all 80
   identified claims across the 6 volumes as `Th_coqc` / `finite_diagnostic` / `Dr` /
   `Open` per this workspace's IDM discipline. 27 of 80 claims are mechanically checkable
   and PASS; 44 are `Dr` (standard derived mathematics, not mechanically checkable); 8 are
   `Open` (explicitly posed-not-answered, including NSR-02/03/04); 1 is a cross-reference
   note. Full detail: `readout-problem-navier-stokes/reproduction/README.md` and
   `BUILD_STATUS.md`.
3. **The Volume-2-vs-GLS-2026-006 open question from intake is now resolved**: `diff -u`
   between the extracted Volume 2 text (pp.16-23 of the combined PDF) and the
   `State_Breakdown_Math_Only_v0_2.pdf` text GLS-2026-006's own repo was built from found
   them **identical in body content**, differing only by a trailing-newline `pdftotext`
   extraction artifact. Volume 2's finite witness (its Theorem 3.1) and GLS-2026-006's own
   published witness claim are the SAME artifact, not two independent ones. No founder
   decision is needed on this point — there is no discrepancy to decide between.
4. **Three internal cross-reference slips were found in the source PDFs' own proof text**
   (Volume 2 Theorem 11.1's proof cites a nonexistent "Theorem 9.1" and a nonexistent
   "Proposition 11.1"; Volume 6 Theorem 6.1's proof cites a nonexistent "Theorem 2.1" and
   appears to conflate two other theorems). These do not affect the mechanical checks
   (which check the finite mathematics directly, not the prose's own citations) and are
   flagged, not silently fixed, in `reproduction/LEDGER.json`/`LEDGER.md` and
   `BUILD_STATUS.md`, for the founder/author to correct in a future revision of the source
   PDF.
5. **One genuine reproducibility gap remains, documented not hidden**: Volume 2 Section
   13's worked numerical example does not specify the exact forcing vector `G_R` /
   initial condition used to generate its published error table; the reproduction system
   verifies the underlying `O(h)` convergence claim with an explicit substitute instead of
   the paper's exact numbers. See `reproduction/README.md` for detail.

## What is still NOT done (still deferred, per intake's own scope statement)

- No Toledo lookup or duplication check has been run for Volume 1's NSR-01/02/03/04
  proposals, nor for anything else across the 6 volumes.
- No comparison of Volume 1's NSR-01 against GLS-2026-006's already-published
  `PROP-NS-WITNESS-01`/`PROP-NS-CONTINUATION-01` for overlap or conflict.
- No paper has been drafted from this series; no Zenodo action taken for GLS-2026-007
  itself. `spine_stage` for this project remains `intake` (P02-only) plus this
  reproduction-system addendum — it has not advanced to a full glosa spine pass.
- Volumes 3-6's `Assumption 1.1` (that a real Navier-Stokes solution with a genuine H^3
  continuum breakdown and a real finite-energy weak continuation past it actually exists)
  remains an open, unverified standing assumption — the reproduction system records this
  as `Open`/`Dr`, it does not and cannot resolve it.

## Where the work lives

- Reproduction system: `readout-problem-navier-stokes/reproduction/` (repo:
  `github.com/morrocwi/readout-problem-navier-stokes`).
- This note's companion repo-side documentation: `reproduction/README.md`,
  `reproduction/BUILD_STATUS.md`.
