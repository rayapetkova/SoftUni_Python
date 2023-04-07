from math import ceil

numbers = list(map(int, input().split(", ")))
max_value = max(numbers)
all_groups = ceil(max_value / 10)
group = 10

for i in range(all_groups):
    result_group = []
    for num in numbers:
        if group - 10 < num <= group:
            result_group.append(num)
    print(f"Group of {group}'s: {result_group}")
    group += 10
