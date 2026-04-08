def safe_remove_pass(code: str, line_number: int) -> str:
    lines = code.splitlines()
    if 0 <= line_number - 1 < len(lines):
        if lines[line_number - 1].strip() == "pass":
            lines.pop(line_number - 1)
    return "\n".join(lines)
