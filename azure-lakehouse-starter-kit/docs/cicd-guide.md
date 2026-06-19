# CI/CD Guide

## Purpose

Describe how to validate and deploy ADF and Databricks assets.

## CI Checks

- Validate folder structure.
- Validate JSON artifacts.
- Compile Python notebooks.
- Run unit tests.
- Validate notebook syntax.
- Check for obvious secret placeholders.

## Deployment Targets

| Asset | Deployment Pattern |
| --- | --- |
| ADF pipelines | ARM, REST, Azure CLI, or ADF publish pattern |
| Databricks notebooks | Databricks CLI or workspace import |
| Databricks jobs | Jobs API or Databricks Asset Bundles |
| Config | Environment-specific variable files or secure pipeline variables |

## Environment Strategy

- Dev for active engineering.
- Test for integration validation.
- Prod for approved releases.
- Manual approval before production.

## Secrets

Use Azure DevOps variable groups, GitHub Actions secrets, Key Vault, or managed identities. Do not store secrets in JSON artifacts or notebooks.
