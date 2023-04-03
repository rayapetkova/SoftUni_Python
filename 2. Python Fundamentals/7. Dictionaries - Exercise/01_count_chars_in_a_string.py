text = input()

dictionary = {element: text.count(element) for element in text if not element.isspace()}

for key, value in dictionary.items():
    print(f"{key} -> {value}")




#2
#
# text = input()
# dictionary = {}
#
# for element in text:
#     if not element.isspace():
#         dictionary[element] = dictionary.get(element, 0) + 1
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")





#3
#
# text = input()
# dictionary = {}
#
# for element in text:
#     if not element.isspace() and element not in dictionary.keys():
#         dictionary[element] = text.count(element)
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
