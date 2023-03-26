def area(curr_base, curr_height):
    return (curr_base * curr_height) / 2


base, height = float(input()), float(input())
print(f"{area(base, height):.12g}")