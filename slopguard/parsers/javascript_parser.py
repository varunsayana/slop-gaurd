from typing import Any, Dict, List
from slopguard.parsers.base import BaseParser


class TreeSitterParser(BaseParser):
    def __init__(self, language_ptr):
        from tree_sitter import Language, Parser

        self.lang = Language(language_ptr)
        self.parser = Parser(self.lang)

    def parse(self, code: str) -> Any:
        return self.parser.parse(bytes(code, "utf8"))

    def _extract_nodes(self, node: Any, types: List[str]) -> List[Any]:
        results = []
        if node.type in types:
            results.append(node)
        for child in node.children:
            results.extend(self._extract_nodes(child, types))
        return results

    def get_functions(self, tree: Any) -> List[Dict[str, Any]]:
        if tree is None:
            return []
        nodes = self._extract_nodes(
            tree.root_node,
            ["function_declaration", "arrow_function", "method_definition"],
        )
        funcs = []
        for n in nodes:
            name_node = n.child_by_field_name("name")
            name = name_node.text.decode("utf8") if name_node else "anonymous"
            funcs.append(
                {
                    "name": name,
                    "start_line": n.start_point[0] + 1,
                    "end_line": n.end_point[0] + 1,
                    "node": n,
                }
            )
        return funcs

    def get_classes(self, tree: Any) -> List[Dict[str, Any]]:
        if tree is None:
            return []
        nodes = self._extract_nodes(tree.root_node, ["class_declaration"])
        cls = []
        for n in nodes:
            name_node = n.child_by_field_name("name")
            name = name_node.text.decode("utf8") if name_node else "anonymous"
            cls.append(
                {
                    "name": name,
                    "start_line": n.start_point[0] + 1,
                    "end_line": n.end_point[0] + 1,
                    "node": n,
                }
            )
        return cls

    def get_imports(self, tree: Any) -> List[Dict[str, Any]]:
        if tree is None:
            return []
        nodes = self._extract_nodes(tree.root_node, ["import_statement"])
        imports = []
        for n in nodes:
            imports.append(
                {
                    "node": n,
                    "start_line": n.start_point[0] + 1,
                    "end_line": n.end_point[0] + 1,
                    "names": [n.text.decode("utf8")],
                }
            )
        return imports


class JavascriptParser(TreeSitterParser):
    def __init__(self):
        try:
            import tree_sitter_javascript

            super().__init__(tree_sitter_javascript.language())
        except ImportError:
            super().__init__(
                None
            )  # Should handle this properly but let's just fail gracefully


class TypescriptParser(TreeSitterParser):
    def __init__(self):
        try:
            import tree_sitter_typescript

            super().__init__(tree_sitter_typescript.language_typescript())
        except ImportError:
            super().__init__(None)
