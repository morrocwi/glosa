#!/usr/bin/env bash
# glosa — first public release (run by the AI only after the founder signs registry/RELEASE_APPROVAL.txt)
# Steps: gate checks → create public GitHub repo → push main → tag → (Zenodo publish is a separate, gated script)
# tier: Dr (tool). Fail-closed at every step. Usage: scripts/release_push.sh vX.Y.Z [--dry-run]
set -euo pipefail
V="${1:?version tag required, e.g. v0.1.0}"; DRY="${2:-}"
cd "$(dirname "$0")/.."
grep -q '^APPROVED' registry/RELEASE_APPROVAL.txt 2>/dev/null || { echo "STOP: registry/RELEASE_APPROVAL.txt missing or not APPROVED"; exit 1; }
git check-ignore -q registry/RELEASE_APPROVAL.txt || { echo "STOP: RELEASE_APPROVAL.txt must be git-ignored"; exit 1; }
[ -f reviews/PUBLISH_GATE_v1.md ] && grep -qE '^\*\*Verdict:\*\* *(PASS|PASS_WITH_LIMITS)|Verdict: *(PASS|PASS_WITH_LIMITS)' reviews/PUBLISH_GATE_v1.md || { echo "STOP: publish gate verdict not PASS/PASS_WITH_LIMITS"; exit 1; }
bash scripts/check_repo.sh >/dev/null && bash scripts/check_leak.sh >/dev/null && bash scripts/check_forbidden_words.sh >/dev/null && python3 -m unittest discover -s tests >/dev/null 2>&1 || { echo "STOP: a mechanical check failed"; exit 1; }
python3 scripts/check_version.py "$V" >/dev/null 2>&1 || echo "note: check_version.py did not confirm $V against CITATION.cff — verify manually"
echo "gate ok — release $V"
[ "$DRY" = "--dry-run" ] && { echo "dry-run: would create morrocwi/glosa (public), push main, tag $V"; exit 0; }
git branch -M main
gh repo view morrocwi/glosa >/dev/null 2>&1 || gh repo create morrocwi/glosa --public --source=. --remote=origin --description "glosa — Rigour Without Infrastructure: a standalone-scholar methodology for human–AI knowledge co-production (K0 public working release, CC BY 4.0)" --push
git remote get-url origin >/dev/null 2>&1 || git remote add origin https://github.com/morrocwi/glosa.git
git push -u origin main
git tag -a "$V" -m "glosa $V — K0 public working release (not peer reviewed, no independent check yet)"; git push origin "$V"
echo "pushed main + $V → https://github.com/morrocwi/glosa"
