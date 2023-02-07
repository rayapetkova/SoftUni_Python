from math import ceil

numbers = list(map(int, input().split(", ")))

max_number = max(numbers)
needed_num = abs(ceil(max_number / 10))

new = [[] for i in range(needed_num)]
for i in range(needed_num):
    for b in numbers:
        if b <= (i + 1) * 10 and b > i * 10:
            new[i].append(b)

for i in range(1, needed_num + 1):
    print(f"Group of {i}0's: {new[i - 1]}")