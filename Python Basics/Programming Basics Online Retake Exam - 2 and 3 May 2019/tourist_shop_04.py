budget = float(input())

budget1 = budget
total = 0
counter = 0

while True:
    name = input()
    if name == "Stop":
        print(f"You bought {counter} products for {total:.2f} leva.")
        break
    price_product = float(input())
    counter = counter + 1

    if counter % 3 == 0:
        price_product = price_product / 2

    if price_product > (budget - total):
        print(f"You don't have enough money!")
        print(f"You need {(price_product - (budget - total)):.2f} leva!")
        break

    total = total + price_product
