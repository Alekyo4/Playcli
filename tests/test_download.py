from click.testing import Result
from typer.testing import CliRunner

from playcli.cli import app

runner: CliRunner = CliRunner()


def test_download():
    result: Result = runner.invoke(app, ["download", "game"])

    assert result.exit_code == 1


def test_download_platform():
    result: Result = runner.invoke(app, ["download", "game-elamigos"])

    assert result.stdout.find("The game was not found") != -1


def test_download_platform_no_exists():
    result: Result = runner.invoke(app, ["download", "game-game"])

    assert result.exit_code == 1


def test_download_game():
    result: Result = runner.invoke(
        app, ["download", "the-last-of-us-part-i-deluxe-edition-pc-e-elamigos"]
    )

    assert result.exit_code == 0
