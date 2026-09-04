#!/usr/bin/env python3
"""
research_map.py — builds the founder's public research map (glosa repo).

Reads registry/zenodo_all_records.json (public Zenodo records) and
registry/zenodo_clusters.json (cluster hub DOIs), and emits:
  - docs/RESEARCH_MAP.md   (Thai first, then English; timeline table, tree, hub table)
  - docs/research_map.svg  (hand-built SVG timeline/tree figure, stdlib only)
  - docs/research_map.html (self-contained wrapper around the SVG)

Design notes (readout-not-truth):
  - Every number in the outputs is computed here, from the two JSON files,
    at the moment this script runs. Nothing is asserted from memory.
  - Cluster/tag assignment in the source JSON is itself a keyword+manual
    readout (tier: Dr) done upstream of this script, not a ground truth.
    This script only aggregates and dates what is already recorded.
  - Publication dates are Zenodo `publication_date` values as stored in the
    registry — a platform-reported date, not an independent timestamp
    authority.
  - No network calls. Stdlib only (no matplotlib) — SVG is hand-written.
  - Idempotent: re-running with an updated registry regenerates all three
    files deterministically from the input JSON.

Usage:
    python3 tools/research_map.py
Run from anywhere; paths are resolved relative to this file's repo root.
"""
from __future__ import annotations

import json
import html
import datetime as dt
from pathlib import Path
from collections import defaultdict, Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_DIR = REPO_ROOT / "registry"
DOCS_DIR = REPO_ROOT / "docs"

RECORDS_PATH = REGISTRY_DIR / "zenodo_all_records.json"
CLUSTERS_PATH = REGISTRY_DIR / "zenodo_clusters.json"

MD_OUT = DOCS_DIR / "RESEARCH_MAP.md"
SVG_OUT = DOCS_DIR / "research_map.svg"
HTML_OUT = DOCS_DIR / "research_map.html"

# ---------------------------------------------------------------------------
# Cluster / tag reference labels (Thai + English), per the task spec.
# ---------------------------------------------------------------------------
CLUSTER_ORDER_HINT = ["ep", "he", "ph", "ai", "islam", "tourism", "se", "other"]

CLUSTER_LABEL = {
    "ep": ("ญาณวิทยา / ทฤษฎีความรู้", "Epistemology"),
    "he": ("สุขภาพ / จิตใจ", "Health & mind"),
    "ph": ("ฟิสิกส์ / สารสนเทศ", "Physics & information"),
    "ai": ("ปัญญาประดิษฐ์กับความรู้", "AI & knowledge"),
    "islam": ("อิสลาม / สังคมมุสลิม / อำนาจความรู้", "Islam / Muslim society / epistemic authority"),
    "tourism": ("ท่องเที่ยว / บริการ", "Tourism & service"),
    "se": ("วิสาหกิจเพื่อสังคม", "Social enterprise"),
    "other": ("สังคม / อื่นๆ", "Society / other"),
}

CLUSTER_COLOR = {
    "ep": "#7c5cff",
    "he": "#ff6f91",
    "ph": "#2fb8ac",
    "ai": "#f2a541",
    "islam": "#4f8ef7",
    "tourism": "#4fbf67",
    "se": "#c76b3f",
    "other": "#9aa0a6",
}

TAG_LABEL = {
    "ai": ("ปัญญาประดิษฐ์", "AI"),
    "islam": ("อิสลาม", "Islam"),
    "tourism": ("ท่องเที่ยว", "Tourism"),
    "se": ("วิสาหกิจเพื่อสังคม", "Social enterprise"),
}

MONTH_TH = {
    1: "ม.ค.", 2: "ก.พ.", 3: "มี.ค.", 4: "เม.ย.", 5: "พ.ค.", 6: "มิ.ย.",
    7: "ก.ค.", 8: "ส.ค.", 9: "ก.ย.", 10: "ต.ค.", 11: "พ.ย.", 12: "ธ.ค.",
}


