#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

BLUE = "#2563eb"
GOLD = "#f59e0b"
GREEN = "#16a34a"
ORANGE = "#f97316"
RED = "#dc2626"
PURPLE = "#8b5cf6"
GRAY = "#64748b"
INK = "#172033"
SOFT = "#475569"
GRID = "#e2e8f0"


def esc(value):
    return html.escape(str(value))


def open_svg(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#ffffff"/>'
    )


def text(x, y, value, size=16, weight="400", anchor="start", fill=INK):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
        f'{esc(value)}</text>'
    )


def line(x1, y1, x2, y2, stroke=GRID, width=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"{extra}/>'
    )


def box(x, y, w, h, title, lines, fill, stroke, title_fill=INK):
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        text(x + 18, y + 31, title, 16, "700", "start", title_fill),
    ]
    for i, item in enumerate(lines):
        out.append(text(x + 18, y + 57 + i * 21, item, 12.5, "400", "start", SOFT))
    return "".join(out)


def arrow(x1, y1, x2, y2, color=GRAY, dash=None):
    return (
        line(x1, y1, x2 - 12, y2, color, 2, dash)
        + f'<polygon points="{x2-12},{y2-6} {x2},{y2} {x2-12},{y2+6}" fill="{color}"/>'
    )


def primary_rows():
    with (ROOT / "data/derived/primary_results.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def triage_rows():
    with (ROOT / "data/derived/triage_results.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def research_design():
    rows = primary_rows()
    w, h = 1200, 720
    left, right, top, bottom = 90, 1135, 130, 590
    start_x, group_gap, bar_w, inner_gap = 115, 205, 38, 9

    out = [
        open_svg(w, h),
        text(55, 52, "Classification evidence across five requirement labels", 30, "700"),
        text(
            55, 82,
            "Precision, recall, and F1 expose different failure modes that a single aggregate score would hide.",
            15, "400", "start", SOFT,
        ),
    ]

    for i in range(6):
        value = i * 0.2
        y = bottom - value * (bottom - top)
        out += [
            line(left, y, right, y, GRID),
            text(left - 14, y + 5, f"{value:.1f}", 12, "400", "end", GRAY),
        ]

    out += [
        line(left, bottom, right, bottom, "#334155", 1.7),
        line(left, top, left, bottom, "#334155", 1.7),
    ]

    for i, row in enumerate(rows):
        gx = start_x + i * group_gap
        vals = [
            ("precision", float(row["precision"]), BLUE),
            ("recall", float(row["recall"]), RED if row["label"] == "UserRelated" else GOLD),
            ("f1", float(row["f1"]), GREEN),
        ]
        for j, (_, value, color) in enumerate(vals):
            bh = value * (bottom - top)
            x = gx + j * (bar_w + inner_gap)
            y = bottom - bh
            out += [
                f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{bh:.1f}" rx="4" '
                f'fill="{color}" fill-opacity="0.82"/>',
                text(x + bar_w / 2, y - 8, f"{value:.3f}", 11.5, "700", "middle", color),
            ]
        out.append(text(gx + 68, bottom + 31, row["label"], 13, "700", "middle", "#334155"))

    user = next(r for r in rows if r["label"] == "UserRelated")
    out += [
        '<rect x="830" y="112" width="305" height="78" rx="12" fill="#fef2f2" stroke="#fca5a5"/>',
        text(850, 140, "Key failure mode", 14, "700", "start", "#991b1b"),
        text(850, 165, f'UserRelated recall = {float(user["recall"]):.3f}', 14, "700", "start", RED),
        text(850, 185, f'{int(user["fn"])} false negatives; many positives are missed.', 11.5, "400", "start", "#7f1d1d"),
        '<rect x="100" y="630" width="18" height="18" rx="3" fill="#2563eb"/>',
        text(128, 644, "Precision", 12.5, "600"),
        '<rect x="225" y="630" width="18" height="18" rx="3" fill="#f59e0b"/>',
        text(253, 644, "Recall", 12.5, "600"),
        '<rect x="335" y="630" width="18" height="18" rx="3" fill="#16a34a"/>',
        text(363, 644, "F1", 12.5, "600"),
        '<rect x="425" y="630" width="18" height="18" rx="3" fill="#dc2626"/>',
        text(453, 644, "Highlighted recall weakness", 12.5, "600"),
        text(55, 700, "Source: pinned eTour gold labels and automatic predictions • n = 571 requirement elements", 12.5, "400", "start", GRAY),
        "</svg>",
    ]
    return "".join(out)


def method():
    out = [
        open_svg(1200, 760),
        text(55, 52, "Leakage safe evidence triage pipeline", 30, "700"),
        text(
            55, 82,
            "Gold labels are allowed for evaluation and oracle diagnosis, but never for deployable queue construction.",
            15, "400", "start", SOFT,
        ),
        box(55, 125, 245, 125, "Gold reference labels", ["571 eTour items", "Evaluation reference only"], "#fffbeb", GOLD, "#92400e"),
        box(55, 285, 245, 125, "Automatic predictions", ["Five labels per item", "Available before review"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(355, 205, 245, 145, "Classification evaluation", ["Join by requirement ID", "TP • FP • FN • TN", "Precision • Recall • F1"], "#f5f3ff", PURPLE, "#6d28d9"),
        arrow(300, 185, 355, 245, "#d97706"),
        arrow(300, 345, 355, 310, BLUE),
        line(650, 105, 650, 610, RED, 2, "8 7"),
        text(650, 100, "INFORMATION BOUNDARY", 12, "700", "middle", "#b91c1c"),
        '<rect x="620" y="420" width="60" height="110" rx="10" fill="#fef2f2" stroke="#fca5a5"/>',
        text(650, 445, "Gold", 11, "700", "middle", "#991b1b"),
        text(650, 464, "blocked", 11, "700", "middle", "#991b1b"),
        text(650, 483, "from", 11, "700", "middle", "#991b1b"),
        text(650, 502, "deployable", 11, "700", "middle", "#991b1b"),
        text(650, 521, "ranking", 11, "700", "middle", "#991b1b"),
        box(720, 130, 420, 140, "Oracle diagnostic", ["Rank by observed gold versus prediction errors", "Uses answer key • not deployable", "Quantifies concentration ceiling"], "#fff7ed", ORANGE, "#9a3412"),
        arrow(600, 245, 720, 200, ORANGE),
        box(720, 325, 420, 165, "Prediction only queue", ["Rare prediction patterns first", "Then hierarchy inconsistency", "Then predicted label density • then ID"], "#f0fdf4", "#22c55e", "#15803d"),
        arrow(300, 345, 720, 405, BLUE),
        box(720, 545, 420, 105, "Uniform random reference", ["Expected capture share = review budget / 571", "No gold labels used for ranking"], "#f8fafc", "#94a3b8", SOFT),
        box(180, 500, 360, 135, "Compare at fixed budgets", ["10 • 25 • 50 • 100 items", "Errors captured • capture share", "Enrichment versus random expectation"], "#eef2ff", "#6366f1", "#4338ca"),
        arrow(930, 270, 540, 550, ORANGE),
        arrow(930, 490, 540, 585, "#22c55e"),
        arrow(720, 595, 540, 610, GRAY),
        text(55, 725, "Scientific safeguard: the 51.9% top 100 result is an oracle upper bound; the deployable top 100 result is 21.5%.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(out)


def triage():
    rows = triage_rows()
    budgets = [10, 25, 50, 100]

    def values(method):
        by_budget = {int(r["budget"]): float(r["error_capture_share"]) for r in rows if r["method"] == method}
        return [by_budget[b] for b in budgets]

    series = [
        ("Oracle upper bound", values("oracle_upper_bound"), ORANGE, -14),
        ("Prediction only rarity", values("prediction_pattern_rarity"), BLUE, 22),
        ("Uniform random expected", values("random_expected"), GRAY, 35),
    ]

    w, h = 1200, 700
    left, right, top, bottom, max_y = 100, 1120, 130, 570, 0.60
    xs = [left + 90 + i * 285 for i in range(4)]

    out = [
        open_svg(w, h),
        text(55, 52, "Human review error capture by budget", 30, "700"),
        text(55, 82, "Oracle concentration is strong, while prediction only pattern rarity yields a smaller but positive gain over random expectation.", 15, "400", "start", SOFT),
    ]

    for i in range(7):
        value = i * 0.1
        y = bottom - (value / max_y) * (bottom - top)
        out += [
            line(left, y, right, y, GRID),
            text(left - 14, y + 5, f"{value*100:.0f}%", 12, "400", "end", GRAY),
        ]

    out += [
        line(left, bottom, right, bottom, "#334155", 1.7),
        line(left, top, left, bottom, "#334155", 1.7),
    ]
    for x, b in zip(xs, budgets):
        out.append(text(x, bottom + 30, b, 13, "700", "middle", "#334155"))

    out += [
        text((left + right) / 2, 640, "Review budget (requirement elements)", 14, "600", "middle"),
        f'<text x="28" y="{(top+bottom)/2}" transform="rotate(-90 28 {(top+bottom)/2})" '
        'font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="600" '
        'text-anchor="middle" fill="#172033">Share of all 534 label errors captured</text>',
    ]

    for label, vals, color, offset in series:
        pts = [(x, bottom - (v / max_y) * (bottom - top)) for x, v in zip(xs, vals)]
        out.append(
            f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="none" '
            f'stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
        )
        for (x, y), value in zip(pts, vals):
            out += [
                f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" stroke="{color}" stroke-width="3"/>',
                text(x, y + offset, f"{value*100:.1f}%", 11.5, "700", "middle", color),
            ]

    out += [
        '<rect x="760" y="105" width="355" height="100" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>',
        '<line x1="785" y1="132" x2="825" y2="132" stroke="#f97316" stroke-width="4"/>',
        text(838, 137, "Oracle upper bound • uses gold", 12.5, "600"),
        '<line x1="785" y1="160" x2="825" y2="160" stroke="#2563eb" stroke-width="4"/>',
        text(838, 165, "Prediction only rarity", 12.5, "600"),
        '<line x1="785" y1="188" x2="825" y2="188" stroke="#64748b" stroke-width="4"/>',
        text(838, 193, "Uniform random expected", 12.5, "600"),
        text(55, 685, "At budget 100: oracle 277 errors • prediction only 115 errors • random expectation 93.52 errors", 12.5, "400", "start", GRAY),
        "</svg>",
    ]
    return "".join(out)


def architecture():
    specs = [
        ("Pinned evidence", ["Gold labels", "Predictions"], "#fffbeb", GOLD),
        ("Evaluate labels", ["5 confusion matrices", "P • R • F1"], "#f5f3ff", PURPLE),
        ("Oracle ceiling", ["Gold aware", "Diagnostic only"], "#fff7ed", ORANGE),
        ("Deployable queue", ["Prediction only", "Pattern rarity"], "#f0fdf4", "#22c55e"),
        ("Decision evidence", ["Budget curves", "Bounded claims"], "#eff6ff", "#3b82f6"),
    ]
    xs = [35, 270, 505, 740, 975]
    out = [
        open_svg(1200, 500),
        text(55, 52, "Requirements evidence triage research architecture", 30, "700"),
        text(55, 82, "A systems engineering view of evidence, diagnosis, operational routing, and bounded decision support.", 15, "400", "start", SOFT),
    ]
    for i, (title, lines_, fill, stroke) in enumerate(specs):
        out.append(box(xs[i], 160, 190, 150, title, lines_, fill, stroke))
        if i < len(specs) - 1:
            out.append(arrow(xs[i] + 190, 235, xs[i+1], 235, GRAY))
    out += [
        '<rect x="735" y="345" width="195" height="78" rx="12" fill="#fef2f2" stroke="#ef4444"/>',
        text(832, 372, "Leakage control", 14, "700", "middle", "#991b1b"),
        text(832, 394, "No gold in deployable", 12, "600", "middle", "#991b1b"),
        text(832, 414, "ranking features", 12, "600", "middle", "#991b1b"),
        text(55, 470, "Primary engineering question: how much human review value can be recovered without using the answer key?", 13, "600", "start", "#334155"),
        "</svg>",
    ]
    return "".join(out)


def evaluation():
    out = [
        open_svg(1200, 620),
        text(55, 52, "Evidence boundary and released findings", 30, "700"),
        box(55, 100, 1090, 95, "Classification evidence", ["F1 spans 0.653 to 0.945; UserRelated recall is 0.502 and drives the clearest label specific weakness."], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(55, 220, 1090, 95, "Oracle diagnostic", ["Gold aware top 100 review captures 277 of 534 label errors, or 51.9%. This is a non deployable ceiling."], "#fff7ed", ORANGE, "#9a3412"),
        box(55, 340, 1090, 95, "Deployable result", ["Prediction only rarity captures 115 of 534 errors in 100 items, or 21.5%, versus 17.5% expected at random."], "#f0fdf4", "#22c55e", "#15803d"),
        box(55, 460, 1090, 95, "Claim boundary", ["Single benchmark • exploratory post hoc heuristic • no optimality, calibrated uncertainty, cost saving, or external validation claim."], "#fef2f2", "#ef4444", "#991b1b"),
        "</svg>",
    ]
    return "".join(out)


def render(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "architecture.svg": architecture(),
        "method.svg": method(),
        "research_design.svg": research_design(),
        "triage.svg": triage(),
        "evaluation.svg": evaluation(),
    }
    for name, content in figures.items():
        ET.fromstring(content)
        (out_dir / name).write_text(content, encoding="utf-8")
    return figures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(ROOT / "assets"))
    args = parser.parse_args()
    figures = render(Path(args.out_dir))
    print("generated_figures:", len(figures))


if __name__ == "__main__":
    main()
