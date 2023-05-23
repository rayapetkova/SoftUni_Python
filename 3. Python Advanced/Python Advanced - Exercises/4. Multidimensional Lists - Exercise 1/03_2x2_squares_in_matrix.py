def check_valid_indices(curr_row, curr_col):
    if curr_row + 1 >= rows or curr_col + 1 >= cols:
        return False

    return True


def get_square_list(curr_row, curr_col, curr_matrix):
    square_characters = []

    for c_row in range(curr_row, curr_row + 2):
        for c_col in range(curr_col, curr_col + 2):
            square_characters.append(curr_matrix[c_row][c_col])

    return square_characters


def check_if_characters_are_same(square_lst):
    return len(set(square_lst)) == 1


rows, cols = [int(n) for n in input().split()]
matrix = []
total_square_matrices = 0

for row in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for col in range(cols):
        if not check_valid_indices(row, col):
            break

        square_chars_list = get_square_list(row, col, matrix)
        if check_if_characters_are_same(square_chars_list):
            total_square_matrices += 1

print(total_square_matrices)
