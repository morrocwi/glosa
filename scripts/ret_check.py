#!/usr/bin/env python3
"""scripts/ret_check.py -- RET-Check v0.1: an AI-independent recursive provenance auditor.

tier: Dr (specified from `cases/ret/PREREGISTRATION_v0_1.md` and the theory source below;
independently unreviewed; will read `finite_diagnostic` once `tests/test_ret_check.py` has run --
see `methodology/P21_ret_check.md`).

Founder order (verbatim, Blackbox Log `BBL-2026-09-07-223`): "RET-Check v0.1 -- AI-independent
recursive provenance auditor: โปรแกรมเล็ก Python standard library ไม่มี LLM (AI=0 ตอน runtime) ..."
-- a small Python **standard-library-only** program, no LLM, `AI = 0` at runtime, that reads
CSV/JSON provenance rows and computes N_A / N_P / recursive cycles / external interruption, then
prints a RET SELF-AUDIT report with a RET RISK label. This module implements the founder's spec
using THE PAPER'S OWN definitions -- it does not invent new ones. Theory source:
`The_Recursive_Epistemic_Tunnel_GENESIS_FIRST_FULL_v2_0.md` (RET GENESIS FIRST v2.0), sections
13-21 and 25-30. Every computed quantity below cites its section and RET-Nxx working alias; Toledo
codes are not yet registered for these objects (`methodology/P19`) -- cite the RET-Nxx alias until
the registrar assigns a Toledo code, then update the cite in this docstring and in
`methodology/P21_ret_check.md`.

READOUT, NOT TRUTH -- read `cases/ret/PREREGISTRATION_v0_1.md`'s "What the program can NOT verify"
section before trusting any report this script prints. In summary: `root_independent` (is a
provenance root independent) and `record_type: world_record` / an independent `review` (is a
record world-side) are INPUT DECLARATIONS supplied by the case author. This program audits the
DECLARED graph structure -- who cites whom, which roots and records are declared independent --
never whether those declarations are true. Every report header restates this.

Computed quantities and their section citations:

  N_A(c)   -- number of distinct agents with record_type == "endorsement" for claim c.
              Section 15 (the Epistemic Mirror Effect): "N_A(c) = number of endorsing agents".
  N_P(c)   -- number of distinct source_root values declared root_independent == true for c.
              Section 15's N_P(c), refined by section 16's typed provenance structure
              Pi(c) = (V_c, E_c, tau_c) (RET-N07). root_independent is an input declaration
              (see the disclaimer above) -- this program never derives independence itself.
  Flagship -- N_A(c) up  does-not-imply  N_P(c) up. Section 15, RET-N06 (non-entailment).
  Recursive cycle -- any directed cycle in the parent -> agent graph for c. Section 14, RET-N04
              ("a minimal cycle is a_i -> a_j -> a_i"; a multi-agent cycle generalizes this).
              "Return-to-origin" additionally reports whether the cycle includes a row whose
              parent == "-" (an origin node for that claim).
  External interruption -- a world_record row, or a review row declared root_independent == true,
              whose own ancestry (walked backward through parent edges) does not intersect any
              node of a detected recursion cycle. Operationalizes section 28's AI-Independent
              Consequence Requirement (RET-N16: CausalAncestry(y) is not a subset of the
              recursive network up to the freeze time) and sections 29-30's AI-Off World-Closure
              (RET-N17 / RET-N18) as a graph-lineage test this program can actually run. When no
              cycle exists at all, any qualifying world_record/review row counts (there is
              nothing recursive for its lineage to "pass through").
  Effective-alternatives regime (optional; only when effective_alternatives_before/after are
              supplied on at least one row of the claim) -- section 19: "evidence_driven_convergence"
              (RET-N09: delta < 0 AND an external interruption is present) vs.
              "tunnel_contraction_risk" (RET-N10: delta < 0, a cycle is present, and no external
              interruption is present). This label is a report annotation; it does not feed the
              RET RISK formula below (the founder specified that formula in terms of N_A, N_P,
              cycle, and interruption only -- see the preregistration).

RET RISK formula (pre-registered in `cases/ret/PREREGISTRATION_v0_1.md`, exact, first match wins):

  1. LOW    if N_P(c) >= N_A(c)
  2. LOW    if an external interruption is present AND N_P(c) >= 1
  3. HIGH   if N_A(c) > N_P(c) AND a recursive cycle is detected AND no external interruption
  4. MEDIUM otherwise (N_A(c) > N_P(c), and either no cycle, or an interruption present but
            N_P(c) == 0)

No priority-word claims are made about this program's accuracy or novelty (`AGENTS.md` rule 6);
its correctness is exactly what `tests/test_ret_check.py` demonstrates, run and read yourself.

Standard library only. No network call, no import of anything that would let an LLM run inside
this process (enforced by `tests/test_ret_check.py::test_no_network_no_third_party_import`, which
diffs `sys.modules` before/after importing this module).

Usage (standalone):
    python3 scripts/ret_check.py <path.json|path.csv> [--json]
Also callable via `./cli/glosa ret check <path> [--json]` (cli/README.md) -- that command imports
and calls this module's `run()` function directly, so the two never drift.

Exit codes: 0 = a report was produced (regardless of the RET RISK label the report contains --
this is a diagnostic tool, not a pass/fail gate on the claim's content). 2 = the input file could
not be read, parsed, or validated against the row shape below.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROW_FIELDS = ("claim", "agent", "parent", "source_root", "root_independent", "record_type")
OPTIONAL_ROW_FIELDS = (
    "evidence_ref",
    "effective_alternatives_before",
    "effective_alternatives_after",
    "self_application",
)
VALID_RECORD_TYPES = ("endorsement", "world_record", "review")

DISCLAIMER_HEADER = (
    "Readout, not truth: independence of a provenance root (root_independent) and the world-side\n"
    "status of a record (record_type: world_record, or an independent review) are INPUT\n"
    "DECLARATIONS supplied by the case author -- this program audits the DECLARED graph structure\n"
    "only. It never verifies that a declared-independent root truly is independent, or that a\n"
    "declared world_record truly occurred in the world outside the recursive network. See\n"
    "cases/ret/PREREGISTRATION_v0_1.md ('What the program can NOT verify')."
)

SELF_APPLICATION_SENTENCE = (
    "The RET manuscript itself remains at RET-risk until independent world-side or reviewer-side "
    "resistance is added."
)


class RetCheckInputError(ValueError):
    """Raised when input rows fail the shape/type checks below (maps to exit code 2)."""


# --------------------------------------------------------------------------------------------
# Loading and validating rows
# --------------------------------------------------------------------------------------------

def _coerce_bool(value: Any, field: str, row_index: int) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        v = value.strip().lower()
        if v in ("true", "1", "yes"):
            return True
        if v in ("false", "0", "no", ""):
            return False
    raise RetCheckInputError(f"row {row_index}: field {field!r} is not a legal boolean: {value!r}")


def _coerce_optional_int(value: Any, field: str, row_index: int) -> "int | None":
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        raise RetCheckInputError(f"row {row_index}: field {field!r} is not a legal integer: {value!r}")


def _validate_row(raw: dict, row_index: int) -> dict:
    for field in REQUIRED_ROW_FIELDS:
        if field not in raw or raw[field] in (None, ""):
            raise RetCheckInputError(f"row {row_index}: missing required field {field!r}")
    record_type = str(raw["record_type"]).strip()
    if record_type not in VALID_RECORD_TYPES:
        raise RetCheckInputError(
            f"row {row_index}: record_type {record_type!r} not one of {VALID_RECORD_TYPES}"
        )
    row = {
        "claim": str(raw["claim"]).strip(),
        "agent": str(raw["agent"]).strip(),
        "parent": str(raw["parent"]).strip(),
        "source_root": str(raw["source_root"]).strip(),
        "root_independent": _coerce_bool(raw["root_independent"], "root_independent", row_index),
        "record_type": record_type,
        "evidence_ref": (str(raw["evidence_ref"]).strip() if raw.get("evidence_ref") not in (None, "") else None),
        "effective_alternatives_before": _coerce_optional_int(
            raw.get("effective_alternatives_before"), "effective_alternatives_before", row_index
        ),
        "effective_alternatives_after": _coerce_optional_int(
            raw.get("effective_alternatives_after"), "effective_alternatives_after", row_index
        ),
        "self_application": _coerce_bool(raw.get("self_application", False), "self_application", row_index),
    }
    return row


def load_rows(path: "str | Path") -> list[dict]:
    """Load rows from a JSON (list-of-objects, or {"rows": [...]}) or CSV file. Raises
    RetCheckInputError on any structural problem (maps to exit code 2 at the CLI boundary)."""
    p = Path(path)
    if not p.exists():
        raise RetCheckInputError(f"input file not found: {p}")
    text = p.read_text(encoding="utf-8")
    suffix = p.suffix.lower()
    raw_rows: list[dict]
    if suffix == ".json":
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RetCheckInputError(f"invalid JSON in {p}: {exc}")
        if isinstance(data, list):
            raw_rows = data
        elif isinstance(data, dict) and isinstance(data.get("rows"), list):
            raw_rows = data["rows"]
        else:
            raise RetCheckInputError(
                f"{p}: JSON must be a list of row objects, or an object with a 'rows' list"
            )
    elif suffix == ".csv":
        try:
            with p.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                raw_rows = list(reader)
        except csv.Error as exc:
            raise RetCheckInputError(f"invalid CSV in {p}: {exc}")
    else:
        raise RetCheckInputError(f"{p}: unrecognized suffix {suffix!r} -- must be .json or .csv")

    if not raw_rows:
        raise RetCheckInputError(f"{p}: no rows found")

    rows = []
    for i, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise RetCheckInputError(f"row {i}: not an object/mapping: {raw!r}")
        rows.append(_validate_row(raw, i))
    return rows


def group_by_claim(rows: list[dict]) -> "dict[str, list[dict]]":
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["claim"], []).append(row)
    return grouped


# --------------------------------------------------------------------------------------------
# Graph analysis (section 14 RET-N04 cycle; section 28/29-30 external interruption)
# --------------------------------------------------------------------------------------------

def _find_cycle(rows: list[dict]) -> "tuple[bool, list[str]]":
    """Directed-cycle detection over parent -> agent edges (section 14, RET-N04). Returns
    (has_cycle, cycle_path) where cycle_path is one witnessed cycle, first node repeated last."""
    nodes: set[str] = set()
    forward: dict[str, list[str]] = {}
    for row in rows:
        nodes.add(row["agent"])
        if row["parent"] != "-":
            nodes.add(row["parent"])
            forward.setdefault(row["parent"], []).append(row["agent"])

    color: dict[str, int] = {n: 0 for n in nodes}  # 0=white, 1=gray, 2=black
    found: list[str] = []

    def dfs(u: str, stack: list[str]) -> bool:
        color[u] = 1
        stack.append(u)
        for v in sorted(forward.get(u, [])):
            if color.get(v, 0) == 0:
                if dfs(v, stack):
                    return True
            elif color.get(v) == 1:
                idx = stack.index(v)
                found.extend(stack[idx:] + [v])
                return True
        stack.pop()
        color[u] = 2
        return False

    for n in sorted(nodes):
        if color.get(n, 0) == 0:
            if dfs(n, []):
                return True, found
    return False, []


def _ancestors(agent: str, reverse: "dict[str, list[str]]") -> "set[str]":
    """All nodes reachable backward from `agent` through parent edges (cycle-safe)."""
    visited: set[str] = set()
    stack = [agent]
    while stack:
        n = stack.pop()
        for p in reverse.get(n, []):
            if p not in visited:
                visited.add(p)
                stack.append(p)
    return visited


def _external_interruption(rows: list[dict], cycle_nodes: "set[str]") -> "tuple[bool, list[dict]]":
    """Section 28 (RET-N16) / sections 29-30 (RET-N17/RET-N18): a world_record row, or a review row
    declared root_independent == true, whose own ancestry does not intersect the recursion cycle."""
    reverse: dict[str, list[str]] = {}
    for row in rows:
        if row["parent"] != "-":
            reverse.setdefault(row["agent"], []).append(row["parent"])

    qualifying: list[dict] = []
    for row in rows:
        is_candidate = row["record_type"] == "world_record" or (
            row["record_type"] == "review" and row["root_independent"]
        )
        if not is_candidate:
            continue
        lineage = {row["agent"]} | _ancestors(row["agent"], reverse)
        if not (lineage & cycle_nodes):
            qualifying.append(row)
    return (len(qualifying) > 0), qualifying


# --------------------------------------------------------------------------------------------
# Per-claim analysis
# --------------------------------------------------------------------------------------------

def analyze_claim(claim: str, rows: list[dict]) -> dict:
    n_a_agents = sorted({r["agent"] for r in rows if r["record_type"] == "endorsement"})
    n_p_roots = sorted({r["source_root"] for r in rows if r["root_independent"]})
    n_a, n_p = len(n_a_agents), len(n_p_roots)

    cycle_detected, cycle_path = _find_cycle(rows)
    cycle_nodes = set(cycle_path)
    origin_agents = {r["agent"] for r in rows if r["parent"] == "-"}
    return_to_origin = cycle_detected and bool(cycle_nodes & origin_agents)

    interruption_present, interruption_rows = _external_interruption(rows, cycle_nodes)

    before_vals = [r["effective_alternatives_before"] for r in rows if r["effective_alternatives_before"] is not None]
    after_vals = [r["effective_alternatives_after"] for r in rows if r["effective_alternatives_after"] is not None]
    before = before_vals[-1] if before_vals else None
    after = after_vals[-1] if after_vals else None
    if before is not None and after is not None:
        delta = after - before
        if delta < 0 and interruption_present:
            regime = "evidence_driven_convergence"
        elif delta < 0 and cycle_detected and not interruption_present:
            regime = "tunnel_contraction_risk"
        elif delta < 0:
            regime = "alternatives_decreased_unclassified"
        elif delta > 0:
            regime = "alternatives_increased"
        else:
            regime = "alternatives_unchanged"
    else:
        delta = None
        regime = "not_computed (effective_alternatives not supplied)"

    if n_p >= n_a:
        risk = "LOW"
        risk_reason = f"N_P({n_p}) >= N_A({n_a}): independent provenance keeps pace with endorsement (rule 1)."
    elif interruption_present and n_p >= 1:
        risk = "LOW"
        risk_reason = (
            f"an external interruption is present and N_P({n_p}) >= 1: independent world-side/"
            "reviewer-side resistance already entered (rule 2)."
        )
    elif n_a > n_p and cycle_detected and not interruption_present:
        risk = "HIGH"
        risk_reason = (
            f"N_A({n_a}) > N_P({n_p}), a recursive cycle was detected, and no external "
            "interruption was found (rule 3)."
        )
    else:
        risk = "MEDIUM"
        risk_reason = (
            f"N_A({n_a}) > N_P({n_p}), and either no cycle was detected or an interruption is "
            f"present with N_P == 0 (rule 4, the remaining case)."
        )

    self_application = any(r["self_application"] for r in rows)

    return {
        "claim": claim,
        "n_a": n_a,
        "n_a_agents": n_a_agents,
        "n_p": n_p,
        "n_p_roots": n_p_roots,
        "flagship": f"N_A({n_a}) {'>' if n_a > n_p else ('==' if n_a == n_p else '<')} N_P({n_p})",
        "cycle_detected": cycle_detected,
        "cycle_path": cycle_path,
        "return_to_origin": return_to_origin,
        "external_interruption_present": interruption_present,
        "external_interruption_rows": [
            {"agent": r["agent"], "record_type": r["record_type"], "evidence_ref": r["evidence_ref"]}
            for r in interruption_rows
        ],
        "effective_alternatives_before": before,
        "effective_alternatives_after": after,
        "effective_alternatives_delta": delta,
        "regime": regime,
        "risk": risk,
        "risk_reason": risk_reason,
        "self_application": self_application,
    }


# --------------------------------------------------------------------------------------------
# Report rendering ("RET SELF-AUDIT" plain-text shape)
# --------------------------------------------------------------------------------------------

def render_report(result: dict) -> str:
    lines = []
    lines.append("RET SELF-AUDIT")
    lines.append("=" * len("RET SELF-AUDIT"))
    lines.append(f"Claim: {result['claim']}")
    lines.append(
        "Source: RET-Check v0.1 (scripts/ret_check.py; methodology/P21_ret_check.md; cites "
        "GENESIS FIRST v2.0 sections 13-21, 25-30)"
    )
    lines.append(DISCLAIMER_HEADER)
    lines.append("")
    lines.append("-- Agents / Provenance --")
    lines.append(f"N_A (distinct endorsing agents)            : {result['n_a']} {result['n_a_agents']}")
    lines.append(f"N_P (distinct declared-independent roots)  : {result['n_p']} {result['n_p_roots']}")
    lines.append(f"Flagship (N_A up does-not-imply N_P up, RET-N06): {result['flagship']}")
    lines.append("")
    lines.append("-- Recursive structure (section 14, RET-N04) --")
    lines.append(f"Recursive cycle detected                   : {'YES' if result['cycle_detected'] else 'NO'}")
    if result["cycle_detected"]:
        lines.append(f"Cycle path                                 : {' -> '.join(result['cycle_path'])}")
    lines.append(f"Return-to-origin path                       : {'YES' if result['return_to_origin'] else 'NO'}")
    lines.append("")
    lines.append("-- External interruption (section 28 RET-N16; sections 29-30 AOWC RET-N17/N18) --")
    lines.append(f"External interruption present               : {'YES' if result['external_interruption_present'] else 'NO'}")
    if result["external_interruption_rows"]:
        for r in result["external_interruption_rows"]:
            lines.append(f"  - {r['agent']} ({r['record_type']}, evidence_ref={r['evidence_ref']})")
    lines.append("")
    lines.append("-- Effective alternatives (section 19, RET-N09/RET-N10; optional) --")
    if result["effective_alternatives_delta"] is None:
        lines.append("Effective alternatives supplied              : NO")
    else:
        lines.append(
            f"Effective alternatives supplied              : YES "
            f"before={result['effective_alternatives_before']} "
            f"after={result['effective_alternatives_after']} "
            f"delta={result['effective_alternatives_delta']}"
        )
    lines.append(f"Regime                                       : {result['regime']}")
    lines.append("")
    lines.append("-- RET RISK --")
    lines.append(f"RET RISK: {result['risk']}")
    lines.append(f"Reason: {result['risk_reason']}")
    if result["self_application"] and result["risk"] == "HIGH":
        lines.append("")
        lines.append(SELF_APPLICATION_SENTENCE)
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------------------------
# Top-level run() -- called by both this file's __main__ and cli/glosa's `ret check` verb
# --------------------------------------------------------------------------------------------

def run(path: "str | Path") -> dict:
    """Load `path`, analyze every claim found in it, and return a result dict:
    {"ok": bool, "path": str, "claims": [analyze_claim(...), ...], "report": "<all reports>"}.
    Raises RetCheckInputError on invalid input (caller maps that to exit code 2)."""
    rows = load_rows(path)
    grouped = group_by_claim(rows)
    claims = [analyze_claim(claim, claim_rows) for claim, claim_rows in grouped.items()]
    report = "\n".join(render_report(c) for c in claims)
    return {"ok": True, "path": str(path), "claims": claims, "report": report}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="RET-Check v0.1 -- AI-independent recursive provenance auditor "
                     "(cases/ret/PREREGISTRATION_v0_1.md)."
    )
    parser.add_argument("path", help="a JSON or CSV file of provenance rows (see this file's own docstring for the row shape)")
    parser.add_argument("--json", action="store_true", help="print the structured result as JSON instead of the plain-text RET SELF-AUDIT report")
    args = parser.parse_args(argv)

    try:
        result = run(args.path)
    except RetCheckInputError as exc:
        error = {"ok": False, "path": args.path, "error": str(exc)}
        if args.json:
            print(json.dumps(error, indent=2, ensure_ascii=False))
        else:
            print(f"RET-Check: input invalid -- {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=False))
    else:
        print(result["report"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
