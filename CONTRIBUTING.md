# Contributing

Thank you for considering a contribution to this Microsoft learning repository.

This repo is organized as a collection of focused Microsoft learning blueprints. Each topic should be practical, beginner-friendly, and useful for real teams. Contributions should improve learning value, implementation quality, architecture clarity, or enterprise readiness.

## Contribution Philosophy

This repository should feel like a community learning hub, not a personal notes folder. Contributions should be practical, teachable, and safe for real teams to adapt.

Good contributions usually do at least one of these things:

- Help beginners understand a Microsoft platform concept faster.
- Help engineers implement a pattern with less guesswork.
- Help architects explain trade-offs clearly.
- Help teams avoid governance, CI/CD, security, or quality mistakes.
- Add a reusable example that can be run or adapted.

## Good Contribution Ideas

- Add a new Microsoft topic folder using the same blueprint pattern.
- Add a new business scenario inside an existing topic.
- Improve notebooks, scripts, templates, or examples with clearer validation.
- Add new SQL, DAX, KQL, Python, or configuration examples where relevant.
- Add data quality rules, test cases, or validation guidance.
- Improve governance, CI/CD, or security guidance.
- Add Power BI report design, semantic model, or measure examples.
- Add interview questions with practical answers.
- Add architecture decision guides or real-world patterns.
- Add monitoring, audit, or operational examples.
- Fix typos, broken links, or unclear explanations.

## Contribution Types

| Type | Good Example | Review Focus |
| --- | --- | --- |
| Documentation | Add Direct Lake vs Import guidance | Accuracy, clarity, official references |
| Notebook | Add incremental load pattern | Platform compatibility, comments, validation |
| SQL or DAX | Add branch activity ranking query or measure | Business usefulness, readable naming |
| Data quality | Add freshness or reconciliation rule | Pass/fail clarity, operational value |
| Governance | Add PII classification template | Practical enterprise fit |
| CI/CD | Add deployment checklist details | Environment safety and repeatability |
| Community | Add blog or video demo plan | Learning value and repo visibility |
| New topic | Add a new Microsoft blueprint folder | Folder structure, scope, README quality, runnable examples |

## Contribution Standards

Before submitting a pull request:

1. Keep examples beginner-friendly.
2. Prefer small, focused changes.
3. Avoid committing secrets, tenant IDs, workspace IDs, or production data.
4. Make sure sample code has comments where a beginner would need help.
5. Update documentation when behavior changes.
6. Use consistent naming conventions from the relevant topic folder.
7. Explain why the change is useful.
8. Cite official Microsoft documentation when describing current platform behavior.
9. Keep examples synthetic and safe for public repositories.

## Topic Folder Standards

Each major topic should live in its own folder at the repository root.

A strong topic folder usually includes:

- `README.md` with purpose, audience, learning path, setup, and project flow.
- `docs/` for concept explanations and decision guides.
- `sample-data/` or sample inputs when needed.
- `notebooks/`, `sql/`, `scripts/`, `powerbi/`, or equivalent implementation folders when relevant.
- `architecture/` for diagrams and patterns.
- `governance/` or `cicd/` guidance when the topic is enterprise-oriented.
- `roadmap/` or learning plan material when useful.

Keep topic folders independent enough that a learner can open one folder and understand how to run or study that blueprint.

## How To Open a Good Issue

Use the GitHub issue templates:

- Bug report: incorrect behavior, broken code, bad link, or failing example.
- Feature request: new guide, pattern, or capability.
- Documentation improvement: unclear, outdated, or missing explanation.
- New example request: notebook, SQL, pipeline, DAX, KQL, governance, or architecture example.

High-quality issues include:

- The topic folder or section affected.
- The expected outcome.
- The audience who benefits.
- Official documentation links when platform behavior is involved.

## Pull Request Expectations

Use the pull request template in `.github/pull_request_template.md`.

Before opening a pull request:

- Keep the change focused.
- Update index files such as the root README or topic README files when adding new content.
- Run lightweight validation when possible:
  - Notebook files should be valid JSON.
  - JSON templates should parse.
  - Python files should compile.
  - CSV files should parse.
  - SQL, DAX, KQL, or scripts should be reviewed.
  - Links should be reviewed.
- Avoid unrelated formatting churn.

## Documentation Style

- Use clear, direct language.
- Avoid unexplained acronyms.
- Include practical examples.
- Keep tables and diagrams readable in GitHub.
- Prefer implementation guidance over vague recommendations.
- When explaining a decision, include when to use it, when not to use it, and the practical recommendation.
- When writing for beginners, explain the mental model before the implementation detail.

## Notebook Style

- Include purpose, prerequisites, and expected outputs.
- Keep code cells focused.
- Add comments where a beginner would need context.
- Log row counts and validation results.
- Avoid tenant-specific IDs, secrets, and production paths.
- Prefer platform-compatible patterns for the topic.

## SQL, DAX, and Script Style

- Use business-friendly aliases.
- Include comments that explain the business question.
- Avoid exposing PII in broad consumption examples.
- Keep validation queries separate from business metric queries.

## Code of Conduct

All contributors are expected to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
