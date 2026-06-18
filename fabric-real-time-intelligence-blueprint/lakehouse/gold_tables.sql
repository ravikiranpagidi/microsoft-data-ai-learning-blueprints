-- Gold tables summarize real-time events for Power BI and AI-ready datasets.

CREATE TABLE IF NOT EXISTS shipment_sla_summary
USING DELTA
AS
SELECT
    CAST(event_timestamp AS DATE) AS event_date,
    customer_region,
    route_id,
    COUNT(DISTINCT shipment_id) AS total_shipments,
    SUM(CASE WHEN is_delayed THEN 1 ELSE 0 END) AS delayed_shipments,
    SUM(CASE WHEN is_sla_at_risk THEN 1 ELSE 0 END) AS sla_breach_candidates,
    AVG(delay_minutes) AS average_delay_minutes,
    MAX(delay_minutes) AS max_delay_minutes
FROM shipment_status_clean
GROUP BY CAST(event_timestamp AS DATE), customer_region, route_id;

CREATE TABLE IF NOT EXISTS route_delay_summary
USING DELTA
AS
SELECT
    route_id,
    COUNT(DISTINCT shipment_id) AS shipment_count,
    AVG(delay_minutes) AS average_delay_minutes,
    SUM(CASE WHEN is_delayed THEN 1 ELSE 0 END) AS delayed_shipment_count
FROM shipment_status_clean
GROUP BY route_id;

CREATE TABLE IF NOT EXISTS vehicle_health_summary
USING DELTA
AS
SELECT
    vehicle_id,
    route_id,
    COUNT(*) AS telemetry_event_count,
    AVG(speed_mph) AS average_speed_mph,
    AVG(fuel_level) AS average_fuel_level,
    MAX(engine_temperature) AS max_engine_temperature,
    SUM(CASE WHEN harsh_braking THEN 1 ELSE 0 END) AS harsh_braking_count,
    SUM(CASE WHEN has_vehicle_alert THEN 1 ELSE 0 END) AS vehicle_alert_count
FROM vehicle_telemetry_clean
GROUP BY vehicle_id, route_id;

CREATE TABLE IF NOT EXISTS warehouse_condition_summary
USING DELTA
AS
SELECT
    warehouse_id,
    zone_id,
    COUNT(*) AS sensor_event_count,
    AVG(temperature) AS average_temperature,
    MAX(temperature) AS max_temperature,
    AVG(humidity) AS average_humidity,
    SUM(CASE WHEN door_open THEN 1 ELSE 0 END) AS door_open_count,
    SUM(CASE WHEN has_temperature_breach THEN 1 ELSE 0 END) AS temperature_breach_count
FROM warehouse_sensor_clean
GROUP BY warehouse_id, zone_id;
