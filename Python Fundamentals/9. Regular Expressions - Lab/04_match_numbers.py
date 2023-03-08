import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
valid_nums = re.finditer(pattern, text)

final = []
for number in valid_nums:
    final.append(number.group())

print(*final, sep=" ")