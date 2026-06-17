# Why Apply Data Quality Before Gold Layer

## Status

Accepted

## Context

Gold tables feed SQL views, semantic models, and business dashboards. Poor quality at this layer damages trust quickly.

## Decision

Run data quality checks after Silver and before Gold consumption refresh. Block production promotion for critical failures.

## Consequences

Business users receive more reliable data. Pipelines may fail more often at first, but failures surface real issues earlier.

## Alternatives Considered

Validate only in Power BI, validate only manually, or ignore low-volume issues.

## Recommendation

Treat data quality as a release gate, not a reporting afterthought.
