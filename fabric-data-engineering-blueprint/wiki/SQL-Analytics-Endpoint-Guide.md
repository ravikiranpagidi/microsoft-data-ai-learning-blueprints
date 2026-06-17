# SQL Analytics Endpoint Guide

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply sql analytics endpoint guide to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Building Dimensions and Facts](Building-Dimensions-and-Facts) | [Home](Home) | [Power BI Consumption Guide](Power-BI-Consumption-Guide)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the Fabric Lakehouse SQL Analytics Endpoint and how SQL users can query Delta tables and create consumption views.

## Who Should Read This

SQL analysts, BI developers, data engineers, and learners who prefer SQL access to Lakehouse data.

## What Is the SQL Analytics Endpoint?

The SQL Analytics Endpoint provides a read-only T-SQL query surface over Lakehouse Delta tables. It is automatically available for a Lakehouse and helps SQL users query curated data without writing Spark code.

## How It Helps SQL Users

SQL users can query Gold tables, create views, validate row counts, build business metrics, and support Power BI consumption. This is especially useful for teams moving from SQL Server, Synapse dedicated SQL pools, or traditional warehouses.

## Querying Lakehouse Tables

After notebooks create Delta tables, those tables are visible in the SQL Analytics Endpoint. You can run SELECT queries against tables such as dim_customer and fact_transaction.

## Creating Views

This repo includes create_gold_views.sql and powerbi_consumption_views.sql. Views are helpful when you want business-friendly names, reusable joins, and stable consumption patterns.

## Important Limitations

The SQL Analytics Endpoint is read-only for Lakehouse Delta tables. Use Spark notebooks or other supported write paths to create and update tables. Use SQL for querying, views, validation, and consumption logic.

## Practical Workflow

1. Run Gold notebook.
2. Open SQL Analytics Endpoint.
3. Run create_gold_views.sql.
4. Run validation_queries.sql.
5. Run business_metrics.sql.
6. Run powerbi_consumption_views.sql if you want wide reporting views.

## Best Practices

- Use SQL views for repeatable consumption logic.
- Keep write operations in notebooks or pipelines.
- Validate Gold before creating semantic models.
- Avoid hiding complex data quality issues inside SQL views.
- Document which views are approved for reporting.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Trying to update Lakehouse tables through SQL endpoint | Endpoint is read-only for tables | Use Spark for writes. |
| Building all logic in one giant SQL view | Hard to govern and tune | Keep Gold model clean and views focused. |
| Letting every analyst create their own metric SQL | Metric drift | Use approved metric views and semantic measures. |

## Official Reference

- [SQL Analytics Endpoint for Lakehouse](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sql-analytics-endpoint)

## Related Repo Files

- [sql/create_gold_views.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/create_gold_views.sql)
- [sql/business_metrics.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/business_metrics.sql)
- [sql/validation_queries.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/validation_queries.sql)
- [sql/powerbi_consumption_views.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/powerbi_consumption_views.sql)

## Related Wiki Pages

- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Power BI Consumption Guide](Power-BI-Consumption-Guide)
- [Semantic Model Design](Semantic-Model-Design)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I understand SQL Analytics Endpoint is read-only over Lakehouse tables.
- [ ] I can run validation and business metric SQL.
- [ ] I know why views help SQL and Power BI users.
- [ ] I know not to use SQL endpoint as the transformation write engine.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Building Dimensions and Facts](Building-Dimensions-and-Facts) | [Home](Home) | [Power BI Consumption Guide](Power-BI-Consumption-Guide) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
