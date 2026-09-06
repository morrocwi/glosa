#!/usr/bin/env python3
"""glosa — publish a NEW VERSION of an existing Zenodo record under its existing concept DOI.

Flow (Zenodo deposit API): newversion → latest_draft → replace files → PUT metadata → publish.
Token: env ZENODO_TOKEN only (source ~/.config/glosa/secrets.env). Never printed. Stops at first HTTP error.

usage:
  zenodo_new_version.py RECORD_ID --file PATH [--file PATH ...] --version LABEL
      [--title T] [--prepend-description FILE] [--description FILE] [--date YYYY-MM-DD]
      [--add-related DOI:RELATION ...] [--keep-old-files] [--dry-run] [--draft]
      --founder-instructed "verbatim instruction"  --i-have-founder-approval

Founder ruling BBL-2026-09-06-158: uplifted papers are new versions under the same concept DOI.
"""
import argparse, json, os, sys, pathlib, datetime, urllib.request, urllib.error

API = 'https://zenodo.org/api'


def api(method, url, data=None, raw=None, ctype='application/json'):
    tok = os.environ.get('ZENODO_TOKEN')
    if not tok:
        print('ZENODO_TOKEN missing (source ~/.config/glosa/secrets.env)', file=sys.stderr); sys.exit(2)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    rq = urllib.request.Request(url, data=body, method=method,
                                headers={'Authorization': 'Bearer ' + tok, 'Content-Type': ctype})
    try:
        with urllib.request.urlopen(rq) as r:
            return json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        print('HTTP', e.code, e.read()[:400].decode(errors='replace'), file=sys.stderr); sys.exit(1)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('record_id')
    p.add_argument('--file', action='append', required=True)
    p.add_argument('--version', required=True)
    p.add_argument('--title')
    p.add_argument('--prepend-description', help='file whose HTML/text is prepended to the existing description')
    p.add_argument('--description', help='file replacing the whole description')
    p.add_argument('--date', default=datetime.date.today().isoformat())
    p.add_argument('--add-related', action='append', default=[], help='DOI:relation, e.g. 10.5281/zenodo.1:isSupplementTo')
    p.add_argument('--keep-old-files', action='store_true')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--draft', action='store_true', help='stop before publish')
    p.add_argument('--founder-instructed', required=True)
    p.add_argument('--i-have-founder-approval', action='store_true')
    a = p.parse_args(argv)
    if not a.i_have_founder_approval:
        print('refusing: --i-have-founder-approval not set', file=sys.stderr); return 2
    for f in a.file:
        if not pathlib.Path(f).is_file():
            print('missing file', f, file=sys.stderr); return 2

    if a.dry_run:
        print(json.dumps({'record': a.record_id, 'files': a.file, 'version': a.version, 'title': a.title,
                          'date': a.date, 'related_add': a.add_related, 'prepend': a.prepend_description,
                          'founder_instructed': a.founder_instructed}, indent=1, ensure_ascii=False))
        return 0

    dep = api('GET', f'{API}/deposit/depositions/{a.record_id}')
    nv = api('POST', f'{API}/deposit/depositions/{a.record_id}/actions/newversion')
    draft_url = nv['links']['latest_draft']
    draft = api('GET', draft_url)
    did = draft['id']
    print('draft', did)
    if not a.keep_old_files:
        for f in draft.get('files', []):
            api('DELETE', f"{draft_url}/files/{f['id']}")
    bucket = draft['links']['bucket']
    for f in a.file:
        name = pathlib.Path(f).name
        api('PUT', f'{bucket}/{name}', raw=pathlib.Path(f).read_bytes(), ctype='application/octet-stream')
        print('uploaded', name)
    md = draft['metadata']
    md['version'] = a.version
    md['publication_date'] = a.date
    if a.title:
        md['title'] = a.title
    if a.description:
        md['description'] = pathlib.Path(a.description).read_text()
    elif a.prepend_description:
        md['description'] = pathlib.Path(a.prepend_description).read_text() + md.get('description', '')
    rel = md.get('related_identifiers', [])
    for item in a.add_related:
        doi, relation = item.rsplit(':', 1)
        if not any(r.get('identifier') == doi and r.get('relation') == relation for r in rel):
            rel.append({'identifier': doi, 'relation': relation, 'resource_type': 'publication-article', 'scheme': 'doi'})
    md['related_identifiers'] = rel
    for k in list(md):
        if k in ('doi', 'prereserve_doi'):
            md.pop(k, None)
    api('PUT', draft_url, data={'metadata': md})
    print('metadata updated')
    if a.draft:
        print('draft left unpublished:', draft_url); return 0
    pub = api('POST', f'{draft_url}/actions/publish')
    print('published', pub.get('doi'), pub.get('links', {}).get('html'))
    reg = pathlib.Path(__file__).resolve().parent.parent / 'registry' / 'zenodo_uploads' / f"{pub['id']}.json"
    reg.write_text(json.dumps({'id': pub['id'], 'doi': pub.get('doi'), 'conceptdoi': pub.get('conceptdoi'),
                               'version': a.version, 'new_version_of': a.record_id, 'files': [pathlib.Path(f).name for f in a.file],
                               'founder_instructed': a.founder_instructed, 'date': a.date}, indent=1, ensure_ascii=False))
    print('registry', reg)
    return 0


if __name__ == '__main__':
    sys.exit(main())
