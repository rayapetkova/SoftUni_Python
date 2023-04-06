budget = float(input())
category = input()
people_num = int(input())
all_price = 0

if category == "VIP":
    ticket = 499.99
    if 1 <= people_num <= 4:
        all_price = ticket * people_num + ((75 / 100) * budget)
    elif 5 <= people_num <= 9:
        all_price = ticket * people_num + ((60 / 100) * budget)
    elif 10 <= people_num <= 24:
        all_price = ticket * people_num + ((50 / 100) * budget)
    elif 25 <= people_num <= 49:
        all_price = ticket * people_num + ((40 / 100) * budget)
    elif people_num >= 50:
        all_price = ticket * people_num + ((25 / 100) * budget)
elif category == "Normal":
    ticket = 249.99
    if 1 <= people_num <= 4:
        all_price = ticket * people_num + ((75 / 100) * budget)
    elif 5 <= people_num <= 9:
        all_price = ticket * people_num + ((60 / 100) * budget)
    elif 10 <= people_num <= 24:
        all_price = ticket * people_num + ((50 / 100) * budget)
    elif 25 <= people_num <= 49:
        all_price = ticket * people_num + ((40 / 100) * budget)
    elif people_num >= 50:
        all_price = ticket * people_num + ((25 / 100) * budget)

if budget >= all_price:
    print(f"Yes! You have {(budget - all_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(all_price - budget):.2f} leva.")