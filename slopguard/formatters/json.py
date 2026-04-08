import json
from typing import Dict, Any
from slopguard.models import Finding


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Finding):
            return obj.model_dump()
        return super().default(obj)


class JsonFormatter:
    def format(self, results: Dict[str, Any]) -> str:
        return json.dumps(results, cls=JsonEncoder, indent=2)
