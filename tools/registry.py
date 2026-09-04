#!/usr/bin/env python3
"""
registry.py — glosa research registry CLI (stdlib + pyyaml if available, else JSON fallback).

Tier: Dr (tooling). readout-not-truth: this tool reports what is written in the registry file, not
whether the underlying work is correct — see registry/README.md "what the registry is NOT".

Subcommands:
  new --title-th --title-en          allocate the next GLS-YYYY-NNN id, write a new entry
  list                                print all entries (id | title_en | stage | k_state | updated)
  status <id>                         print one entry in full
  advance <id> <stage> --by human|ai|joint [--stub] [--litreview-manifest-ref REF]
                                       append a history row; the state machine is strict-forward,
                                       one step at a time (no skipping stages); `lrs` and every
                                       stage after it require a litreview_manifest_ref, --stub is
                                       only a valid escape through genre_routed (method and later
                                       need a real ref), and `released` additionally requires
                                       doi_version plus an APPROVED registry/RELEASE_APPROVAL.txt
  check                                audit every entry against the state-machine invariants
                                       above (transition legality, litreview gating, stub ceiling,
                                       release requirements); exit 1 and list violations if any
  render                              write ~/ANSE.ASIA/glosa/RESEARCH_LIBRARY.md
"""
import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_YAML = REPO_ROOT / "registry" / "RESEARCH_REGISTRY.yaml"
REGISTRY_JSON = REPO_ROOT / "registry" / "RESEARCH_REGISTRY.json"
LIBRARY_MD = REPO_ROOT / "RESEARCH_LIBRARY.md"

SPINE_STAGES = [
    "problem", "blackbox", "lens_in", "analysis", "lens_out", "lrs",
    "hypothesis_selected", "genre_routed", "method", "paper_draft", "review", "released",
]
STAGE_INDEX = {s: i for i, s in enumerate(SPINE_STAGES)}

# The state machine is strict-forward, one legal step at a time (MUST-10): from a given stage
# there is exactly one allowed next stage, and cmd_advance/cmd_check refuse anything else,
# including skips. This dict is the single source of truth for that invariant.
ALLOWED_TRANSITIONS = {
    SPINE_STAGES[i]: SPINE_STAGES[i + 1] for i in range(len(SPINE_STAGES) - 1)
}

# litreview_manifest_ref is required starting at "lrs" (the literature-review-synthesis stage
# itself) and for every stage after it -- not merely from paper_draft onward. A project cannot
# legitimately claim to have selected a hypothesis, routed a genre, built a method, or drafted a
# paper without having done (or explicitly stubbed) the literature-review step first.
STAGES_REQUIRING_LITREVIEW = set(SPINE_STAGES[STAGE_INDEX["lrs"]:])

# --stub is an explicit, logged admission that a prerequisite is not really met. It is only a
# valid escape hatch through "genre_routed". Beyond that (method, paper_draft, review, released)
# a real litreview_manifest_ref is mandatory -- no stubbing a paper or a release into existence.
STUB_CEILING = "genre_routed"

RELEASE_APPROVAL_TXT = REPO_ROOT / "registry" / "RELEASE_APPROVAL.txt"

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False


def today() -> str:
    return _dt.date.today().isoformat()


def registry_path() -> Path:
    if REGISTRY_YAML.exists():
        return REGISTRY_YAML
    if REGISTRY_JSON.exists():
        return REGISTRY_JSON
    return REGISTRY_YAML if HAVE_YAML else REGISTRY_JSON


def load_registry() -> dict:
    path = registry_path()
    if not path.exists():
        return {"entries": []}
    text = path.read_text()
    if path.suffix == ".yaml":
        if HAVE_YAML:
            return yaml.safe_load(text) or {"entries": []}
        # no yaml lib but file is yaml — refuse rather than mis-parse
        print(f"registry.py: PyYAML not installed and {path} is YAML — install pyyaml or "
              f"convert to RESEARCH_REGISTRY.json", file=sys.stderr)
        sys.exit(2)
    return json.loads(text) if text.strip() else {"entries": []}


