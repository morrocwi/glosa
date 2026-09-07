#!/usr/bin/env python3
"""cases/repro/run_EQ-068_higgs_pdg.py -- runner for the EQ-068_higgs_pdg reproduction card.

tier: Dr (this runner is specified from design/RESISTANCE_LADDER_v0_1.md Section 6, Card 1,
and the pinned source below; independently unreviewed).

Standard library only (no numpy/mpmath needed for this card -- see cases/repro/
EQ-068_higgs_pdg.json's environment.packages, which is correctly empty). `AI = 0` at runtime:
this file performs one deterministic computation and prints its JSON result; it calls no model.

WHAT THIS REPRODUCES. Toledo code EQ-068 (registry/genesis_root.json in the Toledo repo) quotes,
verbatim: "(a) fit Lambda_RD->GeV = 246/v_native = 88.96060634765863; independent Higgs-mass
prediction 218.005 GeV vs real PDG 125.20 GeV -- 74.13% error, fails a 5% band." The source code
that produced that number was committed to the readout_genesis repo at commit
294bfbff9a7aeead9d831a761f4eb38fb9b648f0 (path domains/standard_model/item1_exploration/
rd_to_gev_fit_calibrated_bridge/rd_to_gev_fit_calibrated_bridge_v0_1.py) and depends on two
sibling modules (native_vacuum_amplitude_v0_1.py, order_vacuum_threshold_closure_v0_1.py) that
are present, UNCHANGED, in that repo's current HEAD (082dde893b70c7500c13d463239909c99cf17f0a) --
verified directly: `git -C <readout_genesis> log --oneline -- <those two files>` shows no commit
after 294bfbff9a. The pinned commit is itself on branch
candidate/rd-to-gev-fit-calibrated-bridge-2026-07-25, NOT an ancestor of HEAD -- an honest,
disclosed finding of this reproduction run, not silently patched over: EQ-068's own Genesis text
already labels this a "DRAFT/UNMERGED" candidate, and this runner reproduces it exactly as such,
never presenting it as a merged/mainline result. The
rd_to_gev_fit_calibrated_bridge_v0_1.py file itself is NOT present in the readout_genesis working
tree at HEAD (a `git cat-file -e HEAD:<path>` check returns "does not exist") -- the draft/unmerged
candidate's source survives in git history at the pinned commit above (plus a compiled
__pycache__/*.pyc in the working tree, not used by this runner). This
runner therefore extracts the exact byte content of that commit via `git show <commit>:<path>`,
hashes it (the declared input_hash), places it at the identical relative path depth the file's
own `Path(__file__).resolve().parents[4]` ROOT computation requires (so its imports of the two
sibling modules resolve correctly against the CURRENT, live sibling files -- exactly as the
original author ran it on 2026-07-25), executes it fresh in a subprocess, hashes stdout (the
declared output_hash), and REMOVES the temporary file it placed, leaving the readout_genesis
working tree exactly as it found it (a pre/post `git status --porcelain` diff is printed and
this script exits non-zero if the removal left any residue).

Usage:
    python3 cases/repro/run_EQ-068_higgs_pdg.py [--genesis-repo PATH] [--python PATH]

Default --genesis-repo is "../readout_genesis" resolved relative to this glosa checkout's own
repo root (sibling-checkout convention already used elsewhere in this workspace, e.g. Toledo's
scripts/v15_tunnel.py citing "../readout_genesis/formal") -- no absolute filesystem path, no
username, is ever written into this file (glosa's own publish-safety gate,
scripts/leak_denylist.txt's "/home/... " patterns).

Exit codes: 0 = ran and printed the JSON report (regardless of PASS/FAIL against the
pre-registered tolerance -- that comparison is repro_check.py's/the card's job, not this
runner's). 2 = could not locate/verify the pinned commit or the sibling modules, or the working
tree was not clean before/after (fail-closed: never silently proceed on a dirty or
unreconstructable tree).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PINNED_COMMIT = "294bfbff9a7aeead9d831a761f4eb38fb9b648f0"
REL_PATH = (
    "domains/standard_model/item1_exploration/rd_to_gev_fit_calibrated_bridge/"
    "rd_to_gev_fit_calibrated_bridge_v0_1.py"
)
# The two sibling modules this file imports, and the HEAD commit at which they were last read
# by this runner's own author (recorded for the reproduction card's own environment note --
# this runner re-derives their content fresh from whatever HEAD actually is, it never trusts
# this recorded value as ground truth; see the printed report's own genesis_repo_head field).
SIBLINGS_LAST_VERIFIED_UNCHANGED_SINCE = "082dde893b70c7500c13d463239909c99cf17f0a"

THIS_REPO_ROOT = Path(__file__).resolve().parents[2]  # cases/repro/ -> glosa repo root


class RunnerError(RuntimeError):
    pass


def _run(cmd, cwd=None, check=True):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise RunnerError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nstderr: {proc.stderr}")
    return proc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--genesis-repo",
        default=str((THIS_REPO_ROOT / ".." / "readout_genesis").resolve()),
        help="path to a readout_genesis checkout (default: ../readout_genesis, sibling of this repo)",
    )
    parser.add_argument("--python", default=sys.executable, help="python interpreter to run the pinned file with")
    args = parser.parse_args(argv)

    genesis_repo = Path(args.genesis_repo)
    if not (genesis_repo / ".git").exists():
        print(f"RunnerError: {genesis_repo} is not a git repository (no .git)", file=sys.stderr)
        return 2

    pre_status = _run(["git", "status", "--porcelain"], cwd=str(genesis_repo)).stdout
    target = genesis_repo / REL_PATH
    if target.exists():
        print(f"RunnerError: {target} already exists in the working tree -- refusing to overwrite it", file=sys.stderr)
        return 2

    head = _run(["git", "rev-parse", "HEAD"], cwd=str(genesis_repo)).stdout.strip()
    commit_exists = subprocess.run(
        ["git", "cat-file", "-e", f"{PINNED_COMMIT}^{{commit}}"], cwd=str(genesis_repo)
    ).returncode == 0
    if not commit_exists:
        print(f"RunnerError: pinned commit {PINNED_COMMIT} does not exist as a commit object in {genesis_repo}", file=sys.stderr)
        return 2
    # Honest disclosure, not silently assumed: this commit is a DRAFT/UNMERGED candidate (matching
    # EQ-068's own Genesis text) -- it need not be, and as of this runner's own drafting is NOT, an
    # ancestor of the checked-out HEAD used below for the two live sibling modules. Both facts are
    # recorded verbatim in the printed report so a reader never mistakes this for a merged/mainline
    # computation.
    is_ancestor_of_head = subprocess.run(
        ["git", "merge-base", "--is-ancestor", PINNED_COMMIT, "HEAD"], cwd=str(genesis_repo)
    ).returncode == 0
    branches_containing = _run(
        ["git", "branch", "--all", "--contains", PINNED_COMMIT], cwd=str(genesis_repo), check=False
    ).stdout.strip()

    source_bytes = _run(["git", "show", f"{PINNED_COMMIT}:{REL_PATH}"], cwd=str(genesis_repo)).stdout.encode("utf-8")
    input_hash = sha256_bytes(source_bytes)

    target.parent.mkdir(parents=True, exist_ok=True)
    wrote_new_file = not target.exists()
    target.write_bytes(source_bytes)
    try:
        proc = _run([args.python, str(target)], cwd=str(genesis_repo), check=False)
        if proc.returncode != 0:
            print("RunnerError: the pinned computation exited non-zero", file=sys.stderr)
            print(proc.stderr, file=sys.stderr)
            return 2
        stdout_text = proc.stdout
    finally:
        if wrote_new_file and target.exists():
            target.unlink()

    post_status = _run(["git", "status", "--porcelain"], cwd=str(genesis_repo)).stdout
    if pre_status != post_status:
        print("RunnerError: readout_genesis working tree was not restored to its pre-run state", file=sys.stderr)
        print("pre:\n" + pre_status, file=sys.stderr)
        print("post:\n" + post_status, file=sys.stderr)
        return 2

    output_hash = sha256_bytes(stdout_text.encode("utf-8"))
    report = {
        "runner": "cases/repro/run_EQ-068_higgs_pdg.py",
        "pinned_commit": PINNED_COMMIT,
        "pinned_commit_is_ancestor_of_head": is_ancestor_of_head,
        "pinned_commit_found_on_branches": branches_containing.splitlines(),
        "rel_path": REL_PATH,
        "genesis_repo_head": head,
        "genesis_repo_head_note": "the two sibling modules this pinned file imports are read live from THIS checked-out HEAD, not from the pinned commit (they are unmodified since before the pinned commit -- see this file's own module docstring)",
        "input_sha256": input_hash,
        "output_sha256": output_hash,
        "computation_stdout": json.loads(stdout_text),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
