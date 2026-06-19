# Databricks notebook source
# MAGIC %md
# MAGIC # Logging Utilities
# MAGIC
# MAGIC Small logging helpers used by the starter notebooks. Production implementations often write to a control table, Azure Monitor, or a centralized observability platform.

# COMMAND ----------

from datetime import datetime, timezone
from typing import Any, Dict


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def log_step(message: str) -> None:
    print(f"[{utc_now_iso()}] {message}")


def log_count(label: str, row_count: int) -> None:
    log_step(f"{label}: {row_count:,} rows")


def write_audit_event(spark_session: Any, table_name: str, event: Dict[str, Any]) -> None:
    rows = [{**event, "audit_utc": utc_now_iso()}]
    df = spark_session.createDataFrame(rows)
    df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(table_name)
