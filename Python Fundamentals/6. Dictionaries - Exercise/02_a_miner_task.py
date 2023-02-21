resources = {}
elements = []

while True:
    command = input()
    if command == "stop":
        break
    elements.append(command)

for i in range(len(elements)):
    if i % 2 == 0:
        item, quantity = elements[i], int(elements[i + 1])
        resources[item] = resources.get(item, 0) + quantity

[print(f"{key} -> {value}") for key, value in resources.items()]
