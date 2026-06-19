# Data Quality Framework

## Purpose

Describe the lightweight DQ framework used in the starter kit.

## Control Tables

| Table | Purpose |
| --- | --- |
| `dq_rules` | Stores active quality rules |
| `dq_results` | Stores pass/fail outcomes |
| `dq_error_records` | Stores failed record samples and metadata |

## Rule Types

- `NOT_NULL`
- `UNIQUE`
- `ACCEPTED_VALUES`
- `RANGE_CHECK`
- `REFERENTIAL_INTEGRITY`
- `SCHEMA_MATCH`
- `DUPLICATE_CHECK`

## How It Works

1. Read active rules from `dq_rules`.
2. Apply rules to a target table or DataFrame.
3. Write a result row to `dq_results`.
4. Write failed records to quarantine or `dq_error_records`.
5. Stop the pipeline for critical rule failures.
6. Allow warning-level failures to continue with visibility.

## Quarantine Pattern

Bad records should be separated into quarantine tables with:

- Source table.
- Rule name.
- Failure reason.
- Batch ID.
- Record payload.
- Error timestamp.
