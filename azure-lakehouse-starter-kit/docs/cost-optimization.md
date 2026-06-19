# Cost Optimization

## Purpose

Give practical cost guidance for ADF, Databricks, storage, and operations.

## ADF

- Avoid unnecessary pipeline activity loops.
- Use metadata to reduce duplicated pipelines.
- Monitor copy duration and data movement costs.
- Schedule loads based on business need.

## Databricks

- Use job clusters for scheduled workloads.
- Use all-purpose clusters for development only.
- Enable autoscaling where useful.
- Use smaller clusters for small starter-kit data.
- Terminate idle clusters.
- Consider spot instances for fault-tolerant workloads.

## Delta And Storage

- Avoid small files.
- Compact tables when needed.
- Partition only when useful.
- Use lifecycle policies for raw and archive zones.
- Track storage growth by layer.

## Governance

- Tag Azure resources by environment, owner, cost center, and workload.
- Review unused resources monthly.
- Monitor job failures and retries.