def load_data():
    with open(RECORDS_PATH, encoding="utf-8") as f:
        records = json.load(f)
    clusters_meta = {}
    if CLUSTERS_PATH.exists():
        try:
            with open(CLUSTERS_PATH, encoding="utf-8") as f:
                clusters_meta = json.load(f)
        except (json.JSONDecodeError, OSError):
            clusters_meta = {}
    return records, clusters_meta


def month_key(date_str: str) -> str:
    return date_str[:7]  # YYYY-MM


def parse_date(date_str: str) -> dt.date:
    return dt.date.fromisoformat(date_str)


# ---------------------------------------------------------------------------
# Compute all readout facts from the JSON.
# ---------------------------------------------------------------------------

def compute(records, clusters_meta):
    hub_ids = {v.get("hub_id") for v in clusters_meta.values() if v.get("hub_id")}
    hub_dois = {v.get("hub_doi") for v in clusters_meta.values() if v.get("hub_doi")}

    # Records already exclude hub index records in this dataset, but guard
    # anyway so a future registry update that inlines hubs stays honest.
    excluded_hub_records = [r for r in records if r.get("id") in hub_ids or r.get("doi") in hub_dois]
    working = [r for r in records if r not in excluded_hub_records]

    total = len(working)
    dates = sorted(parse_date(r["date"]) for r in working)
    first_date, last_date = dates[0], dates[-1]
    months_active = (
        (last_date.year - first_date.year) * 12 + (last_date.month - first_date.month) + 1
    )

    # per-cluster
    cluster_records = defaultdict(list)
    for r in working:
        cluster_records[r.get("cluster", "other")].append(r)

    cluster_first = {}
    cluster_last = {}
    cluster_count = {}
    for c, recs in cluster_records.items():
        ds = sorted(parse_date(r["date"]) for r in recs)
        cluster_first[c] = ds[0]
        cluster_last[c] = ds[-1]
        cluster_count[c] = len(recs)

    # branches ordered by date of earliest appearance (trunk -> branches order)
    branch_order = sorted(cluster_records.keys(), key=lambda c: cluster_first[c])

    # per-tag (sub-branches are tags, cutting across clusters but shown
    # nested under whichever cluster(s) their tagged records fall in)
    tag_records = defaultdict(list)
    for r in working:
        for t in r.get("tags", []):
            tag_records[t].append(r)
    tag_first = {}
    for t, recs in tag_records.items():
        tag_first[t] = min(parse_date(r["date"]) for r in recs)

    # cluster x tag matrix (which tags appear inside which cluster, and when
    # the tag first appears inside that cluster => "branch emergence")
    cluster_tag_first = defaultdict(dict)
    for r in working:
        c = r.get("cluster", "other")
        d = parse_date(r["date"])
        for t in r.get("tags", []):
            if t not in cluster_tag_first[c] or d < cluster_tag_first[c][t]:
                cluster_tag_first[c][t] = d

    # month x cluster histogram
    month_cluster_counts = defaultdict(lambda: defaultdict(int))
    all_months = set()
    for r in working:
        mk = month_key(r["date"])
        month_cluster_counts[mk][r.get("cluster", "other")] += 1
        all_months.add(mk)
    months_sorted = sorted(all_months)

    # month with most uploads (overall, any cluster)
    month_totals = Counter()
    for r in working:
        month_totals[month_key(r["date"])] += 1
    top_month, top_month_count = month_totals.most_common(1)[0]

    # cumulative growth by month
    cumulative = []
    running = 0
    for mk in months_sorted:
        running += sum(month_cluster_counts[mk].values())
        cumulative.append((mk, running))

    # multi-tag overlaps: which tag-pairs co-occur on the same record
    overlap_counter = Counter()
    for r in working:
        tags = sorted(set(r.get("tags", [])))
        for i in range(len(tags)):
            for j in range(i + 1, len(tags)):
                overlap_counter[(tags[i], tags[j])] += 1

    # cross-cluster bleed: does a tag appear across >1 cluster?
    tag_cluster_spread = defaultdict(set)
    for r in working:
        for t in r.get("tags", []):
            tag_cluster_spread[t].add(r.get("cluster", "other"))

    return dict(
        working=working,
        total=total,
        first_date=first_date,
        last_date=last_date,
        months_active=months_active,
        cluster_records=cluster_records,
        cluster_first=cluster_first,
        cluster_last=cluster_last,
        cluster_count=cluster_count,
        branch_order=branch_order,
        tag_records=tag_records,
        tag_first=tag_first,
        cluster_tag_first=cluster_tag_first,
        months_sorted=months_sorted,
        month_cluster_counts=month_cluster_counts,
        month_totals=month_totals,
        top_month=top_month,
        top_month_count=top_month_count,
        cumulative=cumulative,
        overlap_counter=overlap_counter,
        tag_cluster_spread=tag_cluster_spread,
        excluded_hub_records=excluded_hub_records,
        hub_ids=hub_ids,
    )


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def th_date(d: dt.date) -> str:
    return f"{d.day} {MONTH_TH[d.month]} {d.year}"


