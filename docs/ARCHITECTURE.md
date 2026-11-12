# Adb Pipeline Agent architecture

Identify failed dependencies before retrying an Azure Databricks-style pipeline.

```mermaid
flowchart LR
    N0["example.json"]
    N1["agent.py"]
    N2["Check task dependency state before recommending a retry."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
