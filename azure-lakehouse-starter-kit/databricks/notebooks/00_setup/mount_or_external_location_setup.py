# Databricks notebook source
# MAGIC %md
# MAGIC # 00 - Storage Access Setup Notes
# MAGIC
# MAGIC **Purpose:** Document the recommended storage access pattern for the starter kit.
# MAGIC
# MAGIC For new Azure Databricks implementations, prefer Unity Catalog external locations and volumes over legacy mounts. Mount examples are intentionally not used as the primary pattern because they are harder to govern consistently.

# COMMAND ----------

try:
    dbutils.widgets.text("catalog", "retail_lakehouse_dev")  # type: ignore[name-defined]
    dbutils.widgets.text("storage_credential", "<storage-credential-name>")  # type: ignore[name-defined]
    dbutils.widgets.text("storage_account", "<storage-account-name>")  # type: ignore[name-defined]
except Exception:
    pass


def get_widget(name: str, default: str) -> str:
    try:
        value = dbutils.widgets.get(name)  # type: ignore[name-defined]
        return value if value else default
    except Exception:
        return default


catalog = get_widget("catalog", "retail_lakehouse_dev")
storage_credential = get_widget("storage_credential", "<storage-credential-name>")
storage_account = get_widget("storage_account", "<storage-account-name>")

print("Recommended Unity Catalog setup commands:")
print(
    f"""
CREATE EXTERNAL LOCATION IF NOT EXISTS retail_raw
URL 'abfss://raw@{storage_account}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL {storage_credential});

CREATE VOLUME IF NOT EXISTS {catalog}.raw.source_files
COMMENT 'Raw retail source files used by the Azure Lakehouse Starter Kit';
"""
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Best Practice
# MAGIC
# MAGIC Use:
# MAGIC
# MAGIC - Azure Data Lake Storage Gen2 for durable lake storage
# MAGIC - Unity Catalog storage credentials and external locations for governed access
# MAGIC - Volumes for file-based landing and reference data
# MAGIC - Tables for managed or external Delta data
# MAGIC
# MAGIC Avoid putting secrets in notebooks or pipeline JSON files.

