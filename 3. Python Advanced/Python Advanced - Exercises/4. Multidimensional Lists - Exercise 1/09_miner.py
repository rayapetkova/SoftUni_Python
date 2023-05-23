from collections import deque


def find_miner_and_coal(curr_matrix):
    miner_pos, total_coal = (), 0

    for c_row in range(size):
        for c_col in range(size):

            if curr_matrix[c_row][c_col] == "s":
                miner_pos = (c_row, c_col)

            elif curr_matrix[c_row][c_col] == "c":
                total_coal += 1

    return miner_pos, total_coal


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < size and 0 <= c_col < size


size = int(input())
commands = deque(input().split())
matrix = [input().split() for n in range(size)]

all_commands = {
    "left": (0, -1),
    "right": (0, +1),
    "up": (-1, 0),
    "down": (+1, 0)
}

miner_idx, all_coal = find_miner_and_coal(matrix)
printed_result = False

while commands:
    command = commands.popleft()
    row_idx = miner_idx[0] + all_commands[command][0]
    col_idx = miner_idx[1] + all_commands[command][1]

    if not check_valid_indices(row_idx, col_idx):
        continue

    if matrix[row_idx][col_idx] == "e":
        print(f"Game over! ({row_idx}, {col_idx})")
        printed_result = True
        break

    if matrix[row_idx][col_idx] == "c":
        all_coal -= 1

    matrix[row_idx][col_idx] = "s"
    miner_idx = (row_idx, col_idx)

    if all_coal == 0:
        print(f"You collected all coal! ({miner_idx[0]}, {miner_idx[1]})")
        printed_result = True
        break

if not commands and not printed_result:
    print(f"{all_coal} pieces of coal left. ({miner_idx[0]}, {miner_idx[1]})")
