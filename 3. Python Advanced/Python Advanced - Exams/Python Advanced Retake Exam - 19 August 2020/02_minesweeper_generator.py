def check_valid_indices(c_row, c_col):
    return 0 <= c_row < size and 0 <= c_col < size


def find_bombs(c_directions, c_row, c_col):
    total_bombs = 0

    for c_direction in c_directions:
        r, c = c_row + c_direction[0], c_col + c_direction[1]

        if not check_valid_indices(r, c):
            continue

        if matrix[r][c] == "*":
            total_bombs += 1

    return total_bombs


size = int(input())
bombs = int(input())
matrix = [[0] * size for i in range(size)]

for i in range(bombs):
    command = input().split(", ")
    row, col = int(command[0][1:]), int(command[1][0:-1])

    if not check_valid_indices(row, col):
        continue

    matrix[row][col] = "*"

directions = (
    (-1, 0),   # up
    (+1, 0),   # down
    (0, -1),   # left
    (0, +1),   # right
    (-1, -1),  # up left
    (-1, +1),  # up right
    (+1, -1),  # bottom left
    (+1, +1)   # bottom right
)

for curr_row in range(size):
    for curr_col in range(size):
        if matrix[curr_row][curr_col] == "*":
            continue

        matrix[curr_row][curr_col] = find_bombs(directions, curr_row, curr_col)

[print(' '.join(str(n) for n in nested)) for nested in matrix]
