from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
cases = [
    ("example.json", "expected.json"),
    ("examples/regression.json", "examples/regression.expected.json"),
]
for source, expectation in cases:
    actual = subprocess.check_output(
        [sys.executable, str(root / "agent.py"), str(root / source)],
        text=True,
    )
    expected = json.loads((root / expectation).read_text(encoding="utf-8"))
    if json.loads(actual) != expected:
        raise SystemExit(f"{source} differs from {expectation}")
    print(f"{source} matched {expectation}")
