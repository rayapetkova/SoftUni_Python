def even_nums(numbers):
    int_numbers_list = list(map(int, numbers))
    idx_of_even_numbers = []

    for i, v in enumerate(int_numbers_list):
        if v % 2 == 0:
            idx_of_even_numbers.append(i)
    return idx_of_even_numbers


curr_numbers = input().split(", ")
print(even_nums(curr_numbers))