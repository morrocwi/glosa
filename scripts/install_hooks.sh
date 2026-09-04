#!/usr/bin/env bash
# glosa — install the git pre-commit hook that runs the leak scan (fail-closed) before every commit.
# Regression origin 2026-09-04: absolute local paths written by a CLI command reached a public commit
# twice before CI caught them. A commit-time scan catches this on the maker's machine first.
set -e
cd "$(dirname "$0")/.."
mkdir -p .git/hooks
cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
cd "$(git rev-parse --show-toplevel)"
bash scripts/check_leak.sh >/tmp/glosa_precommit_leak.log 2>&1 || { grep FOUND /tmp/glosa_precommit_leak.log | head -20; echo "pre-commit: leak scan FAILED — commit refused (see above)"; exit 1; }
bash scripts/check_forbidden_words.sh >/dev/null 2>&1 || { echo "pre-commit: forbidden-word scan FAILED — commit refused"; exit 1; }
HOOK
chmod +x .git/hooks/pre-commit
echo "installed .git/hooks/pre-commit (leak + forbidden-word scan)"
