#!/usr/bin/env python3
from __future__ import annotations

import sqlite3
from pathlib import Path


MEMOIRE_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = MEMOIRE_ROOT / "data" / "test_llms.db"
TABLES_AND_FIGURES_DIR = MEMOIRE_ROOT / "source" / "tableaux_et_figures"


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
    out_notes = MEMOIRE_ROOT / "generated" / "notes"
    out_fragments = TABLES_AND_FIGURES_DIR

    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    summary = cur.execute("SELECT * FROM report_llm_campaign_summary_v1").fetchone()
    small_finetuning = [dict(row) for row in cur.execute("SELECT * FROM report_llm_small_finetuning_v1").fetchall()]
    object_aug = [dict(row) for row in cur.execute("SELECT * FROM report_llm_object_augmentation_v1").fetchall()]
    pro_variants = [dict(row) for row in cur.execute("SELECT * FROM report_llm_pro_variants_v1").fetchall()]

    small_rows = [
        [
            latex_escape(row["variant_label"]),
            fmt_int(row["total_validations"]),
            fmt_float(row["average_iou"]),
            fmt_float(row["delta_iou_vs_base"]),
            fmt_float(float(row["avg_response_time_ms"]) / 1000.0, 1),
            fmt_float(row["cost_per_100_videos"], 3),
        ]
        for row in small_finetuning
    ]
    write_text(
        out_fragments / "table_llm_small_finetuning.tex",
        make_table_block(
            caption=r"Impact du fine-tuning sur les petites variantes Gemini 2.5, avec les m\^emes 29 cas de validation lorsqu'ils sont disponibles",
            label="tab:llm-small-finetuning",
            colspec=r">{\raggedright\arraybackslash}Xrrrrr",
            headers=[r"Variante", r"n", r"IoU moy.", r"$\Delta$ vs base", r"Temps (s)", r"Co\^ut / 100 vid."],
            rows=small_rows,
        ),
    )

    object_rows = [
        [
            latex_escape(row["variant_label"]),
            fmt_int(row["test_count"]),
            fmt_float(row["avg_iou_score"]),
            fmt_float(row["delta_iou_vs_plain"]),
            fmt_int(round(float(row["avg_input_length"]))),
            fmt_float(float(row["avg_response_time_ms"]) / 1000.0, 1),
        ]
        for row in object_aug
    ]
    write_text(
        out_fragments / "table_llm_object_augmentation.tex",
        make_table_block(
            caption=r"Premiers essais d'augmentation visuelle par objets dans le contexte textuel",
            label="tab:llm-object-augmentation",
            colspec=r">{\raggedright\arraybackslash}Xrrrrr",
            headers=[r"Variante", r"n", r"IoU moy.", r"$\Delta$ vs texte", r"Car. entr\'ee", r"Temps (s)"],
            rows=object_rows,
        ),
    )

    pro_rows = [
        [
            latex_escape(row["variant_label"]),
            fmt_int(row["total_validations"]),
            fmt_float(row["average_iou"]),
            fmt_float(row["delta_iou_vs_base"]),
            fmt_float(float(row["avg_response_time_ms"]) / 1000.0, 1),
            fmt_float(row["cost_per_100_videos"], 3) if row["cost_per_100_videos"] is not None else latex_escape(row["cost_note"]),
        ]
        for row in pro_variants
    ]
    write_text(
        out_fragments / "table_llm_pro_variants.tex",
        make_table_block(
            caption=r"Comparaison des variantes Gemini 2.5 Pro: base, fine-tuning et entr\'ee vid\'eo directe",
            label="tab:llm-pro-variants",
            colspec=r">{\raggedright\arraybackslash}Xrrrrr",
            headers=[r"Variante", r"n", r"IoU moy.", r"$\Delta$ vs base", r"Temps (s)", r"Co\^ut / 100 vid."],
            rows=pro_rows,
        ),
    )

    flash_base = next(row for row in small_finetuning if row["model_name"] == "google/gemini-2.5-flash")
    flash_ft = next(row for row in small_finetuning if row["model_name"] == "gemini-2.5-flash_text")
    flash_lite_base = next(row for row in small_finetuning if row["model_name"] == "google/gemini-2.5-flash-lite")
    flash_lite_ft = next(row for row in small_finetuning if row["model_name"] == "gemini-2.5-flash-lite_text")
    obj_plain = next(row for row in object_aug if row["input_type"] == "plain")
    obj_diff = next(row for row in object_aug if row["input_type"] == "diff_7s")
    obj_full = next(row for row in object_aug if row["input_type"] == "full_7s")
    pro_base = next(row for row in pro_variants if row["model_name"] == "google/gemini-2.5-pro")
    pro_text = next(row for row in pro_variants if row["model_name"] == "gemini-2.5_pro_text")
    pro_objects = next(row for row in pro_variants if row["model_name"] == "gemini-2.5_pro_objects")
    pro_video = next(row for row in pro_variants if row["model_name"] == "gemini-2.5_pro_video")

    evidence_md = [
        "# LLM Campaign Notes",
        "",
        f"- Tracked items: `{int(summary['tracked_items'])}`; validation items: `{int(summary['validation_items'])}`; tracked videos: `{int(summary['tracked_videos'])}`.",
        f"- Upfront fine-tuning investment reported by the project: `${float(summary['fine_tuning_investment_usd']):.0f}`.",
        f"- Gemini 2.5 Flash: `{float(flash_base['average_iou']):.3f}` -> `{float(flash_ft['average_iou']):.3f}` after text fine-tuning (`{float(flash_ft['delta_iou_vs_base']):+.3f}`).",
        f"- Gemini 2.5 Flash-Lite: `{float(flash_lite_base['average_iou']):.3f}` -> `{float(flash_lite_ft['average_iou']):.3f}` after text fine-tuning (`{float(flash_lite_ft['delta_iou_vs_base']):+.3f}`).",
        f"- Object augmentation: `plain={float(obj_plain['avg_iou_score']):.3f}`, `diff_7s={float(obj_diff['avg_iou_score']):.3f}`, `full_7s={float(obj_full['avg_iou_score']):.3f}`.",
        f"- Gemini 2.5 Pro: `base={float(pro_base['average_iou']):.3f}`, `ft_text={float(pro_text['average_iou']):.3f}`, `ft_objects={float(pro_objects['average_iou']):.3f}`, `video={float(pro_video['average_iou']):.3f}`.",
    ]
    write_text(out_notes / "llm_campaign_notes.md", "\n".join(evidence_md) + "\n")

    con.close()


if __name__ == "__main__":
    main()
