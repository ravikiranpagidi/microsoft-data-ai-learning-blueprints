# Sample Data

The sample data represents a small Retail Banking Customer Analytics domain.

## Upload Path

Upload these CSV files into your Fabric Lakehouse Files area:

~~~text
Files/retail_banking/source/
~~~

Expected files:

| File | Entity | Notes |
| --- | --- | --- |
| customers.csv | Customer | Contains sample PII fields for governance examples |
| accounts.csv | Account | Account status, type, balance, and customer relationship |
| products.csv | Product | Banking products and categories |
| transactions.csv | Transaction | Monetary activity by account, branch, product, channel, and timestamp |
| branches.csv | Branch | Branch geography and region |

## Data Use Notice

The data is synthetic and intended for demos, learning, and local experimentation. It does not represent real customers or real financial activity.
