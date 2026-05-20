# Contributing

Thank you for considering a contribution to the Microsoft Fabric Data Engineering Blueprint.

This project is designed to be practical, beginner-friendly, and useful for real teams. Contributions should improve learning value, implementation quality, or enterprise readiness.

## Contribution Philosophy

This repository should feel like a community blueprint, not a personal notes folder. Contributions should be practical, teachable, and safe for real teams to adapt.

Good contributions usually do at least one of these things:

- Help beginners understand a Fabric concept faster.
- Help engineers implement a pattern with less guesswork.
- Help architects explain trade-offs clearly.
- Help teams avoid governance, CI/CD, security, or quality mistakes.
- Add a reusable example that can be run or adapted.

## Good Contribution Ideas

- Add a new business scenario using the same repository pattern.
- Improve PySpark notebooks with clearer validation or incremental load examples.
- Add new SQL analytics endpoint views.
- Add data quality rules and test cases.
- Improve governance, CI/CD, or security guidance.
- Add Power BI report design screenshots or semantic model examples.
- Add interview questions with practical answers.
- Add architecture decision guides or real-world patterns.
- Add monitoring, audit, or operational examples.
- Fix typos, broken links, or unclear explanations.

## Contribution Types

| Type | Good example | Review focus |
| --- | --- | --- |
| Documentation | Add Direct Lake vs Import guidance | Accuracy, clarity, official references |
| Notebook | Add incremental load pattern | Fabric compatibility, comments, validation |
| SQL | Add branch activity ranking query | Business usefulness, readable naming |
| Data quality | Add freshness or reconciliation rule | Pass/fail clarity, operational value |
| Governance | Add PII classification template | Practical enterprise fit |
| CI/CD | Add deployment checklist details | Environment safety and repeatability |
| Community | Add blog/video demo plan | Learning value and repo visibility |

## Contribution Standards

Before submitting a pull request:

1. Keep examples beginner-friendly.
2. Prefer small, focused changes.
3. Avoid committing secrets, tenant IDs, workspace IDs, or production data.
4. Make sure sample code has comments where a beginner would need help.
5. Update documentation when behavior changes.
6. Use consistent naming conventions from <code>governance/naming-standards.md</code>.
7. Explain why the change is useful.
8. Cite official Microsoft documentation when describing current Fabric platform behavior.
9. Keep examples synthetic and safe for public repositories.

## How To Open a Good Issue

Use the GitHub issue templates:

- Bug report: incorrect behavior, broken code, bad link, or failing example.
- Feature request: new guide, pattern, or capability.
- Documentation improvement: unclear, outdated, or missing explanation.
- New example request: notebook, SQL, pipeline, governance, or architecture example.

High-quality issues include:

- The file or section affected.
- The expected outcome.
- The audience who benefits.
- Official documentation links when platform behavior is involved.

## Pull Request Expectations

Use the pull request template in <code>.github/pull_request_template.md</code>.

Before opening a pull request:

- Keep the change focused.
- Update index files such as README or folder README files when adding new content.
- Run lightweight validation when possible:
  - Notebook files should be valid JSON.
  - JSON pipeline templates should parse.
  - Python files should compile.
  - CSV files should parse.
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
- Prefer Fabric-compatible PySpark patterns.

## SQL Style

- Use business-friendly aliases.
- Include comments that explain the business question.
- Avoid exposing PII in broad consumption examples.
- Keep validation queries separate from business metric queries.

## Code of Conduct

All contributors are expected to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
