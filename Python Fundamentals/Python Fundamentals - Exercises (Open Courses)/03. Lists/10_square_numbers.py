import math

numbers = list(map(int, input().split()))
final = []

for num in numbers:
    if num >= 0:
        root = math.sqrt(num)
        if root.is_integer():
            final.append(num)

print(*sorted(final, reverse=True), sep=" ")