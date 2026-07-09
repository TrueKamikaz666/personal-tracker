import json
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def download(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.text


def load_json(path):

    with open(path, encoding="utf-8") as file:
        return json.load(file)
