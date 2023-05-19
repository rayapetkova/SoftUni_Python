from collections import deque

firework_effects = deque([int(n) for n in input().split(", ")])
explosive_power = [int(n) for n in input().split(", ")]

dictionary = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
firework_show_successful = False

while firework_effects and explosive_power:
    firework_effect, power = firework_effects.popleft(), explosive_power.pop()
    result = firework_effect + power

    if firework_effect <= 0:
        explosive_power.append(power)
        continue

    elif power <= 0:
        firework_effects.appendleft(firework_effect)
        continue

    if result % 3 == 0 and result % 5 != 0:
        dictionary['Palm Fireworks'] = dictionary.get('Palm Fireworks', 0) + 1

    elif result % 5 == 0 and result % 3 != 0:
        dictionary['Willow Fireworks'] = dictionary.get('Willow Fireworks', 0) + 1

    elif result % 3 == 0 and result % 5 == 0:
        dictionary['Crossette Fireworks'] = dictionary.get('Crossette Fireworks', 0) + 1

    else:
        firework_effect -= 1
        firework_effects.append(firework_effect)
        explosive_power.append(power)

    if dictionary['Palm Fireworks'] >= 3 and dictionary['Willow Fireworks'] >= 3 and dictionary['Crossette Fireworks'] >= 3:
        firework_show_successful = True
        break

if firework_show_successful:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(e) for e in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(p) for p in explosive_power)}")

for key, value in dictionary.items():
    print(f"{key}: {value}")