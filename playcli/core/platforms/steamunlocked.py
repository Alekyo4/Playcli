from bs4 import BeautifulSoup
from typer import Exit

from playcli.core.web import scrap
from playcli.models.driver import Driver, GameSearch, GameDownload, Link


class Steamunlocked(Driver):
    url: str = "https://steamunlocked.net/"

    E: dict[str, dict] = {
        "game": {"link": ".btn-download"},
        "search": {"card": ".cover-item-title > a"},
    }

    def download(self, id_: str) -> GameDownload:
        eh: dict[str, str] = self.E["game"]

        try:
            target: str = self.url + id_

            parse: BeautifulSoup = scrap(target, ex=False)

            link: Link = Link(
                target="DOWNLOAD", url=parse.select_one(eh["link"])["href"]  # type: ignore
            )

            return GameDownload(target=target, links=[link])
        except Exit:
            return GameDownload()

    def search(self, q: str, page: int) -> list[GameSearch]:
        eh: dict[str, str] = self.E["search"]

        parse: BeautifulSoup = scrap(self.url, ["page", str(page)], {"s": q})
        rs: list[GameSearch] = []

        for el in parse.select(eh["card"]):
            id_: str = el["href"]  # type: ignore

            title: str = el.text.replace("Free Download", "")

            for x in [self.url, "-free-download", "/"]:
                id_ = id_.replace(x, "")

            rs.append(
                GameSearch(id_=id_, title=title.strip(), platform=self.__class__.__name__)
            )

        return rs
