def find_white_and_black(curr_matrix):
    b, w = (), ()
    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "b":
                b = (r, c)
            elif curr_matrix[r][c] == "w":
                w = (r, c)
    return w, b


def check_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


SIZE = 8
matrix = [input().split() for i in range(SIZE)]

white, black = find_white_and_black(matrix)

diagonals = (
    (-1, -1),
    (-1, +1)
)

second_diagonals = (
    (+1, -1),
    (+1, +1)
)

letters = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

colors = ["white", "black"]
turn = 0
win = False

while True:
    if white[0] == 0:
        current_col = white[1]
        print(f"Game over! White pawn is promoted to a queen at {letters[current_col]}8.")
        break
    if black[0] == SIZE - 1:
        current_col = black[1]
        print(f"Game over! Black pawn is promoted to a queen at {letters[current_col]}1.")
        break

    move = colors[turn]
    if move == "white":
        for diagonal in diagonals:
            c_row, c_col = white[0] + diagonal[0], white[1] + diagonal[1]
            if not check_indices(c_row, c_col):
                continue
            if matrix[c_row][c_col] == "b":
                print(f"Game over! White win, capture on {letters[c_col]}{SIZE - c_row}.")
                win = True
                break

        row_white, col_white = white[0] - 1, white[1]
        matrix[white[0]][white[1]] = "-"
        white = (row_white, col_white)
        matrix[white[0]][white[1]] = "w"

    else:
        for second in second_diagonals:
            c_row, c_col = black[0] + second[0], black[1] + second[1]
            if not check_indices(c_row, c_col):
                continue
            if matrix[c_row][c_col] == "w":
                print(f"Game over! Black win, capture on {letters[c_col]}{SIZE - c_row}.")
                win = True
                break
        row_black, col_black = black[0] + 1, black[1]
        matrix[black[0]][black[1]] = "-"
        black = (row_black, col_black)
        matrix[black[0]][black[1]] = "b"

    if win:
        break

    turn += 1
    if turn == 2:
        turn = 0
