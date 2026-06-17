# OneLake Explained

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply onelake explained to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Fabric Data Engineering Overview](Fabric-Data-Engineering-Overview) | [Home](Home) | [Lakehouse Concepts](Lakehouse-Concepts)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain OneLake conceptually and show how it supports Fabric Lakehouse projects, shortcuts, Files, Tables, and shared analytics access.

## Who Should Read This

Anyone who has used ADLS Gen2, data lakes, storage accounts, or Power BI workspaces and wants to understand the Fabric storage model.

## What Is OneLake?

OneLake is the logical data lake built into Microsoft Fabric. It gives Fabric workloads a shared storage foundation so data can be discovered and reused across experiences without every team creating isolated storage patterns.

## OneLake vs ADLS Gen2 Conceptually

OneLake is built on ADLS Gen2 concepts, but Fabric presents it as a SaaS-managed data lake. In traditional Azure projects, engineers often think about storage accounts, containers, resource groups, firewall settings, and separate service configuration. In Fabric, users work through workspaces and items such as Lakehouses, Warehouses, and semantic models.

## Workspace and Item Organization

A workspace is the collaboration boundary. A Lakehouse is an item inside a workspace. The Lakehouse has a Files area and a Tables area. Other Fabric items can interact with those tables through Spark, SQL, Power BI, and shortcuts.

## Shortcuts

Shortcuts let you reference data that lives elsewhere without copying it into the Lakehouse. They are useful for data sharing, avoiding duplication, and building a logical data product over distributed data. Use shortcuts carefully when ownership, performance, and access rules are clear.

## Files and Tables

- Files are for raw or unmanaged files such as CSV, JSON, logs, and source extracts.
- Tables are managed Delta tables that support analytics and metadata.

## Practical Example

In this repo, CSV files land under Files/retail_banking/source. Notebooks read those files and write Bronze, Silver, and Gold Delta tables in the Tables area. SQL and Power BI should consume tables or views, not raw CSV files.

## Best Practices

- Use clear folder conventions in Files.
- Use Delta tables for analytics-ready data.
- Avoid copying data when shortcuts are a better governed option.
- Do not use OneLake as an unstructured dumping ground.
- Document ownership for each data product.

## Common Mistakes

| Mistake | Why it matters | Better approach |
| --- | --- | --- |
| Uploading everything into random folders | Data becomes hard to find | Use domain and layer folder conventions. |
| Querying raw CSV files directly for BI | Reports become fragile | Convert to Delta tables first. |
| Creating shortcuts without ownership clarity | Access and quality issues spread | Document owner, source, and SLA. |

## Official Reference

- [Microsoft Fabric overview and OneLake concepts](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)

## Related Repo Files

- [docs/04-onelake-explained.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/docs/04-onelake-explained.md)
- [architecture/fabric-end-to-end-architecture.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/architecture/fabric-end-to-end-architecture.md)
- [sample-data/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/sample-data)

## Related Wiki Pages

- [Lakehouse Concepts](Lakehouse-Concepts)
- [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can explain OneLake as Fabric shared logical storage.
- [ ] I understand the difference between Files and Tables.
- [ ] I know when shortcuts can reduce copying.
- [ ] I know why BI should usually use tables or views.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Fabric Data Engineering Overview](Fabric-Data-Engineering-Overview) | [Home](Home) | [Lakehouse Concepts](Lakehouse-Concepts) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
