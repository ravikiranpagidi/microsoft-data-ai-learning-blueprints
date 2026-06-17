# Contributor Guide

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply contributor guide to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [90-Day Professional Growth Plan](90-Day-Professional-Growth-Plan) | [Home](Home) | [FAQ](FAQ)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary)

## Purpose

Explain how community members can contribute high-quality documentation, notebooks, SQL, sample data, patterns, and examples.

## Who Should Read This

Open-source contributors, maintainers, learners, and community members who want to improve the project.

## Contribution Philosophy

This repo should feel like a serious open-source learning platform. Contributions should be clear, practical, beginner-friendly, and aligned with Microsoft Fabric Data Engineering patterns.

## Types of Contributions Welcome

- Documentation improvements.
- Wiki page improvements.
- Notebook examples.
- SQL metrics and validation queries.
- Data quality rules.
- Architecture diagrams.
- Interview questions.
- Roadmap improvements.
- Governance and CI/CD examples.
- Additional realistic sample domains.

## Adding Documentation

Use clear headings, short explanations, practical examples, best practices, common mistakes, related links, and a checklist. Avoid vague statements that do not help a reader act.

## Adding Notebooks

Notebook contributions should include title, purpose, prerequisites, markdown explanation, clean PySpark code, logging, validation, expected output, and next steps. Keep code educational but realistic.

## Adding Sample Data

Sample data should be small, realistic, and safe. Do not add real customer data. Update DQ rules, notebooks, SQL scripts, and docs if relationships change.

## Adding Architecture Patterns

Architecture patterns should include use case, diagram, pros, cons, and when to choose. If the pattern changes a major design decision, add an ADR.

## Opening Issues

Good issues include:

- Clear title.
- What needs to change.
- Why it matters.
- Suggested files or pages.
- Screenshots or examples if relevant.

## Pull Request Expectations

- Keep PRs focused.
- Explain the change and why it matters.
- Update related docs.
- Validate notebook JSON if notebooks change.
- Run basic syntax checks for Python and YAML.
- Avoid unrelated formatting churn.

## Code Style

- Use readable PySpark.
- Prefer explicit column names.
- Add comments only where they clarify non-obvious logic.
- Keep paths parameterized where practical.
- Avoid secrets and real data.

## Documentation Style

- Professional and beginner-friendly.
- Practical over theoretical.
- Enterprise-aware without being heavy.
- Clear examples over generic claims.
- Include common mistakes and checklists.

## Community Standards

Be respectful, constructive, and specific. Help learners feel capable. Review with the goal of improving the resource, not showing superiority.

## Good First Contributions

| Contribution | Files to touch | Why it helps |
| --- | --- | --- |
| Add a new FAQ item | FAQ.md | Helps beginners unblock quickly. |
| Add an interview scenario | Interview-Preparation-Guide.md and interview-guide folder | Makes the repo stronger for job seekers. |
| Add a validation query | sql/validation_queries.sql | Improves implementation trust. |
| Add a DQ rule | data-quality/dq_rules.yml | Improves production readiness. |
| Improve a decision table | Fabric-Decision-Guide.md | Helps architects and practitioners choose well. |
| Add a sample dashboard recommendation | semantic-model or docs | Helps Power BI learners. |

## Pull Request Review Checklist

- [ ] The contribution is specific to Fabric and this Retail Banking blueprint.
- [ ] The change includes practical examples, not only theory.
- [ ] Any new table, column, or metric is documented.
- [ ] Any new sample data is synthetic and safe.
- [ ] Any notebook change includes explanation and validation.
- [ ] Any architecture change updates or adds an ADR if needed.
- [ ] The PR description explains why the change helps the community.

## Documentation Voice

Write like a senior teammate teaching a capable beginner. Be direct, concrete, and kind. Avoid generic claims like enterprise-ready unless the page explains exactly what makes it enterprise-ready.

## Related Repo Files

- [CONTRIBUTING.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/CODE_OF_CONDUCT.md)
- [.github/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/.github)
- [community/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/community)

## Related Wiki Pages

- [Architecture Decision Records Guide](Architecture-Decision-Records-Guide)
- [Interview Preparation Guide](Interview-Preparation-Guide)
- [FAQ](FAQ)
- [Glossary](Glossary)

## Summary Checklist

- [ ] I read the contribution guidelines.
- [ ] My contribution is focused and practical.
- [ ] Related docs are updated.
- [ ] No real sensitive data is included.
- [ ] The PR explains why the change matters.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [90-Day Professional Growth Plan](90-Day-Professional-Growth-Plan) | [Home](Home) | [FAQ](FAQ) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary)
