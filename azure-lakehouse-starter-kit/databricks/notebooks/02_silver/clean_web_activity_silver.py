# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Web Activity
# MAGIC
# MAGIC Cleans clickstream-style JSON events and prepares them for customer journey analysis.

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

bronze_df = spark.table(f"{catalog}.bronze.brz_web_activity")

silver_df = (
    bronze_df.select(
        F.trim("event_id").alias("event_id"),
        F.trim("customer_id").alias("customer_id"),
        F.to_timestamp("event_timestamp").alias("event_timestamp"),
        F.lower(F.trim("event_type")).alias("event_type"),
        F.trim("product_id").alias("product_id"),
        F.trim("session_id").alias("session_id"),
        F.lower(F.trim("device_type")).alias("device_type"),
        F.lower(F.trim("traffic_source")).alias("traffic_source"),
    )
    .filter(F.col("event_id").isNotNull())
    .filter(F.col("event_timestamp").isNotNull())
    .dropDuplicates(["event_id"])
    .withColumn("event_date", F.to_date("event_timestamp"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

silver_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_web_activity")
print(f"Silver web activity: {silver_df.count():,}")

