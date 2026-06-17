# Lakehouse to Power BI Flow

This diagram shows how curated Lakehouse data becomes trusted Power BI analytics.

~~~mermaid
flowchart LR
    gold["Gold Delta tables<br/>dim_customer, fact_transaction"] --> sql["SQL analytics endpoint"]
    sql --> views["Business-friendly SQL views"]
    views --> model["Power BI semantic model"]
    model --> measures["Certified measures"]
    model --> rls["Optional row-level security"]
    model --> reports["Power BI reports and dashboards"]

    classDef gold fill:#0078D4,stroke:#004578,color:#ffffff;
    classDef fabric fill:#742774,stroke:#4B155F,color:#ffffff;
    classDef bi fill:#F2C811,stroke:#B38600,color:#111111;
    class gold gold;
    class sql,views fabric;
    class model,measures,rls,reports bi;
~~~

## Consumption Rules

- Report authors should use Gold tables or Gold views.
- Bronze and Silver should be engineering layers unless explicitly approved.
- Measures should be defined once in the semantic model.
- Business-friendly naming should be applied before broad consumption.
- PII should be masked, excluded, or restricted before reaching shared reports.
