from collections import deque
from colorama import Fore


def check_valid_idx(c_num, const):
    return 0 <= c_num < const


def put_round_disk(c, symbol):
    r = 0

    for c_row in range(ROWS):
        if matrix[c_row][c] != 0:
            matrix[c_row - 1][c] = symbol
            r = c_row - 1
            break

        if c_row == ROWS - 1:
            matrix[c_row][c] = symbol
            r = c_row
            break
    print(*matrix, sep="\n")
    return r


def check_win(c_directions, curr_row, curr_col, symbol):
    for direction in c_directions:
        counter_cells = 1

        for move in range(1, 5):
            row, col = curr_row + move * direction[0], curr_col + move * direction[1]

            if not check_valid_idx(row, ROWS) or not check_valid_idx(col, COLS):
                continue

            if matrix[row][col] == symbol:
                counter_cells += 1

                if counter_cells == 4:
                    return True

        for move in range(1, 5):
            row2, col2 = curr_row - move * direction[0], curr_col - move * direction[1]

            if not check_valid_idx(row2, ROWS) or not check_valid_idx(col2, COLS):
                continue

            if matrix[row2][col2] == symbol:
                counter_cells += 1

                if counter_cells == 4:
                    return True


ROWS, COLS = 6, 7

matrix = [[0] * COLS for r in range(ROWS)]

directions = (
    (-1, -1),  # top left diagonal
    (-1, 0),  # top
    (-1, +1),  # top right diagonal
    (0, -1),  # left
    (0, +1),  # right
    (+1, -1),  # bottom left diagonal
    (+1, 0),  # bottom
    (+1, +1),  # bottom right diagonal
)

player_1_symbol = input("What symbol would you like to play with? (player 1): ")
player_2_symbol = input("What symbol would you like to play with? (player 2): ")

players = deque([(1, player_1_symbol), (2, player_2_symbol)])

win = False

while not win:

    player = players[0]

    try:
        c_col = int(input(f"In which column would you like to put the round disk? (player {player[0]}): ")) - 1
        if not check_valid_idx(c_col, COLS):
            print(Fore.RED + "Please enter a valid column number." + Fore.RESET)
            continue

        if matrix[0][c_col] != 0:
            print(Fore.RED + f"No free space left in this column. Please choose another one." + Fore.RESET)
            continue

    except ValueError:
        print(Fore.RED + f"Please enter an integer number." + Fore.RESET)
        continue

    return_row = put_round_disk(c_col, player[1])

    if check_win(directions, return_row, c_col, player[1]):
        win = True
        print(*matrix, sep="\n")
        print(f"Player {player[0]} wins!")
        exit()

    players.append(players.popleft())
    print(*matrix, sep="\n")
