import sys


def create_square_list(curr_row, curr_col, curr_matrix):
    numbers = []

    for i in range(curr_row, curr_row + 2):
        for j in range(curr_col, curr_col + 2):
            numbers.append(curr_matrix[i][j])

    return numbers


def add_to_dictionary(curr_dict, big_number, curr_square_list):
    curr_dict[big_number] = curr_dict.get(big_number, curr_square_list)


def print_final_result(curr_dict):
    biggest_num_of_dict = max(curr_dict.keys())
    first_half = curr_dict[biggest_num_of_dict][:2]
    second_half = curr_dict[biggest_num_of_dict][2:]
    print(*first_half, sep=" ")
    print(*second_half, sep=" ")
    print(biggest_num_of_dict)


rows, cols = [int(n) for n in input().split(", ")]
matrix = []

for row in range(rows):
    nums = [int(num) for num in input().split(", ")]
    matrix.append(nums)

biggest_number = -sys.maxsize
dictionary_number_lst = {}

for row in range(rows):
    for col in range(cols):
        if row + 1 >= rows or col + 1 >= cols:
            break
        square_list = create_square_list(row, col, matrix)
        sum_square_list = sum(square_list)
        if sum_square_list > biggest_number:
            biggest_number = sum_square_list
            add_to_dictionary(dictionary_number_lst, sum_square_list, square_list)

print_final_result(dictionary_number_lst)
