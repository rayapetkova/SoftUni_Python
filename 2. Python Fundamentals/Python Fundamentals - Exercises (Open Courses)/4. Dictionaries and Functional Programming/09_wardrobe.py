num = int(input())

dictionary = {}

for i in range(num + 1):
    line = input()
    if "->" not in line:
        current_colour, current_item = line.split(" ", 1)
        for key, value in dictionary.items():
            print(f"{key} clothes:")
            for some_item, number in value.items():
                if key == current_colour and current_item == some_item:
                    print(f"* {some_item} - {number} (found!)")
                else:
                    print(f"* {some_item} - {number}")
        break
    command = line.split(" -> ")
    colour = command[0]
    clothes = command[1].split(",")
    dictionary[colour] = dictionary.get(colour, {})
    for item in clothes:
        dictionary[colour][item] = dictionary[colour].get(item, 0) + 1