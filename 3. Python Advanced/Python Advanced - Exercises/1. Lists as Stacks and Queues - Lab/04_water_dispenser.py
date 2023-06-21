from collections import deque

quantity = int(input())

people = deque()

while True:
    name = input()
    if name == "Start":
        break

    people.append(name)

while True:
    line = input()
    if line == "End":
        break

    if line.isdigit():
        liters = int(line)

        if quantity >= liters:
            print(f"{people.popleft()} got water")
            quantity -= liters
        else:
            print(f"{people.popleft()} must wait")

    else:
        command, liters = line.split()[0], int(line.split()[1])
        quantity += liters

print(f"{quantity} liters left")
