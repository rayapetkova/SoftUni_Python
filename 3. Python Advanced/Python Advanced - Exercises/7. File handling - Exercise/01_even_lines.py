import os

symbols = ["-", ",", ".", "!", "?"]
with open("txt_files/01_even_lines.txt", "r") as text_file:
    lines = text_file.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        sentence = lines[i]
        sentence = sentence.replace("\n", "")

        for s in symbols:
            sentence = sentence.replace(s, "@")

        print(' '.join(sentence.split()[::-1]))
