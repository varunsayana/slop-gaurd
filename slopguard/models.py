"""
SlopGuard Core Data Models
"""

from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Confidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Scope(str, Enum):
    LINE = "line"
    FILE = "file"


class Category(str, Enum):
    NECESSITY = "Necessity"
    SPECIFICITY = "Specificity"
    COHERENCE = "Coherence"
    CONSISTENCY = "Consistency"
    TRUSTWORTHINESS = "Trustworthiness"
    PERFORMANCE_RISK = "Performance Risk"


class Finding(BaseModel):
    rule_id: str
    title: str
    severity: Severity
    confidence: Confidence
    scope: Scope = Scope.LINE
    caused_by_pr: bool = False
    file_path: str
    line_number: Optional[int] = None
    line_span: Optional[tuple[int, int]] = None
    short_explanation: str
    why_it_matters: str
    suggested_remediation: str
    categories: List[Category] = []


class RuleConfig(BaseModel):
    enabled: bool = True
    severity: Optional[Severity] = None
    # For custom rule configs (e.g. max_comment_ratio)
    options: dict = {}


class RunContext(BaseModel):
    repo_path: str
    base_ref: Optional[str] = None
    head_ref: Optional[str] = None
    is_staged_only: bool = False
    patch_file: Optional[str] = None
    single_file: Optional[str] = None
