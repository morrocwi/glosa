#!/usr/bin/env python3
"""Render the knowledge-graph companion to docs/dag_v0.3.svg (task K6-kg,
design/REPO_SPEC_v0.6_PATCH.md §3 / ROADMAP_v0.3.md step S6).

Reads every knowledge/harvest_v0.3/<hub>/kc-*.yaml card (id, title, kind,
base_relation, glosa_use) plus knowledge/harvest_v0.3/kg_edges_v0.3.jsonl,
writes:
  - docs/kg_v0.3.json  -- {nodes, edges, counts} readout of the same data,
    machine-readable companion to the picture.
  - docs/kg_v0.3.svg   -- concentric layout, no graphviz dependency (same
    hand-drawn-SVG pattern as docs/gen_dag_svg.py): the 'base' hub's cards
    sit on a centre ring (the lens the rest of the corpus is judged
    against, per FOUNDATION §1.0), every other hub's cards sit as an
    angular sector on an outer ring. Colour = base_relation. Size = each
    card's in-degree (how many edges in kg_edges_v0.3.jsonl name it as
    `to`) among edges between two real cards.

Readout, not truth: this is a diagram of the jsonl/yaml files as they
stand today, not a claim about the corpus's actual epistemic structure.
Tier Dr (a rendering script, not a checked claim).
"""
import glob
import json
import math
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARVEST_DIR = os.path.join(ROOT, "knowledge", "harvest_v0.3")
EDGES_PATH = os.path.join(HARVEST_DIR, "kg_edges_v0.3.jsonl")
JSON_OUT = os.path.join(ROOT, "docs", "kg_v0.3.json")
SVG_OUT = os.path.join(ROOT, "docs", "kg_v0.3.svg")

# base_relation -> colour (matches the vocabulary rolled up in
# KNOWLEDGE_STATUS_v0.3.md and kc-base-038's own verdict-class list).
RELATION_COLOR = {
    "holds": "#2f9e44",
    "refined_by_later_work": "#f08c00",
    "superseded": "#e03131",
    "outdated": "#868e96",
    "open": "#1c7ed6",
}
DEFAULT_COLOR = "#adb5bd"

# Pseudo targets that appear in kg_edges_v0.3.jsonl but are not cards
# (a card declaring "I am a base card" or "this feeds the FOUNDATION doc").
# Nodes = base cards + hub cards only (task scope), so these are counted
# in docs/kg_v0.3.json's `counts` block but not drawn as ring nodes.
PSEUDO_TARGETS = {"base", "FOUNDATION"}


def load_nodes():
    nodes = {}
    for fp in sorted(glob.glob(os.path.join(HARVEST_DIR, "*", "kc-*.yaml"))):
        hub = os.path.basename(os.path.dirname(fp))
        d = yaml.safe_load(open(fp, encoding="utf-8")) or {}
        cid = d.get("id") or os.path.splitext(os.path.basename(fp))[0]
        nodes[cid] = {
            "id": cid,
            "title": d.get("title", ""),
            "kind": d.get("kind", ""),
            "base_relation": d.get("base_relation", ""),
            "glosa_use": d.get("glosa_use", ""),
            "hub": hub,
        }
    return nodes


