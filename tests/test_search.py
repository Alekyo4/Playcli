from click.testing import Result
from typer.testing import CliRunner

from playcli.cli import app

runner: CliRunner = CliRunner()


def test():
    result: Result = runner.invoke(app, ["search", "game"])

    assert result.exit_code == 0 and result.stdout != "No results were found."


def test_page():
    result: Result = runner.invoke(app, ["search", "game", "--page", "2"])

    assert result.exit_code == 0 and result.stdout != "No results were found."


def test_page_error():
    result: Result = runner.invoke(app, ["search", "game", "--page", "-1"])

    assert result.exit_code == 2


def test_platform():
    result: Result = runner.invoke(app, ["search", "game", "--platform", "elamigos"])

    assert result.exit_code == 0


def test_recursive():
    result: Result = runner.invoke(app, ["search", "game b", "--platform", "recursive"])

    assert result.exit_code == 0 and result.stdout.find("-steamunlocked") != -1


def test_all():
    result: Result = runner.invoke(app, ["search", "game", "--platform", "all"])

    assert result.exit_code == 0
