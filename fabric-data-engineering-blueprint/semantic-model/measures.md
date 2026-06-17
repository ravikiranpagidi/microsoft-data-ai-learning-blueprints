# Measures

These example DAX measures are designed for the Retail Banking Customer Analytics semantic model.

## Core Measures

~~~DAX
Total Transaction Amount =
SUM ( fact_transaction[absolute_transaction_amount] )
~~~

~~~DAX
Transaction Count =
DISTINCTCOUNT ( fact_transaction[transaction_id] )
~~~

~~~DAX
Posted Transaction Count =
CALCULATE (
    [Transaction Count],
    fact_transaction[is_posted] = TRUE ()
)
~~~

~~~DAX
Average Transaction Amount =
DIVIDE ( [Total Transaction Amount], [Transaction Count] )
~~~

~~~DAX
Active Customer Count =
CALCULATE (
    DISTINCTCOUNT ( dim_customer[customer_key] ),
    dim_customer[is_active_customer] = TRUE ()
)
~~~

~~~DAX
Account Count =
DISTINCTCOUNT ( dim_account[account_key] )
~~~

~~~DAX
Open Account Count =
CALCULATE (
    [Account Count],
    dim_account[is_open_account] = TRUE ()
)
~~~

~~~DAX
Customer Segment Count =
DISTINCTCOUNT ( dim_customer[customer_segment] )
~~~

~~~DAX
Total Current Balance =
SUM ( dim_account[current_balance] )
~~~

~~~DAX
Average Current Balance =
AVERAGE ( dim_account[current_balance] )
~~~

## Trend Measures

~~~DAX
Transaction Amount Previous Month =
CALCULATE (
    [Total Transaction Amount],
    DATEADD ( dim_date[date_value], -1, MONTH )
)
~~~

~~~DAX
Transaction Amount Month over Month Change =
[Total Transaction Amount] - [Transaction Amount Previous Month]
~~~

~~~DAX
Transaction Amount Month over Month Change % =
DIVIDE (
    [Transaction Amount Month over Month Change],
    [Transaction Amount Previous Month]
)
~~~

## Naming Standards

- Use business names, not technical names.
- Avoid vague names such as Count, Amount, and Total.
- Prefix time intelligence measures only when needed for clarity.
- Add descriptions to measures in the semantic model.
