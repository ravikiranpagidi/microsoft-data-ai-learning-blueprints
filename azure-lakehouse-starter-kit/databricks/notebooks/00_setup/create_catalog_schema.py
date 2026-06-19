# Databricks notebook source
# MAGIC %md
# MAGIC # 00 - Create Catalog And Schemas
# MAGIC
# MAGIC **Purpose:** Create Unity Catalog objects for the Retail Customer Analytics lakehouse.
# MAGIC
# MAGIC **Concepts covered:**
# MAGIC - Catalog and schema separation by environment
# MAGIC - Bronze, Silver, Gold, and DQ schemas
# MAGIC - Idempotent setup
# MAGIC
# MAGIC **Prerequisites:**
# MAGIC - Unity Catalog enabled workspace
# MAGIC - Permission to create catalog and schemas
# MAGIC - Storage credentials and external locations already approved by your platform team

# COMMAND ----------

try:
    dbutils.widgets.text("environment", "dev")  # type: ignore[name-defined]
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
except Exception:
    pass


def get_widget(name: str, default: str) -> str:
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


environment = get_widget("environment", "dev")
catalog = get_widget("catalog", f"retail_lakehouse_{environment}")

schemas = ["bronze", "silver", "gold", "dq", "ops"]

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
spark.sql(f"USE CATALOG {catalog}")

for schema_name in schemas:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema_name}")
    print(f"Ensured schema: {catalog}.{schema_name}")

spark.sql(
    f"""
    CREATE TABLE IF NOT EXISTS {catalog}.ops.pipeline_run_audit
    (
        run_id STRING,
        pipeline_name STRING,
        layer STRING,
        entity_name STRING,
        status STRING,
        row_count BIGINT,
        message STRING,
        started_utc TIMESTAMP,
        ended_utc TIMESTAMP
    )
    USING DELTA
    """
)

spark.sql(
    f"""
    CREATE TABLE IF NOT EXISTS {catalog}.dq.dq_results
    (
        run_id STRING,
        layer STRING,
        table_name STRING,
        rule_name STRING,
        rule_type STRING,
        status STRING,
        failed_count BIGINT,
        checked_utc TIMESTAMP,
        details STRING
    )
    USING DELTA
    """
)

print(f"Catalog setup completed for {catalog}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Expected Output
# MAGIC
# MAGIC The notebook creates:
# MAGIC
# MAGIC - `bronze` schema for raw Delta tables
# MAGIC - `silver` schema for cleaned Delta tables
# MAGIC - `gold` schema for dimensional and customer analytics tables
# MAGIC - `dq` schema for data quality results
# MAGIC - `ops` schema for pipeline audit information

