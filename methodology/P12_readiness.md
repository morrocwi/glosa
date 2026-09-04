# P12 — Readiness

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction; AI drafted this card,
> narrating this workspace's own `project-onboard` gate pattern for glosa's own repo. Comparison
> language is same/different/cited only.

## id

`P12`

## Rule

Before any work begins inside a project directory this session has not already onboarded into
during the current session — a new problem/project, a repo not yet read this session, resuming
after a gap — produce a **Readiness Report** before touching any code or claim card:

1. **Overview** — what this project is, in one paragraph, read from `CLAIM_BOUNDARY.md`/the
   project skeleton (`templates/knowledge/project_skeleton.md`), not invented.
2. **Tools/context loaded** — which methodology cards (`P0`–`P15`), schemas, and templates were
   actually read this session before starting, named explicitly (not "the usual ones").
3. **100% status**, in three buckets, each populated or explicitly empty:
   - **Blockers** — anything that must be resolved before work can proceed at all (a missing
     `human_owner`, an unresolved SCRAM, a license question).
   - **Negatives** — known gaps, open items, unresolved must-fixes already on file for this
     project (read from its own honest-edges section, not silently dropped).
   - **Positives** — what is already in a usable, current state for this project.

The report is written **before** any file is created or edited in the project, fail-closed: no
readiness report, no work.

## Why / incident

Standing rule in this founder's workspace (`feedback-project-onboard-gate`): entering a new repo
or project without first producing this report has previously led to work proceeding on stale or
incomplete context — the report exists specifically to force a session to state what it actually
knows and does not know about a project's current state *before* it acts, rather than discovering
gaps mid-task. glosa's own `S14` literature-review system independently converges on the same
shape at hypothesis-selection time (`hypothesis_selection.yaml`'s comparison table, §6) —
readiness-before-action is the same discipline applied one level up, at project-entry time.

## Inputs → outputs

- **Inputs:** the project's `CLAIM_BOUNDARY.md`/skeleton, its existing claim cards and their
  `revision_history`, its own honest-edges/open-items section (if any exists yet), the
  methodology cards relevant to the task at hand.
- **Outputs:** a Readiness Report (a file or a message, per the calling context) with the three
  named sections above, and — where the project is new — a `templates/knowledge/
  project_skeleton.md` instance if one does not already exist.

## Gate

No claim card, code change, or file write proceeds inside a project until its Readiness Report
exists for the current session. A report that leaves the Blockers section silently empty without
having actually checked for blockers (rather than genuinely finding none) is itself a violation of
this card's own rule 3 (`NC-26`, "not checked" ≠ "checked, nothing found," applied to the report's
own completeness).

## Human / AI split

Human: confirms the report's Overview actually matches the project as they understand it, and is
the one who resolves any named Blocker. AI: drafts the report from the project's own files,
performs the mechanical checks (which files exist, which cards are `Draft` vs `Approved-for-*`),
and states plainly which parts of the report are read from the project's own record versus
inferred.

## Disclaimers

`D-CANDIDATE-STATUS` (any project state named as a Positive that has not itself cleared an
independent check), `D-STANDPOINT` (the report states whose standpoint it is written from), `D-
NONCLAIM` (the report does not claim completeness beyond what was actually read).

## NC pairs

`NC-26` "not checked" ≠ "checked, nothing found" (A2) · `NC-27` LOCAL_EVIDENCE_NOT_FOUND ≠ NO_
LOCAL_EVIDENCE_EXISTS (a project with no yet-discovered blockers is not the same statement as a
project confirmed blocker-free) · `NC-53` No human available ≠ Research stop.

## Not-do

- Do not begin editing a project's files before its Readiness Report exists for this session.
- Do not report "no blockers" without having actually checked the project's own open-items
  record.
- Do not reuse a stale readiness report from a previous session without re-checking it against
  the project's current state (a project may have changed since).
- Do not let the Readiness Report substitute for `P2`'s own intake gate on a specific new
  problem — readiness is project-entry; intake is problem-entry; they answer different questions.

## Tier

Dr (specified; independently unreviewed).
