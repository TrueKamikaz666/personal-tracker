import json
from bs4 import BeautifulSoup


def extract_products(html):

    soup = BeautifulSoup(html, "lxml")

    products = []

    scripts = soup.find_all(
        "script",
        attrs={"type": "application/ld+json"}
    )

    for script in scripts:

        if not script.string:
            continue

        try:

            data = json.loads(script.string)

        except Exception:

            continue

        if isinstance(data, list):

            iterable = data

        else:

            iterable = [data]

        for item in iterable:

            if not isinstance(item, dict):
                continue

            if item.get("@type") == "Product":

                products.append(item)

    return products
