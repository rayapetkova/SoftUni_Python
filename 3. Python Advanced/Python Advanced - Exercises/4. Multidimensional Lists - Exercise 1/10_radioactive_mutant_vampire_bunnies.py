from collections import deque


def find_player_and_bunnies(curr_matrix):
    player_pos, bunnies_positions = (), []
    for c_row in range(rows):
        for c_col in range(cols):

            if curr_matrix[c_row][c_col] == "P":
                player_pos = (c_row, c_col)
            elif curr_matrix[c_row][c_col] == "B":
                bunnies_positions.append((c_row, c_col))

    return player_pos, bunnies_positions


def check_player_win(current_row, current_col):
    return 0 <= current_row < rows and 0 <= current_col < cols


def check_if_position_is_bunny(current_row, current_col, curr_matrix):
    return curr_matrix[current_row][current_col] == "B"


def bunnies_spreading(found_bunnies, curr_matrix, commands_dict, player_indices):
    found_player = False
    for bunny in found_bunnies:
        for command in commands_dict:
            c_row = bunny[0] + commands_dict[command][0]
            c_col = bunny[1] + commands_dict[command][1]

            if 0 <= c_row < rows and 0 <= c_col < cols:
                if curr_matrix[c_row][c_col] == "P":
                    found_player = True

                curr_matrix[c_row][c_col] = "B"

    return found_player


rows, cols = [int(n) for n in input().split()]
matrix = []

for row in range(rows):
    matrix.append(list(input()))

positions = deque(list(input()))

all_commands = {
    'L': (0, -1),
    'R': (0, +1),
    'U': (-1, 0),
    'D': (+1, 0)
}

player_idx, bunnies = find_player_and_bunnies(matrix)
dead, dead_string = False, ""
won = False

while positions:
    position = positions.popleft()
    c_row = all_commands[position][0] + player_idx[0]
    c_col = all_commands[position][1] + player_idx[1]

    if not check_player_win(c_row, c_col):
        matrix[player_idx[0]][player_idx[1]] = "."
        bunnies_spreading(bunnies, matrix, all_commands, player_idx)
        won = True
        break

    if check_if_position_is_bunny(c_row, c_col, matrix):
        dead_string = f"dead: {c_row} {c_col}"
        matrix[player_idx[0]][player_idx[1]] = "B"
        bunnies_spreading(bunnies, matrix, all_commands, player_idx)
        dead = True
        break

    else:
        matrix[c_row][c_col] = "P"
        matrix[player_idx[0]][player_idx[1]] = "."
        player_idx = (c_row, c_col)

    if bunnies_spreading(bunnies, matrix, all_commands, player_idx):
        dead_string = f"dead: {player_idx[0]} {player_idx[1]}"
        matrix[player_idx[0]][player_idx[1]] = "B"
        dead = True
        break

    else:
        bunnies = find_player_and_bunnies(matrix)[1]


for nested_lst in matrix:
    print(*nested_lst, sep="")

if won:
    print(f"won: {player_idx[0]} {player_idx[1]}")
if dead:
    print(dead_string)
