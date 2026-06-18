"""Send synthetic logistics events to an HTTP endpoint pattern for Eventstream demos.

Fabric Eventstream configuration can vary by source type. Use this script when
you have an HTTP endpoint or gateway pattern available for your demo. Keep
tokens and endpoints in environment variables.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from typing import Any, Dict

import requests

from generate_events import LogisticsEventGenerator, load_config


def send_events(config: Dict[str, Any], count: int, interval_seconds: float) -> int:
    endpoint = os.getenv("FABRIC_EVENTSTREAM_ENDPOINT")
    token = os.getenv("FABRIC_EVENTSTREAM_TOKEN")

    if not endpoint:
        raise ValueError("Set FABRIC_EVENTSTREAM_ENDPOINT before sending events.")

    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    generator = LogisticsEventGenerator(config)
    sent = 0
    for event in generator.generate_many(count):
        response = requests.post(endpoint, headers=headers, data=json.dumps(event), timeout=15)
        response.raise_for_status()
        sent += 1
        if interval_seconds > 0:
            time.sleep(interval_seconds)
    return sent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send synthetic events to a Fabric Eventstream endpoint pattern.")
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
    print(f"Sent {sent} events to configured HTTP endpoint.")


if __name__ == "__main__":
    main()
