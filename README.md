# SlopGuard 🛡️

[![PyPI version](https://badge.fury.io/py/slopguard-core.svg)](https://badge.fury.io/py/slopguard-core)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)

**SlopGuard** is a fully open-source, zero-backend, zero-hosting-cost tool designed to analyze pull requests and local git diffs to detect low-value, production-risky, overengineered, inefficient, or unnecessary code changes.

> [!IMPORTANT]
> **This is NOT an “AI detector.”** It does not probabilistically classify code as "AI" or "Human" and does not ping expensive cloud LLMs.
> Instead, it is a **“PR Quality & Production-Slop Detector.”** Its goal is to stop bad patches before they merge by structurally identifying architectural smells natively associated with rushed or auto-generated "slop", regardless of who wrote it.

## 🚀 Quickstart

### Installation

Install SlopGuard globally using pip:

```bash
pip install slopguard-core
```
*(Note: The internal CLI executable is strictly branded as `slopguard` natively during execution)*

### Local Diff Analysis
Run SlopGuard inside any repository to automatically detect issues before you commit:

```bash
# Analyze staged changes
slopguard analyze --staged

# Analyze difference between branches
slopguard analyze --base main --head HEAD

# Analyze patched files
slopguard analyze --patch diff.patch
```

---

## 🛠️ What SlopGuard Catches

SlopGuard uses sophisticated Abstract Syntax Tree (AST) scanning to dynamically catch:

- **Unnecessary Abstractions**: Useless wrapper layers and helper functions that add zero logic.
- **Dead Code**: Unused imports, unreachable paths, and empty branches.
- **Broad Exception Swallowing**: Silently masking critical logic flows (`except Exception:`).
- **Over-Split Logic & Fake Edge Cases**: Needlessly complex architectural bloat.
- **Performance Constraints**: 
  - `repeated_expensive_call_in_loop`: Networking or DB operations firing implicitly inside iterating lists.
  - `unnecessary_data_copy`: Useless RAM allocation natively via redundant `list()` casting.
  - `sync_blocking_in_async_context`: Accidentally destroying concurrency by invoking blocking requests in event loops.

---

## 🤖 GitHub Action Integration

Run SlopGuard on all Pull Requests effortlessly. It natively pipes via `reviewdog` to leave precise **inline comments directly on the changed lines of your PRs**!

Create a file inside your repository at `.github/workflows/slopguard.yml`:

```yaml
name: SlopGuard
on: [pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      
      # Directly execute the open-source pipeline!
      - uses: your-username/slop-guard@main
        with:
          reporter: "github-pr-review"
          level: "warning"
```

---

## 💻 Advanced Usage

SlopGuard acts as a complete diagnostic toolset:

- `slopguard explain [rule_id]` - Learn the deep technical rationale and mitigation steps for any specific AST rule.
- `slopguard rules list` - See all dynamically loaded detection modules.
- `slopguard config init` - Generate a baseline `.slopguard.yml` to tune your severities and adjust PR drop thresholds.

## 🤝 Contributing
SlopGuard is completely community-driven. See [CONTRIBUTING.md](CONTRIBUTING.md) to build custom AST parsers, tune rules, or architect formatters!

## 📄 License
MIT License.
