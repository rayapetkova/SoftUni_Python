movie = input()
pack = input()
num_tickets = int(input())

bill = 0

if movie == "John Wick":
    if pack == "Drink":
        bill += 12 * num_tickets
    elif pack == "Popcorn":
        bill += 15 * num_tickets
    elif pack == "Menu":
        bill += 19 * num_tickets
elif movie == "Star Wars":
    if pack == "Drink":
        bill += 18 * num_tickets
    elif pack == "Popcorn":
        bill += 25 * num_tickets
    elif pack == "Menu":
        bill += 30 * num_tickets

    if num_tickets >= 4:
        bill -= 0.3 * bill
elif movie == "Jumanji":
    if pack == "Drink":
        bill += 9 * num_tickets
    elif pack == "Popcorn":
        bill += 11 * num_tickets
    elif pack == "Menu":
        bill += 14 * num_tickets

    if num_tickets == 2:
        bill -= 0.15 * bill

print(f"Your bill is {bill:.2f} leva.")