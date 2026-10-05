def path(data, criterion):
    res = []
    for i in data:
        if not criterion(i):
            res.append(i)
        else:
            break
    if not res:
        return "Danger!"
    return ", ".join(res)


def func(line):
    return len(line.split()) == 2