def load_edges():
    edges = []
    with open(EDGES_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            edges.append(json.loads(line))
    return edges


def compute_in_degree(nodes, edges):
    deg = {nid: 0 for nid in nodes}
    for e in edges:
        if e["from"] in nodes and e["to"] in nodes:
            deg[e["to"]] = deg.get(e["to"], 0) + 1
    return deg


def node_radius(in_degree):
    # sqrt scale so a handful of heavily-cited base cards don't dwarf the
    # canvas; clamped so every card stays visible (min) and legible (max).
    r = 3.2 + math.sqrt(max(in_degree, 0)) * 1.6
    return max(3.2, min(r, 16.0))


def write_json(nodes, edges, in_degree):
    pseudo_edges = [e for e in edges if e["to"] in PSEUDO_TARGETS]
    card_edges = [e for e in edges if e["to"] not in PSEUDO_TARGETS]
    out = {
        "generated_by": "docs/gen_kg_svg.py",
        "source": {
            "cards": "knowledge/harvest_v0.3/*/kc-*.yaml",
            "edges": "knowledge/harvest_v0.3/kg_edges_v0.3.jsonl",
        },
        "tier": "Dr",
        "counts": {
            "n_nodes": len(nodes),
            "n_edges_total": len(edges),
            "n_edges_card_to_card": len(card_edges),
            "n_edges_pseudo_target": len(pseudo_edges),
        },
        "nodes": [
            {**nodes[nid], "in_degree": in_degree.get(nid, 0)}
            for nid in sorted(nodes)
        ],
        "edges": edges,
    }
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write("\n")


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def layout(nodes):
    """Return {id: (x, y)} — base ring at centre, one angular sector per
    other hub on an outer ring."""
    cx, cy = 480, 480
    base_ids = sorted([n for n, d in nodes.items() if d["hub"] == "base"])
    hub_names = sorted({d["hub"] for d in nodes.values() if d["hub"] != "base"})
    pos = {}

    # centre ring: base cards evenly spaced on a circle
    r_base = 150
    n = max(len(base_ids), 1)
    for i, nid in enumerate(base_ids):
        theta = 2 * math.pi * i / n
        pos[nid] = (cx + r_base * math.cos(theta), cy + r_base * math.sin(theta))

    # outer ring: each hub gets a contiguous angular sector, cards spread
    # across two radii inside the sector (staggered) to reduce overlap
    sector_width = 2 * math.pi / max(len(hub_names), 1)
    gap = sector_width * 0.08  # visual gap between sectors
    r_outer_lo, r_outer_hi = 300, 430
    for h_idx, hub in enumerate(hub_names):
        members = sorted([n for n, d in nodes.items() if d["hub"] == hub])
        start = h_idx * sector_width + gap / 2
        end = (h_idx + 1) * sector_width - gap / 2
        m = max(len(members), 1)
        for j, nid in enumerate(members):
            frac = (j + 0.5) / m
            theta = start + frac * (end - start)
            radius = r_outer_lo if j % 2 == 0 else r_outer_hi
            pos[nid] = (cx + radius * math.cos(theta), cy + radius * math.sin(theta))
    return pos, cx, cy, r_base, hub_names, sector_width, gap, r_outer_lo, r_outer_hi


def write_svg(nodes, edges, in_degree):
    pos, cx, cy, r_base, hub_names, sector_width, gap, r_lo, r_hi = layout(nodes)
    W = H = 960
    legend_h = 190
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{W}" height="{H + legend_h}" viewBox="0 0 {W} {H + legend_h}" '
        'font-family="Helvetica, Arial, sans-serif">',
        f'<rect x="0" y="0" width="{W}" height="{H + legend_h}" fill="#ffffff"/>',
        f'<text x="{W/2}" y="26" text-anchor="middle" font-size="18" '
        'font-weight="bold" fill="#1c1c1c">glosa knowledge graph (kg) v0.3'
        "</text>",
        f'<text x="{W/2}" y="46" text-anchor="middle" font-size="11" '
        'fill="#495057">readout of knowledge/harvest_v0.3 -- base cards '
        "(centre ring) + hub cards (outer sectors); size = in-degree, "
        "colour = base_relation. Tier Dr.</text>",
    ]

    # sector divider lines + hub labels
    for h_idx, hub in enumerate(hub_names):
        theta = h_idx * sector_width
        x2 = cx + (r_hi + 25) * math.cos(theta)
        y2 = cy + (r_hi + 25) * math.sin(theta)
        parts.append(
            f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" '
            'stroke="#e9ecef" stroke-width="1"/>'
        )
        mid_theta = theta + sector_width / 2
        lx = cx + (r_hi + 45) * math.cos(mid_theta)
        ly = cy + (r_hi + 45) * math.sin(mid_theta)
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" '
            'font-size="12" font-weight="bold" fill="#212529">'
            f"{esc(hub)}</text>"
        )

    # base ring guide circle
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{r_base}" fill="none" '
        'stroke="#dee2e6" stroke-width="1" stroke-dasharray="3,3"/>'
    )

    # edges: only card-to-card (pseudo targets 'base'/'FOUNDATION' have no
    # ring position and are summarized in the legend instead)
    for e in edges:
        a, b = e.get("from"), e.get("to")
        if a in pos and b in pos:
            x1, y1 = pos[a]
            x2, y2 = pos[b]
            parts.append(
                f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                'stroke="#ced4da" stroke-width="0.6" stroke-opacity="0.55"/>'
            )

    # nodes
    for nid, (x, y) in pos.items():
        d = nodes[nid]
        color = RELATION_COLOR.get(d["base_relation"], DEFAULT_COLOR)
        r = node_radius(in_degree.get(nid, 0))
        title = esc(d["title"])
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" '
            'fill-opacity="0.88" stroke="#1c1c1c" stroke-width="0.4">'
            f"<title>{esc(nid)} [{esc(d['kind'])}] {title} "
            f"(base_relation={esc(d['base_relation'])}, "
            f"glosa_use={esc(d['glosa_use'])}, "
            f"in_degree={in_degree.get(nid, 0)})</title></circle>"
        )

    # centre label
    parts.append(
        f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="middle" '
        'font-size="11" fill="#868e96">base</text>'
    )

    # legend + counts, drawn below the ring canvas
    ly0 = H + 20
    parts.append(
        f'<text x="24" y="{ly0}" font-size="13" font-weight="bold" '
        'fill="#1c1c1c">Legend -- colour = base_relation</text>'
    )
    lx = 24
    ly = ly0 + 22
    for rel, color in RELATION_COLOR.items():
        parts.append(f'<circle cx="{lx+6}" cy="{ly-4}" r="6" fill="{color}"/>')
        parts.append(
            f'<text x="{lx+18}" y="{ly}" font-size="11" fill="#212529">'
            f"{esc(rel)}</text>"
        )
        ly += 18
    parts.append(f'<circle cx="{lx+6}" cy="{ly-4}" r="6" fill="{DEFAULT_COLOR}"/>')
    parts.append(
        f'<text x="{lx+18}" y="{ly}" font-size="11" fill="#212529">'
        "(other / unset)</text>"
    )

    n_base = sum(1 for d in nodes.values() if d["hub"] == "base")
    n_hub = len(nodes) - n_base
    card_edges = sum(1 for e in edges if e["to"] not in PSEUDO_TARGETS)
    pseudo_edges = len(edges) - card_edges
    counts_x = 300
    parts.append(
        f'<text x="{counts_x}" y="{ly0}" font-size="13" font-weight="bold" '
        'fill="#1c1c1c">Counts</text>'
    )
    count_lines = [
        f"nodes total: {len(nodes)}  (base: {n_base}, hub: {n_hub} across "
        f"{len(hub_names)} hubs)",
        f"edges total: {len(edges)}  (card-to-card: {card_edges}, "
        f"to base/FOUNDATION pseudo-target: {pseudo_edges})",
        "size = in-degree among card-to-card edges only (sqrt scale, "
        "clamped 3.2-16px)",
        "hub sectors (outer ring, clockwise from 0deg): "
        + ", ".join(hub_names),
    ]
    for i, line in enumerate(count_lines):
        parts.append(
            f'<text x="{counts_x}" y="{ly0 + 22 + i*18}" font-size="11" '
            f'fill="#212529">{esc(line)}</text>'
        )

    parts.append("</svg>")
    svg = "\n".join(parts)
    with open(SVG_OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    return len(svg.encode("utf-8"))


def main():
    nodes = load_nodes()
    edges = load_edges()
    in_degree = compute_in_degree(nodes, edges)
    write_json(nodes, edges, in_degree)
    svg_bytes = write_svg(nodes, edges, in_degree)
    print(
        f"wrote {JSON_OUT} ({len(nodes)} nodes, {len(edges)} edges) and "
        f"{SVG_OUT} ({svg_bytes} bytes)"
    )
    return nodes, edges, svg_bytes


if __name__ == "__main__":
    main()
