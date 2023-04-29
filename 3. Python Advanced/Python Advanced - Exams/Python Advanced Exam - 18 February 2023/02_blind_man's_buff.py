def find_me(curr_matrix):
    for r in range(rows):
        for c in range(cols):
            if curr_matrix[r][c] == "B":
                return r, c


def check_valid_indices_and_obstacles(curr_matrix, my_pos, c_direction):
    curr_row, curr_col = my_pos[0] + c_direction[0], my_pos[1] + c_direction[1]
    return 0 <= curr_row < rows and 0 <= curr_col < cols and curr_matrix[curr_row][curr_col] != "O"


rows, cols = [int(n) for n in input().split()]
matrix = [input().split() for i in range(rows)]

my_position = find_me(matrix)

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'right': (0, +1),
    'left': (0, -1)
}

moves_made, touched_opponents = 0, 0
while True:
    direction = input()
    if direction == "Finish" or touched_opponents == 3:
        break
    direction_pos = directions[direction]
    if not check_valid_indices_and_obstacles(matrix, my_position, directions[direction]):
        continue
    row, col = my_position[0] + direction_pos[0], my_position[1] + direction_pos[1]
    if matrix[row][col] == "P":
        matrix[row][col] = "-"
        touched_opponents += 1
    moves_made += 1
    my_position = (row, col)

print(f"Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")