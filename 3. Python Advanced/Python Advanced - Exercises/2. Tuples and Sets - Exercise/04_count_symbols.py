text = input()
dictionary_characters = {}

for element in text:
    dictionary_characters[element] = text.count(element)

sorted_dict = sorted(dictionary_characters.items())

for char, count_times in sorted_dict:
    print(f"{char}: {count_times} time/s")





#2
#
# text = input()
# dictionary_characters = {}
#
# for element in text:
#     dictionary_characters[element] = dictionary_characters.get(element, 0) + 1
#
# sorted_dict = sorted(dictionary_characters.items())
# for char, count_times in sorted_dict:
#     print(f"{char}: {count_times} time/s")
