# Access Control Model

## Role-Based Access

| Role | Bronze | Silver | Gold | Semantic model | Typical responsibility |
| --- | --- | --- | --- | --- | --- |
| Platform Admin | Admin | Admin | Admin | Admin | Capacity, tenant, workspace policy |
| Data Engineer | Read/Write | Read/Write | Read/Write | Build support | Pipelines, notebooks, data quality |
| Data Steward | Read | Read | Read/Approve | Review | Definitions, quality, classification |
| Semantic Model Author | No default | Limited read | Read | Build | Power BI model and measures |
| Analyst | No default | No default | Read | Read/Build as approved | Analysis and report creation |
| Business Viewer | No default | No default | No direct table access | Read | Consume certified reports |

## Bronze, Silver, Gold Access Pattern

- Bronze: restricted to engineering and audit use.
- Silver: available to engineering and data stewards for validation.
- Gold: default layer for broad analytical consumption.
- Semantic model: preferred access point for most business users.

## Least Privilege

Start with the minimum access required. Increase access only when there is a documented business reason.

## Practical Recommendation

Use Microsoft Entra groups to manage access by role and environment. Avoid assigning users individually except for temporary troubleshooting.
