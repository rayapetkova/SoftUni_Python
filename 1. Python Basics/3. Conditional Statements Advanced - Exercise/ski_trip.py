days = int(input())
type_accommodation = input()
rate = input()
all_price = 0

if type_accommodation == "room for one person":
    nights = days - 1
    all_price = nights * 18.00
elif type_accommodation == "apartment":
    nights = days - 1
    all_price = nights * 25.00
    if nights < 10:
        all_price = all_price - ((30 / 100) * all_price)
    elif 10 < nights < 15:
        all_price = all_price - ((35 / 100) * all_price)
    elif nights > 15:
        all_price = all_price - ((50 / 100) * all_price)
elif type_accommodation == "president apartment":
    nights = days - 1
    all_price = nights * 35.00
    if nights < 10:
        all_price = all_price - ((10 / 100) * all_price)
    elif 10 < nights < 15:
        all_price = all_price - ((15 / 100) * all_price)
    elif nights > 15:
        all_price = all_price - ((20 / 100) * all_price)

if rate == "positive":
    all_price = all_price + ((25 / 100) * all_price)
elif rate == "negative":
    all_price = all_price - ((10 / 100) * all_price)

print(f"{all_price:.2f}")