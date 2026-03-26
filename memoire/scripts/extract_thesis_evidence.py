#!/usr/bin/env python3
from __future__ import annotations

import sqlite3
from pathlib import Path


MEMOIRE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = Path("/Users/lafleur/dev/mecene-clips/benchmark/data/benchmark.sqlite3")
ACTIVE_VLM_TEMPLATE = "gemini-flash-lite-movement-clean-v2"
DATASET_SLUG = "validation29"
TABLES_AND_FIGURES_DIR = MEMOIRE_ROOT / "source" / "tableaux_et_figures"

CONTEXT_LABELS = {
    "transcript-v1": "transcript-v1",
    "timeline-scenes-dialogue-inline-v1": "timeline-scenes-inline-v1",
    "timeline-dialogue-inline-v1": "timeline-dialogue-inline-v1",
    "scenes-dialogue-inline-v1": "scenes-dialogue-inline-v1",
    "scene-details-dialogue-inline-v1": "scene-details-dialogue-inline-v1",
    "timeline-scenes-dialogue-scene-grouped-v1": "scene-grouped-v1",
    "timeline-scenes-dialogue-scene-grouped-dialogue-script-v1": "scene-grouped-dialogue-script-v1",
    "timeline-scenes-dialogue-typed-v1": "typed-v1",
    "timeline-scenes-dialogue-typed-novlm-v1": "typed-novlm-v1",
    "timeline-scenes-dialogue-typed-numbered-v1": "typed-numbered-v1",
    "timeline-scenes-dialogue-typed-timestamps-v1": "typed-timestamps-v1",
    "scenes-dialogue-typed-novlm-v1": "no-vlm-v1",
    "video-direct-v1": "video-direct-v1",
}

