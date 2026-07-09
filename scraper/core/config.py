from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]


CONFIG_FILE = ROOT / "config.json"


def load():

    with open(CONFIG_FILE, encoding="utf-8") as file:

        return json.load(file)from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]


CONFIG_FILE = ROOT / "config.json"


def load():

    with open(CONFIG_FILE, encoding="utf-8") as file:

        return json.load(file)
