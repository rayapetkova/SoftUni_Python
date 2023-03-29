import re

numbers = input().split("|")[::-1]
final = []

new = [n for n in numbers if n and not n.isspace()]

for elements in new:
    valid_nums = re.finditer(r"-?\d+", elements)
    for valid in valid_nums:
        final.append(valid.group())

print(*final, sep=" ")