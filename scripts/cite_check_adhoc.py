#!/usr/bin/env python3
"""glosa -- lightweight ad-hoc single-reference citation check.

The full pipeline (lit_crossvendor_check.py) needs a records/lit/<slug>/<hyp>/ manifest tree --
too heavy for "check 8 references in one paper" or a one-off spot check. This is a SEPARATE
script, not a mode flag on lit_crossvendor_check.py, because that file already has a slug/hyp-based
CLI contract (frozen scope, citations/ directory, .i3.json siblings) this deliberately does not
disturb.

What it does, for ONE raw reference string:
  1. Tries every backend in scripts/lit_crossvendor_check.py::FETCH_BACKENDS (the same registry
     lit_crossvendor_check.py itself dispatches through -- reused by import, not duplicated) across
     every identifier shape the caller gave it (a --doi/--pmid if supplied, an arXiv id extracted
     from an arXiv-style DOI, and the bare reference text itself for the backends that support a
     title search). Unlike fetch_meta() (which stops at the first non-None backend, because a
     manifest card already knows its identifier kind), this tries ALL of them and keeps every
     candidate, because an ad-hoc check does not know in advance which backend will actually hold
     this source.
  2. Scores each candidate's title against --reference with difflib.SequenceMatcher (stdlib, no
     new dependency) and classifies existence_tier:
       VERIFIED_EXACT  similarity >= 0.85
       VERIFIED_FUZZY  0.6 <= similarity < 0.85
       AMBIGUOUS       two or more candidates >= 0.6 within AMBIGUOUS_MARGIN of each other
       NOT_FOUND       every backend returned nothing (or nothing >= 0.6) and none errored
       CHECK_ERROR     a backend errored/rate-limited AND no other backend found anything either
                       -- never silently equated with NOT_FOUND (a rate-limit is not the same
                       fact as "does not exist").
  3. Computes venue_tier via scripts/lit_venue_tier.py::compute_venue_tier on the winning
     candidate's metadata (§5.7: metadata only, never a substitute for claim_match).
  4. If --claim was given, invokes the SAME cross-vendor AI dispatch mechanism
     lit_crossvendor_check.py already uses (its own packet()/run_vendor() functions, imported and
     called directly -- not reimplemented) to get a claim_match verdict against a synthetic,
     single-use card built from --reference/--claim.
  5. Emits one JSON object carrying all of the above PLUS a mandatory "disclosure" string that
     must never be silently omitted (see DISCLOSURE below): this is not a full citation_card.yaml
     and no §5.4 human spot-check sampling has been applied to it.

usage:
  cite_check_adhoc.py --reference "<text>" [--doi <doi>] [--pmid <pmid>] [--claim "<sentence>"]
                       [--vendor claude|codex|gemini] [--tci-csv <path>] [--quartile-csv <path>]
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lit_crossvendor_check import FETCH_BACKENDS, packet, run_vendor, route_class  # noqa: E402
from lit_venue_tier import compute_venue_tier  # noqa: E402

DISCLOSURE = (
    "LIGHTWEIGHT_ADHOC_CHECK -- not a full citation_card.yaml, no §5.4 human spot-check "
    "sampling applied; do not treat this as status: VERIFIED"
)

ARXIV_DOI_RE = re.compile(r"^10\.48550/arxiv\.(.+)$", re.I)
AMBIGUOUS_MARGIN = 0.05


def _norm(t):
    return re.sub(r"\s+", " ", (t or "").strip().lower())


def _similarity(a, b):
    return difflib.SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def _identifier_variants(reference, doi, pmid):
    """Every identifier shape worth trying against the registry for ONE ad-hoc reference. Order
    is not significant here (unlike fetch_meta()'s first-match dispatch) since every variant is
    tried against every backend and every non-None result is scored, not just the first."""
    seen = set()
    variants = []

    def add(kind, value):
        key = (kind, value)
        if value and key not in seen:
            seen.add(key)
            variants.append({"kind": kind, "value": value})

    if doi:
        add("DOI", doi)
        m = ARXIV_DOI_RE.match(doi.strip())
        if m:
            add("ARXIV", m.group(1))
    if pmid:
        add("PMID", pmid)
    # Bare-text fallback: enables the title-search paths in fetch_openalex/fetch_pubmed/
    # fetch_semanticscholar even when no identifier was supplied at all, and widens the net
    # alongside an identifier when one was.
    add("", reference)
    return variants


# Which backends a given identifier.kind actually engages, mirroring each fetch_*() function's
# own kind-gate (see lit_crossvendor_check.py) -- used ONLY to tell a genuine "this backend ran a
# real check and confirmed nothing" from "this backend was not applicable to this identifier kind
# at all", so a rate-limit on one backend never masks a real, completed, clean search by another.
_BACKEND_APPLIES = {
    "zenodo": lambda kind: kind == "DOI",
    "crossref": lambda kind: kind == "DOI",
    "europepmc": lambda kind: kind in ("PMCID", "PMC"),
    "arxiv": lambda kind: kind == "ARXIV",
    "url-fetch": lambda kind: kind in ("URL", "OFFICIAL_URL", "WEB", "WEBPAGE"),
    "openalex": lambda kind: kind == "DOI" or kind in ("", "OTHER_STABLE", "TITLE"),
    "pubmed": lambda kind: kind == "PMID" or kind in ("", "OTHER_STABLE"),
    "semanticscholar": lambda kind: kind in ("", "OTHER_STABLE", "DOI", "ARXIV"),
}


def _gather_candidates(reference, doi, pmid):
    """Runs every identifier variant through every backend in the registry, keeping every
    non-None hit. Returns (candidates, errors, had_clean_applicable_check); an "error"-flagged
    backend result (e.g. Semantic Scholar's rate_limited marker) goes to errors, never silently
    treated as NOT_FOUND. had_clean_applicable_check is True iff at least one backend that was
    actually applicable to some identifier variant (not skipped for a kind mismatch) completed
    without erroring -- real evidence of "searched, found nothing" rather than "never checked"."""
    candidates = []
    errors = []
    had_clean_applicable_check = False
    for variant in _identifier_variants(reference, doi, pmid):
        for name, _by, fn in FETCH_BACKENDS:
            applies = _BACKEND_APPLIES.get(name, lambda kind: True)(variant["kind"])
            try:
                r = fn(variant)
            except Exception as e:  # noqa: BLE001
                errors.append({"backend": name, "identifier_tried": variant, "error": str(e)[:200]})
                continue
            if r is None:
                if applies:
                    had_clean_applicable_check = True
                continue
            if isinstance(r, dict) and r.get("error"):
                errors.append({"backend": name, "identifier_tried": variant, "error": r["error"]})
                continue
            had_clean_applicable_check = True
            title = (r.get("title") or "").strip()
            candidates.append({
                "backend": name,
                "identifier_tried": variant,
                "metadata": r,
                "title": title,
                "similarity": _similarity(reference, title) if title else 0.0,
            })
    return candidates, errors, had_clean_applicable_check


def _distinct_by_title(ranked):
    """Multiple backends independently finding the SAME work (identical/near-identical
    normalized title) is corroboration, not ambiguity -- keeps only the best-scoring candidate
    per distinct normalized title before the ambiguity check below runs."""
    best_per_title = {}
    for c in ranked:
        key = _norm(c["title"])
        if key not in best_per_title or c["similarity"] > best_per_title[key]["similarity"]:
            best_per_title[key] = c
    return sorted(best_per_title.values(), key=lambda c: c["similarity"], reverse=True)


def _classify(candidates, errors, had_clean_applicable_check):
    if not candidates:
        # CHECK_ERROR only when errors are the reason we have nothing -- i.e. no OTHER, applicable
        # backend ever completed a clean check (found nothing for real vs. was never applicable).
        if errors and not had_clean_applicable_check:
            return "CHECK_ERROR", None
        return "NOT_FOUND", None
    ranked = sorted(candidates, key=lambda c: c["similarity"], reverse=True)
    best = ranked[0]
    distinct = _distinct_by_title(ranked)
    close = [c for c in distinct if c["similarity"] >= 0.6]
    if len(close) >= 2 and (close[0]["similarity"] - close[1]["similarity"]) < AMBIGUOUS_MARGIN:
        return "AMBIGUOUS", best
    if best["similarity"] >= 0.85:
        return "VERIFIED_EXACT", best
    if best["similarity"] >= 0.6:
        return "VERIFIED_FUZZY", best
    return "NOT_FOUND", best


def _claim_match_verdict(reference, claim, best, vendor):
    """Reuses lit_crossvendor_check.py's own packet()/run_vendor() mechanism against a synthetic,
    single-use card -- does not reimplement a parallel prompt or dispatch path."""
    identifier = (best or {}).get("identifier_tried") or {"kind": "", "value": reference}
    meta = (best or {}).get("metadata") or {"source": "no-candidate"}
    card = {
        "id": "adhoc-000",
        "identifier": identifier,
        "notes": reference,
        "scope": "SUPPORTS_GENERAL_CLAIM_ONLY",
        "exact_passage": "",
        "page_or_locator": None,
        "disclosure": DISCLOSURE,
    }
    v = run_vendor(vendor, packet(card, claim, meta, None, ""))
    return {
        "verdict": v,
        "route": f"route:{vendor} ({route_class(vendor)})",
        "claim_match_verified": bool(v.get("claim_match")),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--reference", required=True)
    ap.add_argument("--doi", default=None)
    ap.add_argument("--pmid", default=None)
    ap.add_argument("--claim", default=None)
    ap.add_argument("--vendor", default="claude", choices=["claude", "codex", "gemini"])
    ap.add_argument("--tci-csv", default=None)
    ap.add_argument("--quartile-csv", default=None)
    a = ap.parse_args()

    candidates, errors, had_clean_applicable_check = _gather_candidates(a.reference, a.doi, a.pmid)
    existence_tier, best = _classify(candidates, errors, had_clean_applicable_check)

    winning_meta = (best or {}).get("metadata") or {}
    venue = compute_venue_tier(winning_meta, reference_text=a.reference, tci_csv=a.tci_csv, quartile_csv=a.quartile_csv)

    out = {
        "reference": a.reference,
        "identifiers_tried": _identifier_variants(a.reference, a.doi, a.pmid),
        "existence_tier": existence_tier,
        "best_match": ({
            "backend": best["backend"],
            "title": best["title"],
            "similarity": round(best["similarity"], 4),
            "metadata": best["metadata"],
        } if best else None),
        "all_candidates": [
            {"backend": c["backend"], "title": c["title"], "similarity": round(c["similarity"], 4)}
            for c in sorted(candidates, key=lambda c: c["similarity"], reverse=True)
        ],
        "backend_errors": errors,
        "venue_tier": venue,
        "disclosure": DISCLOSURE,
    }
    if a.claim:
        out["claim"] = a.claim
        out["claim_match"] = _claim_match_verdict(a.reference, a.claim, best, a.vendor)

    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
