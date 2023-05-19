from math import floor


def find_player(curr_matrix):
    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "P":
                return r, c


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < SIZE and 0 <= c_col < SIZE


def player_movement_out_of_matrix(c_row, c_col, c_direction):
    player_pos = ()

    if c_direction == "left":
        player_pos = (c_row, SIZE - 1)

    elif c_direction == "right":
        player_pos = (c_row, 0)

    elif c_direction == "up":
        player_pos = (SIZE - 1, c_col)

    elif c_direction == "down":
        player_pos = (0, c_col)

    return player_pos


SIZE = int(input())
matrix = [input().split() for _ in range(SIZE)]

player = find_player(matrix)

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

coins, lost = 0, False
player_path = []
player_path.append(f"[{player[0]}, {player[1]}]")

while coins < 100:
    direction = input()
    if direction not in directions.keys():
        continue

    row, col = player[0] + directions[direction][0], player[1] + directions[direction][1]

    if not check_valid_indices(row, col):
        player = player_movement_out_of_matrix(row, col, direction)
        row, col = player[0], player[1]

    if matrix[row][col].isdigit():
        coins += int(matrix[row][col])
        matrix[row][col] = "."

    elif matrix[row][col] == "X":
        coins = floor(coins / 2)
        player_path.append(f"[{row}, {col}]")
        lost = True
        break

    player = (row, col)
    player_path.append(f"[{row}, {col}]")

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")

if lost:
    print(f"Game over! You've collected {coins} coins.")

print(f"Your path:")
print('\n'.join(p for p in player_path))
