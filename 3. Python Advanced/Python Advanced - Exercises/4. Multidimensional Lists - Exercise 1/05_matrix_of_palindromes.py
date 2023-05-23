rows, cols = [int(n) for n in input().split()]
first_last = ord('a')

for row in range(first_last, rows + first_last):
    for col in range(row, cols + row):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")

    print()
