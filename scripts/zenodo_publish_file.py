#!/usr/bin/env python3
"""glosa — publish ONE file as a Zenodo record from a small JSON spec. tier: Dr (tool); each run is logged.
usage: zenodo_publish_file.py spec.json [--draft] [--dry-run]
       [--i-have-founder-approval | --founder-instructed "<verbatim instruction + date>"]
spec: {"file": path, "title": str, "upload_type": "publication|presentation|dataset|software|other",
       "publication_type": "preprint|other|workingpaper|report|..." (only for publication),
       "publication_date": "YYYY-MM-DD", "description_html": str, "keywords": [..], "language": "eng|tha",
       "version": str, "related": [{"identifier": doi_or_url, "relation": "references|isPartOf|isSupplementTo|..."}],
       "access_right": "open|restricted|embargoed" (default open), "license": "cc-by-4.0"}
Token: env ZENODO_TOKEN only (source ~/.config/glosa/secrets.env). Never printed. Stops at first HTTP error.
Duplicate guard: searches Zenodo for the author + title phrase first; refuses if a hit has the same title.

MUST-11 founder-approval gate: an actual publish (no --draft, no --dry-run) is an irreversible,
externally-visible action -- POST a deposition then actions/publish -- so it is refused unless
EITHER (1) --i-have-founder-approval is passed AND registry/RELEASE_APPROVAL.txt exists and
contains the word APPROVED, OR (2) --founder-instructed "<verbatim instruction + date>" is passed
(a same-session explicit chat instruction that bypasses the file check but is LOGGED into
registry/zenodo_uploads/<deposition_id>.json so the bypass is auditable, never silent). --draft
and --dry-run never publish, so they are exempt from the gate. --dry-run additionally makes NO
network call at all: it prints the metadata it would send and exits 0.
"""
import argparse
import datetime
import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

CREATOR = {'name': 'Lahtee, Yaoharee', 'orcid': '0009-0005-3861-0626', 'affiliation': 'Open Civil Science Initiative'}

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_APPROVAL_PATH = REPO_ROOT / "registry" / "RELEASE_APPROVAL.txt"
ZENODO_UPLOADS_DIR = REPO_ROOT / "registry" / "zenodo_uploads"


def api(method, url, data=None, raw=None, ctype='application/json'):
    tok = os.environ.get('ZENODO_TOKEN')
    if not tok:
        print('ZENODO_TOKEN missing (source ~/.config/glosa/secrets.env)', file=sys.stderr); sys.exit(2)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    rq = urllib.request.Request(url, data=body, method=method, headers={'Authorization': 'Bearer ' + tok, 'Content-Type': ctype})
    try:
        with urllib.request.urlopen(rq) as r:
            return json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        print('HTTP', e.code, e.read()[:400].decode(errors='replace'), file=sys.stderr); sys.exit(1)


def founder_approval_gate(args):
    """MUST-11: hard-refuse an actual publish unless founder-approved via one of two auditable
    routes. Mirrors scripts/zenodo_deposit.py's cmd_publish gate exactly (same class of action:
    POST a deposition, then actions/publish). Never makes a network call itself."""
    if args.founder_instructed:
        if len(args.founder_instructed.strip()) < 15:
            print(
                'zenodo_publish_file: refused — --founder-instructed must be the verbatim '
                'founder instruction plus a date, not a short placeholder', file=sys.stderr,
            )
            sys.exit(1)
        print(f'zenodo_publish_file: proceeding under --founder-instructed (will be logged): {args.founder_instructed}')
        return
    if not args.i_have_founder_approval:
        print('zenodo_publish_file: refused — publish requires --i-have-founder-approval '
              '(or --founder-instructed "<verbatim instruction + date>")', file=sys.stderr)
        sys.exit(1)
    if not RELEASE_APPROVAL_PATH.exists():
        print(f'zenodo_publish_file: refused — {RELEASE_APPROVAL_PATH} does not exist', file=sys.stderr)
        sys.exit(1)
    text = RELEASE_APPROVAL_PATH.read_text()
    if 'APPROVED' not in text:
        print(f'zenodo_publish_file: refused — {RELEASE_APPROVAL_PATH} does not contain APPROVED', file=sys.stderr)
        sys.exit(1)


