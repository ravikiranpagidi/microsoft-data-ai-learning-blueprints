# Databricks notebook source
# MAGIC %md
# MAGIC # 04 - Data Quality: Referential Integrity Checks
# MAGIC
# MAGIC Validates that child records have matching parent records before Gold consumption.

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

checks = [
    {
        "name": "orders_have_valid_customer",
        "child_table": f"{catalog}.silver.sil_orders",
        "parent_table": f"{catalog}.silver.sil_customers",
        "child_key": "customer_id",
        "parent_key": "customer_id",
    },
    {
        "name": "order_items_have_valid_product",
        "child_table": f"{catalog}.silver.sil_order_items",
        "parent_table": f"{catalog}.silver.sil_products",
        "child_key": "product_id",
        "parent_key": "product_id",
    },
    {
        "name": "payments_have_valid_order",
        "child_table": f"{catalog}.silver.sil_payments",
        "parent_table": f"{catalog}.silver.sil_orders",
        "child_key": "order_id",
        "parent_key": "order_id",
    },
]

results = []

for check in checks:
    child = spark.table(check["child_table"]).alias("child")
    parent = spark.table(check["parent_table"]).alias("parent")
    failed_count = (
        child.join(parent, F.col(f"child.{check['child_key']}") == F.col(f"parent.{check['parent_key']}"), "left_anti")
        .count()
    )
    results.append(
        {
            "run_id": run_id,
            "layer": "silver",
            "table_name": check["child_table"],
            "rule_name": check["name"],
            "rule_type": "referential_integrity",
            "status": "PASS" if failed_count == 0 else "FAIL",
            "failed_count": failed_count,
            "details": f"{check['child_key']} must exist in {check['parent_table']}.{check['parent_key']}",
        }
    )

result_df = spark.createDataFrame(results).withColumn("checked_utc", F.current_timestamp())
result_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable(f"{catalog}.dq.dq_results")
display(result_df)

if result_df.filter(F.col("status") == "FAIL").count() > 0:
    raise ValueError("Referential integrity checks failed.")

