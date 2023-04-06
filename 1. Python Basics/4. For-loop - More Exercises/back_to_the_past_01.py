inherited_money = float(input())
year = int(input())

ivan_start_age = 17
money = inherited_money

for y in range(1800, year + 1):
    if y % 2 == 0:
        money = money - 12000
    else:
        ivan_start_age = ivan_start_age + 2
        money = money - (12000 + 50 * ivan_start_age)

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")