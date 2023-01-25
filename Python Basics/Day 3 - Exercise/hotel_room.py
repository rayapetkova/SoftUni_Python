month = input()
overnight_stay_num = int(input())
all_price_studio = 0
all_price_apartment = 0

if month == "May" or month == "October":
    all_price_studio = 50 * overnight_stay_num
    all_price_apartment = 65 * overnight_stay_num
    if 7 < overnight_stay_num <= 14:
        all_price_studio = all_price_studio - ((5 / 100) * all_price_studio)
        all_price_apartment = 65 * overnight_stay_num
    elif overnight_stay_num > 14:
        all_price_studio = all_price_studio - ((30 / 100) * all_price_studio)
        all_price_apartment = all_price_apartment - ((10 / 100) * all_price_apartment)
elif month == "June" or month == "September":
    all_price_studio = 75.20 * overnight_stay_num
    all_price_apartment = 68.70 * overnight_stay_num
    if overnight_stay_num > 14:
        all_price_studio = all_price_studio - ((20 / 100) * all_price_studio)
        all_price_apartment = all_price_apartment - ((10 / 100) * all_price_apartment)
elif month == "July" or month == "August":
    all_price_studio = 76 * overnight_stay_num
    all_price_apartment = 77 * overnight_stay_num
    if overnight_stay_num > 14:
        all_price_studio = 76 * overnight_stay_num
        all_price_apartment = all_price_apartment - ((10 / 100) * all_price_apartment)

print(f"Apartment: {all_price_apartment:.2f} lv.")
print(f"Studio: {all_price_studio:.2f} lv.")