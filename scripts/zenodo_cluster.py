#!/usr/bin/env python3
"""glosa — organize an author's Zenodo records into programme clusters (hub-and-spoke).
tier: Dr (specified; executed once 2026-09-04 for the founder's account)

Subcommands
  fetch   -> registry/zenodo_all_records.json   (public API, no token)
  tag     -> apply keyword rules + manual overrides; write clusters per record (no token)
  hubs    -> create one published "programme index" record per cluster that lacks one (token)
  link    -> for every member record: edit metadata, add isPartOf hub(s) + references anchors, republish (token)
  report  -> print membership table

Token: read ONLY from env ZENODO_TOKEN (source ~/.config/glosa/secrets.env). Never printed, never argv.
Stops at the first HTTP error (no retry loops). State file: registry/zenodo_clusters.json (append-only outcomes).
"""
import datetime
import os, sys, json, re, html, time, tempfile, subprocess, urllib.request, urllib.parse

REG = 'registry'
RECS = f'{REG}/zenodo_all_records.json'
STATE = f'{REG}/zenodo_clusters.json'
AUTHOR = 'Lahtee, Yaoharee'
CREATOR = {'name': AUTHOR, 'orcid': '0009-0005-3861-0626', 'affiliation': 'Open Civil Science Initiative'}

# primary (exclusive) cluster rules — a record gets exactly one of ep/he/ph/other by score
PRIMARY = {
 'ep': r'epistem|knowledge|knower|readout|truth|interpret|authority|gettier|faqr|scholar|legitim|translation|informationism|constraint-first|alethic|mediated agency|qualia|civilization of knowledge|generative abundance|standalone|category stabilization|logic|philosoph|zero readout|declaration bound|retained|language bridge',
 'he': r'health|phobia|plaque|clinical|medic|repair capacity|autonomic|aging|cellular|wellbeing|endurance|training|blood|lymph|disease|diabetes|dysregulation|psych|mind|phenomenal|life architecture|sana|family',
 'ph': r'physic|gravit|quantum|cosmolog|black.hole|lagrangian|field theory|spectral|eigen|telegraph|relativity|mass|hodge|dirac|z pole|electroweak|gauge|white dwarf|ringdown|tully|kibble|planck|inertia|banded|sturm|pixel|prft|causal memory|causal physics|expansion|diffusiv|energy|wavelength|frequency|dissipat|operational compactness|informational (pixel|field|diffusivity)|equation of everything|eoe|cosmo',
}
# secondary (multi-label) tags — a record may carry several
TAGS = {
 'ai': r'\bai\b|artificial intelligence|\bllm|language model|lora\b|generative|ai-native|ai-mediated|ai-coached|machine learning|chatbot|ปัญญาประดิษฐ',
 'islam': r'islam|muslim|halal|hilal|nikah|faqr|ash.ar|imam|shar[iī]|mosque|qur|ummah|มุสลิม|อิสลาม',
 'tourism': r'touris|travel|hospitality|service systems|ท่องเที่ยว',
 'aihp': r'(?!x)x',  # curated series: membership by OVERRIDE_TAGS_ADD only (founder BBL-2026-09-04-111)
 'jps': r'(?!x)x',  # curated series: society, justice, peace, violence — membership by OVERRIDE_TAGS_ADD only (founder chat 2026-09-05)
 'se': r'social enterprise|social-enterprise|entrepreneur|enterprise survival|mission drift|social business|วิสาหกิจ',
}
# manual overrides by Zenodo record id (founder/chair readout 2026-09-04)
OVERRIDE_PRIMARY = {
 'ep': [22302410, 18918275, 18176092, 18968098, 20537309, 18085092, 19183837],
 'he': [18174493, 22255211, 22302161, 22302173, 22302190],
 'ph': [17942505, 17344093, 17335909, 17334604, 17475434, 17475130, 17473885, 17464990, 17393189],
 'other': [22301882, 17305576, 17305534, 20159825, 18444260, 18897585, 18925131, 22099526, 22227005, 18383439],
}
OVERRIDE_TAGS_REMOVE = {'tourism': [17899050, 17600798], 'ai': [17439693, 17393189, 17378613, 17341231, 18897585, 18213737], 'islam': [17280895]}
OVERRIDE_TAGS_ADD = {
 'jps': [22357788, 22345709, 18925131, 18383439, 18444260, 18897585, 22129490, 20159825, 22099526, 19425809, 18943971, 19115417, 17280895],
 'aihp': [22357788, 22357744, 22345709, 22341671, 22341297, 22339909, 19215748, 17280546, 22318040, 22319715, 22308446,22308448,22308451, 19640361, 19205869, 22163849, 22307843, 22307841, 22307148, 22307561, 22307564, 22308072, 22308066, 22301202, 22301318, 21425420, 18711408, 18517054, 18925129, 18943971, 19176260, 22302410, 22301886, 22307891, 21529456],'se': [17281646, 22301882], 'islam': [17281646], 'ai': [22357788, 22357744, 22345709, 22341671, 22341297, 22339909, 22301882, 22302410], 'ep': []}
