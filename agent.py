import argparse
import json
from pathlib import Path


def evaluate(data):
    tasks = data["tasks"]
    deps = data["dependencies"]
    if any(dep not in tasks for values in deps.values() for dep in values):
        raise ValueError("unknown dependency")
    blocked = sorted(name for name, state in tasks.items() if state in {"failed","pending"}
                     and any(tasks[dep] != "success" for dep in deps.get(name, [])))
    return {"retry": sorted(name for name, state in tasks.items()
                            if state == "failed" and name not in blocked), "blocked": blocked}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), indent=2))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")


if __name__ == "__main__":
    main()
