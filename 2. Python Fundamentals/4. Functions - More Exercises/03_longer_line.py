from math import floor


def longer_line(x1_n, y1_n, x2_n, y2_n, x3_n, y3_n, x4_n, y4_n):
    x1, y1, x2, y2 = abs(x1_n), abs(y1_n), abs(x2_n), abs(y2_n)
    x3, y3, x4, y4 = abs(x3_n), abs(y3_n), abs(x4_n), abs(y4_n)

    if floor(x1 + y1 + x2 + y2) >= floor(x3 + y3 + x4 + y4):
        closest_1 = x1 + y1
        closest_2 = x2 + y2
        if closest_1 <= closest_2:
            return f"({x1_n}, {y1_n})({x2_n}, {y2_n})"
        if closest_1 > closest_2:
            return f"({x2_n}, {y2_n})({x1_n}, {y1_n})"

    elif floor(x1 + y1 + x2 + y2) < floor(x3 + y3 + x4 + y4):
        closest_1 = x3 + y3
        closest_2 = x4 + y4
        if closest_1 <= closest_2:
            return f"({x3_n}, {y3_n})({x4_n}, {y4_n})"
        if closest_1 > closest_2:
            return f"({x4_n}, {y4_n})({x3_n}, {y3_n})"


curr_x1, curr_y1 = floor(float(input())), floor(float(input()))
curr_x2, curr_y2 = floor(float(input())), floor(float(input()))
curr_x3, curr_y3 = floor(float(input())), floor(float(input()))
curr_x4, curr_y4 = floor(float(input())), floor(float(input()))

print(longer_line(curr_x1, curr_y1, curr_x2, curr_y2, curr_x3, curr_y3, curr_x4, curr_y4))
