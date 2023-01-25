n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            print(f"{chr(96 + i)}{chr(96 + j)}{(chr(96 + k))}")