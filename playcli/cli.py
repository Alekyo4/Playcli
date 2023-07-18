from typing import Annotated

from typer import Option, Typer

from playcli.core import commands as c

app: Typer = Typer(help="Download games with ease")


@app.command(help="Code repository")
def credits() -> None:
    c.credits()


@app.command(help="Search for games on multiple platforms")
def search(
    title: list[str], page: Annotated[int, Option("--page", "-p", min=1)] = 1
) -> None:
    c.search(" ".join(title), page)