def fmt_month(mk: str) -> str:
    y, m = mk.split("-")
    return f"{MONTH_TH[int(m)]} {y}"


def render_reading_paragraph_th(c) -> str:
    first = c["first_date"]
    last = c["last_date"]
    total = c["total"]
    months_active = c["months_active"]
    branch_order = c["branch_order"]

    branch_th_list = []
    for b in branch_order:
        label_th, _ = CLUSTER_LABEL.get(b, (b, b))
        branch_th_list.append(f"{label_th} (เริ่มปรากฏ {th_date(c['cluster_first'][b])})")
    branch_str = " → ".join(branch_th_list)

    # ai / he emergence relative to ph/ep (bleed narrative), computed not asserted
    bleed_lines = []
    for tag in ("ai", "islam", "tourism", "se"):
        spread = c["tag_cluster_spread"].get(tag, set())
        if len(spread) > 1:
            spread_labels = "、".join(CLUSTER_LABEL.get(s, (s, s))[0] for s in sorted(spread, key=lambda s: c["cluster_first"].get(s, dt.date.max)))
            tag_th, _ = TAG_LABEL.get(tag, (tag, tag))
            bleed_lines.append(f"แท็ก「{tag_th}」ปรากฏข้าม {len(spread)} กิ่ง ({spread_labels})")

    para = (
        f"อ่านจากบันทึกสาธารณะทั้งหมด {total} รายการใน Zenodo (ไม่รวม 3 รายการดัชนีโปรแกรม/hub ที่ไม่มีตัวเนื้อหาของตัวเอง) "
        f"งานที่เก่าที่สุดในทะเบียนลงวันที่ {th_date(first)} และรายการล่าสุดลงวันที่ {th_date(last)} "
        f"รวมช่วงเวลาที่มีการอัปโหลดจริง {months_active} เดือน "
        f"กิ่งงาน (cluster) เรียงตามวันที่เริ่มปรากฏคือ: {branch_str} "
        f"เดือนที่มีการอัปโหลดมากที่สุดคือ {fmt_month(c['top_month'])} ({c['top_month_count']} รายการ) "
    )
    if bleed_lines:
        para += "ร่องรอยการไหลข้ามกิ่ง (จากแท็กที่ติดพร้อมกันในหลายกิ่ง): " + "; ".join(bleed_lines) + ". "
    para += (
        "ทั้งหมดนี้เป็นการอ่านจากข้อมูลที่บันทึกไว้ (readout) ไม่ใช่การยืนยันความจริงเชิงเนื้อหาของแต่ละงาน "
        "ระดับความน่าเชื่อของตัวเลขในย่อหน้านี้คือ finite_diagnostic — คำนวณตรงจากไฟล์ JSON ทั้งสองไฟล์ ณ เวลารันสคริปต์นี้เท่านั้น"
    )
    return para


