# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Silver Transformation: Orders And Order Items
# MAGIC
# MAGIC Cleans order headers and line items, validates basic amounts, and writes `sil_orders` and `sil_order_items`.

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

orders_bronze = spark.table(f"{catalog}.bronze.brz_orders")
items_bronze = spark.table(f"{catalog}.bronze.brz_order_items")

orders_silver = (
    orders_bronze.select(
        F.trim("order_id").alias("order_id"),
        F.trim("customer_id").alias("customer_id"),
        F.to_date("order_date").alias("order_date"),
        F.initcap(F.trim("order_status")).alias("order_status"),
        F.initcap(F.trim("channel")).alias("channel"),
        F.upper(F.trim("store_id")).alias("store_id"),
        F.col("order_total").cast("decimal(12,2)").alias("order_total"),
        F.upper(F.trim("currency")).alias("currency"),
        F.col("_ingestion_utc"),
        F.col("_batch_id"),
    )
    .filter(F.col("order_id").isNotNull())
    .filter(F.col("customer_id").isNotNull())
    .filter(F.col("order_total") >= 0)
    .dropDuplicates(["order_id"])
    .withColumn("is_completed", F.col("order_status") == F.lit("Completed"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

items_silver = (
    items_bronze.select(
        F.trim("order_item_id").alias("order_item_id"),
        F.trim("order_id").alias("order_id"),
        F.trim("product_id").alias("product_id"),
        F.col("quantity").cast("int").alias("quantity"),
        F.col("unit_price").cast("decimal(10,2)").alias("unit_price"),
        F.col("discount_amount").cast("decimal(10,2)").alias("discount_amount"),
        F.col("line_total").cast("decimal(12,2)").alias("line_total"),
        F.col("_ingestion_utc"),
        F.col("_batch_id"),
    )
    .filter(F.col("order_item_id").isNotNull())
    .filter(F.col("order_id").isNotNull())
    .filter(F.col("product_id").isNotNull())
    .filter(F.col("quantity") > 0)
    .filter(F.col("line_total") >= 0)
    .dropDuplicates(["order_item_id"])
    .withColumn("calculated_line_total", (F.col("quantity") * F.col("unit_price")) - F.col("discount_amount"))
    .withColumn("silver_processed_utc", F.current_timestamp())
    .withColumn("silver_batch_id", F.lit(batch_id))
)

orders_count = orders_silver.count()
items_count = items_silver.count()

if orders_count == 0 or items_count == 0:
    raise ValueError("Order Silver transformation produced zero rows.")

orders_silver.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_orders")
items_silver.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.silver.sil_order_items")

print(f"Silver orders: {orders_count:,}")
print(f"Silver order items: {items_count:,}")

