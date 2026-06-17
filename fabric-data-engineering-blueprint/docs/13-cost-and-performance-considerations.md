# Cost and Performance Considerations

## Concept

Fabric performance and cost depend on capacity, data volume, file layout, Spark job design, pipeline frequency, model design, and user behavior.

## Why It Matters

A design that is inexpensive at small scale may become expensive when jobs run frequently or reports query inefficient shapes.

## How It Works in Microsoft Fabric

Fabric capacity is shared across workloads. Lakehouse file design, Delta maintenance, query patterns, and semantic model design all affect user experience.

## Real-World Use Case

Monthly transaction trends should query Gold fact tables with date keys and useful views instead of scanning raw CSV files repeatedly.

## Beginner Explanation

Performance is not only faster code. It is also fewer unnecessary scans, better data layout, and clearer consumption patterns.

## Enterprise Best Practice

Measure before tuning. Optimize Gold tables and semantic models that are actually used.

## Common Mistakes

- Optimizing Bronze before knowing usage.
- Running full reloads forever.
- Creating many duplicate semantic models.
- Letting reports scan uncurated large tables.
- Ignoring data freshness and job duration trends.

## Practical Recommendation

Start simple, log row counts and runtimes, and optimize tables that support common business queries.
