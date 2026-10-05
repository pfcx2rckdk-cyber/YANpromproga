a = input().split()
bl = 0
wh = 0

for i in a:
    da = int(i)
    if da % 2 == 0:
        wh += da
    else:
        bl += da

print(f"Тёмного мёда: {bl}.")
print(f"Светлого мёда: {wh}.")