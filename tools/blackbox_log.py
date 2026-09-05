#!/usr/bin/env python3
"""ปูมกล่องดำ — Blackbox Log (glosa). tier: Dr (tool).
A daily, append-only, verbatim log of the founder's voice (ข้อค้นพบ/ความคิด/คำถาม) kept as ONE Zenodo record
(stable concept DOI) that receives a new version each time it is updated. Thai is the source of truth.

usage:
  blackbox_log.py add  "ข้อความ" [--kind question|finding|proposal|ruling|experience] [--tag t1,t2] [--by founder]
  blackbox_log.py add-file path.md   (multi-line entry, verbatim)
  blackbox_log.py render             -> blackbox/log/BLACKBOX_LOG.md + .html + .pdf (via tools/render.py)
  blackbox_log.py deposit [--publish]  -> first time: create record; later: new version (needs ZENODO_TOKEN in env)
  blackbox_log.py check-note path/to/blackbox_note.json  -> question_trace coverage check (below)
Rules: entries are append-only (a correction is a new entry with kind=correction and `corrects:`); one pre-release
history mutation on 2026-09-04 is disclosed in BBL-2026-09-04-082 rather than hidden;
the log holds the founder's own words only; the AI writes no entries (founder ruling 2026-09-04) except a disclosed correction entry, by=ai, on the founder's instruction (BBL-2026-09-04-082).

`check-note` (design/SESSION_ARCH_v0.4_SPEC.md §9.1/§9.4, design/FOUNDATION_v0.7_PATCH.md §4,
schema.blackbox-question-trace, build_now): a MECHANICAL COVERAGE CHECK on a schema/blackbox_note.
schema.json instance -- a different artifact from this file's own Blackbox LOG entries.jsonl above
(the founder's private daily voice log; unrelated). Checks that every `lines[]` entry with
`kind == "question"` has a matching `question_trace[]` entry (`question_trace[].n == lines[].n`),
or that the note explicitly marks the question as a genuinely fresh one via `derived_from_line:
null` on that trace entry -- never silently uncovered. tier: Dr (tool; independently unreviewed).
"""
import os, sys, json, datetime, subprocess, urllib.request, urllib.parse, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT, 'blackbox', 'log')
ENTRIES = os.path.join(LOG_DIR, 'entries.jsonl')
STATE = os.path.join(ROOT, 'registry', 'blackbox_log_zenodo.json')
TITLE_TH = 'ปูมกล่องดำ — บันทึกเสียงดิบ ข้อค้นพบ และคำถามรายวันของ เยาฮารี แหละตี (Blackbox Log, Yaoharee Lahtee)'
CREATOR = {'name': 'Lahtee, Yaoharee', 'orcid': '0009-0005-3861-0626', 'affiliation': 'Open Civil Science Initiative'}
LENS = 'Readout Universe — Yaoharee Lahtee'


def now():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat(timespec='seconds')


CATS = {'epistemology': 'ญาณวิทยา / ผู้รู้กับความรู้', 'ai-society': 'AI กับสังคม / การศึกษา', 'method': 'วิธีวิทยา / ระบบ glosa', 'blackbox': 'กล่องดำ / เสียงดิบ', 'health': 'สุขภาพ / จิตใจ', 'islam': 'อิสลาม / สังคมมุสลิม', 'se': 'วิสาหกิจเพื่อสังคม', 'physics': 'ฟิสิกส์ / สารสนเทศ', 'other': 'อื่นๆ'}


def add(text, kind='finding', tags=None, by='founder', corrects=None, source='chat', category='other', source_note=None):
    os.makedirs(LOG_DIR, exist_ok=True)
    n = 1
    if os.path.exists(ENTRIES):  # max existing sequence + 1 (never reuse an id, even after removals)
        for line in open(ENTRIES, encoding='utf-8'):
            if line.strip():
                n = max(n, int(json.loads(line)['id'].rsplit('-', 1)[1]) + 1)
    e = {'id': f'BBL-{datetime.date.today().isoformat()}-{n:03d}', 'ts': now(), 'by': by, 'kind': kind, 'tags': tags or [],
         'text_verbatim': text, 'corrects': corrects, 'source': source, 'source_note': source_note, 'category': category, 'lens_used': LENS if by == 'founder' else None}
    with open(ENTRIES, 'a', encoding='utf-8') as f:
        f.write(json.dumps(e, ensure_ascii=False) + '\n')
    print(e['id']); return e


