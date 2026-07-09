import requests
from bs4 import BeautifulSoup

from models import create_product


URL = "https://funko.com/search?q=limited+edition"


def scrape_funko():

    products = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
    }

    try:

        response = requests.get(
            URL,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        cards = soup.select(".product-tile")

        for card in cards[:20]:

            product = create_product()

            title = card.select_one(".product-name")

            if title:

                product["name"] = title.get_text(
                    " ",
                    strip=True
                )

            link = card.select_one("a")

            if link and link.has_attr("href"):

                href = link["href"]

                if href.startswith("/"):

                    href = "https://funko.com" + href

                product["url"] = href

            image = card.select_one("img")

            if image:

                if image.has_attr("src"):

                    product["image"] = image["src"]

                elif image.has_attr("data-src"):

                    product["image"] = image["data-src"]

            price = card.select_one(
                ".price"
            )

            if price:

                product["price"] = price.get_text(
                    " ",
                    strip=True
                )

            product["store"] = "Funko"

            product["available"] = True

            products.append(product)

    except Exception as error:

        print(error)

    return products
