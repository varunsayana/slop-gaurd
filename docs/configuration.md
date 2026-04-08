# Configuration

The `.slopguard.yml` configuration allows rule tweaks.

## Example
```yaml
version: 1
thresholds:
  fail_score: 80
  warn_score: 50

paths:
  include:
    - "src/**"
  exclude:
    - "tests/**"
    - "docs/**"

baseline:
  enabled: true
  sample_size: 200

rules:
  useless_wrapper_function:
    enabled: true
    severity: medium
  repeated_expensive_work:
    enabled: true
    severity: high
```
Run `slopguard config init` to generate this automatically.
