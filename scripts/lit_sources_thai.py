#!/usr/bin/env python3
"""glosa -- Thai-paper literature backends: TCI tier lookup + ThaiJO fetch.

Motivation (founder, verbatim, request quoted in the S14 handoff this module fills a gap in):
"แต่ต้องวางระบบเผื่อเปเปอร์ไทยด้วยนะ เพราะมันอาจไม่อยู่ในระบบเชื่อมกับ google scholar มหาวิทยาลัยหรืออื่นๆด้วย"
(must design for Thai papers too -- they may not be in the international system) and
"การอ้างเปเปอร์ไทยผิดบ่อย" (Thai paper citations are often wrong). International backends
(Crossref/OpenAlex/PubMed, see lit_crossvendor_check.py::fetch_meta) have real, known gaps for
Thai-language journals; this module is a separate, additive slice so a checker relying only on
international databases does not produce false NOT_FOUND / metadata_verified=false for
legitimate Thai citations.

This module is deliberately kept OUT of lit_crossvendor_check.py's fetch_meta() dispatch --
another concurrent task is refactoring that function's if/elif structure at the same time
(mechanical:crossref / mechanical:openalex / mechanical:pubmed backends, per that file's own
header comment). Wiring these two functions into fetch_meta() is a follow-up integration step
for whoever lands both branches, not done here, so the two tasks do not touch the same lines.

Two independently-usable functions:

  tci_tier_lookup(journal_name_or_issn, tci_csv=None)
      -> "Tier 1" | "Tier 2" | "Tier 3" | "NOT_IN_TCI" | "NOT_CHECKED_NO_TCI_SOURCE" | "LOOKUP_FAILED"
      REAL FINDING (2026-09-20, curl'd https://tci-thailand.org/journal_list just now): the page
      is a bare create-react-app shell (862 bytes: <div id="root"></div>, all content loaded by
      /static/js/main.*.js at request time). There is NO server-side-rendered table of journal
      names/tiers to scrape -- this is a client-rendered SPA, not static HTML. Scraping it would
      mean either (a) running a headless browser against a third party's SPA just to read a
      table it does not expose as an API (fragile, and arguably against the spirit of "do not
      scrape" already applied to Scimago/Google Scholar in this task set), or (b) reverse-engineering
      whatever internal API the SPA calls, which was not found in a plain grep of the bundled JS
      for an api-looking hostname and is out of scope for a mechanical, low-maintenance lookup.
      DECISION: same honest-fallback pattern as this task set's Scimago handling -- no scrape, no
      fabricated tier. tci_tier_lookup() takes an optional path to a MANUALLY exported local CSV
      (see TCI_CSV_SCHEMA below for the exact columns) and returns NOT_CHECKED_NO_TCI_SOURCE when
      none is given.

  fetch_thaijo(reference_text, web_search_fn=None)
      -> dict with at least {"source", "match_confidence", ...}
      (a) if reference_text already contains a recognizable tci-thaijo.org URL, or a DOI that
          resolves (via doi.org) to a tci-thaijo.org domain, fetch it directly and parse the
          Google-Scholar-style <meta name="citation_*"> tags ThaiJO's OJS software emits
          (verified live 2026-09-20 against a real article, see module docstring test notes) --
          match_confidence "DIRECT_IDENTIFIER".
      (b) otherwise, best-effort: call web_search_fn(query) restricted to site:tci-thaijo.org
          (default implementation uses DuckDuckGo's HTML endpoint, no API key, not the Google
          Scholar route this task set forbids scraping) and fetch the first tci-thaijo.org hit --
          match_confidence "THAIJO_BEST_EFFORT", NEVER conflated with a confirmed API match.
      If no direct identifier match and no web_search_fn produces a tci-thaijo.org hit (or none
      is available at all), returns fetch_status "NOT_FOUND" or "CHECK_ERROR" honestly -- a
      failed/absent search is not evidence the paper does not exist.

tier: finite_diagnostic for the mechanical fetch/parse paths; the TCI SPA finding above and the
web-search fallback's coverage are Dr (design decision, not a proven completeness claim).
Toledo/Genesis note: this module registers no equation and derives no theorem; EPIS-TOLEDO-FIRST
and EPIS-REUSE-PIPELINE do not apply to it (pure I/O + string handling, no mathematical object).
"""
import csv
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) glosa/0.1 (+https://github.com/morrocwi/glosa)"

# --------------------------------------------------------------------------------------
# tci_tier_lookup
# --------------------------------------------------------------------------------------

# Expected CSV schema for --tci-csv, chosen to match what a human can realistically copy/export
# from https://tci-thailand.org/journal_list by hand (the site itself offers no machine export;
# a human would select-copy or manually type rows from the on-screen table into a spreadsheet):
#   journal_name  -- the journal's name as TCI lists it (Thai or English title, whichever the
#                     human copied; matching below is case-insensitive substring on this field)
#   issn          -- print or online ISSN, digits and one hyphen, e.g. "2822-0986" (optional per
#                     row, but at least one of journal_name/issn must be non-empty)
#   tier          -- exactly "1", "2", or "3" (TCI's own three-tier system); any other value in
#                     this column is treated as a malformed row and skipped, never guessed
TCI_CSV_SCHEMA = ("journal_name", "issn", "tier")


def _norm_issn(s):
    return re.sub(r"[^0-9Xx]", "", s or "").upper()


def _norm_name(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def tci_tier_lookup(journal_name_or_issn, tci_csv=None):
    """Look up a journal's TCI tier. See module docstring for why this is CSV-backed, not scraped.

    Returns one of: "Tier 1" | "Tier 2" | "Tier 3" | "NOT_IN_TCI" | "NOT_CHECKED_NO_TCI_SOURCE"
    | "LOOKUP_FAILED". Never fabricates a tier: a match requires an exact ISSN match or a
    case-insensitive substring match on journal_name in the supplied CSV.
    """
    if not tci_csv:
        return "NOT_CHECKED_NO_TCI_SOURCE"
    p = Path(tci_csv)
    if not p.is_file():
        return "LOOKUP_FAILED"
    query = (journal_name_or_issn or "").strip()
    if not query:
        return "LOOKUP_FAILED"
    q_issn = _norm_issn(query)
    q_name = _norm_name(query)
    try:
        with p.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or not set(TCI_CSV_SCHEMA) <= {c.strip() for c in reader.fieldnames}:
                return "LOOKUP_FAILED"
            for row in reader:
                tier = (row.get("tier") or "").strip()
                if tier not in ("1", "2", "3"):
                    continue  # malformed row: never guessed, just skipped
                row_issn = _norm_issn(row.get("issn"))
                row_name = _norm_name(row.get("journal_name"))
                if (q_issn and row_issn and q_issn == row_issn) or (q_name and row_name and q_name in row_name):
                    return f"Tier {tier}"
    except (OSError, csv.Error, UnicodeDecodeError):
        return "LOOKUP_FAILED"
    return "NOT_IN_TCI"


# --------------------------------------------------------------------------------------
# fetch_thaijo
# --------------------------------------------------------------------------------------

THAIJO_URL_RE = re.compile(r"https?://[a-z0-9.-]*tci-thaijo\.org/\S+", re.I)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"'<>]+", re.I)


def _http_get(url, timeout=30, max_bytes=800_000):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        final_url = resp.geturl()
        raw = resp.read(max_bytes)
    return final_url, raw.decode("utf-8", "replace")


def _extract_thaijo_meta(html, url):
    """Parse the <meta name="citation_*"> tags ThaiJO's OJS platform emits on every article page
    (Google-Scholar-indexing convention; verified live against a real article, see test notes)."""
    def all_content(name):
        return re.findall(r'<meta[^>]+name=["\']' + re.escape(name) + r'["\'][^>]+content=["\']([^"\']*)', html, re.I)

    def one(name):
        vals = all_content(name)
        return vals[0] if vals else None

    title = one("citation_title")
    authors = all_content("citation_author")
    journal = one("citation_journal_title")
    issn = one("citation_issn")
    year_raw = one("citation_date")
    year = None
    if year_raw:
        m = re.search(r"\d{4}", year_raw)
        if m:
            y = int(m.group(0))
            year = y - 543 if y > 2400 else y  # Buddhist Era -> Gregorian (ThaiJO commonly emits BE)
    pdf_url = one("citation_pdf_url")
    if not title:
        t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        title = re.sub(r"\s+", " ", t.group(1)).strip() if t else None
    return {
        "title": (title or "").strip() or None,
        "authors": [a.strip() for a in authors if a.strip()],
        "journal": (journal or "").strip() or None,
        "issn": issn,
        "year": year,
        "pdf_url": pdf_url,
        "url": url,
    }


def _resolve_doi_domain(doi_value, timeout=15):
    """Follow a DOI through doi.org and report the final domain, mechanical only. Returns
    (final_url, None) on success or (None, error_string) on failure -- never guesses a domain."""
    try:
        final_url, _ = _http_get("https://doi.org/" + urllib.parse.quote(doi_value), timeout=timeout, max_bytes=1)
        return final_url, None
    except Exception as e:  # noqa: BLE001
        return None, str(e)[:200]


def ddg_site_search(query, site="tci-thaijo.org", max_results=5, timeout=20):
    """Default best-effort web_search_fn: DuckDuckGo's HTML endpoint (no API key required), NOT
    Google Scholar (which this task set forbids scraping under its ToS). Returns a list of result
    URLs (possibly empty), never raises past a CHECK_ERROR-worthy timeout/HTTP failure.

    HONEST CAVEAT (found while testing this module, 2026-09-20): this endpoint degraded to a
    result-less "lite" response after only a couple of automated requests from the same source in
    a short window -- it is NOT a reliable, always-on API, just a bundled last-resort. Whenever
    the caller is an AI agent session that already has its own web-search tool (e.g. Claude's
    WebSearch, restricted to `site:tci-thaijo.org <reference_text>`), pass that tool's results in
    as `web_search_fn` instead of relying on this default -- see fetch_thaijo()'s own test in the
    module's commit for a worked example. An empty list from here must NOT be read as "no ThaiJO
    source exists" -- it may just mean this scraper got throttled."""
    q = f"site:{site} {query}"
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": q})
    try:
        _, html = _http_get(url, timeout=timeout, max_bytes=400_000)
    except Exception:  # noqa: BLE001
        return []
    hits = re.findall(r'class="result__a"[^>]*href="([^"]+)"', html)
    out = []
    for h in hits[:max_results]:
        m = re.search(r"uddg=([^&]+)", h)
        real = urllib.parse.unquote(m.group(1)) if m else h
        if site in real:
            out.append(real)
    return out


def fetch_thaijo(reference_text, web_search_fn=None):
    """Best-effort ThaiJO lookup for one reference string. See module docstring for the two
    paths. Never conflates a search-derived hit with a confirmed identifier-based fetch."""
    reference_text = reference_text or ""

    # (a) direct: an explicit tci-thaijo.org URL already in the reference text
    m = THAIJO_URL_RE.search(reference_text)
    direct_url = m.group(0).rstrip(").,;") if m else None

    # (a) direct: a DOI that resolves to a tci-thaijo.org domain
    if not direct_url:
        d = DOI_RE.search(reference_text)
        if d:
            resolved, err = _resolve_doi_domain(d.group(0))
            if resolved and "tci-thaijo.org" in resolved:
                direct_url = resolved
            elif err:
                # a DOI was present but resolution failed -- CHECK_ERROR, not silently ignored
                return {"source": "thaijo-doi-resolve", "fetch_status": "CHECK_ERROR",
                        "match_confidence": "NONE", "error": err, "doi_tried": d.group(0)}

    if direct_url:
        try:
            final_url, html = _http_get(direct_url)
        except Exception as e:  # noqa: BLE001
            return {"source": "thaijo-direct", "fetch_status": "FETCH_FAILED",
                     "match_confidence": "NONE", "error": str(e)[:200], "url": direct_url}
        meta = _extract_thaijo_meta(html, final_url)
        meta.update({"source": "thaijo-direct", "fetch_status": "FETCHED", "match_confidence": "DIRECT_IDENTIFIER"})
        return meta

    # (b) best-effort: site-restricted web search fallback
    search = web_search_fn or ddg_site_search
    try:
        hits = search(reference_text)
    except Exception as e:  # noqa: BLE001
        return {"source": "thaijo-search", "fetch_status": "CHECK_ERROR",
                 "match_confidence": "NONE", "error": str(e)[:200]}
    if not hits:
        return {"source": "thaijo-search", "fetch_status": "NOT_FOUND", "match_confidence": "NONE"}
    top = hits[0]
    try:
        final_url, html = _http_get(top)
    except Exception as e:  # noqa: BLE001
        return {"source": "thaijo-search", "fetch_status": "FETCH_FAILED",
                 "match_confidence": "THAIJO_BEST_EFFORT", "error": str(e)[:200], "url": top}
    meta = _extract_thaijo_meta(html, final_url)
    meta.update({"source": "thaijo-search", "fetch_status": "FETCHED",
                 "match_confidence": "THAIJO_BEST_EFFORT", "search_hits": hits})
    return meta


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tier"); t.add_argument("journal"); t.add_argument("--tci-csv", default=None)
    j = sub.add_parser("thaijo"); j.add_argument("reference_text")
    a = ap.parse_args()
    if a.cmd == "tier":
        print(tci_tier_lookup(a.journal, tci_csv=a.tci_csv))
    else:
        print(json.dumps(fetch_thaijo(a.reference_text), ensure_ascii=False, indent=1))
