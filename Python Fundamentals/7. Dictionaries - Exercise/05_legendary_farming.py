
items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
not_found = True

while not_found:
    items = input().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i + 1].lower()
        if material in items_dict.keys():
            items_dict[material] += quantity
            if items_dict[material] >= 250:
                not_found = False
                break
        else:
            junk[material] = junk.get(material, 0) + quantity

name = ''

if items_dict['shards'] >= 250:
    name = "Shadowmourne"
    items_dict['shards'] -= 250
elif items_dict['fragments'] >= 250:
    name = "Valanyr"
    items_dict['fragments'] -= 250
elif items_dict['motes'] >= 250:
    name = "Dragonwrath"
    items_dict['motes'] -= 250

print(f"{name} obtained!")
[print(f"{element}: {number}") for element, number in items_dict.items()]
[print(f"{junk_element}: {junk_number}") for junk_element, junk_number in junk.items()]