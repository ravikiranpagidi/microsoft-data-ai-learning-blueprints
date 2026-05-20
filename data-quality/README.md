# Data Quality Framework

This folder contains a lightweight YAML-driven data quality framework for Fabric PySpark notebooks.

## Files

| File | Purpose |
| --- | --- |
| dq_rules.yml | Rule configuration for Silver and Gold tables |
| dq_framework.py | Reusable PySpark data quality runner |
| dq_examples.md | Example checks and expected output |
| dq_report_template.md | Markdown report template |

## Rule Types

- not_null
- duplicate_key
- accepted_values
- range
- referential_integrity
- row_count_min
- freshness

## How to Use

1. Upload or reference dq_rules.yml from a notebook.
2. Import dq_framework.py or paste it into a Fabric notebook cell.
3. Run checks after Silver transformation and before Gold publication.
4. Stop the pipeline if required rules fail.