HUBS = {
 'ep': dict(title='Readout Universe — Epistemology programme index (Yaoharee Lahtee, 2026)', th='ญาณวิทยา / ทฤษฎีความรู้', anchors=['10.5281/zenodo.21529456', '10.5281/zenodo.22301202', '10.5281/zenodo.22301318']),
 'he': dict(title='Readout Universe — Health & mind programme index (Yaoharee Lahtee, 2026)', th='สุขภาพ / จิตใจ', anchors=['10.5281/zenodo.20229203', '10.5281/zenodo.18813886']),
 'ph': dict(title='Readout Universe — Physics & information programme index (Yaoharee Lahtee, 2026)', th='ฟิสิกส์ / สารสนเทศ', anchors=['10.5281/zenodo.21203637', '10.5281/zenodo.21529456']),
 'ai': dict(title='Readout Universe — Artificial intelligence & knowledge programme index (Yaoharee Lahtee, 2026)', th='ปัญญาประดิษฐ์กับความรู้', anchors=['10.5281/zenodo.22301202', '10.5281/zenodo.22163849', '10.5281/zenodo.19215748']),
 'islam': dict(title='Readout Universe — Islam, Muslim society & knowledge authority programme index (Yaoharee Lahtee, 2026)', th='อิสลาม / สังคมมุสลิม / อำนาจความรู้', anchors=['10.5281/zenodo.22206607', '10.5281/zenodo.22129490', '10.5281/zenodo.18943971']),
 'tourism': dict(title='Readout Universe — Muslim-friendly tourism & service programme index (Yaoharee Lahtee, 2026)', th='ท่องเที่ยว / บริการ', anchors=['10.5281/zenodo.19059720', '10.5281/zenodo.18258377']),
 'aihp': dict(title='When AI Expands Human Potential — series index: human–AI epistemic fusion, standalone scholarship, and the Readout hypothesis-generation programme (Yaoharee Lahtee, 2025–2026)', th='เมื่อ AI ขยายศักยภาพมนุษย์ — ซีรีส์งานที่ทำให้มนุษย์กับ AI ผลิตความรู้ร่วมกันได้ (ฟิวชันทางญาณวิทยา): Standalone Scholar, glosa, Bounded Knower I–IV + State of Evidence, Written by AI Still True, Readout Condition, Human LoRA และงานที่เกี่ยวข้อง', anchors=['10.5281/zenodo.19215748', '10.5281/zenodo.22163849', '10.5281/zenodo.22307843']),
 'jps': dict(title='Society, Justice, Peace & Violence — series index: structured coexistence, causal ethics, conflict and repair, authority and minority politics (Yaoharee Lahtee, 2025–2026)', th='สังคม / ความยุติธรรม / สันติภาพ / ความรุนแรง — ไวยากรณ์เชิงเหตุของการอยู่ร่วมกัน จริยศาสตร์เชิงเหตุ ความขัดแย้งและการซ่อมแซม อำนาจความรู้และการเมืองของชนกลุ่มน้อย', anchors=['10.5281/zenodo.18925131', '10.5281/zenodo.18383439', '10.5281/zenodo.18444260']),
 'se': dict(title='Readout Universe — Social enterprise programme index (Yaoharee Lahtee, 2026)', th='วิสาหกิจเพื่อสังคม', anchors=['10.5281/zenodo.22227005', '10.5281/zenodo.18506938']),
}
TODAY = datetime.date.today().isoformat()
SCRATCH = os.environ.get('GLOSA_SCRATCH', tempfile.gettempdir())


