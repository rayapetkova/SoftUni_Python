def numbers(nums):
    for i in nums:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


current_nums = input().split(", ")
numbers(current_nums)




#2
#
# def numbers(nums):
#     for i in nums:
#         print(i == i[::-1])
#
#
# current_nums = input().split(", ")
# numbers(current_nums)
