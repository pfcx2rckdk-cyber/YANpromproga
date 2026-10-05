def arsenal(*weapons):
    res = []
    s_len = sum(len(item) for item in weapons)
    avg = s_len / len(weapons) if weapons else 0

    for item in weapons:
        if len(item) <= avg:
            formatted_item = item.capitalize()
            if formatted_item not in res:
                res.append(formatted_item)

    res.sort()
    return res