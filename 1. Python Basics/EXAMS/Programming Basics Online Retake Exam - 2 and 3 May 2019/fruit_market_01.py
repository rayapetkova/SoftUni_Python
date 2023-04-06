strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price_for_one_kg = strawberries_price / 2
oranges_price_for_one_kg = raspberries_price_for_one_kg - ((40 / 100) * raspberries_price_for_one_kg)
bananas_price_for_one_kg = raspberries_price_for_one_kg - ((80 / 100) * raspberries_price_for_one_kg)

raspberries_price = raspberries_price_for_one_kg * raspberries_kg
oranges_price = oranges_price_for_one_kg * oranges_kg
bananas_price = bananas_price_for_one_kg * bananas_kg
strawberries_price = strawberries_price * strawberries_kg

total = raspberries_price + oranges_price + bananas_price + strawberries_price
print(f"{total:.2f}")