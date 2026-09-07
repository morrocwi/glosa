#!/usr/bin/env python3
"""scripts/repro_check.py -- Reproduction Ledger run/hash/compare driver (P22, `glosa repro`).

tier: Dr (specified from founder ruling BBL-2026-09-07-229 and
`design/RESISTANCE_LADDER_v0_1.md` §2/§3; will read `finite_diagnostic` once
`tests/test_reproduction_card.py` has run -- see `methodology/P22_reproduction_ledger.md`).

This module's OWN process is standard-library only (`hashlib`, `json`, `re`, `shutil`,
`subprocess`, `tempfile`) -- the same "no third-party import" convention
`tests/test_ret_check.py::test_no_network_no_third_party_import` already enforces for
`scripts/ret_check.py`, re-exercised here by `tests/test_reproduction_card.py`. Unlike
`ret_check.py`, this driver DOES launch a subprocess (`execute_run`/`verify_in_temp_dir`) --
that is its own declared job (P22 item 2/3: "Executes `command` via `subprocess`..."). The
founder's "AI = 0 at runtime" requirement (`schema/reproduction_card.schema.json`'s
`run.ai_at_runtime` const) is a property of the LLM-authoring loop around a reproduction, never a
claim that the reproduced computation itself must avoid subprocess/network access -- a card whose
own oracle computation needs `mpmath`/`numpy` (`environment.packages`, P22 §2) runs as exactly
such a subprocess, launched by this file, never imported into this file's own process.

Called from `cli/glosa`'s `cmd_repro_*` handlers by relative-path import, same convention as
`cli/glosa` already uses for `ret_check`/`check_core_epistemic_structure` -- one implementation,
never duplicated between the CLI and a standalone script.

Comparison grammar (P22 §2's own "the runner parses it mechanically per oracle.kind, never
re-interprets it loosely"): this driver recognizes exactly three tolerance grammars --
"±N% ..." (percent), "exact ... match" / "0 ... discrepancy" / "0 digit mismatch to N decimal
places" (exact), and "... categorical ..." (categorical, case-insensitive string match). A
tolerance string matching none of these returns an honest `ERROR`, never a guessed PASS/FAIL
(readout-not-truth: an uninterpreted rule is reported as uninterpreted). The external reference
value a comparison needs (the oracle's own published number, or the expected category) is supplied
by the operator via `--reference` at `glosa repro run` time -- this driver makes no network call to
fetch it itself (no live PDG/CODATA/etc. lookup is implemented anywhere in this repository, same
floor `cli/README.md` already states for `glosa cite check`).
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


class ReproCheckError(ValueError):
    """Raised on a structural problem this driver cannot proceed past (CLI maps this to exit 1)."""


# --------------------------------------------------------------------------------------------
# Hashing (P22: "SHA-256 of the declared input/output file(s), computed by the runner, never
# typed by hand")
# --------------------------------------------------------------------------------------------

def sha256_of_file(path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_labeled_files(pairs) -> "str | None":
    """Deterministic combined hash over `(label, read_path)` pairs: SHA-256 of the sorted
    "<label>:<sha256 of the file at read_path>" lines. `label` is what goes INTO the hash text
    (the declared path a reader would recognize, e.g. the original `--input`/`--output` argument);
    `read_path` is only WHERE this process actually reads the bytes from right now -- the two
    differ exactly once, for `glosa repro verify`'s isolated-copy mode (`verify_in_temp_dir`
    below), so a hash computed over a file re-executed into a throwaway temp directory still
    equals the hash `glosa repro run` recorded over the same declared name at the original run's
    own working directory (`sha256_of_files`'s own promise: independent of "absolute-path
    identity", not independent of the declared label). Returns None when `pairs` is empty."""
    pairs = [(str(label), str(read_path)) for label, read_path in (pairs or [])]
    if not pairs:
        return None
    lines = sorted(f"{label}:{sha256_of_file(read_path)}" for label, read_path in pairs)
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def sha256_of_files(paths) -> "str | None":
    """Deterministic combined hash over a declared list of files: SHA-256 of the sorted
    "<path-as-given>:<sha256 of that file>" lines, so the result is independently re-derivable by
    anyone re-running `glosa repro verify` (P22 item 3) without depending on original file order
    or absolute-path identity. Returns None when `paths` is empty -- legal for a card whose
    comparison target is entirely the command's own stdout, with no declared file artifact.
    Thin wrapper over `sha256_of_labeled_files` with label == read_path (the ordinary case: no
    isolated-copy indirection)."""
    paths = [str(p) for p in (paths or [])]
    return sha256_of_labeled_files([(p, p) for p in paths])


def _extract_self_reported_hashes(stdout_text: str) -> "tuple[str | None, str | None]":
    """A runner script MAY compute its own `input_hash`/`output_hash` internally and print them
    as top-level keys in its own JSON stdout (exactly the way `_extract_observed` already reads
    an `observed` key back) -- e.g. a card whose real input is a pinned external byte string
    (a git blob at a commit, not a static file sitting in this repo) fetched and hashed by the
    runner itself, never a file this driver could hash by path. When present, these self-reported
    values are read back verbatim, never recomputed a second, different way (P22's "computed by
    the runner" is satisfied by the runner computing it; this driver's own job is to read that
    computation back honestly). Returns `(None, None)` when stdout is not a JSON object or
    carries neither key -- never guessed, never defaulted to a declared-file hash inferred from
    context this function does not have."""
    text = (stdout_text or "").strip()
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None, None
    if not isinstance(data, dict):
        return None, None
    input_hash = data.get("input_hash") or data.get("input_sha256")
    output_hash = data.get("output_hash") or data.get("output_sha256")
    return (str(input_hash) if input_hash else None), (str(output_hash) if output_hash else None)


def compute_hashes(stdout_text: str, declared_input_hash: "str | None" = None,
                    declared_output_hash: "str | None" = None) -> dict:
    """The ONE shared hash-computation rule `glosa repro run` (first execution) and `glosa repro
    verify` (independent re-execution) both call, so the two are always compared apples-to-apples
    -- never two different formulas that happen to usually agree. Priority, applied independently
    for input vs. output:

    1. A self-reported `input_sha256`/`output_sha256` (or `input_hash`/`output_hash`) top-level
       key in the command's own JSON stdout (`_extract_self_reported_hashes`) -- read back
       verbatim, taking priority over a caller-supplied declared-file hash, because a runner that
       bothers to self-report is naming the exact bytes IT considers its own input/output, which
       may not be a file this driver could hash by path at all (`cases/repro/
       run_EQ-068_higgs_pdg.py`'s pinned git-blob input is the paradigm case this exists for).
    2. `declared_input_hash`/`declared_output_hash` -- the caller's own `sha256_of_files`/
       `sha256_of_labeled_files` result over `--input`/`--output` file(s), when such files were
       declared (unchanged from P22 §2's original convention).
    3. (output only) SHA-256 of the command's own raw stdout bytes, when stdout is non-empty and
       neither (1) nor (2) produced a value -- the bare "the output IS this run's stdout" case
       (`cases/repro/EQ-045_gauge_dim.json`'s own shape: no declared output file, no self-report,
       the printed JSON result itself is what a reader would compare).
    4. `None` -- honestly absent, never fabricated to fill the field.
    """
    self_input_hash, self_output_hash = _extract_self_reported_hashes(stdout_text)
    input_hash = self_input_hash or declared_input_hash
    output_hash = self_output_hash or declared_output_hash
    if output_hash is None and (stdout_text or "").strip():
        output_hash = hashlib.sha256((stdout_text or "").encode("utf-8")).hexdigest()
    return {"input_hash": input_hash, "output_hash": output_hash}


# --------------------------------------------------------------------------------------------
# Tolerance parsing + comparison
# --------------------------------------------------------------------------------------------

_PERCENT_RE = re.compile(r"±?\s*(\d+(?:\.\d+)?)\s*%")
_ZERO_DISCREPANCY_RE = re.compile(r"\b0\s*(?:digit\s+mismatch|discrepancy)\b", re.I)
_EXACT_WORD_RE = re.compile(r"\bexact\b", re.I)
_EXACT_CONTEXT_RE = re.compile(r"match|equal|identical|digit", re.I)
_CATEGORICAL_RE = re.compile(r"\bcategorical\b", re.I)


def parse_tolerance(tolerance: str) -> dict:
    """Classify a `preregistered_prediction.tolerance` string into one of the three mechanical
    comparison grammars this driver implements, or `{"kind": "unparseable", ...}` when it
    recognizes none of them. `compare()` below turns `"unparseable"` into an honest `ERROR`
    result, never a guessed PASS/FAIL."""
    text = (tolerance or "").strip()
    m = _PERCENT_RE.search(text)
    if m:
        return {"kind": "percent", "pct": float(m.group(1)), "raw": text}
    # Categorical is checked BEFORE the generic "exact" grammar: a string like "exact categorical
    # match (LOW/MEDIUM/HIGH -- no numeric band)" (design/RESISTANCE_LADDER_v0_1.md §6 Card 2's
    # own worked tolerance text) contains the word "exact" too, but names its own, more specific
    # grammar -- categorical string equality, not digit-for-digit exactness.
    if _CATEGORICAL_RE.search(text):
        return {"kind": "categorical", "raw": text}
    if _ZERO_DISCREPANCY_RE.search(text) or (_EXACT_WORD_RE.search(text) and _EXACT_CONTEXT_RE.search(text)):
        return {"kind": "exact", "raw": text}
    return {"kind": "unparseable", "raw": text}


def compare(observed: Any, reference: Any, tolerance: str) -> dict:
    """Compare `observed` (from the run's own JSON stdout / declared output, see
    `_extract_observed`) against `reference` (the external oracle's own value, supplied by the
    operator -- see this module's own docstring) per `tolerance`'s parsed grammar. Returns
    `{"status": "PASS"|"FAIL"|"ERROR", "observed": ..., "deviation": ..., "note": str}`.

    `reference=None` always yields `ERROR` for every grammar below (percent/exact/categorical all
    need one) -- this driver never substitutes a default or infers one; a card whose observed
    value is already a self-contained PASS/FAIL string (rare, but legal) should be given as
    `reference` explicitly by the caller instead of relying on this function to guess."""
    spec = parse_tolerance(tolerance)
    kind = spec["kind"]

    if kind == "percent":
        if reference is None:
            return {"status": "ERROR", "observed": observed, "deviation": None,
                     "note": "percent tolerance declared but no --reference value was supplied to compare against"}
        try:
            obs_f, ref_f = float(observed), float(reference)
        except (TypeError, ValueError):
            return {"status": "ERROR", "observed": observed, "deviation": None,
                     "note": "observed/reference could not both be parsed as numbers for a percent-tolerance comparison"}
        if ref_f == 0:
            return {"status": "ERROR", "observed": observed, "deviation": None,
                     "note": "reference value is 0 -- a percent deviation is undefined"}
        deviation = abs(obs_f - ref_f) / abs(ref_f)
        status = "PASS" if deviation <= spec["pct"] / 100.0 else "FAIL"
        return {"status": status, "observed": observed, "deviation": deviation,
                "note": f"|observed-reference|/|reference| = {deviation:.6f}, tolerance = {spec['pct']}% "
                        f"(tolerance text: {spec['raw']!r})"}

    if kind == "exact":
        if reference is None:
            return {"status": "ERROR", "observed": observed, "deviation": None,
                     "note": "exact-match tolerance declared but no --reference value was supplied to compare against"}
        match = str(observed).strip() == str(reference).strip()
        return {"status": "PASS" if match else "FAIL", "observed": observed,
                "deviation": 0 if match else "mismatch",
                "note": f"exact string match against reference (tolerance text: {spec['raw']!r}): {match}"}

    if kind == "categorical":
        if reference is None:
            return {"status": "ERROR", "observed": observed, "deviation": None,
                     "note": "categorical tolerance declared but no --reference value (the expected category) was supplied"}
        match = str(observed).strip().upper() == str(reference).strip().upper()
        return {"status": "PASS" if match else "FAIL", "observed": observed,
                "deviation": "match" if match else "mismatch",
                "note": f"categorical match against {reference!r} (tolerance text: {spec['raw']!r}): {match}"}

    return {"status": "ERROR", "observed": observed, "deviation": None,
            "note": f"tolerance {tolerance!r} did not match any grammar this driver implements "
                    "(percent / exact / categorical) -- reported as ERROR, never guessed"}


def _extract_observed(stdout_text: str) -> Any:
    """Prefer a JSON object on stdout carrying an 'observed' key; else fall back to the raw
    stripped stdout text as the observed value. Never fabricates a value the command itself did
    not produce."""
    text = (stdout_text or "").strip()
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return text
    if isinstance(data, dict) and "observed" in data:
        return data["observed"]
    return text


# --------------------------------------------------------------------------------------------
# Execution (P22 item 2: `glosa repro run`) and independent re-execution (P22 item 3: `glosa
# repro verify`, maker != checker)
# --------------------------------------------------------------------------------------------

def execute_run(command: str, timeout: int = 600) -> dict:
    """Execute `command` via `subprocess` in the CURRENT working directory (the caller -- `cli/
    glosa`'s `cmd_repro_run` -- decides that directory; this function never changes it). This
    driver's own Python process stays stdlib-only; the launched command is a separate process and
    may do anything, including import mpmath/numpy for its own declared oracle computation
    (P22's `environment.packages` exception). Returns
    `{"stdout": str, "stderr": str, "returncode": int, "observed": Any}`. Raises
    `ReproCheckError` if the command cannot even be launched -- never silently swallowed."""
    try:
        proc = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.SubprocessError) as exc:
        raise ReproCheckError(f"could not execute command {command!r}: {exc}") from exc
    return {
        "stdout": proc.stdout, "stderr": proc.stderr, "returncode": proc.returncode,
        "observed": _extract_observed(proc.stdout),
    }


