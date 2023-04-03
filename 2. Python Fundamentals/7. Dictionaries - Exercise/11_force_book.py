sides = {}
found = False

while True:
    line = input()
    if line == "Lumpawaroo":
        break
    if "|" in line:
        force_side, force_user = line.split(" | ")
        for users in sides.values():
            if force_user in users:
                found = True
                break
        if not found:
            sides[force_side] = sides.get(force_side, []) + [force_user]
    else:
        force_user, force_side = line.split(" -> ")
        for key, value in sides.items():
            if force_user in value:
                sides[key].remove(force_user)
                break
        sides[force_side] = sides.get(force_side, []) + [force_user]
        print(f"{force_user} joins the {force_side} side!")

for key, value in sides.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        [print(f"! {name}") for name in value]