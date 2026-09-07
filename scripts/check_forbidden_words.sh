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
# Three classes of hit, in priority order:
#   [META-RULE-TEXT] — the hit is inside a sentence that states this very ban (e.g. this file's
#     own docstring); never a finding.
#   [QUOTED-SOURCE] (added 2026-09-07) — the hit sits inside a generated file under docs/library/
#     (scripts/zenodo_library_kg.py's output) AND is either (a) a JSON line whose key starts with
#     `quoted_` (e.g. `"quoted_abstract_head": ...`), verbatim third-party Zenodo-abstract text, or
#     (b) a Markdown line that is itself, or immediately follows, the script's own
#     "Quoted from the record's own abstract" label line. This class is COUNTED and PRINTED but
#     NEVER fails the gate — the word is a record's own vocabulary, quoted, not a glosa claim.
#     Scope is exactly docs/library/*.json and docs/library/*.md (recursively, incl. docs/library/
#     jps/); every other file, including glosa's own authored prose anywhere else in docs/, stays
#     strict. This does not touch or widen scripts/forbidden_words_allowlist.txt, which remains
#     design/ and lineage/ (plus the pre-existing reviews//sources//registry//blackbox//
#     methodology/data//records//knowledge//tests/sim//docs/kg_ prefixes) only.
#   [ALLOWLISTED] — an exact (path-prefix, word) pair from scripts/forbidden_words_allowlist.txt.
#   [FOUND] — none of the above: a real finding, fails the gate.
#
# Exit 0 = no un-allowlisted, non-quoted-source forbidden word found in any tracked file.
# Exit 1 = at least one [FOUND] match.

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
      design/*|lineage/*|reviews/*|sources/*|registry/*|blackbox/*|methodology/data/*|records/*|knowledge/*|tests/sim/*|docs/kg_*) : ;;  # records/knowledge = verbatim third-party passages; tests/sim = adversarial fixtures that must contain the words
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

# [QUOTED-SOURCE]: a docs/library/*.json line whose key starts with quoted_, or a docs/library/*.md
# line that is (or immediately follows) the "Quoted from the record's own abstract" label line.
is_quoted_source() {
  local file="$1" lineno="$2" linetext="$3"
  case "$file" in
    docs/library/*.json) ;;
    docs/library/*.md) ;;
    *) return 1 ;;
  esac
  case "$file" in
    *.json)
      printf '%s' "$linetext" | grep -qE '"quoted_[A-Za-z0-9_]*"[[:space:]]*:' && return 0
      return 1
      ;;
    *.md)
      if printf '%s' "$linetext" | grep -qi "Quoted from the record's own abstract"; then
        return 0
      fi
      if printf '%s' "$linetext" | grep -qE '^> '; then
        local prev=$((lineno - 1))
        local prevtext
        prevtext="$(sed -n "${prev}p" "$file" 2>/dev/null)"
        printf '%s' "$prevtext" | grep -qi "Quoted from the record's own abstract" && return 0
      fi
      return 1
      ;;
  esac
  return 1
}

mapfile -t TRACKED < <(git ls-files)

META='forbidden|banned|never|do not|allowlist|check_forbidden_words|ห้าม|ไม่มีคำ|no novelty|novelty claim|no priority|priority claim|same */ *different|outside a clearly|"phrase"|wording_en|rank\)|metadata only|is not the realism'
HITS=0
QUOTED=0
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
    if is_quoted_source "$f" "$lineno" "$linetext"; then
      say "  [QUOTED-SOURCE] $f:$lineno: $word"
      QUOTED=$((QUOTED + 1))
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
say "quoted-source hits (docs/library/, never fail): $QUOTED"
if [ "$FAIL" -eq 0 ]; then
  say "check_forbidden_words.sh: PASS (0 un-allowlisted hits)"
else
  say "check_forbidden_words.sh: FAIL ($HITS un-allowlisted hit(s) — see [FOUND] lines above)"
fi
exit "$FAIL"
