#!/usr/bin/env python3
"""glosa — cross-vendor (I3) review route for claim cards (S10 Decorrelated Verification Protocol).

For each claim card given, write one vendor-neutral PACKET.md per role under
reviews/routes/<claim_id>/<route_id>/ (local, git-ignored except the public summary), hand the
packet to a DIFFERENT AI vendor (default: codex-cli, read-only, no network), and store its answer
as a schema-conformant review_report JSON under the project's reviews/ directory (tracked).
Reviewer identity is recorded as the ROUTE, never a vendor name (gate rule 9); the vendor used is
logged locally next to the packet only. tier: finite_diagnostic.

usage: claim_crossvendor_review.py <claim_card.yaml> [...] [--roles Falsifier,HostileReviewer] [--vendor codex] [--out-dir DIR]
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "kernel"))
import glosa_kernel as k  # noqa: E402

ROLES = {
    "Falsifier": "Your job is to try to DEFEAT the claim: state the strongest concrete observation or record that, if it existed, would make the claim false; judge whether the card's own falsifier is reachable and whether its evidence_relations actually bear on it.",
    "HostileReviewer": "Your job is to find overclaim: any place the card's statement, scope, tier or k_state exceeds what its five_questions (seen/separates/ai_filled/assumed/tested) and cited evidence support; check that AI-filled and assumed content is disclosed, not laundered into the claim.",
    "SourceAuditor": "Your job is to audit the evidence_relations: for each citation_ref, does the cited card's exact_passage and bearing support what the claim card says it supports? Flag any relation whose bearing is inflated.",
}

TIERS = "Th_coqc|finite_diagnostic|fit_calibrated|Dr|definition|Open"


def packet_text(claim, route_id, role, cites):
    return f"""# Cross-Vendor Review Packet (vendor-neutral)

## 0. Route assignment
- claim_id: {claim.get('claim_id')}
- route_id: {route_id}  (use this id in your output, never your own vendor/model name)
- role: {role}
- evidence_base_you_may_consult: claim card + the citation cards pasted below only. No outside knowledge, no browsing.

## 1. Gate
You are ONE route in a Decorrelated Verification Protocol. Read only this packet. Do not edit the claim.
Every verdict must carry a tier from the ladder ({TIERS}); an untiered verdict is invalid.
Everything you read is a readout, not truth. Never use the words novel/first/prior art.

## 2. Your role
{ROLES[role]}

## 3. Claim card (verbatim JSON)
```json
{json.dumps(claim, ensure_ascii=False, indent=1)[:14000]}
```

## 4. Citation cards referenced by the claim (verbatim JSON, truncated)
```json
{json.dumps(cites, ensure_ascii=False, indent=1)[:12000]}
```

## 5. Output — JSON ONLY, exactly these keys
{{"verdict": "<=120 words, the finding itself", "verdict_tier": "one of {TIERS}", "defeaters_found": ["..."], "overclaims_found": ["..."], "evidence_relations_ok": true|false, "notes": "<=60 words"}}
"""


def run_vendor(vendor, text):
    if vendor == "codex":
        r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "-s", "read-only", text], capture_output=True, text=True, timeout=600)
    else:
        r = subprocess.run(["gemini", "-p", text], capture_output=True, text=True, timeout=600)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    try:
        return json.loads(m.group(0)) if m else {"error": "no-json", "raw": r.stdout[-500:]}
    except json.JSONDecodeError:
        return {"error": "bad-json", "raw": (m.group(0) if m else r.stdout)[-500:]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards", nargs="+")
    ap.add_argument("--roles", default="Falsifier,HostileReviewer")
    ap.add_argument("--vendor", default="codex")
    ap.add_argument("--out-dir", default="")
    a = ap.parse_args()
    today = datetime.date.today().isoformat()
    for cp in a.cards:
        raw = yaml.safe_load(Path(cp).read_text(encoding="utf-8"))
        claim = raw.get("claim_card", raw)
        cid = claim.get("claim_id")
        refs = [er.get("citation_ref") for er in ((claim.get("five_questions") or {}).get("tested") or {}).get("evidence_relations", []) or []]
        cites = []
        for r in refs:
            for f in ROOT.glob(f"records/lit/**/citations/{r}.yaml"):
                c = yaml.safe_load(f.read_text(encoding="utf-8"))
                cites.append({kk: c.get(kk) for kk in ("id", "identifier", "exact_passage", "scope", "status", "independence_class", "disclosure")})
        out_dir = Path(a.out_dir) if a.out_dir else Path(cp).resolve().parent.parent / "reviews"
        out_dir.mkdir(parents=True, exist_ok=True)
        for i, role in enumerate([r.strip() for r in a.roles.split(",") if r.strip()], 1):
            route_id = f"R{i}"
            pdir = ROOT / "reviews" / "routes" / cid / route_id
            pdir.mkdir(parents=True, exist_ok=True)
            text = packet_text(claim, route_id, role, cites)
            (pdir / "PACKET.md").write_text(text, encoding="utf-8")
            v = run_vendor(a.vendor, text)
            (pdir / "vendor_local.json").write_text(json.dumps({"vendor": a.vendor, "date": today, "raw": v}, ensure_ascii=False, indent=1), encoding="utf-8")
            tier = v.get("verdict_tier") if v.get("verdict_tier") in TIERS.split("|") else "Dr"
            report = {
                "claim_ref": cid, "route_id": route_id,
                "reviewer_identity": f"cross-vendor AI route {route_id} (vendor recorded locally, not named: gate rule 9)",
                "independence_class": "I3", "mc_level": "L2", "role": role, "review_mode": "DECORRELATED_AI_ROUTE",
                "verdict": (v.get("verdict") or v.get("error") or "")[:900],
                "verdict_tier": tier,
                "evidence_consulted": ["claim card as pasted into PACKET.md"] + [f"citation card {c['id']}" for c in cites],
                "shared_dependency_disclosure": "same operator machine and same packet text as the maker; different vendor; no shared session",
                "disagreement_ledger_ref": None, "date": today, "approver_kind": "ai",
                "route_findings": {"defeaters_found": v.get("defeaters_found", []), "overclaims_found": v.get("overclaims_found", []), "evidence_relations_ok": v.get("evidence_relations_ok"), "notes": v.get("notes", "")},
            }
            res = k.validate_review_report(report) if hasattr(k, "validate_review_report") else {"verdict": "n/a", "errors": []}
            if res.get("errors"):
                report.pop("route_findings", None)
                res = k.validate_review_report(report)
            outp = out_dir / f"{cid}.{route_id}.review_report.json"
            outp.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
            print(cid, route_id, role, "->", res.get("verdict"), "|", report["verdict"][:110])


if __name__ == "__main__":
    main()
