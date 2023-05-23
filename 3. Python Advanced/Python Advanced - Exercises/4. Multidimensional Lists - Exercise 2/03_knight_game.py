def find_knights(curr_matrix):
    knights = []
    for c_row in range(size):
        for c_col in range(size):
            if curr_matrix[c_row][c_col] == "K":
                knights.append((c_row, c_col))

    return knights


def check_valid_indices(c_row, c_col):
    return 0 <= c_row < size and 0 <= c_col < size


def one_knight_hits(c_knight: tuple, moves: tuple):
    all_hits = 0

    for c_row, c_col in moves:
        curr_row = c_knight[0] + c_row
        curr_col = c_knight[1] + c_col

        if check_valid_indices(curr_row, curr_col) and matrix[curr_row][curr_col] == "K":
            all_hits += 1

    return all_hits


def remove_biggest_hits(curr_dict):
    max_hits = max(curr_dict.keys())
    c_row = curr_dict[max_hits][0]
    c_col = curr_dict[max_hits][1]
    matrix[c_row][c_col] = "0"
    curr_dict.pop(max_hits)


size = int(input())
matrix = []

for row in range(size):
    matrix.append(list(input()))

knights_coordinates = find_knights(matrix)

all_moves = (
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, -1),
    (+2, +1)
)

biggest_hits = 0
all_knights = {}
removed_knights = 0

while True:
    for knight in knights_coordinates:
        knight_hits = one_knight_hits(knight, all_moves)

        if knight_hits > biggest_hits:
            biggest_hits = knight_hits
            all_knights[biggest_hits] = knight

    if not sum(all_knights.keys()):
        break

    knights_coordinates.remove(all_knights[biggest_hits])
    remove_biggest_hits(all_knights)
    removed_knights += 1
    all_knights = {}
    biggest_hits = 0

print(removed_knights)
