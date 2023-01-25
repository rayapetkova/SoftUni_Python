budget = float(input())
season = input()
all_price = 0
place = ()
accommodation = ()

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        all_price = (30 / 100) * budget
    elif season == "winter":
        accommodation = "Hotel"
        all_price = (70 / 100) * budget
elif 100 < budget <= 1000:
    place = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        all_price = (40 / 100) * budget
    elif season == "winter":
        accommodation = "Hotel"
        all_price = (80 / 100) * budget
elif budget > 1000:
    place = "Europe"
    if season == "summer" or season == "winter":
        accommodation = "Hotel"
        all_price = (90 / 100) * budget

print(f"Somewhere in {place}")
print(f"{accommodation} - {all_price:.2f}")