def verify_in_temp_dir(command: str, input_paths=None, output_paths=None, timeout: int = 600,
                        cwd: "str | None" = None) -> dict:
    """P22 item 3 (`glosa repro verify`): re-execute `command` fresh, under an identity DIFFERENT
    from whoever ran it first (the CLI layer enforces the identity check; this function only does
    the mechanical re-execution). Two execution modes (integration fix, 2026-09-08, this driver's
    original isolated-copy-only mode could not resolve a `command` that names a path relative to
    this repo's own root, e.g. `python3 cases/repro/run_EQ-045_gauge_dim.py` -- both first-batch
    real cards use exactly that shape):

    - `cwd=None` (default when the CALLER does not pin one): a clean, throwaway temporary
      directory. Every declared input file is copied in by its own basename first, so the command
      sees the same declared inputs but cannot silently depend on unrelated state left over in the
      original directory; hashing still LABELS each file by its originally-declared path (never
      the throwaway copy's own location -- `sha256_of_labeled_files`), so the recomputed hash
      matches the run-time hash for identical content regardless of where the bytes physically
      sat. Best for a self-contained command with no repo-relative file references.
    - `cwd=<a real directory>` (the CLI passes the repo's own checkout root here by default, see
      `cli/glosa`'s `cmd_repro_verify`): the command runs there directly, so a `command` naming a
      path relative to that checkout (the common case for a real Reproduction Card in this repo)
      resolves exactly as it did at `glosa repro run` time. Declared input/output files are hashed
      at their given paths directly (no copy needed -- this already IS the tracked checkout, not
      unrelated stray state); a reader who wants strict empty-directory isolation for a
      self-contained command can still get it by not pinning a `cwd`.

    In both modes, once the process exits, `input_hash`/`output_hash` are computed by
    `compute_hashes` (self-reported stdout JSON keys, else the declared-file hash, else -- output
    only -- a raw hash of the command's own stdout bytes) -- the SAME function `glosa repro run`
    calls, so a verify run is always compared against a run-time hash produced by the identical
    rule. Returns `{"input_hash": str|None, "output_hash": str|None, "returncode": int,
    "stdout": str, "stderr": str}`. Never touches the original card file -- the CALLER compares
    the two hashes and writes the resulting `review_report.yaml`."""
    isolated = cwd is None
    work_dir = Path(tempfile.mkdtemp(prefix="glosa-repro-verify-")) if isolated else Path(cwd)
    try:
        if isolated:
            copied_pairs = []
            for src in (input_paths or []):
                src_p = Path(src)
                if src_p.is_file():
                    dst = work_dir / src_p.name
                    shutil.copy2(src_p, dst)
                    copied_pairs.append((str(src_p), str(dst)))
            declared_input_hash = sha256_of_labeled_files(sorted(copied_pairs)) if copied_pairs else None
        else:
            existing_pairs = [(str(p), str(p)) for p in (input_paths or []) if Path(p).is_file()]
            declared_input_hash = sha256_of_labeled_files(sorted(existing_pairs)) if existing_pairs else None
        try:
            proc = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout, cwd=str(work_dir))
        except (OSError, subprocess.SubprocessError) as exc:
            raise ReproCheckError(f"could not execute command {command!r} during verify: {exc}") from exc
        if isolated:
            resolved_pairs = []
            for out in (output_paths or []):
                candidate = work_dir / Path(out).name
                resolved_pairs.append((str(out), str(candidate) if candidate.is_file() else str(out)))
            existing_output_pairs = [(label, p) for label, p in resolved_pairs if Path(p).is_file()]
        else:
            existing_output_pairs = [(str(p), str(p)) for p in (output_paths or []) if Path(p).is_file()]
        declared_output_hash = sha256_of_labeled_files(sorted(existing_output_pairs)) if existing_output_pairs else None
        hashes = compute_hashes(proc.stdout, declared_input_hash, declared_output_hash)
        return {
            "input_hash": hashes["input_hash"], "output_hash": hashes["output_hash"],
            "returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
        }
    finally:
        if isolated:
            shutil.rmtree(work_dir, ignore_errors=True)


