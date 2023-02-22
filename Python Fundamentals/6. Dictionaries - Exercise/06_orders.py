dictionary = {}

while True:
    command = input()
    if command == "buy":
        break
    line = command.split()
    name, price, quantity = line[0], float(line[1]), int(line[2])
    dictionary[name] = dictionary.get(name, [0, 0])

    dictionary[name][0] = price
    dictionary[name][1] += quantity

for key, values in dictionary.items():
    total = values[0] * values[1]
    print(f"{key} -> {total:.2f}")




#2
#
# dictionary = {}
#
# while True:
#     command = input()
#     if command == "buy":
#         break
#     line = command.split()
#     name, price, quantity = line[0], float(line[1]), int(line[2])
#     if name in dictionary.keys():
#         dictionary[name][0] = price
#         dictionary[name][1] += quantity
#     else:
#         dictionary[name] = [price, quantity]
#
# for key, values in dictionary.items():
#     total = values[0] * values[1]
#     print(f"{key} -> {total:.2f}")
