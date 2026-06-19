# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Products
# MAGIC
# MAGIC Cleans product reference data and prepares it for dimensional modeling.

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

bronze_df = spark.table(f"{catalog}.bronze.brz_products")
source_count = bronze_df.count()

silver_df = (
    bronze_df.select(
        F.trim("product_id").alias("product_id"),
        F.initcap(F.trim("product_name")).alias("product_name"),
        F.initcap(F.trim("category")).alias("category"),
        F.initcap(F.trim("sub_category")).alias("sub_category"),
        F.initcap(F.trim("brand")).alias("brand"),
        F.col("unit_price").cast("decimal(10,2)").alias("unit_price"),
        F.col("is_active").cast("boolean").alias("is_active"),
        F.to_date("effective_date").alias("effective_date"),
        F.col("_ingestion_utc"),
        F.col("_batch_id"),
    )
    .filter(F.col("product_id").isNotNull())
    .filter(F.col("unit_price") >= 0)
    .dropDuplicates(["product_id"])
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

target_count = silver_df.count()
if target_count == 0:
    raise ValueError("Product Silver transformation produced zero rows.")

silver_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_products")

print(f"Source rows: {source_count:,}")
print(f"Silver rows: {target_count:,}")

