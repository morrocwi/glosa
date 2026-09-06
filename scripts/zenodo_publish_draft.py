#!/usr/bin/env python3
"""glosa — finish an EXISTING unpublished Zenodo draft: replace its files, refresh metadata from the spec, publish.
usage: zenodo_publish_draft.py <deposition_id> spec.json --file <pdf> [--dry-run] --founder-instructed "<verbatim>" --i-have-founder-approval
MUST-11 gate as in zenodo_publish_file.py (publish is irreversible). Logs to registry/zenodo_uploads/<id>.json.
"""
import argparse, json, os, sys, pathlib, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from zenodo_publish_file import api, build_metadata, founder_approval_gate, log_founder_instruction
REG = pathlib.Path(__file__).resolve().parent.parent / 'registry' / 'zenodo_uploads'

def main():
    p = argparse.ArgumentParser(); p.add_argument('deposition_id'); p.add_argument('spec'); p.add_argument('--file', action='append', required=True)
    p.add_argument('--dry-run', action='store_true'); p.add_argument('--founder-instructed', required=True); p.add_argument('--i-have-founder-approval', action='store_true')
    a = p.parse_args(); spec = json.load(open(a.spec)); md = build_metadata(spec)
    if a.dry_run:
        print(json.dumps({'deposition': a.deposition_id, 'files': a.file, 'metadata': md}, ensure_ascii=False, indent=1)[:3000]); return
    founder_approval_gate(a)
    dep = api('GET', f'https://zenodo.org/api/deposit/depositions/{a.deposition_id}')
    if dep.get('submitted'): sys.exit('refused: deposition already published')
    for f in dep.get('files', []):
        api('DELETE', f['links']['self']); print('deleted', f.get('filename'))
    bucket = dep['links']['bucket']
    for fp in a.file:
        fn = os.path.basename(fp); api('PUT', bucket + '/' + urllib.parse.quote(fn), raw=open(fp, 'rb').read(), ctype='application/octet-stream'); print('uploaded', fn)
    api('PUT', f'https://zenodo.org/api/deposit/depositions/{a.deposition_id}', {'metadata': md}); print('metadata updated')
    pub = api('POST', f'https://zenodo.org/api/deposit/depositions/{a.deposition_id}/actions/publish')
    print('published', pub.get('doi'), pub.get('links', {}).get('record_html'))
    REG.mkdir(parents=True, exist_ok=True); (REG / f"{a.deposition_id}.json").write_text(json.dumps(pub, ensure_ascii=False, indent=1))
    log_founder_instruction(a.deposition_id, a.founder_instructed, {'files': a.file, 'mode': 'publish_existing_draft'})

if __name__ == '__main__': main()
