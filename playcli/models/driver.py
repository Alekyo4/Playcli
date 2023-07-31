class Link:
    def __init__(self, target: str, url: str) -> None:
        self.target: str = target
        self.url: str = url

class GameDownload:
    def __init__(self, target: str | None = None, links: list[Link] = []):
        self.target: str | None = target
        self.links: list[Link] = links

class GameSearch:
    def __init__(self, id_: str, platform: str, title: str) -> None:
        self.id: str = id_
        self.title: str = title

        self.platform: str = platform


class Driver:
    url: str

    E: dict[str, dict]

    def download(self, id_: str) -> GameDownload:
        ...

    def search(self, q: str, page: int) -> list[GameSearch]:
        ...
