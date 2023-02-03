

def numbers(nums):
    int_input = [int(i) for i in nums]
    min_num = min(int_input)
    max_num = max(int_input)
    sum_nums = sum(int_input)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_nums}")


current_nums = input().split()
numbers(current_nums)
