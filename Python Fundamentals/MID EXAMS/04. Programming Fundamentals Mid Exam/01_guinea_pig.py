food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
weight_in_kg = float(input())

food_gr = food_in_kg * 1000
hay_gr = hay_in_kg * 1000
cover_gr = cover_in_kg * 1000
weight_gr = weight_in_kg * 1000

days = 1
go_to_store = False

while True:
    if days == 31:
        break
    food_gr -= 300
    if days % 2 == 0:
        hay_gr -= (5 / 100) * food_gr
    if days % 3 == 0:
        cover_gr -= (1 / 3) * weight_gr
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        go_to_store = True
        break
    days += 1

if go_to_store:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.")