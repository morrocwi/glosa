#!/usr/bin/env python3
"""glosa -- two-track venue-tier classification (design/S14_literature-review-system.md Sec 5.7).

venue_quality_index is METADATA ONLY (Sec 5.7 point 1): it is never a substitute for
claim_match_verified and never gates a card's status. It is recorded with an index_name and a
date_read so a downstream reader can tell which index produced it and when it was read.

compute_venue_tier(metadata) classifies a fetched-metadata dict into zero or more of:
  PREPRINT                    -- OpenAlex type=="preprint", or a known preprint-repo name match
                                  (arXiv/bioRxiv/medRxiv/SSRN/PsyArXiv) in the venue/container text.
                                  index_name "OpenAlex-type".
  TCI_TIER_1 / _2 / _3         -- the source is identifiably Thai (Thai-script text in title or
  or NOT_IN_TCI                  container, a .th URL, or the caller already knows the venue is
                                  Thai) AND scripts/lit_sources_thai.py::tci_tier_lookup() resolves
                                  a real tier or a confirmed NOT_IN_TCI against a supplied --tci-csv.
                                  index_name "TCI".
  Q1..Q4                       -- a --quartile-csv (Scimago SJR export shape, see
                                  QUARTILE_CSV_SCHEMA below) is supplied and the source's ISSN
                                  matches a row. index_name "SJR".
  UNRANKED_NO_QUARTILE_SOURCE  -- none of the above applied or resolved (the honest default; never
                                  fabricated).

A source can legitimately carry BOTH an international index AND a TCI tier (a Thai-authored paper
published in a preprint repo, or indexed by both TCI and Scimago) -- compute_venue_tier never
forces a single winner: it returns a single dict when exactly one applies, a list of dicts when
more than one applies, and a single UNRANKED_NO_QUARTILE_SOURCE dict when none does.

Toledo/Genesis note: this module registers no equation and derives no theorem; EPIS-TOLEDO-FIRST
and EPIS-REUSE-PIPELINE do not apply (pure classification/lookup logic, no mathematical object).
tier: finite_diagnostic for the mechanical preprint/TCI-CSV/quartile-CSV lookups themselves; Dr for
the classification policy (which signals count as "identifiably Thai", the preprint-repo name
list) -- a design decision, not a measured or derived quantity.
"""
import csv
import re
from datetime import date
from pathlib import Path

from lit_sources_thai import tci_tier_lookup

# Known preprint-repository name fragments, matched case-insensitively against the venue/container
# string or the backend's own "source" tag when OpenAlex's own "type" field is absent or not
# "preprint" (e.g. a Crossref/Zenodo/arXiv-backend hit that never carries an OpenAlex type at all).
PREPRINT_REPO_NAMES = ("arxiv", "biorxiv", "medrxiv", "ssrn", "psyarxiv")

THAI_SCRIPT_RE = re.compile(r"[฀-๿]")
TH_DOMAIN_RE = re.compile(r"\.th(?:/|$|[/?#])", re.I)

# Expected columns for --quartile-csv, matching a Scimago SJR "All journals" CSV export
# (scimagojr.com's own download; scimagojr.com itself returns HTTP 403 to programmatic fetches --
# confirmed by real curl before this task -- so this is a MANUALLY exported local file, same
# honest-fallback pattern as lit_sources_thai.py's TCI CSV). Delimiter is ';' in the real Scimago
# export (its own convention, chosen because journal titles routinely contain commas); a plain
# ',' -delimited file with the same two column names is also accepted for a hand-built CSV.
#   Issn              -- one or more ISSNs for the source, Scimago's own format joins multiple
#                         ISSNs with ", " in a single cell (print + electronic), digits only,
#                         no hyphen (e.g. "15393755, 15393755"); matching below strips
#                         non-alphanumerics from both sides so hyphenated input also matches.
#   SJR Best Quartile  -- "Q1".."Q4", or "-" for an unranked source (Scimago's own placeholder for
#                          "no quartile assigned that year"); a "-" or any value outside Q1..Q4 is
#                          treated as "no match in this row", never guessed.
QUARTILE_CSV_SCHEMA = ("Issn", "SJR Best Quartile")


def _today_iso():
    return date.today().isoformat()


def _norm_issn_list(cell):
    """Scimago's own export joins multiple ISSNs in one cell with ', '. Returns a set of
    digit-only ISSN strings (case-insensitive 'X' check-digit kept, hyphens/spaces stripped)."""
    out = set()
    for piece in re.split(r"[,;]", cell or ""):
        d = re.sub(r"[^0-9Xx]", "", piece).upper()
        if d:
            out.add(d)
    return out


