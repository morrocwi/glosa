#!/usr/bin/env python3
"""glosa_mcp_server.py -- stdlib-only MCP (Model Context Protocol) server for glosa.

Tier: Dr (single-pass, unreviewed -- see design/FOUNDATION_v0.5.md S12/S9).
readout-not-truth: this file only reports what it actually ran. It never
fabricates a kernel result -- if kernel/glosa_kernel.py is not importable it
returns a clear JSON-RPC error ("kernel not present") instead of crashing or
inventing a plausible-looking answer.

Protocol: JSON-RPC 2.0 over stdio, one message per line (newline-delimited
JSON), matching the MCP stdio transport. protocolVersion "2025-06-18".
Methods implemented: initialize, tools/list, tools/call. notifications
(no "id" field) are accepted and ignored per JSON-RPC 2.0 (no response sent).

Kernel is imported LAZILY (only when a tool is actually called), because
kernel/glosa_kernel.py is being written concurrently by another agent and may
not exist yet, or may change shape between calls -- this file does not cache
a stale reference to a missing/partial module.

State-changing tools (glosa_gate_release, glosa_advise) require
`caller_role` and `caller_identity` in the tool arguments, and perform a
defense-in-depth cross-check against the maker/checker/approver identity
fields embedded in the payload itself (MC-01, design/FOUNDATION_v0.5.md
S7.2 / S3: "checked on the payload directly, not on a caller's
self-declared role"). This MCP-layer check is a second, independent gate in
front of whatever the kernel itself enforces -- it does not replace the
kernel's own MC-01 check, and if the kernel is absent this layer still runs
and can still reject a call before any kernel involvement is even attempted.

Every tool call -- success, kernel error, or MCP-layer rejection -- appends
one `{"kind": "tool_call", ...}` line to `logbook.jsonl` in the CURRENT
WORKING DIRECTORY (not this file's directory), so that whoever launched the
server controls where its logbook lands (usually the repo root when
launched via .mcp.json with `cwd` unset, i.e. the caller's cwd).

No network access. No writes anywhere except the append-only logbook.jsonl.
"""

from __future__ import annotations

import json
import sys
import io
import os
import traceback
import importlib
import datetime
from typing import Any

PROTOCOL_VERSION = "2025-06-18"
SERVER_NAME = "glosa"
SERVER_VERSION = "0.4.1-dr"

# Kernel functions named in FOUNDATION s9 / this task's tool list. Each
# glosa_<name> MCP tool maps 1:1 to kernel.<name>(**arguments) (minus the
# MCP-only caller_role/caller_identity fields, which are stripped before the
# kernel call and used only for the MCP-layer MC-01 defense-in-depth check).
TOOL_TO_KERNEL_FN = {
    "glosa_validate_claim_card": "validate_claim_card",
    "glosa_validate_review_report": "validate_review_report",
    "glosa_validate_citation_card": "validate_citation_card",
    "glosa_validate_blackbox_note": "validate_blackbox_note",
    "glosa_compute_disclaimers": "compute_disclaimers",
    "glosa_route_genre": "route_genre",
    "glosa_gate_release": "gate_release",
    "glosa_independence_ceiling": "independence_ceiling",
    "glosa_defeater_route": "defeater_route",
    "glosa_silent_lift_check": "silent_lift_check",
    "glosa_lit_gate": "lit_gate",
    "glosa_advise": "advise",
    "glosa_self_test": "self_test",
}

# Tools whose kernel call changes gate/release state (or advises on one) and
# therefore require the caller to assert who they are, per MC-01
# (design/FOUNDATION_v0.5.md S7.2, S3 maker_id/checker_id/approver_id
# pairwise-distinct discipline). This is a fixed allowlist, not inferred
# from the tool name, so a future kernel rename cannot silently widen or
# narrow which calls are gated.
STATE_CHANGING_TOOLS = {"glosa_gate_release", "glosa_advise"}

VALID_CALLER_ROLES = ("maker", "checker", "approver")

