def find_alice_and_holes(curr_matrix):
    alice, rabbits = (), []
    for c_row in range(size):
        for c_col in range(size):

            if curr_matrix[c_row][c_col] == "A":
                alice = (c_row, c_col)
            elif curr_matrix[c_row][c_col] == "R":
                rabbits.append((c_row, c_col))

    return alice, rabbits


def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


def alice_movement(curr_matrix, curr_row, curr_col):
    if curr_matrix[curr_row][curr_col].isdigit():
        return int(curr_matrix[curr_row][curr_col])

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

while tea_bags < 10:
    line = input()
    row, col = moves[line][0], moves[line][1]
    move = (alice_coordinates[0] + row, alice_coordinates[1] + col)

    if not check_valid_indices(move[0], move[1]) or move in rabbit_holes:
        if move in rabbit_holes:
            matrix[move[0]][move[1]] = "*"
        print(f"Alice didn't make it to the tea party.")
        break

    movement = alice_movement(matrix, move[0], move[1])

    if movement:
        tea_bags += movement

    alice_coordinates = move
    matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
for nested in matrix:
    print(*nested, sep=" ")
