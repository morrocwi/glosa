# glosa research registry

## The id rule

**One problem = one project = one id.** An id (`GLS-YYYY-NNN`) is assigned once, at intake
(`registry.py new`), and never reused or reassigned to a different problem. A project that forks
into several hypotheses (S3b/S3c, `design/FOUNDATION_v0.5.md` §2.2) still keeps one registry id —
the fork lives inside `hypothesis_refs`, not as separate registry rows.

## How stages advance

`spine_stage` moves forward through the same enum the spine itself uses (§2.2 of
`design/FOUNDATION_v0.5.md`): `problem → blackbox → lens_in → analysis → lens_out → lrs →
hypothesis_selected → genre_routed → method → paper_draft → review → released`. Advancing is done
by `tools/registry.py advance <id> <stage> --by human|ai|joint`, which appends a `history` entry —
it never overwrites or deletes a prior stage's record.

The state machine is **strict-forward, one step at a time** — `advance` refuses any target stage
that is not the immediate next stage after the entry's current `spine_stage`. Skipping stages
(e.g. `problem` straight to `method`) is refused with a "next legal stage is X" error; call
`advance` once per stage in sequence instead.

Three gates layer on top of that base rule:

- **`lrs` and every stage after it** (`lrs, hypothesis_selected, genre_routed, method,
  paper_draft, review, released`) require a `litreview_manifest_ref` — either already on the
  entry, or supplied with `--litreview-manifest-ref REF` on this call.
- **`--stub` is only a valid escape through `genre_routed`.** Passing `--stub` in place of a real
  ref works for `lrs`, `hypothesis_selected`, and `genre_routed` (and is itself logged as
  `stub: true` in the `history` row). For `method`, `paper_draft`, `review`, and `released`,
  `--stub` is refused outright — those stages require a real `litreview_manifest_ref`, no
  stubbing a paper or a release into existence.
- **`released` additionally requires `doi_version` set on the entry, and
  `registry/RELEASE_APPROVAL.txt` present and containing `APPROVED`** (founder sign-off; see
  `RELEASE_APPROVAL.txt.EXAMPLE`) — this is also the mechanism `RELEASE_CHECKLIST.md`'s R7
  ("Tag, publish, Zenodo") step is meant to call once a release actually ships.

`tools/registry.py check` audits every entry in `RESEARCH_REGISTRY.yaml` against all of the
above (transition legality of the full `history` sequence, litreview gating, stub-ceiling
placement, and the `released` requirements) and exits non-zero with a listed reason for each
entry that violates an invariant — this is the mechanism that catches a future hand-edit of the
YAML file bypassing `advance` entirely (see "MUST-10" in
`design/ARCHITECTURE_REVIEW_v1.md` / `reviews/ARCH_lifecycle.md` F3 for the incident this closes:
`GLS-2026-001` itself was once hand-edited to `paper_draft` with no ref and no `stub: true`, a
state `advance` itself refuses to produce — corrected in this file's own history on 2026-09-04).

## What the registry is NOT

- **Not a truth ledger.** An entry's `k_state`/`spine_stage`/DOI fields are readouts of what this
  tooling was told and observed — not a certification that the work is correct, complete, or
  reviewed. K-state discipline, tier tags, and PUB-ADVERSARIAL-REVIEW live in the spine itself
  (`design/FOUNDATION_v0.5.md`), not here.
  registry entry does not certify a claim, a paper, or a release — MIMCG / PUB-ADVERSARIAL-REVIEW
  still govern whether anything may ship.
- **Not a replacement for the Blackbox Note, Claim Card, or `litreview_manifest.yaml`.** Those
  documents carry the actual epistemic content; the registry only points at them (`blackbox_ref`,
  `hypothesis_refs`, `litreview_manifest_ref`) so a reader can find where each project's work
  actually lives.
- **Not append-only in every field.** Only `history` is append-only. Other fields (`spine_stage`,
  `k_state`, `doi_*`, `updated`) are overwritten in place to reflect current status; if you need the
  prior value, read `history`.

## Files

- `RESEARCH_REGISTRY.yaml` — the data (or `.json` fallback if PyYAML is unavailable; `registry.py`
  handles both transparently).
- `RELEASE_APPROVAL.txt.EXAMPLE` — template for the founder's publish-approval file (never commit
  the real `RELEASE_APPROVAL.txt` with `APPROVED` in it to a public branch without the founder
  having actually written it).
- `zenodo_state.json` — machine state written by `scripts/zenodo_deposit.py` (deposition id,
  prereserved DOI, conceptrecid, upload/publish status). Not hand-edited.
