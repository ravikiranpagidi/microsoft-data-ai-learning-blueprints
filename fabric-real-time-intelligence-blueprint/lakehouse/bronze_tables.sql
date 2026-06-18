-- Bronze tables preserve raw event structure for historical replay and audit.

CREATE TABLE IF NOT EXISTS raw_shipment_events (
    event_type STRING,
    shipment_id STRING,
    order_id STRING,
    vehicle_id STRING,
    driver_id STRING,
    customer_region STRING,
    origin STRING,
    destination STRING,
    route_id STRING,
    planned_delivery_time TIMESTAMP,
    current_eta TIMESTAMP,
    shipment_status STRING,
    delay_minutes INT,
    temperature_required BOOLEAN,
    event_timestamp TIMESTAMP,
    ingestion_timestamp TIMESTAMP,
    source_name STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vehicle_telemetry (
    event_type STRING,
    vehicle_id STRING,
    latitude DOUBLE,
    longitude DOUBLE,
    speed_mph DOUBLE,
    fuel_level DOUBLE,
    engine_temperature DOUBLE,
    harsh_braking BOOLEAN,
    route_id STRING,
    event_timestamp TIMESTAMP,
    ingestion_timestamp TIMESTAMP,
    source_name STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_warehouse_sensor_events (
    event_type STRING,
    warehouse_id STRING,
    zone_id STRING,
    temperature DOUBLE,
    humidity DOUBLE,
    vibration_level DOUBLE,
    door_open BOOLEAN,
    refrigerated_zone BOOLEAN,
    event_timestamp TIMESTAMP,
    ingestion_timestamp TIMESTAMP,
    source_name STRING
)
USING DELTA;
