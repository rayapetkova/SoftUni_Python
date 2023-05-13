from collections import deque

materials = input().split()
magic_levels = deque(input().split())

dictionary = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_levels:
    material, magic_level = int(materials.pop()), int(magic_levels.popleft())
    present = material + magic_level
    if present < 100:
        if present % 2 == 0:
            material *= 2
            magic_level *= 3
            present = material + magic_level
        else:
            present *= 2

    elif present > 499:
        present /= 2

    if 100 <= present <= 199:
        dictionary['Gemstone'] += 1
    elif 200 <= present <= 299:
        dictionary['Porcelain Sculpture'] += 1
    elif 300 <= present <= 399:
        dictionary['Gold'] += 1
    elif 400 <= present <= 499:
        dictionary['Diamond Jewellery'] += 1

if (dictionary['Gemstone'] > 0 and dictionary['Porcelain Sculpture'] > 0) or \
        (dictionary['Gold'] > 0 and dictionary['Diamond Jewellery'] > 0):
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(m) for m in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(l) for l in magic_levels)}")


for key, value in sorted(dictionary.items()):
    if value > 0:
        print(f"{key}: {value}")
