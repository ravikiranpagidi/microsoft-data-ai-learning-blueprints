# Fabric Project Checklist

Use this checklist to move from a learning project to a reliable Microsoft Fabric implementation.

## Workspace Setup

- [ ] Workspace purpose documented.
- [ ] Environment identified: Dev, Test, or Prod.
- [ ] Capacity assigned and understood.
- [ ] Workspace admins limited.
- [ ] Microsoft Entra groups used for access.
- [ ] Support owner documented.

## Naming Standards

- [ ] Workspace follows naming standard.
- [ ] Lakehouse follows naming standard.
- [ ] Pipelines use action-based names.
- [ ] Notebooks use numeric execution order.
- [ ] Tables use Bronze, Silver, Gold prefixes or dimensional names.
- [ ] SQL views use business-friendly names.
- [ ] Semantic model and report names are clear.

## Lakehouse Setup

- [ ] Lakehouse created in correct workspace.
- [ ] Files and Tables areas understood.
- [ ] Source folder structure created.
- [ ] Bronze, Silver, and Gold table strategy documented.
- [ ] Shortcut strategy documented if shortcuts are used.
- [ ] Sensitive data location reviewed.

## Data Ingestion

- [ ] Source files or systems identified.
- [ ] Ingestion frequency documented.
- [ ] Batch ID strategy defined.
- [ ] Source-to-Bronze row count logged.
- [ ] Missing file handling defined.
- [ ] Retry and alerting behavior documented.

## Transformation

- [ ] Bronze preserves raw data and lineage metadata.
- [ ] Silver cleans column names and data types.
- [ ] Silver removes duplicates by business key.
- [ ] Silver standardizes status and category values.
- [ ] Gold model grain is documented.
- [ ] Gold facts and dimensions have stable keys.

## Data Quality

- [ ] Not-null checks defined.
- [ ] Duplicate checks defined.
- [ ] Accepted value checks defined.
- [ ] Range checks defined.
- [ ] Referential integrity checks defined.
- [ ] Row count reconciliation implemented.
- [ ] Freshness checks implemented.
- [ ] Critical failures block consumption refresh.

## Security

- [ ] PII fields identified.
- [ ] Data classification completed.
- [ ] Least privilege access applied.
- [ ] Bronze and Silver access restricted.
- [ ] Gold access approved by data owner.
- [ ] Export permissions reviewed.
- [ ] Row-level security considered for Power BI.

## Governance

- [ ] Data owner assigned.
- [ ] Data steward assigned.
- [ ] Business glossary published.
- [ ] Metric definitions approved.
- [ ] Data quality owner identified.
- [ ] Change request process documented.
- [ ] Lineage and dependencies reviewed.

## Power BI Consumption

- [ ] Star schema relationships created.
- [ ] Date table marked.
- [ ] Surrogate keys hidden from report view.
- [ ] Measures defined centrally.
- [ ] Direct Lake vs Import decision documented.
- [ ] Certified semantic model considered.
- [ ] Reports use Gold tables or governed views.

## CI/CD

- [ ] Git integration strategy documented.
- [ ] Deployment path defined.
- [ ] Dev, Test, Prod workspaces identified.
- [ ] Environment-specific configuration separated.
- [ ] Pull request review process defined.
- [ ] Release checklist used.
- [ ] Rollback approach documented.

## Production Readiness

- [ ] End-to-end pipeline tested.
- [ ] Data quality passed.
- [ ] SQL views validated.
- [ ] Semantic model refreshed.
- [ ] Business owner approved metrics.
- [ ] Monitoring or operational checks defined.
- [ ] Support process documented.
- [ ] Known limitations published.
