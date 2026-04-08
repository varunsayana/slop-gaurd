from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseParser(ABC):
    @abstractmethod
    def parse(self, code: str) -> Any:
        """Parses source code into an AST or generic structure."""
        pass

    @abstractmethod
    def get_functions(self, ast: Any) -> List[Dict[str, Any]]:
        """Extracts function boundaries, names, and metadata."""
        pass

    @abstractmethod
    def get_classes(self, ast: Any) -> List[Dict[str, Any]]:
        """Extracts class boundaries, names, and metadata."""
        pass

    @abstractmethod
    def get_imports(self, ast: Any) -> List[Dict[str, Any]]:
        """Extracts imports."""
        pass