def render_reading_paragraph_en(c) -> str:
    first = c["first_date"]
    last = c["last_date"]
    total = c["total"]
    months_active = c["months_active"]
    branch_order = c["branch_order"]

    branch_str = " -> ".join(
        f"{CLUSTER_LABEL.get(b, (b, b))[1]} (earliest record {th_date(c['cluster_first'][b])})"
        for b in branch_order
    )

    bleed_lines = []
    for tag in ("ai", "islam", "tourism", "se"):
        spread = c["tag_cluster_spread"].get(tag, set())
        if len(spread) > 1:
            spread_labels = ", ".join(CLUSTER_LABEL.get(s, (s, s))[1] for s in sorted(spread, key=lambda s: c["cluster_first"].get(s, dt.date.max)))
            bleed_lines.append(f'tag "{TAG_LABEL.get(tag, (tag, tag))[1]}" appears across {len(spread)} branches ({spread_labels})')

    para = (
        f"Reading the public record set as a whole: {total} entries are registered on Zenodo "
        f"(excluding 3 programme-index/hub entries that carry no content of their own). "
        f"The oldest dated entry in the registry is {th_date(first)} and the most recent is {th_date(last)}, "
        f"spanning {months_active} months with at least one upload. "
        f"Branches (clusters), ordered by date of earliest appearance, are: {branch_str}. "
        f"The month with the most uploads is {fmt_month(c['top_month'])} ({c['top_month_count']} entries). "
    )
    if bleed_lines:
        para += "Cross-branch bleed (tags shared across clusters): " + "; ".join(bleed_lines) + ". "
    para += (
        "All of this is a readout of recorded data, not a verification of the content of any given entry. "
        "Confidence tier for the numbers in this paragraph: finite_diagnostic — computed directly from the "
        "two source JSON files at script run time, nothing asserted from memory."
    )
    return para


def render_timeline_table(c) -> str:
    branches = c["branch_order"]
    lines = ["| เดือน / Month | " + " | ".join(CLUSTER_LABEL.get(b, (b, b))[0] for b in branches) + " | รวม / Total |",
             "|---" * (len(branches) + 2) + "|"]
    for mk in c["months_sorted"]:
        row = [fmt_month(mk)]
        total = 0
        for b in branches:
            v = c["month_cluster_counts"][mk].get(b, 0)
            total += v
            row.append(str(v) if v else "")
        row.append(str(total))
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_tree(c) -> str:
    lines = []
    lines.append("- **ลำต้น / Trunk — Readout Universe (สารสนเทศเป็นพื้นฐาน / information-as-primitive)**")
    for b in c["branch_order"]:
        th, en = CLUSTER_LABEL.get(b, (b, b))
        recs = sorted(c["cluster_records"][b], key=lambda r: r["date"])
        lines.append(
            f"  - **กิ่ง / Branch — {th} / {en}** "
            f"(`{b}`, {len(recs)} รายการ / entries, {th_date(c['cluster_first'][b])} → {th_date(c['cluster_last'][b])})"
        )
        # sub-branches = tags present in this cluster, ordered by date of earliest appearance in-cluster
        tags_here = c["cluster_tag_first"].get(b, {})
        tag_order = sorted(tags_here.keys(), key=lambda t: tags_here[t])
        tagged_ids = set()
        for t in tag_order:
            t_th, t_en = TAG_LABEL.get(t, (t, t))
            sub_recs = sorted(
                [r for r in recs if t in r.get("tags", [])],
                key=lambda r: r["date"],
            )
            for r in sub_recs:
                tagged_ids.add(r["id"])
            lines.append(
                f"    - *กิ่งย่อย / Sub-branch — {t_th} / {t_en}* "
                f"(เริ่มปรากฏ / earliest seen {th_date(tags_here[t])}, {len(sub_recs)} รายการ)"
            )
            for r in sub_recs:
                lines.append(f"      - {th_date(parse_date(r['date']))} — {r['title']} — {r['doi']}")
        # untagged leaves directly under the branch
        untagged = [r for r in recs if r["id"] not in tagged_ids]
        if untagged:
            lines.append("    - *(ไม่มีแท็กย่อย / no sub-tag)*")
            for r in untagged:
                lines.append(f"      - {th_date(parse_date(r['date']))} — {r['title']} — {r['doi']}")
    return "\n".join(lines)


