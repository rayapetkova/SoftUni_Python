import sys


def check_valid_indices(curr_row, curr_col, all_rows, all_cols):
    return curr_row + 2 < all_rows and curr_col + 2 < all_cols


def get_3x3_list(curr_row, curr_col, curr_matrix):
    square_list = []

    for c_row in range(curr_row, curr_row + 3):
        for c_col in range(curr_col, curr_col + 3):
            square_list.append(curr_matrix[c_row][c_col])

    return square_list


def print_final_result(curr_dictionary):
    biggest_key_sum = max(curr_dictionary.keys())
    print(f"Sum = {biggest_key_sum}")

    while dictionary_big_numbers[biggest_key_sum]:
        nested_list = dictionary_big_numbers[biggest_key_sum][:3]
        print(*nested_list, sep=" ")
        del dictionary_big_numbers[biggest_key_sum][:3]


rows, cols = [int(n) for n in input().split()]
matrix = []

for row in range(rows):
    numbers = [int(n) for n in input().split()]
    matrix.append(numbers)

biggest_number = -sys.maxsize
dictionary_big_numbers = {}

for row in range(rows):
    for col in range(cols):
        if not check_valid_indices(row, col, rows, cols):
            break

        square_list_nums = get_3x3_list(row, col, matrix)
        sum_square_list = sum(square_list_nums)
        if sum_square_list > biggest_number:
            biggest_number = sum_square_list
            dictionary_big_numbers[sum_square_list] = square_list_nums

print_final_result(dictionary_big_numbers)
