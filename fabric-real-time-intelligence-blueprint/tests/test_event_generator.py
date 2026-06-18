import json
import sys
from pathlib import Path


GENERATOR_DIR = Path(__file__).resolve().parents[1] / "src" / "event-generator"
sys.path.insert(0, str(GENERATOR_DIR))

from generate_events import LogisticsEventGenerator, load_config, write_jsonl  # noqa: E402


def test_generator_creates_expected_event_types(tmp_path):
    config = load_config(GENERATOR_DIR / "config.example.json")
    generator = LogisticsEventGenerator(config)
    events = [generator.generate_event() for _ in range(50)]

    event_types = {event["event_type"] for event in events}

    assert "shipment" in event_types
    assert "vehicle" in event_types
    assert "warehouse" in event_types
    assert all("event_timestamp" in event for event in events)


def test_write_jsonl_creates_valid_json_lines(tmp_path):
    config = load_config(GENERATOR_DIR / "config.example.json")
    generator = LogisticsEventGenerator(config)
    output = tmp_path / "events.jsonl"

    written = write_jsonl(generator.generate_many(5), output)

    assert written == 5
    lines = output.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 5
    assert all(json.loads(line)["event_type"] in {"shipment", "vehicle", "warehouse"} for line in lines)
