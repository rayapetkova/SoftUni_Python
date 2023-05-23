size = int(input())
matrix = []

for row in range(size):
    characters = list(input())
    matrix.append(characters)

symbol = input()
found = False

for row in range(size):
    for col in range(size):

        if matrix[row][col] == symbol:
            found = True
            print(f"({row}, {col})")
            break

    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
    
