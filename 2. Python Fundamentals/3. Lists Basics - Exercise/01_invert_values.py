given_nums = input().split(" ")
list_name = []

for i in given_nums:
    i = int(i)
    new_num = i * (-1)
    list_name.append(new_num)

print(list_name)