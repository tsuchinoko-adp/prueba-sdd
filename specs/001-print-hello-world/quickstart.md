# Quickstart & Validation Guide: Print Hello World

**Feature**: `001-print-hello-world`
**Branch**: `001-print-hello-world`

This guide describes how to validate the feature end-to-end against the [Data Model](../data-model.md) and [Interface Contract](../contracts/stdout-interface.md).

## Prerequisites

- Python 3.12+ (or active Databricks Runtime Notebook with Python 3.12 kernel).
- No external packages or cluster dependencies required.

## Validation Scenarios

### Scenario 1: Notebook Execution (Databricks)

1. Open or attach a Python notebook in Databricks.
2. In an empty code cell, execute the script block containing the contract verification followed by the native print statement.
3. **Expected Outcome**:
   - The cell executes in < 1 second.
   - The cell output pane displays:
     ```text
     Hello World
     ```
   - Zero Spark jobs or stages appear in the Spark UI.

### Scenario 2: Local Python CLI Execution

1. Run the entrypoint via Python:
   ```bash
   python -c "mensaje = 'Hello World'; assert isinstance(mensaje, str) and mensaje == 'Hello World'; print(mensaje)"
   ```
2. **Expected Outcome**:
   - Terminal prints: `Hello World`
   - Exit code: `0`

### Scenario 3: Automated Unit Test Validation

1. Run pytest against the test suite:
   ```bash
   pytest tests/test_hello_world.py
   ```
2. **Expected Outcome**:
   - Test intercepts stdout and verifies contract criteria.
   - All assertions pass with 100% green status.
