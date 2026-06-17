# Building Dimensions and Facts

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply building dimensions and facts to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric) | [Home](Home) | [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain how this repo builds dimensions and facts, including grain, keys, relationships, example joins, and validation queries.

## Who Should Read This

Data engineers and BI developers implementing or reviewing notebook 03 and SQL scripts.

## Gold Tables

The Gold model contains five dimensions and one fact table.

| Table | Grain | Key | Purpose |
| --- | --- | --- | --- |
| dim_customer | One row per customer | customer_key | Customer attributes and segment. |
| dim_account | One row per account | account_key | Account status, type, balance, product and branch links. |
| dim_product | One row per product | product_key | Product category and family. |
| dim_branch | One row per branch | branch_key | Branch location and region. |
| dim_date | One row per calendar date | date_key | Calendar analysis. |
| fact_transaction | One row per transaction | transaction_id | Transaction measures and foreign keys. |

## Relationship Design

fact_transaction joins to dim_customer, dim_account, dim_product, dim_branch, and dim_date using surrogate keys. Natural keys are retained for traceability and validation.

## Fact Table Grain

The grain is one row per transaction event. This means transaction_count should usually count transaction_id. Amount metrics should aggregate transaction_amount or absolute_transaction_amount depending on business meaning.

## Example Join

A typical SQL query joins fact_transaction to dimensions by surrogate key, filters to posted transactions, and groups by date, branch, product, or customer segment.

Example pattern:

    SELECT d.year_month, p.product_category, COUNT(*) AS transaction_count
    FROM dbo.fact_transaction f
    JOIN dbo.dim_date d ON f.date_key = d.date_key
    JOIN dbo.dim_product p ON f.product_key = p.product_key
    WHERE f.is_posted = 1
    GROUP BY d.year_month, p.product_category;

## Validation Queries

Validation should check:

- Row counts by table.
- Duplicate surrogate keys.
- Missing dimension keys in fact_transaction.
- Silver to Gold transaction reconciliation.
- Status and amount distributions.

## Best Practices

- Generate deterministic surrogate keys for learning examples.
- Keep natural keys for traceability.
- Use dim_date for all time intelligence.
- Validate every fact foreign key.
- Keep fact measures additive where possible.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Fact table has unclear grain | Measures become wrong | State one row per transaction. |
| Joining by names instead of keys | Slow and fragile | Use surrogate or stable natural keys. |
| Missing dim_date | Inconsistent time filtering | Generate and use date_key. |

## Related Repo Files

- [notebooks/03_gold_dimensional_model.ipynb](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/notebooks/03_gold_dimensional_model.ipynb)
- [sql/validation_queries.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/validation_queries.sql)
- [sql/business_metrics.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/business_metrics.sql)
- [semantic-model/measures.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/semantic-model/measures.md)

## Related Wiki Pages

- [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric)
- [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide)
- [Semantic Model Design](Semantic-Model-Design)
- [Data Quality Framework](Data-Quality-Framework)

## Summary Checklist

- [ ] I know each Gold table and its grain.
- [ ] I understand surrogate and natural key usage.
- [ ] I can write a basic fact-to-dimension join.
- [ ] I know which validation queries to run.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric) | [Home](Home) | [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
