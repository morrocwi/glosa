---
name: glosa-deliver
description: When a human asks to share/send a rendered glosa output, map the file to a delivery channel (Google Drive, Gmail draft, Canva, Calendar) via connectors — never by python — and gate on explicit human approval before anything leaves the repo. Load before any deliver/share/send request.
---

# glosa-deliver

Rendering (`tools/render.py`) never sends anything anywhere. Delivery is a separate,
human-gated step performed by an AI session's own connectors (Google Drive, Gmail,
Canva, Calendar — Claude Code MCP connectors, or the Codex/Gemini equivalents), never by
writing python HTTP calls to these services.

## When this applies

The work is at a stable checkpoint (a K-tier readout state, e.g. K1) **and** the human
asks to share, send, publish-to-doc, email, or put-on-slides.

## Step 1 — read the manifest

```
python3 tools/render.py deliver-manifest dist/manifest.json --dir dist
```

This lists rendered files with a suggested channel; it performs no delivery itself.

## Step 2 — map output → channel

| output | channel | how |
|---|---|---|
| `.docx` / `.pdf` | Google Drive | `create_file` (or `update_file` on redeploy) via the Google Drive connector; share the resulting link |
| a short summary / cover note | Gmail **draft** | `create_draft` — **never** `send_message` without explicit human approval in this turn |
| `.pptx` | Canva or plain pptx attachment | `import-design-from-url`/`generate-design-structured` into Canva if the human wants it editable there; otherwise attach the `.pptx` as-is |
| DOI / repo links | include as plain links in whichever body (Drive doc, email draft, Canva notes) — never re-host the file elsewhere |

## Non-negotiables

- **Never call `send_message` (Gmail) or any other "send/publish" action without the
  human confirming in the same turn.** Drafts and previews only, by default.
- Every delivery message body **must** include the tier/K-state disclaimer line — copy
  it from the rendered file's own footer/closing line, do not invent a stronger one.
- Follow the workspace's public-facing adversarial-review gate before any delivery
  reaches someone outside this workstation — this skill does not replace that gate.
- If no matching connector is available for a session (Claude Code MCP, Codex/Gemini
  equivalent), say so and hand the human the local file path instead of improvising an
  HTTP call to the service.

See `TOOLCHAIN.md` → "Connectors (optional)" for enable/verify/degrade per connector.
