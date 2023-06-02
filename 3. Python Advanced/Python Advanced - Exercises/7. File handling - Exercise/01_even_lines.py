import os

symbols = ["-", ",", ".", "!", "?"]

with open('all_files/text.txt', 'r') as file:
    result = file.readlines()

for sentence in range(0, len(result), 2):
    for symbol in symbols:
        result[sentence] = result[sentence].replace(symbol, "@")

    result[sentence] = result[sentence].replace("\n", "")

    print(' '.join(result[sentence].split()[::-1]))