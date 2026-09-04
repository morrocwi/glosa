#!/usr/bin/env python3
"""Render design/DAG_v0.3.yaml to docs/dag_v0.3.dot and docs/dag_v0.3.svg.

Used because `dot` (graphviz) is not installed on this workstation; this draws
a plain layered box-and-arrow SVG by hand (kind = layer, top to bottom),
matching what `dot -Tsvg` would be asked to render from the .dot file this
script also writes. Readout, not truth: this is a diagram of the YAML file,
not a claim about what will happen.
"""
import yaml
import html

ROOT = __file__.rsplit('/', 2)[0]
DAG_YAML = f"{ROOT}/design/DAG_v0.3.yaml"
DOT_OUT = f"{ROOT}/docs/dag_v0.3.dot"
SVG_OUT = f"{ROOT}/docs/dag_v0.3.svg"

KIND_COLOR = {
    'foundation': '#4c6ef5',
    'schema': '#12b886',
    'kernel': '#f76707',
    'cli': '#7048e8',
    'template': '#ae3ec9',
    'docs': '#868e96',
    'process': '#495057',
}
STATUS_STYLE = {
    'done': ('#2f9e44', 'solid'),
    'proposed': ('#1c1c1c', 'solid'),
    'deferred': ('#adb5bd', 'dashed'),
}
EDGE_STYLE = {
    'requires': ('#1c1c1c', 'solid'),
    'informs': ('#868e96', 'dashed'),
    'conflicts': ('#e03131', 'solid'),
}


def load():
    d = yaml.safe_load(open(DAG_YAML))
    nodes = {n['id']: n for n in d['nodes']}
    edges = d['edges']
    return nodes, edges


def write_dot(nodes, edges):
    lines = ['digraph glosa_dag_v0_3 {', '  rankdir=TB;', '  node [shape=box, style="rounded,filled", fontname="Helvetica"];']
    # cluster by kind for rank grouping
    kinds = {}
    for n in nodes.values():
        kinds.setdefault(n['kind'], []).append(n['id'])
    for kind, ids in kinds.items():
        lines.append(f'  subgraph cluster_{kind} {{ label="{kind}"; style=dashed;')
        for nid in ids:
            n = nodes[nid]
            color = KIND_COLOR.get(n['kind'], '#dee2e6')
            _, border_style = STATUS_STYLE.get(n['status'], ('#000', 'solid'))
            label = n['title'].replace('"', "'")
            lines.append(
                f'    "{nid}" [label="{label}\\n[{n["status"]}]", fillcolor="{color}", '
                f'style="rounded,filled,{border_style}"];'
            )
        lines.append('  }')
    for e in edges:
        color, style = EDGE_STYLE.get(e['kind'], ('#000', 'solid'))
        lines.append(f'  "{e["from"]}" -> "{e["to"]}" [label="{e["kind"]}", color="{color}", style={style}];')
    lines.append('}')
    with open(DOT_OUT, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def wrap_text(text, width=26):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if len(trial) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def write_svg(nodes, edges):
    # layer by kind, in a fixed order
    layer_order = ['process', 'kernel', 'schema', 'foundation', 'docs', 'cli', 'template']
    layers = {k: [] for k in layer_order}
    for nid, n in nodes.items():
        layers.setdefault(n['kind'], []).append(nid)
    layers = {k: v for k, v in layers.items() if v}

    box_w, box_h = 200, 70
    h_gap, v_gap = 40, 110
    margin = 40

    positions = {}
    max_row_w = 0
    y = margin
    for kind in layer_order:
        if kind not in layers:
            continue
        row = sorted(layers[kind])
        row_w = len(row) * box_w + (len(row) - 1) * h_gap
        max_row_w = max(max_row_w, row_w)
        x = margin
        for nid in row:
            positions[nid] = (x, y, kind)
            x += box_w + h_gap
        y += box_h + v_gap

    width = max_row_w + 2 * margin
    height = y + margin

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
               f'viewBox="0 0 {width} {height}" font-family="Helvetica,Arial,sans-serif">')
    svg.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>')
    svg.append('<defs>'
                '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                '<path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker>'
                '<marker id="arrow-conflict" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                '<path d="M0,0 L10,5 L0,10 z" fill="#e03131"/></marker>'
                '</defs>')

    # layer labels
    y = margin
    for kind in layer_order:
        if kind not in layers:
            continue
        svg.append(f'<text x="{margin}" y="{y - 12}" font-size="13" fill="#495057" font-weight="bold">{kind}</text>')
        y += box_h + v_gap

    def center(nid):
        x, y, _ = positions[nid]
        return x + box_w / 2, y + box_h / 2

    def edge_point(nid, other_nid):
        x, y, _ = positions[nid]
        ox, oy, _ = positions[other_nid]
        cx, cy = x + box_w / 2, y + box_h / 2
        ocx, ocy = ox + box_w / 2, oy + box_h / 2
        if oy > y:
            return cx, y + box_h
        elif oy < y:
            return cx, y
        else:
            return (x + box_w, cy) if ocx > cx else (x, cy)

    # edges first (behind boxes)
    for e in edges:
        if e['from'] not in positions or e['to'] not in positions:
            continue
        x1, y1 = edge_point(e['from'], e['to'])
        x2, y2 = edge_point(e['to'], e['from'])
        color = {'requires': '#495057', 'informs': '#adb5bd', 'conflicts': '#e03131'}.get(e['kind'], '#495057')
        dash = ' stroke-dasharray="6,4"' if e['kind'] == 'informs' else ''
        marker = 'arrow-conflict' if e['kind'] == 'conflicts' else 'arrow'
        svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                   f'stroke="{color}" stroke-width="1.6"{dash} marker-end="url(#{marker})"/>')

    # nodes
    for nid, n in nodes.items():
        x, y, kind = positions[nid]
        fill = KIND_COLOR.get(kind, '#dee2e6')
        status = n['status']
        stroke = {'done': '#2f9e44', 'proposed': '#1c1c1c', 'deferred': '#adb5bd'}.get(status, '#1c1c1c')
        dash = ' stroke-dasharray="5,3"' if status == 'deferred' else ''
        opacity = '0.55' if status == 'deferred' else ('0.85' if status == 'done' else '1')
        svg.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" '
                   f'fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="2"{dash}/>')
        title_lines = wrap_text(n['title'], 28)[:3]
        ty = y + 18
        for line in title_lines:
            svg.append(f'<text x="{x + box_w/2}" y="{ty}" font-size="10.5" fill="white" '
                       f'text-anchor="middle" font-weight="600">{html.escape(line)}</text>')
            ty += 13
        badge = f"[{status}]" + (" ⚑H" if n['human_decision_needed'] else "")
        svg.append(f'<text x="{x + box_w/2}" y="{y + box_h - 6}" font-size="9" fill="white" '
                   f'text-anchor="middle" font-style="italic">{html.escape(badge)}</text>')

    # legend
    ly = height - margin + 5
    svg.append(f'<text x="{margin}" y="{ly}" font-size="10" fill="#495057">'
               'solid=requires, dashed-gray=informs, red=conflicts; dashed border=deferred; '
               '⚑H=human_decision_needed</text>')
    svg.append('</svg>')

    with open(SVG_OUT, 'w') as f:
        f.write('\n'.join(svg))


if __name__ == '__main__':
    nodes, edges = load()
    write_dot(nodes, edges)
    write_svg(nodes, edges)
    print(f"wrote {DOT_OUT}")
    print(f"wrote {SVG_OUT}")
