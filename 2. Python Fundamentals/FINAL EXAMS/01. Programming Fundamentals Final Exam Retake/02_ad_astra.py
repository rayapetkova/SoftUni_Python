import re

text = input()

pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
total = 0
valid_texts = re.finditer(pattern, text)

for valid in valid_texts:
    total += int(valid["calories"])

days = int(total / 2000)
print(f"You have food to last you for: {days} days!")

valid_texts = re.finditer(pattern, text)
for valid1 in valid_texts:
    print(f"Item: {valid1['item']}, Best before: {valid1['date']}, Nutrition: {valid1['calories']}")