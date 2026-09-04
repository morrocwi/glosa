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

TMP_FILELIST="$(mktemp)"
trap 'rm -f "$TMP_FILELIST"' EXIT
for f in "${TRACKED[@]}"; do
  case "$f" in
    scripts/check_leak.sh|scripts/leak_denylist.txt|scripts/leak_denylist.local.txt) continue ;;
  esac
  [ -f "$f" ] || continue
  # Skip obvious binaries.
  if file --mime "$f" 2>/dev/null | grep -q 'charset=binary'; then
    continue
  fi
  printf '%s\n' "$f" >> "$TMP_FILELIST"
done

# Load patterns (skip blank lines and comments).
PATTERNS=()
while IFS= read -r line; do
  case "$line" in
    ''|'#'*) continue ;;
  esac
  PATTERNS+=("$line")
done < "$DENYLIST"

say "-- scanning $(wc -l < "$TMP_FILELIST" | tr -d ' ') tracked files against ${#PATTERNS[@]} patterns --"
say ""

HITS=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  for pat in "${PATTERNS[@]}"; do
    MATCHES="$(grep -inE -- "$pat" "$f" 2>/dev/null || true)"
    if [ -n "$MATCHES" ]; then
      while IFS= read -r m; do
        [ -z "$m" ] && continue
        say "  [FOUND] $f:$m  (pattern: $pat)"
        HITS=$((HITS + 1))
        FAIL=1
      done <<< "$MATCHES"
    fi
  done
done < "$TMP_FILELIST"

# Author's-own-email allow check: separately report every email match so a
# human can confirm which lines (if any) are the intended public author line.
say ""
say "-- email addresses found (for human confirmation, not auto-failed) --"
EMAIL_PATTERN='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
while IFS= read -r f; do
  [ -z "$f" ] && continue
  MATCHES="$(grep -nE -- "$EMAIL_PATTERN" "$f" 2>/dev/null || true)"
  if [ -n "$MATCHES" ]; then
    while IFS= read -r m; do
      [ -z "$m" ] && continue
      say "  [EMAIL] $f:$m"
    done <<< "$MATCHES"
  fi
done < "$TMP_FILELIST"

say ""
say "== summary =="
if [ "$FAIL" -eq 0 ]; then
  say "check_leak.sh: PASS (0 denylist hits)"
else
  say "check_leak.sh: FAIL ($HITS denylist hit(s) — see [FOUND] lines above)"
fi
exit "$FAIL"
