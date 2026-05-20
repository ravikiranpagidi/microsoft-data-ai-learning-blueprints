# Fabric End-to-End Architecture

This view shows the full Microsoft Fabric Data Engineering flow for the Retail Banking Customer Analytics blueprint.

~~~mermaid
flowchart LR
    source["Source CSV files"] --> pipeline["Fabric Data Pipeline<br/>Copy activity"]
    pipeline --> onelake["OneLake"]
    onelake --> files["Lakehouse Files<br/>retail_banking/source"]
    files --> bronze["Bronze Delta tables<br/>raw plus metadata"]
    bronze --> notebook["Fabric Notebook<br/>PySpark transformation"]
    notebook --> silver["Silver Delta tables<br/>clean and conformed"]
    silver --> dq["Data quality checks<br/>rules, reconciliation, freshness"]
    dq --> gold["Gold dimensional model<br/>facts and dimensions"]
    gold --> sql["SQL analytics endpoint<br/>views and metrics"]
    sql --> semantic["Power BI semantic model<br/>relationships and measures"]
    semantic --> dashboard["Business dashboards<br/>customer analytics"]

    classDef fabric fill:#742774,stroke:#4B155F,color:#ffffff;
    classDef storage fill:#0078D4,stroke:#004578,color:#ffffff;
    classDef quality fill:#107C10,stroke:#0B5A0B,color:#ffffff;
    classDef consume fill:#F2C811,stroke:#B38600,color:#111111;
    class pipeline,notebook,sql fabric;
    class onelake,files,bronze,silver,gold storage;
    class dq quality;
    class semantic,dashboard consume;
~~~

## Icon-Backed Component Map

| Icon | Fabric component | Responsibility |
| --- | --- | --- |
| ![Pipeline](assets/icons/pipeline_48_item.svg) | Data Pipeline | Land files and orchestrate notebook execution |
| ![OneLake](assets/icons/one_lake_48_color.svg) | OneLake | Shared storage foundation for Fabric items |
| ![Lakehouse](assets/icons/lakehouse_48_item.svg) | Lakehouse | Store Files and Delta Tables |
| ![Notebook](assets/icons/notebook_48_item.svg) | Notebook | Run PySpark transformations and validation |
| ![SQL database](assets/icons/sql_database_48_item.svg) | SQL analytics endpoint | Expose Gold views and metrics to SQL and BI users |
| ![Semantic model](assets/icons/semantic_model_48_item.svg) | Semantic model | Define relationships and measures |
| ![Power BI](assets/icons/power_bi_48_color.svg) | Power BI | Publish business dashboards |

## Component Responsibilities

| Component | Responsibility |
| --- | --- |
| Source CSV files | Operational extracts for customer, account, product, transaction, and branch data |
| Fabric Data Pipeline | Land files into Lakehouse Files and orchestrate notebooks |
| Lakehouse Files | Store raw source files under controlled folders |
| Bronze Delta tables | Preserve raw structure with ingestion metadata |
| Fabric Notebooks | Transform, validate, enrich, and publish data |
| Silver Delta tables | Store cleaned and conformed entities |
| Data quality framework | Enforce not-null, duplicate, range, accepted values, referential, freshness, and reconciliation checks |
| Gold dimensional model | Publish dimensions and facts for analytics |
| SQL analytics endpoint | Expose SQL views and business metrics |
| Power BI semantic model | Define relationships, measures, and business names |
| Dashboard | Answer banking analytics questions |
