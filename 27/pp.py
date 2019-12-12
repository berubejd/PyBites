import json

from pathlib import Path
from pprint import pprint as pp

JSON_FILE = Path("/tmp/1.json")

json_data = []

with open(JSON_FILE, "r") as fp:
    json_data = json.loads(fp.read())

pp(json_data)
