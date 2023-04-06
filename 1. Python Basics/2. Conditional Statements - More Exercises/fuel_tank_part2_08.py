type_fuel = input()
liters = float(input())
card = input()
all_liters_price = 0

if type_fuel == "Gasoline":
    if card == "Yes":
        one_liter_gasoline = 2.22 - 0.18
        all_liters_price = liters * one_liter_gasoline
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)
    elif card == "No":
        all_liters_price = liters * 2.22
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)

elif type_fuel == "Diesel":
    if card == "Yes":
        one_liter_diesel = 2.33 - 0.12
        all_liters_price = liters * one_liter_diesel
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)
    elif card == "No":
        all_liters_price = liters * 2.33
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)

elif type_fuel == "Gas":
    if card == "Yes":
        one_liter_gas = 0.93 - 0.08
        all_liters_price = one_liter_gas * liters
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)
    elif card == "No":
        all_liters_price = liters * 0.93
        if 20 < liters <= 25:
            all_liters_price = all_liters_price - ((8 / 100) * all_liters_price)
        elif liters > 25:
            all_liters_price = all_liters_price - ((10 / 100) * all_liters_price)

print(f"{all_liters_price:.2f} lv.")