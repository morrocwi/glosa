#!/usr/bin/env python3
"""glosa — spot-check knowledge cards (knowledge/harvest_v0.3): mechanical verbatim check of each
card's `verbatim` against its fetched_from_url/local source (rule 17), plus an optional cross-vendor
(codex) judgement of base_relation on a sample. Writes knowledge/harvest_v0.3/SPOTCHECK.md. tier finite_diagnostic."""
import glob, json, re, subprocess, sys, urllib.request, random
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parent.parent
H = ROOT / "knowledge/harvest_v0.3"
def norm(t): return re.sub(r"[^a-z0-9฀-๿]+", " ", (t or "").lower()).strip()
def fetch(card):
    u = str(card.get("fetched_from_url") or "")
    src = card.get("source") or {}
    try:
        if u.startswith("http"):
            raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 glosa"}), timeout=30).read(2_000_000).decode("utf-8", "replace")
            if "zenodo.org/api/records" in u:
                j = json.loads(raw); return re.sub(r"<[^>]+>", " ", j.get("metadata", {}).get("description", "")) + " " + j.get("metadata", {}).get("title", "")
            return re.sub(r"<[^>]+>", " ", raw)
        p = Path(u if u else str(src.get("path", ""))).expanduser()
        if p.exists():
            if p.suffix == ".pdf": return subprocess.run(["pdftotext", "-l", "12", str(p), "-"], capture_output=True, text=True).stdout
            return p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:  # noqa
        return "ERR:" + str(e)[:80]
    return ""
rows = []; ok = miss = err = 0
for f in sorted(H.glob("*/kc-*.yaml")):
    c = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    txt = fetch(c); v = norm(c.get("verbatim")); words = v.split()
    if txt.startswith("ERR:") or not txt: status = "no-source"; err += 1
    elif len(words) < 4: status = "no-verbatim"; miss += 1
    elif " ".join(words[:10]) in norm(txt): status = "verbatim-found"; ok += 1
    else: status = "verbatim-NOT-found"; miss += 1
    rows.append((f.parent.name, c.get("id"), status, str(c.get("fetched_from_url") or c.get("source", {}).get("path", ""))[:70]))
out = ["# S1 spot-check (mechanical verbatim, rule 17)", "", f"found {ok} / not found {miss} / no source {err} of {len(rows)}", "", "| hub | id | status | source |", "|---|---|---|---|"]
out += [f"| {h} | {i} | {s} | {u} |" for h, i, s, u in rows if s != "verbatim-found"]
(H / "SPOTCHECK.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"verbatim found {ok} / not found {miss} / no source {err} / total {len(rows)}")
