numbers = input().split(" ")
numbers_list = [int(j) for j in numbers]
removed_nums = int(input())

for i in range(1, removed_nums + 1):
    min_num = min(numbers_list)
    numbers_list.remove(min_num)

numbers_list_str = map(str, numbers_list)
print(', '.join(numbers_list_str))