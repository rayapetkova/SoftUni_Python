def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


def movement(all_moves, curr_move, bunny, curr_matrix):
    total, path_eggs = 0, []
    c_row = bunny[0] + all_moves[curr_move][0]
    c_col = bunny[1] + all_moves[curr_move][1]

    while True:
        if not check_valid_indices(c_row, c_col) or curr_matrix[c_row][c_col] == "X":
            break

        total += int(curr_matrix[c_row][c_col])
        path_eggs.append([c_row, c_col])
        c_row += all_moves[curr_move][0]
        c_col += all_moves[curr_move][1]

    return total, path_eggs


def print_result(directions_eggs: dict, biggest_amount_eggs: int):
    current_direction, current_path = directions_eggs[biggest_amount_eggs]
    print(current_direction)
    [print(coordinates) for coordinates in current_path]
    print(biggest_amount_eggs)


SIZE = int(input())
matrix = []
bunny_coordinates, traps = (), []

for row in range(SIZE):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_coordinates = (row, matrix[row].index("B"))

    traps.append(matrix[row].count("X"))

moves = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

biggest_total_eggs = 0
all_directions_eggs = {}

for move in moves:
    eggs, all_path = movement(moves, move, bunny_coordinates, matrix)

    if eggs >= biggest_total_eggs:
        biggest_total_eggs = eggs
        all_directions_eggs[eggs] = (move, all_path)

print_result(all_directions_eggs, biggest_total_eggs)
