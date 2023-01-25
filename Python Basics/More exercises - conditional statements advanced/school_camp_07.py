season = input()
type_group = input()
students_num = int(input())
nights = int(input())

price = 0
sport = ()

if season == "Winter":
    if type_group == "girls":
        price = nights * students_num * 9.60
        sport = "Gymnastics"
    elif type_group == "boys":
        price = nights * students_num * 9.60
        sport = "Judo"
    elif type_group == "mixed":
        price = nights * students_num * 10
        sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        price = nights * students_num * 7.20
        sport = "Athletics"
    elif type_group == "boys":
        price = nights * students_num * 7.20
        sport = "Tennis"
    elif type_group == "mixed":
        price = nights * students_num * 9.50
        sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        price = nights * students_num * 15
        sport = "Volleyball"
    elif type_group == "boys":
        price = nights * students_num * 15
        sport = "Football"
    elif type_group == "mixed":
        price = nights * students_num * 20
        sport = "Swimming"

if students_num >= 50:
    price = price - ((50 / 100) * price)
    print(f"{sport} {price:.2f} lv.")
elif 20 <= students_num < 50:
    price = price - ((15 / 100) * price)
    print(f"{sport} {price:.2f} lv.")
elif 10 <= students_num < 20:
    price = price - ((5 / 100) * price)
    print(f"{sport} {price:.2f} lv.")
else:
    print(f"{sport} {price:.2f} lv.")