-- Operational monitoring examples for a Fabric Lakehouse project.
-- These queries assume you create audit tables similar to the examples below.

-- Example audit table shape:
-- CREATE TABLE dbo.audit_pipeline_run (
--     batch_id VARCHAR(50),
--     environment VARCHAR(20),
--     pipeline_name VARCHAR(200),
--     activity_name VARCHAR(200),
--     status VARCHAR(50),
--     started_at DATETIME2,
--     ended_at DATETIME2,
--     rows_read BIGINT,
--     rows_written BIGINT,
--     message VARCHAR(4000)
-- );

-- 1. Latest pipeline run status.
SELECT TOP (20)
    batch_id,
    environment,
    pipeline_name,
    activity_name,
    status,
    started_at,
    ended_at,
    DATEDIFF(second, started_at, ended_at) AS duration_seconds,
    rows_read,
    rows_written,
    message
FROM dbo.audit_pipeline_run
ORDER BY started_at DESC;

-- 2. Failed activity summary.
SELECT
    pipeline_name,
    activity_name,
    COUNT(*) AS failure_count,
    MAX(started_at) AS latest_failure_at
FROM dbo.audit_pipeline_run
WHERE status IN ('Failed', 'Cancelled')
GROUP BY pipeline_name, activity_name
ORDER BY latest_failure_at DESC;

-- 3. Row count reconciliation by batch.
SELECT
    batch_id,
    pipeline_name,
    SUM(rows_read) AS total_rows_read,
    SUM(rows_written) AS total_rows_written,
    SUM(rows_read) - SUM(rows_written) AS row_count_difference
FROM dbo.audit_pipeline_run
GROUP BY batch_id, pipeline_name
HAVING SUM(rows_read) <> SUM(rows_written);

-- 4. Data freshness from the Gold fact table.
SELECT
    MAX(transaction_timestamp) AS latest_transaction_timestamp,
    DATEDIFF(hour, MAX(transaction_timestamp), SYSUTCDATETIME()) AS hours_since_latest_transaction
FROM dbo.fact_transaction
WHERE is_posted = 1;

-- 5. Data quality status trend.
-- Example table shape:
-- CREATE TABLE dbo.audit_data_quality_result (
--     batch_id VARCHAR(50),
--     table_name VARCHAR(200),
--     rule_name VARCHAR(200),
--     severity VARCHAR(50),
--     status VARCHAR(50),
--     failed_count BIGINT,
--     run_timestamp DATETIME2
-- );

SELECT
    CAST(run_timestamp AS DATE) AS run_date,
    status,
    severity,
    COUNT(*) AS rule_count,
    SUM(failed_count) AS failed_row_count
FROM dbo.audit_data_quality_result
GROUP BY CAST(run_timestamp AS DATE), status, severity
ORDER BY run_date DESC, severity, status;
