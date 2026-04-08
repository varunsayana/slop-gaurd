from typing import Dict, Any


class MarkdownFormatter:
    def format(self, results: Dict[str, Any]) -> str:
        score = results.get("score", 100)
        status = results.get("status", "Pass")
        findings = results.get("findings", [])

        md = [
            f"# SlopGuard Analysis: {status} ({score}/100)\n",
            "This PR was analyzed for unnecessary complexity, bad architecture, and useless indirection.\n\n",
        ]

        if findings:
            md.append("| Severity | Rule | File | Explanation |")
            md.append("|---|---|---|---|")
            for f in findings:
                loc = f"`{f.file_path}:{f.line_number}`"
                md.append(
                    f"| {f.severity.upper()} | {f.rule_id} | {loc} | {f.short_explanation} |"
                )
        else:
            md.append("✅ **No issues detected!** Great job keeping the PR clean.")

        md_str = "\n".join(md)
        # Print to github step summary if in GHA
        import os

        if "GITHUB_STEP_SUMMARY" in os.environ:
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
                f.write(md_str + "\n")
        return md_str
