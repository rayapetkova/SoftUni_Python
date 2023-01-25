import math

type = input()

if type == "square":
    a = float(input())
    S = a * a
    print(f"{S:.3f}")
elif type == "rectangle":
    a = float(input())
    b = float(input())
    S = a * b
    print(f"{S:.3f}")
elif type == "circle":
    r = float(input())
    S = r * r * math.pi
    print(f"{S:.3f}")
elif type == "triangle":
    a = float(input())
    ha = float(input())
    S = ((a * ha) / 2)
    print(f"{S:.3f}")