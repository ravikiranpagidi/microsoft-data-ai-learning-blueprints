# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Payments
# MAGIC
# MAGIC Cleans payment data and standardizes payment status and method names.

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

bronze_df = spark.table(f"{catalog}.bronze.brz_payments")

silver_df = (
    bronze_df.select(
        F.trim("payment_id").alias("payment_id"),
        F.trim("order_id").alias("order_id"),
        F.to_date("payment_date").alias("payment_date"),
        F.initcap(F.trim("payment_method")).alias("payment_method"),
        F.initcap(F.trim("payment_status")).alias("payment_status"),
        F.col("payment_amount").cast("decimal(12,2)").alias("payment_amount"),
        F.upper(F.trim("currency")).alias("currency"),
        F.col("_ingestion_utc"),
        F.col("_batch_id"),
    )
    .filter(F.col("payment_id").isNotNull())
    .filter(F.col("order_id").isNotNull())
    .filter(F.col("payment_amount") >= 0)
    .dropDuplicates(["payment_id"])
    .withColumn("is_captured", F.col("payment_status") == F.lit("Captured"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

row_count = silver_df.count()
if row_count == 0:
    raise ValueError("Payment Silver transformation produced zero rows.")

silver_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_payments")
print(f"Silver payments: {row_count:,}")

