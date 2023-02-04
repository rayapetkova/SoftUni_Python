from math import floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    if abs(x1) + abs(y1) + abs(x2) + abs(y2) > abs(x3) + abs(y3) + abs(x4) + abs(y4):
        closest_1 = abs(x1) + abs(y1)
        closest_2 = abs(x2) + abs(y2)
        if closest_1 < closest_2:
            return f"({x1}, {y1})({x2}, {y2})"
        if closest_1 > closest_2:
            return f"({x2}, {y2})({x1}, {y1})"
    elif abs(x1) + abs(y1) + abs(x2) + abs(y2) < abs(x3) + abs(y3) + abs(x4) + abs(y4):
        closest_1 = abs(x3) + abs(y3)
        closest_2 = abs(x4) + abs(y4)
        if closest_1 < closest_2:
            return f"({x3}, {y3})({x4}, {y4})"
        if closest_1 > closest_2:
            return f"({x4}, {y4})({x3}, {y3})"
    elif abs(x1) + abs(y1) + abs(x2) + abs(y2) == abs(x3) + abs(y3) + abs(x4) + abs(y4):
        closest_1 = abs(x1) + abs(y1)
        closest_2 = abs(x2) + abs(y2)
        if closest_1 < closest_2:
            return f"({x1}, {y1})({x2}, {y2})"
        if closest_1 > closest_2:
            return f"({x2}, {y2})({x1}, {y1})"


curr_x1, curr_y1 = float(input()), float(input())
curr_x2, curr_y2 = float(input()), float(input())
curr_x3, curr_y3 = float(input()), float(input())
curr_x4, curr_y4 = float(input()), float(input())

print(longer_line(curr_x1, curr_y1, curr_x2, curr_y2, curr_x3, curr_y3, curr_x4, curr_y4))
