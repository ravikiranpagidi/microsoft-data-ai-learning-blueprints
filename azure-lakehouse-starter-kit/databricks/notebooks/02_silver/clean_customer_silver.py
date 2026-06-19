# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Customers
# MAGIC
# MAGIC **Purpose:** Clean customer data, standardize values, cast dates, remove duplicates, and create a trusted Silver Delta table.

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

source_table = f"{catalog}.bronze.brz_customers"
target_table = f"{catalog}.silver.sil_customers"

bronze_df = spark.table(source_table)
source_count = bronze_df.count()

silver_df = (
    bronze_df.select(
        F.trim(F.col("customer_id")).alias("customer_id"),
        F.initcap(F.trim(F.col("first_name"))).alias("first_name"),
        F.initcap(F.trim(F.col("last_name"))).alias("last_name"),
        F.lower(F.trim(F.col("email"))).alias("email"),
        F.regexp_replace(F.col("phone"), "[^0-9]", "").alias("phone_digits"),
        F.initcap(F.trim(F.col("loyalty_tier"))).alias("loyalty_tier"),
        F.initcap(F.trim(F.col("customer_segment"))).alias("customer_segment"),
        F.to_date("signup_date").alias("signup_date"),
        F.initcap(F.trim(F.col("status"))).alias("status"),
        F.upper(F.trim(F.col("state"))).alias("state"),
        F.upper(F.trim(F.col("country"))).alias("country"),
        F.col("_ingestion_utc"),
        F.col("_batch_id"),
    )
    .filter(F.col("customer_id").isNotNull())
    .dropDuplicates(["customer_id"])
    .withColumn("is_active", F.col("status") == F.lit("Active"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

target_count = silver_df.count()

if target_count == 0:
    raise ValueError("Customer Silver transformation produced zero rows.")

silver_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(target_table)

print(f"Source rows: {source_count:,}")
print(f"Silver rows: {target_count:,}")
print(f"Wrote {target_table}")

