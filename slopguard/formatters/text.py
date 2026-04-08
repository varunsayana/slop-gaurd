from typing import Dict, Any
from rich.console import Console
from rich.table import Table


class TextFormatter:
    def format(self, results: Dict[str, Any]) -> str:
        console = Console(force_terminal=True)
        score = results.get("score", 100)
        status = results.get("status", "Pass")

        color = "green"
        if status == "Warn":
            color = "yellow"
        elif status == "Fail":
            color = "red"

        header = f"[{color}]Overall Score: {score}/100 ({status})[/{color}]"
        console.print(header)

        findings = results.get("findings", [])
        if findings:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Severity")
            table.add_column("Rule")
            table.add_column("File:Line")
            table.add_column("Details")

            for f in findings:
                scolor = (
                    "red"
                    if f.severity == "high"
                    else "yellow"
                    if f.severity == "medium"
                    else "blue"
                )
                loc = f"{f.file_path}:{f.line_number}"
                table.add_row(
                    f"[{scolor}]{f.severity}[/{scolor}]",
                    f.rule_id,
                    loc,
                    f.short_explanation,
                )
            console.print(table)
        else:
            console.print("[green]No slop detected![/green]")

        return ""  # rich prints directly to stdout for texts
