PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) verify_example.py

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
