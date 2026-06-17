# Governance Checklist

Use this checklist before publishing Gold tables, SQL views, semantic models, or reports.

## Data Classification

- [ ] Tables and columns classified.
- [ ] PII fields identified.
- [ ] Confidential financial fields identified.
- [ ] Classification reviewed by data steward.

## Access

- [ ] Bronze access limited to engineering and approved audit roles.
- [ ] Silver access limited to engineering and stewards.
- [ ] Gold access granted through groups.
- [ ] Semantic model access approved by owner.
- [ ] Export permissions reviewed.

## Quality

- [ ] Required data quality checks pass.
- [ ] Row counts reconciled.
- [ ] Freshness checked.
- [ ] Known issues documented.

## Ownership

- [ ] Data owner assigned.
- [ ] Data steward assigned.
- [ ] Support contact documented.
- [ ] Metric definitions approved.

## Release

- [ ] Changes tested in non-production workspace.
- [ ] Deployment checklist completed.
- [ ] Release notes prepared.
- [ ] Rollback plan documented.
