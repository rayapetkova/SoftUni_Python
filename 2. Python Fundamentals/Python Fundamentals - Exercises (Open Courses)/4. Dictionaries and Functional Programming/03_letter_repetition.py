text = input()
dictionary = {}

for symbol in text:
    dictionary[symbol] = dictionary.get(symbol, 0) + 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")