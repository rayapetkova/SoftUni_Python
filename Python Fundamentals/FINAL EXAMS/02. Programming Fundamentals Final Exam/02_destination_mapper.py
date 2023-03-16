import re
text = input()
total = 0
final = []

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
valid_destinations = re.finditer(pattern, text)
for valid in valid_destinations:
    final.append(valid[2])
print(f"Destinations: {', '.join(final)}")
for word in final:
    total += len(word)
print(f"Travel Points: {total}")