"""Validate Azure Lakehouse Starter Kit assets without requiring Spark.

This script is intentionally lightweight so it can run in GitHub Actions,
Azure DevOps, or on a contributor workstation before Databricks deployment.
"""

import ast
import json
from pathlib import Path


ROOT = Path.cwd()
if (ROOT / "azure-lakehouse-starter-kit").exists():
    ROOT = ROOT / "azure-lakehouse-starter-kit"


def validate_json_files() -> list[Path]:
    validated: list[Path] = []
    for path in ROOT.rglob("*.json"):
        if path.name == "web_activity.json":
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                if line.strip():
                    json.loads(line)
                else:
                    raise ValueError(f"Blank JSON Lines record in {path} at line {line_number}")
        else:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        validated.append(path)
    return validated


def validate_python_files() -> list[Path]:
    validated: list[Path] = []
    for path in list((ROOT / "databricks" / "notebooks").rglob("*.py")) + list((ROOT / "scripts").rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        ast.parse(source, filename=str(path))
        validated.append(path)
    return validated


def validate_required_assets() -> None:
    required_paths = [
        ROOT / "README.md",
        ROOT / "data" / "sample" / "customers.csv",
        ROOT / "data" / "sample" / "orders.csv",
        ROOT / "schemas" / "customer_schema.json",
        ROOT / "adf" / "pipelines" / "pl_master_orchestration.json",
        ROOT / "databricks" / "jobs" / "lakehouse_workflow.json",
        ROOT / "sql" / "views" / "vw_customer_360.sql",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required starter kit assets: {missing}")


def main() -> None:
    validate_required_assets()
    json_files = validate_json_files()
    python_files = validate_python_files()
    print(f"Validated {len(json_files)} JSON files")
    print(f"Validated {len(python_files)} Python files")


main()
