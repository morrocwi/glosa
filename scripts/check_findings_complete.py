#!/usr/bin/env python3
"""glosa — no finding is ever dropped (gate rule 10, founder BBL-2026-09-05-121).
Checks that every id in an upstream ledger appears in each downstream record (carried forward or
explicitly closed). Usage: check_findings_complete.py <upstream.json> <downstream file> [...]
Upstream: JSON list of objects with an "id" field (or dict of ids). Downstream: any text file; an id
counts as present if the exact id string occurs in it. Exit 1 on any missing id. tier finite_diagnostic."""
import json, sys, re
from pathlib import Path
def ids_of(p):
    d = json.loads(Path(p).read_text(encoding="utf-8"))
    if isinstance(d, dict): d = list(d.values()) if all(isinstance(v, dict) for v in d.values()) else d.get("proposals") or d.get("findings") or []
    return [x.get("id") for x in d if isinstance(x, dict) and x.get("id")]
def main():
    if len(sys.argv) < 3: print(__doc__); sys.exit(2)
    ids = ids_of(sys.argv[1]); fail = 0
    for down in sys.argv[2:]:
        text = Path(down).read_text(encoding="utf-8", errors="replace")
        missing = [i for i in ids if i not in text]
        print(f"{down}: {len(ids)-len(missing)}/{len(ids)} ids present" + (f" — MISSING: {', '.join(missing)}" if missing else ""))
        fail |= bool(missing)
    print("check_findings_complete:", "FAIL" if fail else "PASS"); sys.exit(1 if fail else 0)
if __name__ == "__main__": main()
