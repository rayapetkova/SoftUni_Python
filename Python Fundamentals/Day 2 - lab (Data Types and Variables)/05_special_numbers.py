n = int(input())
special = False

for i in range(1, n + 1):
    new = 0
    if i > 10:
        i = str(i)
        for j in i:
            j = int(j)
            new = new + j
            if new == 5 or new == 7 or new == 11:
                special = True
            else:
                special = False
    else:
        i = int(i)
        if i == 5 or i == 7:
            special = True
        else:
            special = False

    if special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")