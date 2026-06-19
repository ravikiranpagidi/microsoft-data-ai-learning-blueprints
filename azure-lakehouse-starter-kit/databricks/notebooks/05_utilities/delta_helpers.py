# Databricks notebook source
# MAGIC %md
# MAGIC # Delta Helpers
# MAGIC
# MAGIC Utility functions for safe Delta writes and simple optimization patterns.

# COMMAND ----------

from typing import Iterable, Optional


def write_delta_table(df, table_name: str, mode: str = "overwrite", merge_schema: bool = True) -> None:
    writer = df.write.format("delta").mode(mode)
    if merge_schema:
        writer = writer.option("mergeSchema", "true")
    if mode == "overwrite":
        writer = writer.option("overwriteSchema", "true")
    writer.saveAsTable(table_name)


def optimize_delta_table(spark_session, table_name: str, zorder_columns: Optional[Iterable[str]] = None) -> None:
    zorder_columns = list(zorder_columns or [])
    if zorder_columns:
        zorder_expr = ", ".join(zorder_columns)
        spark_session.sql(f"OPTIMIZE {table_name} ZORDER BY ({zorder_expr})")
    else:
        spark_session.sql(f"OPTIMIZE {table_name}")


def vacuum_delta_table(spark_session, table_name: str, retention_hours: int = 168) -> None:
    spark_session.sql(f"VACUUM {table_name} RETAIN {retention_hours} HOURS")
