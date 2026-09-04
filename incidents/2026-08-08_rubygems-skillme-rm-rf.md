tier: Dr (specified; independently unreviewed)

# rubygems skillme rm -rf — 2026-08-08

## Source
the internal survey (local, not public) §B, `skillme` entry: "Incident: rubygems 'skillme' with `rm -rf
~/.claude/skills` pre_uninstall (2026-08-08)."

## What happened [tier: finite_diagnostic (documented)]
The workspace's own internal skill and repo are named `skillme` (`~/ANSE.ASIA/skillme`). On
2026-08-08 it was found that a **separate, unrelated package** published on rubygems.org also uses
the name `skillme`, and that package's `pre_uninstall` hook runs `rm -rf ~/.claude/skills` — a
destructive, unscoped delete of the entire local Claude skills directory, triggered merely by
uninstalling that gem, regardless of what it actually does while installed. The two `skillme`s
share nothing except the name; the rubygems package is not derived from, related to, or a fork of
this workspace's internal skill.

## What rule it produced [tier: Dr]
A name collision between an internal artifact and an external package is not a naming
inconvenience — it is an attack/mistake surface, because a human or an automated tool searching by
name has no way to distinguish them until it reads the package contents. Generalized rule for
glosa's `skill-library` vetting flow (already the internal-first / external-vetted separation this
repo re-derives, `SKILL-INTERNAL-FIRST` pattern): **vet by artifact content and package identity
(exact source URL, maintainer, checksum), never by name alone**, and treat any install/uninstall
hook in a third-party package as a red flag requiring explicit read-through before it is ever run —
`VETTING_PROTOCOL.md`'s "read entire thing before trusting, regardless of reputation" rule applies
with full force to lifecycle hooks specifically, since those execute with no further confirmation
at install or removal time.

## What would have caught it earlier
A pre-install/pre-uninstall hook scan as a mandatory step of any external-package vetting pass —
grep the package manifest for `pre_install`/`post_install`/`pre_uninstall`/`post_uninstall` (or the
ecosystem's equivalent) and read every matched script in full before installing anything with a
name that matches, or nearly matches, an internal artifact's name. This is the same discipline
`OPS-LIVE-AUTH-STOP`-style rules apply to credentials — treat anything that executes automatically
and irreversibly (a destructive shell command, an auth retry) as requiring a stop-and-verify step
before it runs, not after.

## Non-collapse pairs this incident illustrates
- No listed Appendix A pair maps directly onto "package name ≠ package identity" — this is flagged
  here as an open gap rather than forced onto an existing pair; a future revision may add it to
  Appendix A Family B (Access/Inference) as a named non-collapse pair if the repo's maintainers
  judge it recurring enough to warrant one.
