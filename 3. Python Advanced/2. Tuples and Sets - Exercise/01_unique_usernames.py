num = int(input())
unique_names_set = set()

for i in range(num):
    unique_names_set.add(input())

[print(name) for name in unique_names_set]