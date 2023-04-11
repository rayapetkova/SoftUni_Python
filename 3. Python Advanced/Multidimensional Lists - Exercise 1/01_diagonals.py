size = int(input())
matrix = []

for row in range(size):
    numbers = [int(n) for n in input().split(", ")]
    matrix.append(numbers)
primary = []
secondary = []

for idx in range(size):
    primary.append(matrix[idx][idx])

for idx in range(size):
    secondary.append(matrix[idx][size - idx - 1])

print(f"Primary diagonal: {', '.join(str(n) for n in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary)}. Sum: {sum(secondary)}")