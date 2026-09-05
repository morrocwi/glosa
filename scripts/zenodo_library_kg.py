#!/usr/bin/env python3
"""glosa — knowledge graph of the Zenodo library "When AI Expands Human Potential" (hub 22308201).

Builds, from LIVE Zenodo metadata only (no invented relations), a graph that another AI can read:
  docs/library/aihp_kg.json        nodes + edges, JSON-LD-flavoured (@context, @id = DOI URL)
  docs/library/aihp_kg_edges.jsonl one edge per line: {source, relation, target, declared_on}
  docs/library/AIHP_LIBRARY_KG.md  reading guide for AIs/humans: what the library is, node table,
                                   lineage chains, how to traverse, what NOT to infer
  docs/library/aihp_kg.svg         layered render (rows = year-month, no external dependency)

Every edge comes from a record's own related_identifiers (Zenodo metadata the author wrote), plus
version edges (isVersionOf) from Zenodo's concept ids. Readout, not truth: the graph is a diagram of
the metadata as fetched on the build date; it is not a claim about which paper is "better".
tier: Dr (tool). usage: zenodo_library_kg.py [--hub 22308201] [--out docs/library]
"""
import argparse
import datetime
import json
import re
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

API = "https://zenodo.org/api/records"
DOI_RE = re.compile(r"10\.5281/zenodo\.(\d+)")


def get(url, tries=4):
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(url, timeout=60))
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(2 + 2 * i)


