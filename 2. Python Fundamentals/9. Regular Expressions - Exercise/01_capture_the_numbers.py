import re

text = input()
pattern = r"\d+"
final = []

while text:
    numbers = re.findall(pattern, text)
    for num in numbers:
        final.append(num)
    text = input()

print(*final, sep=" ")