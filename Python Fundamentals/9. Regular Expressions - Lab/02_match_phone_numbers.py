import re
numbers = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", numbers)

valid_numbers = []
for number in matches:
    valid_numbers.append(number.group())

print(", ".join(valid_numbers))