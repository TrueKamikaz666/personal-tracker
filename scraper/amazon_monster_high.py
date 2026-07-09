import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.es/s?k=monster+high"


def scrape_monster_high():

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
                "Amazon error:",
                response.status_code
            )
            return products


        soup = BeautifulSoup(
            response.text,
            "lxml"
        )


        items = soup.select(
            "div[data-component-type='s-search-result']"
        )


        for item in items[:10]:

            title = item.select_one(
                "h2"
            )


            if not title:
                continue


            link = item.select_one(
                "a.a-link-normal"
            )


            products.append(
                {
                    "name": title.get_text(
                        " ",
                        strip=True
                    ),
                    "url": (
                        "https://www.amazon.es"
                        + link["href"]
                        if link else ""
                    ),
                    "store": "Amazon España"
                }
            )


    except Exception as error:

        print(
            "Amazon scraper error:",
            error
        )


    return products
