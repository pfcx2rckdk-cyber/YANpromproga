def potions(soch):
    ans = ""
    with open("recipes.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(",")
            if soch.lower() in line[0].lower():
                ans = line[1:]

    return ans


