#!/usr/bin/env bash
# scripts/check_repo.sh — glosa repo-consistency gate.
#
# Readout, not truth: this script reports what it observed against a fixed
# checklist. It does not certify the repo is "ready" or "safe" — that is a
# human/independent-review judgment (see RELEASE_CHECKLIST.md).
#
# Checks:
#   1. Required top-level files are present.
#   2. No LaTeX build artifacts are tracked in git.
#   3. Every tracked *.json file parses.
#   4. .glosa/secrets.env and .glosa/author_profile.json are NOT tracked by git.
#   5. registry/RELEASE_APPROVAL.txt is not tracked by git (it is gitignored and, when it
#      contains APPROVED, is a live founder-approval decision — never a public artifact), and
#      no tracked file matches *.env anywhere in the repo (MUST-11).
#
# Exit 0 = all checks passed. Exit 1 = at least one check failed (see output).

set -u
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)" || exit 1

FAIL=0
say()  { printf '%s\n' "$*"; }
ok()   { say "  [OK]   $*"; }
bad()  { say "  [FAIL] $*"; FAIL=1; }

say "== glosa check_repo.sh =="
say "repo root: $(pwd)"
say ""

# --- 1. required top-level files ---
say "-- required top-level files --"
REQUIRED_FILES=(
  README.md
  LICENSE
  CITATION.cff
  .zenodo.json
  CLAIM_BOUNDARY.md
  ASSUMPTIONS.md
  NON_CLAIMS.md
  AGENTS.md
  CLAUDE.md
  GEMINI.md
  llms.txt
  CHANGELOG.md
)
for f in "${REQUIRED_FILES[@]}"; do
  if [ -f "$f" ]; then
    ok "$f present"
  else
    bad "$f MISSING"
  fi
done
say ""

# --- 2. no LaTeX build artifacts tracked ---
say "-- tracked LaTeX build artifacts --"
if command -v git >/dev/null 2>&1 && git rev-parse --git-dir >/dev/null 2>&1; then
  ARTIFACT_PATTERN='\.(aux|log|out|bbl|blg|synctex\.gz|fdb_latexmk|fls|toc|lof|lot|nav|snm|vrb)$'
  TRACKED_ARTIFACTS="$(git ls-files | grep -E "$ARTIFACT_PATTERN" || true)"
  if [ -z "$TRACKED_ARTIFACTS" ]; then
    ok "no tracked LaTeX build artifacts"
  else
    bad "tracked LaTeX build artifacts found:"
    while IFS= read -r line; do [ -n "$line" ] && say "         $line"; done <<< "$TRACKED_ARTIFACTS"
  fi
else
  bad "not inside a git repository — cannot check tracked files"
fi
say ""

# --- 3. JSON files parse ---
say "-- JSON parse check (tracked *.json) --"
if git rev-parse --git-dir >/dev/null 2>&1; then
  JSON_FILES="$(git ls-files '*.json' || true)"
  if [ -z "$JSON_FILES" ]; then
    ok "no tracked JSON files"
  else
    PY="$(command -v python3 || true)"
    while IFS= read -r jf; do
      [ -z "$jf" ] && continue
      [ -f "$jf" ] || continue
      if [ -n "$PY" ]; then
        if "$PY" -c "import json,sys; json.load(open(sys.argv[1], encoding='utf-8'))" "$jf" 2>/tmp/glosa_json_err.$$; then
          ok "$jf parses"
        else
          bad "$jf FAILS to parse: $(cat /tmp/glosa_json_err.$$ 2>/dev/null | tail -1)"
        fi
        rm -f /tmp/glosa_json_err.$$
      else
        bad "python3 not found — cannot validate $jf"
      fi
    done <<< "$JSON_FILES"
  fi
else
  bad "not inside a git repository — cannot enumerate JSON files"
fi
say ""

# --- 4. secrets / local author profile must not be tracked ---
say "-- local-only files must NOT be tracked --"
for f in ".glosa/secrets.env" ".glosa/author_profile.json"; do
  if git rev-parse --git-dir >/dev/null 2>&1 && git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
    bad "$f IS TRACKED — must be removed from git and confirmed in .gitignore"
  else
    ok "$f not tracked"
  fi
done
say ""

# --- 5. RELEASE_APPROVAL.txt must not be tracked; no *.env tracked anywhere (MUST-11) ---
say "-- founder-approval file + secrets-env must NOT be tracked --"
if git rev-parse --git-dir >/dev/null 2>&1; then
  if git ls-files --error-unmatch registry/RELEASE_APPROVAL.txt >/dev/null 2>&1; then
    bad "registry/RELEASE_APPROVAL.txt IS TRACKED — a founder-approval decision file must never be committed"
  else
    ok "registry/RELEASE_APPROVAL.txt not tracked"
  fi
  if git check-ignore -q registry/RELEASE_APPROVAL.txt 2>/dev/null; then
    ok "registry/RELEASE_APPROVAL.txt is covered by .gitignore"
  else
    bad "registry/RELEASE_APPROVAL.txt is NOT covered by .gitignore — add it"
  fi
  TRACKED_ENV="$(git ls-files '*.env' || true)"
  if [ -z "$TRACKED_ENV" ]; then
    ok "no tracked *.env files"
  else
    bad "tracked *.env file(s) found:"
    while IFS= read -r line; do [ -n "$line" ] && say "         $line"; done <<< "$TRACKED_ENV"
  fi
else
  bad "not inside a git repository — cannot check RELEASE_APPROVAL.txt / *.env tracking"
fi
say ""

say "== summary =="
if [ "$FAIL" -eq 0 ]; then
  say "check_repo.sh: PASS"
else
  say "check_repo.sh: FAIL — see [FAIL] lines above"
fi
exit "$FAIL"
