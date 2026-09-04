#!/usr/bin/env python3
"""validate_examples.py -- CI's real schema-validate check (MUST-5).

tier: finite_diagnostic (this script IS the mechanical check; run it, read its own output).

Replaces the CI job that used to reimplement schema validation inline with a bare
`jsonschema.validate(instance, schema)` call -- that call cannot resolve this repo's cross-file
`$ref`s (raises an uncaught RefResolutionError the job's except-clause never catches) AND walked
a `schema/examples/<name>/pass|fail/*.json` directory layout that does not exist on disk (the
real layout is flat `schema/examples/<name>.example.json` files plus one `schema/examples/fail/`
directory). That combination silently reported "checked 0 example file(s)" and exited 0 green.

This script:
  1. Imports `kernel/glosa_kernel.py`'s OWN `_validator_for`/`_schema_validate` (the RefResolver
     + store pattern documented in `schema/README.md`) instead of reimplementing it -- one-fact-
     one-home: the resolver pattern lives in the kernel, not duplicated here.
  2. Validates every `schema/examples/*.example.json` against `schema/<name>.schema.json`
     (derived from the filename, matching the 1:1 naming convention `schema/README.md`
     documents) via `validate_claim_card` when the name is `claim_card` (schema + kernel rules
     together) and via the raw schema validator otherwise.
  3. Validates every `schema/examples/fail/*.json` fixture and asserts it is REJECTED -- either
     by the JSON Schema itself, or (for `claim_card`-shaped fixtures, per `schema/README.md`'s
     own table) by `validate_claim_card`'s kernel-only rules. A fixture that validates cleanly
     at both levels is a hard failure: a "deliberate-FAIL fixture" that does not fail proves
     nothing.
  4. Prints "checked N example file(s)" and exits 1 if N == 0 or any mismatch occurred, so a
     directory-layout drift (the exact bug this script replaces) cannot silently report 0 and
     pass green again.

No network call. stdlib + `jsonschema` (optional at import time in the kernel; this script
requires it to be installed, same as CI's `pip install jsonschema` step).
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schema"
EXAMPLES_DIR = SCHEMA_DIR / "examples"
FAIL_DIR = EXAMPLES_DIR / "fail"

sys.path.insert(0, str(REPO_ROOT))

import json  # noqa: E402

from kernel import glosa_kernel as k  # noqa: E402


def _load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if not k._HAVE_JSONSCHEMA:  # pragma: no cover - CI always installs jsonschema first
        print("jsonschema is not importable -- install it (`pip install jsonschema`) before "
              "running this check; the kernel's fallback presence-only check is not a substitute "
              "for real schema validation in CI.")
        return 1

    if not EXAMPLES_DIR.is_dir():
        print(f"FAIL: expected directory not found: {EXAMPLES_DIR}")
        return 1

    checked = 0
    failures: list[str] = []

    # -- 1. every schema/examples/*.example.json must PASS its own schema (+ kernel rules for
    #    claim_card, since that name has a dedicated validate_* function that layers kernel-only
    #    rules 5/6/8/4-9-date-arithmetic on top of the schema).
    example_files = sorted(EXAMPLES_DIR.glob("*.example.json"))
    for ex_path in example_files:
        name = ex_path.name[: -len(".example.json")]
        schema_path = SCHEMA_DIR / f"{name}.schema.json"
        if not schema_path.is_file():
            failures.append(f"{ex_path}: no matching schema {schema_path.name}")
            continue
        checked += 1
        instance = _load(ex_path)
        if name == "claim_card":
            result = k.validate_claim_card(instance)
            if not result["ok"]:
                failures.append(
                    f"{ex_path} should PASS validate_claim_card but did not: {result['errors']}"
                )
            else:
                print(f"  [OK]   {ex_path} passes validate_claim_card (schema + kernel rules)")
        else:
            errors, used_fallback = k._schema_validate(instance, schema_path.name)
            if used_fallback:
                failures.append(
                    f"{ex_path}: jsonschema RefResolver unavailable -- fell back to the coarse "
                    "presence-only check, which is not a real schema-validate pass"
                )
            elif errors:
                failures.append(f"{ex_path} should PASS {schema_path.name} but failed: {errors}")
            else:
                print(f"  [OK]   {ex_path} validates against {schema_path.name}")

    # -- 2. every schema/examples/fail/*.json must FAIL -- at schema level or kernel level.
    #    schema/README.md documents all current fail fixtures as claim_card-shaped, so route
    #    through validate_claim_card (schema allOf + kernel rules together); if a future fixture
    #    is not claim_card-shaped (no "shape" key), fall back to raw claim_card schema
    #    validation only as a last resort and say so.
    if not FAIL_DIR.is_dir():
        failures.append(f"no fail fixtures directory: {FAIL_DIR}")
    else:
        fail_files = sorted(FAIL_DIR.glob("*.json"))
        for fail_path in fail_files:
            checked += 1
            instance = _load(fail_path)
            reason = instance.get("_fail_reason", "(no _fail_reason field)")
            if "shape" in instance:
                result = k.validate_claim_card(instance)
                rejected = not result["ok"]
                errors = result["errors"]
            elif "identifier" in instance and "claim_ref" in instance:
                # citation_card-shaped fixture (K-C1/rule26) -- corrected 2026-09-05: previously
                # every non-"shape" fixture fell through to claim_card schema validation
                # regardless of its actual object type, which happened to still reject it, but
                # for the wrong reason (missing claim_card-required fields), not the rule the
                # fixture actually names.
                result = k.validate_citation_card(instance)
                rejected = not result["ok"]
                errors = result["errors"]
            else:
                errors, _used_fallback = k._schema_validate(instance, "claim_card.schema.json")
                rejected = bool(errors)
            if rejected:
                print(f"  [OK]   {fail_path} correctly rejected ({reason})")
            else:
                failures.append(
                    f"{fail_path} should FAIL (per its own _fail_reason: {reason}) but "
                    "validated cleanly at both schema and kernel level"
                )

    print(f"checked {checked} example file(s)")
    if checked == 0:
        print("FAIL: checked 0 example file(s) -- this is the exact silent-pass bug MUST-5 "
              "fixes; a directory-layout mismatch must be reported as a failure, not a green 0.")
        return 1

    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"  [FAIL] {f}")
        return 1

    print(f"PASS: {len(example_files)} valid example(s), "
          f"{len(list(FAIL_DIR.glob('*.json'))) if FAIL_DIR.is_dir() else 0} fail fixture(s), "
          "all correct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
