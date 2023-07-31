from rich import print

from playcli.models import Driver, GameDownload


def call(id_: str, driver: Driver):
    download: GameDownload = driver.download(id_)

    if not download.target:
        print("[red]The game was not found[/]")

        return

    print(f"[green]> {download.target}\n[/]")

    for link in download.links:
        print(f"[green bold]{link.target}:[/]")
        print(link.url)
