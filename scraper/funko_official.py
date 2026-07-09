import requests
from bs4 import BeautifulSoup


URL = "https://funko.com/search?q=limited+edition"


def scrape_funko():

    products = []


    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64)"
        )
    }


    try:

        response = requests.get(
            URL,
            headers=headers,
            timeout=10
        )


        if response.status_code != 200:

            print(
                "Funko error:",
                response.status_code
            )

            return products


        soup = BeautifulSoup(
            response.text,
            "lxml"
        )


        cards = soup.select(
            ".product-tile"
        )


        for card in cards[:10]:

            title = card.select_one(
                ".product-name"
            )


            if title:

                products.append(
                    {
                        "name": title.get_text(
                            " ",
                            strip=True
                        ),
                        "store": "Funko"
                    }
                )


    except Exception as error:

        print(
            "Funko scraper error:",
            error
        )


    return products
