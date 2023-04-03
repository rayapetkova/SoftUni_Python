factor = int(input())
count = int(input())
list_name = []

for i in range(1, count + 1):
    list_name.append(i * factor)

print(list_name)