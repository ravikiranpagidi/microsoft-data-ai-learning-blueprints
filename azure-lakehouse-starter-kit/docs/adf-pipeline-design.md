# ADF Pipeline Design

## Purpose

Explain the Azure Data Factory orchestration pattern used in the starter kit.

## Pipeline 1: pl_ingest_to_raw

Responsibilities:

- Trigger daily or on demand.
- Read active source objects from metadata.
- Loop over each source object.
- Copy data into ADLS raw.
- Apply file naming convention.
- Log audit status.
- Handle failures.

Pattern:

```text
Trigger -> Lookup metadata -> ForEach source -> Copy to raw -> Validate arrival -> Log status
```

## Pipeline 2: pl_process_bronze

Responsibilities:

- Receive source object and batch ID.
- Run Databricks Bronze notebook.
- Write Bronze Delta table.
- Update process status.

## Pipeline 3: pl_process_silver_gold

Responsibilities:

- Run Silver transformation.
- Run DQ checks.
- Stop or quarantine failed records.
- Run Gold transformation.
- Publish status.

## Pipeline 4: pl_master_orchestration

Responsibilities:

- Call ingestion.
- Call Bronze processing.
- Call Silver and Gold processing.
- Send failure notification placeholder.
- Log run status.

## Metadata-Driven Design

The metadata table controls source name, source type, object name, target folder, load type, format, active flag, and notebook path. This reduces hardcoded ADF pipelines.
