#!/usr/bin/env bash
# scripts/check_forbidden_words.sh — glosa overclaim/register gate.
#
# Readout, not truth: greps tracked files for the forbidden-word list
# (AGENTS.md rule 6 / FOUNDATION_v0.5): novel, novelty, unprecedented,
# prior art / prior-art, concession, seminal, pioneering. A hit is a
# finding to review — a design/lineage historical mention can be exempted
# via scripts/forbidden_words_allowlist.txt (design/ and lineage/ ONLY);
# every other path is a hard fail on any match.
#
# Exit 0 = no un-allowlisted forbidden word found in any tracked file.
# Exit 1 = at least one un-allowlisted match found.

set -u
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)" || exit 1

ALLOWLIST="scripts/forbidden_words_allowlist.txt"
FAIL=0

say() { printf '%s\n' "$*"; }

say "== glosa check_forbidden_words.sh =="
say "repo root: $(pwd)"
say "allowlist: $ALLOWLIST"
say ""

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  say "  [FAIL] not inside a git repository — cannot enumerate tracked files"
  exit 1
fi

# The forbidden-word regex (word-boundary, case-insensitive).
PATTERN='novel|novelty|unprecedented|prior[ -]art|concession|seminal|pioneering'

is_allowlisted() {
  # $1 = file path, $2 = matched word (lowercased)
  local file="$1" word="$2"
  [ -f "$ALLOWLIST" ] || return 1
  while IFS=$'\t' read -r prefix aw; do
    case "$prefix" in
      ''|'#'*) continue ;;
    esac
    # Honored prefixes: design/ and lineage/ (historical discussion), plus the quoted/data classes
    # below (see allowlist header): reviews/ (audit reports quoting hits), sources/ (third-party or
    # founder papers reproduced verbatim), registry/ (Zenodo metadata as data), blackbox/ (verbatim voice).
    case "$prefix" in
      design/*|lineage/*|reviews/*|sources/*|registry/*|blackbox/*|methodology/data/*) : ;;
      *) continue ;;
    esac
    case "$file" in
      "$prefix"*)
        if [ "$(printf '%s' "$aw" | tr 'A-Z' 'a-z')" = "$(printf '%s' "$word" | tr 'A-Z' 'a-z')" ]; then
          return 0
        fi
        ;;
    esac
  done < "$ALLOWLIST"
  return 1
}

mapfile -t TRACKED < <(git ls-files)

META='forbidden|banned|never|do not|allowlist|check_forbidden_words|ห้าม|ไม่มีคำ|no novelty|novelty claim|no priority|priority claim|same */ *different|outside a clearly|"phrase"|wording_en|rank\)|metadata only|is not the realism'
HITS=0
for f in "${TRACKED[@]}"; do
  case "$f" in
    scripts/check_forbidden_words.sh|scripts/forbidden_words_allowlist.txt|*.i3.json|*.i5.json) continue ;;  # route-verdict sidecars quote third-party text (data, not our claims)
  esac
  [ -f "$f" ] || continue
  if file --mime "$f" 2>/dev/null | grep -q 'charset=binary'; then
    continue
  fi
  MATCHES="$(grep -noiE -- "$PATTERN" "$f" 2>/dev/null || true)"
  [ -z "$MATCHES" ] && continue
  while IFS= read -r m; do
    [ -z "$m" ] && continue
    lineno="${m%%:*}"
    word="${m#*:}"
    linetext="$(sed -n "${lineno}p" "$f" 2>/dev/null)"
    if printf '%s' "$linetext" | grep -qiE -- "$META"; then
      say "  [META-RULE-TEXT] $f:$lineno: $word"
      continue
    fi
    if is_allowlisted "$f" "$word"; then
      say "  [ALLOWLISTED] $f:$lineno: $word"
    else
      say "  [FOUND] $f:$lineno: $word"
      HITS=$((HITS + 1))
      FAIL=1
    fi
  done <<< "$MATCHES"
done

say ""
say "== summary =="
if [ "$FAIL" -eq 0 ]; then
  say "check_forbidden_words.sh: PASS (0 un-allowlisted hits)"
else
  say "check_forbidden_words.sh: FAIL ($HITS un-allowlisted hit(s) — see [FOUND] lines above)"
fi
exit "$FAIL"