def entries():
    return [json.loads(l) for l in open(ENTRIES, encoding='utf-8')] if os.path.exists(ENTRIES) else []


def render():
    es = entries(); os.makedirs(LOG_DIR, exist_ok=True)
    md = [f'# {TITLE_TH}', '',
          '> **นี่คือปูมเสียงดิบ ไม่ใช่บทความ** — ทุกบรรทัดคือคำพูดตามที่พูด (verbatim) ณ วันเวลานั้น ยังไม่ผ่านการปรุง ไม่ผ่านการตรวจอิสระ (tier: positional / Dr) '
          'บันทึกเพิ่มได้อย่างเดียว ไม่แก้ไม่ลบ (แก้ = บรรทัดใหม่ที่อ้างบรรทัดเดิม) เลนส์ที่ใช้มองปัญหา: **Readout Universe — Yaoharee Lahtee** '
          '(10.5281/zenodo.21529456, 10.5281/zenodo.22301318, 10.5281/zenodo.22301202; github.com/morrocwi/readout_universe) '
          'ระบบที่เก็บ: glosa (github.com/morrocwi/glosa) **ปูมนี้มีเฉพาะเสียงของผู้เขียนเท่านั้น** — ไม่มีบรรทัดที่ AI เขียน (คำตัดสินผู้เขียน 2026-09-04: บันทึกระบบที่ AI เคยใส่ไว้ 1 รายการถูกถอดออกและเก็บไว้ที่ blackbox/log/removed_ai_entries.json) ป้าย "เนื้อหาที่สร้างโดย AI" ที่ Facebook ติดให้บางโพสต์เกิดจากรูปประกอบที่ทำด้วย AI ไม่ใช่ตัวข้อความ จึงไม่ถูกนำมาบันทึก',
          '', f'จำนวนบันทึก: {len(es)} · อัปเดตล่าสุด: {es[-1]["ts"] if es else "-"}', '',
          '## สารบัญตามหมวดความคิด (ไม่เรียงตามวันที่)', '']
    for c, cname in CATS.items():
        ce = [e for e in es if e.get('category', 'other') == c]
        if not ce: continue
        md += [f'### {cname} ({len(ce)})', '']
        for e in ce:
            first = e['text_verbatim'].strip().splitlines()[0][:90]
            md += [f"- **{e['id']}** ({e['ts'][:10]}, {e['kind']}{', ' + ', '.join(e['tags']) if e.get('tags') else ''}) — {first}…"]
        md += ['']
    md += ['', '## ลำดับเวลา (ทุกบันทึก ตามที่พูดจริง)', '']
    day = None
    for e in es:
        d = e['ts'][:10]
        if d != day:
            md += ['', f'## {d}', '']; day = d
        tag = (' · ' + ', '.join(e['tags'])) if e.get('tags') else ''
        who = 'ผู้ก่อตั้ง' if e['by'] == 'founder' else f"AI ({e['by']})"
        cat = CATS.get(e.get('category', 'other'), 'อื่นๆ'); src = f" · ที่มา: {e['source']}" + (f" ({e['source_note']})" if e.get('source_note') else '')
        md += [f"**{e['id']}** · {e['ts'][11:16]} · {who} · {e['kind']} · หมวด: {cat}{tag}{src}" + (f" · แก้ {e['corrects']}" if e.get('corrects') else ''), '',
               '\n'.join('> ' + l for l in e['text_verbatim'].splitlines()), '']
    p = os.path.join(LOG_DIR, 'BLACKBOX_LOG.md'); open(p, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    r = os.path.join(ROOT, 'tools', 'render.py')
    for fmt in ('md2html', 'md2pdf'):
        out = p[:-3] + ('.html' if fmt == 'md2html' else '.pdf')
        subprocess.run([sys.executable, r, fmt, p, out], capture_output=True, timeout=300)
    print('rendered', p); return p


def api(method, url, data=None, raw=None, ctype='application/json'):
    tok = os.environ.get('ZENODO_TOKEN')
    if not tok:
        print('ZENODO_TOKEN missing', file=sys.stderr); sys.exit(2)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    rq = urllib.request.Request(url, data=body, method=method, headers={'Authorization': 'Bearer ' + tok, 'Content-Type': ctype})
    try:
        with urllib.request.urlopen(rq, timeout=600) as r:
            return json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        print('HTTP', e.code, e.read()[:400].decode(errors='replace'), file=sys.stderr); sys.exit(1)


def deposit(publish=False):
    p = render(); es = entries(); today = datetime.date.today().isoformat()
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    desc = ('<p><strong>ปูมกล่องดำ (Blackbox Log)</strong> — บันทึกเสียงดิบ ข้อค้นพบ และคำถามรายวันของผู้เขียน ตามที่พูดจริง (verbatim) '
            'ไม่ผ่านการปรุงและไม่ผ่านการตรวจอิสระ (tier: positional/Dr) บันทึกเพิ่มได้อย่างเดียว ไม่แก้ไม่ลบ; อัปเดตเป็นเวอร์ชันใหม่ของ record เดียวกัน '
            'เลนส์ที่ใช้มองปัญหา: Readout Universe — Yaoharee Lahtee. ระบบที่เก็บ: glosa (github.com/morrocwi/glosa). '
            f'เวอร์ชันนี้: {len(es)} บันทึก ถึง {es[-1]["ts"][:10] if es else today}.</p>'
            '<p><em>Blackbox Log</em> — a daily, append-only, verbatim record of the author\'s raw voice (one pre-release correction is disclosed in BBL-2026-09-04-082), findings and questions (Thai is the source of truth). '
            'Not a paper; not reviewed; tier positional/Dr. Contains the author\'s own words only; the single AI-written line is a disclosed correction entry (by=ai, BBL-2026-09-04-082), never the author\'s voice. Each update is a new version of the same record. Lens: Readout Universe — Yaoharee Lahtee; kept by the glosa toolchain.</p>')
    meta = {'metadata': {'title': TITLE_TH, 'upload_type': 'publication', 'publication_type': 'other', 'publication_date': today,
            'creators': [CREATOR], 'description': desc, 'access_right': 'open', 'license': 'cc-by-4.0', 'language': 'tha',
            'version': f'{today} ({len(es)} entries)', 'keywords': ['blackbox log', 'ปูมกล่องดำ', 'research diary', 'raw voice', 'Readout Universe', 'glosa', 'Yaoharee Lahtee'],
            'related_identifiers': [{'identifier': '10.5281/zenodo.21529456', 'relation': 'references', 'resource_type': 'publication-preprint'},
                                    {'identifier': '10.5281/zenodo.22301318', 'relation': 'references', 'resource_type': 'publication-preprint'},
                                    {'identifier': '10.5281/zenodo.22301202', 'relation': 'references', 'resource_type': 'publication-preprint'},
                                    {'identifier': 'https://github.com/morrocwi/glosa', 'relation': 'isSupplementedBy', 'resource_type': 'software'}]}}
    if st.get('deposition_id'):
        nv = api('POST', f"https://zenodo.org/api/deposit/depositions/{st['deposition_id']}/actions/newversion")
        did = int(nv['links']['latest_draft'].rstrip('/').split('/')[-1])
        d = api('GET', f'https://zenodo.org/api/deposit/depositions/{did}')
        for f in d.get('files', []):
            api('DELETE', f"https://zenodo.org/api/deposit/depositions/{did}/files/{f['id']}")
    else:
        d = api('POST', 'https://zenodo.org/api/deposit/depositions', {}); did = d['id']
    bucket = d['links']['bucket']
    api('PUT', f'https://zenodo.org/api/deposit/depositions/{did}', meta)
    for fn in ('BLACKBOX_LOG.md', 'BLACKBOX_LOG.pdf', 'entries.jsonl'):
        fp = os.path.join(LOG_DIR, fn)
        if os.path.exists(fp):
            api('PUT', bucket + '/' + fn, raw=open(fp, 'rb').read(), ctype='application/octet-stream')
    out = {'deposition_id': did, 'status': 'draft', 'entries': len(es), 'date': today}
    if publish:
        pub = api('POST', f'https://zenodo.org/api/deposit/depositions/{did}/actions/publish')
        out.update({'status': 'published', 'doi': pub.get('doi'), 'conceptdoi': pub.get('conceptdoi'), 'url': pub.get('links', {}).get('record_html')})
        st.update({'deposition_id': did, 'conceptdoi': pub.get('conceptdoi'), 'latest_doi': pub.get('doi'), 'versions': st.get('versions', []) + [out]})
    else:
        st.update({'deposition_id': did, 'draft': out})
    os.makedirs(os.path.dirname(STATE), exist_ok=True); json.dump(st, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False))


