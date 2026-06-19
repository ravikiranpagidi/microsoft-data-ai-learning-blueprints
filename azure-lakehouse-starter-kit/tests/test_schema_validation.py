import csv
import json
from pathlib import Path


ROOT = Path.cwd()
if (ROOT / "azure-lakehouse-starter-kit").exists():
    ROOT = ROOT / "azure-lakehouse-starter-kit"


def load_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / "sample" / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_schema_files_are_valid_json() -> None:
    for path in (ROOT / "schemas").glob("*.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert "dataset" in payload
        assert "columns" in payload
        assert payload["columns"]


def test_customer_required_columns_match_schema() -> None:
    customers = load_csv("customers.csv")
    schema = json.loads((ROOT / "schemas" / "customer_schema.json").read_text(encoding="utf-8"))
    expected_columns = [column["name"] for column in schema["columns"]]
    assert list(customers[0].keys()) == expected_columns