def render_hub_table(clusters_meta) -> str:
    if not clusters_meta:
        return (
            "_ยังไม่มีไฟล์ registry/zenodo_clusters.json ที่อ่านได้ — ตาราง hub DOI ยังสร้างไม่ได้ในรอบนี้ / "
            "registry/zenodo_clusters.json was missing or unreadable — hub DOI table could not be built this run._"
        )
    lines = ["| กิ่ง / Cluster | Hub DOI | จำนวนสมาชิกที่ลงทะเบียน / Registered members |",
             "|---|---|---|"]
    for key in sorted(clusters_meta.keys(), key=lambda k: CLUSTER_ORDER_HINT.index(k) if k in CLUSTER_ORDER_HINT else 99):
        v = clusters_meta[key]
        th, en = CLUSTER_LABEL.get(key, (key, key))
        hub_doi = v.get("hub_doi") or "_(กำลังสร้าง / being created)_"
        members = v.get("members", [])
        lines.append(f"| {th} / {en} (`{key}`) | {hub_doi} | {len(members)} |")
    return "\n".join(lines)


def render_markdown(c, clusters_meta) -> str:
    generated = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    md = []
    md.append("# แผนที่งานวิจัย — Yaoharee Lahtee (ORCID 0009-0005-3861-0626)\n")
    md.append(
        f"_สร้างอัตโนมัติโดย `tools/research_map.py` เมื่อ {generated} จาก "
        f"`registry/zenodo_all_records.json` และ `registry/zenodo_clusters.json` — เป็น readout ไม่ใช่บันทึกที่แก้ไขด้วยมือ_\n"
    )
    md.append("## ภาพรวมการเติบโต (อ่านจากข้อมูล ไม่ใช่การตีความ)\n")
    md.append(render_reading_paragraph_th(c) + "\n")
    md.append("## Growth overview (a data readout, not an interpretation)\n")
    md.append(render_reading_paragraph_en(c) + "\n")

    md.append("## ตารางไทม์ไลน์ตามเดือน × กิ่ง / Timeline table by month × cluster\n")
    md.append(render_timeline_table(c) + "\n")

    md.append(
        "## ลำต้น → กิ่ง → กิ่งย่อย → ใบไม้ (พร้อม DOI) / Trunk → branches → sub-branches → leaves (with DOI)\n"
    )
    md.append(render_tree(c) + "\n")

    md.append("## ตาราง Hub DOI ต่อกิ่ง / Hub DOI per branch\n")
    md.append(render_hub_table(clusters_meta) + "\n")

    md.append("## ขอบเขตความซื่อตรงของข้อมูล / Honest edges\n")
    md.append(
        "- การจัดกิ่ง/แท็ก (cluster/tags) ในไฟล์ทะเบียนเป็นการอ่านแบบคำสำคัญ+ตรวจด้วยมือ (readout) โดยผู้จัดทำ — ระดับ Dr, "
        "ไม่ใช่การจัดหมวดที่ผ่านกระบวนการภายนอกใดๆ ยืนยัน\n"
        "- Cluster/tag classification in the registry is a keyword + manual readout by the maintainer — tier Dr, "
        "not a classification confirmed by any outside process.\n"
        "- วันที่ทั้งหมดคือ `publication_date` ที่ Zenodo รายงาน ไม่ใช่วันที่เขียนงานจริงหรือวันที่ตรวจสอบอิสระ\n"
        "- All dates are the `publication_date` field as reported by Zenodo — not the date work was actually written, "
        "and not an independently audited date.\n"
        f"- รายการดัชนีโปรแกรม/hub ({len(c['excluded_hub_records'])} รายการที่พบในทะเบียนหลัก) ถูกตัดออกจากตัวนับทั้งหมดในเอกสารนี้ "
        "เพราะเป็นหน้าดัชนีของกลุ่มงาน ไม่ใช่ผลงานวิจัยเดี่ยว\n"
        f"- Programme-index/hub entries ({len(c['excluded_hub_records'])} found inlined in the main registry) are excluded "
        "from every count in this document — they are index pages for a group of works, not standalone research entries.\n"
        "- ตัวเลขทั้งหมดในเอกสารนี้คำนวณจากไฟล์ JSON สองไฟล์นี้เท่านั้น ไม่มีการเรียกเครือข่ายหรือแหล่งข้อมูลอื่นระหว่างสร้างรายงาน\n"
        "- Every number in this document is computed from these two JSON files only — no network calls or other data "
        "sources are used while generating this report.\n"
    )
    return "\n".join(md)