def question_trace_coverage(note):
    """Coverage check for schema.blackbox-question-trace (build_now): `note` is a parsed
    schema/blackbox_note.schema.json instance (dict). Returns a Result-shaped dict
    {ok, errors, warnings, tier} -- `errors` names every `lines[].kind == "question"` line
    (by `n`) that has no matching `question_trace[]` entry (`question_trace[].n == lines[].n`)
    and whose `derived_from_line` on that entry is not explicitly `null` (a genuinely-fresh
    question is legal, just must be marked, never silently absent). An entirely missing/empty
    `question_trace` on a note with >=1 question-kind line is a full-coverage failure, one error
    per uncovered line -- matching the acceptance test in
    design/SESSION_ARCH_v0.4_SPEC.md §12 (`question_trace_gap` fixture)."""
    if not isinstance(note, dict):
        return {"ok": False, "errors": ["question_trace_coverage: instance is not an object"], "warnings": [], "tier": "Dr"}
    lines = note.get("lines") or []
    question_ns = [l.get("n") for l in lines if isinstance(l, dict) and l.get("kind") == "question"]
    trace = note.get("question_trace") or []
    covered = {t.get("n") for t in trace if isinstance(t, dict)}
    errors = []
    for n in question_ns:
        if n not in covered:
            errors.append(
                f"question_trace_gap: lines[n={n}] is kind=question with no matching "
                f"question_trace[].n == {n} entry (add one, with derived_from_line: null if this "
                "question is genuinely fresh)"
            )
    return {"ok": not errors, "errors": errors, "warnings": [], "tier": "Dr"}


