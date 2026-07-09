import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

OUTPUT = ROOT / "docs" / "latest.json"


data = {

    "updated": datetime.utcnow().isoformat(),

    "monsterHigh": [],

    "funko": []

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
