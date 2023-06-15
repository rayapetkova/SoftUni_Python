from collections import deque

bomb_effects = deque([int(n) for n in input().split(", ")])
bomb_casings = [int(n) for n in input().split(", ")]

dictionary = {
    'Datura Bombs': [40, 0],
    'Cherry Bombs': [60, 0],
    'Smoke Decoy Bombs': [120, 0]
}

while bomb_effects and bomb_casings:
    if dictionary['Datura Bombs'][1] >= 3 and dictionary['Cherry Bombs'][1] >= 3 and dictionary['Smoke Decoy Bombs'][1] >= 3:
        break

    bomb_effect, bomb_casing = bomb_effects.popleft(), bomb_casings.pop()
    sum_values = bomb_effect + bomb_casing

    for kind_bomb, value in dictionary.items():
        if sum_values == value[0]:
            dictionary[kind_bomb][1] += 1
            break
    else:
        bomb_casing -= 5
        bomb_casings.append(bomb_casing)
        bomb_effects.appendleft(bomb_effect)

lst_values = []
for key, value in dictionary.items():
    if value[1] >= 3:
        lst_values.append(key)

if len(lst_values) == 3:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(e) for e in bomb_effects)}")

if not bomb_casings:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(e) for e in bomb_casings)}")


for type_bomb, value in sorted(dictionary.items()):
    print(f"{type_bomb}: {value[1]}")
