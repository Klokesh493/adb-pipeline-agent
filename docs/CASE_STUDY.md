# Adb Pipeline Agent walkthrough

## Business problem

Identify failed dependencies before retrying an Azure Databricks-style pipeline.

## Reproduce the workflow

Run `python3 agent.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
{
  "retry": [
    "extract"
  ],
  "blocked": [
    "transform"
  ]
}
```

The sample supplies these fields. `tasks`, `dependencies`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Regression scenario

A failed task waits until its upstream task succeeds.

`make verify` runs this scenario and compares the result with the checked-in expected JSON.
