import requests
from bs4 import BeautifulSoup


class GeniusScraper:
    def __init__(self) -> None:
        self.urls = []

    def add_url(self, url) -> None:
        if isinstance(url, str):
            self.urls.append(url)
        elif isinstance(url, list):
            self.urls += url
        else:
            raise TypeError("What are you passing to add_url?")

    def scrap(self):
        lyrics = []
        for url in self.urls:
            lyric = ""
            res = requests.get(url)
            page = BeautifulSoup(res.content, "html.parser")
            for div in page.find_all(attrs={"class": "Lyrics__Container-sc-1ynbvzw-6"}):
                for link in div.find_all("a"):
                    lyric += link.text.strip()
                    lyric += "\n"
            lyrics.append(lyric)
        return lyrics

