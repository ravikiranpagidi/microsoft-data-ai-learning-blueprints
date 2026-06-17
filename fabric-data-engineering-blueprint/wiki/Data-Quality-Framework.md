# Data Quality Framework

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply data quality framework to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Semantic Model Design](Semantic-Model-Design) | [Home](Home) | [Governance and Security](Governance-and-Security)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the rule-driven data quality framework, supported checks, example rules, report output, and extension pattern.

## Who Should Read This

Data engineers, stewards, and architects who want quality checks before business consumption.

## Why Data Quality Matters

Data quality protects trust. If customer IDs are duplicated, transaction amounts are malformed, or fact rows do not reconcile to Silver, reports may look polished but be wrong. Quality checks make issues visible before users rely on the data.

## Framework Files

| File | Purpose |
| --- | --- |
| dq_rules.yml | Defines table-level quality rules. |
| dq_framework.py | Runs rules against Spark tables and returns results. |
| 04_data_quality_checks.ipynb | Notebook implementation and report output. |
| dq_report_template.md | Template for publishing quality results. |

## Supported Rule Types

| Rule type | Purpose | Example |
| --- | --- | --- |
| not_null | Required fields are populated | customer_id is required. |
| duplicate_key | Business key is unique | transaction_id is unique. |
| accepted_values | Column values match approved list | status is Active or Inactive. |
| range | Numeric value is reasonable | balance is within an expected range. |
| referential_integrity | Child keys exist in parent table | account customer_id exists in customers. |
| row_count_reconciliation | Source and target counts match | silver_transactions equals fact_transaction. |
| freshness | Data is recent enough | ingestion timestamp within allowed hours. |
| sql_expression | Custom failure expression | email value lacks @ symbol. |

## Example Rule

    name: transaction_id_unique
    type: duplicate_key
    columns: [transaction_id]
    severity: critical

## Example Output

The framework produces a table with table_name, rule_name, rule_type, severity, status, failed_count, details, and run_timestamp. The notebook also prints a markdown-style report.

## How to Extend the Framework

1. Add a new rule to dq_rules.yml.
2. If the rule type already exists, run the DQ notebook.
3. If the rule type is new, add a handler to dq_framework.py.
4. Add a small example to dq_examples.md.
5. Document the expected behavior in this Wiki or data-quality README.

## Best Practices

- Mark key integrity checks as critical.
- Use warnings for values that require review but should not stop every run.
- Keep rules readable for data stewards.
- Persist results for trend analysis.
- Fail promotion when critical rules fail.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Only checking row counts | Bad values can still pass | Use multiple rule types. |
| Keeping rules inside notebooks only | Rules are hard to review | Put rules in YAML. |
| Ignoring warning trends | Problems become normalized | Review DQ history. |

## Related Repo Files

- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/data-quality/dq_rules.yml)
- [data-quality/dq_framework.py](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/data-quality/dq_framework.py)
- [notebooks/04_data_quality_checks.ipynb](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/notebooks/04_data_quality_checks.ipynb)
- [data-quality/dq_examples.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/data-quality/dq_examples.md)

## Related Wiki Pages

- [Silver Layer Design](Silver-Layer-Design)
- [Gold Layer Design](Gold-Layer-Design)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Access Control Model](Access-Control-Model)

## Summary Checklist

- [ ] I know why data quality checks are required.
- [ ] I understand all supported rule types.
- [ ] I can add or modify a YAML rule.
- [ ] I know how DQ results are reported.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Semantic Model Design](Semantic-Model-Design) | [Home](Home) | [Governance and Security](Governance-and-Security) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
