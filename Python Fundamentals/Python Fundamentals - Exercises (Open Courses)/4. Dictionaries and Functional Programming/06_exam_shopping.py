dictionary = {}

while True:
    line = input()
    if line == "shopping time":
        break
    command = line.split()
    product, quantity = command[1], int(command[2])
    dictionary[product] = dictionary.get(product, 0) + quantity

while True:
    line = input()
    if line == "exam time":
        break
    command = line.split()
    product, quantity = command[1], int(command[2])
    if product not in dictionary.keys():
        print(f"{product} doesn't exist")
    elif dictionary[product] <= 0:
        print(f"{product} out of stock")
    else:
        dictionary[product] -= quantity

for key, value in dictionary.items():
    if value > 0:
        print(f"{key} -> {value}")