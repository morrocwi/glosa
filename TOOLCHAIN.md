# glosa — toolchain (what the whole cycle needs installed/enabled)

This is the install/enable list for one full glosa cycle: write → validate → render →
check → archive → (optionally) deliver. It is public — this file names **tools and
connector categories only**, never a credential, token, or private filesystem path.
Local credentials live in `~/.config/glosa/secrets.env` on whichever machine runs the
cycle — that file itself is never committed and is not described here beyond its name.

Tier note (readout-not-truth): every "verify" step below is something a maintainer can
run and see for themselves; "verified" markers with a date mean a maintainer actually ran
that command on 2026-09-04, not that it will hold on every machine forever — re-run
`scripts/check_toolchain.sh` on your own machine before trusting this file's status column.

For the machine-readable installers: `requirements.txt` (pip) and `apt-packages.txt`
(informational Debian/Ubuntu package names — nothing in this repo runs `apt` for you).

---

## Core

| tool | purpose in the cycle | install | verify | if missing |
|---|---|---|---|---|
| python3 ≥ 3.10 | runs every script in `tools/`, `scripts/`, `cli/`, `kernel/` | usually preinstalled; else your distro's user-level pyenv/conda | `python3 --version` | nothing in this repo runs |
| git | version control, PR workflow | usually preinstalled | `git --version` | can't track changes |
| gh (GitHub CLI) | PR/issue/release workflow against the public GitHub mirror | `gh` binary from github.com/cli/cli (user-level tarball, no admin needed) or your package manager | `gh auth status` | manual web-UI PR/issue/release steps instead |

## Validation

| tool | purpose | install | verify | if missing |
|---|---|---|---|---|
| jsonschema (pip) | validates claim cards, review reports, etc. against `schema/*.schema.json` | `pip install --user jsonschema` (in `requirements.txt`) | `python3 -c "import jsonschema"` | schema-conformance checks in `scripts/check_*.sh` can't run |
| PyYAML (pip) | reads/writes YAML manifests/decisions | `pip install --user pyyaml` (in `requirements.txt`) | `python3 -c "import yaml"` | any YAML-consuming script fails |

## Rendering (`tools/render.py`)

| tool | purpose | install | verify | if missing |
|---|---|---|---|---|
| markdown (pip) | parses the glosa paper markdown for every render route | `pip install --user markdown` | `python3 -c "import markdown"` | no rendering at all |
| python-docx (pip) | direct DOCX build (`md2docx`) | `pip install --user python-docx` | `python3 -c "import docx"` | `md2docx` falls back to the soffice HTML→DOCX route |
| python-pptx (pip) | slide deck build (`md2pptx`) | `pip install --user python-pptx` | `python3 -c "import pptx"` | `md2pptx` unavailable |
| LibreOffice (`soffice`) | headless HTML→PDF, HTML/ODT→DOCX fallback, the **only verified working Thai-rendering PDF/DOCX route** in this environment | your distro package manager (**requires admin**: `sudo apt install libreoffice`) or a user-level LibreOffice AppImage/tarball if admin is unavailable | `soffice --headless --convert-to pdf --outdir /tmp x.html` | `md2pdf` and the docx fallback route both fail; no Thai PDF/DOCX at all |
| Noto Thai fonts (Noto Sans/Serif/Looped Thai) | Thai glyph coverage inside the soffice-rendered HTML/PDF/DOCX | **requires admin**: `sudo apt install fonts-noto-thai fonts-noto-looped-thai`, or user-level: drop `.ttf` files in `~/.local/share/fonts` and run `fc-cache -f` | `fc-list | grep -i "noto.*thai"` | Thai text renders with a fallback/tofu glyph |
| pandoc (optional) | an alternate markdown-conversion route; **not used** by `tools/render.py`'s direct routes | **requires admin** for the apt route, or user-level `.deb`/tarball install from pandoc.org | `pandoc --version` | no effect on this tool; direct routes already cover md→html/pdf/docx/pptx |
| pdflatex | `tex2pdf` route, **EN-only** — verified working 2026-09-04, no Thai glyph support | usually ships with any TeX Live install (**requires admin** for a fresh install: `sudo apt install texlive-latex-base`) | `pdflatex --version` | `tex2pdf` unavailable entirely |
| bibtex | bibliography step inside `tex2pdf` | ships with TeX Live | `bibtex --version` | `tex2pdf` skips the bibliography step and warns |
| texlive-xetex (xelatex) | Thai-capable LaTeX route | **verified MISSING 2026-09-04**; **requires admin**: `sudo apt install texlive-xetex texlive-lang-other texlive-fonts-extra` | `xelatex --version` | Thai LaTeX unavailable; use `md2pdf` (soffice) for Thai instead |
| lualatex | alternate Thai-capable LaTeX route | present in this environment but **verified broken for Thai 2026-09-04** (fontspec/luaotfload failure) — treat as unavailable until an admin repairs the TeX Live font stack | `lualatex --version` (presence only; does not confirm Thai works) | same as xelatex: use `md2pdf` for Thai |

