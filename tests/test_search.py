from playcli.cli import app
from typer.testing import CliRunner
from click.testing import Result

runner: CliRunner = CliRunner()

def test_search():
    result: Result = runner.invoke(app, ["search", "games"])
    
    assert result.exit_code == 0 and result.stdout != "No results were found."

def test_search_page():
    result: Result = runner.invoke(app, ["search", "games", "--page", "2"])

    assert result.exit_code == 0 and result.stdout != "No results were found."

def test_search_page_error():
    result: Result = runner.invoke(app, ["search", "games", "--page", "-1"])

    assert result.exit_code == 2