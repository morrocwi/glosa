#!/usr/bin/env python3
"""scripts/ret_check.py -- RET-Check v0.3: an AI-independent recursive provenance auditor.

tier: Dr (specified from `cases/ret/PREREGISTRATION_v0_1.md` and the theory source below;
independently unreviewed; will read `finite_diagnostic` once `tests/test_ret_check.py` has run --
see `methodology/P21_ret_check.md`).

v0.3 (2026-09-08, founder ruling `BBL-2026-09-07-229`, `design/RESISTANCE_LADDER_v0_1.md` sec 4)
adds exactly ONE capability on top of v0.2: `reproduction_card_to_row()` below, a converter from a
Reproduction Card (methodology P22, owned by stream S1) into one RET-Check provenance row -- the
RET RISK formula, `analyze_claim()`, `_find_cycle()`, and `_external_interruption()` are BYTE-FOR-
BYTE UNCHANGED from v0.2 (`cases/ret/PREREGISTRATION_v0_1.md`'s own standing rule: never retune the
formula to make a case pass; this is a new INPUT PATH into the same graph algorithm, never a rule
change). See the converter's own docstring below and `cases/ret/PREREGISTRATION_v0_1.md`'s v0.3
addendum (scenario F) for the one new preregistered case this adds.

Founder order (verbatim, Blackbox Log `BBL-2026-09-07-223`): "RET-Check v0.1 -- AI-independent
recursive provenance auditor: โปรแกรมเล็ก Python standard library ไม่มี LLM (AI=0 ตอน runtime) ..."
-- a small Python **standard-library-only** program, no LLM, `AI = 0` at runtime, that reads
CSV/JSON provenance rows and computes N_A / N_P / recursive cycles / external interruption, then
prints a RET SELF-AUDIT report with a RET RISK label. This module implements the founder's spec
using THE PAPER'S OWN definitions -- it does not invent new ones. Theory source:
`The_Recursive_Epistemic_Tunnel_GENESIS_FIRST_FULL_v2_0.md` (RET GENESIS FIRST v2.0), sections
13-21 and 25-30. Every computed quantity below cites its section, its RET-Nxx working alias, and
(as of v0.2, 2026-09-08) the Toledo code the registrar assigned it (`methodology/P19`; Toledo
v1.5.0 pending, concept DOI 10.5281/zenodo.22537318; full table:
Toledo repo's registry/proposals/recursive_epistemic_tunnel_v2_0.merged.json): RET-N04 = EQ-015/H.41.v1,
RET-N05 = weld/H.35.v1, RET-N06 = weld/H.36.v1, RET-N07 = A.8/M.20.v1, RET-N09 = weld/H.37.v1,
RET-N10 = EQ-015/H.43.v1, RET-N16 = A.8/M.21.v1, RET-N17 = A.8/M.22.v1, RET-N18 = A.8/M.23.v1.

READOUT, NOT TRUTH -- read `cases/ret/PREREGISTRATION_v0_1.md`'s "What the program can NOT verify"
section before trusting any report this script prints. In summary: `root_independent` (is a
provenance root independent) and `record_type: world_record` / an independent `review` (is a
record world-side) are INPUT DECLARATIONS supplied by the case author. This program audits the
DECLARED graph structure -- who cites whom, which roots and records are declared independent --
never whether those declarations are true. Every report header restates this.

CORRECTION (2026-09-08, before any case was tuned to match): N_P(c) is the number of DISTINCT
PROVENANCE ROOTS, full stop -- the founder's own Mirror example has 1 shared root S1, and it reads
N_P = 1, not 0, even though that root is not independent. An earlier draft of this module counted
only independence-declared roots as N_P, which mis-scored the Mirror example as N_P = 0. That
independence-only count is now its own separate, explicitly labelled readout, N_P^ind(c) -- see
below. This is a correction of the operator's definition to match the paper/founder text, not a
retuning of the risk formula to make any case pass or fail differently (cases/ret/
PREREGISTRATION_v0_1.md carries the same dated note; the RET RISK label itself is unchanged for
every pre-registered scenario -- rules 1-4 below always used the independence-only count and
still do, now spelled N_P^ind rather than N_P).

Computed quantities and their section citations:

  N_A(c)     -- number of distinct agents with record_type == "endorsement" for claim c.
                Section 15 (the Epistemic Mirror Effect): "N_A(c) = number of endorsing agents".
  N_P(c)     -- number of DISTINCT PROVENANCE ROOTS (source_root values) for c, regardless of
                whether any of them is declared independent. Section 15's literal N_P(c) as a raw
                root count, refined by section 16's typed provenance structure
                Pi(c) = (V_c, E_c, tau_c) (RET-N07, Toledo A.8/M.20.v1), which is what N_P^ind
                narrows down to below.
  N_P^ind(c) -- number of those roots ADDITIONALLY declared root_independent == true. A separate,
                narrower readout of the same Pi(c) structure -- root_independent is an input
                declaration (see the disclaimer above), never derived by this program. The RET
                RISK formula below is computed from N_P^ind(c), never the raw N_P(c): a root that
                is merely present is not the same claim as a root that is independent, and only
                the latter should be read as resistance against a tunnel.
  Flagship   -- N_A(c) up  does-not-imply  N_P(c) up. Section 15, RET-N06 (non-entailment; Toledo
                weld/H.36.v1). Reported against the raw root count N_P(c), matching the paper's
                own literal reading.
  Recursive cycle -- any directed cycle in the parent -> agent graph for c. Section 14, RET-N04
              (Toledo EQ-015/H.41.v1; "a minimal cycle is a_i -> a_j -> a_i"; a multi-agent cycle
              generalizes this). "Return-to-origin" additionally reports whether the cycle
              includes a row whose parent == "-" (an origin node for that claim).
  External interruption -- a world_record row, or a review row declared root_independent == true,
              whose own ancestry (walked backward through parent edges) does not intersect any
              node of a detected recursion cycle. Operationalizes section 28's AI-Independent
              Consequence Requirement (RET-N16, Toledo A.8/M.21.v1: CausalAncestry(y) is not a
              subset of the recursive network up to the freeze time) and sections 29-30's AI-Off
              World-Closure (RET-N17, Toledo A.8/M.22.v1 / RET-N18, Toledo A.8/M.23.v1) as a
              graph-lineage test this program can actually run. When no cycle exists at all, any
              qualifying world_record/review row counts (there is nothing recursive for its
              lineage to "pass through").
  Effective-alternatives regime (optional; only when effective_alternatives_before/after are
              supplied on at least one row of the claim) -- section 19: "evidence_driven_convergence"
              (RET-N09, Toledo weld/H.37.v1: delta < 0 AND an external interruption is present) vs.
              "tunnel_contraction_risk" (RET-N10, Toledo EQ-015/H.43.v1: delta < 0, a cycle is
              present, and no external interruption is present). This label is a report
              annotation; it does not feed the
              RET RISK formula below (the founder specified that formula in terms of N_A, N_P^ind,
              cycle, and interruption only -- see the preregistration).

RET RISK formula (pre-registered in `cases/ret/PREREGISTRATION_v0_1.md`, exact, first match wins;
uses N_P^ind, the independence-declared root count, never the raw root count N_P):

  1. LOW    if N_P^ind(c) >= N_A(c)
  2. LOW    if an external interruption is present AND N_P^ind(c) >= 1
  3. HIGH   if N_A(c) > N_P^ind(c) AND a recursive cycle is detected AND no external interruption
  4. MEDIUM otherwise (N_A(c) > N_P^ind(c), and either no cycle, or an interruption present but
            N_P^ind(c) == 0)

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


class RetCheckConversionError(ValueError):
    """v0.3. Raised by `reproduction_card_to_row()` when a Reproduction Card's `oracle.kind` must
    be REFUSED per `design/RESISTANCE_LADDER_v0_1.md` sec 4's mapping table -- never silently
    converted into a provenance row. Distinct from `RetCheckInputError` (a structural input-shape
    problem at THIS module's own CLI boundary, exit code 2): a conversion refusal is a deliberate
    design-rule refusal raised for the CALLER (`glosa repro to-ret`, owned by stream S1) to map to
    exit code 1, per the design doc's own "exits 1 with: ..." wording -- this module never exits
    the process itself for this error, it only raises."""


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
# v0.3 converter: Reproduction Card -> one RET-Check provenance row
# (design/RESISTANCE_LADDER_v0_1.md sec 4, "external oracle = external interruption")
# --------------------------------------------------------------------------------------------

INDEPENDENCE_CLASS_LADDER = ("I0", "I1", "I2", "I3", "I4", "I5")  # P6's ladder, methodology/P06_independent_check.md

EXTERNAL_ORACLE_KINDS = ("published_value", "independent_implementation", "public_dataset")

COQ_KERNEL_REFUSAL_MESSAGE = (
    "Coq closure is machine-side resistance (R2); run `glosa score` for that rung, "
    "not `glosa ret check`."
)


def _independence_at_least(independence_class: "str | None", floor: str) -> bool:
    """True iff `independence_class` is on P6's I0..I5 ladder and at or above `floor`. An
    unrecognized or missing class is treated as NOT meeting any floor (fail-closed -- see
    reproduction_card_to_row()'s human_review branch, which must refuse rather than guess)."""
    if independence_class not in INDEPENDENCE_CLASS_LADDER:
        return False
    return INDEPENDENCE_CLASS_LADDER.index(independence_class) >= INDEPENDENCE_CLASS_LADDER.index(floor)


def reproduction_card_to_row(
    card: dict,
    claim: str,
    *,
    reviewer_identity: "str | None" = None,
    independence_class: "str | None" = None,
) -> dict:
    """v0.3. Convert ONE Reproduction Card (methodology P22, `schema/reproduction_card.schema.json`,
    owned by stream S1) into exactly one RET-Check provenance row, per
    `design/RESISTANCE_LADDER_v0_1.md` sec 4's mapping table. This is the ONLY new capability v0.3
    adds -- `analyze_claim()`, `_find_cycle()`, `_external_interruption()`, and the RET RISK
    formula above are byte-for-byte unchanged; a card converted through this function becomes a
    row that `analyze_claim()` processes exactly like any hand-authored row in
    `cases/ret/A_mirror.json` etc. -- one graph algorithm, two input paths, never a new rule.

    Intended caller: `cli/glosa`'s `glosa repro to-ret` (owned by stream S1), which reads the card
    file off disk, looks up an `independence_class` from a linked `review_report.yaml` when
    `oracle.kind == "human_review"`, and appends/writes the returned row into a case file this
    module's own `run()`/`analyze_claim()` then reads.

    `claim` is the RET-Check claim id this row is being attached to -- NOT read from the card. A
    Reproduction Card backs zero or more Toledo codes (`card["toledo_codes"]`), but WHICH
    RET-Check claim it resists is a fact about how the caller is using it, supplied here
    explicitly, never inferred.

    Refuses (raises `RetCheckConversionError`, no row returned -- nothing is ever silently
    downgraded to a weaker row instead) for:

      - `card["oracle"]["kind"] == "coq_kernel"`: that resistance is machine-side (rung R2 of the
        resistance ladder, design doc sec 1) -- `COQ_KERNEL_REFUSAL_MESSAGE` verbatim, sec 4's own
        refusal text. Never converted into a RET-Check world/reviewer-side row: this is what keeps
        R2's machine-side count and RET's `N_P^ind` world/reviewer-side count from ever blending
        into one number (design doc sec 1, "machine-side vs. world-side, kept explicitly
        separate").
      - `card["oracle"]["kind"] == "human_review"` when `independence_class` is not `>= "I2"`
        (`methodology/P06_independent_check.md`'s I0..I5 ladder) -- refused rather than silently
        marked `root_independent = true` (design doc sec 4's own instruction: "else the row is
        refused ... never silently marked independent").
      - any other/missing `oracle.kind`, or a missing `oracle.source` for an external-oracle kind:
        the card is malformed for conversion purposes -- refused with an explanation, never
        guessed.

    Mapping (design doc sec 4 table, "external oracle = external interruption"):

      published_value / independent_implementation / public_dataset
          -> record_type "world_record", agent = card["id"], parent = "-",
             source_root = "<oracle.source> v<oracle.version>" (bare source if no version is
             pinned yet), root_independent = True unconditionally -- "the oracle is, by
             construction, outside the claim's own authoring network" (design doc sec 4).
      human_review (independence_class >= I2)
          -> record_type "review", agent = reviewer_identity or card["lineage"]["run_by"],
             source_root = the same reviewer identity, root_independent = True.

    The returned dict is passed through this module's own `_validate_row()` before being handed
    back, so a converted row and a hand-authored row are validated by exactly the same code path
    (one fact in one home: row-shape validation lives in `_validate_row()` alone)."""
    oracle = card.get("oracle") or {}
    kind = oracle.get("kind")
    card_id = card.get("id", "<no-id>")

    if kind == "coq_kernel":
        raise RetCheckConversionError(COQ_KERNEL_REFUSAL_MESSAGE)

    if kind in EXTERNAL_ORACLE_KINDS:
        source = oracle.get("source")
        if not source:
            raise RetCheckConversionError(
                f"reproduction_card {card_id!r}: oracle.kind {kind!r} requires oracle.source to "
                "be named before it can become a RET-Check provenance row."
            )
        version = oracle.get("version")
        source_root = f"{source} v{version}" if version else source
        toledo_codes = card.get("toledo_codes") or []
        evidence_ref = f"reproduction_card:{card_id}" + (
            f" toledo_codes={toledo_codes}" if toledo_codes else ""
        )
        raw = {
            "claim": claim,
            "agent": card_id,
            "parent": "-",
            "source_root": source_root,
            "root_independent": True,
            "record_type": "world_record",
            "evidence_ref": evidence_ref,
        }
        return _validate_row(raw, row_index=-1)

    if kind == "human_review":
        if not _independence_at_least(independence_class, "I2"):
            raise RetCheckConversionError(
                f"reproduction_card {card_id!r}: oracle.kind == 'human_review' requires an "
                "independence_class >= I2 (methodology/P06_independent_check.md's I0..I5 ladder) "
                f"to be marked root_independent -- received {independence_class!r}. Refusing to "
                "silently mark this row independent."
            )
        lineage = card.get("lineage") or {}
        identity = reviewer_identity or lineage.get("run_by")
        if not identity:
            raise RetCheckConversionError(
                f"reproduction_card {card_id!r}: oracle.kind == 'human_review' requires a "
                "reviewer identity (reviewer_identity= argument, or lineage.run_by on the card) "
                "to name the row's agent/source_root."
            )
        raw = {
            "claim": claim,
            "agent": identity,
            "parent": "-",
            "source_root": identity,
            "root_independent": True,
            "record_type": "review",
            "evidence_ref": (
                f"reproduction_card:{card_id} (human_review, independence_class={independence_class})"
            ),
        }
        return _validate_row(raw, row_index=-1)

    raise RetCheckConversionError(
        f"reproduction_card {card_id!r}: unrecognized oracle.kind {kind!r} -- expected one of "
        f"{EXTERNAL_ORACLE_KINDS + ('human_review', 'coq_kernel')}."
    )


# --------------------------------------------------------------------------------------------
# Graph analysis (section 14 RET-N04/Toledo EQ-015/H.41.v1 cycle; section 28/29-30 external interruption)
# --------------------------------------------------------------------------------------------

def _find_cycle(rows: list[dict]) -> "tuple[bool, list[str]]":
    """Directed-cycle detection over parent -> agent edges (section 14, RET-N04, Toledo EQ-015/H.41.v1). Returns
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
    """Section 28 (RET-N16, Toledo A.8/M.21.v1) / sections 29-30 (RET-N17, Toledo A.8/M.22.v1 / RET-N18, Toledo A.8/M.23.v1): a world_record row, or a review row
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
    # N_P -- distinct provenance roots, period (section 15's literal reading, corrected
    # 2026-09-08: the founder's own Mirror example is 1 shared root S1 -> N_P = 1, not 0, even
    # though that root is NOT declared independent). Independence is a SEPARATE readout, N_P^ind
    # (section 16's Pi(c) typed provenance distinction) -- see cases/ret/PREREGISTRATION_v0_1.md's
    # dated correction note.
    n_p_roots = sorted({r["source_root"] for r in rows})
    n_p_ind_roots = sorted({r["source_root"] for r in rows if r["root_independent"]})
    n_a, n_p, n_p_ind = len(n_a_agents), len(n_p_roots), len(n_p_ind_roots)

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

    # RET RISK is an INDEPENDENCE question, not a raw-root-count question -- rules 1-4 below use
    # N_P^ind (n_p_ind), never the raw root count N_P (n_p). A shared, non-independent root still
    # counts once toward N_P (the founder's Mirror correction), but it must not by itself lower
    # risk the way an independent root would.
    if n_p_ind >= n_a:
        risk = "LOW"
        risk_reason = f"N_P^ind({n_p_ind}) >= N_A({n_a}): independent provenance keeps pace with endorsement (rule 1)."
    elif interruption_present and n_p_ind >= 1:
        risk = "LOW"
        risk_reason = (
            f"an external interruption is present and N_P^ind({n_p_ind}) >= 1: independent "
            "world-side/reviewer-side resistance already entered (rule 2)."
        )
    elif n_a > n_p_ind and cycle_detected and not interruption_present:
        risk = "HIGH"
        risk_reason = (
            f"N_A({n_a}) > N_P^ind({n_p_ind}), a recursive cycle was detected, and no external "
            "interruption was found (rule 3)."
        )
    else:
        risk = "MEDIUM"
        risk_reason = (
            f"N_A({n_a}) > N_P^ind({n_p_ind}), and either no cycle was detected or an interruption "
            f"is present with N_P^ind == 0 (rule 4, the remaining case)."
        )

    self_application = any(r["self_application"] for r in rows)

    return {
        "claim": claim,
        "n_a": n_a,
        "n_a_agents": n_a_agents,
        "n_p": n_p,
        "n_p_roots": n_p_roots,
        "n_p_ind": n_p_ind,
        "n_p_ind_roots": n_p_ind_roots,
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
        "Source: RET-Check v0.3 (scripts/ret_check.py; methodology/P21_ret_check.md; cites "
        "GENESIS FIRST v2.0 sections 13-21, 25-30)"
    )
    lines.append(DISCLAIMER_HEADER)
    lines.append("")
    lines.append("-- Agents / Provenance --")
    lines.append(f"N_A (distinct endorsing agents)            : {result['n_a']} {result['n_a_agents']}")
    lines.append(f"N_P (distinct provenance roots)             : {result['n_p']} {result['n_p_roots']}")
    lines.append(f"N_P^ind (roots declared independent)        : {result['n_p_ind']} {result['n_p_ind_roots']}")
    lines.append(f"Flagship (N_A up does-not-imply N_P up, RET-N06/Toledo weld/H.36.v1): {result['flagship']}")
    lines.append("")
    lines.append("-- Recursive structure (section 14, RET-N04, Toledo EQ-015/H.41.v1) --")
    lines.append(f"Recursive cycle detected                   : {'YES' if result['cycle_detected'] else 'NO'}")
    if result["cycle_detected"]:
        lines.append(f"Cycle path                                 : {' -> '.join(result['cycle_path'])}")
    lines.append(f"Return-to-origin path                       : {'YES' if result['return_to_origin'] else 'NO'}")
    lines.append("")
    lines.append("-- External interruption (section 28 RET-N16/Toledo A.8/M.21.v1; sections 29-30 AOWC RET-N17/Toledo A.8/M.22.v1, RET-N18/Toledo A.8/M.23.v1) --")
    lines.append(f"External interruption present               : {'YES' if result['external_interruption_present'] else 'NO'}")
    if result["external_interruption_rows"]:
        for r in result["external_interruption_rows"]:
            lines.append(f"  - {r['agent']} ({r['record_type']}, evidence_ref={r['evidence_ref']})")
    lines.append("")
    lines.append("-- Effective alternatives (section 19, RET-N09/Toledo weld/H.37.v1, RET-N10/Toledo EQ-015/H.43.v1; optional) --")
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
        description="RET-Check v0.3 -- AI-independent recursive provenance auditor "
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
