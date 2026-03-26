#!/usr/bin/env python3
from __future__ import annotations

import sqlite3
from pathlib import Path


MEMOIRE_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = MEMOIRE_ROOT / "data" / "test_llms.db"
SQL_PATH = Path(__file__).resolve().with_name("test_llms_report_views.sql")


def main() -> None:
    con = sqlite3.connect(DB_PATH)
    try:
        sql = SQL_PATH.read_text(encoding="utf-8")
        con.executescript(sql)
        con.commit()

        views = con.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'view' AND name LIKE 'report_llm_%'
            ORDER BY name
            """
        ).fetchall()
        summary = con.execute(
            """
            SELECT
              tracked_items,
              validation_items,
              tracked_videos,
              validation_videos,
              fine_tuning_investment_usd
            FROM report_llm_campaign_summary_v1
            """
        ).fetchone()

        print(f"[refresh-test-llms-reporting] db={DB_PATH}")
        print(f"[refresh-test-llms-reporting] report views={len(views)}")
        for (name,) in views:
            print(f"  - {name}")
        if summary is not None:
            print(
                "[refresh-test-llms-reporting] "
                f"tracked_items={summary[0]} validation_items={summary[1]} "
                f"tracked_videos={summary[2]} validation_videos={summary[3]} "
                f"fine_tuning_investment_usd={summary[4]:.0f}"
            )
    finally:
        con.close()


if __name__ == "__main__":
    main()
