"""Generate synthetic logistics events for the Fabric Real-Time Intelligence blueprint."""

from __future__ import annotations

import argparse
import json
import random
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_config(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


@dataclass
class LogisticsEventGenerator:
    config: Dict[str, Any]

    def __post_init__(self) -> None:
        seed = self.config.get("random_seed")
        if seed is not None:
            random.seed(seed)

    def generate_event(self) -> Dict[str, Any]:
        event_type = self._choose_event_type()
        if event_type == "shipment":
            return self.generate_shipment_event()
        if event_type == "vehicle":
            return self.generate_vehicle_telemetry_event()
        return self.generate_warehouse_sensor_event()

    def generate_many(self, count: int, interval_seconds: float = 0.0) -> Iterable[Dict[str, Any]]:
        for _ in range(count):
            yield self.generate_event()
            if interval_seconds > 0:
                time.sleep(interval_seconds)

    def _choose_event_type(self) -> str:
        event_mix = self.config.get("event_mix", {})
        choices = list(event_mix.keys()) or ["shipment", "vehicle", "warehouse"]
        weights = list(event_mix.values()) or [0.45, 0.35, 0.20]
        return random.choices(choices, weights=weights, k=1)[0]

    def generate_shipment_event(self) -> Dict[str, Any]:
        now = utc_now()
        planned = now + timedelta(minutes=random.randint(10, 180))
        delay_minutes = random.choices(
            population=[0, 5, 10, 15, 25, 35, 50, 75],
            weights=[35, 20, 15, 10, 8, 6, 4, 2],
            k=1,
        )[0]
        current_eta = planned + timedelta(minutes=delay_minutes)
        status = "Delayed" if delay_minutes >= 30 else random.choice(self.config["shipment_statuses"])

        return {
            "event_type": "shipment",
            "shipment_id": f"SHP-{random.randint(100000, 999999)}",
            "order_id": f"ORD-{random.randint(900000, 999999)}",
            "vehicle_id": f"VH-{random.randint(100, 240)}",
            "driver_id": f"DRV-{random.randint(1, 60):03d}",
            "customer_region": random.choice(self.config["regions"]),
            "origin": random.choice(self.config["origins"]),
            "destination": random.choice(self.config["destinations"]),
            "route_id": random.choice(self.config["routes"]),
            "planned_delivery_time": iso_utc(planned),
            "current_eta": iso_utc(current_eta),
            "shipment_status": status,
            "delay_minutes": delay_minutes,
            "temperature_required": random.choice([True, False, False]),
            "event_timestamp": iso_utc(now),
        }

    def generate_vehicle_telemetry_event(self) -> Dict[str, Any]:
        now = utc_now()
        speed = max(0, round(random.gauss(48, 18), 1))
        engine_temperature = round(random.gauss(205, 16), 1)

        return {
            "event_type": "vehicle",
            "vehicle_id": f"VH-{random.randint(100, 240)}",
            "latitude": round(random.uniform(32.0, 47.5), 6),
            "longitude": round(random.uniform(-122.5, -82.0), 6),
            "speed_mph": speed,
            "fuel_level": round(random.uniform(8, 100), 1),
            "engine_temperature": engine_temperature,
            "harsh_braking": random.random() < 0.06,
            "route_id": random.choice(self.config["routes"]),
            "event_timestamp": iso_utc(now),
        }

    def generate_warehouse_sensor_event(self) -> Dict[str, Any]:
        now = utc_now()
        refrigerated_zone = random.choice([True, False])
        target_temp = 39 if refrigerated_zone else 70

        return {
            "event_type": "warehouse",
            "warehouse_id": random.choice(self.config["warehouses"]),
            "zone_id": f"ZONE-{random.randint(1, 12):02d}",
            "temperature": round(random.gauss(target_temp, 6), 1),
            "humidity": round(random.uniform(30, 80), 1),
            "vibration_level": round(max(0, random.gauss(2.5, 1.1)), 2),
            "door_open": random.random() < 0.12,
            "refrigerated_zone": refrigerated_zone,
            "event_timestamp": iso_utc(now),
        }


def write_jsonl(events: Iterable[Dict[str, Any]], output_path: str | Path) -> int:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output.open("w", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps(event, sort_keys=True) + "\n")
            count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate synthetic logistics events.")
    parser.add_argument("--config", default="config.example.json", help="Path to config JSON.")
    parser.add_argument("--count", type=int, default=None, help="Number of events to generate.")
    parser.add_argument("--interval-seconds", type=float, default=None, help="Delay between generated events.")
    parser.add_argument("--output", default="../../samples/generated-events.jsonl", help="Output JSONL path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    count = args.count or int(config.get("default_count", 100))
    interval = args.interval_seconds
    if interval is None:
        interval = float(config.get("default_interval_seconds", 0.0))

    generator = LogisticsEventGenerator(config)
    written = write_jsonl(generator.generate_many(count, interval), args.output)
    print(f"Generated {written} events at {args.output}")


if __name__ == "__main__":
    main()
