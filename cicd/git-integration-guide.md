# Git Integration Guide

## Concept

Fabric Git integration connects supported workspace items to a Git repository so changes can be tracked, reviewed, and promoted with more discipline.

## What Should Be Version-Controlled

- Notebooks
- SQL scripts
- Pipeline templates or exported definitions
- Data quality rules
- Documentation
- Semantic model metadata when supported by your workflow
- Governance and release checklists

## What Should Not Be Version-Controlled

- Secrets
- Personal access tokens
- Production data
- Tenant-specific credentials
- Workspace-specific IDs unless intentionally templated
- Local cache files
- Large generated extracts

## Practical Workflow

1. Make changes in Dev.
2. Sync supported Fabric items to Git.
3. Open a pull request.
4. Review notebooks, SQL, pipeline definitions, and docs.
5. Merge after validation.
6. Promote through deployment pipeline or controlled release process.

## Common Mistakes

- Treating Git sync as a substitute for code review.
- Editing production directly.
- Committing environment IDs and secrets.
- Not checking which Fabric items are supported by Git integration in the current tenant.
