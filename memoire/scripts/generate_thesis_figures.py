#!/usr/bin/env python3
from __future__ import annotations

import re
import sqlite3
import textwrap
from pathlib import Path


MEMOIRE_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path("/Users/lafleur/dev/mecene-clips/benchmark/data/benchmark.sqlite3")
FRAGMENTS_DIR = MEMOIRE_ROOT / "source" / "tableaux_et_figures"

EXAMPLE_SAMPLE_KEY = "6O3MzPeomqs-H4-0h_iDWME"
CASE_SAMPLE_KEYS = [
    "6O3MzPeomqs-H4-0h_iDWME",
    "0qz1ZKR4hkE-43_ki2v9WIQ",
    "9ByjCwumwBM-xSiFAXHE-mI",
    "VMUt82uYCd8--cHI7WOC2PQ",
]

CASE_NOTES = {
    "6O3MzPeomqs-H4-0h_iDWME": "Bon pic narratif et bornes presque parfaitement align\\'ees.",
    "0qz1ZKR4hkE-43_ki2v9WIQ": "Le noyau narratif est correct, avec une fin simplement plus courte.",
    "9ByjCwumwBM-xSiFAXHE-mI": "Segment voisin plausible, mais zone temporelle totalement rat\\'ee.",
    "VMUt82uYCd8--cHI7WOC2PQ": "Mauvais pic local: extrait plausible, mais bien trop loin de la r\\'ef\\'erence.",
}


def latex_escape(value: object) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def wrap_lines(text: str, width: int = 56, protect_leading_bracket: bool = False) -> str:
    collapsed = " ".join(text.split())
    wrapped = textwrap.wrap(collapsed, width=width)
    rendered: list[str] = []
    for line in wrapped:
        safe = latex_escape(line)
        if protect_leading_bracket and line.startswith("["):
            safe = r"\mbox{} " + safe
        rendered.append(safe)
    return r"\\ ".join(rendered)


