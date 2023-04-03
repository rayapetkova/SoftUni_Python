def sorted_nums(nums):
    int_nums = [int(i) for i in nums]
    print(sorted(int_nums))


current_nums = input().split()
sorted_nums(current_nums)