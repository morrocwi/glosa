#!/usr/bin/env python3
"""scripts/check_non_collapse.py — non-collapse (ownership-phrasing) WARN-only checker.

tier: finite_diagnostic (this script's own exit code / printed lines are the readout; read
stdout, do not take this docstring's word for it).

Provenance: `design/ARCHITECTURE_FIRST_REVIEW_PROPOSAL_v0.2.md` §3d/§8-R4 (founder-delegated
resolution R4, 2026-09-23). §3d's non-collapse gate says a row or sentence that makes a literature
strand the OWNER or SOURCE of an architecture node's mechanism (e.g. "N2 is a PID controller",
"[node] ← [theory]") is a failure this repo should be able to flag mechanically, the same way
`scripts/check_forbidden_words.sh` flags banned vocabulary. R4 explicitly scopes this as
**WARN-only**: this script never fails a gate on its own — it surfaces candidate ownership/
subtraction phrasing for a HUMAN to read and dispose of (keep, reword, or mark false-positive).
The human's disposition is recorded wherever that human records it (a review packet, a PR
comment, a Blackbox Note) — this script does not record dispositions itself.

What it checks: for each given path (markdown or YAML — any UTF-8 text file), every line is
matched, case-insensitively, against a fixed list of ownership/subtraction patterns (English and
Thai — loaded from `design/non_collapse_patterns.json`, see PATTERNS below). A hit prints:

    WARN <path>:<line>: matched '<pattern>' : <excerpt>

Exit codes:
  0 — ran cleanly (default, or `--strict` with no hits and no IO errors).
  1 — `--strict` was passed AND at least one line matched a pattern (no IO errors).
  2 — usage error (no paths given), OR `--strict` was passed AND at least one given path was
      missing/not a file/not readable as UTF-8 text. Without `--strict`, an unreadable or missing
      path is instead a warn-and-continue: it prints `[ERROR]`/`[SKIP]` and the run still exits 0
      (matching R4's "never auto-fails a gate" instruction for normal, non-strict use).
`--strict` exists for a future opt-in CI lane that wants a hard gate; it is never invoked by
default.

Meta-section skip: a Markdown heading line (`#`, `##`, ... `######`) whose text contains the
literal marker `<!-- non-collapse:meta -->` opens a skipped region. Every line after that heading
is skipped (not scanned) until the next heading of the SAME level or SHALLOWER (fewer or equal
`#` characters) is reached, or end of file. This lets a document keep a section that DISCUSSES
forbidden ownership phrasing (a forbidden-phrases table, a worked "wrong vs. right" example, this
script's own docstring quoted into a design doc) without every quoted example itself becoming a
WARN hit. A meta heading marker on a non-heading line, or a marker with no following heading
change, is not recognized as a section boundary — only a `#`-prefixed line carrying the marker
opens a region, and only a `#`-prefixed line of equal-or-shallower depth closes it.

Fenced code blocks (``` or ~~~, 3+ of the same character opening a line, optionally with a
trailing info-string): a `#`-prefixed line INSIDE a fence is never treated as a heading — it
cannot open or close a meta-skip region, since it is code/quoted text, not real document
structure. Phrase matching still runs on fenced lines exactly as on any other line (a fence is
not itself a meta-skip mechanism) — if a fence is being used to show an example of forbidden
phrasing, wrap it in a real `<!-- non-collapse:meta -->` heading section as usual to skip it.

Usage:
    python3 scripts/check_non_collapse.py <path> [<path> ...] [--strict]

stdlib-only (json from the standard library is used to load the pattern-data file). No network.
Run directly, or point it at a proposal/review file before publish.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Pattern data (label, regex-string pairs) lives in design/non_collapse_patterns.json, not as
# literal string constants in this file — scripts/check_forbidden_words.sh's overclaim-vocabulary
# gate (AGENTS.md rule 6) would otherwise fail on this script's own source every time it is
# self-scanned, since a couple of the pattern labels/regexes below are themselves drawn from that
# same forbidden-vocabulary family. Path prefixes already exempted for that reason (per
# scripts/forbidden_words_allowlist.txt) include design/, which is why the data lives there
# instead of here.
_PATTERNS_DATA_PATH = Path(__file__).resolve().parent.parent / "design" / "non_collapse_patterns.json"


def _load_raw_patterns(path: Path = _PATTERNS_DATA_PATH):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return [(label, pat) for label, pat in data["patterns"]]


_RAW_PATTERNS = _load_raw_patterns()

PATTERNS = [(label, re.compile(pat, re.IGNORECASE)) for label, pat in _RAW_PATTERNS]

_HEADING_RE = re.compile(r"^(#{1,6})\s")
_META_MARKER = "<!-- non-collapse:meta -->"
_FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


def _heading_level(line: str):
    m = _HEADING_RE.match(line)
    return len(m.group(1)) if m else None


def scan_text(path_label: str, text: str):
    """Yield (path_label, lineno, pattern_label, excerpt) for every match outside a
    non-collapse:meta-skipped region. A `#`-prefixed line inside a fenced code block (``` or ~~~)
    is never treated as a heading, so it can never open or close a meta-skip region; it is still
    scanned for phrase matches like any other line."""
    skip_level = None  # None = not skipping; int = skipping until a heading of this level or shallower
    in_fence = False
    fence_char = None  # the fence character ("`" or "~") a closing fence must match
    fence_len = None  # the opening fence's run length -- a closing fence must be >= this long
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        fence_m = _FENCE_RE.match(stripped)
        if fence_m:
            marker = fence_m.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
            elif (
                marker[0] == fence_char
                and len(marker) >= fence_len
                and stripped[len(marker):].strip() == ""
                # a closing fence must be the same character, at least as long as the opening
                # fence, and followed only by whitespace (no trailing info-string/text) -- a
                # shorter run, or a marker with trailing text, does not close the fence.
            ):
                in_fence = False
                fence_char = None
                fence_len = None
            # a fence delimiter line itself is not a heading; fall through to phrase scanning below

        level = None if in_fence else _heading_level(line)

        if skip_level is not None:
            if level is not None and level <= skip_level:
                skip_level = None  # boundary reached; this line itself is evaluated below
            else:
                continue  # still inside the skipped meta section
        if level is not None and _META_MARKER in line:
            skip_level = level
            continue  # the meta heading line itself is never scanned

        for label, rx in PATTERNS:
            m = rx.search(line)
            if m:
                excerpt = line.strip()
                if len(excerpt) > 160:
                    excerpt = excerpt[:157] + "..."
                yield (path_label, lineno, label, excerpt)


def check_paths(paths):
    """Return (hits, errors). hits: list of (path, lineno, label, excerpt) tuples across all given
    paths. errors: list of (path, reason) tuples for paths that were missing/not a file/not
    readable as UTF-8 text — the caller decides whether an error is fatal (--strict) or just a
    warn-and-continue (default)."""
    hits = []
    errors = []
    for p in paths:
        pp = Path(p)
        if not pp.is_file():
            print(f"[ERROR] not a file: {p}")
            errors.append((p, "not a file"))
            continue
        try:
            text = pp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"[SKIP] not UTF-8 text: {p}")
            errors.append((p, "not UTF-8 text"))
            continue
        except OSError as exc:
            print(f"[ERROR] cannot read {p}: {exc}")
            errors.append((p, str(exc)))
            continue
        for hit in scan_text(str(p), text):
            hits.append(hit)
    return hits, errors


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    strict = "--strict" in argv
    paths = [a for a in argv if a != "--strict"]

    if not paths:
        print(__doc__)
        return 2

    hits, errors = check_paths(paths)
    for path, lineno, label, excerpt in hits:
        print(f"WARN {path}:{lineno}: matched '{label}' : {excerpt}")

    print(f"\ncheck_non_collapse: {len(hits)} candidate ownership/subtraction phrase(s) found "
          f"across {len(paths)} path(s)")

    if strict and errors:
        print(f"check_non_collapse: --strict: {len(errors)} unreadable/missing path(s) "
              f"(usage/IO error) — see [ERROR]/[SKIP] lines above", file=sys.stderr)
        return 2

    if strict and hits:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
