import csv
from pathlib import Path


ROOT = Path.cwd()
if (ROOT / "azure-lakehouse-starter-kit").exists():
    ROOT = ROOT / "azure-lakehouse-starter-kit"


def load_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / "data" / "sample" / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def assert_unique(rows: list[dict[str, str]], key: str) -> None:
    values = [row[key] for row in rows]
    assert len(values) == len(set(values))


def test_sample_primary_keys_are_unique() -> None:
    assert_unique(load_csv("customers.csv"), "customer_id")
    assert_unique(load_csv("products.csv"), "product_id")
    assert_unique(load_csv("orders.csv"), "order_id")
    assert_unique(load_csv("order_items.csv"), "order_item_id")
    assert_unique(load_csv("payments.csv"), "payment_id")


def test_order_customer_references_exist() -> None:
    customers = {row["customer_id"] for row in load_csv("customers.csv")}
    for order in load_csv("orders.csv"):
        assert order["customer_id"] in customers


def test_order_item_product_references_exist() -> None:
    products = {row["product_id"] for row in load_csv("products.csv")}
    for item in load_csv("order_items.csv"):
        assert item["product_id"] in products
