# Orchestration Pattern

## Recommended Flow

~~~mermaid
flowchart LR
    start["Schedule or manual trigger"] --> setBatch["Create batch ID"]
    setBatch --> copy["Copy source CSV files"]
    copy --> bronze["Run Bronze notebook"]
    bronze --> silver["Run Silver notebook"]
    silver --> gold["Run Gold notebook"]
    gold --> dq["Run data quality notebook"]
    dq --> decision{"DQ passed?"}
    decision -->|Yes| refresh["Refresh semantic model"]
    decision -->|No| alert["Alert data owner and engineer"]
~~~

## Operational Guidance

- Use one batch ID across all activities in a run.
- Fail fast on missing files.
- Do not refresh Power BI when data quality fails.
- Log row counts from source, Bronze, Silver, and Gold.
- Keep production schedules aligned with data availability SLAs.

## Common Mistakes

- Running notebooks manually in production.
- Scheduling refresh before data quality checks complete.
- Hardcoding Dev workspace or Lakehouse IDs in templates.
- Treating pipeline success as business data success.
