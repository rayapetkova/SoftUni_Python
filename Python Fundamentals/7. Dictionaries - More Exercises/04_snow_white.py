def different_dwarfs(dwarfs, name, hat_colour):
    dwarfs[hat_colour] = dwarfs.get(hat_colour, {})
    dwarfs[hat_colour][name] = dwarfs[hat_colour].get(name, 0)


def check_greater_physics(first, second):
    return first > second


current_dwarfs = {}
dwarfs_list = []

while True:
    line = input()
    if line == "Once upon a time":
        break
    dwarf_name, dwarf_hat_colour, dwarf_physics = [int(x) if x.isdigit() else x for x in line.split(" <:> ")]
    different_dwarfs(current_dwarfs, dwarf_name, dwarf_hat_colour)
    if check_greater_physics(dwarf_physics, current_dwarfs[dwarf_hat_colour][dwarf_name]):
        current_dwarfs[dwarf_hat_colour][dwarf_name] = dwarf_physics

for hat in current_dwarfs.keys():
    for name_dwarf, physics_dwarf in current_dwarfs[hat].items():
        dwarfs_list.append({"length": len(current_dwarfs[hat]), "hat_colour": hat, "dwarf name": name_dwarf, "dwarf physics": physics_dwarf})

for final in sorted(dwarfs_list, key=lambda x: (-x["dwarf physics"], -x["length"])):
    print(f"({final['hat_colour']}) {final['dwarf name']} <-> {final['dwarf physics']}")