def _lookup_quartile(issn, quartile_csv):
    """Returns 'Q1'..'Q4' on a matching ISSN row, else None (no match / bad file / no ISSN)."""
    if not issn or not quartile_csv:
        return None
    p = Path(quartile_csv)
    if not p.is_file():
        return None
    want = re.sub(r"[^0-9Xx]", "", issn).upper()
    if not want:
        return None
    try:
        with p.open(encoding="utf-8-sig", newline="") as f:
            sample = f.read(4096)
            f.seek(0)
            delimiter = ";" if sample.count(";") >= sample.count(",") else ","
            reader = csv.DictReader(f, delimiter=delimiter)
            if reader.fieldnames is None or not set(QUARTILE_CSV_SCHEMA) <= {c.strip() for c in reader.fieldnames}:
                return None
            for row in reader:
                q = (row.get("SJR Best Quartile") or "").strip().upper()
                if q not in ("Q1", "Q2", "Q3", "Q4"):
                    continue  # "-" or malformed: never guessed, just skipped
                if want in _norm_issn_list(row.get("Issn")):
                    return q
    except (OSError, csv.Error, UnicodeDecodeError):
        return None
    return None


def _is_preprint(metadata):
    mtype = (metadata.get("type") or "").strip().lower()
    if mtype == "preprint":
        return True
    haystack = " ".join(str(metadata.get(k) or "") for k in ("container", "source")).lower()
    return any(name in haystack for name in PREPRINT_REPO_NAMES)


def _looks_thai(metadata, reference_text):
    haystack = " ".join(str(metadata.get(k) or "") for k in ("title", "container")) + " " + (reference_text or "")
    if THAI_SCRIPT_RE.search(haystack):
        return True
    url_fields = (metadata.get("url"), metadata.get("_card_url"), metadata.get("pdf_url"))
    return any(u and TH_DOMAIN_RE.search(str(u)) for u in url_fields)


def compute_venue_tier(metadata, reference_text="", tci_csv=None, quartile_csv=None):
    """Classify one fetched-metadata dict (as returned by a lit_crossvendor_check.py backend, or
    by lit_sources_thai.fetch_thaijo) into a venue_quality_index reading.

    `metadata` is the required, positional argument (the fetched candidate). `reference_text`,
    `tci_csv`, `quartile_csv` are optional keyword-style extras: `reference_text` lets Thai-script
    detection also see the raw citing reference (not just fetched metadata, which may be in
    English even for a Thai venue); `tci_csv`/`quartile_csv` are the same manually-exported local
    tables `lit_sources_thai.tci_tier_lookup` and this module's own `_lookup_quartile` already
    document -- passed through here rather than read from argv so this function stays a pure,
    testable classifier with no CLI coupling of its own.

    Returns a single dict, a list of dicts (when more than one track legitimately applies), or a
    single {"tier": "UNRANKED_NO_QUARTILE_SOURCE", ...} dict when none applies/resolves.
    """
    metadata = metadata or {}
    today = _today_iso()
    hits = []

    if _is_preprint(metadata):
        hits.append({"tier": "PREPRINT", "index_name": "OpenAlex-type", "date_read": today})

    if _looks_thai(metadata, reference_text):
        journal_key = metadata.get("container") or metadata.get("journal") or metadata.get("title") or reference_text
        issn_key = metadata.get("issn")
        tci = tci_tier_lookup(issn_key, tci_csv=tci_csv) if issn_key else "NOT_CHECKED_NO_TCI_SOURCE"
        if not tci.startswith("Tier") and tci != "NOT_IN_TCI":
            tci = tci_tier_lookup(journal_key, tci_csv=tci_csv)
        if tci.startswith("Tier "):
            n = tci.split(" ", 1)[1]
            hits.append({"tier": f"TCI_TIER_{n}", "index_name": "TCI", "date_read": today})
        elif tci == "NOT_IN_TCI":
            hits.append({"tier": "NOT_IN_TCI", "index_name": "TCI", "date_read": today})
        # NOT_CHECKED_NO_TCI_SOURCE / LOOKUP_FAILED: no --tci-csv given or file unusable -- silently
        # falls through to the other tracks / UNRANKED below rather than asserting a tier.

    if quartile_csv:
        issn = metadata.get("issn")
        q = _lookup_quartile(issn, quartile_csv)
        if q:
            hits.append({"tier": q, "index_name": "SJR", "date_read": today})

    if not hits:
        return {"tier": "UNRANKED_NO_QUARTILE_SOURCE", "index_name": None, "date_read": today}
    return hits[0] if len(hits) == 1 else hits


if __name__ == "__main__":
    import argparse
    import json

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--title", default="")
    ap.add_argument("--container", default="")
    ap.add_argument("--type", default="", help="OpenAlex-style type field, e.g. preprint")
    ap.add_argument("--issn", default="")
    ap.add_argument("--reference-text", default="")
    ap.add_argument("--tci-csv", default=None)
    ap.add_argument("--quartile-csv", default=None)
    a = ap.parse_args()
    md = {"title": a.title, "container": a.container, "type": a.type, "issn": a.issn}
    print(json.dumps(compute_venue_tier(md, reference_text=a.reference_text, tci_csv=a.tci_csv, quartile_csv=a.quartile_csv), ensure_ascii=False, indent=1))
