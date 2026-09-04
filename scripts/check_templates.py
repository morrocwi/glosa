#!/usr/bin/env python3
"""scripts/check_templates.py — template-vs-schema drift checker (glosa MUST-3).

tier: finite_diagnostic (this script's own exit code is the readout; run it and read stdout,
do not take this docstring's word for it).

Readout, not truth: this script reports what Draft7Validator observed against a fixed set of
files. It is not a substitute for a human filling in a template correctly; it only catches the
class of drift ARCH_structure.md F7 and ARCH_usability.md F1 found by hand once already
(`templates/knowledge/citation_card.yaml` missing the schema-required `independence_class`
field; `templates/knowledge/blackbox_note.yaml` not parsing as YAML at all) — so it does not
silently regress again.

What it does, for every `templates/knowledge/*.yaml` file that has a sibling
`schema/<name>.schema.json` (mapped by filename stem):
  1. Parse the template as YAML (fails loudly, not silently, if it does not parse — this alone
     would have caught MUST-2 before it shipped).
  2. Unwrap the one template that nests its content one key deeper than its schema
     (`blackbox_note.yaml`'s `blackbox_note:` top key — see WRAPPER_KEYS below; every other
     template in this directory is flat).
  3. Walk the parsed content in lockstep with the JSON Schema, replacing values that read as an
     unfilled human placeholder (`<...>` brackets, a `TODO` prefix, a `this | or | that`-style
     menu of options, or an id that does not match its own field's `pattern`) with a minimal
     type-appropriate dummy — never inventing or dropping a key, only rewriting a leaf value
     already present. This means a template's REAL problems (a missing required key, a stale
     enum value, a genuinely wrong field name) still reach the validator and get reported; only
     the "please fill this in" placeholder text is normalized away first.
  4. Validate the result with `jsonschema.Draft7Validator`, resolved against every
     `schema/*.schema.json` + `schema/common.defs.json` the same way `kernel/glosa_kernel.py`'s
     own `_validator_for` does (RefResolver + a `{$id: schema}` store), since a bare
     `jsonschema.validate()` cannot follow this repo's cross-file `$ref`s.
  5. Print one PASS/FAIL/SKIP line per file, plus every validation error found, and exit 1 if
     any file failed.

A file with no sibling schema (every `templates/knowledge/*.md` protocol card, and any future
`.yaml` template that has not been schema-ratified yet) is reported SKIP, not FAIL — a missing
schema is not itself a defect this script is positioned to judge.

Not wired into `scripts/check_repo.sh` by this fix (that file was out of this fixer's assigned
scope — see design/ARCH_MUST_2_3_8_NOTES.md if present, or the handoff that assigned this task).
Run directly: `python3 scripts/check_templates.py`.

stdlib-only except `PyYAML` (`yaml`, already a repo dependency — every other `templates/knowledge/
*.yaml` file in this repo is only ever read via PyYAML) and `jsonschema` (already a repo
dependency — see `kernel/glosa_kernel.py`'s own optional-import pattern, mirrored here without
the fallback-when-absent branch since this is a maintainer-run dev-time check, not shipped
runtime code: if either import is missing, this script says so plainly and exits 1 rather than
guessing).
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore

    _HAVE_YAML = True
except Exception:  # pragma: no cover - exercised only in an environment without PyYAML
    yaml = None  # type: ignore
    _HAVE_YAML = False

try:
    from jsonschema import Draft7Validator, RefResolver  # type: ignore

    _HAVE_JSONSCHEMA = True
except Exception:  # pragma: no cover - exercised only in an environment without jsonschema
    Draft7Validator = None  # type: ignore
    RefResolver = None  # type: ignore
    _HAVE_JSONSCHEMA = False


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "templates" / "knowledge"
SCHEMA_DIR = REPO_ROOT / "schema"

# templates/knowledge/blackbox_note.yaml wraps every field one key deeper (under a top-level
# `blackbox_note:` key) than schema/blackbox_note.schema.json describes, so a human opening the
# raw file sees the record's name first. Every other templates/knowledge/*.yaml file is flat —
# its top-level keys ARE the schema's top-level properties. Add here, never guess, if a future
# template adopts the same wrapper convention.
WRAPPER_KEYS = {
    "blackbox_note": "blackbox_note",
}

_BRACKET_PLACEHOLDER_RE = re.compile(r"<[^<>]*>")


# --------------------------------------------------------------------------------------------
# Schema loading — mirrors kernel/glosa_kernel.py's _load_schema_store/_validator_for pattern.
# --------------------------------------------------------------------------------------------

def _load_schema_store():
    store = {}
    paths = list(SCHEMA_DIR.glob("*.schema.json")) + [SCHEMA_DIR / "common.defs.json"]
    for p in paths:
        if not p.is_file():
            continue
        schema = json.loads(p.read_text(encoding="utf-8"))
        if "$id" in schema:
            store[schema["$id"]] = schema
    return store


def _common_defs():
    return json.loads((SCHEMA_DIR / "common.defs.json").read_text(encoding="utf-8"))


def _json_pointer(doc, pointer):
    node = doc
    for part in pointer.strip("/").split("/"):
        if part == "":
            continue
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def _resolve_local_ref(node, common_defs):
    """Resolve the one $ref shape every templates/knowledge/*.yaml schema actually uses:
    'common.defs.json#/definitions/<name>' (checked by hand against all 11 relevant schema
    files as of this fix — none of them $ref a same-file fragment or a third schema file).
    Returns {} for anything else, which fill_placeholders treats as 'nothing more to resolve'."""
    ref = node.get("$ref", "")
    if ref.startswith("common.defs.json#"):
        return _json_pointer(common_defs, ref.split("#", 1)[1])
    return {}


def _is_placeholder_string(value):
    if isinstance(value, str) and value.strip() == '':
        return True
    if not isinstance(value, str):
        return False
    if _BRACKET_PLACEHOLDER_RE.search(value):
        return True
    if value.strip().upper().startswith("TODO"):
        return True
    if " | " in value:  # e.g. "th | en | mixed" — a menu of options, not a chosen value
        return True
    return False


def _dummy_for_pattern(pattern):
    """Generate a short literal matching a simple anchored regex: literal runs plus
    [class]{n}/[class]+/[class]* quantified character classes — the only pattern shapes used
    anywhere in schema/*.schema.json as of this fix (verified by hand: `grep -n '"pattern"'
    schema/*.schema.json`, every hit is `^literal-[a-z0-9-]+-[0-9]{N}$`-shaped or `^A[0-9]+$`-
    or `^D-[A-Z0-9-]+$`-shaped). Not a general regex-to-string generator."""
    s = pattern
    if s.startswith("^"):
        s = s[1:]
    if s.endswith("$"):
        s = s[:-1]
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i + 1])
            i += 2
            continue
        if c == "[":
            j = s.index("]", i)
            cls = s[i + 1 : j]
            i = j + 1
            rep = 1
            if i < len(s) and s[i] == "{":
                k = s.index("}", i)
                rep = int(s[i + 1 : k].split(",")[0])
                i = k + 1
            elif i < len(s) and s[i] == "+":
                rep = 1
                i += 1
            elif i < len(s) and s[i] == "*":
                rep = 0
                i += 1
            ch = "0" if "0-9" in cls else ("a" if "a-z" in cls else ("A" if "A-Z" in cls else (cls[0] if cls else "x")))
            out.append(ch * rep)
            continue
        out.append(c)
        i += 1
    return "".join(out)


def fill_placeholders(value, node, common_defs):
    """Walk `value` in lockstep with JSON-schema node `node`; replace only leaves that read as
    an unfilled placeholder with a minimal type-appropriate dummy. Never adds or removes a key
    — a missing required key stays missing, so Draft7Validator still reports it."""
    if not isinstance(node, dict):
        return value
    if "$ref" in node:
        node = _resolve_local_ref(node, common_defs)
        if not node:
            return value

    if "enum" in node:
        if isinstance(value, str) and value in node["enum"]:
            return value  # a real chosen value (right or wrong) — leave for the validator to judge
        if _is_placeholder_string(value) or value is None:
            return node["enum"][0]
        return value

    if "const" in node:
        return node["const"] if _is_placeholder_string(value) else value

    if "pattern" in node and isinstance(value, str):
        try:
            if re.fullmatch(node["pattern"], value):
                return value
        except re.error:
            pass
        return _dummy_for_pattern(node["pattern"])

    node_type = node.get("type")
    types = node_type if isinstance(node_type, list) else ([node_type] if node_type else [])

    if "object" in types and isinstance(value, dict):
        props = node.get("properties", {})
        return {
            k: (fill_placeholders(v, props[k], common_defs) if k in props else v)
            for k, v in value.items()
        }

    if "array" in types and isinstance(value, list):
        items_schema = node.get("items", {})
        return [fill_placeholders(v, items_schema, common_defs) for v in value]

    if "string" in types and _is_placeholder_string(value):
        return "example"

    if "boolean" in types and _is_placeholder_string(value):
        return False

    if ("integer" in types or "number" in types) and _is_placeholder_string(value):
        return 0

    return value


def check_one(path, store, common_defs):
    rel = str(path.relative_to(REPO_ROOT))
    name = path.stem
    schema_id = f"https://glosa.example/schema/{name}.schema.json"
    schema = store.get(schema_id)
    if schema is None:
        return {"file": rel, "status": "SKIP", "reason": f"no sibling schema/{name}.schema.json"}

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # yaml.YAMLError and friends
        return {"file": rel, "status": "FAIL", "errors": [f"YAML parse error: {exc}"]}

    if not isinstance(raw, dict):
        return {"file": rel, "status": "FAIL", "errors": ["top-level YAML content is not a mapping"]}

    wrapper = WRAPPER_KEYS.get(name)
    if wrapper:
        if wrapper not in raw:
            return {"file": rel, "status": "FAIL", "errors": [f"expected top-level wrapper key '{wrapper}:' not found"]}
        instance = raw[wrapper]
    else:
        instance = raw

    if not isinstance(instance, dict):
        return {"file": rel, "status": "FAIL", "errors": ["template content is not a mapping"]}

    filled = fill_placeholders(copy.deepcopy(instance), schema, common_defs)

    resolver = RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    validator = Draft7Validator(schema, resolver=resolver)
    errors = sorted(validator.iter_errors(filled), key=lambda e: str(list(e.path)))
    if errors:
        return {
            "file": rel,
            "status": "FAIL",
            "errors": [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors],
        }
    return {"file": rel, "status": "PASS"}


def main():
    if not _HAVE_YAML:
        print("[ERROR] PyYAML is not importable — cannot check templates/knowledge/*.yaml")
        return 1
    if not _HAVE_JSONSCHEMA:
        print("[ERROR] jsonschema is not importable — cannot validate templates against schema/*.schema.json")
        return 1
    if not TEMPLATES_DIR.is_dir():
        print(f"[ERROR] {TEMPLATES_DIR} not found")
        return 1

    store = _load_schema_store()
    common_defs = _common_defs()

    results = [check_one(p, store, common_defs) for p in sorted(TEMPLATES_DIR.glob("*.yaml"))]

    any_fail = False
    for r in results:
        if r["status"] == "SKIP":
            print(f"[SKIP] {r['file']} — {r['reason']}")
        elif r["status"] == "PASS":
            print(f"[PASS] {r['file']}")
        else:
            any_fail = True
            print(f"[FAIL] {r['file']}")
            for e in r["errors"]:
                print(f"        {e}")

    n_pass = sum(1 for r in results if r["status"] == "PASS")
    n_fail = sum(1 for r in results if r["status"] == "FAIL")
    n_skip = sum(1 for r in results if r["status"] == "SKIP")
    print(f"\n{n_pass} passed, {n_fail} failed, {n_skip} skipped (no sibling schema) — {len(results)} templates/knowledge/*.yaml checked")

    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
