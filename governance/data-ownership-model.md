# Data Ownership Model

## Roles

| Role | Responsibilities |
| --- | --- |
| Data Owner | Owns business definition, access approval, and data usage policy. |
| Data Steward | Maintains definitions, quality rules, classifications, and issue resolution. |
| Data Engineer | Builds pipelines, notebooks, tables, and quality automation. |
| Semantic Model Author | Builds relationships, measures, RLS, and report-ready model structure. |
| Platform Admin | Manages capacity, workspace policies, tenant settings, and platform monitoring. |
| Consumer | Uses certified data and reports according to access policy. |

## Ownership RACI

| Activity | Owner | Steward | Engineer | Model Author | Admin |
| --- | --- | --- | --- | --- | --- |
| Define active customer | A | R | C | C | I |
| Build Silver transformations | C | C | R | I | I |
| Approve Gold publication | A | R | C | C | I |
| Define measures | A | R | C | R | I |
| Approve access | A | R | I | I | C |
| Promote to production | A | C | R | R | C |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

## Recommendation

Every Gold table and certified semantic model should have a named owner and steward before production release.
