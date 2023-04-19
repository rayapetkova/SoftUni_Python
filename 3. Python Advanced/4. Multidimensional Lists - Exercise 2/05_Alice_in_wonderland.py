def find_alice_and_holes(curr_matrix):
    alice, rabbits = (), []
    for c_row in range(size):
        for c_col in range(size):
            if curr_matrix[c_row][c_col] == "A":
                alice = (c_row, c_col)
            elif curr_matrix[c_row][c_col] == "R":
                rabbits.append((c_row, c_col))
    return alice, rabbits


def check_valid_indices(matrix_size, curr_row, curr_col, alice_position):
    alice_row, alice_col = alice_position[0], alice_position[1]
    return 0 <= alice_row + curr_row < matrix_size and 0 <= alice_col + curr_col < matrix_size


def alice_movement(curr_matrix, alice_position, curr_row, curr_col):
    c_row, c_col = alice_position[0] + curr_row, alice_position[1] + curr_col
    if curr_matrix[c_row][c_col].isdigit():
        return int(curr_matrix[c_row][c_col])
    return False


size = int(input())
matrix = []

for crow in range(size):
    matrix.append(input().split())

moves = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

tea_bags = 0
alice_coordinates, rabbit_holes = find_alice_and_holes(matrix)
matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"

while True:
    line = input()
    row, col = moves[line][0], moves[line][1]
    move = (alice_coordinates[0] + row, alice_coordinates[1] + col)
    if not check_valid_indices(size, row, col, alice_coordinates) or move in rabbit_holes:
        if move in rabbit_holes:
            matrix[move[0]][move[1]] = "*"
        print(f"Alice didn't make it to the tea party.")
        break
    movement = alice_movement(matrix, alice_coordinates, row, col)
    if movement:
        tea_bags += movement
    alice_coordinates = move
    matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"
    if tea_bags >= 10:
        print(f"She did it! She went to the party.")
        break

for nested in matrix:
    print(*nested, sep=" ")
