# Lakehouse Concepts

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply lakehouse concepts to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [OneLake Explained](OneLake-Explained) | [Home](Home) | [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the Fabric Lakehouse as a practical architecture pattern for storing, transforming, querying, and consuming data.

## Who Should Read This

Beginners learning Lakehouse concepts, SQL users moving toward lakehouse patterns, and Power BI developers who need to understand where report data comes from.

## What Is a Lakehouse?

A Lakehouse combines data lake flexibility with table-oriented analytics patterns. In Fabric, a Lakehouse item provides a Files area for raw files and a Tables area for managed Delta tables. It can be accessed by Spark notebooks, SQL Analytics Endpoint, Power BI, pipelines, and other Fabric experiences.

## Lakehouse as Storage + Metadata + Compute Access

A Lakehouse is not just a folder. It gives you organized storage, metadata for tables, and multiple access patterns. Spark is used for engineering transformations. SQL users can query Delta tables through the SQL Analytics Endpoint. Power BI can consume curated tables and semantic models.

## Files Area

Use Files for landing raw data, examples, exports, and non-tabular objects. In this repo, CSV source files start in Files/retail_banking/source.

## Tables Area

Use Tables for Delta tables that should be queried, governed, optimized, and consumed. Bronze, Silver, and Gold tables are written with saveAsTable in the notebooks.

## Delta Format

Delta tables add reliability and metadata on top of file-based storage. They support schema, transaction logs, and efficient query behavior. This makes them a better analytics foundation than raw CSV files.

## Access Patterns

| Consumer | Best access pattern |
| --- | --- |
| Data engineer | Spark notebooks over Lakehouse tables |
| SQL analyst | SQL Analytics Endpoint views |
| BI developer | Gold tables or semantic model |
| Data steward | DQ reports, governance docs, curated views |

## Best Practices

- Treat Files as landing and staging, not the final reporting layer.
- Treat Tables as governed data assets.
- Use consistent Bronze, Silver, and Gold table names.
- Keep business metrics consistent by defining them in Gold, SQL views, or semantic models.
- Document table grain and ownership.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Calling every file a table | Users confuse raw files with governed assets | Promote data to Delta tables. |
| Mixing raw and curated data in one table | Quality and lineage become unclear | Use medallion layers. |
| Skipping table descriptions | Consumers do not know how to use data | Add documentation and glossary entries. |

## Related Repo Files

- [docs/03-lakehouse-vs-warehouse.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/docs/03-lakehouse-vs-warehouse.md)
- [notebooks/01_bronze_ingestion.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/notebooks/01_bronze_ingestion.ipynb)
- [notebooks/03_gold_dimensional_model.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/notebooks/03_gold_dimensional_model.ipynb)

## Related Wiki Pages

- [OneLake Explained](OneLake-Explained)
- [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse)
- [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse)
- [Bronze Layer Design](Bronze-Layer-Design)

## Summary Checklist

- [ ] I can explain the Files and Tables areas.
- [ ] I understand why Delta tables are used.
- [ ] I know which users access the Lakehouse through Spark, SQL, and Power BI.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [OneLake Explained](OneLake-Explained) | [Home](Home) | [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
