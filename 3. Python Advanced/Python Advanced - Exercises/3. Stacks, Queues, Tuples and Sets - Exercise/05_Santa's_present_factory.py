from collections import deque

materials = [int(n) for n in input().split()]
magic_levels = deque(int(n) for n in input().split())

craft_presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

final = {}

while materials and magic_levels:
    material, magic = materials.pop(), magic_levels.popleft()
    total = material * magic

    if magic == 0 and material == 0:
        continue

    if material == 0:
        magic_levels.appendleft(magic)
        continue

    elif magic == 0:
        materials.append(material)
        continue

    if total in craft_presents:
        final[craft_presents[total]] = final.get(craft_presents[total], 0) + 1
    elif total < 0:
        total = material + magic
        materials.append(total)
    else:
        material += 15
        materials.append(material)

if ('Doll' in final.keys() and 'Wooden train' in final.keys()) or ('Teddy bear' in final.keys() and 'Bicycle' in final.keys()):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(n) for n in reversed(materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(n) for n in magic_levels)}")

sorted_final = sorted(final.items(), key=lambda x: x[0])
for element, number in sorted_final:
    print(f"{element}: {number}")