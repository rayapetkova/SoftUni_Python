import re
text = input()
mirror_words = []
all_matches = 0

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

valid_pairs = re.finditer(pattern, text)

for valid in valid_pairs:
    if valid[2] == valid[3][::-1]:
        mirror_words.append(f"{valid[2]} <=> {valid[3]}")
    all_matches += 1

if all_matches == 0:
    print(f"No word pairs found!")
else:
    print(f"{all_matches} word pairs found!")
if not mirror_words:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")