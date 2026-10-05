import json

title, material, keeper, power, avg, visibility = '', '', '', 0, 0, ''
with open("rings.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.strip().split()
        if not words:
            continue
        ag = int(words[3])
        if ag >= power:
            power = ag
            title = words[0]
            material = words[1]
            keeper = words[2]
            avg = len(title) + len(keeper) + power
            if avg % 2 == 0:
                visibility = "visible"
            else:
                visibility = "invisible"

result = {
    "title": title,
    "material": material,
    "keeper": keeper,
    "power": power,
    "visibility": visibility
}

with open("powerful.json", "w", encoding="utf-8") as f_out:
    json.dump(result, f_out, indent=2)