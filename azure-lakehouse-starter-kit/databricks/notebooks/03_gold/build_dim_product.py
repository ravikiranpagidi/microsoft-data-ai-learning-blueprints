# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Gold Model: dim_product
# MAGIC
# MAGIC Builds a conformed product dimension for sales, inventory, and web activity analysis.

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
products = spark.table(f"{catalog}.silver.sil_products")

dim_product = (
    products.select(
        "product_id",
        "product_name",
        "category",
        "sub_category",
        "brand",
        "unit_price",
        "is_active",
        "effective_date",
    )
    .dropDuplicates(["product_id"])
    .withColumn("product_key", F.row_number().over(Window.orderBy("product_id")))
    .withColumn("gold_processed_utc", F.current_timestamp())
)

dim_product.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{catalog}.gold.dim_product")
print(f"dim_product rows: {dim_product.count():,}")

