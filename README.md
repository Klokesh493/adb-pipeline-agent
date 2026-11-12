# Adb Pipeline Agent

Identify failed dependencies before retrying an Azure Databricks-style pipeline.

## Quick start

Run `python3 agent.py example.json` with Python 3.10 or newer. Compare the result with `expected.json`. The JSON keys in the example define the supported input shape.

This offline prototype reads synthetic input and returns a recommendation or diagnostic. It uses no credentials, external APIs, or infrastructure mutations. Results require operator review.

## Local verification

Run `make verify` with Make and Python 3 installed. The sample runs through the CLI and its JSON is compared with `expected.json`.

## Business problem

Retrying a failed pipeline task before its upstream dependencies recover can repeat the failure and obscure the original blocker.

## Project walkthrough

```mermaid
flowchart LR
    A["Task states and dependency lists"]
    B["Validate dependency references"]
    C{"Any prerequisite incomplete?"}
    D["Blocked task list"]
    E["Failed eligible task enters retry list"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