def log_founder_instruction(deposition_id, instruction, extra=None):
    """Log a --founder-instructed bypass into registry/zenodo_uploads/<id>.json so it is
    auditable, never silent. Mirrors scripts/zenodo_deposit.py's log_founder_instruction."""
    ZENODO_UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = ZENODO_UPLOADS_DIR / f'{deposition_id}.json'
    record = {}
    if out_path.exists():
        try:
            record = json.loads(out_path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            record = {}
    record['deposition_id'] = deposition_id
    record['founder_instructed_bypass'] = {
        'instruction': instruction,
        'logged_at': datetime.datetime.now().isoformat(timespec='seconds'),
    }
    if extra:
        record.update(extra)
    out_path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'logged --founder-instructed bypass to {out_path}')


def build_metadata(spec):
    md = {'title': spec['title'], 'upload_type': spec['upload_type'], 'publication_date': spec['publication_date'],
          'creators': [CREATOR], 'description': spec['description_html'], 'access_right': spec.get('access_right', 'open'),
          'license': spec.get('license', 'cc-by-4.0'), 'keywords': spec.get('keywords', []), 'language': spec.get('language', 'eng'),
          'version': spec.get('version', '1.0')}
    if spec['upload_type'] == 'publication':
        md['publication_type'] = spec.get('publication_type', 'preprint')
    if spec.get('related'):
        md['related_identifiers'] = [dict(identifier=r['identifier'], relation=r['relation'], resource_type=r.get('resource_type', 'publication')) for r in spec['related']]
    return md


def parse_args(argv):
    p = argparse.ArgumentParser(description='glosa — publish ONE file as a Zenodo record from a JSON spec')
    p.add_argument('spec', help='path to the spec JSON file')
    p.add_argument('--draft', action='store_true', help='create the deposition and upload files but do not publish')
    p.add_argument('--dry-run', action='store_true', help='print the metadata that would be sent and exit 0 -- no network call at all')
    p.add_argument('--i-have-founder-approval', action='store_true')
    p.add_argument(
        '--founder-instructed', metavar='"<verbatim instruction + date>"',
        help='bypass the RELEASE_APPROVAL.txt file check for an explicit same-session founder '
             'chat instruction; the instruction is logged to registry/zenodo_uploads/<id>.json',
    )
    return p.parse_args(argv)


def main():
    args = parse_args(sys.argv[1:])
    spec = json.load(open(args.spec, encoding='utf-8'))
    md = build_metadata(spec)

    if args.dry_run:
        # No network call anywhere in this branch (task instruction: "no network calls in
        # tests" -- --dry-run is the mechanism that makes MUST-11's drift test runnable offline).
        print(json.dumps({'dry_run': True, 'metadata': md, 'files': spec.get('files') or [spec['file']]}, ensure_ascii=False, indent=1))
        return

    publishing = not args.draft
    if publishing:
        founder_approval_gate(args)

    q = urllib.parse.quote('creators.name:"Lahtee, Yaoharee" AND title:"%s"' % spec['title'][:60].replace('"', ''))
    hits = json.load(urllib.request.urlopen(f'https://zenodo.org/api/records?q={q}&size=3'))['hits']
    for h in hits['hits']:
        if h['metadata']['title'].strip().lower() == spec['title'].strip().lower():
            print('DUPLICATE — already on Zenodo:', h['doi']); sys.exit(3)
    dep = api('POST', 'https://zenodo.org/api/deposit/depositions', {}); did = dep['id']; bucket = dep['links']['bucket']
    api('PUT', f'https://zenodo.org/api/deposit/depositions/{did}', {'metadata': md})
    for fp in spec.get('files') or [spec['file']]:
        fn = os.path.basename(fp)
        api('PUT', bucket + '/' + urllib.parse.quote(fn), raw=open(fp, 'rb').read(), ctype='application/octet-stream')
    if args.draft:
        print(json.dumps({'deposition_id': did, 'status': 'draft'})); return
    if args.founder_instructed:
        log_founder_instruction(did, args.founder_instructed)
    pub = api('POST', f'https://zenodo.org/api/deposit/depositions/{did}/actions/publish')
    out = {'deposition_id': did, 'doi': pub.get('doi'), 'conceptdoi': pub.get('conceptdoi'), 'url': pub.get('links', {}).get('record_html'), 'title': spec['title']}
    print(json.dumps(out, ensure_ascii=False))
    os.makedirs('registry/zenodo_uploads', exist_ok=True)
    out_path = f'registry/zenodo_uploads/{did}.json'
    existing = {}
    if os.path.exists(out_path):
        try:
            existing = json.load(open(out_path, encoding='utf-8'))
        except (OSError, ValueError):
            existing = {}
    existing.update(out)
    json.dump(existing, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
