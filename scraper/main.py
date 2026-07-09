import json
from datetime import datetime, UTC
from pathlib import Path

from amazon_monster_high import scrape_monster_high
from funko_official import scrape_funko


ROOT = Path(__file__).resolve().parent.parent

OUTPUT = ROOT / "docs" / "latest.json"


data = {
    "updated": datetime.now(UTC).isoformat(),
    "monsterHigh": scrape_monster_high(),
    "funko": scrape_funko()
}


with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False
    )


print("latest.json generated")
