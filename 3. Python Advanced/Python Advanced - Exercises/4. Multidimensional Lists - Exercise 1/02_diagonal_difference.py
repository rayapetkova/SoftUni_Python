size = int(input())
matrix = []

for row in range(size):
    numbers = [int(n) for n in input().split()]
    matrix.append(numbers)

primary, secondary = [], []

[primary.append(matrix[idx][idx]) for idx in range(size)]
[secondary.append(matrix[idx][size - idx - 1]) for idx in range(size)]

print(abs(sum(primary) - sum(secondary)))
