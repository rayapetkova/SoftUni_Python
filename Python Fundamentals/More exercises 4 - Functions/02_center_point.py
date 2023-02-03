import math
from math import floor


def coordinates(x1, y1, x2, y2):
    closest_1 = abs(x1) + abs(y1)
    closest_2 = abs(x2) + abs(y2)
    if closest_1 == closest_2:
        return f"({floor(x1)}, {floor(y1)})"
    if closest_1 > closest_2:
        return f"({floor(x2)}, {floor(y2)})"
    if closest_1 < closest_2:
        return f"({floor(x1)}, {floor(y1)})"


current_x1 = float(input())
current_y1 = float(input())
current_x2 = float(input())
current_y2 = float(input())

print(coordinates(current_x1, current_y1, current_x2, current_y2))