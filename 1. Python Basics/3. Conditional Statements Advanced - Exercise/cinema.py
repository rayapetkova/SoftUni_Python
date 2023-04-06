projection = input()
rows = int(input())
columns = int(input())
all_price = 0

if projection == "Premiere":
    ticket = 12.00
    seats = rows * columns
    all_price = ticket * seats
elif projection == "Normal":
    ticket = 7.50
    seats = rows * columns
    all_price = ticket * seats
elif projection == "Discount":
    ticket = 5.00
    seats = rows * columns
    all_price = ticket * seats

print(f"{all_price:.2f} leva")