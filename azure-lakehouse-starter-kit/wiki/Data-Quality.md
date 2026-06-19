# Data Quality

## Purpose

This page explains how data quality checks are applied before data becomes business-ready.

## Included Rule Types

| Rule Type | Example |
| --- | --- |
| Schema check | Required columns exist |
| Not null | `customer_id` cannot be null |
| Duplicate check | `order_item_id` must be unique |
| Referential integrity | Orders must reference valid customers |
| Range check | Sales amount cannot be negative |

## Included Files

- `databricks/notebooks/04_data_quality/dq_rules.yml`
- `dq_schema_checks.py`
- `dq_null_checks.py`
- `dq_duplicate_checks.py`
- `dq_referential_checks.py`
- `sql/dq/dq_control_tables.sql`

## Practical Use

Run DQ checks after Silver transformations and before Gold publishing. High severity failures should stop the pipeline. Lower severity warnings can be reviewed by data stewards.

## Checklist

- [ ] Required keys are populated.
- [ ] Business keys are unique.
- [ ] Child records reference known parents.
- [ ] Metrics are in expected ranges.
- [ ] DQ failures are visible in `dq.dq_results`.

## Related Pages

- [Medallion Design](Medallion-Design)
- [Databricks Notebooks](Databricks-Notebooks)
- [Security Governance](Security-Governance)

