numbers = [int(j) for j in input().split()]

while True:
    line = input()
    if line == "Finish":
        print(" ".join(str(x) for x in numbers))
        break
    command = line.split()
    if command[0] == "Add":
        value = int(command[1])
        numbers.append(value)
    elif command[0] == "Remove":
        value = int(command[1])
        if value in numbers:
            numbers.remove(value)
    elif command[0] == "Replace":
        value = int(command[1])
        if value in numbers:
            idx_value = numbers.index(value)
            numbers[idx_value] = int(command[2])
    elif command[0] == "Collapse":
        value = int(command[1])
        numbers = [i for i in numbers if i >= value]
