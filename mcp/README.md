# glosa MCP server

**Tier: Dr** (single-pass, unreviewed — see `design/FOUNDATION_v0.5.md` §9, §12; not yet through
an independent I2+ review or the MIMCG gate). readout-not-truth: nothing below is claimed to work
beyond what `test_mcp_stdio.py` actually showed when it was last run — see the "Executed" section
at the bottom of this file for that raw output, not a paraphrase of it.

`glosa_mcp_server.py` is a **stdlib-only** JSON-RPC 2.0 server speaking the Model Context Protocol
(MCP) over stdio (`protocolVersion: "2025-06-18"`). It exposes one MCP tool per kernel function
named in `design/FOUNDATION_v0.5.md` §9 / the R3 task list:

```
glosa_validate_claim_card       glosa_validate_review_report    glosa_validate_citation_card
glosa_validate_blackbox_note    glosa_compute_disclaimers       glosa_route_genre
glosa_gate_release              glosa_independence_ceiling      glosa_defeater_route
glosa_silent_lift_check         glosa_lit_gate                  glosa_advise
glosa_self_test
```

Every tool call is a thin, lazy pass-through to `kernel/glosa_kernel.py` (`kernel.<name-without-
glosa_prefix>(**arguments)`). The kernel is imported **lazily, on the first tool call that needs
it** — not at server startup — because `kernel/glosa_kernel.py` is written by a different agent in
parallel with this file. **If the kernel file does not exist, or fails to import, or is missing the
called function, the server returns a normal JSON-RPC tool result with `isError: true` and an
`"error"` string that starts with `"kernel not present"` — it never crashes and never fabricates a
plausible-looking kernel answer.**

`glosa_gate_release` and `glosa_advise` are state-changing. Per MC-01 (`design/
FOUNDATION_v0.5.md` §3, §7.2 — "checked on the payload directly, not on a caller's self-declared
role"), the MCP layer itself requires `caller_role` (`"maker" | "checker" | "approver"`) and
`caller_identity` in the tool arguments, and rejects the call *before it ever reaches the kernel* if
the payload's own `maker_id` / `checker_id` / `approver_id` field for that role does not match
`caller_identity`. This is defense-in-depth on top of whatever check the kernel itself performs —
it does not replace the kernel's own MC-01 logic, and both checks run independently.

Every tool call — success, kernel error, or MCP-layer rejection — appends one
`{"kind": "tool_call", ...}` line to `logbook.jsonl` **in the server process's current working
directory** (so wire the client's `cwd` deliberately; see the `.mcp.json` snippet below).

## Wire format

Newline-delimited JSON-RPC 2.0 over stdio (one message per line), matching the standard MCP stdio
transport. Methods implemented: `initialize`, `notifications/initialized` (accepted, no reply, per
JSON-RPC notification semantics), `tools/list`, `tools/call`, `ping`. Unknown methods with an `id`
get a `-32601 method not found` error; unknown notifications (no `id`) are silently ignored.

## Claude Code — `.mcp.json`

Add an entry like this to your project's `.mcp.json` (or `~/.claude.json` under `mcpServers` for a
user-level install). `cwd` controls where `logbook.jsonl` lands — point it at the glosa repo root
so the logbook sits next to the rest of the project, not wherever Claude Code happened to launch
from:

```json
{
  "mcpServers": {
    "glosa": {
      "command": "python3",
      "args": ["~/ANSE.ASIA/glosa/mcp/glosa_mcp_server.py"],
      "cwd": "~/ANSE.ASIA/glosa"
    }
  }
}
```

After adding this, restart Claude Code (or run `/mcp` to reconnect) and the twelve `glosa_*` tools
should appear under the `glosa` server in `tools/list`.

## Codex / Gemini

Both accept the same generic "spawn this stdio command as an MCP server" shape as Claude Code;
consult each tool's own MCP-server config docs for the exact key names (Codex's `config.toml`
`[mcp_servers.glosa]` table with `command`/`args`; Gemini CLI's `settings.json` `mcpServers` map).
The command, args, and `cwd` above are identical regardless of which client launches the process —
this server does not do anything client-specific. No API keys, no network access, no extra
dependencies: `python3 glosa_mcp_server.py` is the entire contract.

## Manual smoke test

```bash
python3 mcp/test_mcp_stdio.py
```

Spawns the server, sends `initialize` → `tools/list` → `tools/call glosa_self_test`, and prints
each raw JSON-RPC response. It does **not** assert the kernel is present — a `glosa_self_test`
response with `isError: true` and `"kernel not present"` is an expected, correct outcome while
`kernel/glosa_kernel.py` does not yet exist or does not yet define `self_test`.

## Executed — actual output (see task report for the exact run and timestamp)

This README does not duplicate the raw run output inline (it would drift out of sync with the code
the moment either file changes again). The exact `test_mcp_stdio.py` output for the run that
accompanied this file's authorship is reported verbatim in the R3 task handoff / PR description,
not restated here as a second, driftable copy.
