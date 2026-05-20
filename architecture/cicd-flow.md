# CI/CD Flow

This architecture shows how Fabric items should move across environments.

~~~mermaid
flowchart LR
    repo["Git repository<br/>notebooks, SQL, docs, rules"] --> dev["Dev workspace<br/>fab-retailbank-dev"]
    dev --> test["Test workspace<br/>fab-retailbank-test"]
    test --> prod["Prod workspace<br/>fab-retailbank-prod"]
    dev --> validate["Unit checks<br/>notebook smoke test"]
    test --> qa["Data quality<br/>UAT and reconciliation"]
    prod --> monitor["Operational monitoring<br/>refresh and freshness"]
~~~

## Promotion Gates

| Stage | Gate |
| --- | --- |
| Dev | Code reviewed, no secrets, notebooks run with sample data |
| Test | Data quality passes, SQL views validate, semantic model relationships reviewed |
| Prod | Release approved, owner notified, monitoring enabled |

## Recommendation

Do not edit production directly. Use Dev for changes, Test for validation, and Prod for stable consumption.
