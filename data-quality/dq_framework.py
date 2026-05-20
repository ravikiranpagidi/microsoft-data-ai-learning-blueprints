"""Lightweight PySpark data quality framework for Microsoft Fabric notebooks."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


@dataclass
class DataQualityResult:
    table_name: str
    rule_name: str
    rule_type: str
    severity: str
    status: str
    failed_count: int
    details: str
    run_timestamp: str


class DataQualityRunner:
    """Run configured data quality rules against Spark tables."""

    def __init__(self, spark: SparkSession, rules: Dict[str, Any]):
        self.spark = spark
        self.rules = rules
        self.run_timestamp = datetime.now(timezone.utc).isoformat()
        self.results: List[DataQualityResult] = []

    def run(self) -> DataFrame:
        tables = self.rules.get("tables", {})
        for table_name, table_config in tables.items():
            for rule in table_config.get("rules", []):
                self._run_rule(table_name, rule)
        return self.to_dataframe()

    def to_dataframe(self) -> DataFrame:
        rows = [result.__dict__ for result in self.results]
        if rows:
            return self.spark.createDataFrame(rows)
        schema = "table_name string, rule_name string, rule_type string, severity string, status string, failed_count int, details string, run_timestamp string"
        return self.spark.createDataFrame([], schema=schema)

    def markdown_report(self) -> str:
        total = len(self.results)
        failed = sum(1 for result in self.results if result.status == "FAIL")
        lines = [
            "# Data Quality Report",
            "",
            f"Run timestamp: {self.run_timestamp}",
            f"Total rules: {total}",
            f"Failed rules: {failed}",
            "",
            "| Table | Rule | Type | Severity | Status | Failed Count | Details |",
            "| --- | --- | --- | --- | --- | ---: | --- |",
        ]
        for result in self.results:
            lines.append(f"| {result.table_name} | {result.rule_name} | {result.rule_type} | {result.severity} | {result.status} | {result.failed_count} | {result.details} |")
        return "\n".join(lines)

    def _run_rule(self, table_name: str, rule: Dict[str, Any]) -> None:
        rule_type = rule["type"]
        if rule_type == "not_null":
            self._not_null(table_name, rule)
        elif rule_type == "duplicate_key":
            self._duplicate_key(table_name, rule)
        elif rule_type == "accepted_values":
            self._accepted_values(table_name, rule)
        elif rule_type == "range":
            self._range(table_name, rule)
        elif rule_type == "referential_integrity":
            self._referential_integrity(table_name, rule)
        elif rule_type == "row_count_min":
            self._row_count_min(table_name, rule)
        elif rule_type == "freshness":
            self._freshness(table_name, rule)
        else:
            self._add(table_name, rule, "FAIL", 1, f"Unsupported rule type: {rule_type}")

    def _add(self, table_name: str, rule: Dict[str, Any], status: str, failed_count: int, details: str) -> None:
        self.results.append(DataQualityResult(table_name, rule.get("name", rule.get("type", "unknown")), rule.get("type", "unknown"), rule.get("severity", "warning"), status, int(failed_count), details, self.run_timestamp))

    def _not_null(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self.spark.table(table_name)
        for column_name in rule.get("columns", []):
            failed = df.filter(F.col(column_name).isNull()).count()
            child_rule = dict(rule)
            child_rule["name"] = f"{rule['name']}:{column_name}"
            self._add(table_name, child_rule, "PASS" if failed == 0 else "FAIL", failed, f"Column {column_name} must not be null")

    def _duplicate_key(self, table_name: str, rule: Dict[str, Any]) -> None:
        columns = rule["columns"]
        failed = self.spark.table(table_name).groupBy(*columns).count().filter(F.col("count") > 1).count()
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Unique key columns: {columns}")

    def _accepted_values(self, table_name: str, rule: Dict[str, Any]) -> None:
        column_name = rule["column"]
        values = rule["values"]
        failed = self.spark.table(table_name).filter(~F.col(column_name).isin(values) | F.col(column_name).isNull()).count()
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Accepted values for {column_name}: {values}")

    def _range(self, table_name: str, rule: Dict[str, Any]) -> None:
        column_name = rule["column"]
        condition = F.lit(False)
        if "min" in rule:
            condition = condition | (F.col(column_name) < F.lit(rule["min"]))
        if "max" in rule:
            condition = condition | (F.col(column_name) > F.lit(rule["max"]))
        failed = self.spark.table(table_name).filter(condition).count()
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Expected range for {column_name}: {rule.get('min')} to {rule.get('max')}")

    def _referential_integrity(self, table_name: str, rule: Dict[str, Any]) -> None:
        child_column = rule["column"]
        parent_table = rule["parent_table"]
        parent_column = rule["parent_column"]
        failed = self.spark.table(table_name).select(child_column).distinct().alias("child").join(self.spark.table(parent_table).select(parent_column).distinct().alias("parent"), F.col(f"child.{child_column}") == F.col(f"parent.{parent_column}"), "left_anti").count()
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"{child_column} must exist in {parent_table}.{parent_column}")

    def _row_count_min(self, table_name: str, rule: Dict[str, Any]) -> None:
        actual = self.spark.table(table_name).count()
        minimum = int(rule.get("min_count", 1))
        failed = 0 if actual >= minimum else minimum - actual
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Actual row count {actual}, minimum {minimum}")

    def _freshness(self, table_name: str, rule: Dict[str, Any]) -> None:
        column_name = rule["column"]
        max_age_hours = int(rule.get("max_age_hours", 24))
        row = self.spark.table(table_name).agg(((F.unix_timestamp(F.current_timestamp()) - F.unix_timestamp(F.max(column_name))) / 3600).alias("age_hours")).collect()[0]
        age_hours = row["age_hours"]
        failed = 0 if age_hours is not None and age_hours <= max_age_hours else 1
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Age hours {age_hours}, maximum {max_age_hours}")
