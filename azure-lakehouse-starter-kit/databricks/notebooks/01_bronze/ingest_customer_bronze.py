# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Bronze Ingestion: Customers
# MAGIC
# MAGIC **Purpose:** Read raw customer CSV files from ADLS Gen2 or a Unity Catalog volume, add ingestion metadata, and append to a Bronze Delta table.

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

source_path = f"{raw_base_path}/customers"
target_table = f"{catalog}.bronze.brz_customers"

print(f"Reading customers from {source_path}")

raw_df = (
    spark.read.option("header", "true")
    .option("inferSchema", "false")
    .csv(source_path)
)

bronze_df = (
    raw_df.withColumn("_ingestion_utc", F.current_timestamp())
    .withColumn("_source_file_name", F.input_file_name())
    .withColumn("_batch_id", F.lit(batch_id))
)

row_count = bronze_df.count()
bronze_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(target_table)

print(f"Wrote {row_count:,} rows to {target_table}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Expected Output
# MAGIC
# MAGIC A Bronze table named `brz_customers` that preserves the source shape and adds `_ingestion_utc`, `_source_file_name`, and `_batch_id`.

