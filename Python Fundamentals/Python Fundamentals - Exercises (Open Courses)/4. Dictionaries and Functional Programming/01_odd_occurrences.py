text = [n.lower() for n in input().split()]
dictionary = {}

for word in text:
    dictionary[word] = dictionary.get(word, 0) + 1

final = []
for key, value in dictionary.items():
    if value % 2 != 0:
        final.append(key)

print(*final, sep=", ")