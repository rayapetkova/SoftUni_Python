all_things = ["0" for i in range(1, 11)]

while True:
    command = input()
    if command == "End":
        new_all_things = [i for i in all_things if i != "0"]
        print(new_all_things)
        break
    command_list = command.split("-")
    idx = int(command_list[0]) - 1
    thing = str(command_list[1])
    all_things[idx] = thing
