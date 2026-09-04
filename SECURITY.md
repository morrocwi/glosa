# Security Policy

## Scope

This repo is a public methodology, schema, template, and tooling
collection (no hosted service, no user data store). The realistic risk
classes are:

- A leaked local path, username, internal IP, session ID, or private-repo
  name accidentally committed from the author's own workstation.
- A real credential or token accidentally committed.
- A malicious pull request that tries to smuggle a prompt-injection payload
  into a file an AI assistant is likely to read and act on later (`AGENTS.md`,
  `CLAUDE.md`, `GEMINI.md`, `SKILL.md` files, `methodology/`, `schema/`
  examples).
- A supply-chain issue in `scripts/`, `cli/`, or `mcp/` code (a script that
  does something other than what it claims to do).

## Reporting a vulnerability or leak

**Do not open a public GitHub issue** for a suspected credential leak,
private-path leak, or personal-data leak — that would publicize the exact
thing being reported.

Instead:
1. If you can see the leaked material yourself right now on the public
   repo, note the exact file path and line, but do not quote the secret
   value itself anywhere public (including in a private report, if
   avoidable — describe it, e.g. "an AWS-shaped key at path X line Y").
2. Send the report to the author's public contact line listed in
   `.zenodo.json` / `CITATION.cff`.
3. Expect an acknowledgement and a fix (redaction + history consideration)
   before any public follow-up discussion of the specific finding.

For a suspicious pull request (payload aimed at an AI assistant reading
`AGENTS.md`-family files, or a script that does something undisclosed),
open a normal GitHub issue — this class of report does not itself leak
anything by being public, and public scrutiny is useful here.

## What this repo does NOT provide

- No bug bounty.
- No SLA on response time — this is a standalone-scholar project, not a
  funded security team.
- No claim that `scripts/check_leak.sh` / `scripts/check_forbidden_words.sh`
  provide complete coverage. They are a denylist-based readout, not a
  certification (see `RELEASE_CHECKLIST.md` R3). If you find a leak class
  the current denylist misses, that is itself a welcome report — see above.

## Handling of accepted reports

An accepted leak report results in: redaction/removal of the specific
content, an addition to `scripts/leak_denylist.txt` (generic pattern only,
never the specific secret value) to catch recurrence, and — if the leaked
material was ever pushed publicly — a note that git history may still
contain it until a history rewrite is performed (rewriting published git
history has its own costs; the founder decides whether/when to do this,
consistent with `AGENTS.md`'s human-holds-standpoint rule).
