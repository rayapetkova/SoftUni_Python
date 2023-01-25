budget = float(input())
season = input()
location = ()
accommodation = ()
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = (65 / 100) * budget
    elif season == "Winter":
        location = "Morocco"
        price = (45 / 100) * budget
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = (80 / 100) * budget
    elif season == "Winter":
        location = "Morocco"
        price = (60 / 100) * budget
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = (90 / 100) * budget
    elif season == "Winter":
        location = "Morocco"
        price = (90 / 100) * budget

print(f"{location} - {accommodation} - {price:.2f}")