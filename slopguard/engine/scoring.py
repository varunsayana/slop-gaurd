from typing import List, Dict, Any
from slopguard.models import Finding, Severity, Category

class ScoringEngine:
    def __init__(self):
        self.severity_weights = {
            Severity.LOW: 2,
            Severity.MEDIUM: 5,
            Severity.HIGH: 15
        }

    def score(self, findings: List[Finding]) -> Dict[str, Any]:
        """
        Computes the slop score from 0-100 based on weighted penalties.
        A score of 100 means zero slop.
        """
        base_score = 100
        penalties = 0
        categories_breakdown = {k: 0 for k in Category}
        
        for f in findings:
            penalty = self.severity_weights.get(f.severity, 0)
            penalties += penalty
            for cat in f.categories:
                categories_breakdown[cat] += 1
                
        final_score = max(0, base_score - penalties)
        
        counts = {
            "low": sum(1 for f in findings if f.severity == Severity.LOW),
            "medium": sum(1 for f in findings if f.severity == Severity.MEDIUM),
            "high": sum(1 for f in findings if f.severity == Severity.HIGH),
        }
        
        status = "Pass"
        if final_score < 50:
            status = "Fail"
        elif final_score < 80:
            status = "Warn"
            
        return {
            "score": final_score,
            "status": status,
            "categories": categories_breakdown,
            "counts": counts
        }
