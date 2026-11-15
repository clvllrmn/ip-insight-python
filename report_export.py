from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from formatter import display_information


def build_report(result):
    """Create a text report using the existing formatter."""
    output = StringIO()

    with redirect_stdout(output):
        display_information(result)

    return output.getvalue()


def save_report(result, filename="ip_insight_report.txt"):
    """Save the formatted report to a text file."""
    path = Path(filename)
    path.write_text(build_report(result), encoding="utf-8")
    return path
