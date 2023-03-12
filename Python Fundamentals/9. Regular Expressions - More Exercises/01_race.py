import re

names = input().split(",")
for i in range(len(names)):
    names[i] = names[i].strip()

dict_with_names = {}
letters_pattern = r"[a-zA-Z]"
digits_pattern = r"\d"

while True:
    info = input()
    if info == "end of race":
        break
    name = "".join(re.findall(letters_pattern, info))
    distance = "".join(re.findall(digits_pattern, info))
    if name in names:
        dict_with_names[name] = dict_with_names.get(name, 0) + (sum(int(n) for n in distance))

positions = {1: '1st', 2: '2nd', 3: '3rd'}
sorted_dict = sorted(dict_with_names.items(), key=lambda x: -x[1])

for num, (person_name, km) in enumerate(sorted_dict[:3], 1):
    print(f"{positions[num]} place: {person_name}")
