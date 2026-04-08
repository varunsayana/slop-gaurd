# GitHub Action

## Usage
Include the action in your `.github/workflows/slopguard.yml` file.

```yaml
on: [pull_request]

jobs:
  slopguard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./ # Or your organization/slopguard
```

The action will checkout the repository, install Python and dependencies, and execute the SlopGuard binary. The action utilizes Markdown formatting to print an interactive summary into your GitHub Actions console log and optional PR annotations.
