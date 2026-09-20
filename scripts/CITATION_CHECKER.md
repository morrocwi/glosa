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

## 4. Download signal — `is_oa`/`oa_url`/`pdf_url`, `download_available`/`download_url`,
   `acquisition_status`, and `cite_fetch_source.py`

Read from the real committed code (`lit_crossvendor_check.py` and `cite_check_adhoc.py`), not
guessed. This layer adds "is there a full text we could fetch" on top of the existence/venue
checks above — it never changes `existence_tier`, `claim_match`, or the `disclosure` field.

**Where the raw signal comes from (per-backend metadata, never fabricated):**

- `fetch_openalex(identifier)` now also returns `is_oa` (bool, from OpenAlex's own
  `open_access.is_oa`) and `oa_url` (str or `None`, from `open_access.oa_url`) alongside the
  existing `source`/`title`/`authors`/`year`/`container`/`abstract`/`type` fields.
- `fetch_arxiv(identifier)` now also returns `pdf_url`, always built as
  `f"https://arxiv.org/pdf/{aid}"` for any arXiv id it resolved — arXiv's PDF path is
  deterministic from the id, so this is not fetched separately, just constructed.
- No other backend (`zenodo`, `crossref`, `europepmc`, `url-fetch`, `pubmed`,
  `semanticscholar`) currently returns a download field — a reference resolved only by one of
  those backends will have `download_available: false`.

**What `cite_check_adhoc.py` derives from that, on the winning candidate only:**

- `download_url` — `winning_meta.get("oa_url")` if `is_oa` or `oa_url` is truthy, else
  `winning_meta.get("pdf_url")` if present, else a rescue lookup (below), else `None`. Read
  straight off a backend's own metadata dict; never constructed or guessed.
- **Cross-candidate rescue (adversarial-review finding, 2026-09-20):** the winning candidate is
  picked by title-similarity tie-break across `FETCH_BACKENDS`' order, which can pick a backend
  (e.g. `crossref`) carrying no OA field even when a DIFFERENT backend independently found the
  SAME work (identical normalized title — corroboration, not a different work) with a real
  `oa_url`/`pdf_url`. If the winning candidate itself has no download signal, `cite_check_adhoc.py`
  now scans the other candidates sharing the winner's normalized title and uses the first one that
  does — so a genuinely open-access paper doesn't silently report `download_available: false` just
  because a non-signal-bearing backend happened to win the tie.
- `download_available` — `bool(download_url)`.
- `acquisition_status` — **always the literal string `"not_obtained"`, unconditionally, no matter
  what `download_available` says.** This is deliberate, not a placeholder to fill in later:
  `cite_check_adhoc.py` only ever reads metadata from the fetch backends — it never downloads a
  single byte itself, so "obtained" is a fact about a file existing on disk, which only
  `cite_fetch_source.py` (a separate, explicitly-invoked mechanical fetch, §below) can produce,
  and only a caller that actually ran it and checked its result JSON is in a position to know
  whether that happened. **There is no persistent state tracking across invocations** — running
  `cite_check_adhoc.py` twice on the same reference, even after a file was successfully
  downloaded in between, still prints `acquisition_status: "not_obtained"`, because this script
  has no record of, and does not look for, anything `cite_fetch_source.py` may have done. Never
  read `download_available: true` as "the file exists" or `acquisition_status` as anything other
  than this checker's own honest ignorance of what happened outside it.

**`scripts/cite_fetch_source.py` — the separate, explicit fetch step:**

A standalone script, not a mode of `cite_check_adhoc.py` and not auto-invoked by it. It does no
existence/venue/claim checking at all — a dumb, one-shot HTTP fetch of one `--url` with real
safety rails:

```bash
python3 scripts/cite_fetch_source.py --url <url> --dest <dir> [--filename <name>] [--force]
```

- `--url` (required) — the URL to fetch, typically a `download_url` from a `cite_check_adhoc.py`
  result.
- `--dest` (required) — destination directory; created with `os.makedirs(..., exist_ok=True)` if
  missing.
- `--filename` (optional) — override the saved filename; default is the URL path's basename (or
  literally `"download"` if the path has none).
- `--force` (optional flag) — **required to overwrite an existing file.** Without it, if
  `<dest>/<filename>` already exists, the script fails loud (`refusing to overwrite existing
  file: ... (pass --force to overwrite)`, stderr, exit code 1) and writes nothing — no silent
  overwrite is possible.
- **Content-type mismatch flagging** — if the response `Content-Type` is `text/html`, the script
  still saves the bytes (never silently discards them — a paywall/CAPTCHA/error/withdrawn page is
  often exactly what such a response means, and the caller may want to inspect it) and adds
  `"content_type_mismatch": true` to the result JSON, plus a stderr warning. **This fires for ANY
  `text/html` response, not only when the URL's path ends in `.pdf`** (adversarial-review finding,
  2026-09-20: the original check only looked for a literal `.pdf` suffix, which silently missed
  real PDF-serving URL shapes with no extension — e.g. arXiv's own `https://arxiv.org/pdf/<id>`,
  exactly the shape `fetch_arxiv()`'s `pdf_url` field produces. A `/pdf/`-shaped URL now also
  counts as "looks like a PDF" for the more specific wording in the warning message, but the
  mismatch flag itself no longer depends on that detection at all — `text/html` is simply never an
  acceptable content-type for this tool's purpose). Any other `Content-Type` outside
  `("application/pdf", "application/octet-stream")` prints a plain, separate stderr warning (not
  tagged `content_type_mismatch` — that flag is reserved for the `text/html` case specifically).
