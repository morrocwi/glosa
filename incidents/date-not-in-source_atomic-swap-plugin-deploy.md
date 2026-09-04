tier: Dr (specified; independently unreviewed)

# Atomic-swap plugin deploy incident (anonymized narrative)

## Source
**This incident is not named in the internal survey (local, not public) or `HANDOFF_2026-09-04_ultracode-
foundation-meeting.md`** — those two files do not carry it. It is included here because the task
requesting this file named it explicitly by title ("atomic-swap plugin deploy incident"), and the
only record of it available is a private, dated operational incident memory
(`feedback-atomic-swap-bulk-plugin-deploy`, private ANSE.ASIA workspace memory, 2026-07-24). Per
readout-not-truth and the "never invent" instruction, the date is stated exactly as recorded in
that memory (2026-07-24) rather than left blank, but the filename keeps the honest flag
`date-not-in-source` because neither of the two named source documents for this task (SURVEY/
HANDOFF) carries it — a reader following only those two files would not find this date confirmed
there. The affected site is a private ANSE.ASIA WordPress property; per this repo's standing rule
(private repos/sites are re-derived as patterns, never linked, `D-DERIVED-PATTERNS`), no domain,
path, or internal identifier is reproduced below.

## What happened [tier: finite_diagnostic (documented)]
A batch of outdated WordPress plugins was deployed to a live, traffic-serving site using a
single-connection FTP mirror tool that uploads a plugin's files one at a time, in whatever order
the local directory listing returns — an order that does not necessarily respect the plugin's own
internal file dependencies. For most (small) plugins in the batch this was harmless. For one large,
multi-file plugin, the upload took roughly 26 minutes; one file that referenced a class defined in
a different subdirectory finished uploading several minutes before that subdirectory itself
finished. During that window, the live site — still serving real traffic throughout the transfer —
received a request that loaded the newer file expecting a class that had not arrived yet, and threw
a real fatal error, caught by the site's own error monitor. A second, similarly large plugin in the
same batch showed an equally wide file-modification-time spread and carried the same risk, without
happening to be hit by a request during its own vulnerable window — a fact recorded explicitly as
luck, not safety. The same investigation separately found that the deploy script's own success
check piped the deploy tool's output through another command before checking the exit code,
which silently discarded the deploy tool's own real exit status rather than reporting it.

## What rule it produced [tier: Dr]
Generalized rule: a **live, multi-file deploy against a system that keeps serving traffic during
the transfer** must never write new files directly into the path being served. The fix is an
atomic swap — upload the complete new version to a separate, not-yet-served directory, verify the
upload is complete, then perform a single atomic rename operation to swap it into place. A
directory rename is a single filesystem operation with no partially-old-partially-new window; a
multi-file mirror onto a live path is not. In glosa terms, this generalizes beyond WordPress
specifically to any of glosa's own callable-layer operations that write multiple related files to a
location another process may read concurrently (e.g. writing a `litreview_manifest.yaml` alongside
the `citation_card.yaml` rows it references, or `glosa kg merge` rendering a repo-wide view from
several per-project files) — those operations should write to a temporary location and atomically
replace the target, never overwrite the live multi-file target file-by-file. The exit-code bug found
in the same investigation is a separate, general rule: **piping a command's output through another
command before checking the exit status silently discards the real exit code** — any glosa
kernel/CLI function that shells out to another tool must capture that tool's own exit status
directly (e.g. `${PIPESTATUS[0]}` in bash, or writing output to a file and checking the invoked
process's status separately), never rely on `$?` read after a pipeline when the piped-through
command's own exit status is what matters.

## What would have caught it earlier
A deploy-time rule requiring any target with more than a small, fixed number of interdependent
files (a rule of thumb: any plugin/theme with a subdirectory tree) to go through an
upload-to-new-directory-then-atomic-rename step, verified by comparing a file count/checksum
between the local and newly-uploaded copy before the rename — never a direct multi-file mirror onto
the live path. Separately, a standing rule that any script's own "did this succeed" check must be
tested against a deliberately-failing run at least once, to confirm the check can actually detect a
failure and is not silently reading the wrong command's exit status (the same shape as the
`check_docs` silent-pass incident above: a check that has never been exercised against its own
failure case is unverified as a check).

## Non-collapse pairs this incident illustrates
- No Appendix A pair maps directly onto "atomic operation ≠ sequence of individually-successful
  operations" or "a pipeline's final exit code ≠ the exit code of the command that actually matters
  in it" — both are flagged here as open gaps for a future Appendix A addition rather than forced
  onto an unrelated pair.
