def print_half(num, stars):
    for i in range(num - stars):
        print(" ", end="")

    for j in range(1, stars):
        print(f"* ", end="")

    print("*")


n = int(input())

for first_stars in range(1, n):
    print_half(n, first_stars)

for second_stars in range(n, 0, -1):
    print_half(n, second_stars)
