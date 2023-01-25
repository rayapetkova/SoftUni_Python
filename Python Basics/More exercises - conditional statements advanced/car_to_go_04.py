budget = float(input())
season = input()
type_car = ()
class_car = ()
price = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = (35 / 100) * budget
    elif season == "Winter":
        type_car = "Jeep"
        price = (65 / 100) * budget
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = (45 / 100) * budget
    elif season == "Winter":
        type_car = "Jeep"
        price = (80 / 100) * budget
elif budget > 500:
    class_car = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_car = "Jeep"
        price = (90 / 100) * budget

print(f"{class_car}")
print(f"{type_car} - {price:.2f}")