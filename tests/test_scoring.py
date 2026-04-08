from slopguard.engine.scoring import ScoringEngine
from slopguard.models import Finding, Severity, Confidence

def test_scoring_engine_perfect():
    engine = ScoringEngine()
    res = engine.score([])
    assert res["score"] == 100
    assert res["status"] == "Pass"

def test_scoring_engine_with_slop():
    engine = ScoringEngine()
    findings = [
        Finding(
            rule_id="test",
            title="test",
            severity=Severity.HIGH,
            confidence=Confidence.HIGH,
            file_path="f.py",
            short_explanation="test",
            why_it_matters="x",
            suggested_remediation="y"
        )
    ]
    res = engine.score(findings)
    assert res["score"] == 85 # 100 - 15 (high severity weight)
    assert res["status"] == "Pass" # 85 > 80 (warn)
