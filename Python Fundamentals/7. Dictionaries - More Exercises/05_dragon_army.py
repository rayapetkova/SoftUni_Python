num = int(input())

dragons_type = {}


def check_if_null(curr_type, curr_name, curr_dragons_type):
    if curr_dragons_type[curr_type][curr_name]["damage"] == "null":
        curr_dragons_type[curr_type][curr_name]["damage"] = 45
    if curr_dragons_type[curr_type][curr_name]["health"] == "null":
        curr_dragons_type[curr_type][curr_name]["health"] = 250
    if curr_dragons_type[curr_type][curr_name]["armor"] == "null":
        curr_dragons_type[curr_type][curr_name]["armor"] = 10


for _ in range(num):
    line = input().split()
    type, name, damage, health, armor = line[0], line[1], line[2], line[3], line[4]
    dragons_type[type] = dragons_type.get(type, {})
    dragons_type[type][name] = dragons_type[type].get(name, {})
    dragons_type[type][name]["damage"], dragons_type[type][name]["health"], dragons_type[type][name]["armor"] \
        = damage, health, armor
    check_if_null(type, name, dragons_type)

damage_total, health_total, armor_total = 0, 0, 0

for some_type, names in dragons_type.items():
    for some_name, some_values in names.items():
        damage_total += int(some_values["damage"])
        health_total += int(some_values["health"])
        armor_total += int(some_values["armor"])
    print(f"{some_type}::({damage_total / len(names):.2f}/{health_total / len(names):.2f}/{armor_total / len(names):.2f})")
    for some_name, some_values in sorted(names.items(), key=lambda x: x[0]):
        print(f"-{some_name} -> damage: {some_values['damage']}, health: {some_values['health']}, armor: {some_values['armor']}")

    damage_total, health_total, armor_total = 0, 0, 0