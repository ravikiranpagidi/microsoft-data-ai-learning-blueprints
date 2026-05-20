# Power BI Model Guidelines

## Model Design

- Use the Gold star schema as the semantic model source.
- Hide surrogate key columns from report view after relationships are created.
- Keep natural keys visible only when report authors need drill-through or reconciliation.
- Use a dedicated measures table if your modeling standard prefers it.
- Mark dim_date as the date table.

## Naming Standards

| Object | Standard | Example |
| --- | --- | --- |
| Tables | Business-friendly singular or plural names | Customer, Account, Transaction |
| Measures | Clear business metric name | Total Transaction Amount |
| Columns | Title case in report view | Customer Segment |
| Keys | Hidden after relationship setup | customer_key |

## Relationship Rules

- Use single-direction filtering from dimensions to facts.
- Avoid bi-directional relationships unless there is a documented modeling need.
- Do not relate fact tables directly to each other.
- Keep inactive relationships documented.

## Report Author Guidance

Report authors should use measures instead of dragging raw numeric columns into visuals. This protects metric consistency across dashboards.

## Security

If row-level security is needed, define it in the semantic model using business attributes such as region or branch. Confirm the security model with data owners before publishing.

## Common Mistakes

- Building Power BI reports directly on Bronze tables.
- Creating local measures in each report file.
- Leaving technical keys visible to business users.
- Using many-to-many relationships to hide data modeling issues.
- Publishing reports without metric definitions.
