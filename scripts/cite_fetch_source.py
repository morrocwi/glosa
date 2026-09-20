#!/usr/bin/env python3
"""glosa -- mechanical fetch utility for a citation's download URL.

SEPARATE from cite_check_adhoc.py on purpose: that script only ever reads metadata from the
fetch backends (it never downloads a byte), so "did we actually obtain the file" stays a fact
this script alone produces, and only when a caller explicitly runs it. This script does no
existence/venue/claim checking at all -- it is a dumb, explicit, one-shot HTTP fetch with real
safety rails:

  - Never silently overwrites an existing file at --dest/--filename -- fails loud (stderr + exit
    1) unless --force is passed.
  - Checks the response Content-Type against what the URL implies is expected (a PDF-looking URL
    that comes back text/html is very often a paywall/CAPTCHA/error page). On a mismatch this is
    only a warning tagged into the result JSON as "content_type_mismatch": true -- the bytes are
    still saved, never silently discarded, so the caller can inspect why it looked wrong.
  - Enforces a 50MB max size: aborts immediately if Content-Length exceeds it, or streams with a
    running byte counter and aborts mid-download (deleting the partial file) if actual bytes
    exceed it when Content-Length is absent/unreliable.
  - On success prints a single JSON object: {"saved_to": ..., "bytes": ..., "content_type": ...}.

usage:
  cite_fetch_source.py --url <url> --dest <dir> [--filename <name>] [--force]
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

MAX_BYTES = 50 * 1024 * 1024  # 50MB
CHUNK = 64 * 1024

# Content-Types considered "a real document" for the fallback check. text/html deliberately
# excluded (adversarial-review finding, 2026-09-20): this tool exists to fetch a paper's actual
# source file, and a text/html response is almost always a paywall/CAPTCHA/withdrawn/error page,
# never a legitimate target -- it must always warn, never pass silently.
ACCEPTABLE_CONTENT_TYPES = ("application/pdf", "application/octet-stream")


def _default_filename(url):
    path = urllib.parse.urlparse(url).path
    name = os.path.basename(path) or "download"
    return name


def _looks_like_pdf_url(url):
    """A URL shape that implies the target is a PDF -- checked BEFORE fetching, used only to
    label a text/html response as an expected-PDF mismatch (see fetch()). Covers both the
    literal '.pdf' suffix and the '/pdf/' path segment several real sources use with no
    extension (e.g. arXiv's own https://arxiv.org/pdf/<id> -- adversarial-review finding,
    2026-09-20: the original suffix-only check silently missed exactly this real shape)."""
    path = urllib.parse.urlparse(url).path.lower()
    return path.endswith(".pdf") or "/pdf/" in path


def _fail(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def fetch(url, dest_dir, filename=None, force=False):
    filename = filename or _default_filename(url)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, filename)

    if os.path.exists(dest_path) and not force:
        _fail(
            f"refusing to overwrite existing file: {dest_path} (pass --force to overwrite)"
        )

    req = urllib.request.Request(url, headers={"User-Agent": "glosa-cite-fetch/1.0"})
    try:
        resp = urllib.request.urlopen(req, timeout=60)
    except Exception as e:  # noqa: BLE001
        _fail(f"fetch failed: {e}")

    content_type = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
    content_length_hdr = resp.headers.get("Content-Length")
    content_length = int(content_length_hdr) if content_length_hdr and content_length_hdr.isdigit() else None

    if content_length is not None and content_length > MAX_BYTES:
        resp.close()
        _fail(
            f"aborting: Content-Length {content_length} bytes exceeds max {MAX_BYTES} bytes"
        )

    # Flag ANY text/html response as a mismatch, not only when the URL also looks PDF-shaped
    # (adversarial-review finding, 2026-09-20): a URL like arxiv.org/pdf/<id> has no ".pdf"
    # suffix, so the old suffix-only _looks_like_pdf_url() check silently missed exactly this
    # real shape -- text/html is essentially never the real target of this tool regardless of
    # URL shape, so it always warns now, and still additionally names the "looks like a PDF URL"
    # case explicitly when that's also true (the more specific, more actionable message).
    content_type_mismatch = content_type.startswith("text/html")

    tmp_path = dest_path + ".partial"
    total = 0
    try:
        with open(tmp_path, "wb") as f:
            while True:
                chunk = resp.read(CHUNK)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BYTES:
                    f.close()
                    os.remove(tmp_path)
                    _fail(
                        f"aborting mid-download: exceeded max {MAX_BYTES} bytes "
                        f"(no reliable Content-Length was given)"
                    )
                f.write(chunk)
    finally:
        resp.close()

    if force and os.path.exists(dest_path):
        os.remove(dest_path)
    os.replace(tmp_path, dest_path)

    if content_type_mismatch:
        pdf_shaped = _looks_like_pdf_url(url)
        print(
            (f"warning: URL looks like a PDF ({url}) but " if pdf_shaped else f"warning: ")
            + f"Content-Type was {content_type!r} -- this often means a paywall/CAPTCHA/"
            f"error/withdrawn page was saved instead of the real document; file was still "
            f"saved for inspection at {dest_path}",
            file=sys.stderr,
        )
    elif not content_type or not any(content_type.startswith(ct) for ct in ACCEPTABLE_CONTENT_TYPES):
        print(
            f"warning: unexpected Content-Type {content_type!r} for {url}",
            file=sys.stderr,
        )

    result = {"saved_to": dest_path, "bytes": total, "content_type": content_type}
    if content_type_mismatch:
        result["content_type_mismatch"] = True
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--url", required=True)
    ap.add_argument("--dest", required=True, help="destination directory")
    ap.add_argument("--filename", default=None, help="override the filename (default: basename of URL path)")
    ap.add_argument("--force", action="store_true", help="allow overwriting an existing file at the destination")
    a = ap.parse_args()

    result = fetch(a.url, a.dest, a.filename, a.force)
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
