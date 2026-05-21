# Lakehouse vs Warehouse

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply lakehouse vs warehouse to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Lakehouse Concepts](Lakehouse-Concepts) | [Home](Home) | [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Help readers decide when to use a Fabric Lakehouse and when to use a Fabric Warehouse.

## Who Should Read This

Architects, data engineers, SQL developers, and BI teams choosing the right storage and compute pattern for a new Fabric project.

## Beginner Explanation

Lakehouse and Warehouse both support analytical workloads in Fabric, but they are optimized for different working styles. A Lakehouse is ideal when engineering teams need file flexibility, Spark transformations, Delta tables, and multi-engine access. A Warehouse is ideal when teams want a SQL-first relational warehouse experience.

## Decision Table

| Area | Lakehouse | Warehouse |
| --- | --- | --- |
| Best use case | Data engineering, lake patterns, Spark transformations | SQL-first modeling, warehouse analytics |
| Data format | Delta tables and files in OneLake | Relational warehouse tables |
| Main user persona | Data engineer, data scientist, advanced BI engineer | SQL developer, warehouse developer, BI engineer |
| Engineering use | Strong Spark and notebook support | SQL transformations and warehouse modeling |
| BI use | Gold Delta tables and SQL endpoint views | SQL warehouse tables and semantic models |
| Performance considerations | Optimize Delta files and model carefully | SQL engine optimized for warehouse patterns |
| Flexibility | High for mixed raw and curated data | High for relational SQL modeling |
| Governance need | Strong layer and table governance | Strong schema and permission governance |

## Use Lakehouse When

- You need Bronze, Silver, and Gold layers.
- You process semi-structured or raw files.
- You want Spark notebooks for transformations.
- You need data science or AI-ready lake patterns.
- You want direct access to Delta tables.

## Use Warehouse When

- Your team works primarily in SQL.
- You need a relational warehouse experience.
- Your transformations are mostly T-SQL.
- Your consumers expect warehouse schemas and SQL permissions.

## Practical Example

This repo uses Lakehouse because the project starts with CSV files, applies PySpark transformations, builds Delta tables, and teaches medallion architecture. A SQL-first team could still create a Warehouse downstream or use the SQL Analytics Endpoint for SQL consumption.

## Best Practices

- Do not choose based only on tool preference. Choose based on workload pattern.
- Keep Lakehouse and Warehouse roles clear if both are used.
- Avoid duplicating the same curated dataset without a governance reason.
- Use ADRs to document the choice.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Assuming Warehouse replaces Lakehouse | Raw and Spark workflows may suffer | Use Lakehouse for engineering-heavy workflows. |
| Assuming Lakehouse removes dimensional modeling | BI still needs clear facts and dimensions | Build Gold star schemas. |
| Using both without ownership | Consumers get confused | Define source of truth. |

## Related Repo Files

- [docs/03-lakehouse-vs-warehouse.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/docs/03-lakehouse-vs-warehouse.md)
- [architecture/data-product-architecture.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/architecture/data-product-architecture.md)
- [adr/001-why-medallion-architecture.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/adr/001-why-medallion-architecture.md)

## Related Wiki Pages

- [Lakehouse Concepts](Lakehouse-Concepts)
- [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can compare Lakehouse and Warehouse in practical terms.
- [ ] I know why this repo uses Lakehouse.
- [ ] I can document the choice with an ADR.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Lakehouse Concepts](Lakehouse-Concepts) | [Home](Home) | [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
