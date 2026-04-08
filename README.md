# SlopGuard

SlopGuard is a fully open-source, zero-backend, zero-hosting-cost tool designed to analyze pull requests and local git diffs to detect low-value, production-risky, overengineered, inefficient, or unnecessary code changes.

**This is NOT an “AI detector.”** Instead, it is a “PR quality and production-slop detector.” Its goal is to stop bad patches before they merge by identifying architectural and logical smells natively associated with rushed or auto-generated "slop", regardless of who wrote it.

## What SlopGuard Catches

- Unnecessary abstractions and wrapper layers
- Useless helper functions that add zero value
- Dead code, unused imports, empty branches
- Broad exception swallowing inside core logic
- Over-split logic
- Fake edge-case handling
- Style drift from the repository baseline
- Repeated expensive calls/computations in loops

## What SlopGuard is NOT

- It does not ping expensive cloud LLM APIs.
- It does not attempt to probabilistically classify code as "AI" or "Human".
- It does not run a server or webhook backend.

## Installation

You can install it directly from the repo (or PyPI once published):

```bash
pip install -e .
```

## CLI Usage

Run SlopGuard inside any repository to analyze current changes:

**Local Diff:**

```bash
slopguard analyze --repo . --base main --head HEAD
```

**Staged Changes:**

```bash
slopguard analyze --staged
```

**Patch File:**

```bash
slopguard analyze --patch diff.patch
```

**Direct File:**

```bash
slopguard analyze file path/to/file.py
```

### Other Commands

- `slopguard explain` - Explain why a file or finding was marked.
- `slopguard rules list` - See available rules.
- `slopguard config init` - Generate a baseline `.slopguard.yml` config file.
- `slopguard autofix --safe` - Apply explicit, 100% safe automatic fixes for unambiguous dead code.

## GitHub Action

Run SlopGuard on PRs utilizing native inline GitHub review comments using `reviewdog`. Create `.github/workflows/slopguard.yml`:

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
      - uses: ./ # Or your organization/slopguard
        with:
          reporter: "github-pr-review"
          level: "warning"
```

## Performance Rules

In addition to architecture and dead code, SlopGuard specifically flags performance bottlenecks such as:

1. `repeated_expensive_call_in_loop`: Networking or DB operations firing implicitly in loops creating N+1 issues.
2. `unnecessary_data_copy`: Useless RAM allocation natively via redundant `list()` casting.
3. `sync_blocking_in_async_context`: Accidentally destroying concurrency by invoking blocking requests in event loops.

## Configuration

Configure using `.slopguard.yml` in your repository root. Setup thresholds, toggle baseline checks, and customize rule severity.

```bash
slopguard config init
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License.
