# Citation checker — backends, venue tiers, ad-hoc mode

Companion doc for `scripts/lit_crossvendor_check.py`, `scripts/lit_venue_tier.py`,
`scripts/lit_sources_thai.py`, and `scripts/cite_check_adhoc.py`. This is a *reference for the
mechanical checking layer*, not a restatement of the full pipeline design — for the manifest/
`litreview_manifest.yaml`/gate machinery these scripts feed, see
`design/S14_literature-review-system.md` and `templates/knowledge/lit_review_gate_checklist.md`.

No new equation or theorem is registered by any of this — pure lookup/classification/dispatch
code, so `EPIS-TOLEDO-FIRST` / `EPIS-REUSE-PIPELINE` do not apply to it (each module's own header
comment says so).

## 1. The backend registry (`FETCH_BACKENDS` in `lit_crossvendor_check.py`)

`fetch_meta(identifier)` no longer hand-rolls an if/elif chain. It walks an ordered list of
`(name, metadata_verified_by, fn)` tuples and returns the first backend whose `fn(identifier)`
does not return `None`:

```python
FETCH_BACKENDS = [
    ("zenodo", "mechanical:zenodo", fetch_zenodo),
    ("crossref", "mechanical:crossref", fetch_crossref),
    ("europepmc", "mechanical:europepmc", fetch_europepmc),
    ("arxiv", "mechanical:arxiv", fetch_arxiv),
    ("url-fetch", "mechanical:url-fetch", fetch_urlpage),
    ("openalex", "mechanical:openalex", fetch_openalex),
    ("pubmed", "mechanical:pubmed", fetch_pubmed),
    ("semanticscholar", "mechanical:semanticscholar", fetch_semanticscholar),
]
```

**To add a future source: append one `fetch_<name>(identifier)` function and one tuple to this
list — do not edit the dispatch loop itself.** The convention every existing backend follows:

- Take the card's `identifier` dict (`{"kind": ..., "value": ...}`) and return `None` immediately
  if this backend's `kind` gate does not match (so the next backend in the list gets a turn).
- Return a plain `dict` with at least `source`, `title`, `authors`, `year` on a hit; `abstract`
  when the API exposes one (truncated — see each function for its own cap, 1500–2500 chars).
- On a genuine transient failure that is *not* "no match" (e.g. a rate limit), return a
  distinguishable `{"error": "...", "source": "..."}` marker rather than `None` — `None` means
  "not applicable / no match, try the next backend"; an `error` dict means "this backend was
  applicable and something went wrong," which callers (`cite_check_adhoc.py`) keep separate from
  a real `NOT_FOUND`. `fetch_semanticscholar` is the worked example (HTTP 429 → one retry → sleep
  → `{"error": "rate_limited", ...}`).
- Never raise past `fetch_meta`'s own `try/except` — an uncaught exception there already degrades
  to `{"source": "fetch-failed", "error": str(e)[:200]}`, but a backend that raises for an
  *expected* condition (e.g. no results) should return `None`, not throw.

`cite_check_adhoc.py` imports this same registry (`from lit_crossvendor_check import
FETCH_BACKENDS, ...`) rather than duplicating it, and additionally keeps a small
`_BACKEND_APPLIES` map so it can tell "this backend ran and confirmed nothing" from "this backend
was not applicable to this identifier kind at all" — update that map too when a new backend's
`kind` gate does not match the existing pattern.

## 2. The two-track venue-tier system (`lit_venue_tier.py`) — real, honest ceiling

`compute_venue_tier(metadata, reference_text="", tci_csv=None, quartile_csv=None)` classifies a
fetched-metadata dict per `design/S14_literature-review-system.md` §5.7:
`venue_quality_index` is **metadata only** — it never gates `claim_match_verified` or a card's
`status`. It can return zero, one, or more than one tier hit (a Thai-authored preprint can
legitimately carry both `PREPRINT` and a `TCI_TIER_n`/`NOT_IN_TCI` reading at once).

Read plainly, this is the real ceiling as of 2026-09-20, not an aspiration:

- **`PREPRINT`** — the only track that is genuinely live/automatic. It reads OpenAlex's own
  `type` field when present, or matches a known preprint-repo name (`arxiv`, `biorxiv`, `medrxiv`,
  `ssrn`, `psyarxiv`) against the container/source string. No manual file needed.
