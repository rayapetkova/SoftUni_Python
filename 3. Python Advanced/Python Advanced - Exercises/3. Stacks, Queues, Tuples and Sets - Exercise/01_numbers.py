first = set(int(n) for n in input().split())
second = set(int(n) for n in input().split())
num = int(input())

for i in range(num):
    line = input().split()

    if line[0] == "Add" and line[1] == "First":
        for el in line[2:]:
            first.add(int(el))

    elif line[0] == "Add" and line[1] == "Second":
        for el in line[2:]:
            second.add(int(el))

    elif line[0] == "Remove" and line[1] == "First":
        for el in line[2:]:
            first.discard(int(el))

    elif line[0] == "Remove" and line[1] == "Second":
        for el in line[2:]:
            second.discard(int(el))

    elif "Check" in line:
        if first.issubset(second) or second.issubset(first):
            print(True)

        else:
            print(False)

print(', '.join(str(n) for n in sorted(first)))
print(', '.join(str(n) for n in sorted(second)))






#2 - solved task with functions
#
# def adding_elements(command, curr_first, curr_second):
#     if command[1] == "First":
#         for el in command[2:]:
#             curr_first.add(int(el))
#     elif command[1] == "Second":
#         for el in command[2:]:
#             curr_second.add(int(el))
#
#
# def removing_elements(command, curr_first, curr_second):
#     if command[1] == "First":
#         for el in command[2:]:
#             curr_first.discard(int(el))
#     elif command[1] == "Second":
#         for el in command[2:]:
#             curr_second.discard(int(el))
#
#
# first = set(int(n) for n in input().split())
# second = set(int(n) for n in input().split())
# num = int(input())
#
# for i in range(num):
#     line = input().split()
#     if line[0] == "Add":
#         adding_elements(line, first, second)
#     elif line[0] == "Remove":
#         removing_elements(line, first, second)
#     elif "Check" in line:
#         if first.issubset(second) or second.issubset(first):
#             print(True)
#         else:
#             print(False)
#
# print(', '.join(str(n) for n in sorted(first)))
# print(', '.join(str(n) for n in sorted(second)))