class ApiError(Exception):
    pass


def api(method, url, data=None, raw=None, ctype='application/json', soft=False):
    tok = os.environ.get('ZENODO_TOKEN')
    if not tok:
        print('ZENODO_TOKEN not in environment — source ~/.config/glosa/secrets.env first', file=sys.stderr); sys.exit(2)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    rq = urllib.request.Request(url, data=body, method=method, headers={'Authorization': 'Bearer ' + tok, 'Content-Type': ctype})
    try:
        with urllib.request.urlopen(rq) as resp:
            return json.loads(resp.read() or b'{}')
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode(errors='replace'); print('HTTP', e.code, url[-70:], msg, file=sys.stderr)
        if soft: raise ApiError(f'{e.code} {msg}')
        sys.exit(1)


def load(p, default):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else default


def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def cmd_fetch():
    recs = []
    q = urllib.parse.quote(f'creators.name:"{AUTHOR}"')
    for p in range(1, 12):
        d = json.load(urllib.request.urlopen(f'https://zenodo.org/api/records?q={q}&size=25&page={p}&sort=mostrecent'))
        hs = d.get('hits', {}).get('hits', [])
        if not hs:
            break
        for h in hs:
            m = h['metadata']
            desc = html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', m.get('description', ''))))
            recs.append(dict(id=h['id'], doi=h['doi'], concept=h.get('conceptdoi'), title=m['title'], date=m.get('publication_date'),
                             type=m.get('resource_type', {}).get('title'), kw=[k.lower() for k in m.get('keywords', [])], desc=desc[:1500]))
    save(RECS, recs); print('fetched', len(recs))


def cmd_tag():
    recs = load(RECS, None)
    if recs is None:
        cmd_fetch(); recs = load(RECS, [])
    hub_titles = {h['title'] for h in HUBS.values()}
    for r in recs:
        t = (r['title'] + ' ' + ' '.join(r['kw'])).lower(); d = r['desc'].lower()
        s = {k: len(re.findall(rx, t)) * 3 + len(re.findall(rx, d)) for k, rx in PRIMARY.items()}
        best = max(s, key=s.get); r['cluster'] = best if s[best] > 0 else 'other'
        for c, ids in OVERRIDE_PRIMARY.items():
            if r['id'] in ids: r['cluster'] = c
        head = (r['title'] + ' ' + ' '.join(r['kw']) + ' ' + r['desc'][:700]).lower()
        r['tags'] = [k for k, rx in TAGS.items() if re.search(rx, head)]
        r['tags'] = [t for t in r['tags'] if r['id'] not in OVERRIDE_TAGS_REMOVE.get(t, [])]
        for t, ids in OVERRIDE_TAGS_ADD.items():
            if r['id'] in ids and t not in r['tags']: r['tags'].append(t)
        if r['title'] in hub_titles or 'programme index' in r['title'].lower():
            r['cluster'] = 'hub'; r['tags'] = []
    save(RECS, recs); cmd_report()


def _resolve_latest(rid):
    # a record id absent from the creator search (index lag after a republish, or an old version id)
    # is resolved through /api/records/<id> -> links.latest so the hub never silently drops a member
    try:
        d = json.load(urllib.request.urlopen(f'https://zenodo.org/api/records/{rid}'))
        latest = (d.get('links') or {}).get('latest')
        if latest:  # /api/records/<id>/versions/latest -> the concept's current version
            d2 = json.load(urllib.request.urlopen(latest))
            if d2.get('id') and d2['id'] != d['id']: d = d2
        m = d.get('metadata') or {}
        return {'id': d['id'], 'doi': d.get('doi') or m.get('doi'), 'title': m.get('title', ''), 'date': m.get('publication_date', ''), 'tags': [], 'cluster': None}
    except Exception as e:  # noqa: BLE001
        print('WARN unresolved override id', rid, str(e)[:80]); return None


