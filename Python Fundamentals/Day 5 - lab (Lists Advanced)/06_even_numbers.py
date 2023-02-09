nums = [int(j) for j in input().split(", ")]
numbers = [i for i in range(len(nums)) if nums[int(i)] % 2 == 0]
print(numbers)




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
#
# nums = [int(j) for j in input().split(", ")]
# numbers = list(map(lambda x: x if nums[x] % 2 == 0 else 'not even', range(len(nums))))
# even_numbers = list(filter(lambda a: a != 'not even', numbers))
# print(even_numbers)