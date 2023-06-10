from collections import deque


def check_valid_indices(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def find_king_and_queens(curr_matrix):
    c_king, c_queens = (), deque()

    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "K":
                c_king = (r, c)
            elif curr_matrix[r][c] == "Q":
                c_queens.append((r, c))

    return c_king, c_queens


def move_queens(pos):
    for direction in directions:
        row, col = pos[0], pos[1]
        queens_standing_the_way = []

        while True:
            row += directions[direction][0]
            col += directions[direction][1]

            if not check_valid_indices(row, col):
                break

            if matrix[row][col] == "Q":
                queens_standing_the_way.append((row, col))

            elif matrix[row][col] == "K":
                if not queens_standing_the_way:
                    final.append([pos[0], pos[1]])
                break


SIZE = 8

matrix = [input().split() for i in range(SIZE)]

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
    'up_right': (-1, +1),
    'up_left': (-1, -1),
    'bottom_left': (+1, -1),
    'bottom_right': (+1, +1)
}

king, queens = find_king_and_queens(matrix)
final = []


for q in queens:
    move_queens(q)

if not final:
    print(f"The king is safe!")
else:
    [print(lst) for lst in final]
