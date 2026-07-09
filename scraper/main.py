import json
from datetime import datetime

from monsterhigh import check_monster_high
from funko import check_funko


result = {
    "lastUpdate": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "monsterHigh": check_monster_high(),
    "funko": check_funko()
}

with open("../docs/data.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

print("data.json actualizado correctamente.")
