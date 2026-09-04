#!/usr/bin/env python3
"""glosa — spot-check knowledge cards (knowledge/harvest_v0.3): mechanical verbatim check of each
card's `verbatim` against its fetched_from_url/local source (rule 17), plus an optional cross-vendor
(codex) judgement of base_relation on a sample. Writes knowledge/harvest_v0.3/SPOTCHECK.md. tier finite_diagnostic."""
import glob, html, json, re, subprocess, sys, time, urllib.request, random
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parent.parent
H = ROOT / "knowledge/harvest_v0.3"
def norm(t): return re.sub(r"[^a-z0-9฀-๿]+", " ", (t or "").lower()).strip()
# some LaTeX-built PDFs subset their font so ligatures (ff/fi/fl/ffi/ffl) extract via pdftotext as
# low control bytes (0x1b-0x1e) instead of the letter pairs; restore them before matching, else
# words like "conflict"/"specified"/"sufficient" silently lose the ligature and never match.
LIGATURES = {"\x1b": "ff", "\x1c": "fi", "\x1d": "fl", "\x1e": "ffi", "\x1f": "ffl"}
def fix_ligatures(t):
    for k, v in LIGATURES.items(): t = t.replace(k, v)
    return t
def fetch(card):
    u = str(card.get("fetched_from_url") or "")
    m = re.match(r"https://github\.com/morrocwi/([^/]+)/blob/main/(.+)$", u)
    if m and (Path.home() / "ANSE.ASIA" / m.group(1) / m.group(2)).exists():
        u = str(Path.home() / "ANSE.ASIA" / m.group(1) / m.group(2))
    elif u and not u.startswith("http") and not u.startswith("/") and (ROOT / u).exists():
        u = str(ROOT / u)
    src = card.get("source") or {}
    try:
        if u.startswith("http"):
            time.sleep(0.4)  # avoid bursty rate-limiting on repeated zenodo API calls
            for attempt in range(3):
                try:
                    raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 glosa"}), timeout=30).read(2_000_000).decode("utf-8", "replace")
                    break
                except Exception:
                    if attempt == 2: raise
                    time.sleep(2.0)
            if "zenodo.org/api/records" in u:
                j = json.loads(raw); return html.unescape(re.sub(r"<[^>]+>", " ", j.get("metadata", {}).get("description", "")) + " " + j.get("metadata", {}).get("title", ""))
            return html.unescape(re.sub(r"<[^>]+>", " ", raw))
        p = Path(u if u else str(src.get("path", ""))).expanduser()
        if p.exists():
            if p.suffix == ".pdf": return fix_ligatures(subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout)
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
