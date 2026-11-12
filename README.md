# ADB Pipeline Agent

Retrying a failed pipeline task before its upstream dependencies recover can repeat the failure and obscure the original blocker.

## What I built

I built a retry planner for Databricks-style task exports. It checks that every referenced prerequisite exists, then splits failed or pending tasks with incomplete prerequisites from failed tasks that are eligible for retry.

## How it works

```mermaid
flowchart LR
    A["JSON task states and dependencies"] --> B["Validate prerequisite references"]
    B --> C{"Failed or pending task with an incomplete dependency?"}
    C -->|Yes| D["Report task as blocked"]
    C -->|No| E{"Task failed?"}
    E -->|Yes| F["Recommend retry"]
    E -->|No| G["Omit task"]
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [agent.py](agent.py) implements the CLI and decision rules. Uses `argparse` to parse command-line options, `json` to read or write structured records, `pathlib` to read local files. |
| Make | Runs the documented example and local checks. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 agent.py example.json
```

Extract is eligible for retry. Transform stays blocked until its prerequisite succeeds. [Full expected output](examples/Bundled%20scenario.stdout.txt)

### Additional replay cases

- **Regression scenario** · `python3 agent.py examples/regression.json` · [Expected output](examples/Regression%20scenario.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

This offline check evaluates supplied task states and direct dependencies. It does not detect dependency cycles or trigger Databricks runs.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
