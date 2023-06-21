num = int(input())
set_names = set()

for i in range(num):
    set_names.add(input())

[print(name) for name in set_names]
