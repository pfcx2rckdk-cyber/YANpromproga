import csv
import json
from collections import defaultdict

races = defaultdict(list)

with open("members.csv", "r", encoding="utf-8") as m:
    reader = csv.DictReader(m)
    for row in reader:
        race = row['race']
        name = row["name"]
        races[race].append(name)

with open("council.jsonlines", "w", encoding="utf-8") as out:
    for races_name in sorted(races.keys()):
        members = sorted(races[races_name], key=lambda name: (-len(name), name))

        data = {"race": races_name, "members": members}

        json_line = json.dumps(data, ensure_ascii=False)
        out.write(json_line + "\n")