# Adb Pipeline Agent architecture

Identify failed dependencies before retrying an Azure Databricks-style pipeline.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
