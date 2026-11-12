from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
actual = subprocess.check_output(
    [sys.executable, str(root / "agent.py"), str(root / "example.json")],
    text=True,
)
expected = json.loads((root / "expected.json").read_text(encoding="utf-8"))
if json.loads(actual) != expected:
    raise SystemExit("The sample result differs from expected.json")
print("Sample result matches expected.json")
