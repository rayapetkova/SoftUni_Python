def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


def move_command(steps_move, curr_matrix, curr_position, curr_move_row, curr_move_col):
    c_row = curr_position[0] + (curr_move_row * steps_move)
    c_col = curr_position[1] + (curr_move_col * steps_move)

    if not check_valid_indices(c_row, c_col) or curr_matrix[c_row][c_col] == "x":
        return curr_position

    return c_row, c_col


def shoot_command(curr_position, move_directions, curr_matrix):
    curr_row = curr_position[0] + move_directions[0]
    curr_col = curr_position[1] + move_directions[1]

    while True:
        if not check_valid_indices(curr_row, curr_col):
            break

        if curr_matrix[curr_row][curr_col] == "x":
            curr_matrix[curr_row][curr_col] = "."
            return list((curr_row, curr_col))

        curr_row += move_directions[0]
        curr_col += move_directions[1]


SIZE = 5
matrix = []
current_position, all_targets = (), 0

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        current_position = (row, matrix[row].index("A"))

    all_targets += matrix[row].count("x")

moves_dict = {
    'right': (0, +1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (+1, 0)
}

hit_targets_coordinates = []

for i in range(int(input())):
    command = input().split()
    move_row, move_col = moves_dict[command[1]]

    if "move" in command:
        steps = int(command[2])
        current_position = move_command(steps, matrix, current_position, move_row, move_col)

    elif "shoot" in command:
        target_position = shoot_command(current_position, moves_dict[command[1]], matrix)
        if not target_position:
            continue
        all_targets -= 1
        hit_targets_coordinates.append(target_position)
        if all_targets <= 0:
            break

if not all_targets:
    print(f"Training completed! All {len(hit_targets_coordinates)} targets hit.")
else:
    print(f"Training not completed! {all_targets} targets left.")

[print(coordinates) for coordinates in hit_targets_coordinates]