# Common Enterprise Mistakes

This guide explains common mistakes teams make when moving from a Fabric demo to an enterprise implementation, and how to correct them.

## Mistake 1: Treating Fabric as Only a Power BI Feature

What happens: teams create reports quickly but skip lakehouse design, quality gates, ownership, and deployment planning.

Why it hurts: Power BI becomes the place where data is cleaned, joined, interpreted, and redefined. Metrics drift across reports.

Correction: use Fabric as an analytics platform. Build Lakehouse layers, publish Gold tables, define metrics in semantic models, and document ownership.

## Mistake 2: Giving Everyone Workspace Admin Access

What happens: a proof of concept moves quickly because everyone can do everything.

Why it hurts: production data, PII, models, pipelines, and reports become vulnerable to accidental changes or overexposure.

Correction: use Microsoft Entra groups, workspace roles, item permissions, and least privilege. Make Admin access rare.

## Mistake 3: Building Reports on Bronze Data

What happens: users connect to raw tables or files because the data is available.

Why it hurts: raw data can contain duplicates, nulls, invalid keys, inconsistent status values, and sensitive fields.

Correction: keep Bronze restricted. Publish Gold facts, dimensions, SQL views, and certified semantic models for consumption.

## Mistake 4: Skipping Data Quality Until Users Complain

What happens: pipelines load successfully but business users find broken totals, missing dimensions, or stale data.

Why it hurts: trust is hard to rebuild after a dashboard is wrong.

Correction: add data quality checks as a release gate. Validate keys, duplicates, accepted values, ranges, freshness, and reconciliation before refresh.

## Mistake 5: Hardcoding Environment Values

What happens: notebooks and pipelines contain workspace names, Lakehouse IDs, file paths, or production-specific settings.

Why it hurts: promotion from Dev to Test to Prod becomes manual and fragile.

Correction: parameterize environment, batch ID, source path, and runtime settings. Keep environment-specific configuration documented.

## Mistake 6: Creating Too Many Semantic Models

What happens: every report author creates a separate model with slightly different relationships and measures.

Why it hurts: the organization gets multiple versions of the truth.

Correction: create shared certified semantic models for core data products. Allow local models only for clear exploratory or specialized needs.

## Mistake 7: Confusing Pipeline Success with Data Success

What happens: a pipeline run is green, so the team assumes the data is correct.

Why it hurts: a pipeline can finish even when the data is incomplete, duplicated, late, or semantically wrong.

Correction: track both operational status and data quality status. A production refresh should depend on quality outcomes, not just activity completion.

## Mistake 8: Overusing Wide Tables

What happens: teams flatten every reporting need into one large table.

Why it hurts: wide tables duplicate attributes, obscure grain, reduce reuse, and make semantic models harder to govern.

Correction: use a star schema for reusable analytics. Create views or aggregation tables only when there is a clear performance or usability reason.

## Mistake 9: Ignoring PII in Early Design

What happens: names, emails, phone numbers, date of birth, and account identifiers flow into broad reporting layers.

Why it hurts: sensitive data exposure becomes embedded in reports, exports, and downstream models.

Correction: classify fields early. Exclude, mask, aggregate, or restrict PII before publishing Gold views and semantic models.

## Mistake 10: No Release Checklist

What happens: changes are promoted based on memory, chats, or urgent requests.

Why it hurts: production becomes inconsistent and difficult to support.

Correction: use a release checklist covering code review, quality checks, governance, semantic model validation, approval, deployment, and monitoring.

## Enterprise Readiness Rule

A Fabric solution is not production-ready because it has a dashboard. It is production-ready when the data has ownership, quality, security, documentation, deployment discipline, and support expectations.