PROMPT_LABELS = {
    "basic-selector": "basic-selector",
    "timeline-scenes-dialogue-selector-v2": "selector-v2",
    "timeline-scenes-dialogue-selector-v2-tool-v1": "selector-v2-tool-v1",
    "timeline-scenes-dialogue-selector-v2-tool-sentences-v1": "selector-sentences-v1",
    "timeline-scenes-dialogue-selector-v2-tool-timestamps-v1": "selector-timestamps-v1",
    "timeline-scenes-dialogue-selector-v2-tool-timestamps-range-v2": "selector-timestamps-range-v2",
    "timeline-scenes-dialogue-selector-v2-tool-timestamps-range-v3": "selector-timestamps-range-v3",
    "scenes-dialogue-selector-v2-tool-v1": "scenes-selector-tool-v1",
    "video-direct-selector-v1-tool-timestamps": "video-direct-tool-v1",
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


def fmt_float(value: object, digits: int = 3) -> str:
    if value is None:
        return "--"
    return f"{float(value):.{digits}f}"


def fmt_int(value: object) -> str:
    if value is None:
        return "--"
    return f"{int(value)}"


def compact_context_name(name: object) -> str:
    text = "" if name is None else str(name)
    if not text:
        return "--"
    return CONTEXT_LABELS.get(text, text)


def compact_prompt_name(name: object) -> str:
    text = "" if name is None else str(name)
    if not text:
        return "--"
    return PROMPT_LABELS.get(text, text)


def compact_model_name(name: object) -> str:
    text = "" if name is None else str(name)
    if not text:
        return "--"
    if text.startswith("openrouter-"):
        text = text[len("openrouter-") :]
    if text.startswith("groq-"):
        text = text[len("groq-") :]
    reasoning_suffixes = {
        "__reasoning-none": " (r:none)",
        "__reasoning-low": " (r:low)",
        "__reasoning-medium": " (r:med)",
        "__reasoning-high": " (r:high)",
    }
    for suffix, replacement in reasoning_suffixes.items():
        if text.endswith(suffix):
            text = text[: -len(suffix)] + replacement
            break
    text = text.replace("-preview", "")
    return text


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_table_block(
    *,
    caption: str,
    label: str,
    colspec: str,
    headers: list[str],
    rows: list[list[str]],
    size: str = r"\footnotesize",
) -> str:
    header_line = " & ".join(headers) + r" \\"
    body_lines = "\n".join(" & ".join(row) + r" \\" for row in rows)
    return (
        r"\begin{table}[ht]" + "\n"
        + r"\centering" + "\n"
        + size + "\n"
        + rf"\caption{{{caption}}}" + "\n"
        + rf"\label{{{label}}}" + "\n"
        + rf"\begin{{tabularx}}{{\textwidth}}{{{colspec}}}" + "\n"
        + r"\toprule" + "\n"
        + header_line + "\n"
        + r"\midrule" + "\n"
        + body_lines + "\n"
        + r"\bottomrule" + "\n"
        + r"\end{tabularx}" + "\n"
        + r"\end{table}" + "\n"
    )


def main() -> None:
    db_path = DEFAULT_DB
    out_notes = MEMOIRE_ROOT / "generated" / "notes"
    out_fragments = TABLES_AND_FIGURES_DIR

    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    dataset = cur.execute(
        """
        SELECT
          dataset_slug AS slug,
          dataset_sample_count AS sample_count,
          dataset_created_at AS created_at
        FROM report_thesis_dataset_stats_v1
        """,
    ).fetchone()

    video_stats = cur.execute(
        """
        SELECT
          video_count,
          avg_duration_sec,
          min_duration_sec,
          max_duration_sec
        FROM report_thesis_dataset_stats_v1
        """
    ).fetchone()

    gt_stats = cur.execute(
        """
        SELECT
          avg_gt_duration_sec,
          min_gt_duration_sec,
          max_gt_duration_sec
        FROM report_thesis_dataset_stats_v1
        """
    ).fetchone()

    vlm_stats = cur.execute(
        """
        SELECT
          active_vlm_template AS template_name,
          vlm_video_count AS video_count,
          vlm_min_frames AS min_frames,
          vlm_max_frames AS max_frames,
          vlm_avg_frames AS avg_frames,
          vlm_total_scene_summaries AS total_scene_summaries,
          vlm_last_updated AS last_updated
        FROM report_thesis_dataset_stats_v1
        """
    ).fetchone()

    context_variants = cur.execute(
        """
        SELECT context_name, video_count, min_chars, max_chars, avg_chars
        FROM report_thesis_context_variants_v1
        """
    ).fetchall()

    run_inventory = cur.execute(
        """
        SELECT
          COUNT(*) AS total_runs,
          SUM(CASE WHEN processed_samples >= 29 THEN 1 ELSE 0 END) AS runs_29,
          SUM(CASE WHEN processed_samples = 5 THEN 1 ELSE 0 END) AS runs_5,
          SUM(CASE WHEN processed_samples = 1 THEN 1 ELSE 0 END) AS runs_1,
          SUM(CASE WHEN processed_samples BETWEEN 2 AND 28 THEN 1 ELSE 0 END) AS partial_other
        FROM benchmark_run_leaderboard
        """
    ).fetchone()

    full_runs = cur.execute(
        """
        SELECT
          condition,
          model,
          context,
          text_iou,
          temporal_iou,
          combined_score,
          avg_total_tokens,
          avg_effective_cost_usd,
          avg_initial_data_cost_usd,
          avg_first_run_cost_usd,
          run_name
        FROM report_thesis_main_full_runs_v1
        """
    ).fetchall()

    best_structured = cur.execute(
        """
        SELECT *
        FROM benchmark_run_leaderboard
        WHERE processed_samples >= 29
          AND context_template_name != 'video-direct-v1'
        ORDER BY mean_combined_score DESC, started_at DESC
        LIMIT 1
        """
    ).fetchone()

    direct_video = cur.execute(
        """
        SELECT *
        FROM benchmark_run_leaderboard
        WHERE processed_samples >= 29
          AND context_template_name = 'video-direct-v1'
        ORDER BY mean_combined_score DESC, started_at DESC
        LIMIT 1
        """
    ).fetchone()

    novlm_status = cur.execute(
        """
        SELECT
          MAX(processed_samples) AS max_processed_samples,
          MAX(mean_combined_score) AS best_combined_score,
          COUNT(*) AS run_count
        FROM benchmark_run_leaderboard
        WHERE context_template_name = 'timeline-scenes-dialogue-typed-novlm-v1'
        """
    ).fetchone()

    controlled_gemini_rows = [
        dict(row)
        for row in cur.execute(
            """
            SELECT
              condition,
              model,
              context,
              coverage_note,
              text_iou,
              temporal_iou,
              combined_score,
              avg_total_tokens,
              avg_effective_cost_usd,
              avg_initial_data_cost_usd,
              avg_first_run_cost_usd,
              run_name
            FROM report_thesis_controlled_gemini_ablation_v1
            ORDER BY sort_order
            """
        ).fetchall()
    ]

    best_run_items = cur.execute(
        """
        SELECT
          s.sample_key,
          ri.text_iou,
          ri.temporal_iou,
          ri.combined_score,
          ri.pred_start_sec,
          ri.pred_end_sec,
          ri.gt_start_sec,
          ri.gt_end_sec,
          ri.extracted_moment_text
        FROM benchmark_run_items ri
        JOIN benchmark_samples s ON s.id = ri.sample_id
        WHERE ri.run_id = ?
        ORDER BY ri.combined_score DESC, s.sample_key ASC
        """,
        (best_structured["run_id"],),
    ).fetchall()

    top_examples = best_run_items[:5]
    bottom_examples = list(reversed(best_run_items[-5:]))

    full_runs_rows = []
    for row in full_runs:
        full_runs_rows.append(
            {
                "condition": row["condition"],
                "model": row["model"],
                "context": row["context"],
                "text_iou": float(row["text_iou"]),
                "temporal_iou": float(row["temporal_iou"]),
                "combined_score": float(row["combined_score"]),
                "avg_total_tokens": float(row["avg_total_tokens"]),
                "avg_effective_cost_usd": float(row["avg_effective_cost_usd"]),
                "avg_initial_data_cost_usd": float(row["avg_initial_data_cost_usd"]),
                "avg_first_run_cost_usd": float(row["avg_first_run_cost_usd"]),
                "run_name": row["run_name"],
            }
        )

    exploratory_context_rows = [
        {
            "context_template_name": row["context_template_name"],
            "context_label": compact_context_name(row["context_template_name"]),
            "first_seen_at": row["first_seen_at"],
            "run_count": int(row["run_count"] or 0),
            "max_processed_samples": int(row["max_processed_samples"] or 0),
            "best_run_name": row["best_run_name"],
            "best_prompt_template_name": row["best_prompt_template_name"],
            "best_prompt_label": compact_prompt_name(row["best_prompt_template_name"]),
            "best_model_profile_name": row["best_model_profile_name"],
            "best_model_label": compact_model_name(row["best_model_profile_name"]),
            "best_processed_samples": int(row["best_processed_samples"] or 0),
            "best_text_iou": float(row["best_text_iou"] or 0.0),
            "best_temporal_iou": float(row["best_temporal_iou"] or 0.0),
            "best_combined_score": float(row["best_combined_score"] or 0.0),
            "best_avg_total_tokens": float(row["best_avg_total_tokens"] or 0.0),
            "best_total_effective_cost_usd": float(row["best_total_effective_cost_usd"] or 0.0),
        }
        for row in cur.execute(
            """
            SELECT
              context_template_name,
              first_seen_at,
              run_count,
              max_processed_samples,
              best_run_name,
              best_prompt_template_name,
              best_model_profile_name,
              best_processed_samples,
              best_text_iou,
              best_temporal_iou,
              best_combined_score,
              best_avg_total_tokens,
              best_total_effective_cost_usd
            FROM report_thesis_exploratory_context_runs_v1
            """
        ).fetchall()
    ]

    exploratory_milestones = [
        {
            "started_at": str(row["started_at"]),
            "context_template_name": str(row["context_template_name"]),
            "context_label": compact_context_name(row["context_template_name"]),
            "prompt_template_name": str(row["prompt_template_name"]),
            "prompt_label": compact_prompt_name(row["prompt_template_name"]),
            "model_profile_name": str(row["model_profile_name"]),
            "model_label": compact_model_name(row["model_profile_name"]),
            "processed_samples": int(row["processed_samples"] or 0),
            "combined_score": float(row["combined_score"] or 0.0),
            "delta_vs_previous_best": round(float(row["delta_vs_previous_best"] or 0.0), 3),
            "run_name": str(row["run_name"]),
        }
        for row in cur.execute(
            """
            SELECT
              started_at,
              context_template_name,
              prompt_template_name,
              model_profile_name,
              processed_samples,
              combined_score,
              delta_vs_previous_best,
              run_name
            FROM report_thesis_exploratory_milestones_v1
            """
        ).fetchall()
    ]

    dataset_stats_rows = [[
        fmt_int(dataset["sample_count"]),
        fmt_float(video_stats["avg_duration_sec"], 1),
        latex_escape(f"{video_stats['min_duration_sec']:.1f}-{video_stats['max_duration_sec']:.1f}"),
        fmt_float(gt_stats["avg_gt_duration_sec"], 1),
        latex_escape(f"{gt_stats['min_gt_duration_sec']:.1f}-{gt_stats['max_gt_duration_sec']:.1f}"),
        latex_escape(f"{vlm_stats['video_count']}/{dataset['sample_count']}"),
    ]]
    write_text(
        out_fragments / "table_dataset_stats.tex",
        make_table_block(
            caption=r"Statistiques descriptives du benchmark \texttt{validation29}",
            label="tab:dataset-stats",
            colspec=r">{\raggedright\arraybackslash}p{0.08\textwidth}>{\raggedright\arraybackslash}p{0.17\textwidth}>{\raggedright\arraybackslash}p{0.17\textwidth}>{\raggedright\arraybackslash}p{0.15\textwidth}>{\raggedright\arraybackslash}p{0.17\textwidth}>{\raggedright\arraybackslash}X",
            headers=[
                r"Paires",
                r"Dur\'ee source moyenne (s)",
                r"Dur\'ee source min-max (s)",
                r"Dur\'ee GT moyenne (s)",
                r"Dur\'ee GT min-max (s)",
                r"Couverture VLM",
            ],
            rows=dataset_stats_rows,
        ),
    )

    context_rows = []
    for row in context_variants:
        context_rows.append([
            latex_escape(compact_context_name(row["context_name"])),
            fmt_int(row["video_count"]),
            fmt_int(round(float(row["avg_chars"]))),
            fmt_int(row["min_chars"]),
            fmt_int(row["max_chars"]),
        ])
    write_text(
        out_fragments / "table_context_variants.tex",
        make_table_block(
            caption=r"Variantes de contexte disponibles sur l'ensemble complet",
            label="tab:context-variants",
            colspec=r">{\raggedright\arraybackslash}Xrrrr",
            headers=[r"Contexte", r"Couverture", r"Taille moyenne (car.)", r"Min", r"Max"],
            rows=context_rows,
            size=r"\small",
        ),
    )

    full_run_table_rows = []
    for row in full_runs_rows:
        full_run_table_rows.append([
            latex_escape(row["condition"]),
            latex_escape(compact_model_name(row["model"])),
            latex_escape(compact_context_name(row["context"])),
            fmt_float(row["text_iou"]),
            fmt_float(row["temporal_iou"]),
            fmt_float(row["combined_score"]),
            fmt_int(round(row["avg_total_tokens"])),
            fmt_float(row["avg_effective_cost_usd"], 3),
            fmt_float(row["avg_initial_data_cost_usd"], 3),
            fmt_float(row["avg_first_run_cost_usd"], 3),
        ])
    write_text(
        out_fragments / "table_main_full_runs.tex",
        make_table_block(
            caption=r"Conditions compl\`etes sur 29 \'echantillons retenues pour les revendications principales",
            label="tab:main-full-runs",
            colspec=r">{\raggedright\arraybackslash}p{0.12\textwidth}>{\raggedright\arraybackslash}p{0.17\textwidth}>{\raggedright\arraybackslash}p{0.11\textwidth}rrrrrrr",
            headers=[
                r"Condition",
                r"Mod\`ele",
                r"Contexte",
                r"Txt IoU",
                r"Temp IoU",
                r"Score",
                r"Tokens",
                r"Run/video",
                r"Contexte/video",
                r"1er passage/video",
            ],
            rows=full_run_table_rows,
            size=r"\scriptsize",
        ),
    )

    controlled_gemini_table_rows = []
    for row in controlled_gemini_rows:
        controlled_gemini_table_rows.append([
            latex_escape(str(row["condition"])),
            latex_escape(str(row["coverage_note"])),
            fmt_float(row["text_iou"]),
            fmt_float(row["temporal_iou"]),
            fmt_float(row["combined_score"]),
            fmt_int(round(float(row["avg_total_tokens"]))),
            fmt_float(row["avg_effective_cost_usd"], 3),
            fmt_float(row["avg_initial_data_cost_usd"], 3),
            fmt_float(row["avg_first_run_cost_usd"], 3),
        ])
    write_text(
        out_fragments / "table_controlled_gemini_ablation.tex",
        make_table_block(
            caption=r"Comparaison contr\^ol\'ee sous Gemini 3.1 Flash Lite: m\^eme mod\`ele, m\^eme protocole de sortie, et variation explicite de la repr\'esentation d'entr\'ee",
            label="tab:controlled-gemini-ablation",
            colspec=r">{\raggedright\arraybackslash}p{0.21\textwidth}>{\raggedright\arraybackslash}p{0.24\textwidth}rrrrrrr",
            headers=[
                r"Condition",
                r"Couverture",
                r"Txt IoU",
                r"Temp IoU",
                r"Score",
                r"Tokens",
                r"Run/video",
                r"Contexte/video",
                r"1er passage/video",
            ],
            rows=controlled_gemini_table_rows,
            size=r"\scriptsize",
        ),
    )

    exploratory_context_table_rows = []
    for row in exploratory_context_rows:
        exploratory_context_table_rows.append([
            latex_escape(str(row["context_label"])),
            latex_escape(str(row["best_prompt_label"])),
            latex_escape(str(row["best_model_label"])),
            fmt_int(row["best_processed_samples"]),
            fmt_float(row["best_combined_score"]),
            fmt_int(row["max_processed_samples"]),
        ])
    write_text(
        out_fragments / "table_exploratory_context_runs.tex",
        make_table_block(
            caption=r"Synth\`ese des pilotes exploratoires utilis\'es pour faire \'evoluer la repr\'esentation",
            label="tab:exploratory-context-runs",
            colspec=r">{\raggedright\arraybackslash}p{0.20\textwidth}>{\raggedright\arraybackslash}p{0.20\textwidth}>{\raggedright\arraybackslash}Xrrr",
            headers=[
                r"Contexte",
                r"Prompt pilote",
                r"Mod\`ele pilote",
                r"n pilote",
                r"Score combin\'e",
                r"n max",
            ],
            rows=exploratory_context_table_rows,
            size=r"\footnotesize",
        ),
    )

    exploratory_milestone_table_rows = []
    for row in exploratory_milestones:
        exploratory_milestone_table_rows.append([
            latex_escape(str(row["started_at"]).split("T", 1)[0]),
            latex_escape(str(row["context_label"])),
            latex_escape(str(row["prompt_label"])),
            latex_escape(str(row["model_label"])),
            fmt_int(row["processed_samples"]),
            fmt_float(row["combined_score"]),
        ])
    write_text(
        out_fragments / "table_exploratory_milestones.tex",
        make_table_block(
            caption=r"Jalons o\`u un changement de repr\'esentation ou de prompt am\'eliore le meilleur score exploratoire connu",
            label="tab:exploratory-milestones",
            colspec=r">{\raggedright\arraybackslash}p{0.12\textwidth}>{\raggedright\arraybackslash}p{0.20\textwidth}>{\raggedright\arraybackslash}p{0.20\textwidth}>{\raggedright\arraybackslash}Xrr",
            headers=[r"Date", r"Contexte", r"Prompt", r"Mod\`ele", r"n", r"Score"],
            rows=exploratory_milestone_table_rows,
            size=r"\footnotesize",
        ),
    )

    note_lines = [
        "# Evidence Notes",
        "",
        f"- Dataset: `{dataset['slug']}` with `{dataset['sample_count']}` samples.",
        f"- Source segment duration: mean `{float(video_stats['avg_duration_sec']):.1f}` s, min `{float(video_stats['min_duration_sec']):.1f}` s, max `{float(video_stats['max_duration_sec']):.1f}` s.",
        f"- Ground-truth clip duration: mean `{float(gt_stats['avg_gt_duration_sec']):.1f}` s, min `{float(gt_stats['min_gt_duration_sec']):.1f}` s, max `{float(gt_stats['max_gt_duration_sec']):.1f}` s.",
        f"- Active VLM template `{ACTIVE_VLM_TEMPLATE}` covers `{vlm_stats['video_count']}` videos with `{float(vlm_stats['avg_frames']):.1f}` average frame descriptions.",
        f"- Run inventory: `{run_inventory['total_runs']}` total, `{run_inventory['runs_29']}` full-29, `{run_inventory['runs_5']}` runs on 5 samples, `{run_inventory['runs_1']}` runs on 1 sample.",
        f"- Best full structured run: `{best_structured['run_name']}` (`{best_structured['mean_combined_score']:.3f}`).",
        f"- Full direct-video baseline: `{direct_video['run_name']}` (`{direct_video['mean_combined_score']:.3f}`).",
        f"- Controlled Gemini ablation: `with VLM = {float(controlled_gemini_rows[0]['combined_score']):.3f}`; "
        f"`no-VLM = {float(controlled_gemini_rows[1]['combined_score']):.3f}`; "
        f"`transcript-only = {float(controlled_gemini_rows[2]['combined_score']):.3f}`; "
        f"`direct video = {float(controlled_gemini_rows[3]['combined_score']):.3f}`.",
        "",
        "## Exploratory Pilot Summary",
        "",
        f"- Pilot runs were used to compare representations cheaply before the full `{dataset['sample_count']}`-sample evaluation.",
        f"- Pilot evidence is summarized in `source/tableaux_et_figures/table_exploratory_context_runs.tex`.",
        "",
        "| Context | Best pilot prompt | Best pilot model | Pilot n | Best combined | Max n |",
        "| --- | --- | --- | ---: | ---: | ---: |",
    ]
    for row in exploratory_context_rows:
        note_lines.append(
            f"| `{row['context_label']}` | `{row['best_prompt_label']}` | `{row['best_model_label']}` | "
            f"{int(row['best_processed_samples'])} | {float(row['best_combined_score']):.3f} | {int(row['max_processed_samples'])} |"
        )
    note_lines.extend(
        [
            "",
            "## Exploratory Milestones",
            "",
        ]
    )
    for row in exploratory_milestones:
        note_lines.append(
            f"- `{row['started_at'].split('T', 1)[0]}`: `{row['context_label']}` with `{row['prompt_label']}` "
            f"reached `{float(row['combined_score']):.3f}` on `{int(row['processed_samples'])}` samples "
            f"(delta `{float(row['delta_vs_previous_best']):.3f}`)."
        )
    note_lines.extend(
        [
            "",
        "## Best Structured Run: Top 5",
        "",
        ]
    )
    for row in top_examples:
        note_lines.append(
            f"- `{row['sample_key']}`: combined `{float(row['combined_score']):.3f}`, "
            f"text `{float(row['text_iou']):.3f}`, temporal `{float(row['temporal_iou']):.3f}`"
        )
    note_lines.extend(["", "## Best Structured Run: Bottom 5", ""])
    for row in bottom_examples:
        note_lines.append(
            f"- `{row['sample_key']}`: combined `{float(row['combined_score']):.3f}`, "
            f"text `{float(row['text_iou']):.3f}`, temporal `{float(row['temporal_iou']):.3f}`"
        )
    write_text(out_notes / "evidence_notes.md", "\n".join(note_lines) + "\n")

    con.close()


if __name__ == "__main__":
    main()
