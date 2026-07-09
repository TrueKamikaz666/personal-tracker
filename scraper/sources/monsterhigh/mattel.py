import requests

from bs4 import BeautifulSoup

from core.source import Source


URL = "https://shopping.mattel.com/es-es/products/monster-high-potion-reveal-draculaura-muneca-y-conjunto-de-juego-jkd76-es-es"


class Mattel(Source):

    def __init__(self):

        super().__init__("Mattel")

    def run(self):

        response = requests.get(

            URL,

            headers={
                "User-Agent": "Mozilla/5.0"
            },

            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        product = {

            "store": "Mattel",

            "available": False,

            "url": URL
        }

        text = soup.get_text(" ", strip=True).lower()

        if "dónde comprar" in text:

            product["available"] = True

        return product
