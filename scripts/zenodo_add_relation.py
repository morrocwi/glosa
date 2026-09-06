#!/usr/bin/env python3
"""glosa — add ONE related identifier to many already-published Zenodo records (edit → PUT → publish).
Pattern from zenodo_cluster.py cmd_link; generic. Skips records that already carry the relation.
usage: zenodo_add_relation.py --target DOI --relation isPartOf --records ID [ID ...] [--dry-run] --founder-instructed "..." --i-have-founder-approval
Token: env ZENODO_TOKEN (source ~/.config/glosa/secrets.env). 0.4 s between calls. Stops at first HTTP error.
"""
import argparse, sys, time, json
from zenodo_new_version import api
API = 'https://zenodo.org/api'

def main(argv=None):
    p = argparse.ArgumentParser(); p.add_argument('--target', required=True); p.add_argument('--relation', default='isPartOf')
    p.add_argument('--resource-type', default='publication-book'); p.add_argument('--records', nargs='+', required=True)
    p.add_argument('--dry-run', action='store_true'); p.add_argument('--founder-instructed', required=True); p.add_argument('--i-have-founder-approval', action='store_true')
    a = p.parse_args(argv)
    if not a.i_have_founder_approval: print('refusing: no founder approval flag', file=sys.stderr); return 2
    done, skipped = [], []
    for rid in a.records:
        url = f'{API}/deposit/depositions/{rid}'
        d = api('GET', url)
        rel = d['metadata'].get('related_identifiers', [])
        if any(r.get('identifier') == a.target and r.get('relation') == a.relation for r in rel):
            skipped.append(rid); continue
        if a.dry_run:
            done.append(rid); continue
        api('POST', f'{url}/actions/edit')
        d = api('GET', url); md = d['metadata']
        md.setdefault('related_identifiers', []).append({'identifier': a.target, 'relation': a.relation, 'resource_type': a.resource_type, 'scheme': 'doi'})
        for k in ('doi', 'prereserve_doi'): md.pop(k, None)
        api('PUT', url, {'metadata': md}); api('POST', f'{url}/actions/publish')
        done.append(rid); time.sleep(0.4)
    print(json.dumps({'target': a.target, 'relation': a.relation, 'dry_run': a.dry_run, 'updated': done, 'already_linked': skipped}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
