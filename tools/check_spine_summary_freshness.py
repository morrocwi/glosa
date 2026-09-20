#!/usr/bin/env python3
"""Freshness checker for design/SPINE_AND_CLAIM_CARD_SUMMARY.md.

This is a mechanical readout, not a truth claim: it recomputes the current git blob hash of the
source file the summary claims to excerpt, and compares it against the hash literally stamped in
the summary's own header. It does not check whether the *excerpted text* still matches the source
section-by-section -- only whether the source *file's content as a whole* has changed since the
summary was written. A changed hash means "go re-read the source and re-freeze the summary", not
"the summary is wrong in a specific place".

Usage:
    python3 tools/check_spine_summary_freshness.py

Exit code 0 + "OK" message  -> hashes match, summary is fresh.
Exit code 1 + loud warning  -> hashes differ (or something could not be read), summary is stale.

Run from anywhere inside the repo; paths are resolved relative to this script's own location.
"""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_FILE = REPO_ROOT / "design" / "FOUNDATION_v0.6.md"
SUMMARY_FILE = REPO_ROOT / "design" / "SPINE_AND_CLAIM_CARD_SUMMARY.md"

# Matches the exact line this summary's header uses to stamp the blob hash, e.g.:
#   - **Blob hash (`git hash-object design/FOUNDATION_v0.6.md`):** `0abaafa9c62742...`
STAMPED_HASH_RE = re.compile(
    r"\*\*Blob hash \(`git hash-object [^`]+`\):\*\*\s*`([0-9a-f]{40})`"
)


def fail(message: str) -> None:
    print("=" * 72)
    print("FRESHNESS CHECK FAILED -- design/SPINE_AND_CLAIM_CARD_SUMMARY.md is STALE")
    print("=" * 72)
    print(message)
    print()
    print("This means design/FOUNDATION_v0.6.md has changed since the summary was")
    print("written (or the summary/checker itself is misconfigured). Re-read the")
    print("current source file's spine (§2) and claim-card (§3) sections and")
    print("re-freeze design/SPINE_AND_CLAIM_CARD_SUMMARY.md, updating its stamped hash.")
    sys.exit(1)


def main() -> None:
    if not SOURCE_FILE.is_file():
        fail(f"Source file not found: {SOURCE_FILE}")

    if not SUMMARY_FILE.is_file():
        fail(f"Summary file not found: {SUMMARY_FILE}")

    try:
        result = subprocess.run(
            ["git", "hash-object", str(SOURCE_FILE)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        fail(f"Could not run 'git hash-object' on the source file: {exc}")
        return  # unreachable, fail() exits

    current_hash = result.stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", current_hash):
        fail(f"'git hash-object' returned something that is not a 40-hex-char hash: {current_hash!r}")

    summary_text = SUMMARY_FILE.read_text(encoding="utf-8")
    match = STAMPED_HASH_RE.search(summary_text)
    if not match:
        fail(
            "Could not find a stamped 'Blob hash (`git hash-object ...`): `<hash>`' line "
            f"inside {SUMMARY_FILE}. The summary's header format may have changed."
        )
        return  # unreachable

    stamped_hash = match.group(1)

    if stamped_hash != current_hash:
        fail(
            "Hash mismatch.\n"
            f"  stamped in summary : {stamped_hash}\n"
            f"  current source hash: {current_hash}\n"
            f"  source file         : {SOURCE_FILE}"
        )
        return  # unreachable

    print("OK -- design/SPINE_AND_CLAIM_CARD_SUMMARY.md is fresh.")
    print(f"  source file : {SOURCE_FILE.relative_to(REPO_ROOT)}")
    print(f"  blob hash   : {current_hash}")
    sys.exit(0)


if __name__ == "__main__":
    main()