- **50MB size cap (`MAX_BYTES = 50 * 1024 * 1024`)** — enforced two ways: (1) if the response's
  `Content-Length` header is present and already exceeds the cap, the fetch aborts immediately
  before writing anything; (2) if `Content-Length` is absent or unreliable, the script streams
  the body in 64KB chunks and aborts mid-download the moment the running byte count exceeds the
  cap, deleting the partial `.partial` file it was writing to. Either way the caller gets a
  stderr message and a non-zero exit, never a silently-truncated file.
- On success it downloads to a `<dest_path>.partial` temp file first, then `os.replace()`s it
  into place atomically, and prints one JSON object to stdout:
  `{"saved_to": ..., "bytes": ..., "content_type": ...}` (plus `"content_type_mismatch": true`
  when that warning fired).

**The two scripts stay deliberately separate.** `cite_check_adhoc.py` is safe to run repeatedly
and read-only (metadata lookups only); `cite_fetch_source.py` is the one script in this pair that
writes to disk, and it only runs when a caller explicitly invokes it with a specific URL and
destination — per the founder's own requirement that a download is offered and confirmed, never
silent or automatic.

## 5. The citation-use gate (`cite_use_gate.py`) — ADMIT / HOLD / REJECT, global

Added 2026-09-20 while evaluating whether to absorb `~/ANSE.ASIA/thai-cite-engine` (a Thai-first
citation prototype whose own concept-validation run came back NO-GO the same day — see its
`docs/HANDOFF_2026-09-20.md`). GLOSA already had every ontology piece a machine-readable
existence/claim gate needs (`existence_tier`, `venue_tier`, `claim_match` from
`cite_check_adhoc.py`; `bearing`/`independence_class` in `evidence_relation.schema.json`) but not
wired together into one runtime verdict. Founder ruling that day: GLOSA is not Thai-scoped, it is
global — so this gate reads only the vendor-neutral fields `cite_check_adhoc.py` already produces
identically for every source worldwide; it does not special-case Thai or any other country.

`cite_use_gate.py` imports `check_reference()` from `cite_check_adhoc.py` (refactored out of that
script's `main()` so this module reuses it by import, exactly the "reused, not duplicated"
convention §1–3 above already follow) and layers two things on top:

- **`verdict`: `ADMIT` / `HOLD` / `REJECT`** — `REJECT` only on a clean `NOT_FOUND`; `HOLD` on
  `AMBIGUOUS`/`CHECK_ERROR`, on a verified source whose `claim_match_verified` is false or absent
  (glosa's `SourceExistence != ClaimSupport` non-collapse rule — a real source that doesn't back
  the stated claim is never silently admitted), and on a bare existence match with no `--claim`
  given (unless the caller passes `--existence-only-ok`, since ADMIT with no claim checked would
  overstate what was actually verified). Any future `existence_tier` value this module doesn't yet
  recognize fails closed to `HOLD`, never to a silent `ADMIT`.
- **`coverage_readout`** (`existence`, `claim_match` axes) — `SEARCHED_OK` / `UNAVAILABLE` /
  `NOT_ATTEMPTED`, describing search completeness separately from what was found, per
  `LOCAL_EVIDENCE_NOT_FOUND != NO_LOCAL_EVIDENCE_EXISTS`: a rate-limited backend that leaves
  `NOT_FOUND` unconfirmed reads `UNAVAILABLE`, not the same as a clean `NOT_FOUND` with
  `SEARCHED_OK`.

Like `cite_check_adhoc.py`, every result carries a mandatory `disclosure` — this is a mechanical
gate only, not an independent check or release approval; a real `citation_card.yaml` plus a
`glosa-independent-check` review is still required before `status: VERIFIED`.

```bash
python3 scripts/cite_use_gate.py --reference "<text>" [--doi <doi>] [--pmid <pmid>] \
  [--claim "<sentence>"] [--existence-only-ok] [--vendor claude|codex|gemini] \
  [--tci-csv <path>] [--quartile-csv <path>]
```

Real smoke test (2026-09-20): a fabricated reference → `REJECT` (`NOT_FOUND`, with
`coverage_readout.existence: UNAVAILABLE` because a backend was rate-limited mid-search — the
honest read, not conflated with a clean not-found); "Attention Is All You Need" by real DOI, no
`--claim` → `HOLD` (`EXISTENCE_ONLY`, correctly refusing to overstate an unchecked claim); same
call with `--existence-only-ok` → `ADMIT`.
