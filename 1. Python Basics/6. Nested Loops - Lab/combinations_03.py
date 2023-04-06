number = int(input())
combinations = 0

for x1 in range(0, number + 1):
    for x2 in range(0, number + 1):
        for x3 in range(0, number + 1):
            result = x1 + x2 + x3
            if result == number:
                combinations += 1

print(combinations)