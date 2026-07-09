from datetime import datetime

from core.writer import save


result = {

    "updated": datetime.utcnow().isoformat(),

    "monsterHigh": [],

    "funko": []

}


save(result)

print("OK")v
