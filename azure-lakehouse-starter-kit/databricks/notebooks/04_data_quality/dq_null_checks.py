# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Data Quality: Not Null Checks
# MAGIC
# MAGIC Checks required business keys and metric columns for null values.

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
    {"table": f"{catalog}.silver.sil_customers", "column": "customer_id"},
    {"table": f"{catalog}.silver.sil_products", "column": "product_id"},
    {"table": f"{catalog}.silver.sil_orders", "column": "order_id"},
    {"table": f"{catalog}.silver.sil_order_items", "column": "order_item_id"},
    {"table": f"{catalog}.gold.fact_sales", "column": "sales_line_id"},
]

results = []

for rule in rules:
    table_name = rule["table"]
    column_name = rule["column"]
    failed_count = spark.table(table_name).filter(F.col(column_name).isNull()).count()
    results.append(
        {
            "run_id": run_id,
            "layer": table_name.split(".")[-2],
            "table_name": table_name,
            "rule_name": f"{column_name}_not_null",
            "rule_type": "not_null",
            "status": "PASS" if failed_count == 0 else "FAIL",
            "failed_count": failed_count,
            "details": f"Null check for {column_name}",
        }
    )

result_df = spark.createDataFrame(results).withColumn("checked_utc", F.current_timestamp())
result_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(f"{catalog}.dq.dq_results")
display(result_df)

if result_df.filter(F.col("status") == "FAIL").count() > 0:
    raise ValueError("Not null data quality checks failed.")