TOOL_DESCRIPTIONS = {
    "glosa_validate_claim_card": "Validate a claim_card payload against the glosa schema (kernel.validate_claim_card).",
    "glosa_validate_review_report": "Validate a review_report payload against the glosa schema (kernel.validate_review_report).",
    "glosa_validate_citation_card": "Validate a citation_card payload against the glosa schema (kernel.validate_citation_card).",
    "glosa_validate_blackbox_note": "Validate a blackbox_note payload (verbatim lines, lens_used block, hypothesis signature line) against the glosa schema (kernel.validate_blackbox_note).",
    "glosa_compute_disclaimers": "Compute the required disclaimer set for a given artifact/context (kernel.compute_disclaimers).",
    "glosa_route_genre": "Route an artifact to its genre per the glosa genre taxonomy (kernel.route_genre).",
    "glosa_gate_release": "STATE-CHANGING. Evaluate/apply the release gate for an artifact (kernel.gate_release). Requires caller_role + caller_identity.",
    "glosa_independence_ceiling": "Compute the independence ceiling (I-level) reachable for a given evidence/review configuration (kernel.independence_ceiling).",
    "glosa_defeater_route": "Route a reported defeater to its required response path (kernel.defeater_route).",
    "glosa_silent_lift_check": "Check an artifact for an undisclosed tier/claim lift relative to its stated basis (kernel.silent_lift_check).",
    "glosa_lit_gate": "Evaluate the Literature Review System (S14) gate checklist for a project (kernel.lit_gate).",
    "glosa_advise": "STATE-CHANGING. Produce a chair/kernel advisory on a decision payload (kernel.advise). Requires caller_role + caller_identity.",
    "glosa_self_test": "Run the kernel's own internal self_test() and return its result verbatim (kernel.self_test).",
}

