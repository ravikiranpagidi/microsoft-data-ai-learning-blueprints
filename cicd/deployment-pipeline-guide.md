# Deployment Pipeline Guide

## Concept

Fabric deployment pipelines help promote content between lifecycle stages such as Dev, Test, and Prod.

## Recommended Stages

| Stage | Purpose | Users |
| --- | --- | --- |
| Dev | Build and experiment | Engineers and model authors |
| Test | Validate with controlled data and users | Engineers, stewards, UAT users |
| Prod | Stable certified consumption | Business users and operations |

## Promotion Process

~~~mermaid
flowchart LR
    dev["Dev workspace"] --> review["Pull request and review"]
    review --> test["Deploy to Test"]
    test --> validate["DQ, reconciliation, UAT"]
    validate --> approval["Owner approval"]
    approval --> prod["Deploy to Prod"]
~~~

## Gates

- Notebooks run successfully.
- Data quality checks pass.
- SQL views validate.
- Semantic model relationships and measures reviewed.
- PII exposure reviewed.
- Owner approval captured.

## Recommendation

Keep deployment pipeline promotion boring and repeatable. Surprises belong in Dev, not Prod.
