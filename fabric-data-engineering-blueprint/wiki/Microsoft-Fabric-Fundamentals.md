# Microsoft Fabric Fundamentals

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply microsoft fabric fundamentals to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Getting Started](Getting-Started) | [Home](Home) | [Fabric Data Engineering Overview](Fabric-Data-Engineering-Overview)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the Microsoft Fabric platform at a practical level so readers understand where Data Engineering fits.

## Who Should Read This

Beginners, Azure data professionals, Power BI users, and architects who need a clear mental model before building.

## What Is Microsoft Fabric?

Microsoft Fabric is a unified analytics platform that brings data movement, data engineering, data warehousing, real-time analytics, data science, and Power BI into a single SaaS experience. Instead of stitching together many independent services, Fabric gives teams shared storage, shared governance, and integrated workloads.

## Key Workloads

| Workload | What it is used for | Typical user |
| --- | --- | --- |
| Data Engineering | Lakehouse, Spark notebooks, data preparation, Delta tables | Data engineer |
| Data Factory | Pipelines, copy activity, Dataflow Gen2, orchestration | Data engineer, integration developer |
| Data Warehouse | SQL-first warehouse modeling and T-SQL analytics | SQL developer, BI engineer |
| Power BI | Semantic models, reports, dashboards | BI developer, analyst |
| Real-Time Intelligence | Event streams and real-time analytics | Streaming engineer, analyst |
| Data Science | Experiments, ML models, notebooks | Data scientist |

## Why Fabric Matters

Traditional analytics platforms often require separate storage accounts, integration runtimes, Spark platforms, warehouses, semantic models, and BI workspaces. Fabric reduces that complexity by bringing these experiences together around OneLake and workspace items.

## How Fabric Simplifies Analytics

- OneLake gives a unified logical data lake.
- Lakehouse tables can be used by Spark, SQL, and Power BI.
- Pipelines orchestrate movement and notebook execution.
- SQL Analytics Endpoint gives SQL access to Lakehouse Delta tables.
- Power BI can consume Fabric data with semantic models and Direct Lake patterns.

## Real-World Context

In an enterprise proof of concept, Fabric lets a small team build the first version of a data product without provisioning every Azure service separately. That does not remove the need for architecture. It changes where the architecture effort goes: naming, governance, workspace design, data quality, semantic modeling, and deployment discipline become more important.

## Best Practices

- Start with a clear workspace and Lakehouse naming strategy.
- Separate learning, development, test, and production work.
- Use Lakehouse for engineering patterns and Warehouse for SQL-first warehouse workloads.
- Keep business metrics in the semantic model or governed SQL views, not scattered across reports.
- Document important design choices with ADRs.

## Common Mistakes

| Mistake | Why it hurts | Better approach |
| --- | --- | --- |
| Thinking Fabric is only Power BI | Teams miss engineering and governance features | Learn the workloads together. |
| Treating every workload as interchangeable | Wrong tool selection causes complexity | Use a decision guide. |
| Skipping workspace planning | Security and deployment become messy | Define environment strategy early. |

## Official Reference

- [Microsoft Fabric overview](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)
- [Microsoft Fabric terminology](https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-terminology)

## Related Repo Files

- [docs/01-what-is-microsoft-fabric.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/01-what-is-microsoft-fabric.md)
- [docs/02-fabric-data-engineering-concepts.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/02-fabric-data-engineering-concepts.md)
- [architecture/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/architecture)

## Related Wiki Pages

- [Fabric Data Engineering Overview](Fabric-Data-Engineering-Overview)
- [OneLake Explained](OneLake-Explained)
- [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can explain Fabric as a unified analytics platform.
- [ ] I can name the main workloads and their purpose.
- [ ] I understand how OneLake connects the platform.
- [ ] I know why workspace planning matters.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Getting Started](Getting-Started) | [Home](Home) | [Fabric Data Engineering Overview](Fabric-Data-Engineering-Overview) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
