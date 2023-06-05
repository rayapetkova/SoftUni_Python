import os
from string import punctuation

with open("txt_files/02_line_numbers.txt", "r") as text_file:
    lines = text_file.readlines()

output_txt_file = open("txt_files/02_line_numbers_output.txt", "a")

for i in range(1, len(lines) + 1):
    sentence = lines[i - 1]
    sentence = sentence.replace("\n", "")

    letters, punctuation_marks = 0, 0

    for el in sentence:
        if el.isalpha():
            letters += 1

        elif el in punctuation:
            punctuation_marks += 1

    output_txt_file.write(f"Line {i}: {sentence} ({letters})({punctuation_marks})\n")

output_txt_file.close()