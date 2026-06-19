import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path.cwd()
if (ROOT / "azure-lakehouse-starter-kit").exists():
    ROOT = ROOT / "azure-lakehouse-starter-kit"


def load_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / "sample" / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_order_item_line_totals_are_reasonable() -> None:
    for item in load_csv("order_items.csv"):
        quantity = Decimal(item["quantity"])
        unit_price = Decimal(item["unit_price"])
        discount = Decimal(item["discount_amount"])
        line_total = Decimal(item["line_total"])
        assert line_total == (quantity * unit_price) - discount


def test_completed_orders_have_captured_payments() -> None:
    completed_orders = {row["order_id"] for row in load_csv("orders.csv") if row["order_status"] == "Completed"}
    captured_payments = {row["order_id"] for row in load_csv("payments.csv") if row["payment_status"] == "Captured"}
    assert completed_orders.issubset(captured_payments)
