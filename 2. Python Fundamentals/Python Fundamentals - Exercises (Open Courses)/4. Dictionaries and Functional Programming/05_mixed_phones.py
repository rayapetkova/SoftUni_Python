dictionary = {}

while True:
    line = input()
    if line == "Over":
        break
    command = line.split(" : ")
    if command[1].isnumeric():
        name, number = command[0], command[1]
        dictionary[name] = number
    else:
        number, name = command[0], command[1]
    dictionary[name] = number

for key, value in sorted(dictionary.items()):
    print(f"{key} -> {value}")