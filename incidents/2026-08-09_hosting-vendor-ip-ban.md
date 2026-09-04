tier: Dr (specified; independently unreviewed)

# <hosting-vendor> IP ban — 2026-08-09

## Source
the internal survey (local, not public) §B lists `safe-live-connect` and the workspace's governance/process skills
among the sources folded into this repo's foundation; the incident itself is documented in the
workspace's own binding operational-safety rule (`OPS-LIVE-AUTH-STOP`, `~/.claude/CLAUDE.md`), the
gate file every session in this workspace enters through, cited here as the incident record for a
live-operations rule already generalized once (into `safe-live-connect`) and now generalized again
for glosa's own release/publish discipline. No repository code or credentials are reproduced below.

## What happened [tier: finite_diagnostic (documented)]
On 2026-08-09, while working on a hosting account on the shared server `<hosting-vendor>`, an automated
session attempted authentication against a live host (FTP, WordPress admin login, and remote MySQL)
using credentials parsed from a stale internal file rather than the canonical, current credential
source. Several of these attempts used wrong values — including, in one case, a username mistaken
for a password. Multiple failed login attempts occurred within a few minutes, across more than one
protocol, against the same server. The server's own intrusion-prevention system banned the
session's public IP address at the **whole-server firewall level** — not scoped to the one hosting
account being touched. Because several unrelated sites and a hosting control panel shared that one
physical server (different accounts, same machine), the ban took all of them offline simultaneously,
including sites that had not been touched at all during the incident. The correct credentials were
obtained only after the ban was already in effect, and were unusable until the ban was lifted.

## What rule it produced [tier: Dr]
Generalized into `OPS-LIVE-AUTH-STOP`: **never retry authentication against a live/production host
with unverified or parsed-from-a-file credentials; stop after the first failure.** For glosa, the
directly relevant generalization is at the release-gate level rather than the hosting level: any
action against a **live, shared, externally-visible system** — a publish, a push to a shared
remote, an API call against a rate-limited or ban-capable service — must be treated as having a
blast radius that may exceed the one target being acted on, and a failed first attempt is a signal
to stop and verify, not a signal to retry with a variant. This is the same shape as `PUB-
ADVERSARIAL-REVIEW`'s leak-scan discipline (a check that must run before the action, not be
diagnosed after the fact) and the same shape as the Query Stop Rule in the DVP mechanics (§4.3,
`design/FOUNDATION_v0.5.md`) — "one recorded attempt per acceptance-criteria version; re-asking
until a route agrees is a named SCRAM condition" — both are instances of a single general rule: a
repeated attempt against a system that can react adversarially to repetition is itself the risk,
independent of whether any single attempt looks harmless.

## What would have caught it earlier
Treating "credential file may be stale" as a hard stop-and-confirm gate before the *first*
authentication attempt, not only after a failure — the canonical-credential-source rule (a single
named, current source of truth for live credentials, never a repo file) closes exactly this gap.
For glosa's own callable layer (§9), the same discipline generalizes to: any CLI/MCP function that
calls an external, rate-limited, or ban-capable service (a DOI/Crossref/OpenAlex lookup for citation
verification, a Zenodo publish call) should hard-stop and surface the failure to a human after one
failed attempt, rather than silently retrying with backoff against a target that might interpret
retries as abuse.

## Non-collapse pairs this incident illustrates
- No Appendix A pair maps directly onto "one target's blast radius ≠ the whole shared system's
  blast radius" — recorded here as an open gap for a future Appendix A addition rather than forced
  onto an unrelated pair, consistent with this repo's own rule that the non-collapse table is
  append-only and grows only when a real recurring case names a genuinely new pair.
