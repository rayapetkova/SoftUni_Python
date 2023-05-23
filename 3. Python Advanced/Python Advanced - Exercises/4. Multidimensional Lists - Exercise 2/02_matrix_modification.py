def check_valid_indices(c_row, c_col):
    if 0 <= c_row < len(matrix) and 0 <= c_col < len(matrix):
        return True

    return False


rows = int(input())
matrix = [[int(n) for n in input().split()] for i in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    command = line.split()
    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if not check_valid_indices(row, col):
        print(f"Invalid coordinates")
        continue

    if "Add" in command:
        matrix[row][col] += value
    elif "Subtract" in command:
        matrix[row][col] -= value

for nested in matrix:
    print(*nested, sep=" ")