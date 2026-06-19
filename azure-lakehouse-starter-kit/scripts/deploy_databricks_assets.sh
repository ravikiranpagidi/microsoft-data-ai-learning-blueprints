#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_URL=""
TARGET_PATH=""
ENVIRONMENT="dev"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workspace-url)
      WORKSPACE_URL="$2"
      shift 2
      ;;
    --target-path)
      TARGET_PATH="$2"
      shift 2
      ;;
    --environment)
      ENVIRONMENT="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

if [[ -z "$WORKSPACE_URL" || -z "$TARGET_PATH" ]]; then
  echo "workspace-url and target-path are required"
  exit 1
fi

if [[ -z "${DATABRICKS_TOKEN:-}" ]]; then
  echo "DATABRICKS_TOKEN must be set"
  exit 1
fi

echo "Preparing Databricks deployment"
echo "Workspace: $WORKSPACE_URL"
echo "Target path: $TARGET_PATH"
echo "Environment: $ENVIRONMENT"

python -m compileall azure-lakehouse-starter-kit/databricks/notebooks
python azure-lakehouse-starter-kit/scripts/validate_notebooks.py

echo "Install and configure the Databricks CLI in your pipeline before enabling workspace import commands."
echo "Example:"
echo "databricks workspace import-dir azure-lakehouse-starter-kit/databricks/notebooks $TARGET_PATH/databricks/notebooks --overwrite"
echo "databricks jobs create --json @azure-lakehouse-starter-kit/databricks/jobs/lakehouse_workflow.json"
