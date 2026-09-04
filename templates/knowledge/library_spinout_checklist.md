# Sub-library spin-out checklist — RWI S8 template (Dr, unreviewed)

> Rule: when a mechanism (proof technique, computational method, reusable schema/checker) is
> reused by TWO OR MORE projects, spin it out into its own library. It does not stay
> duplicated inline, and it does not stay informally "the code project A also lends to
> project B." See `S8_knowledge-infrastructure.md` §5 for the layout pattern (inspected
> directly from `finite-readout-acceleration`, `retained-sturm`, `zero-readout-certifies`).

## Trigger

- [ ] Confirmed used by **two or more** projects. Name both/all project ids here:
      _______________

## Minimum bar before extraction

1. [ ] Own `README.md` stating the mechanism's scope and tier independent of any one
       consuming project.
2. [ ] Own `LICENSE` (and, if code and prose/paper license differently, a
       `LICENSE-TEXT.md` + `LICENSES.md` split — zero-readout-certifies pattern).
3. [ ] Own `CITATION.cff` if the library backs a citable claim/result. (Not strictly required
       for pure internal tooling with no citable result — e.g. `finite-readout-acceleration`
       ships without one — but add one once any external project might cite it as a method.)
4. [ ] Own verification layer — EITHER:
       - a `tests/` suite (engineering-mechanism shape), OR
       - a formal-verification directory (`coq/`, `formal/`) plus a reproduction doc
         (`REPRODUCE.md` or equivalent) (formal/proof-claim shape).
5. [ ] Own tier ledger — a `TIER_LEDGER.md` or `CLAIM_MATRIX.md` stating what tier each of the
       library's own claims carries, independent of whatever tier a consuming project assigns
       to its own use of it.
6. [ ] `CHANGELOG.md` present (every inspected pattern library has one).
7. [ ] Both/all consuming projects updated: their `kg/edges.jsonl` now has a `borrows` (or
       `derives_from`, if the project shows its own derivation from the library's result) edge
       pointing at the new library's `project`-type kg node — old inline copies of the
       mechanism deleted from each consuming project, not left as a second silent source of
       truth.
8. [ ] A decision row logged (RWI's own `DECISIONS.md`, matching the workspace-wide rule that
       a decision is not done until it is a logged row) recording: what was spun out, from
       which projects, and the new library's name/location.

## Layout reference (top-level, inspected 2026-09-04)

| | finite-readout-acceleration | retained-sturm | zero-readout-certifies |
|---|---|---|---|
| README / CHANGELOG / LICENSE | yes | yes | yes (+ LICENSE-TEXT.md + LICENSES.md split) |
| CITATION.cff | no (tooling, no citable result) | yes | yes |
| verification layer | `tests/` + `formal/` | `paper/` + `benchmarks/` (no `tests/`) | `coq/` + `paper/` + `REPRODUCE.md` (no `tests/`) |
| other | `examples/`, `DESIGN_NOTES.md` | `docs/`, `environment/`, `patches/` | `Makefile`, `Dockerfile`, `SECURITY.md`, `SUPPORT.md`, `codemeta.json`, `scripts/` |

Both verification-layer shapes are legitimate — choose based on what the library's own claim
type actually is (engineering tool → tests; formal/proof or benchmark result → formal +
reproduction docs).
