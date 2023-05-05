from collections import deque


def find_rover_and_deposits(curr_matrix):
    curr_rover, curr_deposits = (), {}
    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "E":
                curr_rover = (r, c)
            elif curr_matrix[r][c] == "W" or curr_matrix[r][c] == "M" or curr_matrix[r][c] == "C":
                curr_deposits[curr_matrix[r][c]] = curr_deposits.get(curr_matrix[r][c], []) + [(r, c)]
    return curr_rover, curr_deposits


def exact_type_deposit(c_row, c_col, curr_matrix):
    current_type = ""
    if curr_matrix[c_row][c_col] == "W":
        current_type = "Water"
    elif curr_matrix[c_row][c_col] == "M":
        current_type = "Metal"
    elif curr_matrix[c_row][c_col] == "C":
        current_type = "Concrete"
    return current_type


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < SIZE and 0 <= c_col < SIZE


def up_down_left_right(c_row, c_col):
    if c_row < 0:
        c_row = SIZE - 1
    elif c_row >= SIZE:
        c_row = 0
    if c_col < 0:
        c_col = SIZE - 1
    elif c_col >= SIZE:
        c_col = 0
    return c_row, c_col


SIZE = 6
matrix = [input().split() for i in range(SIZE)]

rover, deposits = find_rover_and_deposits(matrix)

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

commands = deque(input().split(", "))

found_deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0
}

for direction in commands:
    row, col = rover[0] + directions[direction][0], rover[1] + directions[direction][1]
    if not check_valid_indices(row, col):
        rover = up_down_left_right(row, col)
        row, col = rover
    if matrix[row][col] in deposits.keys():
        type_deposit = exact_type_deposit(row, col, matrix)
        print(f"{type_deposit} deposit found at ({row}, {col})")
        found_deposits[type_deposit] += 1
    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    rover = (row, col)

if all(value > 0 for value in found_deposits.values()):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
