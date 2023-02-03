def numbers(nums):
    new_list = []
    int_nums = [int(i) for i in nums]
    for n in int_nums:
        if n % 2 == 0:
            new_list.append(n)
    print(new_list)


current_nums = input().split()
numbers(current_nums)