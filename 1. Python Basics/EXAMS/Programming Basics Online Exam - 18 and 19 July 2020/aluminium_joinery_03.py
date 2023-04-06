joinery_num = int(input())
type_joinery = input()
delivery_type = input()

price = 0


if type_joinery == "90X130":
    price = price + joinery_num * 110
    if 30 <= joinery_num < 60:
        price = price - (5 / 100) * price
    elif joinery_num >= 60:
        price = price - (8 / 100) * price

elif type_joinery == "100X150":
    price = price + joinery_num * 140
    if 40 <= joinery_num < 80:
        price = price - (6 / 100) * price
    elif joinery_num >= 80:
        price = price - (10 / 100) * price

elif type_joinery == "130X180":
    price = price + joinery_num * 190
    if 20 <= joinery_num < 50:
        price = price - (7 / 100) * price
    elif joinery_num >= 50:
        price = price - (12 / 100) * price

elif type_joinery == "200X300":
    price = price + joinery_num * 250
    if 25 <= joinery_num < 50:
        price = price - (9 / 100) * price
    elif joinery_num >= 50:
        price = price - (14 / 100) * price

if delivery_type == "With delivery":
    price = price + 60
elif delivery_type == "Without delivery":
    price = price

if joinery_num >= 99:
    price = price - (4 / 100) * price

if joinery_num > 10:
    print(f"{price:.2f} BGN")
else:
    print("Invalid order")