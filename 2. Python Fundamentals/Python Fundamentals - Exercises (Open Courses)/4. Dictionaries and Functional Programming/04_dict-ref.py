dictionary = {}

while True:
    line = input()
    if line == "end":
        break
    command = line.split(" = ")
    name = command[0]
    if command[1].isnumeric():
        number = int(command[1])
        dictionary[name] = number
    else:
        second_name = command[1]
        if second_name in dictionary.keys():
            dictionary[name] = dictionary[second_name]

for key, value in dictionary.items():
    print(f"{key} === {value}")