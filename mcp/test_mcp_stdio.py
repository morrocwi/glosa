#!/usr/bin/env python3
"""test_mcp_stdio.py -- spawn glosa_mcp_server.py and exercise it over stdio.

Tier: Dr. This is a manual/dev smoke test, not a pytest suite and not an
independent review -- it only shows what the server actually returned for
three calls (initialize, tools/list, tools/call self_test) when run on this
machine, at this time. It does not assert the kernel is present; if kernel/
glosa_kernel.py is absent or incomplete, the self_test call is EXPECTED to
come back as an isError:true "kernel not present" result, and that is
printed and treated as a pass for this script's own purpose (proving the
server fails closed instead of crashing).

Usage:
    python3 mcp/test_mcp_stdio.py
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(HERE, "glosa_mcp_server.py")


def send(proc: subprocess.Popen, msg: dict) -> None:
    line = json.dumps(msg) + "\n"
    assert proc.stdin is not None
    proc.stdin.write(line)
    proc.stdin.flush()


def recv(proc: subprocess.Popen) -> dict:
    assert proc.stdout is not None
    line = proc.stdout.readline()
    if not line:
        stderr = proc.stderr.read() if proc.stderr else ""
        raise RuntimeError(f"server closed stdout with no response; stderr:\n{stderr}")
    return json.loads(line)


def main() -> int:
    proc = subprocess.Popen(
        [sys.executable, SERVER],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        cwd=HERE,
    )

    try:
        print("=== 1) initialize ===")
        send(proc, {
            "jsonrpc": "2.0", "id": 1, "method": "initialize",
            "params": {
                "protocolVersion": "2025-06-18",
                "capabilities": {},
                "clientInfo": {"name": "test_mcp_stdio", "version": "0.1"},
            },
        })
        resp1 = recv(proc)
        print(json.dumps(resp1, indent=2))

        print("\n=== 2) tools/list ===")
        send(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        resp2 = recv(proc)
        print(json.dumps(resp2, indent=2))

        print("\n=== 3) tools/call glosa_self_test ===")
        send(proc, {
            "jsonrpc": "2.0", "id": 3, "method": "tools/call",
            "params": {"name": "glosa_self_test", "arguments": {}},
        })
        resp3 = recv(proc)
        print(json.dumps(resp3, indent=2))

    finally:
        if proc.stdin:
            proc.stdin.close()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
        stderr_tail = proc.stderr.read() if proc.stderr else ""
        if stderr_tail.strip():
            print("\n=== server stderr ===")
            print(stderr_tail)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
