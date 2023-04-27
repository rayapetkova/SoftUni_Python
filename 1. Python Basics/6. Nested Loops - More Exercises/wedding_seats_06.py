finish_sector = input()
rows_in_first_sector = int(input())
odd_row_seats_num = int(input())

final = 0

for i in range(65, ord(finish_sector) + 1):
    for j in range(1, rows_in_first_sector + 1):
        if j % 2 != 0:
            spots = odd_row_seats_num + 2
        for k in range(97, 97 + spots):
            print(f"{chr(i)}{j}{chr(k)}")
            final += 1
    rows_in_first_sector += 1

print(final)
