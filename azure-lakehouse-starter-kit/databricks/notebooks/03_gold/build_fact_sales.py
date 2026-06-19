# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Gold Model: fact_sales
# MAGIC
# MAGIC Builds a sales fact table at the order-line grain.

# COMMAND ----------

from pyspark.sql import functions as F

try:
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
except Exception:
    pass


def widget(name: str, default: str) -> str:
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


catalog = widget("catalog", "retail_lakehouse_dev")

orders = spark.table(f"{catalog}.silver.sil_orders").alias("o")
items = spark.table(f"{catalog}.silver.sil_order_items").alias("i")
payments = spark.table(f"{catalog}.silver.sil_payments").alias("p")
dim_customer = spark.table(f"{catalog}.gold.dim_customer").alias("dc")
dim_product = spark.table(f"{catalog}.gold.dim_product").alias("dp")

fact_sales = (
    items.join(orders, "order_id", "inner")
    .join(payments.select("order_id", "payment_method", "payment_status", "is_captured"), "order_id", "left")
    .join(dim_customer.select("customer_key", "customer_id"), "customer_id", "left")
    .join(dim_product.select("product_key", "product_id"), "product_id", "left")
    .select(
        F.col("order_item_id").alias("sales_line_id"),
        "order_id",
        "customer_key",
        "product_key",
        "customer_id",
        "product_id",
        "order_date",
        "channel",
        "store_id",
        "order_status",
        "payment_method",
        "payment_status",
        "is_completed",
        "is_captured",
        "quantity",
        "unit_price",
        "discount_amount",
        "line_total",
        "order_total",
    )
    .withColumn("sales_amount", F.when(F.col("is_completed"), F.col("line_total")).otherwise(F.lit(0).cast("decimal(12,2)")))
    .withColumn("order_year_month", F.date_format("order_date", "yyyy-MM"))
    .withColumn("gold_processed_utc", F.current_timestamp())
)

if fact_sales.filter(F.col("customer_key").isNull()).count() > 0:
    raise ValueError("fact_sales has rows without customer_key. Check customer referential integrity.")

if fact_sales.filter(F.col("product_key").isNull()).count() > 0:
    raise ValueError("fact_sales has rows without product_key. Check product referential integrity.")

fact_sales.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.gold.fact_sales")
print(f"fact_sales rows: {fact_sales.count():,}")

