rows, cols = [int(n) for n in input().split()]
first_last = ord('a')

for row in range(first_last, rows + first_last):
    for col in range(first_last, cols + first_last):
        print(f"{chr(row)}{chr(col + row - 97)}{chr(row)}", end=" ")
    print()
