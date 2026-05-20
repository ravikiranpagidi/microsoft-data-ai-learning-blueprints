# Data Pipeline vs Notebook

## Concept

A Data Pipeline orchestrates movement and activity execution. A Notebook contains code-based data processing logic, usually PySpark or SQL.

## Why It Matters

Clear separation prevents visual pipelines from becoming hard-to-maintain logic containers and prevents notebooks from becoming hidden schedulers.

## How It Works in Microsoft Fabric

Fabric Data Pipelines can copy data, call notebooks, pass parameters, and coordinate dependencies. Fabric Notebooks can read, transform, validate, and write data using Spark.

## Real-World Use Case

Use a pipeline to ingest daily source files and trigger notebooks. Use notebooks to clean transactions, build dimensions, and run quality checks.

## Beginner Explanation

Pipeline asks: what runs and in what order? Notebook asks: how is the data transformed?

## Enterprise Best Practice

Keep orchestration in pipelines and complex transformation in notebooks. Use parameters for environment, batch ID, and source path.

## Common Mistakes

- Hardcoding paths in notebooks and pipelines.
- Putting large SQL or Python transformations inside pipeline expressions.
- Running notebooks manually in production without orchestration.
- Creating many notebooks with no dependency map.

## Practical Recommendation

Use both. A production Fabric data engineering solution usually needs pipelines for orchestration and notebooks for transformations.

## Decision Guide

| Need | Prefer |
| --- | --- |
| Copy files from source to Lakehouse | Data Pipeline |
| Run multi-step PySpark transformations | Notebook |
| Schedule and monitor dependencies | Data Pipeline |
| Build Delta dimensions and facts | Notebook |
| Parameterized repeatable run | Pipeline calling notebook |
| Ad hoc exploration | Notebook |

## Dataflow Gen2 vs Notebook

Use Dataflow Gen2 when low-code shaping is enough and maintainers prefer a visual experience. Use Notebook when transformations require code reuse, Spark control, complex rules, or engineering discipline.

## Shortcut vs Copy

Use a Shortcut when data should be referenced in place and ownership remains elsewhere. Use Copy when you need a managed landing copy, isolation, auditability, or transformation independence.
