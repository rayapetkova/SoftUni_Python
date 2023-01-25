budget = int(input())
season = input()
people_num = int(input())
rent = 0

if season == "Spring":
    rent = 3000
    if people_num <= 6:
        rent = rent - ((10 / 100) * rent)
    elif 6 < people_num <= 11:
        rent = rent - ((15 / 100) * rent)
    else:
        rent = rent - ((25 / 100) * rent)
    if people_num % 2 == 0:
        rent = rent - ((5 / 100) * rent)
elif season == "Summer":
    rent = 4200
    if people_num <= 6:
        rent = rent - ((10 / 100) * rent)
    elif 6 < people_num <= 11:
        rent = rent - ((15 / 100) * rent)
    else:
        rent = rent - ((25 / 100) * rent)
    if people_num % 2 == 0:
        rent = rent - ((5 / 100) * rent)
elif season == "Autumn":
    rent = 4200
    if people_num <= 6:
        rent = rent - ((10 / 100) * rent)
    elif 6 < people_num <= 11:
        rent = rent - ((15 / 100) * rent)
    else:
        rent = rent - ((25 / 100) * rent)
elif season == "Winter":
    rent = 2600
    if people_num <= 6:
        rent = rent - ((10 / 100) * rent)
    elif 6 < people_num <= 11:
        rent = rent - ((15 / 100) * rent)
    else:
        rent = rent - ((25 / 100) * rent)
    if people_num % 2 == 0:
        rent = rent - ((5 / 100) * rent)

if budget >= rent:
    print(f"Yes! You have {(budget - rent):.2f} leva left.")
else:
    print(f"Not enough money! You need {(rent - budget):.2f} leva.")