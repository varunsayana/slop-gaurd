from typing import Dict, Any
import os

class MarkdownSummaryFormatter:
    def format(self, results: Dict[str, Any]) -> str:
        score = results.get("score", 100)
        status = results.get("status", "Pass")
        findings = results.get("findings", [])
        counts = results.get("counts", {})
        categories = results.get("categories", {})
        
        md = [
            "## SlopGuard Report",
            f"Score: **{score}/100**",
            f"Status: **{status}**\n"
        ]
        
        if findings:
            # Sort findings by severity (high -> low)
            severity_weights = {"high": 3, "medium": 2, "low": 1}
            sorted_findings = sorted(findings, key=lambda x: severity_weights.get(x.severity, 0), reverse=True)
            
            top_risks = sorted_findings[:5]
            if top_risks:
                md.append("### Top Issues:")
                for f in top_risks:
                    md.append(f"- **{f.severity.upper()}**: {f.short_explanation} (`{f.file_path}:{f.line_number}`)")
                md.append("\n")
                
            md.append("### Breakdown")
            md.append(f"- **High Risk**: {counts.get('high', 0)}")
            md.append(f"- **Medium Risk**: {counts.get('medium', 0)}")
            md.append(f"- **Low Risk**: {counts.get('low', 0)}")
            md.append("")
            
            # File-level logic separation requested by user
            caused_structural = [f for f in findings if getattr(f, "scope", None) == "file" and getattr(f, "caused_by_pr", False)]
            if caused_structural:
                md.append("### Structural Concerns Introduced by this PR")
                for f in caused_structural:
                     md.append(f"- {f.title}: {f.short_explanation}")
                md.append("\n")

        else:
            md.append("✅ **No issues detected!** Great job keeping the PR clean.")
            
        md_str = "\n".join(md)
        if "GITHUB_STEP_SUMMARY" in os.environ:
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
                f.write(md_str + "\n")
                
        return md_str
