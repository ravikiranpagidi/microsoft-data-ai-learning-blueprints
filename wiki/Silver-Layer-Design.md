# Silver Layer Design

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply silver layer design to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Bronze Layer Design](Bronze-Layer-Design) | [Home](Home) | [Gold Layer Design](Gold-Layer-Design)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Define the Silver layer design for cleaning, standardization, deduplication, null handling, and business key validation.

## Who Should Read This

Data engineers implementing transformation logic and learners running notebook 02.

## Purpose of Silver

Silver turns raw data into trusted, typed, conformed data. It is the quality gate between raw ingestion and business-ready modeling.

## Cleaning and Standardization

Silver should handle column naming, trimming, casing, date parsing, numeric casting, boolean parsing, and status standardization. The goal is not to create final reporting metrics. The goal is to create reliable, reusable entity tables.

## Type Casting

CSV values arrive as strings in Bronze. Silver casts values into dates, timestamps, decimals, booleans, and normalized text. This avoids every downstream consumer having to parse values differently.

## Deduplication

Business keys such as customer_id, account_id, product_id, branch_id, and transaction_id should be unique in Silver. If duplicates arrive, keep the latest trusted record based on ingestion metadata and document the rule.

## Business Key Validation

Silver validates relationships. Accounts should reference existing customers, products, and branches. Transactions should reference existing accounts, products, and branches. Invalid records can be quarantined for review.

## Null Handling

Not every null is bad. Silver should distinguish between acceptable missing optional values and critical missing keys. Missing business keys should fail or quarantine. Optional descriptive columns can be handled with defaults or allowed nulls based on business rules.

## Reference Data Standardization

Values such as account_status, transaction_status, transaction_channel, and region should be standardized to approved values. This makes reporting consistent.

## Practical Example

Notebook 02 creates silver_transactions by casting transaction_timestamp, deriving transaction_date, standardizing transaction_status, calculating absolute_transaction_amount, and validating account_id against silver_accounts.

## Best Practices

- Keep Silver reusable across multiple Gold models.
- Quarantine invalid records rather than silently dropping them.
- Validate relationships before building facts.
- Record transformation rules in documentation.
- Keep row count validation visible.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Silently dropping bad records | Data loss is hidden | Quarantine and report. |
| Casting fields in Gold only | Rework spreads downstream | Type data in Silver. |
| Ignoring business keys | Joins fail later | Validate keys in Silver. |

## Related Repo Files

- [notebooks/02_silver_transformation.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/notebooks/02_silver_transformation.ipynb)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/data-quality/dq_rules.yml)
- [docs/05-medallion-architecture.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/docs/05-medallion-architecture.md)

## Related Wiki Pages

- [Medallion Architecture](Medallion-Architecture)
- [Bronze Layer Design](Bronze-Layer-Design)
- [Gold Layer Design](Gold-Layer-Design)
- [Governance and Security](Governance-and-Security)

## Summary Checklist

- [ ] Columns are standardized.
- [ ] Data types are cast correctly.
- [ ] Duplicates are removed by business key.
- [ ] Critical nulls and invalid references are handled.
- [ ] Quarantine logic is documented.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Bronze Layer Design](Bronze-Layer-Design) | [Home](Home) | [Gold Layer Design](Gold-Layer-Design) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
