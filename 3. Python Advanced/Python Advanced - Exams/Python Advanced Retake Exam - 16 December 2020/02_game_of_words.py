def find_player(c_size, curr_matrix):
    for r in range(c_size):
        for c in range(c_size):
            if curr_matrix[r][c] == "P":
                return r, c


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < size and 0 <= c_col < size


string_given = input()
size = int(input())

matrix = [list(input()) for i in range(size)]

player = find_player(size, matrix)
matrix[player[0]][player[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

for i in range(int(input())):
    direction = input()

    row, col = player[0] + directions[direction][0], player[1] + directions[direction][1]

    if not check_valid_indices(row, col):
        if string_given:
            string_given = string_given[:-1]
        continue

    if matrix[row][col] != "-":
        string_given += matrix[row][col]
        matrix[row][col] = "-"

    player = (row, col)

matrix[player[0]][player[1]] = "P"

print(string_given)
[print(''.join(curr_row)) for curr_row in matrix]