def save_registry(data: dict) -> None:
    path = registry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".yaml" and HAVE_YAML:
        header = (
            "# glosa research registry — readout, not a truth ledger.\n"
            "# id scheme: GLS-YYYY-NNN (one problem = one project = one id, see README.md)\n"
        )
        path.write_text(header + yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    else:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n")


def next_id(entries: list) -> str:
    year = _dt.date.today().year
    pattern = re.compile(rf"^GLS-{year}-(\d{{3}})$")
    max_n = 0
    for e in entries:
        m = pattern.match(e.get("id", ""))
        if m:
            max_n = max(max_n, int(m.group(1)))
    return f"GLS-{year}-{max_n + 1:03d}"


def find_entry(entries: list, entry_id: str):
    for e in entries:
        if e.get("id") == entry_id:
            return e
    return None


# ---------------------------------------------------------------------------

def cmd_new(args):
    data = load_registry()
    entries = data.setdefault("entries", [])
    new_id = next_id(entries)
    entry = {
        "id": new_id,
        "title_th": args.title_th,
        "title_en": args.title_en,
        "problem_ref": None,
        "blackbox_ref": None,
        "hypothesis_refs": [],
        "spine_stage": "problem",
        "k_state": "K0",
        "genre": None,
        "venue_track": None,
        "claim_card_count": 0,
        "litreview_manifest_ref": None,
        "doi_concept": None,
        "doi_version": None,
        "deposition_id": None,
        "repo_path": None,
        "owner_role": "human",
        "created": today(),
        "updated": today(),
        "history": [{"date": today(), "stage": "problem", "by": "joint"}],
    }
    entries.append(entry)
    save_registry(data)
    print(f"created {new_id}")


def cmd_list(args):
    data = load_registry()
    entries = data.get("entries", [])
    for e in entries:
        print(f"{e['id']}\t{e.get('title_en', '')[:60]}\t{e.get('spine_stage')}\t"
              f"{e.get('k_state')}\t{e.get('updated')}")
    if not entries:
        print("(no entries)")


def cmd_status(args):
    data = load_registry()
    entry = find_entry(data.get("entries", []), args.id)
    if not entry:
        print(f"registry.py: no such id {args.id}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(entry, indent=2, ensure_ascii=False))


def cmd_advance(args):
    if args.stage not in SPINE_STAGES:
        print(f"registry.py: unknown stage {args.stage!r} (must be one of {SPINE_STAGES})", file=sys.stderr)
        sys.exit(1)
    data = load_registry()
    entry = find_entry(data.get("entries", []), args.id)
    if not entry:
        print(f"registry.py: no such id {args.id}", file=sys.stderr)
        sys.exit(1)

    current = entry.get("spine_stage")
    if current not in STAGE_INDEX:
        print(
            f"registry.py: {args.id} has unknown current spine_stage {current!r} — cannot compute "
            f"a legal next transition",
            file=sys.stderr,
        )
        sys.exit(1)

    expected_next = ALLOWED_TRANSITIONS.get(current)
    if expected_next is None:
        print(f"registry.py: {args.id} is already at the terminal stage {current!r}", file=sys.stderr)
        sys.exit(1)
    if args.stage != expected_next:
        print(
            f"registry.py: refusing to advance {args.id} from {current!r} to {args.stage!r} — the "
            f"state machine only allows one step at a time; the next legal stage from {current!r} "
            f"is {expected_next!r}. Skipping stages is not allowed.",
            file=sys.stderr,
        )
        sys.exit(1)

    used_stub = False
    if args.stage in STAGES_REQUIRING_LITREVIEW:
        has_ref = bool(entry.get("litreview_manifest_ref")) or bool(args.litreview_manifest_ref)
        if not has_ref:
            if not args.stub:
                print(
                    f"registry.py: refusing to advance {args.id} to {args.stage!r} without a "
                    f"litreview_manifest_ref (pass --litreview-manifest-ref, or --stub to override "
                    f"explicitly — this will be logged as a stub advance, and only works through "
                    f"{STUB_CEILING!r})",
                    file=sys.stderr,
                )
                sys.exit(1)
            if STAGE_INDEX[args.stage] > STAGE_INDEX[STUB_CEILING]:
                print(
                    f"registry.py: refusing --stub for {args.stage!r} — --stub is only a valid "
                    f"escape through {STUB_CEILING!r}; {args.stage!r} requires a real "
                    f"litreview_manifest_ref, no stubbing.",
                    file=sys.stderr,
                )
                sys.exit(1)
            used_stub = True

    if args.stage == "released":
        if not entry.get("doi_version"):
            print(
                f"registry.py: refusing to advance {args.id} to 'released' — entry has no "
                f"doi_version set",
                file=sys.stderr,
            )
            sys.exit(1)
        approval_text = RELEASE_APPROVAL_TXT.read_text() if RELEASE_APPROVAL_TXT.exists() else ""
        if "APPROVED" not in approval_text:
            print(
                "registry.py: refusing to advance to 'released' — registry/RELEASE_APPROVAL.txt "
                "must exist and contain APPROVED (founder sign-off; see "
                "RELEASE_APPROVAL.txt.EXAMPLE)",
                file=sys.stderr,
            )
            sys.exit(1)

    if args.litreview_manifest_ref:
        entry["litreview_manifest_ref"] = args.litreview_manifest_ref

    entry["spine_stage"] = args.stage
    entry["updated"] = today()
    hist_entry = {"date": today(), "stage": args.stage, "by": args.by}
    if used_stub:
        hist_entry["stub"] = True
    entry.setdefault("history", []).append(hist_entry)
    save_registry(data)
    print(f"{args.id} advanced to {args.stage} (by={args.by}{', STUB' if used_stub else ''})")


def cmd_check(args):
    """Audit every entry against the state-machine invariants cmd_advance enforces going forward.

    Exists because RESEARCH_REGISTRY.yaml can be hand-edited directly (a human/AI editing the
    file with a text editor bypasses cmd_advance entirely) — this is the mechanical check that
    notices when that happened. Tier: finite_diagnostic (reports exactly what it found).
    """
    data = load_registry()
    entries = data.get("entries", [])
    violations = []
    approval_text = RELEASE_APPROVAL_TXT.read_text() if RELEASE_APPROVAL_TXT.exists() else ""

    for e in entries:
        eid = e.get("id", "?")
        stage = e.get("spine_stage")
        if stage not in STAGE_INDEX:
            violations.append(f"{eid}: unknown spine_stage {stage!r}")
            continue

        history = e.get("history", [])
        if not history:
            violations.append(f"{eid}: no history rows at all")
        else:
            if history[0].get("stage") != "problem":
                violations.append(
                    f"{eid}: history does not start at 'problem' (starts at "
                    f"{history[0].get('stage')!r})"
                )
            for i in range(1, len(history)):
                prev_stage, cur_stage = history[i - 1].get("stage"), history[i].get("stage")
                if ALLOWED_TRANSITIONS.get(prev_stage) != cur_stage:
                    violations.append(
                        f"{eid}: history row {i} jumps from {prev_stage!r} to {cur_stage!r} — "
                        f"not a legal one-step transition"
                    )
            if history[-1].get("stage") != stage:
                violations.append(
                    f"{eid}: current spine_stage {stage!r} does not match last history row "
                    f"{history[-1].get('stage')!r}"
                )

        if stage in STAGES_REQUIRING_LITREVIEW:
            has_ref = bool(e.get("litreview_manifest_ref"))
            stubbed = any(h.get("stage") == stage and h.get("stub") for h in history)
            if not has_ref and not stubbed:
                violations.append(
                    f"{eid}: at gated stage {stage!r} with no litreview_manifest_ref and no "
                    f"stub:true history row for it"
                )
            if stubbed and STAGE_INDEX[stage] > STAGE_INDEX[STUB_CEILING]:
                violations.append(
                    f"{eid}: stage {stage!r} is marked stub:true but is past the stub ceiling "
                    f"{STUB_CEILING!r} — a real litreview_manifest_ref is required here"
                )

        if stage == "released":
            if not e.get("doi_version"):
                violations.append(f"{eid}: released with no doi_version set")
            if "APPROVED" not in approval_text:
                violations.append(
                    f"{eid}: released with no APPROVED registry/RELEASE_APPROVAL.txt"
                )

    if violations:
        print(f"registry.py check: {len(violations)} violation(s):")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    plural = "y" if len(entries) == 1 else "ies"
    print(f"registry.py check: {len(entries)} entr{plural} OK, 0 violations")


def cmd_render(args):
    data = load_registry()
    entries = data.get("entries", [])
    lines = [
        "# glosa Research Library",
        "",
        f"> Rendered by `tools/registry.py render` on {today()}. This table is a readout of "
        f"`registry/RESEARCH_REGISTRY.yaml`, not a truth ledger — see `registry/README.md`.",
        "",
        f"**{len(entries)} work(s) registered.**",
        "",
        "| id | title | stage | K | DOI | updated |",
        "|---|---|---|---|---|---|",
    ]
    for e in entries:
        doi = e.get("doi_version") or e.get("doi_concept") or "—"
        lines.append(
            f"| {e['id']} | {e.get('title_en', '')} | {e.get('spine_stage')} | "
            f"{e.get('k_state')} | {doi} | {e.get('updated')} |"
        )
    LIBRARY_MD.write_text("\n".join(lines) + "\n")
    print(f"wrote {LIBRARY_MD}")
    print("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="glosa research registry")
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new")
    p_new.add_argument("--title-th", required=True)
    p_new.add_argument("--title-en", required=True)

    sub.add_parser("list")

    p_status = sub.add_parser("status")
    p_status.add_argument("id")

    p_advance = sub.add_parser("advance")
    p_advance.add_argument("id")
    p_advance.add_argument("stage")
    p_advance.add_argument("--by", choices=["human", "ai", "joint"], required=True)
    p_advance.add_argument("--stub", action="store_true")
    p_advance.add_argument("--litreview-manifest-ref", default=None)

    sub.add_parser("check")

    sub.add_parser("render")

    args = parser.parse_args()
    dispatch = {
        "new": cmd_new,
        "list": cmd_list,
        "status": cmd_status,
        "advance": cmd_advance,
        "check": cmd_check,
        "render": cmd_render,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
