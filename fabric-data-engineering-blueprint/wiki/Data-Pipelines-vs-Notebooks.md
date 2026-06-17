# Data Pipelines vs Notebooks

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply data pipelines vs notebooks to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse) | [Home](Home) | [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Compare Fabric Data Pipelines and Fabric Notebooks so teams know where to put orchestration and where to put transformation code.

## Who Should Read This

Data engineers, ADF users moving to Fabric, and beginners deciding whether to build visually or with PySpark.

## Beginner Explanation

A Data Pipeline coordinates work. A Notebook performs code-based transformation. They often work together. A pipeline can copy files, pass parameters, schedule a run, and call notebooks. A notebook can run PySpark logic, transform data, validate records, and write Delta tables.

## Comparison

| Area | Data Pipeline | Notebook |
| --- | --- | --- |
| Main role | Orchestration | Transformation and analysis |
| Interface | Visual activities | Code cells |
| Best for | Copy, scheduling, dependencies, retries | PySpark, SQL, complex logic, validation |
| Monitoring | Activity run view | Notebook run output and logs |
| Reusability | Parameterized pipelines | Parameterized notebooks and functions |
| Beginner friendly | Good for visual flow | Good for learning code step by step |
| Production use | Strong for orchestration | Strong for transformation logic |

## Use Pipelines When

- You need scheduled orchestration.
- You need to copy files from a source system.
- You need retries, dependencies, and activity monitoring.
- You need to call several notebooks in a sequence.

## Use Notebooks When

- You need PySpark transformations.
- You need complex data quality checks.
- You need joins, deduplication, type casting, and business rules.
- You want readable educational code.

## Practical Pattern

A production pipeline might run: ingest source files -> run Bronze notebook -> run Silver notebook -> run Gold notebook -> run DQ notebook -> notify owners. The notebooks contain transformation logic; the pipeline controls the order and runtime parameters.

## Best Practices

- Keep pipelines focused on orchestration.
- Keep transformations modular in notebooks.
- Pass environment and batch parameters from pipelines.
- Log row counts in notebooks.
- Fail fast when critical data quality rules fail.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Putting every transformation in pipeline activities | Logic becomes hard to review | Use notebooks for transformation-heavy work. |
| Running notebooks manually forever | No operational repeatability | Use pipelines for scheduled production runs. |
| Not passing parameters | Dev/Test/Prod changes require code edits | Parameterize paths and environment names. |

## Related Repo Files

- [pipelines/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/pipelines)
- [notebooks/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/notebooks)
- [docs/06-data-pipeline-vs-notebook.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/docs/06-data-pipeline-vs-notebook.md)

## Related Wiki Pages

- [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline)
- [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough)
- [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy)

## Summary Checklist

- [ ] I can explain orchestration versus transformation.
- [ ] I know when to use a pipeline.
- [ ] I know when to use a notebook.
- [ ] I can design a pipeline that calls notebooks in order.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Files vs Tables in Fabric Lakehouse](Files-vs-Tables-in-Fabric-Lakehouse) | [Home](Home) | [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
