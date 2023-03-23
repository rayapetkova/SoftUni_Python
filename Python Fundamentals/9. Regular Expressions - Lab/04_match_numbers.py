import re

text = input()
pattern = r"(^|(?<=\s))-?(0|[1-9]\d*)(\.\d*)?($|(?=\s))"
valid_nums = re.finditer(pattern, text)

final = []
for number in valid_nums:
    final.append(number.group())

print(*final, sep=" ")