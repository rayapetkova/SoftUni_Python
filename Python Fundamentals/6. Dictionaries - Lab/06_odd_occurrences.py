words = list(map(lambda x: x.lower(), input().split()))
dictionary = {}

for i in words:
    if i not in dictionary.keys():
        dictionary[i] = 0
    dictionary[i] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")