# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Data Quality: Schema Checks
# MAGIC
# MAGIC Validates that important Silver and Gold tables contain expected columns.

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
    {"table": f"{catalog}.silver.sil_customers", "columns": ["customer_id", "email", "signup_date", "status"]},
    {"table": f"{catalog}.silver.sil_orders", "columns": ["order_id", "customer_id", "order_date", "order_total"]},
    {"table": f"{catalog}.gold.fact_sales", "columns": ["sales_line_id", "customer_key", "product_key", "sales_amount"]},
]

results = []

for rule in rules:
    table_name = rule["table"]
    expected_columns = set(rule["columns"])
    actual_columns = set(spark.table(table_name).columns)
    missing_columns = sorted(expected_columns - actual_columns)
    results.append(
        {
            "run_id": run_id,
            "layer": table_name.split(".")[-2],
            "table_name": table_name,
            "rule_name": "expected_columns_present",
            "rule_type": "schema",
            "status": "PASS" if not missing_columns else "FAIL",
            "failed_count": len(missing_columns),
            "details": ",".join(missing_columns),
        }
    )

result_df = spark.createDataFrame(results).withColumn("checked_utc", F.current_timestamp())
result_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(f"{catalog}.dq.dq_results")

display(result_df)

if result_df.filter(F.col("status") == "FAIL").count() > 0:
    raise ValueError("Schema data quality checks failed.")

