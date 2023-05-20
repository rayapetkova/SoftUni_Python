def find_santa_and_nice_kids(curr_matrix):
    santa_pos, c_nice_kids = (), 0

    for r in range(SIZE):
        for c in range(SIZE):
            if curr_matrix[r][c] == "S":
                santa_pos = (r, c)
            elif curr_matrix[r][c] == "V":
                c_nice_kids += 1

    return santa_pos, c_nice_kids


def cookie_position(c_row, c_col, curr_matrix, all_directions):
    current_nice_kids, given_presents = 0, 0

    for position in all_directions.keys():
        r, c = c_row + all_directions[position][0], c_col + all_directions[position][1]

        if curr_matrix[r][c] == "V":
            current_nice_kids += 1
            given_presents += 1

        elif curr_matrix[r][c] == "X":
            given_presents += 1

        curr_matrix[r][c] = "-"

    return current_nice_kids, given_presents


presents = int(input())
SIZE = int(input())

matrix = [input().split() for _ in range(SIZE)]

santa, nice_kids = find_santa_and_nice_kids(matrix)
matrix[santa[0]][santa[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

nice_kids_presents = 0
while True:
    if presents <= 0:
        break

    direction = input()

    if direction == "Christmas morning":
        break

    row, col = santa[0] + directions[direction][0], santa[1] + directions[direction][1]

    if matrix[row][col] == "V":
        nice_kids_presents += 1
        presents -= 1

    elif matrix[row][col] == "C":
        cookie_nice_kids, cookie_given_presents = cookie_position(row, col, matrix, directions)
        nice_kids_presents += cookie_nice_kids
        presents -= cookie_given_presents

    matrix[row][col] = "-"
    santa = (row, col)

if presents <= 0 and nice_kids > nice_kids_presents:
    print(f"Santa ran out of presents!")

matrix[santa[0]][santa[1]] = "S"
[print(*nested) for nested in matrix]

if nice_kids_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids - nice_kids_presents} nice kid/s.")