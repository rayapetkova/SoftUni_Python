season = input()
km_for_month = float(input())

price = 0

if season == "Spring" or season == "Autumn":
    if km_for_month <= 5000:
        price = km_for_month * 0.75
    elif 5000 < km_for_month <= 10000:
        price = km_for_month * 0.95
    elif 10000 < km_for_month <= 20000:
        price = km_for_month * 1.45
elif season == "Summer":
    if km_for_month <= 5000:
        price = km_for_month * 0.90
    elif 5000 < km_for_month <= 10000:
        price = km_for_month * 1.10
    elif 10000 < km_for_month <= 20000:
        price = km_for_month * 1.45
elif season == "Winter":
    if km_for_month <= 5000:
        price = km_for_month * 1.05
    elif 5000 < km_for_month <= 10000:
        price = km_for_month * 1.25
    elif 10000 < km_for_month <= 20000:
        price = km_for_month * 1.45

price = price * 4
price = price - ((10 / 100) * price)
print(f"{price:.2f}")