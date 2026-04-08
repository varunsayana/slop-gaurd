from slopguard.formatters.text import TextFormatter
from slopguard.formatters.json import JsonFormatter
from slopguard.formatters.markdown_summary import MarkdownSummaryFormatter
from slopguard.formatters.sarif import SarifFormatter
from slopguard.formatters.reviewdog import ReviewdogFormatter


def get_formatter(format_name: str):
    mapping = {
        "text": TextFormatter(),
        "json": JsonFormatter(),
        "github": MarkdownSummaryFormatter(),
        "markdown": MarkdownSummaryFormatter(),
        "sarif": SarifFormatter(),
        "reviewdog": ReviewdogFormatter(),
    }
    return mapping.get(format_name.lower(), TextFormatter())
