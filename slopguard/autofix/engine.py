from typing import List
from slopguard.models import Finding
from slopguard.config import SlopGuardConfig


class AutofixEngine:
    def __init__(self, config: SlopGuardConfig):
        self.config = config

    def can_fix(self, finding: Finding) -> bool:
        if not self.config.autofix.enabled:
            return False
        # Only trivial dead code triggers autofix to avoid silent rewriting
        if self.config.autofix.safe_only:
            return finding.rule_id in ("dead_code_signals",)
        return False

    def apply_fixes(self, findings: List[Finding]) -> List[Finding]:
        fixed = []
        for finding in findings:
            if self.can_fix(finding):
                # In a full implementation, we would rewrite the code using ast.unparse or libcst
                fixed.append(finding)
        return fixed
