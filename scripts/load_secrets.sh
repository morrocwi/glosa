#!/usr/bin/env bash
# Source this: `. scripts/load_secrets.sh` — loads ~/.config/glosa/secrets.env (600) into the environment.
# Never echo values. Never pass them as command-line args (process table leak). Fail closed if missing.
set -u
F="${GLOSA_SECRETS:-$HOME/.config/glosa/secrets.env}"
if [ ! -f "$F" ]; then echo "glosa: secrets file missing: $F (copy .glosa/secrets.env.EXAMPLE there, chmod 600)" >&2; return 1 2>/dev/null || exit 1; fi
perm=$(stat -c '%a' "$F"); [ "$perm" = "600" ] || { echo "glosa: $F must be mode 600 (is $perm)" >&2; return 1 2>/dev/null || exit 1; }
set -a; . "$F"; set +a
P="${GLOSA_PROFILE:-$HOME/.config/glosa/author_profile.json}"
[ -f "$P" ] && export GLOSA_PROFILE="$P" || echo "glosa: author profile missing: $P" >&2
echo "glosa: secrets loaded (values hidden); profile=${GLOSA_PROFILE:-none}"
