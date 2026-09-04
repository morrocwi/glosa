#!/usr/bin/env bash
# scripts/check_leak.sh — glosa privacy/security leak scan.
#
# Readout, not truth: this is a grep-based scan against
# scripts/leak_denylist.txt (safe generic patterns, no real secrets). It
# finds candidate leaks in TRACKED files. A hit is a finding to review, not
# an automatic proof of a real leak (false positives happen, e.g. inside a
# schema example or a design doc that discusses the pattern itself), and a
# clean run is not proof of "no leak" (only proof this denylist found none).
#
# Also flags: the author's own email appearing OUTSIDE an explicit allowed
# public author-attribution context is NOT specially exempted here — the
# PUB-ADVERSARIAL-REVIEW rule requires a human to confirm any email line is
# the author's own intended public line before publish. This script reports
# every email match; a human/independent reviewer decides which are fine.
#
# Exit 0 = no denylist pattern matched in any tracked file.
# Exit 1 = at least one match found (see output for exact file:line).

set -u
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)" || exit 1

DENYLIST="scripts/leak_denylist.txt"
LOCAL_DENYLIST="scripts/leak_denylist.local.txt"  # git-ignored; merged when present
if [ -f "$LOCAL_DENYLIST" ]; then MERGED="$(mktemp)"; cat "$DENYLIST" "$LOCAL_DENYLIST" > "$MERGED"; DENYLIST="$MERGED"; fi
FAIL=0

say() { printf '%s\n' "$*"; }

say "== glosa check_leak.sh =="
say "repo root: $(pwd)"
say "denylist: $DENYLIST"
say ""

if [ ! -f "$DENYLIST" ]; then
  say "  [FAIL] denylist file $DENYLIST not found"
  exit 1
fi

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  say "  [FAIL] not inside a git repository — cannot enumerate tracked files"
  exit 1
fi

# Build the list of tracked, text-ish files (skip this script and the
# denylist itself, since they necessarily contain the patterns as literal
# pattern text, and skip binary files).
mapfile -t TRACKED < <(git ls-files)

TMP_FILELIST="$(mktemp)"; PATFILE="$(mktemp)"
trap 'rm -f "$TMP_FILELIST" "$PATFILE"' EXIT
for f in "${TRACKED[@]}"; do
  case "$f" in
    scripts/check_leak.sh|scripts/leak_denylist.txt|scripts/leak_denylist.local.txt) continue ;;
  esac
  [ -f "$f" ] && printf '%s\n' "$f" >> "$TMP_FILELIST"
done
# Load patterns (skip blank lines and comments) into one file for a single-pass grep.
grep -vE '^\s*(#|$)' "$DENYLIST" > "$PATFILE"
NPAT="$(wc -l < "$PATFILE" | tr -d ' ')"
say "-- scanning $(wc -l < "$TMP_FILELIST" | tr -d ' ') tracked files against $NPAT patterns (single pass; binaries skipped by grep -I) --"
say ""
HITS=0
# One grep over every file (-I skips binaries); then attribute each hit line to its pattern(s).
MATCHED="$(tr '\n' '\0' < "$TMP_FILELIST" | xargs -0 grep -inHIE -f "$PATFILE" -- 2>/dev/null || true)"
if [ -n "$MATCHED" ]; then
  while IFS= read -r m; do
    [ -z "$m" ] && continue
    line="${m#*:}"; line="${line#*:}"
    pat="$(while IFS= read -r pt; do printf '%s' "$line" | grep -iqE -- "$pt" && { printf '%s' "$pt"; break; }; done < "$PATFILE")"
    say "  [FOUND] $m  (pattern: $pat)"
    HITS=$((HITS + 1)); FAIL=1
  done <<< "$MATCHED"
fi

# Author's-own-email allow check: separately report every email match so a
# human can confirm which lines (if any) are the intended public author line.
say ""
say "-- email addresses found (for human confirmation, not auto-failed) --"
EMAIL_PATTERN='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
tr '\n' '\0' < "$TMP_FILELIST" | xargs -0 grep -nHIE -- "$EMAIL_PATTERN" 2>/dev/null | sed 's/^/  [EMAIL] /' || true

say ""
say "== summary =="
if [ "$FAIL" -eq 0 ]; then
  say "check_leak.sh: PASS (0 denylist hits)"
else
  say "check_leak.sh: FAIL ($HITS denylist hit(s) — see [FOUND] lines above)"
fi
exit "$FAIL"
