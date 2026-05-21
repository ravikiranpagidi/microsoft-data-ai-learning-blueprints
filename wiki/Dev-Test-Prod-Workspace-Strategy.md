# Dev/Test/Prod Workspace Strategy

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply dev/test/prod workspace strategy to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy) | [Home](Home) | [Performance and Optimization](Performance-and-Optimization)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain why Fabric projects should use separate Dev, Test, and Prod workspaces and how to promote changes safely.

## Who Should Read This

Enterprise teams, platform owners, architects, and engineers preparing production Fabric deployments.

## Why Separate Workspaces?

Separate workspaces reduce risk. Development is where engineers experiment. Test is where changes are validated. Production is where business users rely on stable outputs. Mixing them increases the chance of breaking reports or exposing unfinished data.

## Environment Isolation

| Environment | Purpose | Typical users |
| --- | --- | --- |
| Dev | Build and experiment | Engineers and contributors |
| Test | Validate data, reports, security, and performance | Engineers, stewards, testers |
| Prod | Serve approved business users | Business users, analysts, support |

## Naming Strategy

Use consistent names such as:

- fabric-de-blueprint-dev
- fabric-de-blueprint-test
- fabric-de-blueprint-prod

Lakehouse examples:

- lh_retail_banking_dev
- lh_retail_banking_test
- lh_retail_banking_prod

## Parameterization

Parameterize environment-specific values such as source path, Lakehouse name, workspace references, and run mode. Avoid changing code just because you are moving from Dev to Test.

## Testing Process

1. Run notebooks in Dev.
2. Review code changes.
3. Promote to Test.
4. Run ingestion, transformation, DQ, SQL validation, and report checks.
5. Review access and sensitive fields.
6. Promote to Prod after approval.

## Rollback Considerations

Keep release history. Know which notebooks, SQL scripts, and semantic model changes were deployed. If a release fails, revert code and restore previous validated artifacts where possible.

## Best Practices

- Use separate workspaces for real production work.
- Do not test directly in Prod.
- Keep environment configuration explicit.
- Validate data and reports in Test before Prod.
- Keep release notes and approvals.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| One workspace for everything | Dev changes affect business users | Separate Dev/Test/Prod. |
| Different names in every environment | Automation is hard | Use consistent naming. |
| No rollback plan | Production incidents take longer | Keep release history. |

## Related Repo Files

- [cicd/dev-test-prod-strategy.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/cicd/dev-test-prod-strategy.md)
- [cicd/environment-configuration.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/cicd/environment-configuration.md)
- [cicd/release-checklist.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/cicd/release-checklist.md)
- [adr/005-why-use-dev-test-prod-workspaces.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/adr/005-why-use-dev-test-prod-workspaces.md)

## Related Wiki Pages

- [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy)
- [Naming Standards](Naming-Standards)
- [Governance and Security](Governance-and-Security)

## Summary Checklist

- [ ] Dev, Test, and Prod workspaces are separated.
- [ ] Environment names are consistent.
- [ ] Configuration is parameterized.
- [ ] Test validation is required before Prod.
- [ ] Rollback plan is documented.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy) | [Home](Home) | [Performance and Optimization](Performance-and-Optimization) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
