term = input()
type_contract = input()
mobile_internet = input()
months = int(input())
one_month_price = 0

if term == "one":
    if type_contract == "Small":
        one_month_price = 9.98
    elif type_contract == "Middle":
        one_month_price = 18.99
    elif type_contract == "Large":
        one_month_price = 25.98
    elif type_contract == "ExtraLarge":
        one_month_price = 35.99

elif term == "two":
    if type_contract == "Small":
        one_month_price = 8.58
    elif type_contract == "Middle":
        one_month_price = 17.09
    elif type_contract == "Large":
        one_month_price = 23.59
    elif type_contract == "ExtraLarge":
        one_month_price = 31.79

if mobile_internet == "yes":
    if one_month_price <= 10.00:
        one_month_price = one_month_price + 5.50
    elif 10.00 < one_month_price <= 30.00:
        one_month_price = one_month_price + 4.35
    elif one_month_price > 30.00:
        one_month_price = one_month_price + 3.85

total = one_month_price * months

if term == "two":
    total = total - ((3.75 / 100) * total)

print(f"{total:.2f} lv.")