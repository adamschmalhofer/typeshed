from typing import Protocol


class Scrapper(Protocol):
    def ingredients(self) -> list[str]:
        ...


def scrape_me(url: str, timeout: int, wild_mode: bool) -> Scrapper:
    ...
