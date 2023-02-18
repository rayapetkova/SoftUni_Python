num = int(input())
dictionary = {}

for i in range(num):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

for key, values in dictionary.items():
    print(f"{key} - {f', '.join(values)}")





#2
#
# num = int(input())
# dictionary = {}
#
# for i in range(num):
#     word = input()
#     synonym = input()
#     dictionary[word] = dictionary.get(word, []) + [synonym]
#
# for key, values in dictionary.items():
#     print(f"{key} - {', '.join(values)}")




#3
#
# num = int(input())
# dictionary = {}
#
# for i in range(num):
#     word = input()
#     synonym = input()
#     if word in dictionary.keys():
#         dictionary[word] += f', {synonym}'
#     else:
#         dictionary[word] = synonym
#
# for key, values in dictionary.items():
#     print(f"{key} - {values}")
