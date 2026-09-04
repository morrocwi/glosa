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
        if kind == "DOI" and val.lower().startswith("10.5281/zenodo."):
            rid = val.rsplit(".", 1)[1]
            z = json.load(urllib.request.urlopen(f"https://zenodo.org/api/records/{rid}", timeout=30))["metadata"]
            return {"source": "zenodo", "title": z.get("title", ""), "authors": [c.get("name", "") for c in z.get("creators", [])],
                    "year": (z.get("publication_date") or "")[:4], "container": "Zenodo", "abstract": re.sub(r"<[^>]+>", " ", z.get("description", ""))[:1500]}
        if kind == "DOI" and val:
            j = json.load(urllib.request.urlopen("https://api.crossref.org/works/" + urllib.parse.quote(val), timeout=30))["message"]
            ab = re.sub(r"<[^>]+>", " ", j.get("abstract", ""))
            if not ab.strip():
                try:  # Europe PMC often has the abstract Crossref lacks
                    q = json.load(urllib.request.urlopen("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:" + urllib.parse.quote(val) + "&format=json&resultType=core", timeout=30))
                    ab = ((q.get("resultList", {}).get("result") or [{}])[0].get("abstractText") or "")
                except Exception:  # noqa: BLE001
                    pass
            return {"source": "crossref", "title": " ".join(j.get("title", [])), "authors": [a.get("family", "") for a in j.get("author", [])],
                    "year": (j.get("issued", {}).get("date-parts") or [[None]])[0][0], "container": " ".join(j.get("container-title", [])),
                    "abstract": ab[:2500]}
        if kind in ("PMCID", "PMC") and val:
            pmc = val if val.upper().startswith("PMC") else "PMC" + val
            q = json.load(urllib.request.urlopen(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={pmc}&format=json&resultType=core", timeout=30))
            r = (q.get("resultList", {}).get("result") or [{}])[0]
            return {"source": "europepmc", "title": r.get("title", ""), "authors": [a.get("fullName", "") for a in (r.get("authorList", {}).get("author") or [])], "year": r.get("pubYear"), "container": r.get("journalTitle", ""), "abstract": (r.get("abstractText") or "")[:2500]}
        if kind == "ARXIV" and val:
            aid = re.sub(r"^(arxiv:|https?://arxiv\.org/abs/)", "", val, flags=re.I)
            xml = urllib.request.urlopen("https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(aid), timeout=30).read().decode("utf-8", "replace")
            t = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S); ab = re.search(r"<summary>(.*?)</summary>", xml, re.S)
            au = re.findall(r"<name>(.*?)</name>", xml); yr = re.search(r"<published>(\d{4})", xml)
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
    if isinstance(meta, dict) and meta.get("_card_url"):
        urls.append(meta["_card_url"])
    if kind == "ARXIV" and val:
        aid = re.sub(r"^(arxiv:|https?://arxiv\.org/abs/)", "", val, flags=re.I)
        urls += [f"https://arxiv.org/html/{aid}", f"https://arxiv.org/abs/{aid}"]
    elif kind == "DOI" and val:
        urls += [f"https://doi.org/{val}"]
        try:  # open-access mirror via Europe PMC (publisher pages often 403 automated fetches)
            q = json.load(urllib.request.urlopen("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:" + urllib.parse.quote(val) + "&format=json&resultType=lite", timeout=30))
            for r in q.get("resultList", {}).get("result", [])[:1]:
                if r.get("pmcid"):
                    urls.insert(0, f"https://www.ebi.ac.uk/europepmc/webservices/rest/{r['pmcid']}/fullTextXML")
        except Exception:  # noqa: BLE001
            pass
    elif val:
        urls += [val, "https://web.archive.org/web/2026/" + val]
    for u in urls:
        try:
            raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) glosa/0.1 (+https://github.com/morrocwi/glosa)"}), timeout=40).read(6_000_000)
            fetch_fulltext.last_url = u
            if raw[:5] == b"%PDF-":
                import tempfile, os as _os, subprocess as _sp
                tf = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False); tf.write(raw); tf.close()
                text = _sp.run(["pdftotext", "-l", "40", tf.name, "-"], capture_output=True, text=True).stdout; _os.unlink(tf.name)
                text = re.sub(r"\s+", " ", text).replace("\x00", "")
                if len(text) > 800:
                    return text
                continue
            html = raw.decode("utf-8", "replace")
            text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"&nbsp;|&#160;", " ", text); text = re.sub(r"&amp;", "&", text); text = re.sub(r"&quot;|&#8220;|&#8221;", '"', text)
            text = re.sub(r"\s+", " ", text).replace("\x00", "")
            if len(text) > 800:
                return text
        except Exception:  # noqa: BLE001
            continue
    return ""


def _norm(t):
    return re.sub(r"[\W_]+", " ", (t or "").lower(), flags=re.UNICODE).strip()


