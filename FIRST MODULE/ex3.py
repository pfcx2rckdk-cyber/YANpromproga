sogl = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz"
gl = "AaEeIiOoUuYy"

while True:
    a = input()
    if a == "":
        break

    if len(a) < 4:
        print("Слишком короткое.")
    elif len(a) >= 20:
        print("Слишком длинное.")
    elif a[0] not in gl:
        print("Неверное начало.")
    elif a[-1] not in sogl:
        print("Неверный конец.")
    else:
        found_pair = None
        for i in range(len(a) - 1):
            if a[i] in gl and a[i + 1] in gl:
                found_pair = (a[i] + a[i + 1]).lower()
                break

        if found_pair:
            print(f"Две гласные {found_pair} подряд.")
        else:
            print("Красиво!")