w = float(input())
h = float(input())

h_in_cm = h * 100
h_area_without_hall = h_in_cm - 100
desks_in_a_row = h_area_without_hall // 70

w_in_cm = w * 100
rows = w_in_cm // 120

all_seats = rows * desks_in_a_row - 3

print(f"{all_seats:.0f}")