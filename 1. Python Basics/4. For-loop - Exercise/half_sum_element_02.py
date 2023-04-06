import sys

n = int(input())
sum_nums = 0

max_num = -sys.maxsize

for i in range(0, n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum_nums = sum_nums + number

if max_num == sum_nums - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_nums)}")