def fmt_time(seconds: float) -> str:
    total = max(0.0, float(seconds))
    minutes = int(total // 60)
    secs = int(total % 60)
    return f"{minutes:02d}:{secs:02d}"


def frac(value: float, total: float) -> str:
    if total <= 0:
        return "0.000"
    clipped = min(max(value / total, 0.0), 1.0)
    return f"{clipped:.3f}"


def split_sections(rendered_context: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in rendered_context.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line.rstrip())
    return sections


TIMESTAMP_LINE_RE = re.compile(r"^\[(\d{2}):(\d{2})\]\s+(.*)$")
SCENE_HEADER_RE = re.compile(r"^###\s+Scene\s+\d+\s+\[(\d{2}):(\d{2})-(\d{2}):(\d{2})\]")


def to_seconds(minutes: str, seconds: str) -> float:
    return int(minutes) * 60 + int(seconds)


def pick_timeline_excerpt(lines: list[str], start_sec: float, end_sec: float) -> list[str]:
    chosen: list[str] = []
    for line in lines:
        match = TIMESTAMP_LINE_RE.match(line)
        if not match:
            continue
        t = to_seconds(match.group(1), match.group(2))
        if start_sec - 12 <= t <= end_sec + 12:
            chosen.append(line)
        if len(chosen) >= 4:
            break
    if chosen:
        return chosen
    fallback = [line for line in lines if line.startswith("[")][:4]
    return fallback if fallback else ["No detailed visual notes selected."]


def pick_scene_excerpt(lines: list[str], start_sec: float, end_sec: float) -> list[str]:
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if current:
                blocks.append(current)
            current = [line]
        else:
            if current:
                current.append(line)
    if current:
        blocks.append(current)

    for block in blocks:
        header = block[0]
        match = SCENE_HEADER_RE.match(header)
        if not match:
            continue
        scene_start = to_seconds(match.group(1), match.group(2))
        scene_end = to_seconds(match.group(3), match.group(4))
        if scene_start < end_sec and scene_end > start_sec:
            return block[:4]

    return blocks[0][:4] if blocks else ["No scene summary available."]


def timeline_bar(label: str, start_sec: float, end_sec: float, total_sec: float, color: str) -> str:
    start_fraction = frac(start_sec, total_sec)
    width_fraction = frac(max(end_sec - start_sec, 0.0), total_sec)
    return (
        rf"\TimelineBar{{{label}}}{{{start_fraction}}}{{{width_fraction}}}{{{color}}}"
    )


def load_best_structured_run(con: sqlite3.Connection) -> sqlite3.Row:
    cur = con.cursor()
    row = cur.execute(
        """
        SELECT run_id, run_name, context_template_name, model_profile_name, prompt_template_name,
               mean_text_iou, mean_temporal_iou, mean_combined_score
        FROM benchmark_run_leaderboard
        WHERE processed_samples >= 29
          AND context_template_name != 'video-direct-v1'
        ORDER BY mean_combined_score DESC, started_at DESC
        LIMIT 1
        """
    ).fetchone()
    if row is None:
        raise RuntimeError("No full structured run found.")
    return row


def load_case_row(con: sqlite3.Connection, run_id: str, sample_key: str) -> sqlite3.Row:
    cur = con.cursor()
    row = cur.execute(
        """
        SELECT
          s.sample_key,
          v.duration_sec AS source_duration_sec,
          ri.pred_start_sec,
          ri.pred_end_sec,
          ri.gt_start_sec,
          ri.gt_end_sec,
          ri.text_iou,
          ri.temporal_iou,
          ri.combined_score,
          ri.extracted_moment_text,
          ri.rendered_context
        FROM benchmark_run_items ri
        JOIN benchmark_samples s ON s.id = ri.sample_id
        JOIN benchmark_videos v ON v.id = s.video_id
        WHERE ri.run_id = ?
          AND s.sample_key = ?
        """
        ,
        (run_id, sample_key),
    ).fetchone()
    if row is None:
        raise RuntimeError(f"Missing run item for {sample_key}.")
    return row




def build_case_card(row: sqlite3.Row, label: str, color: str) -> str:
    total_sec = float(row["source_duration_sec"])
    text_excerpt = wrap_lines(str(row["extracted_moment_text"])[:140], width=48)
    metrics = (
        rf"\textbf{{{label}}}\\[0.2em]"
        + rf"\texttt{{{latex_escape(row['sample_key'])}}}\\[0.4em]"
        + rf"Txt IoU: {float(row['text_iou']):.3f} \quad "
        + rf"Temp IoU: {float(row['temporal_iou']):.3f} \quad "
        + rf"Score: {float(row['combined_score']):.3f}\\"
        + rf"Dur\'ee GT: {float(row['gt_end_sec']) - float(row['gt_start_sec']):.1f}~s \quad "
        + rf"Dur\'ee pr\'edite: {float(row['pred_end_sec']) - float(row['pred_start_sec']):.1f}~s"
    )
    gt_bar = timeline_bar(
        "GT",
        float(row["gt_start_sec"]),
        float(row["gt_end_sec"]),
        total_sec,
        "MemoBlue",
    )
    pred_bar = timeline_bar(
        "Pr\\'edit",
        float(row["pred_start_sec"]),
        float(row["pred_end_sec"]),
        total_sec,
        color,
    )
    note = CASE_NOTES[str(row["sample_key"])]
    return rf"""\ThesisBox{{0.47\textwidth}}{{%
{metrics}\\[0.5em]
{gt_bar}\\[0.5em]
{pred_bar}\\[0.5em]
\textbf{{Extrait produit}}\\[0.3em]
{text_excerpt}\\[0.5em]
\textbf{{Lecture}}\\[0.3em]
{note}
}}"""


def build_worked_example_fragment(example: sqlite3.Row) -> str:
    sections = split_sections(str(example["rendered_context"]))
    timeline_excerpt = pick_timeline_excerpt(
        sections.get("Detailed Visual Timeline", []),
        float(example["pred_start_sec"]),
        float(example["pred_end_sec"]),
    )
    scene_excerpt = pick_scene_excerpt(
        sections.get("Scenes (gemini-flash-lite-movement-clean-v2)", []),
        float(example["pred_start_sec"]),
        float(example["pred_end_sec"]),
    )

    metadata = (
        r"\textbf{Cas retenu}\\[0.4em]"
        + rf"\texttt{{{latex_escape(example['sample_key'])}}}\\[0.4em]"
        + rf"Source: {float(example['source_duration_sec']):.1f}~s\\"
        + rf"GT: {fmt_time(float(example['gt_start_sec']))}--{fmt_time(float(example['gt_end_sec']))}\\"
        + rf"Pr\'edit: {fmt_time(float(example['pred_start_sec']))}--{fmt_time(float(example['pred_end_sec']))}\\"
        + rf"Txt IoU: {float(example['text_iou']):.3f}\\"
        + rf"Temp IoU: {float(example['temporal_iou']):.3f}\\"
        + rf"Score: {float(example['combined_score']):.3f}"
    )

    timeline_box = (
        r"\textbf{Detailed Visual Timeline}\\[0.3em]"
        + r"\\ ".join(wrap_lines(line, width=44, protect_leading_bracket=True) for line in timeline_excerpt)
    )
    scene_box = (
        r"\textbf{Scenes + Dialogue}\\[0.3em]"
        + r"\\ ".join(wrap_lines(line, width=44) for line in scene_excerpt)
        + r"\\[0.5em]\textbf{Extrait choisi}\\[0.3em]"
        + wrap_lines(str(example["extracted_moment_text"])[:300], width=50)
    )

    total_sec = float(example["source_duration_sec"])
    gt_bar = timeline_bar(
        "R\\'ef\\'erence GT",
        float(example["gt_start_sec"]),
        float(example["gt_end_sec"]),
        total_sec,
        "MemoBlue",
    )
    pred_bar = timeline_bar(
        "Span pr\\'edit",
        float(example["pred_start_sec"]),
        float(example["pred_end_sec"]),
        total_sec,
        "MemoGreen",
    )

    return rf"""\begin{{figure}}[ht]
\centering
\ThesisBox{{0.24\textwidth}}{{{metadata}}}
\hfill
\ThesisBox{{0.33\textwidth}}{{{timeline_box}}}
\hfill
\ThesisBox{{0.33\textwidth}}{{{scene_box}}}

\vspace{{0.8em}}
\ThesisBox{{0.94\textwidth}}{{%
\textbf{{Lecture du cas}}\\[0.4em]
{gt_bar}\\[0.6em]
{pred_bar}\\[0.6em]
Le mod\`ele retrouve ici le bon noyau argumentatif et reste proche des bornes de r\'ef\'erence, ce qui explique le double recouvrement textuel et temporel \'elev\'e.
}}
\caption{{Exemple concret de transformation d'une vid\'eo en contexte structur\'e, puis en span s\'electionn\'e par le mod\`ele.}}
\label{{fig:worked-example}}
\end{{figure}}
"""


def build_success_failure_fragment(case_rows: list[sqlite3.Row]) -> str:
    success_left = build_case_card(case_rows[0], "Succ\\`es A", "MemoGreen")
    success_right = build_case_card(case_rows[1], "Succ\\`es B", "MemoGreen")
    failure_left = build_case_card(case_rows[2], "\\'Echec A", "MemoRed")
    failure_right = build_case_card(case_rows[3], "\\'Echec B", "MemoRed")
    return rf"""\begin{{figure}}[p]
\centering
{success_left}
\hfill
{success_right}

\vspace{{0.8em}}
{failure_left}
\hfill
{failure_right}
\caption{{Comparaison de deux cas de succ\`es et de deux cas d'\'echec du meilleur run structur\'e complet. Les succ\`es combinent recouvrement th\'ematique et calibration temporelle; les \'echecs gardent parfois un signal s\'emantique partiel mais ratent la bonne fen\^etre temporelle.}}
\label{{fig:success-failure-cases}}
\end{{figure}}
"""


def main() -> None:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row

    best_run = load_best_structured_run(con)
    example = load_case_row(con, str(best_run["run_id"]), EXAMPLE_SAMPLE_KEY)
    cases = [load_case_row(con, str(best_run["run_id"]), key) for key in CASE_SAMPLE_KEYS]

    write_text(FRAGMENTS_DIR / "figure_worked_example.tex", build_worked_example_fragment(example))
    write_text(FRAGMENTS_DIR / "figure_success_failure.tex", build_success_failure_fragment(cases))

    con.close()


if __name__ == "__main__":
    main()
