-- Silver tables standardize and validate operational event data.

CREATE TABLE IF NOT EXISTS shipment_status_clean
USING DELTA
AS
SELECT
    shipment_id,
    order_id,
    vehicle_id,
    driver_id,
    customer_region,
    origin,
    destination,
    route_id,
    planned_delivery_time,
    current_eta,
    shipment_status,
    COALESCE(delay_minutes, 0) AS delay_minutes,
    temperature_required,
    event_timestamp,
    CASE WHEN delay_minutes > 0 OR shipment_status = 'Delayed' THEN true ELSE false END AS is_delayed,
    CASE WHEN current_eta > planned_delivery_time THEN true ELSE false END AS is_sla_at_risk
FROM raw_shipment_events
WHERE shipment_id IS NOT NULL
  AND event_timestamp IS NOT NULL;

CREATE TABLE IF NOT EXISTS vehicle_telemetry_clean
USING DELTA
AS
SELECT
    vehicle_id,
    latitude,
    longitude,
    speed_mph,
    fuel_level,
    engine_temperature,
    harsh_braking,
    route_id,
    event_timestamp,
    CASE WHEN engine_temperature > 225 OR fuel_level < 15 OR harsh_braking = true THEN true ELSE false END AS has_vehicle_alert
FROM raw_vehicle_telemetry
WHERE vehicle_id IS NOT NULL
  AND event_timestamp IS NOT NULL;

CREATE TABLE IF NOT EXISTS warehouse_sensor_clean
USING DELTA
AS
SELECT
    warehouse_id,
    zone_id,
    temperature,
    humidity,
    vibration_level,
    door_open,
    refrigerated_zone,
    event_timestamp,
    CASE
        WHEN refrigerated_zone = true AND (temperature < 35 OR temperature > 45) THEN true
        WHEN refrigerated_zone = false AND (temperature < 55 OR temperature > 85) THEN true
        ELSE false
    END AS has_temperature_breach
FROM raw_warehouse_sensor_events
WHERE warehouse_id IS NOT NULL
  AND zone_id IS NOT NULL
  AND event_timestamp IS NOT NULL;
