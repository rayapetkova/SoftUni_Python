def finish(end):
    if end == "End":
        return "End"


def add(people, train):
    train[-1] += people
    return train


def insert(index, people, train):
    train[index] += people


def leave(index, people, train):
    train[index] -= people


wagons = int(input())
curr_train = [0] * wagons


while True:
    command = input()
    if command == "End":
        print(curr_train)
        break

    command = command.split()

    if "add" in command:
        curr_people = int(command[1])
        add(curr_people, curr_train)
    elif "insert" in command:
        curr_idx = int(command[1])
        curr_people = int(command[2])
        insert(curr_idx, curr_people, curr_train)
    elif "leave" in command:
        curr_idx = int(command[1])
        curr_people = int(command[2])
        leave(curr_idx, curr_people, curr_train)
