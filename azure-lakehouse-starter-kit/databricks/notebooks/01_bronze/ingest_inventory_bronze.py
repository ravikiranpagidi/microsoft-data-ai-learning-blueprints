# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Bronze Ingestion: Inventory
# MAGIC
# MAGIC Ingests inventory snapshots into Bronze Delta.

# COMMAND ----------

from pyspark.sql import functions as F

try:
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
    dbutils.widgets.text("raw_base_path", "/Volumes/retail_lakehouse_dev/raw/source_files/retail")
    dbutils.widgets.text("batch_id", "manual")
except Exception:
    pass


def widget(name: str, default: str) -> str:
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


catalog = widget("catalog", "retail_lakehouse_dev")
raw_base_path = widget("raw_base_path", "/Volumes/retail_lakehouse_dev/raw/source_files/retail")
batch_id = widget("batch_id", "manual")

raw_df = spark.read.option("header", "true").option("inferSchema", "false").csv(f"{raw_base_path}/inventory")
bronze_df = (
    raw_df.withColumn("_ingestion_utc", F.current_timestamp())
    .withColumn("_source_file_name", F.input_file_name())
    .withColumn("_batch_id", F.lit(batch_id))
)

row_count = bronze_df.count()
bronze_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(f"{catalog}.bronze.brz_inventory")
print(f"Wrote {row_count:,} inventory rows")

