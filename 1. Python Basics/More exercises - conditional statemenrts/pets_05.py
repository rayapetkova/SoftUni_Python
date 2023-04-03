from math import floor, ceil

days_num = int(input())
left_food_in_kg = int(input())
one_day_food_for_dog_in_kg = float(input())
one_day_food_for_cat_in_kg = float(input())
one_day_food_for_turtle_in_g = float(input())

all_food_for_dog = days_num * one_day_food_for_dog_in_kg
all_food_for_cat = days_num * one_day_food_for_cat_in_kg
all_food_for_turtle = days_num * (one_day_food_for_turtle_in_g / 1000)
all_food = all_food_for_dog + all_food_for_cat + all_food_for_turtle

if all_food <= left_food_in_kg:
    print(f"{floor(left_food_in_kg - all_food)} kilos of food left.")
else:
    print(f"{ceil(all_food - left_food_in_kg)} more kilos of food are needed.")