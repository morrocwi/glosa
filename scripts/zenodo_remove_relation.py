#!/usr/bin/env python3
"""glosa — remove ONE related identifier relation from already-published Zenodo records (edit → PUT → publish).
Pattern from zenodo_add_relation.py, inverted: removes only the exact (identifier, relation) pair —
every other related identifier on the record is kept byte-identical. Refuses to touch a record that
is not the latest version of its concept unless --allow-old-version is passed (checked against the
public /api/records/<id> -> links.latest, no token needed for that check).
usage: zenodo_remove_relation.py --target DOI --relation isPartOf --records ID [ID ...] [--dry-run]
       [--allow-old-version] --founder-instructed "..." --i-have-founder-approval
Token: env ZENODO_TOKEN (source ~/.config/glosa/secrets.env). 0.4 s between calls. Stops at first HTTP error.
"""
import argparse, sys, time, json, urllib.request
from zenodo_new_version import api
API = 'https://zenodo.org/api'


def compute_removal(related_identifiers, target, relation):
    """Pure function. Given the record's current related_identifiers list plus a target identifier
    and relation, return (kept, removed): `kept` is every entry that does NOT exactly match
    (identifier, relation) — preserved byte-identical, in original order; `removed` is the entries
    that do match. No entry is ever mutated, only filtered."""
    kept, removed = [], []
    for entry in related_identifiers:
        if entry.get('identifier') == target and entry.get('relation') == relation:
            removed.append(entry)
        else:
            kept.append(entry)
    return kept, removed


def is_latest_version(rid):
    """True if record id `rid` is the latest version of its concept, False if not, None if unknown
    (network/parse failure — caller should treat that as 'cannot confirm', not as 'is latest').
    Uses the PUBLIC records API only, no token."""
    try:
        with urllib.request.urlopen(f'{API}/records/{rid}') as r:
            d = json.load(r)
    except Exception as e:  # noqa: BLE001
        print('WARN could not fetch record', rid, 'for latest-version check:', str(e)[:120], file=sys.stderr)
        return None
    latest = (d.get('links') or {}).get('latest')
    if not latest:
        return True  # unversioned record (or no version chain reported) -> nothing "later" to defer to
    try:
        with urllib.request.urlopen(latest) as r2:
            d2 = json.load(r2)
        return str(d2.get('id')) == str(d.get('id'))
    except Exception as e:  # noqa: BLE001
        print('WARN could not resolve latest link for', rid, ':', str(e)[:120], file=sys.stderr)
        return None


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--target', required=True)
    p.add_argument('--relation', default='isPartOf')
    p.add_argument('--records', nargs='+', required=True)
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--allow-old-version', action='store_true')
    p.add_argument('--founder-instructed', required=True)
    p.add_argument('--i-have-founder-approval', action='store_true')
    a = p.parse_args(argv)
    if not a.i_have_founder_approval:
        print('refusing: no founder approval flag', file=sys.stderr); return 2

    done, skipped, refused = [], [], []
    for rid in a.records:
        latest = is_latest_version(rid)
        if latest is False and not a.allow_old_version:
            print(f'refusing: record {rid} is not the latest version of its concept '
                  f'(pass --allow-old-version to override)', file=sys.stderr)
            refused.append(rid); continue
        if latest is None:
            print(f'refusing: could not confirm record {rid} is the latest version of its concept '
                  f'(pass --allow-old-version to override)', file=sys.stderr)
            refused.append(rid); continue

        url = f'{API}/deposit/depositions/{rid}'
        d = api('GET', url)
        rel = d['metadata'].get('related_identifiers', [])
        kept, removed = compute_removal(rel, a.target, a.relation)
        if not removed:
            print(f'{rid}: no ({a.target}, {a.relation}) relation found — nothing to remove')
            skipped.append(rid); continue

        print(f'--- record {rid} related_identifiers diff ---')
        print('before:'); print(json.dumps(rel, indent=1, ensure_ascii=False))
        print('after:'); print(json.dumps(kept, indent=1, ensure_ascii=False))

        if a.dry_run:
            done.append(rid); continue

        api('POST', f'{url}/actions/edit')
        d = api('GET', url); md = d['metadata']
        rel2 = md.get('related_identifiers', [])
        kept2, removed2 = compute_removal(rel2, a.target, a.relation)
        md['related_identifiers'] = kept2
        for k in ('doi', 'prereserve_doi'): md.pop(k, None)
        api('PUT', url, {'metadata': md}); api('POST', f'{url}/actions/publish')
        done.append(rid); time.sleep(0.4)

    print(json.dumps({'target': a.target, 'relation': a.relation, 'dry_run': a.dry_run,
                       'updated': done, 'no_relation_found': skipped, 'refused_not_latest_version': refused}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