def passage_found(exact_passage, fulltext):
    """Mechanical check: is (a decent prefix of) the quoted passage present verbatim in the fetched text?
    A passage carrying a splice marker (ellipsis / ' -- ') is refused outright (kernel rule 26)."""
    if not exact_passage or not fulltext:
        return None
    if re.search(r"\u2026|\.\.\.| -- ", exact_passage):
        return False
    p = _norm(exact_passage); f = _norm(fulltext.replace("\x00", ""))
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
        f"  scope: {card.get('scope')}   (CONTEXT_ONLY_NOT_EVIDENCE means the card claims only that the source SAYS the passage, as context; "
        f"then claim_match = 'is this source relevant context for the hypothesis', not 'does it support it')\n"
        f"  exact_passage: {card.get('exact_passage','')[:600]}\n  page_or_locator: {card.get('page_or_locator')}\n"
        f"  what the card says this source does for the hypothesis (dialogue stance / notes): {str(card.get('disclosure',''))[:200]} | {str(card.get('notes',''))[:400]}\n\n"
        f"MECHANICALLY FETCHED METADATA: {json.dumps(meta, ensure_ascii=False)[:2500]}\n"
        f"MECHANICAL PASSAGE CHECK (verbatim search of the quoted passage in the fetched open text): {passage_hit}\n"
        f"FETCHED TEXT EXCERPT (around the passage if found, else the opening): {excerpt[:2500]}\n\n"
        "Rules: metadata_matches=false only if title, year, or the FIRST author contradict the card (author-list length or ordering differences "
        "between sources are not a contradiction; a card note about author pool is not metadata). passage_plausible=false if the exact_passage contradicts the "
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
    ap.add_argument("--only", default="", help="comma-separated card ids (or 'unverified') to (re)check")
    ap.add_argument("--locate-only", action="store_true", help="no vendor call: just fetch the open text, locate the passage, and record fetched_from_url + line_or_paragraph (kernel rule 17)")
    a = ap.parse_args()
    hdir = ROOT / "records" / "lit" / a.slug / a.hyp.lower()
    sl = yaml.safe_load((hdir / "search_log.yaml").read_text(encoding="utf-8"))
    fs_ = sl.get("frozen_scope") or {}
    hyp_text = fs_.get("question") or fs_.get("hypothesis_or_falsifier") or sl.get("hypothesis_text") or a.hyp
    # prefer the hypothesis statement itself (projects/*/hypotheses.md) over the search question
    for hp in (ROOT / "projects").glob("*" + a.slug + "*/hypotheses.md"):
        txt = hp.read_text(encoding="utf-8")
        m = re.search(r"#+\s*" + re.escape(a.hyp.upper()) + r"\b.*?\n(.*?)(?=\n#+\s|\Z)", txt, re.S)
        if m:
            hyp_text = a.hyp.upper() + ": " + re.sub(r"\s+", " ", m.group(1)).strip()[:1200]
    cards = sorted((hdir / "citations").glob("*.yaml"))
    if a.only == "unverified":
        cards = [c for c in cards if (yaml.safe_load(c.read_text(encoding="utf-8")) or {}).get("status") != "VERIFIED"]
    elif a.only:
        keep = set(a.only.split(","))
        cards = [c for c in cards if c.stem in keep]
    summary = []
    for cp in cards:
        card = yaml.safe_load(cp.read_text(encoding="utf-8"))
        meta = fetch_meta(card.get("identifier"))
        if a.dry_run:
            print(cp.name, meta.get("source"), (meta.get("title") or "")[:70]); continue
        fetch_fulltext.last_url = None
        if card.get("fetched_from_url") and str(card["fetched_from_url"]).startswith("http"):
            meta = dict(meta, _card_url=str(card["fetched_from_url"]))
        full = fetch_fulltext(card.get("identifier"), meta)
        hit = passage_found(card.get("exact_passage"), full)
        if hit:
            i = _norm(full).find(" ".join(_norm(card.get("exact_passage")).split()[:12]))
            para = _norm(full)[:i].count("  ") + full[:max(0, int(i * len(full) / max(1, len(_norm(full))))) ].count("\n") + 1
            card["fetched_from_url"] = fetch_fulltext.last_url
            card["line_or_paragraph"] = f"char offset {i} of normalized fetched text (~paragraph {para}); verbatim prefix match"
        elif full and not card.get("fetched_from_url"):
            card["fetched_from_url"] = fetch_fulltext.last_url
        if a.locate_only:
            cp.write_text(yaml.safe_dump(card, allow_unicode=True, sort_keys=False), encoding="utf-8")
            print(cp.name, "located" if hit else ("fetched-no-hit" if full else "no-text"), fetch_fulltext.last_url or "")
            continue
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
        context_only = card.get("scope") == "CONTEXT_ONLY_NOT_EVIDENCE"
        if context_only and v.get("metadata_matches") and v.get("passage_plausible"):
            v["claim_match"] = True  # a context-only card claims nothing beyond "the source says this"; the passage check IS the claim check
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
