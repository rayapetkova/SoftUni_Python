rows, columns = list(map(int, input().split(", ")))
matrix = []
total = 0

for i in range(rows):
    numbers = list(map(int, input().split(", ")))
    matrix.append(numbers)

for row in matrix:
    total += sum(row)

print(total)
print(matrix)