numbers = input().split()
stack_nums = []

while numbers:
    stack_nums.append(numbers.pop())

print(" ".join(stack_nums))
