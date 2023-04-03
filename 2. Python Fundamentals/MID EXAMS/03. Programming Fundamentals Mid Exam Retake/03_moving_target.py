def shoot(idx, power, targets):
    if 0 <= idx < len(targets):
        targets[idx] -= power
        if targets[idx] <= 0:
            targets.pop(idx)


def add(idx, value, targets):
    if 0 <= idx < len(targets):
        targets.insert(idx, value)
    else:
        print("Invalid placement!")


def strike(idx, radius, targets):
    if idx - radius >= 0 and idx + radius + 1 <= len(targets):
        del targets[idx - radius:idx + radius + 1]
    else:
        print(f"Strike missed!")


current_targets = [int(i) for i in input().split()]

while True:
    line = input()
    if line == "End":
        print(*current_targets, sep="|")
        break
    command = line.split()
    current_idx = int(command[1])
    if "Shoot" in command:
        current_power = int(command[2])
        shoot(current_idx, current_power, current_targets)
    elif "Add" in command:
        current_value = int(command[2])
        add(current_idx, current_value, current_targets)
    elif "Strike" in command:
        current_radius = int(command[2])
        strike(current_idx, current_radius, current_targets)
