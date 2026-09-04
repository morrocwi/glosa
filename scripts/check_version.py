#!/usr/bin/env python3
"""scripts/check_version.py — glosa version-consistency gate.

Readout, not truth: this script compares four (or fewer, if a file does not
yet exist) declared version strings and reports whether they agree. It does
not certify the release is otherwise ready.

Checked sources, when present:
  - the current git tag (must look like vX.Y.Z, annotated or lightweight,
    pointing at HEAD) — REQUIRED to run a real comparison; without a tag the
    script reports the other sources' versions and exits 0 (nothing to
    compare against yet, e.g. running on a normal commit pre-release).
  - CITATION.cff        (`version:` field)
  - .zenodo.json        (`version` field, if present — optional key upstream)
  - codemeta.json       (`version` field, if the file exists)
  - plugin.json         (`version` field, if the file exists — glob-searched
                          under plugins/*/.claude-plugin/plugin.json and
                          .claude-plugin/plugin.json, since the exact path is
                          not yet fixed in this repo)

Exit 0 = all present sources agree (or no tag yet to compare against).
Exit 1 = a mismatch was found, or a REQUIRED file is missing/unparseable
         once a tag is present.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

VERSION_RE = re.compile(r"^v?(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)$")


def repo_root() -> Path:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return Path(out.stdout.strip())
    except Exception:
        return Path(".").resolve()


def git_tag_at_head(root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "tag", "--points-at", "HEAD"],
            capture_output=True, text=True, check=True, cwd=root,
        )
        tags = [t for t in out.stdout.splitlines() if VERSION_RE.match(t)]
        return tags[0] if tags else None
    except Exception:
        return None


def read_cff_version(path: Path) -> str | None:
    if not path.is_file():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^version:\s*['\"]?([^'\"#]+)['\"]?\s*$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def read_json_version(path: Path) -> str | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"  [FAIL] {path}: could not parse JSON: {exc}")
        return "__PARSE_ERROR__"
    v = data.get("version")
    return str(v) if v is not None else None


def find_plugin_json_versions(root: Path) -> dict[str, str | None]:
    candidates = list(root.glob(".claude-plugin/plugin.json")) + list(
        root.glob("plugins/*/.claude-plugin/plugin.json")
    )
    found: dict[str, str | None] = {}
    for c in candidates:
        rel = str(c.relative_to(root))
        found[rel] = read_json_version(c)
    return found


def norm(v: str | None) -> str | None:
    if v is None or v == "__PARSE_ERROR__":
        return v
    m = VERSION_RE.match(v.strip())
    return m.group(1) if m else v.strip()


def main() -> int:
    root = repo_root()
    print("== glosa check_version.py ==")
    print(f"repo root: {root}")

    tag = git_tag_at_head(root)
    cff_v = read_cff_version(root / "CITATION.cff")
    zenodo_v = read_json_version(root / ".zenodo.json")
    codemeta_v = read_json_version(root / "codemeta.json")
    plugin_versions = find_plugin_json_versions(root)

    sources: list[tuple[str, str | None]] = [
        ("git tag (HEAD)", tag),
        ("CITATION.cff", cff_v),
        (".zenodo.json", zenodo_v),
        ("codemeta.json", codemeta_v),
    ]
    for path_str, v in plugin_versions.items():
        sources.append((path_str, v))

    print("")
    print("-- observed versions --")
    for name, v in sources:
        print(f"  {name}: {v!r}")

    present = [(n, norm(v)) for n, v in sources if v is not None]

    if tag is None:
        print("")
        print("no git tag at HEAD — nothing to release-compare against yet.")
        print("check_version.py: PASS (informational only)")
        return 0

    # A tag exists: CITATION.cff and .zenodo.json (if it declares a version
    # key) and codemeta.json/plugin.json (if they exist) must all agree with it.
    tag_norm = norm(tag)
    mismatches = []
    for name, v in present:
        if name == "git tag (HEAD)":
            continue
        if v == "__PARSE_ERROR__":
            mismatches.append((name, v))
            continue
        if v != tag_norm:
            mismatches.append((name, v))

    print("")
    if mismatches:
        print("-- MISMATCHES against git tag %r (normalized %r) --" % (tag, tag_norm))
        for name, v in mismatches:
            print(f"  [FAIL] {name} = {v!r} != {tag_norm!r}")
        print("")
        print("check_version.py: FAIL")
        return 1

    print(f"all present sources agree with git tag {tag!r}.")
    print("check_version.py: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
