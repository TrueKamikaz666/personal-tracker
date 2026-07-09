import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


LATEST = ROOT / "docs" / "latest.json"


def save(data):

    with open(
        LATEST,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )
