from typing import Any, Dict, List
from slopguard.parsers.base import BaseParser
import re

class GenericParser(BaseParser):
    """
    Fallback parser based on heuristics when AST parsing is unavailable.
    """
    def parse(self, code: str) -> Any:
        return code.splitlines()

    def get_functions(self, lines: Any) -> List[Dict[str, Any]]:
        funcs = []
        for i, line in enumerate(lines):
            # very naive heuristic for python def or js function
            if re.match(r'^\s*(def|function)\s+\w+', line):
                funcs.append({
                    "name": line.split()[1].split('(')[0],
                    "start_line": i + 1,
                    "end_line": i + 1, # inaccurate for generic
                    "node": None
                })
        return funcs

    def get_classes(self, lines: Any) -> List[Dict[str, Any]]:
        return []

    def get_imports(self, lines: Any) -> List[Dict[str, Any]]:
        return []
