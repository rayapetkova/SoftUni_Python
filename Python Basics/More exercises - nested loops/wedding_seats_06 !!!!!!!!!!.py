finish_sector = input()
rows_in_first_sector = int(input())
odd_row_seats_num = int(input())


for i in range(65, ord(finish_sector)):
    if i > 65:
        rows_in_first_sector = rows_in_first_sector + 1
    for j in range(rows_in_first_sector, rows_in_first_sector + 1):
        if rows_in_first_sector % 2 != 0:
            print(f"{chr(i)}{rows_in_first_sector}{chr(odd_row_seats_num)}")
        else:
            even_row_seats = odd_row_seats_num + 2
            print(f"{chr(i)}{rows_in_first_sector}{chr(even_row_seats)}")