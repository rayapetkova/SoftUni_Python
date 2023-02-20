text = input()

dictionary = {element: text.count(element) for element in text if element != " "}

for key, value in dictionary.items():
    print(f"{key} -> {value}")




#2
#
# text = input()
# dictionary = {}
#
# for element in text:
#     if element != " ":
#         dictionary[element] = text.count(element)
#
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
