# Architecture

SlopGuard is designed natively as a local CLI tool without backend dependencies.

## Flow
1. **CLI Parsing**: `typer` arguments.
2. **Configuration**: Load `slopguard.yml` as a `pydantic` object.
3. **Diff Loading**: Extract modified files using standard `git` binary.
4. **Baseline Calculation**: Computes project norms (comment density, size distribution).
5. **Parsing**: Parse modified lines and surrounding scopes into target ASTs (`node`).
6. **Rule Engine**: Apply enabled rules on the parsed nodes.
7. **Scoring**: Reduce `100` based on rule findings and severities.
8. **Format**: Render SARIF, Markdown, Text, or JSON.
9. **Exit**: Return code `1` if base threshold is crossed.
