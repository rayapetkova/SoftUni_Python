import re

text = input()
cool_threshold = 1
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
all_found = []
cool_ones = []

for el in text:
    if el.isdigit():
        cool_threshold *= int(el)

valid_emojis = re.finditer(pattern, text)
for emoji in valid_emojis:
    all_found.append(emoji[0])
    total = 0
    for element in emoji[2]:
        total += ord(element)
    if total >= cool_threshold:
        cool_ones.append(emoji[0])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_found)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_ones:
    print(cool_emoji)