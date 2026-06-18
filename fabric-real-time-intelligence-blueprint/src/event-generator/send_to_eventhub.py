"""Send synthetic logistics events to Azure Event Hubs."""

from __future__ import annotations

import argparse
import json
import os
import time
from typing import Any, Dict

from azure.eventhub import EventData, EventHubProducerClient

from generate_events import LogisticsEventGenerator, load_config


def send_events(config: Dict[str, Any], count: int, interval_seconds: float) -> int:
    connection_str = os.getenv("EVENTHUB_CONNECTION_STR")
    eventhub_name = os.getenv("EVENTHUB_NAME")

    if not connection_str or not eventhub_name:
        raise ValueError("Set EVENTHUB_CONNECTION_STR and EVENTHUB_NAME before sending events.")

    generator = LogisticsEventGenerator(config)
    producer = EventHubProducerClient.from_connection_string(
        conn_str=connection_str,
        eventhub_name=eventhub_name,
    )

    sent = 0
    with producer:
        for event in generator.generate_many(count):
            batch = producer.create_batch()
            batch.add(EventData(json.dumps(event)))
            producer.send_batch(batch)
            sent += 1
            if interval_seconds > 0:
                time.sleep(interval_seconds)

    return sent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send synthetic events to Azure Event Hubs.")
    parser.add_argument("--config", default="config.example.json")
    parser.add_argument("--count", type=int, default=None)
    parser.add_argument("--interval-seconds", type=float, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    count = args.count or int(config.get("default_count", 100))
    interval = args.interval_seconds
    if interval is None:
        interval = float(config.get("default_interval_seconds", 0.0))

    sent = send_events(config, count, interval)
    print(f"Sent {sent} events to Event Hubs.")


if __name__ == "__main__":
    main()
