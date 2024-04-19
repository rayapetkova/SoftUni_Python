movie = input()
pack = input()
num_tickets = int(input())

bill = 0

if movie == "John Wick":
    if pack == "Drink":
        total_sum = num_tickets * 12
        bill = total_sum
    elif pack == "Popcorn":
        total_sum = num_tickets * 15
        bill = total_sum
    elif pack == "Menu":
        total_sum = num_tickets * 19
        bill = total_sum
elif movie == "Star Wars":
    if pack == "Drink":
        total_sum = num_tickets * 18
        bill = total_sum
    elif pack == "Popcorn":
        total_sum = num_tickets * 25
        bill = total_sum
    elif pack == "Menu":
        total_sum = num_tickets * 30
        bill = total_sum

    if num_tickets >= 4:
        bill = bill - 0.3 * bill  # bill -= 0.3 * bill
elif movie == "Jumanji":
    if pack == "Drink":
        total_sum = num_tickets * 9
        bill = total_sum
    elif pack == "Popcorn":
        total_sum = num_tickets * 11
        bill = total_sum
    elif pack == "Menu":
        total_sum = num_tickets * 14
        bill = total_sum

    if num_tickets == 2:
        bill = bill - 0.15 * bill

print(f"Your bill is {bill:.2f} leva.")