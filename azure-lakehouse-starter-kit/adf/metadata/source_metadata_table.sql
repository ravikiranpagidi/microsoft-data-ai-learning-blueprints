CREATE TABLE dbo.SourceMetadata
(
    source_id             int             NOT NULL PRIMARY KEY,
    source_name           varchar(100)    NOT NULL,
    source_type           varchar(30)     NOT NULL,
    source_schema         varchar(100)    NULL,
    source_object         varchar(200)    NOT NULL,
    target_container      varchar(100)    NOT NULL,
    target_folder         varchar(400)    NOT NULL,
    target_file_name      varchar(200)    NOT NULL,
    file_format           varchar(20)     NOT NULL,
    is_active             bit             NOT NULL DEFAULT 1,
    load_strategy         varchar(30)     NOT NULL DEFAULT 'full',
    watermark_column      varchar(100)    NULL,
    created_utc           datetime2       NOT NULL DEFAULT sysutcdatetime(),
    updated_utc           datetime2       NULL
);

INSERT INTO dbo.SourceMetadata
(
    source_id,
    source_name,
    source_type,
    source_schema,
    source_object,
    target_container,
    target_folder,
    target_file_name,
    file_format,
    is_active,
    load_strategy,
    watermark_column
)
VALUES
(1, 'customers', 'file', NULL, 'customers.csv', 'raw', 'retail/customers', 'customers.csv', 'csv', 1, 'full', NULL),
(2, 'products', 'file', NULL, 'products.csv', 'raw', 'retail/products', 'products.csv', 'csv', 1, 'full', NULL),
(3, 'orders', 'file', NULL, 'orders.csv', 'raw', 'retail/orders', 'orders.csv', 'csv', 1, 'incremental', 'order_date'),
(4, 'order_items', 'file', NULL, 'order_items.csv', 'raw', 'retail/order_items', 'order_items.csv', 'csv', 1, 'incremental', NULL),
(5, 'payments', 'file', NULL, 'payments.csv', 'raw', 'retail/payments', 'payments.csv', 'csv', 1, 'incremental', 'payment_date'),
(6, 'inventory', 'file', NULL, 'inventory.csv', 'raw', 'retail/inventory', 'inventory.csv', 'csv', 1, 'snapshot', 'inventory_date'),
(7, 'web_activity', 'file', NULL, 'web_activity.json', 'raw', 'retail/web_activity', 'web_activity.json', 'json', 1, 'incremental', 'event_timestamp');
