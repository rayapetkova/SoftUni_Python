rows = int(input())
matrix = []

for i in range(rows):
    numbers = [int(n) for n in input().split(", ")]
    matrix.append(numbers)

for lst in matrix[1:]:
    matrix[0].extend(lst)

print(matrix[0])