def members_of(recs, c):
    if c in PRIMARY:
        ms = [r for r in recs if r.get('cluster') == c]
    else:
        ms = [r for r in recs if c in r.get('tags', [])]
        have = {r['id'] for r in recs}
        for rid in OVERRIDE_TAGS_ADD.get(c, []):
            if rid not in have:
                x = _resolve_latest(rid)
                if x: ms.append(x); have.add(x['id']); time.sleep(0.3)
    seen = set(); out = []
    for r in ms:
        if r['doi'] not in seen: seen.add(r['doi']); out.append(r)
    return sorted(out, key=lambda r: r['date'] or '', reverse=True)


def cmd_report():
    recs = load(RECS, [])
    for c in list(PRIMARY) + ['other'] + list(TAGS):
        ms = members_of(recs, c) if c != 'other' else [r for r in recs if r.get('cluster') == 'other']
        print(f'===== {c} ({len(ms)})')
        for r in ms: print(' ', r['doi'].split('.')[-1], r['title'][:85])


def cmd_hubs():
    recs = load(RECS, []); state = load(STATE, {})
    for c, hub in HUBS.items():
        ms = members_of(recs, c)
        if not ms: print(c, 'no members'); continue
        if state.get(c, {}).get('hub_doi'): print(c, 'hub exists', state[c]['hub_doi']); continue
        items = ''.join(f"<li>{html.escape(r['title'])} ({r['date']}) — <a href='https://doi.org/{r['doi']}'>{r['doi']}</a></li>" for r in ms)
        desc = (f"<p><strong>Programme index — {hub['th']}.</strong> A navigation aid listing {len(ms)} works by the author in this programme area (a work may appear in several programme indexes). Inclusion is a readout of the author's own classification (assisted by the glosa toolchain, github.com/morrocwi/glosa), not an evaluation; each record keeps its own status and disclaimers. Anchor works: " + ', '.join(hub['anchors']) + f".</p><ol>{items}</ol>")
        hf = os.path.join(SCRATCH, f'{c}_index.html')
        open(hf, 'w', encoding='utf-8').write(f"<html><meta charset='utf-8'><body style='font-family:Noto Serif Thai,serif'><h1>{html.escape(hub['title'])}</h1>{desc}<p>Generated {TODAY} by glosa.</p></body></html>")
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', SCRATCH, hf], capture_output=True, timeout=180)
        pdf = hf[:-5] + '.pdf'
        meta = {'metadata': {'title': hub['title'], 'upload_type': 'publication', 'publication_type': 'other', 'publication_date': TODAY,
                'creators': [CREATOR], 'description': desc, 'access_right': 'open', 'license': 'cc-by-4.0', 'language': 'eng', 'version': TODAY,
                'keywords': ['programme index', 'Readout Universe', 'Yaoharee Lahtee', hub['th']],
                'related_identifiers': [{'identifier': r['doi'], 'relation': 'hasPart', 'resource_type': 'publication'} for r in ms]}}
        dep = api('POST', 'https://zenodo.org/api/deposit/depositions', {}); did = dep['id']; bucket = dep['links']['bucket']
        api('PUT', f'https://zenodo.org/api/deposit/depositions/{did}', meta)
        if os.path.exists(pdf):
            api('PUT', bucket + f'/{c}_programme_index_{TODAY}.pdf', raw=open(pdf, 'rb').read(), ctype='application/octet-stream')
        api('PUT', bucket + f'/{c}_programme_index_{TODAY}.json', raw=json.dumps([{k: r[k] for k in ('doi', 'title', 'date')} for r in ms], ensure_ascii=False, indent=1).encode(), ctype='application/octet-stream')
        pub = api('POST', f'https://zenodo.org/api/deposit/depositions/{did}/actions/publish')
        state[c] = {'hub_doi': pub['doi'], 'hub_id': did, 'members': [r['doi'] for r in ms], 'anchors': hub['anchors'], 'linked': {}}
        save(STATE, state); print(c, 'HUB published', pub['doi'], 'members', len(ms)); time.sleep(0.5)


