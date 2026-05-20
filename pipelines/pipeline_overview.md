# Pipeline Overview

Fabric Data Pipelines should orchestrate movement and execution sequence for the retail banking blueprint.

## Ingestion Pipeline

Purpose: land source CSV files into Lakehouse Files.

Typical activities:

1. Set batch ID.
2. Copy customers.csv, accounts.csv, products.csv, branches.csv, and transactions.csv.
3. Validate that files exist.
4. Trigger Bronze ingestion notebook.
5. Write audit status.

## Transformation Pipeline

Purpose: run engineering notebooks in the correct order.

Typical activities:

1. Run 01_bronze_ingestion.
2. Run 02_silver_transformation.
3. Run 03_gold_dimensional_model.
4. Run 04_data_quality_checks.
5. Run 05_delta_optimization if scheduled for a maintenance window.
6. Notify semantic model owner that data is ready.

## Pipeline Parameters

| Parameter | Example | Purpose |
| --- | --- | --- |
| environment | dev | Select environment-specific paths and item names |
| batch_id | 20260520180000 | Trace one ingestion and transformation run |
| source_folder | Files/retail_banking/source | Input location |
| load_type | full | Full or incremental load pattern |
