
def scrolls(*data):
    result = []
    for ti, scr in data:
        if 'elves' in scr.lower():
            result.append(ti)
    
    result.sort(reverse=True)
    return result