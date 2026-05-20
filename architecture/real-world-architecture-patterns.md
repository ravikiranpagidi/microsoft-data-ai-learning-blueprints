# Real-World Architecture Patterns

This catalog shows how the same Fabric blueprint can scale from a small learning project to enterprise patterns.

## Pattern 1: Small Team Pattern

Use this when a small analytics team is building its first Fabric proof of concept.

~~~mermaid
flowchart LR
    files["CSV or source exports"] --> lakehouse["Single Lakehouse"]
    lakehouse --> notebooks["Notebooks"]
    notebooks --> gold["Gold tables"]
    gold --> model["Power BI semantic model"]
    model --> report["Team report"]
~~~

Recommended setup:

- One Dev workspace.
- One Lakehouse.
- Manual or simple pipeline ingestion.
- Bronze, Silver, and Gold tables.
- One shared semantic model.
- Lightweight governance checklist.

When to evolve: move to the enterprise pattern when more than one team depends on the data or production refresh becomes business-critical.

## Pattern 2: Enterprise Pattern

Use this when multiple teams, environments, governed releases, and production support are required.

~~~mermaid
flowchart LR
    repo["Git repository"] --> dev["Dev workspace"]
    dev --> test["Test workspace"]
    test --> prod["Prod workspace"]
    prod --> certified["Certified semantic models"]
    certified --> reports["Managed reports"]
    governance["Governance and security"] --> dev
    governance --> test
    governance --> prod
~~~

Recommended setup:

- Dev, Test, and Prod workspaces.
- Git integration and deployment pipelines.
- Data quality gates before production refresh.
- Microsoft Entra groups for role-based access.
- Certified semantic models.
- Release checklist and rollback plan.

Key risk: treating a proof of concept as production without adding ownership, access review, monitoring, and deployment controls.

## Pattern 3: Data Product Pattern

Use this when a domain team owns a reusable data asset for other teams.

~~~mermaid
flowchart TB
    domain["Retail Banking domain"] --> product["Customer Analytics data product"]
    product --> contract["Data contract"]
    product --> quality["Quality rules"]
    product --> gold["Gold facts and dimensions"]
    product --> semantic["Certified semantic model"]
    semantic --> consumers["Consumers and downstream teams"]
~~~

Recommended setup:

- Named data owner and steward.
- Published data contract.
- Gold tables with stable grains and keys.
- Quality rules stored with the product.
- Business glossary and metric definitions.
- Support and change management process.

Key success measure: consumers can understand what the data means, how fresh it is, who owns it, and how to request changes.

## Pattern 4: Self-Service BI Pattern

Use this when analysts need safe flexibility without raw-data exposure.

~~~mermaid
flowchart LR
    bronze["Bronze restricted"] --> silver["Silver stewarded"]
    silver --> gold["Gold certified"]
    gold --> views["SQL views"]
    gold --> model["Shared semantic model"]
    views --> analysts["Approved analysts"]
    model --> reportAuthors["Report authors"]
~~~

Recommended setup:

- Bronze and Silver restricted.
- Gold tables and SQL views available to approved analysts.
- Shared semantic model for most report authors.
- Measure definitions owned centrally.
- Endorsement and certification process.

Key risk: letting self-service become self-sourced. Self-service should mean flexible consumption of governed data, not unmanaged raw access.

## Pattern 5: AI-Ready Lakehouse Pattern

Use this when curated data will support machine learning, semantic search, copilots, or analytics agents.

~~~mermaid
flowchart LR
    sources["Operational and analytical sources"] --> lakehouse["Lakehouse"]
    lakehouse --> silver["Clean Silver data"]
    silver --> gold["Business Gold model"]
    silver --> features["Feature-ready tables"]
    gold --> semantics["Business glossary and metrics"]
    features --> ai["ML and AI workloads"]
    semantics --> ai
~~~

Recommended setup:

- High-quality Silver tables with stable business keys.
- Gold tables with approved business definitions.
- PII classification and masking before AI use.
- Data freshness and lineage documented.
- Feature-ready tables separated from BI-only tables when needed.
- Clear approval path for sensitive attributes.

Key risk: sending raw, sensitive, or poorly defined data into AI workflows. AI-ready means governed, documented, and quality checked.

## Pattern Selection Matrix

| Situation | Recommended pattern |
| --- | --- |
| First proof of concept | Small team pattern |
| Business-critical reporting | Enterprise pattern |
| Domain-owned reusable data | Data product pattern |
| Analyst enablement | Self-service BI pattern |
| ML, copilots, or semantic search | AI-ready lakehouse pattern |
