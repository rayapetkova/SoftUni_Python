from collections import deque


def find_miner(curr_matrix):
    for c_row in range(size):
        for c_col in range(size):
            if curr_matrix[c_row][c_col] == "s":
                return c_row, c_col


def all_coal_in_field(curr_matrix):
    total = 0
    for c_row in range(size):
        for c_col in range(size):
            if curr_matrix[c_row][c_col] == "c":
                total += 1
    return total


def check_valid_indices(miner_indices, all_commands_dict, curr_command):
    if 0 <= all_commands_dict[curr_command][0] + miner_indices[0] < size and \
            0 <= all_commands_dict[curr_command][1] + miner_indices[1] < size:
        return True
    return False


def check_if_end(curr_matrix, miner_indices, command_indices):
    if curr_matrix[miner_indices[0] + command_indices[0]][miner_indices[1] + command_indices[1]] == "e":
        return True
    return False


size = int(input())
commands = deque(input().split())
matrix = []

for row in range(size):
    matrix.append(input().split())

all_commands = {
    "left": (0, -1),
    "right": (0, +1),
    "up": (-1, 0),
    "down": (+1, 0)
}

miner_idx = find_miner(matrix)
all_coal = all_coal_in_field(matrix)
printed_result = False

while commands:
    command = commands.popleft()
    if not check_valid_indices(miner_idx, all_commands, command):
        continue
    if check_if_end(matrix, miner_idx, all_commands[command]):
        row_idx, col_idx = miner_idx[0] + all_commands[command][0], miner_idx[1] + all_commands[command][1]
        print(f"Game over! ({row_idx}, {col_idx})")
        printed_result = True
        break
    if matrix[miner_idx[0] + all_commands[command][0]][miner_idx[1] + all_commands[command][1]] == "c":
        all_coal -= 1
    matrix[miner_idx[0] + all_commands[command][0]][miner_idx[1] + all_commands[command][1]] = "s"
    miner_idx = (miner_idx[0] + all_commands[command][0], miner_idx[1] + all_commands[command][1])
    if all_coal == 0:
        print(f"You collected all coal! ({miner_idx[0]}, {miner_idx[1]})")
        printed_result = True
        break

if not commands and not printed_result:
    print(f"{all_coal} pieces of coal left. ({miner_idx[0]}, {miner_idx[1]})")
