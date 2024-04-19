budget = float(input())
number_series = int(input())

total_price = 0

for series in range(0, number_series):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price = series_price - 0.5 * series_price  # series_price -= 0.5 * series_price
    elif series_name == "Lucifer":
        series_price = series_price - 0.4 * series_price
    elif series_name == "Protector":
        series_price = series_price - 0.3 * series_price
    elif series_name == "TotalDrama":
        series_price = series_price - 0.2 * series_price
    elif series_name == "Area":
        series_price = series_price - 0.1 * series_price

    total_price = total_price + series_price  # total_price += series_price

if budget >= total_price:
    money_left = budget - total_price
    print(f"You bought all the series and left with {money_left:.2f} lv.")
else:
    money_needed = total_price - budget
    print(f"You need {money_needed:.2f} lv. more to buy the series!")
