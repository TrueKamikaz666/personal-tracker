from bs4 import BeautifulSoup

from utils import download
from utils import load_json


SEARCH_URL = "https://shopping.mattel.com/es-es/search?q={}"


def check_monster_high():

    config = load_json("../data/config.json")

    result = {
        "found": False,
        "stores": []
    }

    for product in config["monsterHigh"]:

        html = download(
            SEARCH_URL.format(product["id"])
        )

        soup = BeautifulSoup(html, "lxml")

        if product["id"] in html.upper():

            result["found"] = True

            result["stores"].append({
                "store": "Mattel",
                "product": product["name"],
                "url": SEARCH_URL.format(product["id"])
            })

    return result
