dictionary = {}

while True:
    line = input()
    if ":" not in line:
        line = line.replace("_", " ")
        for el in dictionary[line]:
            print(el)
        break

    name, id, course = line.split(":")
    if course not in dictionary:
        dictionary[course] = []
    dictionary[course].append(f"{name} - {id}")




#2
#
# dictionary = {}
#
# while True:
#     line = input()
#     if ":" not in line:
#         line = line.replace("_", " ")
#         for el in dictionary[line]:
#             print(el)
#         break
#
#     name, id, course = line.split(":")
#     dictionary[course] = dictionary.get(course, []) + [f"{name} - {id}"]