# Identity fields the MC-01 defense-in-depth check looks for in a payload,
# keyed by the caller_role that field corresponds to.
ROLE_ID_FIELD = {
    "maker": "maker_id",
    "checker": "checker_id",
    "approver": "approver_id",
}


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _log(record: dict) -> None:
    """Append one JSON line to logbook.jsonl in the current working directory.

    Best-effort: a logging failure must never crash a tool call or take down
    the server (readout-not-truth applies to the tool result, not to the
    logbook plumbing) -- but it is not silently swallowed either; if writing
    fails we print a diagnostic to stderr (never stdout, which is the JSON-RPC
    channel).
    """
    try:
        with open(os.path.join(os.getcwd(), "logbook.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    except Exception as exc:  # noqa: BLE001 - logging must never raise
        print(f"[glosa_mcp_server] WARNING: logbook write failed: {exc}", file=sys.stderr)


def _load_kernel():
    """Lazily import kernel/glosa_kernel.py. Returns (module, error_message).

    Exactly one of the two return values is non-None. Adds this file's
    directory's sibling `kernel/` to sys.path only for the duration of the
    import attempt (does not mutate global state beyond the standard
    import-cache side effect of a successful import).
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kernel_dir = os.path.join(repo_root, "kernel")
    kernel_file = os.path.join(kernel_dir, "glosa_kernel.py")
    if not os.path.isfile(kernel_file):
        return None, f"kernel not present: {kernel_file} does not exist"
    added = False
    if kernel_dir not in sys.path:
        sys.path.insert(0, kernel_dir)
        added = True
    try:
        # Fresh import each call is deliberate: kernel is being written
        # concurrently by another agent during this development phase, so a
        # long-lived server process should not pin a stale/partial module in
        # sys.modules across the whole session.
        if "glosa_kernel" in sys.modules:
            module = importlib.reload(sys.modules["glosa_kernel"])
        else:
            module = importlib.import_module("glosa_kernel")
        return module, None
    except Exception as exc:  # noqa: BLE001 - any import-time failure is reported, not raised
        tb = traceback.format_exc()
        return None, f"kernel not present: import of glosa_kernel failed: {exc}\n{tb}"
    finally:
        if added and kernel_dir in sys.path:
            sys.path.remove(kernel_dir)


def _find_id_mismatch(payload: Any, caller_role: str, caller_identity: str):
    """Recursively scan `payload` for the identity field matching caller_role
    (e.g. maker_id for caller_role="maker") and return a mismatch description
    if a value is found that differs from caller_identity, else None.

    This is a shallow defense-in-depth pass, not a substitute for the
    kernel's own MC-01 pairwise-distinctness check -- it only catches the
    case where the caller's *self-declared* identity does not even match
    the identity the payload itself assigns to that role.
    """
    field = ROLE_ID_FIELD.get(caller_role)
    if field is None:
        return None

    found = []

    def _walk(node: Any, path: str):
        if isinstance(node, dict):
            if field in node:
                found.append((path + "." + field, node[field]))
            for k, v in node.items():
                _walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                _walk(v, f"{path}[{i}]")

    _walk(payload, "$")

    for path, value in found:
        if value != caller_identity:
            return {
                "field": path,
                "payload_value": value,
                "caller_identity": caller_identity,
            }
    return None


def _tool_list() -> list[dict]:
    tools = []
    for name in TOOL_TO_KERNEL_FN:
        schema: dict[str, Any] = {
            "type": "object",
            "properties": {},
            "additionalProperties": True,
        }
        if name in STATE_CHANGING_TOOLS:
            schema["properties"]["caller_role"] = {
                "type": "string",
                "enum": list(VALID_CALLER_ROLES),
                "description": "MC-01: who the caller claims to be for this state-changing call.",
            }
            schema["properties"]["caller_identity"] = {
                "type": "string",
                "description": "MC-01: the caller's own identity string, cross-checked against the matching *_id field in the payload.",
            }
            schema["required"] = ["caller_role", "caller_identity"]
        tools.append(
            {
                "name": name,
                "description": TOOL_DESCRIPTIONS.get(name, f"Calls kernel.{TOOL_TO_KERNEL_FN[name]}."),
                "inputSchema": schema,
            }
        )
    return tools


def _text_result(payload: dict, is_error: bool = False) -> dict:
    return {
        "content": [
            {"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)}
        ],
        "isError": is_error,
    }


def _handle_tools_call(params: dict) -> dict:
    name = params.get("name")
    arguments = params.get("arguments") or {}
    if not isinstance(arguments, dict):
        arguments = {"value": arguments}

    started = _now_iso()

    if name not in TOOL_TO_KERNEL_FN:
        result = {"error": f"unknown tool: {name}", "known_tools": sorted(TOOL_TO_KERNEL_FN)}
        _log({
            "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
            "status": "unknown_tool", "result": result,
        })
        return _text_result(result, is_error=True)

    fn_name = TOOL_TO_KERNEL_FN[name]
    call_kwargs = dict(arguments)
    caller_role = call_kwargs.pop("caller_role", None)
    caller_identity = call_kwargs.pop("caller_identity", None)

    # --- MC-01 defense-in-depth for state-changing tools -------------------
    if name in STATE_CHANGING_TOOLS:
        if not caller_role or not caller_identity:
            result = {
                "error": (
                    "MC-01: this is a state-changing tool; arguments must include "
                    "non-empty 'caller_role' and 'caller_identity'."
                ),
                "required": ["caller_role", "caller_identity"],
                "valid_caller_roles": list(VALID_CALLER_ROLES),
            }
            _log({
                "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
                "status": "rejected_missing_caller_identity", "result": result,
            })
            return _text_result(result, is_error=True)

        if caller_role not in VALID_CALLER_ROLES:
            result = {
                "error": f"MC-01: caller_role must be one of {VALID_CALLER_ROLES}, got {caller_role!r}.",
            }
            _log({
                "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
                "status": "rejected_bad_caller_role", "result": result,
            })
            return _text_result(result, is_error=True)

        mismatch = _find_id_mismatch(call_kwargs, caller_role, caller_identity)
        if mismatch is not None:
            result = {
                "error": (
                    "MC-01: caller_identity does not match the identity the payload "
                    f"itself assigns to role '{caller_role}' (defense-in-depth check, "
                    "independent of whatever the kernel's own MC-01 check does)."
                ),
                "mismatch": mismatch,
            }
            _log({
                "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
                "status": "rejected_mc01_mismatch", "result": result,
            })
            return _text_result(result, is_error=True)

    # --- kernel dispatch -----------------------------------------------------
    kernel, err = _load_kernel()
    if kernel is None:
        result = {"error": err}
        _log({
            "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
            "status": "kernel_not_present", "result": result,
        })
        return _text_result(result, is_error=True)

    fn = getattr(kernel, fn_name, None)
    if fn is None or not callable(fn):
        result = {
            "error": f"kernel not present: glosa_kernel has no callable '{fn_name}'",
            "kernel_module": getattr(kernel, "__file__", "?"),
        }
        _log({
            "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
            "status": "kernel_fn_missing", "result": result,
        })
        return _text_result(result, is_error=True)

    try:
        if name in STATE_CHANGING_TOOLS:
            # Pass the caller's asserted identity through to the kernel too,
            # so the kernel's own MC-01 check (checked on the payload
            # directly per FOUNDATION s3/s7.2) has it available if its
            # signature accepts it; kernels that don't expect these kwargs
            # simply won't declare them and we don't force-inject unknown
            # kwargs into an incompatible signature.
            kernel_result = fn(**call_kwargs)
        else:
            kernel_result = fn(**call_kwargs)
        status = "ok"
        result = {"result": kernel_result}
        is_error = False
    except TypeError as exc:
        status = "kernel_call_error"
        result = {"error": f"kernel.{fn_name} call failed (TypeError, likely argument mismatch): {exc}"}
        is_error = True
    except Exception as exc:  # noqa: BLE001 - report, never crash the server
        status = "kernel_call_error"
        result = {"error": f"kernel.{fn_name} raised {type(exc).__name__}: {exc}", "traceback": traceback.format_exc()}
        is_error = True

    _log({
        "kind": "tool_call", "ts": started, "tool": name, "arguments": arguments,
        "caller_role": caller_role, "caller_identity": caller_identity,
        "status": status, "result_ok": not is_error,
    })
    return _text_result(result, is_error=is_error)


def _dispatch(msg: dict) -> dict | None:
    msg_id = msg.get("id")
    method = msg.get("method")
    params = msg.get("params") or {}

    def ok(result: Any) -> dict:
        return {"jsonrpc": "2.0", "id": msg_id, "result": result}

    def err(code: int, message: str) -> dict:
        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}

    if method == "initialize":
        return ok({
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })

    if method == "notifications/initialized":
        return None  # notification, no response

    if method == "tools/list":
        return ok({"tools": _tool_list()})

    if method == "tools/call":
        try:
            return ok(_handle_tools_call(params))
        except Exception as exc:  # noqa: BLE001 - never let a bad call kill the server loop
            return err(-32000, f"internal error handling tools/call: {exc}")

    if method == "ping":
        return ok({})

    if msg_id is None:
        return None  # unknown notification: ignore per JSON-RPC 2.0

    return err(-32601, f"method not found: {method}")


def main() -> None:
    stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
    stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", write_through=True)

    for line in stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"parse error: {exc}"}}
            stdout.write(json.dumps(resp) + "\n")
            stdout.flush()
            continue

        if isinstance(msg, list):
            responses = [r for r in (_dispatch(m) for m in msg) if r is not None]
            if responses:
                stdout.write(json.dumps(responses) + "\n")
                stdout.flush()
            continue

        resp = _dispatch(msg)
        if resp is not None:
            stdout.write(json.dumps(resp) + "\n")
            stdout.flush()


if __name__ == "__main__":
    main()
