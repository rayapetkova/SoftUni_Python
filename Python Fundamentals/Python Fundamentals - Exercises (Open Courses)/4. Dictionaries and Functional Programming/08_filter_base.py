def printing_results(curr_input, curr_dict):
    needed_dict = curr_dict[curr_input]
    for key, value in needed_dict.items():
        print(f"Name: {key}\n{curr_input}: {value}\n====================")


dictionary = {'Age': {}, 'Salary': {}, 'Position': {}}

while True:
    line = input()
    if line == "filter base":
        break
    command = line.split(" -> ")
    name = command[0]
    if command[1].isnumeric() and float(command[1]).is_integer():
        dictionary['Age'][name] = command[1]
    elif command[1].replace(".", "", 1).isnumeric():
        dictionary['Salary'][name] = command[1]
    else:
        dictionary['Position'][name] = command[1]

final_input = input()
printing_results(final_input, dictionary)