def check_note(path):
    note = json.load(open(path, encoding='utf-8'))
    res = question_trace_coverage(note)
    if res["ok"]:
        print(f"PASS: {path} -- question_trace coverage OK ({len(note.get('question_trace') or [])} entr(y/ies))")
    else:
        print(f"FAIL: {path}")
        for e in res["errors"]:
            print(" -", e)
    return res["ok"]


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'render':
        render()
    elif a[0] == 'add':
        kind = a[a.index('--kind') + 1] if '--kind' in a else 'finding'
        tags = a[a.index('--tag') + 1].split(',') if '--tag' in a else []
        by = a[a.index('--by') + 1] if '--by' in a else 'founder'
        corrects = a[a.index('--corrects') + 1] if '--corrects' in a else None
        cat = a[a.index('--cat') + 1] if '--cat' in a else 'other'
        src = a[a.index('--source') + 1] if '--source' in a else 'chat'
        add(a[1], kind, tags, by, corrects, src, cat)
    elif a[0] == 'add-file':
        cat = a[a.index('--cat') + 1] if '--cat' in a else 'other'
        add(open(a[1], encoding='utf-8').read().strip(), 'finding', [], 'founder', None, 'file', cat)
    elif a[0] == 'deposit':
        deposit('--publish' in a)
    elif a[0] == 'check-note':
        sys.exit(0 if check_note(a[1]) else 1)
