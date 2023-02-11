groceries = input().split("!")


while True:
    command1 = input()
    if command1 == "Go Shopping!":
        break
    command = command1.split()
    if "Urgent" in command:
        if command[1] not in groceries:
            groceries.insert(0, command[1])
    elif "Unnecessary" in command:
        if command[1] in groceries:
            groceries.remove(command[1])
    elif "Correct" in command:
        if command[1] in groceries:
            needed_idx = groceries.index(command[1])
            groceries[needed_idx] = command[2]
    elif "Rearrange" in command:
        if command[1] in groceries:
            groceries.remove(command[1])
            groceries.append(command[1])

print(", ".join(groceries))