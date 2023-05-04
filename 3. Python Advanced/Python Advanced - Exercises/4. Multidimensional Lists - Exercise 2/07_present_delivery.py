def step_on_cookies_cells(all_directions, curr_matrix, c_row, c_col, total_presents, nice_kids):
    for c_direction in all_directions:
        curr_row, curr_col = all_directions[c_direction][0] + c_row, all_directions[c_direction][1] + c_col
        if curr_matrix[curr_row][curr_col] == "V":
            nice_kids -= 1
        if curr_matrix[curr_row][curr_col] != "-":
            total_presents -= 1
            curr_matrix[curr_row][curr_col] = "-"
    return nice_kids, total_presents


presents = int(input())
SIZE = int(input())
matrix, santa, all_nice_kids = [], (), 0


for i in range(SIZE):
    current_row = input().split()
    matrix.append(current_row)
    if "S" in current_row:
        santa = (i, current_row.index("S"))
    all_nice_kids += current_row.count("V")

NICE_KIDS = all_nice_kids
matrix[santa[0]][santa[1]] = "-"

directions = {
    'left': (0, -1),
    'right': (0, +1),
    'up': (-1, 0),
    'down': (+1, 0)
}

while presents > 0:
    direction = input()
    if direction == "Christmas morning":
        matrix[santa[0]][santa[1]] = "S"
        break
    row, col = santa[0] + directions[direction][0], santa[1] + directions[direction][1]
    if matrix[row][col] == "V":
        all_nice_kids -= 1
        presents -= 1
    elif matrix[row][col] == "C":
        all_nice_kids, presents = step_on_cookies_cells(directions, matrix, row, col, presents, all_nice_kids)
    santa = (row, col)
    matrix[row][col] = "-"

if presents <= 0 and all_nice_kids:
    matrix[santa[0]][santa[1]] = "S"
    print(f"Santa ran out of presents!")
[print(' '.join(nested)) for nested in matrix]

if not all_nice_kids:
    print(f"Good job, Santa! {NICE_KIDS} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids} nice kid/s.")