def rec_node(d):
    m = d["metadata"]
    rid = d["id"]
    return {
        "@id": f"https://doi.org/{d.get('doi') or m.get('doi')}",
        "zenodo_id": rid,
        "concept_doi": (d.get("conceptdoi") or m.get("relations", {}) and d.get("conceptdoi")) or None,
        "conceptrecid": d.get("conceptrecid"),
        "title": m.get("title", ""),
        "date": m.get("publication_date"),
        "version": m.get("version"),
        "resource_type": (m.get("resource_type") or {}).get("title"),
        "language": m.get("language"),
        "keywords": m.get("keywords", []),
        "creators": [c.get("name") for c in m.get("creators", [])],
        "url": f"https://zenodo.org/records/{rid}",
        "related": m.get("related_identifiers", []),
        "abstract_head": re.sub(r"<[^>]+>", " ", m.get("description", ""))[:400].strip(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub", default="22308201")
    ap.add_argument("--out", default="docs/library")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()

    hub = get(f"{API}/{a.hub}")
    hub_node = rec_node(hub)
    members = [DOI_RE.search(x["identifier"]).group(1) for x in hub_node["related"] if x.get("relation") == "hasPart" and DOI_RE.search(x["identifier"])]
    nodes = {str(hub["id"]): dict(hub_node, role="hub")}
    for rid in members:
        nodes[rid] = dict(rec_node(get(f"{API}/{rid}")), role="member")
        time.sleep(0.4)
    # one hop out: records our members point at that are not members (still ours, or external)
    edges = []
    referenced = set()
    for rid, n in list(nodes.items()):
        for x in n["related"]:
            mt = DOI_RE.search(x.get("identifier", ""))
            tgt = mt.group(1) if mt else x.get("identifier")
            edges.append({"source": rid, "relation": x.get("relation"), "target": tgt, "declared_on": rid, "scheme": x.get("scheme", "doi")})
            if mt and tgt not in nodes:
                referenced.add(tgt)
    for rid in sorted(referenced):
        try:
            d = get(f"{API}/{rid}")
            nodes[rid] = dict(rec_node(d), role="referenced_not_member")
        except Exception as e:  # noqa: BLE001
            nodes[rid] = {"@id": f"https://doi.org/10.5281/zenodo.{rid}", "zenodo_id": int(rid), "title": "(unresolved on build date)", "role": "unresolved", "error": str(e)[:80], "related": []}
        time.sleep(0.4)
    # version edges: same concept id ⇒ isVersionOf (derived from Zenodo concept ids, not authored)
    by_concept = defaultdict(list)
    for rid, n in nodes.items():
        if n.get("conceptrecid"):
            by_concept[n["conceptrecid"]].append(rid)
    for c, ids in by_concept.items():
        if len(ids) > 1:
            latest = max(ids, key=lambda r: nodes[r].get("date") or "")
            for r in ids:
                if r != latest:
                    edges.append({"source": r, "relation": "isVersionOf(derived)", "target": latest, "declared_on": "zenodo-concept-id", "scheme": "concept"})

    # lineage chains from authored continues/isContinuedBy edges
    latest_of = {e["source"]: e["target"] for e in edges if e["relation"].startswith("isVersionOf")}
    L_ = lambda r: latest_of.get(r, r)  # collapse versions so a chain is stated once, on latest ids
    cont = defaultdict(set)
    for e in edges:
        if e["relation"] == "continues":
            cont[L_(e["source"])].add(L_(e["target"]))
        elif e["relation"] == "isContinuedBy":
            cont[L_(e["target"])].add(L_(e["source"]))
    chains = []
    roots = [r for r in nodes if r not in cont and any(r in v for v in cont.values())]
    for root in roots:
        chain = [root]
        seen = {root}
        cur = root
        while True:
            nxt = [s for s, ts in cont.items() if cur in ts and s not in seen]
            if not nxt:
                break
            cur = sorted(nxt, key=lambda r: nodes.get(r, {}).get("date") or "")[0]
            chain.append(cur)
            seen.add(cur)
        chains.append(chain)

    graph = {
        "@context": {"@vocab": "http://schema.org/", "doi": "https://doi.org/", "relation": "http://purl.org/dc/terms/relation"},
        "@type": "Dataset",
        "name": "Knowledge graph of the Zenodo library 'When AI Expands Human Potential' (Yaoharee Lahtee, 2025–2026)",
        "built_on": today,
        "hub": f"https://doi.org/10.5281/zenodo.{a.hub}",
        "readout_note": "Nodes and edges are copied from Zenodo metadata on the build date. Edges marked (derived) come from Zenodo concept ids, all others were authored in the records' related_identifiers. This is a readout of the metadata, not a ranking or a validation of any paper.",
        "node_count": len(nodes), "edge_count": len(edges),
        "nodes": [dict(v, zenodo_id=int(k)) if str(k).isdigit() else v for k, v in nodes.items()],
        "edges": edges,
        "lineage_chains": [[nodes[r]["@id"] for r in ch] for ch in chains],
    }
    (out / "aihp_kg.json").write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
    with (out / "aihp_kg_edges.jsonl").open("w", encoding="utf-8") as f:
        for e in edges:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    # ---- guide (markdown) ----
    def T(rid):
        return nodes[rid]["title"] if rid in nodes else rid
    mem = sorted([r for r, n in nodes.items() if n["role"] == "member"], key=lambda r: nodes[r].get("date") or "", reverse=True)
    rel_counts = defaultdict(int)
    for e in edges:
        rel_counts[e["relation"]] += 1
    L = []
    L.append(f"# Knowledge graph — Zenodo library \"When AI Expands Human Potential\"\n")
    L.append(f"Hub record: https://doi.org/10.5281/zenodo.{a.hub} · built {today} from live Zenodo metadata · {len(mem)} member records, {len(nodes)} nodes, {len(edges)} edges.\n")
    L.append("**How to read this (for an AI).** Every node is one Zenodo record (a DOI). Every edge is a relation the author wrote into that record's `related_identifiers` on Zenodo, except edges labelled `(derived)`, which come from Zenodo's own concept ids (two records of the same concept = versions of one work). Nothing here was inferred from paper content. Treat the graph as a readout of the metadata on the build date, not as truth about the papers, and do not read edge counts as importance. To cite a work, use its DOI URL (`@id`); to cite the latest version of a work, follow the `isVersionOf(derived)` edge to its target. Machine files: `aihp_kg.json` (nodes+edges, JSON-LD flavoured), `aihp_kg_edges.jsonl` (one edge per line).\n")
    L.append("**สำหรับผู้อ่านไทย.** กราฟนี้คือแผนที่ห้องสมุด Zenodo ของ เยาฮารี แหละตี เรื่องมนุษย์–AI: จุด = record หนึ่งชิ้น (DOI), เส้น = ความสัมพันธ์ที่ผู้เขียนใส่ไว้ใน metadata ของ Zenodo เอง (ต่อจาก / อ้างถึง / เป็นส่วนหนึ่งของ) ไม่ได้เดาจากเนื้อหา อ่านเป็น readout ไม่ใช่ความจริงสุดท้าย\n")
    L.append("## Relation vocabulary\n")
    L.append("| relation | meaning | count |\n|---|---|---|")
    meaning = {"hasPart": "hub → member (library membership)", "isPartOf": "member → hub or programme index", "continues": "this work continues the target (reading order: target first)", "isContinuedBy": "inverse of continues", "references": "this work cites the target", "isReferencedBy": "inverse of references", "isSupplementTo": "note/annex attached to the target", "isSupplementedBy": "inverse", "isVersionOf(derived)": "older version → latest version of the same concept (from Zenodo concept id)"}
    for r, c in sorted(rel_counts.items(), key=lambda x: -x[1]):
        L.append(f"| `{r}` | {meaning.get(r, '')} | {c} |")
    L.append("\n## Lineage chains (authored `continues` edges, oldest → newest)\n")
    if chains:
        for ch in chains:
            L.append("- " + " → ".join(f"[{T(r)[:60]}]({nodes[r]['@id']})" for r in ch))
    else:
        L.append("- (none declared)")
    L.append("\n## Member records (newest first)\n")
    L.append("| date | title | DOI | version-of | out-edges |\n|---|---|---|---|---|")
    for r in mem:
        n = nodes[r]
        vo = [e["target"] for e in edges if e["source"] == r and e["relation"].startswith("isVersionOf")]
        outs = [e for e in edges if e["source"] == r and e["relation"] not in ("isPartOf",)]
        L.append(f"| {n.get('date')} | {n['title'][:90]} | [{n['@id'].split('/')[-1]}]({n['@id']}) | {('→ '+vo[0]) if vo else 'latest'} | {len(outs)} |")
    other = [r for r, n in nodes.items() if n["role"] not in ("member", "hub")]
    if other:
        L.append("\n## Referenced records outside the hub (one hop)\n")
        for r in sorted(other, key=lambda r: nodes[r].get("date") or ""):
            L.append(f"- {nodes[r].get('date')} · {T(r)[:90]} · {nodes[r]['@id']} · role={nodes[r]['role']}")
    L.append("\n## Traversal recipes\n")
    L.append("1. **Start from the hub** and follow `hasPart` to enumerate the library.\n2. **Reading order for a thread:** pick a member, follow `continues` backwards until no edge remains; read from that root forward.\n3. **Latest version only:** drop any node that has an outgoing `isVersionOf(derived)` edge.\n4. **Evidence base of a paper:** its `references` targets; for the methodology behind a paper look for the `glosa` software record and the `Blackbox Log` record among them.\n5. **Do not infer** authority, quality, or priority from degree; the author's own status line inside each record (K0, not peer reviewed, tiers) is the claim ceiling.\n")
    L.append("\n## Mermaid (lineage + hub, latest versions only)\n")
    L.append("```mermaid\nflowchart TB")
    short = {r: re.sub(r"[^A-Za-z0-9]", "", "n" + r) for r in nodes}
    drop = {e["source"] for e in edges if e["relation"].startswith("isVersionOf")}
    shown = set()
    for r in [a.hub] + mem:
        if r in drop:
            continue
        L.append(f'  {short[r]}["{nodes[r]["title"][:48].replace(chr(34), "")}…<br/>{r}"]')
        shown.add(r)
    for e in edges:
        if e["relation"] in ("continues", "isSupplementTo") and e["source"] in shown and e["target"] in shown:
            L.append(f"  {short[e['source']]} -->|{e['relation']}| {short[e['target']]}")
    for e in edges:
        if e["relation"] == "hasPart" and e["target"] in shown:
            L.append(f"  {short[e['source']]} -.-> {short[e['target']]}")
    L.append("```\n")
    L.append(f"\n_Built by `scripts/zenodo_library_kg.py` (glosa, CC BY 4.0) on {today}. Author of all records: Yaoharee Lahtee._\n")
    (out / "AIHP_LIBRARY_KG.md").write_text("\n".join(L), encoding="utf-8")

    # ---- SVG (rows by month, latest versions only, no dependencies) ----
    show = [r for r in mem if r not in drop]
    months = sorted({(nodes[r].get("date") or "")[:7] for r in show}, reverse=True)
    W, rowh, colw, boxw, boxh = 1600, 96, 300, 270, 56
    per_row = defaultdict(list)
    for r in show:
        per_row[(nodes[r].get("date") or "")[:7]].append(r)
    pos = {}
    y = 120
    maxcols = 1
    for mth in months:
        rs = per_row[mth]
        maxcols = max(maxcols, len(rs))
        rows_needed = (len(rs) + 4) // 5
        for i, r in enumerate(rs):
            pos[r] = (40 + (i % 5) * colw, y + (i // 5) * rowh)
        y += rows_needed * rowh
    H = y + 60
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="Noto Sans, Noto Sans Thai, Arial, sans-serif" font-size="11">',
         f'<rect width="{W}" height="{H}" fill="#fbfaf7"/>',
         f'<text x="40" y="40" font-size="20" font-weight="bold">When AI Expands Human Potential — Zenodo library graph (hub 10.5281/zenodo.{a.hub})</text>',
         f'<text x="40" y="62" fill="#555">rows = publication month (newest top) · latest versions only · solid arrow = continues · dashed = isSupplementTo · thin grey = references · built {today} from Zenodo metadata (readout, not truth)</text>']
    def esc(t):
        return t.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    # edges first
    for e in edges:
        if e["source"] in pos and e["target"] in pos and e["relation"] in ("continues", "isSupplementTo", "references"):
            x1, y1 = pos[e["source"]]; x2, y2 = pos[e["target"]]
            x1 += boxw / 2; x2 += boxw / 2; y1 += boxh / 2; y2 += boxh / 2
            col = {"continues": "#b03a2e", "isSupplementTo": "#1f618d", "references": "#bbb"}[e["relation"]]
            wdt = {"continues": 2.2, "isSupplementTo": 1.8, "references": 0.8}[e["relation"]]
            dash = ' stroke-dasharray="6,4"' if e["relation"] == "isSupplementTo" else ""
            s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{wdt}"{dash} opacity="0.85"/>')
    ycur = None
    for r in show:
        x, yy = pos[r]
        mth = (nodes[r].get("date") or "")[:7]
        if mth != ycur:
            s.append(f'<text x="8" y="{yy + 14}" font-size="10" fill="#888" transform="rotate(-90 8,{yy + 14})">{mth}</text>')
            ycur = mth
        t = nodes[r]["title"]
        s.append(f'<a href="{nodes[r]["@id"]}"><rect x="{x}" y="{yy}" width="{boxw}" height="{boxh}" rx="6" fill="#fff" stroke="#333"/>')
        s.append(f'<text x="{x + 8}" y="{yy + 18}" font-weight="bold">{esc(t[:44])}</text>')
        s.append(f'<text x="{x + 8}" y="{yy + 33}">{esc(t[44:90])}</text>')
        s.append(f'<text x="{x + 8}" y="{yy + 48}" fill="#1f618d">10.5281/zenodo.{r} · {nodes[r].get("date")}</text></a>')
    s.append("</svg>")
    (out / "aihp_kg.svg").write_text("\n".join(s), encoding="utf-8")
    print(f"built: {len(mem)} members, {len(nodes)} nodes, {len(edges)} edges, {len(chains)} lineage chains -> {out}/")


if __name__ == "__main__":
    main()
