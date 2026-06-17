# Dataflow Gen2 vs Notebook vs Pipeline

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply dataflow gen2 vs notebook vs pipeline to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks) | [Home](Home) | [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Provide a practical decision guide for choosing Dataflow Gen2, Notebook, or Pipeline in Fabric projects.

## Who Should Read This

Teams deciding between low-code transformation, code-heavy transformation, and orchestration patterns.

## Beginner Explanation

Dataflow Gen2, Notebook, and Pipeline are not competitors in every situation. They solve different parts of the data engineering workflow. Dataflow Gen2 is useful for low-code data shaping. Notebooks are useful for code-heavy transformations. Pipelines are useful for orchestration.

## Decision Guide

| Need | Best choice | Why |
| --- | --- | --- |
| Low-code transformation | Dataflow Gen2 | Power Query style experience for shaping data. |
| Code-heavy transformation | Notebook | PySpark and SQL give more engineering control. |
| Orchestration | Pipeline | Coordinates copy, notebook, and refresh activities. |
| Business-user friendly prep | Dataflow Gen2 | Familiar transformation interface for analysts. |
| Complex deduplication and joins | Notebook | Easier to test and version code. |
| Scheduling multiple steps | Pipeline | Designed for dependencies and monitoring. |

## Use Dataflow Gen2 When

- Transformations are column shaping, filtering, simple joins, or reusable Power Query logic.
- Business analysts participate in data preparation.
- The logic benefits from a low-code interface.

## Use Notebook When

- You need PySpark, advanced joins, data quality frameworks, or dimensional modeling.
- Transformations need code review and unit-test style thinking.
- Data volumes or logic complexity exceed simple shaping.

## Use Pipeline When

- You need scheduling, dependencies, retries, parameters, and monitoring.
- You are orchestrating multiple notebooks, dataflows, or copy activities.

## Production Readiness

All three can be part of production. The key is ownership and clarity. A production design should say which tool owns ingestion, which owns transformation, how failures are handled, and where outputs are validated.

## Best Practices

- Avoid choosing tools only by personal preference.
- Match the tool to the workload.
- Version-control supported artifacts where possible.
- Document where business logic lives.
- Use deployment pipelines for promotion when appropriate.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Using Dataflow Gen2 for complex engineering logic | Harder to debug and review | Use notebooks. |
| Using notebooks for simple source copy | Extra code and maintenance | Use pipeline copy activities. |
| Using pipelines as a transformation engine | Visual flow becomes brittle | Orchestrate notebooks or dataflows. |

## Official Reference

- [Dataflow Gen2 CI/CD and Git integration](https://learn.microsoft.com/en-us/fabric/data-factory/dataflow-gen2-cicd-and-git-integration)

## Related Repo Files

- [docs/16-fabric-decision-guide.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/16-fabric-decision-guide.md)
- [pipelines/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/pipelines)
- [notebooks/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/notebooks)

## Related Wiki Pages

- [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks)
- [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough)
- [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can choose between Dataflow Gen2, Notebook, and Pipeline.
- [ ] I understand low-code versus code-heavy transformation patterns.
- [ ] I can explain why pipelines should orchestrate rather than hold all logic.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks) | [Home](Home) | [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
