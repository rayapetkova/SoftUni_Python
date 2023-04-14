from collections import deque

materials = [int(n) for n in input().split()]
magic_levels = deque([int(n) for n in input().split()])

dictionary_all_toys = {
    150: 'Doll',
    250: 'Wooden Train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

dictionary_final = {}

while materials and magic_levels:
    material, magic_level = materials.pop(), magic_levels.popleft()
    if material == 0 and magic_level == 0:
        continue
    if material == 0:
        magic_levels.appendleft(magic_level)
        continue
    if magic_level == 0:
        materials.append(material)
        continue
    multiplication = material * magic_level
    if multiplication < 0:
        sum_values = material + magic_level
        materials.append(sum_values)
        continue
    if multiplication not in dictionary_all_toys.keys() and multiplication > 0:
        material += 15
        materials.append(material)
        continue
    toy = dictionary_all_toys[multiplication]
    dictionary_final[toy] = dictionary_final.get(toy, 0) + 1

if ('Doll' in dictionary_final and 'Wooden Train' in dictionary_final) or \
        ('Teddy bear' in dictionary_final and 'Bicycle' in dictionary_final):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(n) for n in materials[::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(n) for n in magic_levels)}")

sorted_final_dictionary = sorted(dictionary_final.items())
for some_toy, amount in sorted_final_dictionary:
    print(f"{some_toy}: {amount}")
