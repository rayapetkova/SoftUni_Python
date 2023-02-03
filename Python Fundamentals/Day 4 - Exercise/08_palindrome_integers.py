def numbers(nums):
    for i in nums:
        list_i = list(i)
        if i == i[::-1]:
            print(True)
        else:
            print(False)


current_nums = input().split(", ")
numbers(current_nums)
