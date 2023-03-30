def printing_result(last_line, curr_dict):
    for key, value in sorted(curr_dict.items()):
        if value[f"{last_line}"]:
            print(f"Name: {key}\n{last_line}: {value[f'{last_line}']}\n====================")


dictionary = {}

while True:
    line = input()
    if line == "filter base":
        break
    command = line.split(" -> ")
    name = command[0]
    dictionary[name] = dictionary.get(name, {'Age': 0, 'Salary': 0, 'Position': ""})
    if command[1].isnumeric() and float(command[1]).is_integer():
        dictionary[name]['Age'] = command[1]
    elif command[1].replace(".", "", 1).isnumeric():
        dictionary[name]['Salary'] = command[1]
    else:
        dictionary[name]['Position'] = command[1]

final_line = input()
if final_line == "Age":
    printing_result(final_line, dictionary)
elif final_line == "Salary":
    printing_result(final_line, dictionary)
elif final_line == "Position":
    printing_result(final_line, dictionary)
elif final_line == "Age":
    printing_result(final_line, dictionary)