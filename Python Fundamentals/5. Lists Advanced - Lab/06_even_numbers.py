# nums = [int(j) for j in input().split(", ")]
# numbers = [i for i in range(len(nums)) if nums[int(i)] % 2 == 0]
# print(numbers)




#2
#
# def even_nums(numbers):
#     int_numbers_list = list(map(int, numbers))
#     idx_of_even_numbers = []
#
#     for i, v in enumerate(int_numbers_list):
#         if v % 2 == 0:
#             idx_of_even_numbers.append(i)
#     return idx_of_even_numbers
#
#
# curr_numbers = input().split(", ")
# print(even_nums(curr_numbers))




#3


def even(nums):
    for i in nums:
        if nums[i] % 2 == 0 and nums[i] != 0:
            return "even"
        elif nums[i] == 0:
            return "zero"
        else:
            return "odd"


current_nums = [int(j) for j in input().split(", ")]
needed_func = even(current_nums)
numbers = list(map(needed_func, range(len(current_nums))))
print(numbers)