# Dev, Test, Prod Strategy

## Environment Purpose

| Environment | Purpose | Data |
| --- | --- | --- |
| Dev | Build and debug | Synthetic or masked sample data |
| Test | Validate release candidates | Controlled representative data |
| Prod | Business consumption | Approved production data |

## Workspace Strategy

Use separate workspaces:

- fab-retailbank-dev
- fab-retailbank-test
- fab-retailbank-prod

## Configuration Strategy

Keep environment-specific settings outside notebook logic where possible. Pass environment, Lakehouse, source folder, and batch ID from the pipeline.

## Access Strategy

Dev can be broader for builders. Prod should be tightly controlled and accessed primarily through certified semantic models and reports.

## Common Mistakes

- Using one workspace for every lifecycle stage.
- Testing with production-only shortcuts and permissions.
- Manually changing Prod after deployment.
- Letting Dev data leak into production reports.
