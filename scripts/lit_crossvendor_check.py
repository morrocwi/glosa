#!/usr/bin/env python3
"""glosa — cross-vendor (I3) claim-match route for literature citation cards.

For every citation_card under records/lit/<slug>/<hyp>/citations/, build a packet holding ONLY
mechanically fetched material (Crossref/Zenodo/OpenAlex metadata + abstract when available, the
card's exact_passage, the hypothesis statement, the card's declared scope) and ask a DIFFERENT
AI vendor (default: OpenAI codex-cli, read-only, no network) to judge:
  metadata_matches  — does the fetched metadata match the card's title/authors/year?
  passage_plausible — is the exact_passage consistent with the fetched abstract/title (never
                      proven from abstract alone; full text is not fetched here)?
  claim_match       — does the source, as evidenced, bear on the hypothesis in the way the card's
                      scope says (SUPPORTS / CHALLENGES / CONTEXT_ONLY)?
The verdict is written next to the card as <card>.i3.json and the card is updated:
  status VERIFIED  only if metadata_matches AND claim_match AND passage_plausible,
  else stays METADATA_OK; independence_class -> I3; who_verified names the route.
tier: finite_diagnostic. Everything here is a readout, not truth: the I3 route is another bounded
reader, and abstract-level judgement is disclosed as such on every card.

usage: lit_crossvendor_check.py <slug> <hyp> [--vendor codex|gemini] [--dry-run]
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def fetch_meta(identifier):
    kind = (identifier or {}).get("kind", "")
    val = (identifier or {}).get("value", "")
    try:
        if kind == "DOI" and val:
            j = json.load(urllib.request.urlopen("https://api.crossref.org/works/" + urllib.parse.quote(val), timeout=30))["message"]
            return {"source": "crossref", "title": " ".join(j.get("title", [])), "authors": [a.get("family", "") for a in j.get("author", [])][:6],
                    "year": (j.get("issued", {}).get("date-parts") or [[None]])[0][0], "container": " ".join(j.get("container-title", [])),
                    "abstract": re.sub(r"<[^>]+>", " ", j.get("abstract", ""))[:1500]}
        if kind == "ARXIV" and val:
            aid = re.sub(r"^(arxiv:|https?://arxiv\.org/abs/)", "", val, flags=re.I)
            xml = urllib.request.urlopen("https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(aid), timeout=30).read().decode("utf-8", "replace")
            t = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S); ab = re.search(r"<summary>(.*?)</summary>", xml, re.S)
            au = re.findall(r"<name>(.*?)</name>", xml)[:6]; yr = re.search(r"<published>(\d{4})", xml)
            return {"source": "arxiv", "title": re.sub(r"\s+", " ", t.group(1)).strip() if t else "", "authors": au, "year": yr.group(1) if yr else None, "abstract": re.sub(r"\s+", " ", ab.group(1)).strip()[:1500] if ab else ""}
        if kind in ("URL", "OFFICIAL_URL", "WEB", "WEBPAGE") and val:
            html = urllib.request.urlopen(urllib.request.Request(val, headers={"User-Agent": "glosa/0.1"}), timeout=30).read(200000).decode("utf-8", "replace")
            title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
            desc = re.search(r'<meta[^>]+(?:name|property)=["\'](?:description|og:description)["\'][^>]+content=["\']([^"\']+)', html, re.I)
            return {"source": "url-fetch", "title": (title.group(1).strip() if title else "")[:300], "abstract": (desc.group(1) if desc else "")[:1500]}
    except Exception as e:  # noqa: BLE001
        return {"source": "fetch-failed", "error": str(e)[:200]}
    return {"source": "no-identifier"}


def fetch_fulltext(identifier, meta):
    """Best-effort open full text (arXiv abs/HTML, the landing page of a DOI, or the URL itself).
    Returns normalized text or ''. Mechanical only."""
    kind = (identifier or {}).get("kind", ""); val = (identifier or {}).get("value", "")
    urls = []
    if kind == "ARXIV" and val:
        aid = re.sub(r"^(arxiv:|https?://arxiv\.org/abs/)", "", val, flags=re.I)
        urls += [f"https://arxiv.org/html/{aid}", f"https://arxiv.org/abs/{aid}"]
    elif kind == "DOI" and val:
        urls += [f"https://doi.org/{val}"]
    elif val:
        urls += [val]
    for u in urls:
        try:
            html = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "glosa/0.1 (+https://github.com/morrocwi/glosa)"}), timeout=40).read(3_000_000).decode("utf-8", "replace")
            text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"&nbsp;|&#160;", " ", text); text = re.sub(r"&amp;", "&", text); text = re.sub(r"&quot;|&#8220;|&#8221;", '"', text)
            text = re.sub(r"\s+", " ", text)
            if len(text) > 800:
                return text
        except Exception:  # noqa: BLE001
            continue
    return ""


def _norm(t):
    return re.sub(r"[^a-z0-9\u0e00-\u0e7f]+", " ", (t or "").lower()).strip()


def passage_found(exact_passage, fulltext):
    """Mechanical check: is (a decent prefix of) the quoted passage present verbatim in the fetched text?"""
    if not exact_passage or not fulltext:
        return None
    p = _norm(exact_passage); f = _norm(fulltext)
    words = p.split()
    if len(words) < 4:
        return None
    probe = " ".join(words[:12])
    return probe in f


def packet(card, hyp_text, meta, passage_hit=None, excerpt=""):
    return (
        "You are an independent checker from a different AI vendor (I3 route) for ONE literature citation card. "
        "Judge ONLY from the material below; do not use outside knowledge; do not browse. Output JSON only: "
        '{"metadata_matches": bool, "passage_plausible": bool, "claim_match": bool, "bearing": "SUPPORTS|CHALLENGES|CONTEXT_ONLY", "reason": "<=60 words"}\n\n'
        f"HYPOTHESIS: {hyp_text}\n\nCARD (written by another AI):\n"
        f"  id: {card.get('id')}\n  identifier: {card.get('identifier')}\n  card_title/notes: {card.get('notes','')[:300]}\n"
        f"  scope: {card.get('scope')}\n  exact_passage: {card.get('exact_passage','')[:600]}\n  page_or_locator: {card.get('page_or_locator')}\n\n"
        f"MECHANICALLY FETCHED METADATA: {json.dumps(meta, ensure_ascii=False)[:2500]}\n"
        f"MECHANICAL PASSAGE CHECK (verbatim search of the quoted passage in the fetched open text): {passage_hit}\n"
        f"FETCHED TEXT EXCERPT (around the passage if found, else the opening): {excerpt[:2500]}\n\n"
        "Rules: metadata_matches=false if title/authors/year contradict the card. passage_plausible=false if the exact_passage contradicts the "
        "abstract/title or if there is no fetched text to compare (say so in reason). claim_match=true only if the source as evidenced bears on the "
        "hypothesis as the card's scope claims. If uncertain, answer false."
    )


def run_vendor(vendor, text):
    if vendor == "codex":
        r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "-s", "read-only", text], capture_output=True, text=True, timeout=300)
        out = r.stdout
    else:
        r = subprocess.run(["gemini", "-p", text], capture_output=True, text=True, timeout=300)
        out = r.stdout
    m = re.search(r"\{.*?\}", out, re.S)
    return json.loads(m.group(0)) if m else {"error": "no-json", "raw": out[-400:]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("hyp"); ap.add_argument("--vendor", default="codex"); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    hdir = ROOT / "records" / "lit" / a.slug / a.hyp.lower()
    sl = yaml.safe_load((hdir / "search_log.yaml").read_text(encoding="utf-8"))
    hyp_text = (sl.get("frozen_scope") or {}).get("question") or sl.get("hypothesis_text") or a.hyp
    cards = sorted((hdir / "citations").glob("*.yaml"))
    summary = []
    for cp in cards:
        card = yaml.safe_load(cp.read_text(encoding="utf-8"))
        meta = fetch_meta(card.get("identifier"))
        if a.dry_run:
            print(cp.name, meta.get("source"), (meta.get("title") or "")[:70]); continue
        full = fetch_fulltext(card.get("identifier"), meta)
        hit = passage_found(card.get("exact_passage"), full)
        excerpt = ""
        if full:
            if hit:
                i = _norm(full).find(" ".join(_norm(card.get("exact_passage")).split()[:12]))
                excerpt = _norm(full)[max(0, i - 900): i + 1500]
            else:
                excerpt = full[:2000]
        v = run_vendor(a.vendor, packet(card, hyp_text, meta, hit, excerpt))
        if hit is True:
            v["passage_plausible"] = True  # mechanical verbatim hit outranks the reader's guess
            v["passage_mechanical"] = "verbatim prefix found in fetched open text"
        elif hit is False:
            v["passage_mechanical"] = "quoted passage NOT found verbatim in fetched open text"
        else:
            v["passage_mechanical"] = "no open full text fetched; abstract/metadata only"
        ok = bool(v.get("metadata_matches")) and bool(v.get("passage_plausible")) and bool(v.get("claim_match"))
        (hdir / "citations" / (cp.stem + ".i3.json")).write_text(json.dumps({"vendor": a.vendor, "fetched": meta, "verdict": v, "date": "2026-09-04"}, ensure_ascii=False, indent=1), encoding="utf-8")
        card["independence_class"] = "I3"
        card["who_verified"] = f"route:{a.vendor} (cross-vendor AI; abstract/metadata level, not full text) -- see {cp.stem}.i3.json"
        card["verification_method"] = "MECHANICAL_LOOKUP_PLUS_MANUAL_READ"
        card["claim_match_verified"] = bool(v.get("claim_match"))
        card["claim_match_verified_by"] = f"route:{a.vendor}"
        card["status"] = "VERIFIED" if ok else "METADATA_OK"
        card["disclosure"] = (card.get("disclosure") or "") + f" | I3 route ({a.vendor}) judged from fetched metadata/abstract + the card's quoted passage, not full text: {v.get('reason','')}"
        cp.write_text(yaml.safe_dump(card, allow_unicode=True, sort_keys=False), encoding="utf-8")
        summary.append((cp.name, card["status"], v.get("bearing"), (v.get("reason") or "")[:90]))
        print(cp.name, card["status"], v.get("bearing"), "|", (v.get("reason") or "")[:90])
    if not a.dry_run:
        print(f"{sum(1 for s in summary if s[1]=='VERIFIED')}/{len(summary)} VERIFIED")


if __name__ == "__main__":
    main()
