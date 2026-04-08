# Contributing to SlopGuard

Thank you for your interest in contributing to SlopGuard! Our goal is to build the best developer tool for catching low-value slop in PRs without relying on expensive hosting or APIs.

## Development Setup

1. Clone the repository
2. Set up a virtual environment: `python -m venv venv` and `source venv/bin/activate`
3. Install development dependencies: `pip install -e ".[dev]"`
4. Run tests: `pytest`

## Adding a New Rule
1. Create your rule class inside `slopguard/rules/`. Inherit from `BaseRule`.
2. Map your rule to one of the defined score categories.
3. Write test cases inside `tests/rules/` and use a fixture file in `tests/fixtures/`.
4. Ensure your rule has no false-positives for idiomatic code.

## Code Style
We use `ruff` for formatting and linting, and `mypy` for static checking.
Run `ruff check .` and `mypy slopguard` before raising a PR.
