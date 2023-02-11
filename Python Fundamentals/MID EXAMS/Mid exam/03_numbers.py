numbers = [int(j) for j in input().split()]

average = sum(numbers) / len(numbers)

final = [j for j in numbers if j > average]
reversed_list = list(reversed(final))

if len(final) >= 1:
    print(*sorted(reversed_list[0:5], reverse=True))
else:
    print("No")