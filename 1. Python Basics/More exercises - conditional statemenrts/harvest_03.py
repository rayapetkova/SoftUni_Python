from math import ceil, floor

x_in_m = int(input())
y_grapes_for_one_m = float(input())
z_wine_in_L = int(input())
workers = int(input())

all_grapes = x_in_m * y_grapes_for_one_m
for_wine = (40 / 100) * all_grapes
wine_for_one_kg_grapes = 1 / 2.5
all_wine = wine_for_one_kg_grapes * for_wine

if all_wine < z_wine_in_L:
    print(f"It will be a tough winter! More {floor(z_wine_in_L - all_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {ceil(all_wine)} liters.")
    print(f"{ceil(all_wine - z_wine_in_L)} liters left -> {ceil((all_wine - z_wine_in_L) / workers)} liters per person.")