# Microsoft Learning Blueprints

> A practical, community-friendly learning hub for Microsoft data, analytics, AI, cloud, and business application tutorials.

This repository is being organized as a single home for Microsoft learning projects. Each major topic lives in its own folder so the community can star, fork, watch, and contribute to one central repository while still keeping every learning path clean and focused.

The first blueprint in this collection is the **Microsoft Fabric Data Engineering Blueprint**, an end-to-end Retail Banking Customer Analytics project that teaches Fabric Lakehouse, OneLake, Data Pipelines, Notebooks, PySpark, Delta tables, SQL Analytics Endpoint, Power BI consumption, governance, CI/CD, and enterprise-ready project structure.

## Why This Repo Uses Topic Folders

A single-topic repository is easy to start, but a topic-folder structure scales better for a public Microsoft learning portfolio.

| Benefit | Why It Matters |
| --- | --- |
| One community home | Stars, forks, issues, pull requests, and discussions can grow around one main repository. |
| Clear topic separation | Each Microsoft topic has its own folder, README, examples, docs, and roadmap. |
| Easier discovery | Learners can browse one repo and choose the path that matches their current goal. |
| Better contribution flow | Contributors can add a topic, improve an existing blueprint, or submit focused examples. |
| Portfolio friendly | The repo can support articles, YouTube demos, meetup sessions, and interview preparation across multiple Microsoft technologies. |

## Current Learning Blueprints

| Folder | Topic | Status | Best For |
| --- | --- | --- | --- |
| [fabric-data-engineering-blueprint](fabric-data-engineering-blueprint/README.md) | Microsoft Fabric Data Engineering | Active | Fabric beginners, Azure data engineers, Power BI developers, architects, students, and enterprise proof-of-concept teams |

## Featured Blueprint

### Microsoft Fabric Data Engineering Blueprint

[Open the Fabric blueprint](fabric-data-engineering-blueprint/README.md)

This blueprint teaches a complete Fabric data engineering flow:

```text
Source CSV files
-> Fabric Data Pipeline
-> Lakehouse Files
-> Bronze Delta tables
-> Silver cleaned Delta tables
-> Gold dimensional model
-> SQL Analytics Endpoint views
-> Power BI semantic model guidance
-> Business dashboard recommendations
```

It uses a **Retail Banking Customer Analytics** sample domain with customers, accounts, products, transactions, branches, and dates.

## Suggested Future Topics

These folders can be added later using the same blueprint style:

| Future Folder | Possible Topic |
| --- | --- |
| `power-bi-semantic-modeling-blueprint/` | Power BI modeling, DAX, relationships, deployment, and governance |
| `azure-data-engineering-blueprint/` | Azure Data Factory, ADLS Gen2, Synapse, Databricks, and orchestration patterns |
| `microsoft-purview-governance-blueprint/` | Catalog, lineage, classification, ownership, and governance operating model |
| `fabric-real-time-intelligence-blueprint/` | Eventstreams, KQL databases, real-time dashboards, and operational analytics |
| `azure-ai-data-blueprint/` | AI-ready data engineering, vector search, RAG data preparation, and responsible AI patterns |

## Repository Layout

```text
.
|-- README.md
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- LICENSE
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- pull_request_template.md
`-- fabric-data-engineering-blueprint/
    |-- README.md
    |-- docs/
    |-- architecture/
    |-- sample-data/
    |-- notebooks/
    |-- pipelines/
    |-- sql/
    |-- data-quality/
    |-- semantic-model/
    |-- governance/
    |-- cicd/
    |-- adr/
    |-- interview-guide/
    |-- roadmap/
    |-- community/
    `-- wiki/
```

## How To Use This Repository

1. Start at the topic table above.
2. Open the blueprint folder that matches what you want to learn.
3. Read that folder's README first.
4. Follow the hands-on setup steps inside the topic folder.
5. Use the issue templates to report problems or request new examples.
6. Use the pull request template when contributing improvements.

## Contribution Model

Contributions are welcome when they improve learning value, implementation quality, or enterprise usefulness.

Good contributions include:

- New Microsoft learning blueprints.
- Better diagrams and decision guides.
- Beginner-friendly explanations.
- Hands-on notebooks, scripts, sample data, or templates.
- Governance, CI/CD, security, and production readiness examples.
- Interview preparation questions and practical exercises.
- Fixes for broken links, typos, unclear wording, or outdated guidance.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Professional Note

This repository is intended to grow into a serious Microsoft learning collection. The goal is to keep each topic practical enough for learners, structured enough for practitioners, and thoughtful enough for architects and enterprise teams.

If a blueprint helps you, consider starring the repository, sharing it with other learners, and contributing improvements back to the community.
