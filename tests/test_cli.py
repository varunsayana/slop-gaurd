from typer.testing import CliRunner
from slopguard.cli import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "A PR quality and production-slop detector" in result.stdout


def test_cli_rules_list():
    result = runner.invoke(app, ["rules", "list"])
    assert result.exit_code == 0
    assert "broad_exception" in result.stdout
