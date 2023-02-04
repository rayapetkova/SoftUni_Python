wagons = int(input())
train = [0] * wagons


while True:
    command = input()
    if command == "End":
        print(train)
        break

    command = command.split()

    if "add" in command:
        people = int(command[1])
        train[-1] += people
    elif "insert" in command:
        idx = int(command[1])
        people = int(command[2])
        train[idx] += people
    elif "leave" in command:
        idx = int(command[1])
        people = int(command[2])
        train[idx] -= people
