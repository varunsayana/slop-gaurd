def count_lines(text: str) -> int:
    return len(text.splitlines())


def clean_docstring(text: str) -> str:
    """Removes standard docstring prefixes/suffixes."""
    text = text.strip()
    if text.startswith('"""') and text.endswith('"""'):
        return text[3:-3].strip()
    return text
