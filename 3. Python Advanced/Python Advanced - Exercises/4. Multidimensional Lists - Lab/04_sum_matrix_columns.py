rows, columns = [int(n) for n in input().split(", ")]
matrix = []

for row in range(rows):
    numbers = [int(num) for num in input().split()]
    matrix.append(numbers)

for col in range(columns):
    total = 0
    
    for row in range(rows):
        total += matrix[row][col]

    print(total)
