
vvod = input().split()
start, end = int(vvod[0]), int(vvod[1])
new = 1
time = 0

while start < end:
    start += new
    new += 2
    time += 1
    
print(f'Время - {time}.''\n'f'Количество дозорных - {start}.')
    
        