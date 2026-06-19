# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Gold Model: customer_360
# MAGIC
# MAGIC Builds an analytics table that summarizes sales and engagement by customer.

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

dim_customer = spark.table(f"{catalog}.gold.dim_customer")
fact_sales = spark.table(f"{catalog}.gold.fact_sales")
web_activity = spark.table(f"{catalog}.silver.sil_web_activity")

sales_summary = (
    fact_sales.groupBy("customer_key", "customer_id")
    .agg(
        F.countDistinct("order_id").alias("order_count"),
        F.sum("quantity").alias("units_sold"),
        F.sum("sales_amount").alias("total_sales_amount"),
        F.avg("sales_amount").alias("avg_line_sales_amount"),
        F.max("order_date").alias("last_order_date"),
    )
)

web_summary = (
    web_activity.groupBy("customer_id")
    .agg(
        F.count("*").alias("web_event_count"),
        F.countDistinct("session_id").alias("web_session_count"),
        F.max("event_timestamp").alias("last_web_event_timestamp"),
    )
)

customer_360 = (
    dim_customer.join(sales_summary, ["customer_key", "customer_id"], "left")
    .join(web_summary, "customer_id", "left")
    .fillna({"order_count": 0, "units_sold": 0, "total_sales_amount": 0, "web_event_count": 0, "web_session_count": 0})
    .withColumn("gold_processed_utc", F.current_timestamp())
)

customer_360.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.gold.customer_360")
print(f"customer_360 rows: {customer_360.count():,}")

