# Databricks notebook source
# MAGIC %md
# MAGIC # Configuration Loader
# MAGIC
# MAGIC Shared helper functions for Azure Lakehouse notebooks. In Databricks, values should normally come from widgets, job parameters, secret scopes, or environment-specific configuration tables.

# COMMAND ----------

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class LakehouseConfig:
    catalog: str
    bronze_schema: str
    silver_schema: str
    gold_schema: str
    dq_schema: str
    raw_base_path: str
    checkpoint_base_path: str
    environment: str


def get_widget_or_default(name: str, default: str) -> str:
    """Return a Databricks widget value when available, otherwise return a default."""
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


def load_config(overrides: Optional[Dict[str, str]] = None) -> LakehouseConfig:
    overrides = overrides or {}
    environment = overrides.get("environment") or get_widget_or_default("environment", "dev")
    catalog = overrides.get("catalog") or get_widget_or_default("catalog", f"retail_lakehouse_{environment}")

    return LakehouseConfig(
        catalog=catalog,
        bronze_schema=overrides.get("bronze_schema", "bronze"),
        silver_schema=overrides.get("silver_schema", "silver"),
        gold_schema=overrides.get("gold_schema", "gold"),
        dq_schema=overrides.get("dq_schema", "dq"),
        raw_base_path=overrides.get("raw_base_path")
        or get_widget_or_default("raw_base_path", f"/Volumes/{catalog}/raw/source_files/retail"),
        checkpoint_base_path=overrides.get("checkpoint_base_path")
        or get_widget_or_default("checkpoint_base_path", f"/Volumes/{catalog}/logs/checkpoints"),
        environment=environment,
    )


def qualified_table(config: LakehouseConfig, layer: str, table_name: str) -> str:
    schema_map = {
        "bronze": config.bronze_schema,
        "silver": config.silver_schema,
        "gold": config.gold_schema,
        "dq": config.dq_schema,
    }
    return f"{config.catalog}.{schema_map[layer]}.{table_name}"
