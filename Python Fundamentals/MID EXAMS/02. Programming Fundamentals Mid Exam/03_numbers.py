numbers = [int(j) for j in input().split()]

average = sum(numbers) / len(numbers)

final = [j for j in numbers if j > average]

if len(final) >= 1:
    print(*sorted(final, reverse=True)[0:5])
else:
    print("No")



# 2

