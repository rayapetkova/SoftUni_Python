num = int(input())
total = 0

for i in range(1, num + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    price = (price_per_capsule * capsules_needed_per_day) * days
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or (
            capsules_needed_per_day < 1 or capsules_needed_per_day > 2000):
        continue

    print(f"The price for the coffee is: ${price:.2f}")
    total = total + price

print(f"Total: ${total:.2f}")