**Bottom line for Thai documents:** use `render.py md2pdf` / `md2docx` (the LibreOffice
route) — that is the one this environment has actually verified renders Thai correctly.
`tex2pdf` is EN-only until an admin fixes the XeTeX/LuaTeX+Thai font stack.

## Citation checking

| tool | purpose | install | verify | if missing |
|---|---|---|---|---|
| curl | HTTP calls to Crossref/OpenAlex APIs for citation existence checks | usually preinstalled | `curl --version` | citation-checking scripts in `scripts/` can't reach the network |
| Crossref / OpenAlex (optional, HTTP only, no key required for basic lookups) | source-existence verification for citation cards | nothing to install — plain HTTPS GET | a manual `curl https://api.crossref.org/works/<doi>` | citation existence checks must be done by hand |

## AI vendors

| vendor surface | purpose | install/enable | verify | if missing |
|---|---|---|---|---|
| Claude Code plugin (`plugins/glosa/`) | skills + MCP wiring for Claude sessions | `claude plugin install` per the plugin's own manifest | plugin shows in `claude plugin list` | Claude sessions lose the glosa skill set; fall back to reading `plugins/glosa/skills/*/SKILL.md` directly |
| Codex `AGENTS.md` | mirrors the same rules for Codex sessions | none — it's a file Codex reads automatically at repo root | Codex session prints/acknowledges it | Codex sessions have no glosa-specific guidance |
| Gemini `GEMINI.md` | mirrors the same rules for Gemini sessions | none — read automatically | Gemini session prints/acknowledges it | same gap as above, for Gemini |
| MCP servers (`mcp/`) | tool-call surface shared across vendors | run per `mcp/`'s own setup (user-level Node/Python process, no admin) | the calling agent's MCP tool list includes glosa's server | agents fall back to calling `tools/`/`scripts/` directly via shell |

## Connectors (optional — used only for `deliver`, never for rendering itself)

None of these are required to render a document; they are required only when a human
asks to **share** a rendered output outside the repo. `tools/render.py` never calls a
connector itself — it only writes a manifest (`deliver-manifest`) that an AI session with
the matching connector reads. See `plugins/glosa/skills/glosa-deliver/SKILL.md`.

| connector | purpose | how to enable | if absent |
|---|---|---|---|
| Google Drive / Docs | store/share a rendered PDF/DOCX as a Drive file or convert to a native Google Doc | connect the Google Drive MCP/first-party connector for the AI session; local credential state lives wherever that connector's own config keeps it (never in this repo) | deliver falls back to attaching the local file directly or asking the human to upload it |
| Gmail | draft (never auto-send) a summary email carrying links/attachments | connect the Gmail MCP/first-party connector; **drafts only** unless a human explicitly approves sending | deliver falls back to describing the email content in-session for the human to send manually |
| Canva | push a rendered outline into a design/slide deck | connect the Canva MCP connector | deliver falls back to the plain `.pptx` from `md2pptx` |
| Google Calendar | optional: attach a rendered doc to a meeting/review event | connect the Google Calendar MCP/first-party connector | scheduling step is done manually |
| Zenodo | archival DOI for a release; token lives locally in `~/.config/glosa/secrets.env` (never in this repo, never printed) | obtain a Zenodo personal access token, store it locally per your own machine's secrets convention | no DOI minted; GitHub release/tag stands alone as the archival point |
| GitHub (`gh auth`) | release tagging, PR workflow, public repo hosting | `gh auth login` (interactive, user-level, no admin) | manual web-UI GitHub steps |
| local git server (optional) | a non-GitHub mirror some contributors may run | project-specific; not part of this repo's required path | GitHub remains the sole remote |

---

## What "requires admin" means here

Every item above marked **requires admin** needs a `sudo`-level package install
(LibreOffice, Noto Thai fonts, pandoc via apt, TeX Live's XeTeX packages). Nothing in
`tools/render.py` or `scripts/check_toolchain.sh` ever calls `sudo` itself — if one of
these is missing, the tool degrades (see the table) rather than trying to install it.
Everything else (pip `--user` installs, `gh auth login`, MCP connector setup, Claude/
Codex/Gemini config files) is user-level.

## Quick check

```
python3 tools/render.py check          # this tool's own toolchain view (exit 1 only if a CORE item is missing)
bash scripts/check_toolchain.sh        # the standalone table version (never installs anything)
```