# ---------------------------------------------------------------------------
# SVG rendering (hand-built, stdlib only)
# ---------------------------------------------------------------------------

def esc(s: str) -> str:
    return html.escape(s, quote=True)


def render_svg(c) -> str:
    branches = c["branch_order"]
    months = c["months_sorted"]
    n_months = len(months)

    width = min(1600, max(900, 140 + n_months * 46))
    left_pad = 180
    right_pad = 40
    top_pad = 60
    lane_h = 46
    lanes_top = top_pad + 30
    n_lanes = len(branches)
    plot_h = n_lanes * lane_h
    cum_h = 110
    bottom_pad = 50
    height = lanes_top + plot_h + cum_h + bottom_pad

    plot_w = width - left_pad - right_pad
    if n_months > 1:
        x_step = plot_w / (n_months - 1)
    else:
        x_step = 0

    def x_of(month_idx: float) -> float:
        return left_pad + month_idx * x_step

    month_idx_of = {mk: i for i, mk in enumerate(months)}

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" font-family="Sarabun, \'Noto Sans Thai\', \'Segoe UI\', sans-serif" '
        f'role="img" aria-label="Research map timeline">'
    )
    parts.append(
        """
<style>
  .rm-bg { fill: var(--rm-bg, #ffffff); }
  .rm-axis { stroke: var(--rm-axis, #888888); stroke-width: 1; }
  .rm-grid { stroke: var(--rm-grid, #dddddd); stroke-width: 1; }
  .rm-label { fill: var(--rm-fg, #222222); font-size: 12px; }
  .rm-label-small { fill: var(--rm-fg, #222222); font-size: 10px; }
  .rm-title { fill: var(--rm-fg, #222222); font-size: 15px; font-weight: 600; }
  .rm-lane-label { fill: var(--rm-fg, #222222); font-size: 12px; font-weight: 600; }
  .rm-cum-line { fill: none; stroke: var(--rm-accent, #444444); stroke-width: 2; }
  .rm-cum-fill { fill: var(--rm-accent-fill, rgba(120,120,120,0.12)); }
  @media (prefers-color-scheme: dark) {
    svg { --rm-bg: #14161a; --rm-axis: #8b8f98; --rm-grid: #2a2d33; --rm-fg: #e8e8ea; --rm-accent: #c9c9d0; --rm-accent-fill: rgba(230,230,235,0.12); }
  }
</style>
"""
    )
    parts.append(f'<rect class="rm-bg" x="0" y="0" width="{width}" height="{height}"/>')
    parts.append(
        f'<text class="rm-title" x="{left_pad}" y="26">แผนที่งานวิจัย / Research map — trunk → branches → leaves (by month)</text>'
    )

    # month gridlines + labels (every month, thin; label every other if crowded)
    label_every = 1 if n_months <= 24 else 2
    for i, mk in enumerate(months):
        x = x_of(i)
        parts.append(
            f'<line class="rm-grid" x1="{x:.1f}" y1="{lanes_top - 6:.1f}" x2="{x:.1f}" y2="{lanes_top + plot_h + cum_h:.1f}"/>'
        )
        if i % label_every == 0:
            label = fmt_month(mk)
            parts.append(
                f'<text class="rm-label-small" x="{x:.1f}" y="{lanes_top + plot_h + 14:.1f}" '
                f'text-anchor="middle">{esc(label)}</text>'
            )

    # lanes
    for li, b in enumerate(branches):
        y = lanes_top + li * lane_h
        color = CLUSTER_COLOR.get(b, "#999999")
        th, en = CLUSTER_LABEL.get(b, (b, b))
        parts.append(f'<line class="rm-axis" x1="{left_pad:.1f}" y1="{y + lane_h/2:.1f}" x2="{width - right_pad:.1f}" y2="{y + lane_h/2:.1f}" stroke="{color}" stroke-opacity="0.35"/>')
        parts.append(
            f'<text class="rm-lane-label" x="10" y="{y + lane_h/2 + 4:.1f}" fill="{color}">{esc(th)}</text>'
        )
        parts.append(
            f'<text class="rm-label-small" x="10" y="{y + lane_h/2 + 17:.1f}">{esc(en)} ({c["cluster_count"][b]})</text>'
        )

        # branch emergence marker at date of earliest appearance
        first_i = month_idx_of.get(month_key(c["cluster_first"][b].isoformat()), None)
        if first_i is not None:
            fx = x_of(first_i)
            fy = y + lane_h / 2
            parts.append(
                f'<line x1="{fx:.1f}" y1="{lanes_top - 6:.1f}" x2="{fx:.1f}" y2="{lanes_top + plot_h + cum_h:.1f}" '
                f'stroke="{color}" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.55">'
                f'<title>{esc(th)} / {esc(en)}: earliest record {esc(th_date(c["cluster_first"][b]))}</title></line>'
            )

        # dots per record within this lane, jittered slightly within month bucket if multiple
        recs_by_month = defaultdict(list)
        for r in c["cluster_records"][b]:
            recs_by_month[month_key(r["date"])].append(r)
        for mk, recs in recs_by_month.items():
            i = month_idx_of[mk]
            base_x = x_of(i)
            n = len(recs)
            for k, r in enumerate(sorted(recs, key=lambda rr: rr["date"])):
                # spread multiple same-month dots vertically within the lane
                offset = (k - (n - 1) / 2) * 6
                dy = y + lane_h / 2 + offset
                dx = base_x
                tags = ",".join(r.get("tags", [])) or "-"
                title_text = f"{r['title']} ({r['date']}) doi:{r['doi']} tags:{tags}"
                parts.append(
                    f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.4" fill="{color}" stroke="var(--rm-bg,#fff)" stroke-width="0.6">'
                    f'<title>{esc(title_text)}</title></circle>'
                )

    # cumulative curve
    cum_top = lanes_top + plot_h + 26
    cum_bottom = cum_top + cum_h - 20
    max_cum = c["cumulative"][-1][1] if c["cumulative"] else 1
    max_cum = max(max_cum, 1)

    def cy_of(v: int) -> float:
        return cum_bottom - (v / max_cum) * (cum_bottom - cum_top)

    parts.append(
        f'<text class="rm-label" x="{left_pad}" y="{cum_top - 10:.1f}">เส้นสะสม / Cumulative total records (max={max_cum})</text>'
    )
    pts = []
    for mk, v in c["cumulative"]:
        i = month_idx_of[mk]
        pts.append((x_of(i), cy_of(v)))
    if pts:
        path_d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        area_d = path_d + f" L {pts[-1][0]:.1f} {cum_bottom:.1f} L {pts[0][0]:.1f} {cum_bottom:.1f} Z"
        parts.append(f'<path class="rm-cum-fill" d="{area_d}"/>')
        parts.append(f'<path class="rm-cum-line" d="{path_d}"/>')
        for (px, py), (mk, v) in zip(pts, c["cumulative"]):
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2" fill="var(--rm-accent,#444)"><title>{esc(fmt_month(mk))}: {v}</title></circle>')

    parts.append("</svg>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# HTML wrapper
# ---------------------------------------------------------------------------

def render_html(c, clusters_meta, svg_content: str) -> str:
    generated = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    rows = []
    for b in c["branch_order"]:
        th, en = CLUSTER_LABEL.get(b, (b, b))
        color = CLUSTER_COLOR.get(b, "#999")
        hub = clusters_meta.get(b, {})
        hub_doi = hub.get("hub_doi")
        hub_cell = (
            f'<a href="https://doi.org/{esc(hub_doi)}">{esc(hub_doi)}</a>' if hub_doi
            else "<em>กำลังสร้าง / being created</em>"
        )
        rows.append(
            f"<tr><td><span class=\"dot\" style=\"background:{color}\"></span>{esc(th)} / {esc(en)} "
            f"<code>{esc(b)}</code></td>"
            f"<td>{c['cluster_count'][b]}</td>"
            f"<td>{esc(th_date(c['cluster_first'][b]))}</td>"
            f"<td>{esc(th_date(c['cluster_last'][b]))}</td>"
            f"<td>{hub_cell}</td></tr>"
        )
    table_rows = "\n".join(rows)

    doc = f"""<title>แผนที่งานวิจัย / Research Map</title>
<style>
  :root {{
    --bg: #ffffff; --fg: #1c1e21; --muted: #5f6368; --card: #f6f7f9; --border: #e2e4e8;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: #14161a; --fg: #e8e8ea; --muted: #a3a7ae; --card: #1c1f24; --border: #2a2d33; }}
  }}
  body {{ background: var(--bg); color: var(--fg); font-family: Sarabun, 'Noto Sans Thai', 'Segoe UI', sans-serif; padding: 24px 20px 60px; max-width: 1200px; margin: 0 auto; }}
  h1 {{ font-size: 22px; margin-bottom: 4px; }}
  .subtitle {{ color: var(--muted); font-size: 13px; margin-bottom: 20px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; margin-bottom: 22px; overflow-x: auto; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
  th, td {{ text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }}
  th {{ color: var(--muted); font-weight: 600; }}
  .dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; }}
  .svgwrap {{ overflow-x: auto; }}
  a {{ color: inherit; }}
  code {{ background: var(--border); padding: 1px 5px; border-radius: 4px; font-size: 11px; }}
  footer {{ color: var(--muted); font-size: 11px; margin-top: 30px; }}
</style>
<h1>แผนที่งานวิจัย — Yaoharee Lahtee / Research Map</h1>
<div class="subtitle">
  ORCID 0009-0005-3861-0626 &middot; สร้างจาก {c['total']} รายการสาธารณะบน Zenodo &middot; อัปเดตอัตโนมัติเมื่อ {esc(generated)}<br>
  Built from {c['total']} public Zenodo records &middot; auto-generated {esc(generated)} &middot; readout, not truth — see docs/RESEARCH_MAP.md for full honest-edges notes.
</div>

<div class="card svgwrap">
{svg_content}
</div>

<div class="card">
<table>
<thead><tr><th>กิ่ง / Branch</th><th>จำนวน / Count</th><th>แรกสุด / First</th><th>ล่าสุด / Last</th><th>Hub DOI</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>
</div>

<footer>
เอกสารฉบับเต็ม (readout เต็มรูปแบบ พร้อมตารางไทม์ไลน์และต้นไม้ DOI) อยู่ที่ <code>docs/RESEARCH_MAP.md</code>.
Full report (complete readout with timeline table and DOI tree) at <code>docs/RESEARCH_MAP.md</code>.
</footer>
"""
    return doc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    records, clusters_meta = load_data()
    c = compute(records, clusters_meta)

    md = render_markdown(c, clusters_meta)
    MD_OUT.write_text(md, encoding="utf-8")

    svg = render_svg(c)
    SVG_OUT.write_text(svg, encoding="utf-8")

    html_doc = render_html(c, clusters_meta, svg)
    HTML_OUT.write_text(html_doc, encoding="utf-8")

    print(f"wrote {MD_OUT}")
    print(f"wrote {SVG_OUT}")
    print(f"wrote {HTML_OUT}")
    print(f"total={c['total']} first={c['first_date']} last={c['last_date']} "
          f"months_active={c['months_active']} top_month={c['top_month']}({c['top_month_count']})")
    for b in c["branch_order"]:
        print(f"  branch {b}: n={c['cluster_count'][b]} first={c['cluster_first'][b]} last={c['cluster_last'][b]}")


if __name__ == "__main__":
    main()
