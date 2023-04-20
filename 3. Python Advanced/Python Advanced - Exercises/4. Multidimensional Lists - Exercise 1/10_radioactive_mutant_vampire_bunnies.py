from collections import deque


def find_player(curr_matrix):
    for c_row in range(rows):
        for c_col in range(cols):
            if curr_matrix[c_row][c_col] == "P":
                return c_row, c_col


def all_bunnies(curr_matrix):
    bunnies_list = []
    for c_row in range(rows):
        for c_col in range(cols):
            if curr_matrix[c_row][c_col] == "B":
                bunnies_list.append((c_row, c_col))
    return bunnies_list


def check_player_win(direction, curr_player_position):
    c_row = direction[0] + curr_player_position[0]
    c_col = direction[1] + curr_player_position[1]
    if 0 <= c_row < rows and 0 <= c_col < cols:
        return True
    return False


def check_if_position_is_bunny(direction, curr_player_position, curr_matrix):
    c_row = direction[0] + curr_player_position[0]
    c_col = direction[1] + curr_player_position[1]
    if curr_matrix[c_row][c_col] == "B":
        return True
    return False


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

player_idx = find_player(matrix)
bunnies = all_bunnies(matrix)
dead, dead_string = False, ""
won = False
while positions:
    position = positions.popleft()
    if not check_player_win(all_commands[position], player_idx):
        matrix[player_idx[0]][player_idx[1]] = "."
        bunnies_spreading(bunnies, matrix, all_commands, player_idx)
        won = True
        break
    c_row = all_commands[position][0] + player_idx[0]
    c_col = all_commands[position][1] + player_idx[1]
    if check_if_position_is_bunny(all_commands[position], player_idx, matrix):
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
        bunnies = all_bunnies(matrix)


for nested_lst in matrix:
    print(*nested_lst, sep="")

if won:
    print(f"won: {player_idx[0]} {player_idx[1]}")
if dead:
    print(dead_string)
