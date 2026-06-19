# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Inventory
# MAGIC
# MAGIC Cleans inventory snapshots and adds a simple low-stock indicator.

# COMMAND ----------

from pyspark.sql import functions as F

try:
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
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
batch_id = widget("batch_id", "manual")

bronze_df = spark.table(f"{catalog}.bronze.brz_inventory")

silver_df = (
    bronze_df.select(
        F.trim("inventory_id").alias("inventory_id"),
        F.trim("product_id").alias("product_id"),
        F.upper(F.trim("store_id")).alias("store_id"),
        F.to_date("inventory_date").alias("inventory_date"),
        F.col("on_hand_quantity").cast("int").alias("on_hand_quantity"),
        F.col("reorder_level").cast("int").alias("reorder_level"),
        F.initcap(F.trim("supplier_name")).alias("supplier_name"),
    )
    .filter(F.col("inventory_id").isNotNull())
    .filter(F.col("product_id").isNotNull())
    .filter(F.col("on_hand_quantity") >= 0)
    .dropDuplicates(["inventory_id"])
    .withColumn("is_below_reorder_level", F.col("on_hand_quantity") <= F.col("reorder_level"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

silver_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_inventory")
print(f"Silver inventory: {silver_df.count():,}")

