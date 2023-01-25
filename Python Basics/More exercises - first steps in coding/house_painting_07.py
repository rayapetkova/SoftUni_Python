x = float(input())
y = float(input())
h = float(input())

first_square_wall = (x * x) - (1.2 * 2)
second_square_wall = x * x
the_two_square_walls = first_square_wall + second_square_wall
side_wall = (x * y) - (1.5 * 1.5)
the_two_side_walls = side_wall * 2
all_walls = the_two_side_walls + the_two_square_walls
green_paint_for_one_m2 = 1 / 3.4
green_paint_for_all_walls = all_walls * green_paint_for_one_m2
print(f"{green_paint_for_all_walls:.2f}")

the_two_roof_rectangles = 2 * (x * y)
the_two_roof_triangles = 2 * ((x * h) / 2)
all_roof_area = the_two_roof_triangles + the_two_roof_rectangles
red_paint_for_one_m2 = 1 / 4.3
red_paint_for_all_roof_area = all_roof_area * red_paint_for_one_m2
print(f"{red_paint_for_all_roof_area:.2f}")