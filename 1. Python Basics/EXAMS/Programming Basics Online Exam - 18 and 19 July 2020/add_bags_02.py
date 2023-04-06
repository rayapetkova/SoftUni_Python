luggage_20kg_price = float(input())
luggage_kg = float(input())
days = int(input())
luggages_num = int(input())

price = 0

if luggage_kg < 10:
    price = (20 / 100) * luggage_20kg_price
elif 10 <= luggage_kg <= 20:
    price = (50 / 100) * luggage_20kg_price
elif luggage_kg > 20:
    price = luggage_20kg_price

if days > 30:
    price = price + (10 / 100) * price
elif 7 <= days <= 30:
    price = price + (15 / 100) * price
elif days < 7:
    price = price + (40 / 100) * price

total_price = luggages_num * price
print(f"The total price of bags is: {total_price:.2f} lv. ")