- **`Q1`..`Q4` (Scimago/SJR quartile)** — **requires a manually-supplied `--quartile-csv`.**
  `scimagojr.com` returns HTTP 403 to programmatic fetches (confirmed by a real `curl` before this
  code was written); there is no live scrape path. The CSV must match a Scimago "All journals"
  export shape (`Issn`, `SJR Best Quartile` columns, `;`-delimited as Scimago's own export uses,
  though a plain `,`-delimited file with the same column names also works). Without that file,
  every source falls through to `UNRANKED_NO_QUARTILE_SOURCE` — this is the honest default, never
  a fabricated tier.
- **`TCI_TIER_1`/`_2`/`_3` / `NOT_IN_TCI`** — also **CSV-backed, not live**, for the same reason:
  `tci-thailand.org/journal_list` was curl'd on 2026-09-20 and confirmed to be a bare
  create-react-app SPA shell (862 bytes, all content loaded client-side by
  `/static/js/main.*.js`) with no server-rendered table to scrape and no discovered API endpoint
  in the bundled JS. `lit_sources_thai.tci_tier_lookup()` takes an optional `--tci-csv` (schema:
  `journal_name`, `issn`, `tier` — see that module's own docstring) and returns
  `NOT_CHECKED_NO_TCI_SOURCE` when none is given, or `LOOKUP_FAILED` for a missing/malformed file
  — never a guessed tier.
- **`UNRANKED_NO_QUARTILE_SOURCE`** — the fallback when nothing above resolved. This is expected
  to be the common case until real CSVs are supplied; it is not an error state.

**ThaiJO coverage, read from the real committed code, not assumed:** `lit_sources_thai.fetch_thaijo()`
has two real paths — (a) a direct `tci-thaijo.org` URL/DOI already in the reference text (parses
the `citation_*` meta tags ThaiJO's OJS software emits, verified live against a real article,
`match_confidence: DIRECT_IDENTIFIER`), and (b) a best-effort DuckDuckGo `site:tci-thaijo.org`
search fallback (`match_confidence: THAIJO_BEST_EFFORT`, never conflated with a confirmed match).
The module's own docstring records an honest caveat found while testing it on 2026-09-20: the
DuckDuckGo HTML endpoint degraded to a result-less "lite" response after only a couple of
automated requests from the same source in a short window — it is a bundled last-resort, not a
reliable always-on API. An empty search result must not be read as "no ThaiJO source exists."
When an AI-agent caller already has its own web-search tool, pass its results in via
`fetch_thaijo`'s `web_search_fn` argument instead of relying on the DuckDuckGo default.

## 3. The ad-hoc mode (`cite_check_adhoc.py`) — explicit, mandatory disclosure

`cite_check_adhoc.py` is a **separate script**, not a mode flag on `lit_crossvendor_check.py`
(which already owns a slug/hyp/manifest-tree CLI contract this does not disturb). It exists for
"check 8 references in one paper" or a one-off spot check with no
`records/lit/<slug>/<hyp>/` tree.

Every JSON object it prints carries a mandatory, never-omitted `disclosure` field:

```python
DISCLOSURE = (
    "LIGHTWEIGHT_ADHOC_CHECK -- not a full citation_card.yaml, no §5.4 human spot-check "
    "sampling applied; do not treat this as status: VERIFIED"
)
```

Concretely: it tries every backend in `FETCH_BACKENDS` across every identifier shape it was
given, scores each hit's title against `--reference` with `difflib.SequenceMatcher`, and
classifies `existence_tier` (`VERIFIED_EXACT` ≥0.85 similarity, `VERIFIED_FUZZY` 0.6–0.85,
`AMBIGUOUS` when two distinct works score within 0.05 of each other, `NOT_FOUND`, or
`CHECK_ERROR` when a backend errored and no other backend completed a clean applicable check). It
then runs `compute_venue_tier` on the winning candidate, and — only if `--claim` was given —
reuses `lit_crossvendor_check.py`'s own `packet()`/`run_vendor()` cross-vendor dispatch (not
reimplemented) for a `claim_match` verdict.

This is deliberately **lighter than the full L5/manifest standard**: no `§5.4` spot-check
sampling, no `dialogue_table.md` row, no `acquisition_status`/`exact_passage`/`page_or_locator`
recorded against a real card. Treat its `existence_tier` and `claim_match` as a fast triage
signal, never as a substitute for `status: VERIFIED` on a real `citation_card.yaml`.

Real test evidence (from the commit that added this file): run for real against a well-known
real reference by DOI (→ `VERIFIED_EXACT`, `venue_tier: PREPRINT`), an obviously fabricated
reference (→ `NOT_FOUND`), and the two literal Thai placeholder reference lines in
`thai_doc/org-templates/AICK/examples/example_paper.data.yaml` (→ both `NOT_FOUND`, confirming no
false positive on template filler text).
