trip_price = float(input())
puzzles_num = int(input())
dolls_num = int(input())
bears_num = int(input())
minions_num = int(input())
trucks_num = int(input())

puzzles_price = puzzles_num * 2.60
dolls_price = dolls_num * 3
bears_price = bears_num * 4.10
minions_price = minions_num * 8.20
trucks_price = trucks_num * 2
toys_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
toys_num = puzzles_num + dolls_num + bears_num + minions_num + trucks_num

if toys_num >= 50:
    price_with_discount = toys_price - (25 / 100) * toys_price
    rent = (10 / 100) * price_with_discount
    profit = price_with_discount - rent
else:
    rent = (10 / 100) * toys_price
    profit = toys_price - rent

if profit >= trip_price:
    print(f"Yes! {(profit - trip_price):.2f} lv left.")
else:
    print(f"Not enough money! {(trip_price - profit):.2f} lv needed.")
