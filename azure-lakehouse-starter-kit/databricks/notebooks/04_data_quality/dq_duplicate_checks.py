# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Data Quality: Duplicate Checks
# MAGIC
# MAGIC Validates that important keys remain unique after Silver and Gold transformations.

# COMMAND ----------

from pyspark.sql import functions as F

try:
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
    dbutils.widgets.text("run_id", "manual")
except Exception:
    pass


def widget(name: str, default: str) -> str:
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


catalog = widget("catalog", "retail_lakehouse_dev")
run_id = widget("run_id", "manual")

rules = [
    {"table": f"{catalog}.silver.sil_customers", "keys": ["customer_id"]},
    {"table": f"{catalog}.silver.sil_products", "keys": ["product_id"]},
    {"table": f"{catalog}.silver.sil_orders", "keys": ["order_id"]},
    {"table": f"{catalog}.silver.sil_order_items", "keys": ["order_item_id"]},
    {"table": f"{catalog}.gold.fact_sales", "keys": ["sales_line_id"]},
]

results = []

for rule in rules:
    table_name = rule["table"]
    keys = rule["keys"]
    duplicate_count = spark.table(table_name).groupBy(*keys).count().filter(F.col("count") > 1).count()
    results.append(
        {
            "run_id": run_id,
            "layer": table_name.split(".")[-2],
            "table_name": table_name,
            "rule_name": "_".join(keys) + "_unique",
            "rule_type": "duplicate",
            "status": "PASS" if duplicate_count == 0 else "FAIL",
            "failed_count": duplicate_count,
            "details": f"Duplicate groups for keys: {','.join(keys)}",
        }
    )

result_df = spark.createDataFrame(results).withColumn("checked_utc", F.current_timestamp())
result_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(f"{catalog}.dq.dq_results")
display(result_df)

if result_df.filter(F.col("status") == "FAIL").count() > 0:
    raise ValueError("Duplicate data quality checks failed.")