def cmd_hubs_refresh():
    recs = load(RECS, []); state = load(STATE, {})
    for c, st in state.items():
        ms = members_of(recs, c); dois = [r['doi'] for r in ms]
        hid = st['hub_id']
        api('POST', f'https://zenodo.org/api/deposit/depositions/{hid}/actions/edit')
        d = api('GET', f'https://zenodo.org/api/deposit/depositions/{hid}'); m = d['metadata']
        rel = [x for x in m.get('related_identifiers', []) if x.get('relation') != 'hasPart']
        rel += [{'identifier': x, 'relation': 'hasPart', 'resource_type': 'publication'} for x in dois]
        m['related_identifiers'] = rel
        for k in ('doi', 'prereserve_doi'): m.pop(k, None)
        api('PUT', f'https://zenodo.org/api/deposit/depositions/{hid}', {'metadata': m})
        api('POST', f'https://zenodo.org/api/deposit/depositions/{hid}/actions/publish')
        st['members'] = dois; save(STATE, state); print('hub refreshed', c, len(dois)); time.sleep(0.4)


def cmd_link():
    recs = load(RECS, []); state = load(STATE, {})
    # per record: which hubs (primary + tags) and which anchors
    plan = {}
    for r in recs:
        if r.get('cluster') == 'hub': continue
        cs = ([r['cluster']] if r.get('cluster') in PRIMARY else []) + [t for t in r.get('tags', []) if t in state]
        cs = [c for c in cs if c in state and state[c].get('hub_doi')]
        if cs: plan[r['id']] = (r, cs)
    done = 0
    for rid, (r, cs) in plan.items():
        already = all(str(rid) in state[c].get('linked', {}) for c in cs)
        if already: continue
        try:
            api('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/edit', soft=True)
            d = api('GET', f'https://zenodo.org/api/deposit/depositions/{rid}', soft=True); m = d['metadata']
        except ApiError as e:
            for c in cs: state[c].setdefault('failed', {})[str(rid)] = str(e)[:120]
            save(STATE, state); print('SKIP', rid, str(e)[:80]); continue
        rel = m.get('related_identifiers', []); have = {x.get('identifier') for x in rel}
        for c in cs:
            hd = state[c]['hub_doi']
            if hd not in have: rel.append({'identifier': hd, 'relation': 'isPartOf', 'resource_type': 'publication-other'}); have.add(hd)
            for a in state[c]['anchors']:
                if a != r['doi'] and a not in have: rel.append({'identifier': a, 'relation': 'references', 'resource_type': 'publication-preprint'}); have.add(a)
        m['related_identifiers'] = rel
        for k in ('doi', 'prereserve_doi'): m.pop(k, None)
        try:
            api('PUT', f'https://zenodo.org/api/deposit/depositions/{rid}', {'metadata': m}, soft=True)
            api('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/publish', soft=True)
        except ApiError as e:
            api('POST', f'https://zenodo.org/api/deposit/depositions/{rid}/actions/discard', soft=True)
            for c in cs: state[c].setdefault('failed', {})[str(rid)] = str(e)[:120]
            save(STATE, state); print('SKIP', rid, str(e)[:80]); continue
        for c in cs: state[c].setdefault('linked', {})[str(rid)] = 'ok'
        save(STATE, state); done += 1; print('linked', rid, r['title'][:60], '->', cs); time.sleep(0.4)
    print('records linked this run:', done, '| planned:', len(plan))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'report'
    {'fetch': cmd_fetch, 'tag': cmd_tag, 'hubs': cmd_hubs, 'hubs-refresh': cmd_hubs_refresh, 'link': cmd_link, 'report': cmd_report}[cmd]()
