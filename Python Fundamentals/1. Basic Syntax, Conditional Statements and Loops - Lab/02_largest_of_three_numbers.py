import sys

a = 3
max_num = -sys.maxsize

for i in range(1, 4):
    new_number = int(input())
    if new_number > max_num:
        max_num = new_number

print(max_num)