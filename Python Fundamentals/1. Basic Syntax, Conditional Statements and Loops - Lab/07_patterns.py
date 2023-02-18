number_stars = int(input())

for i in range(1, number_stars + 1):
    print("*" * i)
for j in range(number_stars -1, -1, -1):
    print("*" * j)