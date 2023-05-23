def print_matrix(curr_matrix):
    for nested_lst in curr_matrix:
        print(*nested_lst, sep=" ")


def check_valid_indices(position, length):
    if position >= length or position < 0:
        return False
    return True


rows, cols = [int(n) for n in input().split()]
matrix = []

for row in range(rows):
    matrix.append(list(input().split()))

while True:
    line = input()
    if line == "END":
        break

    command = line.split()
    if "swap" in command and len(command) == 5:
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])

        if check_valid_indices(row1, rows) and check_valid_indices(col1, cols)\
                and check_valid_indices(row2, rows) and check_valid_indices(col2, cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print_matrix(matrix)

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
