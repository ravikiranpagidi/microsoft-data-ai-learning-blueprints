# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Gold Model: dim_customer
# MAGIC
# MAGIC Builds a business-friendly customer dimension with a surrogate key.

# COMMAND ----------

from pyspark.sql import Window
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
customers = spark.table(f"{catalog}.silver.sil_customers")

window_spec = Window.orderBy("customer_id")

dim_customer = (
    customers.select(
        "customer_id",
        "first_name",
        "last_name",
        F.concat_ws(" ", "first_name", "last_name").alias("customer_name"),
        "email",
        "phone_digits",
        "loyalty_tier",
        "customer_segment",
        "signup_date",
        "status",
        "is_active",
        "state",
        "country",
    )
    .dropDuplicates(["customer_id"])
    .withColumn("customer_key", F.row_number().over(window_spec))
    .withColumn("gold_processed_utc", F.current_timestamp())
)

dim_customer.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.gold.dim_customer")
print(f"dim_customer rows: {dim_customer.count():,}")

