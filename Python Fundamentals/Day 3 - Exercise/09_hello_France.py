purchases = input().split("|")
budget = int(input())
total = 0
all_prices = 0
price = 0
items = []

for i in purchases:
    if "Clothes" in i:
        i = i.split("->")
        price = float(i[1])
        if price <= 50.00 and price <= budget:
            items.append(f"{((40 / 100) * price + price):.2f}")
            total += (40 / 100) * price + price
            all_prices += price
            budget = budget - price
    elif "Shoes" in i:
        i = i.split("->")
        price = float(i[1])
        if price <= 35.00 and price <= budget:
            items.append(f"{((40 / 100) * price + price):.2f}")
            total += (40 / 100) * price + price
            all_prices += price
            budget = budget - price
    elif "Accessories" in i:
        i = i.split("->")
        price = float(i[1])
        if price <= 20.50 and price <= budget:
            items.append(f"{((40 / 100) * price + price):.2f}")
            total += (40 / 100) * price + price
            all_prices += price
            budget = budget - float(price)


result = ' '.join(str(i) for i in items)
print(result)
profit = total - all_prices
print(f"Profit: {profit:.2f}")

if budget + total > 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")