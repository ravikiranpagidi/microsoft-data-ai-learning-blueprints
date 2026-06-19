# Delta Lake

## Purpose

Delta Lake provides reliable table storage for Bronze, Silver, and Gold layers.

## Why Delta Matters

- ACID transactions
- Schema enforcement and evolution
- Time travel
- Efficient incremental processing patterns
- Reliable BI and data science consumption

## Starter Kit Usage

| Layer | Delta Pattern |
| --- | --- |
| Bronze | Append raw data with ingestion metadata |
| Silver | Overwrite or merge clean current-state tables |
| Gold | Publish dimensional and analytics-ready tables |

## Practical Guidance

- Avoid too many small files.
- Partition only when it clearly improves common filters.
- Use `OPTIMIZE` for frequently queried Gold tables.
- Use `VACUUM` with a retention policy approved by the platform team.
- Do not use Delta as a reason to skip data modeling.

## Related Pages

- [Medallion Design](Medallion-Design)
- [Performance guidance in docs](../docs/cost-optimization.md)
- [Data Quality](Data-Quality)

