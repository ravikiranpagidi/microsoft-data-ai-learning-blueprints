# Delta Lake Table Design

## Purpose

Explain practical Delta Lake design choices.

## Best Practices

- Use Delta format for Bronze, Silver, and Gold.
- Partition only when it improves pruning.
- Avoid over-partitioning low-cardinality or small tables.
- Use `MERGE` for upserts.
- Optimize large frequently queried tables.
- Use Z-order where appropriate for common filters.
- Use Vacuum carefully and respect retention requirements.
- Track audit columns such as `ingestion_timestamp`, `batch_id`, and `source_file`.
- Use table comments and metadata.
- Use time travel for recovery.
- Consider change data feed for downstream incremental consumers.

## Example Merge

```sql
MERGE INTO dim_customer AS target
USING silver_customers AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

## Example Optimize

```sql
OPTIMIZE fact_sales ZORDER BY (customer_id, product_id);
```
