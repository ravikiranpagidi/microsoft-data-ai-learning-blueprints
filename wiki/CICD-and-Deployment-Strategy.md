# CI/CD and Deployment Strategy

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply ci/cd and deployment strategy to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Naming Standards](Naming-Standards) | [Home](Home) | [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain CI/CD and deployment strategy for Fabric projects, including Git integration, deployment pipelines, environment configuration, and release checklist thinking.

## Who Should Read This

Open-source maintainers, enterprise teams, architects, and engineers moving from manual demo work to governed delivery.

## Why CI/CD Matters

CI/CD makes changes reviewable, repeatable, and safer. Without it, Fabric projects often depend on manual notebook edits, undocumented SQL changes, and unclear promotion steps.

## Git Integration

Git integration helps version supported Fabric artifacts and documentation. It allows teams to review changes, track history, and collaborate using pull requests.

## Deployment Pipelines

Deployment pipelines help promote Fabric content across environments such as Dev, Test, and Prod. They are useful for controlled movement of artifacts and environment-specific configuration.

## Deployment Flow

~~~mermaid
flowchart LR
    Dev[Dev Workspace] --> PR[Pull Request Review]
    PR --> Test[Test Workspace]
    Test --> Validate[Data Quality and Report Validation]
    Validate --> Release[Release Approval]
    Release --> Prod[Prod Workspace]
~~~

## Environment Configuration

Do not hardcode production paths in notebooks. Use parameters for workspace, Lakehouse, source path, batch ID, and environment where possible.

## What Should Be Version Controlled

- Notebooks
- SQL scripts
- Pipeline templates
- Data quality rules
- Documentation
- Architecture diagrams
- ADRs
- Release checklists

## What Should Not Be Version Controlled

- Secrets
- Personal access tokens
- Large production data extracts
- Environment-specific credentials
- Generated runtime logs unless intentionally published

## Release Checklist

A release should confirm tests, data quality, SQL validation, semantic model impact, access review, documentation updates, and rollback plan.

## Best Practices

- Separate Dev, Test, and Prod workspaces.
- Use pull requests for repo changes.
- Validate data quality before promotion.
- Keep release notes.
- Document manual steps that cannot be automated yet.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Editing production directly | Changes are not reviewable | Promote from Dev/Test. |
| Storing secrets in repo | Security risk | Use secure configuration. |
| No release checklist | Missed validation | Require checklist before Prod. |

## Official Reference

- [Dataflow Gen2 CI/CD and Git integration](https://learn.microsoft.com/en-us/fabric/data-factory/dataflow-gen2-cicd-and-git-integration)

## Related Repo Files

- [cicd/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/cicd)
- [.github/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/.github)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/data-quality/dq_rules.yml)
- [adr/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/adr)

## Related Wiki Pages

- [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy)
- [Performance and Optimization](Performance-and-Optimization)
- [Fabric Decision Guide](Fabric-Decision-Guide)

## Summary Checklist

- [ ] Supported artifacts are version controlled.
- [ ] Secrets are not committed.
- [ ] Dev/Test/Prod promotion is defined.
- [ ] Release checklist is used.
- [ ] Rollback considerations are documented.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Naming Standards](Naming-Standards) | [Home](Home) | [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
