# Scenario-Based Questions

## 1. A Power BI report shows duplicate customer counts. How do you troubleshoot?

Direct answer: Check relationship design, duplicate customer keys, fact grain, and measure definitions.

Practical explanation: Duplicate counts often come from a many-to-many relationship, duplicate dimension rows, or counting rows instead of distinct customer keys.

Real-world example: If dim_customer has duplicate customer_id values, Active Customer Count will be inflated.

Follow-up question: Where would you add a prevention check?

Strong interview-ready response: I would validate uniqueness in Silver and Gold, enforce a duplicate_key data quality rule, and define customer count as DISTINCTCOUNT over customer_key in the semantic model.

## 2. A source file arrives late. What should the pipeline do?

Direct answer: The pipeline should detect the missing or late file, fail or wait based on SLA, and avoid refreshing downstream reports with incomplete data.

Practical explanation: Pipeline success should mean data is complete enough for the agreed business use.

Real-world example: If transactions.csv is missing, refreshing branch activity would mislead users.

Follow-up question: How would you notify stakeholders?

Strong interview-ready response: I would log the missing file event, stop the downstream transformation, notify the data engineering and data owner groups, and publish a freshness status if reports depend on the data.

## 3. Business users request access to Bronze tables for self-service reporting. What do you do?

Direct answer: I would avoid broad Bronze access and instead understand the use case, then publish a Gold table or governed view that meets the need.

Practical explanation: Bronze can contain raw PII, inconsistent values, duplicates, and incomplete data.

Real-world example: Raw customer files include email and phone, which should not be broadly exposed.

Follow-up question: When is Bronze access acceptable?

Strong interview-ready response: Bronze access is acceptable for engineers, auditors, or approved troubleshooting roles. For reporting, I would provide Gold views or semantic model fields with appropriate classification and masking.

## 4. The Gold fact table loads successfully, but SQL views fail. What do you check?

Direct answer: Check table names, schema names, column names, SQL endpoint synchronization, and whether the views reference supported objects.

Practical explanation: Spark table creation and SQL endpoint visibility can have different timing and naming considerations.

Real-world example: A view referencing dbo.fact_transactions will fail if the actual table is dbo.fact_transaction.

Follow-up question: How do you reduce this risk?

Strong interview-ready response: I keep SQL scripts version-controlled, validate them in Test, and include smoke queries in the release checklist.
