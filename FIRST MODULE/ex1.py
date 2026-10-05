a = input().split()
for i in range(len(a)):
    if int(a[i]) >= 90 and int(a[i]) < 140:
        print("Можешь идти")
    else:
        print("Оставайся в Шире")
