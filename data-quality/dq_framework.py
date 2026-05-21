"""Rule-driven PySpark data quality framework for Microsoft Fabric Lakehouse projects.

This module is intentionally lightweight. It is designed for Fabric notebooks where
teams want practical checks without adopting a full external data quality platform
on day one.

Typical usage:

    import yaml
    from dq_framework import DataQualityRunner

    with open("/lakehouse/default/Files/retail_banking/config/dq_rules.yml") as handle:
        rules = yaml.safe_load(handle)

    runner = DataQualityRunner(spark, rules)
    results_df = runner.run()
    runner.write_results("dq_results")
    print(runner.markdown_report())
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


@dataclass
class DataQualityResult:
    """A normalized result row for one data quality rule execution."""

    table_name: str
    rule_name: str
    rule_type: str
    severity: str
    status: str
    failed_count: int
    details: str
    run_timestamp: str


class DataQualityRunner:
    """Run YAML-configured data quality rules against Spark tables.

    Supported rule types:

    - not_null
    - duplicate_key
    - accepted_values
    - range
    - referential_integrity
    - row_count_min
    - row_count_between
    - row_count_reconciliation
    - freshness
    - sql_expression

    The framework records rule failures instead of stopping at the first issue.
    Pipeline failure decisions can be made after all rules are evaluated.
    """

    RESULT_SCHEMA = (
        "table_name string, rule_name string, rule_type string, severity string, "
        "status string, failed_count long, details string, run_timestamp string"
    )

    def __init__(self, spark: SparkSession, rules: Dict[str, Any], run_timestamp: Optional[str] = None):
        self.spark = spark
        self.rules = rules or {}
        self.settings = self.rules.get("settings", {})
        self.run_timestamp = run_timestamp or datetime.now(timezone.utc).isoformat()
        self.results: List[DataQualityResult] = []

    def run(self, include_tables: Optional[Iterable[str]] = None) -> DataFrame:
        """Run all configured rules and return the result DataFrame."""

        requested_tables = set(include_tables) if include_tables else None
        configured_tables = self.rules.get("tables", {})

        for table_name, table_config in configured_tables.items():
            if requested_tables and table_name not in requested_tables:
                continue
            for rule in table_config.get("rules", []):
                try:
                    self._run_rule(table_name, rule)
                except Exception as exc:  # Keep running so the report shows every issue found.
                    self._add(
                        table_name=table_name,
                        rule=rule,
                        status="FAIL",
                        failed_count=1,
                        details=f"Rule execution error: {str(exc)[:500]}",
                    )

        return self.to_dataframe()

    def to_dataframe(self) -> DataFrame:
        """Return results as a Spark DataFrame."""

        if not self.results:
            return self.spark.createDataFrame([], schema=self.RESULT_SCHEMA)
        return self.spark.createDataFrame([asdict(result) for result in self.results], schema=self.RESULT_SCHEMA)

    def write_results(self, table_name: Optional[str] = None, mode: str = "overwrite") -> DataFrame:
        """Persist rule results as a Delta table and return the result DataFrame."""

        target_table = table_name or self.settings.get("results_table", "dq_results")
        results_df = self.to_dataframe()
        (
            results_df.write.format("delta")
            .mode(mode)
            .option("overwriteSchema", "true")
            .saveAsTable(target_table)
        )
        return results_df

    def markdown_report(self) -> str:
        """Render a simple markdown report for notebook output or publishing."""

        total_rules = len(self.results)
        failed_rules = sum(1 for result in self.results if result.status == "FAIL")
        critical_failures = sum(
            1 for result in self.results if result.status == "FAIL" and result.severity == "critical"
        )

        lines = [
            "# Data Quality Report",
            "",
            f"Run timestamp: {self.run_timestamp}",
            f"Total evaluated rule results: {total_rules}",
            f"Failed rule results: {failed_rules}",
            f"Critical failures: {critical_failures}",
            "",
            "| Table | Rule | Type | Severity | Status | Failed Count | Details |",
            "| --- | --- | --- | --- | --- | ---: | --- |",
        ]
        for result in self.results:
            details = result.details.replace("|", "\\|")
            lines.append(
                f"| {result.table_name} | {result.rule_name} | {result.rule_type} | "
                f"{result.severity} | {result.status} | {result.failed_count} | {details} |"
            )
        return "\n".join(lines)

    def has_critical_failures(self) -> bool:
        """Return True when any critical rule failed."""

        return any(result.status == "FAIL" and result.severity == "critical" for result in self.results)

    def should_fail_pipeline(self) -> bool:
        """Return True when framework settings require a pipeline failure."""

        fail_on_critical = bool(self.settings.get("fail_on_critical", True))
        return fail_on_critical and self.has_critical_failures()

    def _run_rule(self, table_name: str, rule: Dict[str, Any]) -> None:
        rule_type = rule.get("type")

        handlers = {
            "not_null": self._not_null,
            "duplicate_key": self._duplicate_key,
            "accepted_values": self._accepted_values,
            "range": self._range,
            "referential_integrity": self._referential_integrity,
            "row_count_min": self._row_count_min,
            "row_count_between": self._row_count_between,
            "row_count_reconciliation": self._row_count_reconciliation,
            "freshness": self._freshness,
            "sql_expression": self._sql_expression,
        }

        handler = handlers.get(rule_type)
        if handler is None:
            self._add(table_name, rule, "FAIL", 1, f"Unsupported rule type: {rule_type}")
            return

        handler(table_name, rule)

    def _table(self, table_name: str) -> DataFrame:
        if not self.spark.catalog.tableExists(table_name):
            raise RuntimeError(f"Table does not exist: {table_name}")
        return self.spark.table(table_name)

    def _with_optional_filter(self, df: DataFrame, rule: Dict[str, Any], filter_key: str = "filter") -> DataFrame:
        filter_expression = rule.get(filter_key)
        return df.where(filter_expression) if filter_expression else df

    def _validate_columns(self, df: DataFrame, columns: Iterable[str], table_name: str) -> None:
        missing_columns = [column for column in columns if column not in df.columns]
        if missing_columns:
            raise RuntimeError(f"Missing columns in {table_name}: {missing_columns}")

    def _add(self, table_name: str, rule: Dict[str, Any], status: str, failed_count: int, details: str) -> None:
        self.results.append(
            DataQualityResult(
                table_name=table_name,
                rule_name=rule.get("name", rule.get("type", "unknown")),
                rule_type=rule.get("type", "unknown"),
                severity=rule.get("severity", "warning"),
                status=status,
                failed_count=int(failed_count),
                details=details,
                run_timestamp=self.run_timestamp,
            )
        )

    def _not_null(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        columns = rule.get("columns", [])
        treat_blank_as_null = bool(rule.get("treat_blank_as_null", True))
        self._validate_columns(df, columns, table_name)

        for column_name in columns:
            condition = F.col(column_name).isNull()
            if treat_blank_as_null:
                condition = condition | (F.trim(F.col(column_name).cast("string")) == "")
            failed = df.filter(condition).count()
            child_rule = dict(rule)
            child_rule["name"] = f"{rule.get('name', 'not_null')}:{column_name}"
            self._add(
                table_name,
                child_rule,
                "PASS" if failed == 0 else "FAIL",
                failed,
                f"{column_name} must not be null" + (" or blank" if treat_blank_as_null else ""),
            )

    def _duplicate_key(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        columns = rule.get("columns", [])
        self._validate_columns(df, columns, table_name)

        failed = df.groupBy(*columns).count().filter(F.col("count") > 1).count()
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Unique key columns: {columns}")

    def _accepted_values(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        column_name = rule["column"]
        values = rule.get("values", [])
        allow_null = bool(rule.get("allow_null", False))
        self._validate_columns(df, [column_name], table_name)

        condition = ~F.col(column_name).isin(values)
        if not allow_null:
            condition = condition | F.col(column_name).isNull()
        else:
            condition = condition & F.col(column_name).isNotNull()

        failed = df.filter(condition).count()
        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Accepted values for {column_name}: {values}; allow_null={allow_null}",
        )

    def _range(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        column_name = rule["column"]
        include_nulls = bool(rule.get("include_nulls", False))
        self._validate_columns(df, [column_name], table_name)

        condition = F.lit(False)
        if "min" in rule:
            condition = condition | (F.col(column_name) < F.lit(rule["min"]))
        if "max" in rule:
            condition = condition | (F.col(column_name) > F.lit(rule["max"]))
        if include_nulls:
            condition = condition | F.col(column_name).isNull()

        failed = df.filter(condition).count()
        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Expected range for {column_name}: {rule.get('min')} to {rule.get('max')}",
        )

    def _referential_integrity(self, table_name: str, rule: Dict[str, Any]) -> None:
        child_column = rule["column"]
        parent_table = rule["parent_table"]
        parent_column = rule["parent_column"]

        child_df = self._with_optional_filter(self._table(table_name), rule)
        parent_df = self._table(parent_table)
        self._validate_columns(child_df, [child_column], table_name)
        self._validate_columns(parent_df, [parent_column], parent_table)

        child_keys = child_df.filter(F.col(child_column).isNotNull()).select(child_column).distinct().alias("child")
        parent_keys = parent_df.select(parent_column).distinct().alias("parent")
        failed = child_keys.join(
            parent_keys,
            F.col(f"child.{child_column}") == F.col(f"parent.{parent_column}"),
            "left_anti",
        ).count()

        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"{child_column} must exist in {parent_table}.{parent_column}",
        )

    def _row_count_min(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        actual = df.count()
        minimum = int(rule.get("min_count", 1))
        failed = 0 if actual >= minimum else minimum - actual
        self._add(table_name, rule, "PASS" if failed == 0 else "FAIL", failed, f"Actual={actual}, minimum={minimum}")

    def _row_count_between(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        actual = df.count()
        minimum = int(rule.get("min_count", 0))
        maximum = int(rule.get("max_count", 2**63 - 1))
        failed = 0 if minimum <= actual <= maximum else abs(actual - min(max(actual, minimum), maximum))
        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Actual={actual}, expected between {minimum} and {maximum}",
        )

    def _row_count_reconciliation(self, table_name: str, rule: Dict[str, Any]) -> None:
        source_table = rule["source_table"]
        target_table = rule["target_table"]
        source_df = self._with_optional_filter(self._table(source_table), rule, "source_filter")
        target_df = self._with_optional_filter(self._table(target_table), rule, "target_filter")

        source_count = source_df.count()
        target_count = target_df.count()
        tolerance = int(rule.get("tolerance", 0))
        difference = abs(source_count - target_count)
        failed = 0 if difference <= tolerance else difference

        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Source={source_table}:{source_count}, target={target_table}:{target_count}, tolerance={tolerance}",
        )

    def _freshness(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._with_optional_filter(self._table(table_name), rule)
        column_name = rule["column"]
        max_age_hours = int(rule.get("max_age_hours", 24))
        self._validate_columns(df, [column_name], table_name)

        row = df.agg(
            ((F.unix_timestamp(F.current_timestamp()) - F.unix_timestamp(F.max(F.col(column_name)))) / 3600).alias(
                "age_hours"
            )
        ).collect()[0]
        age_hours = row["age_hours"]
        failed = 0 if age_hours is not None and age_hours <= max_age_hours else 1

        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Freshness age hours={age_hours}, maximum={max_age_hours}",
        )

    def _sql_expression(self, table_name: str, rule: Dict[str, Any]) -> None:
        df = self._table(table_name)
        expression = rule["expression"]
        failed = df.filter(expression).count()
        self._add(
            table_name,
            rule,
            "PASS" if failed == 0 else "FAIL",
            failed,
            f"Rows matching failure expression: {expression}",
        )
