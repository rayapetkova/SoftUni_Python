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

for num, (person_name, km) in enumerate(sorted(dict_with_names.items(), key=lambda x: -x[1]), 1):
    if num == 1:
        print(f"1st place: {person_name}")
    elif num == 2:
        print(f"2nd place: {person_name}")
    elif num == 3:
        print(f"3rd place: {person_name}")
