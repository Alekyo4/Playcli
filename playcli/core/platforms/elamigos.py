from bs4 import BeautifulSoup
from typer import Exit

from playcli.core.web import scrap
from playcli.models.driver import Driver, GameSearch, GameDownload, Link


class Elamigos(Driver):
    url: str = "https://www.elamigos-games.com/"

    E: dict[str, dict] = {
        "game": {"links": "#dw > a"},
        "search": {
            "card": ".card-title > a",
        },
    }

    def download(self, id_: str) -> GameDownload:
        eh: dict[str, str] = self.E["game"]

        try:
            target: str = self.url + "/".join(["games", id_])

            parse: BeautifulSoup = scrap(target, ex=False)

            links: list[Link] = []

            for lk in parse.select(eh["links"]):
                links.append(Link(target=lk.text, url=lk["href"]))  # type: ignore

            return GameDownload(target=target, links=links)
        except Exit:
            return GameDownload()

    def search(self, q: str, page: int) -> list[GameSearch]:
        eh: dict[str, str] = self.E["search"]

        parse: BeautifulSoup = scrap(self.url, params={"q": q, "page": page})
        rs: list[GameSearch] = []

        for el in parse.select(eh["card"]):
            if not el["href"].startswith(self.url):  # type: ignore
                continue

            title: str = el.text
            id_: str = el["href"].replace(self.url + "games/", "")  # type: ignore

            rs.append(GameSearch(id_=id_, title=title, platform=self.__class__.__name__))

        return rs
