#!/usr/bin/env python3
"""scripts/check_core_epistemic_structure.py — P20 Core Epistemic Structure gate.

tier: finite_diagnostic (this script's own exit code is the readout; run it and read stdout, do
not take this docstring's word for it).

Readout, not truth: this is a structural/lexical check. Given one or more file paths, it reports
whether each one carries the mandatory block from `methodology/P20_core_epistemic_structure.md`
(founder ruling 2026-09-07, Blackbox Log BBL-2026-09-07-216/217/218) — the three labelled lines
(Core Respondent / Experience-Based Expert; Interactional Expert; AI Model(s) Used) plus the
non-collapse line. It never verifies that the named people or models actually held the role
claimed; every finding printed is a HEURISTIC: text-pattern match, same limit as every other
kernel heuristic (see `kernel/glosa_kernel.py`'s own `_result` convention).

What each path is checked as:
  - `.md` / `.tex` / `.txt` (or any other non-data suffix): raw source text, via
    `kernel.glosa_kernel.ces_check_text` — looks for the three labelled lines
    ("**Label:**" Markdown or "\\textbf{Label:}"/"\\item[Label]" LaTeX both match) plus a line
    carrying the non-collapse mark (Unicode ≠, or LaTeX \\neq) at least twice.
  - `.json`: parsed, then checked as a `core_epistemic_structure` object — either the whole file
    IS one (has `respondent`/`interactional`/`ai_models`), or it has a top-level
    `core_epistemic_structure` key holding one (e.g. a `release_manifest` instance).
  - `.yaml` / `.yml`: parsed with PyYAML (this script's own dependency, not the kernel's — the
    kernel stays stdlib-only per its module docstring), same top-level-key search as `.json`.

Exit 0 = every path PASSED. Exit 1 = at least one path FAILED (or could not be checked at all —
a missing file, an unreadable/unparseable one, or a YAML file when PyYAML is not importable).

Usage: `python3 scripts/check_core_epistemic_structure.py <path> [<path> ...]`
Also callable via `./cli/glosa ces check <path> [<path> ...]` (cli/README.md) — that command
imports and calls the same `check_paths()` function below, so the two never drift.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_DIR = REPO_ROOT / "kernel"
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

try:
    import glosa_kernel as k  # noqa: E402
except Exception as exc:  # pragma: no cover - only when the kernel truly is not importable
    k = None  # type: ignore
    _KERNEL_IMPORT_ERROR = f"{type(exc).__name__}: {exc}"
else:
    _KERNEL_IMPORT_ERROR = None

try:
    import yaml  # type: ignore

    _HAVE_YAML = True
except Exception:  # pragma: no cover - exercised only in an environment without PyYAML
    yaml = None  # type: ignore
    _HAVE_YAML = False


def _plain_fail(errors: list[str]) -> dict:
    """Build a Result-shaped dict without reaching into kernel's private `_result` helper."""
    return {"ok": False, "verdict": "FAIL", "errors": errors, "warnings": [], "tier": "finite_diagnostic"}


def _check_data_path(path: Path, suffix: str) -> dict:
    """`.yaml`/`.yml` dispatch that `kernel.ces_check_path` deliberately refuses (kernel is
    stdlib-only) — parse here with PyYAML, then hand the resulting object to the kernel's
    `validate_core_epistemic_structure`, exactly like the kernel's own `.json` branch does."""
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text) if suffix in (".yaml", ".yml") else json.loads(text)
    except Exception as exc:
        return _plain_fail([f"{path}: could not parse as {suffix}: {exc}"])

    if isinstance(data, dict) and "core_epistemic_structure" in data:
        obj = data["core_epistemic_structure"]
    elif isinstance(data, dict) and {"respondent", "interactional", "ai_models"} <= set(data.keys()):
        obj = data
    else:
        return _plain_fail(
            [f"{path}: no 'core_epistemic_structure' object found (and the file is not itself shaped like one)"]
        )
    res = k.validate_core_epistemic_structure(obj)
    res["errors"] = [f"{path}: {e}" for e in res["errors"]]
    return res


def check_one(path_str: str) -> dict:
    """Check one path, returning a Result (see kernel `_result`'s shape)."""
    if k is None:
        return {"ok": False, "verdict": "FAIL", "errors": [f"kernel not importable: {_KERNEL_IMPORT_ERROR}"], "warnings": [], "tier": "Dr"}
    p = Path(path_str)
    if not p.is_file():
        return _plain_fail([f"{path_str}: file not found"])
    suffix = p.suffix.lower()
    if suffix in (".yaml", ".yml"):
        if not _HAVE_YAML:
            return _plain_fail([f"{path_str}: PyYAML is not importable — cannot check a .yaml/.yml file"])
        return _check_data_path(p, suffix)
    return k.ces_check_path(p)


def check_paths(paths: list[str]) -> tuple[int, list[dict]]:
    """Run `check_one` over every path; returns (exit_code, [{'file':..., **Result}, ...])."""
    results = []
    any_fail = False
    for path_str in paths:
        res = check_one(path_str)
        if not res.get("ok"):
            any_fail = True
        results.append({"file": path_str, **res})
    return (1 if any_fail else 0), results


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("usage: check_core_epistemic_structure.py <path> [<path> ...]")
        return 1

    exit_code, results = check_paths(argv)

    for r in results:
        if r["ok"]:
            print(f"[PASS] {r['file']}")
        else:
            print(f"[FAIL] {r['file']}")
            for e in r["errors"]:
                print(f"        {e}")

    n_pass = sum(1 for r in results if r["ok"])
    n_fail = len(results) - n_pass
    print(f"\n{n_pass} passed, {n_fail} failed — {len(results)} file(s) checked (methodology/P20_core_epistemic_structure.md)")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
