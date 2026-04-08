import json
from typing import Dict, Any

class ReviewdogFormatter:
    def format(self, results: Dict[str, Any]) -> str:
        findings = results.get("findings", [])
        
        diagnostics = []
        for f in findings:
            # Map severity
            rd_severity = "INFO"
            if f.severity == "high":
                rd_severity = "ERROR"
            elif f.severity == "medium":
                rd_severity = "WARNING"
                
            diagnostics.append({
                "message": f.short_explanation + "\n\nFix: " + f.suggested_remediation,
                "location": {
                    "path": f.file_path,
                    "range": {
                        "start": { "line": f.line_number or 1 }
                    }
                },
                "severity": rd_severity,
                "code": {
                    "value": f.rule_id
                }
            })
            
        rdjson = {
            "source": {
                "name": "slopguard",
                "url": "https://github.com/slopguard/slopguard"
            },
            "severity": "WARNING",
            "diagnostics": diagnostics
        }
        
        return json.dumps(rdjson, indent=2)
