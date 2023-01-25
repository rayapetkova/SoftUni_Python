budget = float(input())
fuel_L = float(input())
day = input()

fuel_price = fuel_L * 2.10
price_with_person = fuel_price + 100

if day == "Saturday":
    price_with_person = price_with_person - ((10 / 100) * price_with_person)
elif day == "Sunday":
    price_with_person = price_with_person - ((20 / 100) * price_with_person)

if budget >= price_with_person:
    print(f"Safari time! Money left: {(budget - price_with_person):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {(price_with_person - budget):.2f} lv.")