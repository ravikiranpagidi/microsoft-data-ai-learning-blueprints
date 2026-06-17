# Why Gold Star Schema

## Status

Accepted

## Context

Power BI consumption needs clear relationships, reusable dimensions, and consistent metrics for banking analytics.

## Decision

Create Gold dimensions for customer, account, product, branch, and date, plus a fact_transaction table.

## Consequences

Power BI models are easier to use and govern. Some users may ask for one wide table, but the semantic model can still provide friendly views.

## Alternatives Considered

One wide table, report-specific extracts, or direct querying of Silver tables.

## Recommendation

Use a star schema for shared analytics and create SQL views for report-friendly projections.
