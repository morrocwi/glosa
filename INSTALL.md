# Install glosa — ติดตั้ง glosa (สำหรับคนธรรมดา)

> Readout, not truth: the installer prints what it did; `glosa doctor` is what checks it.
> No ssh key, no root, no account needed. Works on Linux, macOS, WSL.

## A. One line (แนะนำ) — ทุกอย่างในคำสั่งเดียว

```bash
curl -fsSL https://raw.githubusercontent.com/morrocwi/glosa/main/install.sh | bash
```

What happens / มันทำอะไร:
1. checks `python3` 3.10+ (ถ้าไม่มี มันจะบอกให้ติดตั้ง python ก่อน)
2. downloads the repo over **HTTPS** into `~/glosa` (git if you have it, otherwise a tarball)
3. `pip install --user` the small dependency list (`requirements.txt`)
4. links the command `glosa` into `~/.local/bin`
5. runs `glosa doctor` and prints PASS/FAIL per item
6. prints the two Claude Code commands and the MCP snippet

Options: `GLOSA_DIR=/where/you/want`, `GLOSA_NO_PIP=1`, `GLOSA_REF=v0.1.0`.

## B. Claude Code plugin (2 คำสั่ง)

```bash
claude plugin marketplace add morrocwi/glosa
claude plugin install glosa@yaoharee-lahtee-glosa
```

Then **open a new session** (plugins load at session start) and type `/glosa`.
If `marketplace add` fails on your machine, do A first and then
`claude plugin marketplace add ~/glosa` (local path — no network needed).

## C. Any other AI (Codex, Gemini, ChatGPT, local models)

- Download: <https://github.com/morrocwi/glosa/archive/refs/heads/main.zip> (or do A).
- Give the AI `plugins/glosa/PROMPT_PACKET.md` — the vendor-neutral version of every skill.
- MCP clients: point the client at `mcp/glosa_mcp_server.py` (snippet printed by the installer).
- Gate files are identical for every vendor: `CLAUDE.md` = `AGENTS.md` = `GEMINI.md`.

## D. Check / ตรวจว่าใช้ได้

```bash
glosa doctor        # PASS/FAIL per item (python, deps, files, plugin manifest, kernel self-test)
glosa demo          # runs the worked example end to end
```

## Troubleshooting / แก้ปัญหา

| symptom | cause | fix |
|---|---|---|
| `Host key verification failed` / `No ED25519 host key is known for github.com` | a tool tried **ssh**; glosa never needs ssh | use route A (HTTPS) or `claude plugin marketplace add ~/glosa` |
| `glosa: command not found` | `~/.local/bin` not on PATH | `export PATH="$HOME/.local/bin:$PATH"` (add to `~/.bashrc`) |
| `ModuleNotFoundError: jsonschema` / `yaml` | pip step skipped | `python3 -m pip install --user -r ~/glosa/requirements.txt` |
| `/glosa` unknown in Claude Code | plugin installed mid-session | open a new session |
| pip refuses (`externally-managed-environment`) | distro-managed python | the installer retries with `--break-system-packages`; or use a venv |

## Uninstall

```bash
rm -f ~/.local/bin/glosa && rm -rf ~/glosa
claude plugin uninstall glosa@yaoharee-lahtee-glosa   # if installed
```

## What the install test guarantees (tests/test_install.py + CI)

- `install.sh` contains no ssh URL and parses (`bash -n`); a fresh HTTPS install into a temp dir
  ends with `glosa doctor` PASS on Python 3.10 and 3.12.
- `.claude-plugin/marketplace.json` points at the in-repo plugin path (never a remote clone),
  and every skill listed has a `SKILL.md`.
- Regression origin: 2026-09-04, the first public install failed on a machine without a GitHub
  ssh host key (founder ruling BBL-2026-09-04-092/093: "ให้คนธรรมดาก็ติดตั้งได้ … ทำ test อย่าให้เกิดเรื่องแบบนี้อีก").