# --------------------------------------------------------------------------------------------
# RET-Check conversion (P22 item 4 / `design/RESISTANCE_LADDER_v0_1.md` §4's mapping table)
# --------------------------------------------------------------------------------------------

_INDEPENDENCE_ORDER = ("I0", "I1", "I2", "I3", "I4", "I5")


def _independence_at_least_i2(independence_class) -> bool:
    try:
        return _INDEPENDENCE_ORDER.index(independence_class) >= _INDEPENDENCE_ORDER.index("I2")
    except ValueError:
        return False


def to_ret_rows(card: dict, claim_id: str, reviewer_independence_class: "str | None" = None,
                 evidence_ref: "str | None" = None) -> list:
    """Convert one reproduction_card into RET-Check provenance rows
    (`scripts/ret_check.py`'s row shape), per `design/RESISTANCE_LADDER_v0_1.md` §4's mapping
    table. Raises `ReproCheckError`:

    - for `oracle.kind == "coq_kernel"` -- machine-side resistance (R2), never converted into a
      RET-Check world-side/reviewer-side row (P23's own "never blend into one number" rule,
      enforced here mechanically, not just documented).
    - for `oracle.kind == "human_review"` when `reviewer_independence_class` is missing or below
      `I2` (`P6`'s ladder) -- the row is refused, never silently marked independent (design §4's
      own "else the row is refused ... never silently marked independent").
    """
    oracle = card.get("oracle") or {}
    kind = oracle.get("kind")
    ref = evidence_ref if evidence_ref is not None else card.get("id")

    if kind == "coq_kernel":
        raise ReproCheckError(
            "Coq closure is machine-side resistance (R2); run `glosa score` for that rung, not "
            "`glosa repro to-ret`."
        )

    source_root = oracle.get("source") or "unknown-oracle-source"
    if oracle.get("version"):
        source_root = f"{source_root} ({oracle['version']})"

    if kind in ("published_value", "independent_implementation", "public_dataset"):
        return [{
            "claim": claim_id,
            "agent": card.get("id", "unknown-card"),
            "parent": "-",
            "source_root": source_root,
            "root_independent": True,
            "record_type": "world_record",
            "evidence_ref": ref,
        }]

    if kind == "human_review":
        if not _independence_at_least_i2(reviewer_independence_class):
            raise ReproCheckError(
                f"oracle.kind is 'human_review' but the reviewer's independence_class is "
                f"{reviewer_independence_class!r}, not >= I2 -- pass "
                "--review-report pointing at a review_report.yaml whose independence_class is "
                "I2 or above (P6's ladder); the row is refused, never silently marked independent."
            )
        return [{
            "claim": claim_id,
            "agent": (card.get("lineage") or {}).get("run_by", "unknown-reviewer"),
            "parent": "-",
            "source_root": source_root,
            "root_independent": True,
            "record_type": "review",
            "evidence_ref": ref,
        }]

    raise ReproCheckError(f"unrecognized or unconvertible oracle.kind {kind!r}")
