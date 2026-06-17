# Governance Model

This view shows the access and ownership model for the blueprint.

~~~mermaid
flowchart TB
    owner["Data owner<br/>Retail banking business"] --> steward["Data steward<br/>definitions and quality"]
    platform["Platform admin<br/>capacity and workspace policy"] --> engineer["Data engineer<br/>pipelines and notebooks"]
    engineer --> bronze["Bronze<br/>restricted engineering access"]
    engineer --> silver["Silver<br/>engineering and steward access"]
    steward --> gold["Gold<br/>certified business-ready data"]
    gold --> analysts["Analysts<br/>SQL and Power BI consumption"]
    gold --> executives["Executives<br/>certified reports"]
    security["Security and compliance<br/>PII classification"] --> bronze
    security --> silver
    security --> gold
~~~

## Access Pattern

| Layer | Typical access |
| --- | --- |
| Bronze | Data engineers, platform administrators, limited auditors |
| Silver | Data engineers, data stewards, selected analysts for validation |
| Gold | Analysts, semantic model authors, business consumers |
| Semantic model | Report authors and viewers according to business role |

## Recommendation

Use least privilege. Make Gold the default consumption layer and treat Bronze as restricted operational evidence.
