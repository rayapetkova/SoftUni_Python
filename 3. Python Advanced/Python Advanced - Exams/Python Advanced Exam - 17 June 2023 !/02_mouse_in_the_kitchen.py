def check_valid_indices(r, c):
    return 0 <= r < rows and 0 <= c < cols


def find_mouse(curr_matrix):
    c_mouse, all_cheese = (), []
    for c_row in range(rows):
        for c_col in range(cols):
            if curr_matrix[c_row][c_col] == "M":
                c_mouse = (c_row, c_col)

            elif curr_matrix[c_row][c_col] == "C":
                all_cheese.append((c_row, c_col))

    return c_mouse, all_cheese


rows, cols = [int(n) for n in input().split(",")]

matrix = [list(input()) for i in range(rows)]

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

mouse, total_cheese = find_mouse(matrix)
matrix[mouse[0]][mouse[1]] = "*"

while True:
    direction = input()

    if direction == "danger":
        matrix[mouse[0]][mouse[1]] = "M"
        print(f"Mouse will come back later!")
        break

    row, col = mouse[0] + directions[direction][0], mouse[1] + directions[direction][1]

    if not check_valid_indices(row, col):
        matrix[mouse[0]][mouse[1]] = "M"
        print(f"No more cheese for tonight!")
        break

    if matrix[row][col] == "C":
        total_cheese.remove((row, col))

        if not total_cheese:
            matrix[row][col] = "M"
            print(f"Happy mouse! All the cheese is eaten, good night!")
            break

        mouse = (row, col)
        matrix[row][col] = "*"

    elif matrix[row][col] == "T":
        matrix[row][col] = "M"
        mouse = (row, col)
        print(f"Mouse is trapped!")
        break

    elif matrix[row][col] == "@":
        continue

    mouse = (row, col)

[print(''.join(nested)) for nested in matrix]
