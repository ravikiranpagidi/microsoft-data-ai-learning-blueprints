# Why Separate Engineering and Consumption Layers

## Status

Accepted

## Context

Report authors need trusted data, while engineers need raw and intermediate data for troubleshooting and transformation.

## Decision

Restrict Bronze and Silver primarily to engineering workflows and publish Gold tables, SQL views, and semantic models for consumption.

## Consequences

Business users get simpler, safer data. Engineers keep auditability and flexibility. The trade-off is extra governance and documentation.

## Alternatives Considered

Expose all tables to all users, or build Power BI directly from raw files.

## Recommendation

Make Gold and certified semantic models the default consumption path.
