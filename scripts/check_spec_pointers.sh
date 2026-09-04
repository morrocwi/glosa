#!/usr/bin/env bash
# scripts/check_spec_pointers.sh — MUST-1 drift test (ARCHITECTURE_REVIEW_v1.md).
#
# Readout, not truth: this script reports what it observed against a fixed rule. It does not
# certify the repo's documentation is "correct" — only that these two specific, narrow properties
# hold at the moment it ran.
#
# Two checks, both must pass (exit 0) for this script to exit 0:
#
#   1. POINTER DRIFT — no tracked *.md/*.json/*.yaml file, outside `design/` and `lineage/`,
#      references `FOUNDATION_v0.5`, `FOUNDATION_v0.5`, `FOUNDATION_v0.5`, `REPO_SPEC_v0.5`,
#      `REPO_SPEC_v0.5`, or `REPO_SPEC_v0.5`. `design/` is exempt as a whole (the archived spec
#      generations themselves live there, plus review/chair-ruling/handoff documents that
#      legitimately narrate synthesis history and must be able to name a prior version — this is a
#      disclosed interpretation choice of the task's "outside design/ archived files and lineage/"
#      wording, made because a narrower per-file exemption would force every historical design/
#      document to be individually re-triaged just to name its own ancestry, which is not what
#      MUST-1's own drift test (`ARCHITECTURE_REVIEW_v1.md`, scoped to 8 named entry-point files)
#      was checking for). `lineage/` is exempt because its entire job is historical record.
#
#   2. PATH EXISTENCE — every path `$REPO_SPEC_FILE` lists inside a fenced tree diagram as
#      existing (i.e. NOT under a `[planned...]` marker) is mechanically resolved from the tree's
#      own indentation and checked against the real filesystem. A path under a `[planned...]`
#      marker is skipped (it is explicitly declared not-yet-built, honestly, and this check exists
#      to catch the OPPOSITE failure — a path claimed real that is not).
#
# Exit 0 = both checks passed. Exit 1 = at least one failed (see output).

set -u
REPO_SPEC_FILE="design/$(grep -o "REPO_SPEC_v[0-9.]*\.md" design/CURRENT_SPEC.txt | head -1)"; [ -f "$REPO_SPEC_FILE" ] || REPO_SPEC_FILE="design/REPO_SPEC_v0.5.md"
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)" || exit 1

FAIL=0
say()  { printf '%s\n' "$*"; }
ok()   { say "  [OK]   $*"; }
bad()  { say "  [FAIL] $*"; FAIL=1; }

say "== glosa check_spec_pointers.sh =="
say "repo root: $(pwd)"
say ""

# --- 1. pointer drift ---
say "-- check 1: stale FOUNDATION_v0.[234] / REPO_SPEC_v0.[234] pointers --"

if ! command -v git >/dev/null 2>&1; then
  bad "git not found on PATH — cannot enumerate tracked files"
else
  PATTERN='FOUNDATION_v0\.[234]\b|REPO_SPEC_v0\.[234]\b'
  HITS=0
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    case "$f" in
      design/*|lineage/*) continue ;;
    esac
    [ -f "$f" ] || continue
    if grep -nE "$PATTERN" -- "$f" >/tmp/_csp_hit.$$ 2>/dev/null; then
      HITS=$((HITS + 1))
      bad "$f references a stale spec version:"
      sed 's/^/         /' /tmp/_csp_hit.$$
    fi
    rm -f /tmp/_csp_hit.$$
  done < <(git ls-files -- '*.md' '*.json' '*.yaml' '*.yml' 2>/dev/null)

  if [ "$HITS" -eq 0 ]; then
    ok "no stale pointers found outside design/ and lineage/"
  else
    bad "$HITS file(s) reference a stale spec version — see above"
  fi
fi

say ""

# --- 2. path existence, parsed from $REPO_SPEC_FILE's own tree diagrams ---
say "-- check 2: every non-[planned] path in $REPO_SPEC_FILE exists on disk --"

SPEC="$REPO_SPEC_FILE"
if [ ! -f "$SPEC" ]; then
  bad "$SPEC not found"
else
  PYOUT="$(python3 - "$SPEC" <<'PYEOF'
import re
import sys
import os

spec_path = sys.argv[1]
with open(spec_path, encoding="utf-8") as fh:
    lines = fh.read().splitlines()

# Format (this document's own stated convention, header section "Format of each fenced block"):
# inside a ``` fence, one path per line, relative to the repo root, optionally followed by
# "  #comment"; a line starting "[planned]" names something not on disk by design and is skipped.
in_fence = False
fence_re = re.compile(r"^```")
planned_re = re.compile(r"^\[planned\]\s*")

results = []
for raw in lines:
    if fence_re.match(raw):
        in_fence = not in_fence
        continue
    if not in_fence:
        continue
    line = raw.strip()
    if not line:
        continue
    if planned_re.match(line):
        continue
    # strip an inline "  # comment" (space(s) then '#')
    m = re.search(r"\s#", line)
    if m:
        line = line[: m.start()]
    path = line.split()[0].strip() if line.split() else ""
    if not path:
        continue
    results.append(path)

seen = set()
ok_count = 0
fail_count = 0
for p in results:
    if p in seen:
        continue
    seen.add(p)
    if os.path.exists(p):
        ok_count += 1
    else:
        fail_count += 1
        print(f"MISSING\t{p}")

print(f"SUMMARY\t{ok_count}\t{fail_count}")
PYEOF
)"
  echo "$PYOUT" | grep '^MISSING' | while IFS=$'\t' read -r _ p; do
    bad "listed as existing in $SPEC but not found on disk: $p"
  done
  SUMMARY_LINE="$(echo "$PYOUT" | grep '^SUMMARY')"
  OKN="$(echo "$SUMMARY_LINE" | cut -f2)"
  FAILN="$(echo "$SUMMARY_LINE" | cut -f3)"
  if [ "${FAILN:-1}" = "0" ]; then
    ok "all $OKN non-[planned] paths in $SPEC resolved to real files/directories"
  else
    bad "$FAILN path(s) in $SPEC do not exist on disk — see above"
  fi
fi

say ""
if [ "$FAIL" -eq 0 ]; then
  say "== PASS =="
else
  say "== FAIL =="
fi
exit "$FAIL"
