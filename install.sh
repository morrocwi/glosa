#!/usr/bin/env bash
# glosa installer — one line, no ssh, no root.
#   curl -fsSL https://raw.githubusercontent.com/morrocwi/glosa/main/install.sh | bash
# Options (env):  GLOSA_DIR=~/glosa   GLOSA_SOURCE=<git url | local path | tarball url>
#                 GLOSA_NO_PIP=1 (skip pip)   GLOSA_REF=main (branch/tag)
# What it does: 1) checks python3 >= 3.10  2) fetches the repo over HTTPS (git, or tarball fallback)
#               3) pip --user installs requirements.txt  4) links cli/glosa into ~/.local/bin
#               5) runs `glosa doctor`  6) prints the two Claude Code commands + the MCP snippet.
# Everything here is a readout, not truth: `glosa doctor` is what verifies the result.
set -euo pipefail

GLOSA_DIR="${GLOSA_DIR:-$HOME/glosa}"
GLOSA_REF="${GLOSA_REF:-main}"
GLOSA_SOURCE="${GLOSA_SOURCE:-https://github.com/morrocwi/glosa.git}"
BIN_DIR="$HOME/.local/bin"

say() { printf '%s\n' "$*"; }
die() { printf 'glosa install: STOP — %s\n' "$*" >&2; exit 1; }

say "== glosa install =="
say "ติดตั้ง glosa (ไม่ต้องใช้ ssh, ไม่ต้อง root) → $GLOSA_DIR"

# 1. python
command -v python3 >/dev/null 2>&1 || die "python3 not found. Install Python 3.10+ first (ต้องมี python3 ก่อน)."
PYV="$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' || die "python3 $PYV is too old; need 3.10+"
say "python3 $PYV ok"

# 2. fetch (HTTPS only — never ssh)
if [ -d "$GLOSA_SOURCE/.git" ] || [ -f "$GLOSA_SOURCE/cli/glosa" ]; then
  say "source = local path $GLOSA_SOURCE"
  mkdir -p "$GLOSA_DIR"
  (cd "$GLOSA_SOURCE" && tar --exclude=.git -cf - .) | (cd "$GLOSA_DIR" && tar -xf -)
elif [ -d "$GLOSA_DIR/.git" ]; then
  say "updating existing checkout"
  git -C "$GLOSA_DIR" pull --ff-only origin "$GLOSA_REF" || die "git pull failed"
elif command -v git >/dev/null 2>&1; then
  case "$GLOSA_SOURCE" in git@*|ssh://*) die "ssh source not allowed; use https" ;; esac
  git clone --depth 1 --branch "$GLOSA_REF" "$GLOSA_SOURCE" "$GLOSA_DIR" || die "git clone failed (check network)"
else
  TARBALL="https://github.com/morrocwi/glosa/archive/refs/heads/${GLOSA_REF}.tar.gz"
  say "git not found — downloading tarball $TARBALL"
  mkdir -p "$GLOSA_DIR"
  curl -fsSL "$TARBALL" | tar -xz --strip-components=1 -C "$GLOSA_DIR" || die "tarball download failed"
fi
[ -f "$GLOSA_DIR/cli/glosa" ] || die "cli/glosa missing after fetch"

# 3. pip (user-level; optional)
if [ "${GLOSA_NO_PIP:-0}" != "1" ]; then
  if python3 -m pip --version >/dev/null 2>&1; then
    python3 -m pip install --user --quiet -r "$GLOSA_DIR/requirements.txt" 2>/dev/null \
      || python3 -m pip install --user --quiet --break-system-packages -r "$GLOSA_DIR/requirements.txt" \
      || say "warning: pip install failed — run: python3 -m pip install --user -r $GLOSA_DIR/requirements.txt"
  else
    say "warning: pip missing — install jsonschema + pyyaml + markdown yourself (see TOOLCHAIN.md)"
  fi
fi

# 4. link CLI
mkdir -p "$BIN_DIR"
chmod +x "$GLOSA_DIR/cli/glosa"
ln -sf "$GLOSA_DIR/cli/glosa" "$BIN_DIR/glosa"
case ":$PATH:" in *":$BIN_DIR:"*) ;; *) say "note: add to PATH →  export PATH=\"\$HOME/.local/bin:\$PATH\"" ;; esac

# 5. verify
say ""
"$GLOSA_DIR/cli/glosa" doctor || die "doctor reported problems (see above)"

# 6. next steps
cat <<EOF

== done / เสร็จแล้ว ==
CLI:        $BIN_DIR/glosa  (try: glosa demo)
Repo:       $GLOSA_DIR
Claude Code (2 คำสั่ง แล้วเปิดเซสชันใหม่):
    claude plugin marketplace add $GLOSA_DIR
    claude plugin install glosa@yaoharee-lahtee-glosa
    (or from GitHub: claude plugin marketplace add morrocwi/glosa)
MCP (any vendor that speaks MCP) — add to your client config:
    {"mcpServers":{"glosa":{"command":"python3","args":["$GLOSA_DIR/mcp/glosa_mcp_server.py"]}}}
Codex / Gemini / others without plugins: open $GLOSA_DIR/plugins/glosa/PROMPT_PACKET.md
Docs: $GLOSA_DIR/INSTALL.md
EOF
