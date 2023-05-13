def check_valid_indices(c_row, c_col):
    return 0 <= c_row < SIZE and 0 <= c_col < SIZE


def bucket_pos(curr_matrix, c_row, c_col):
    total_col_points = 0
    for r in range(0, c_row):
        if curr_matrix[r][c_col].isdigit():
            total_col_points += int(curr_matrix[r][c_col])

    for second_r in range(c_row + 1, SIZE):
        if curr_matrix[second_r][c_col].isdigit():
            total_col_points += int(curr_matrix[second_r][c_col])

    return total_col_points


SIZE = 6
matrix = [input().split() for _ in range(SIZE)]

total_points = 0

for _ in range(3):
    throw = input().split(", ")
    row, col = int(throw[0][1:]), int(throw[1][:-1])

    if not check_valid_indices(row, col):
        continue

    if matrix[row][col] == "B":
        total_points += bucket_pos(matrix, row, col)
        matrix[row][col] = "-"

prize = ""

if 100 <= total_points <= 199:
    prize = "Football"
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
elif total_points >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")