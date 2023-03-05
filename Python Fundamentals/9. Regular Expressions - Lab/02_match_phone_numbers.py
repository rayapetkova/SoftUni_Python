import re
numbers = input()

pattern = re.finditer(r"\+359([ -])\d\1\d{3}\1\d{4}\b", numbers)

valid_numbers = []
for number in pattern:
    valid_numbers.append(number.group())

print(", ".join(valid_numbers))