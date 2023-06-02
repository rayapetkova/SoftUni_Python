from string import punctuation
symbols_lst = ["-", ",", ".", "!", "?"]

with open("all_files/text.txt", "r") as file:
    result = file.readlines()

print(result)

output = open("all_files/output_file", "a")

for i in range(len(result)):
    letters, symbols = 0, 0

    for el in result[i]:
        if el.isalpha():
            letters += 1

        elif el in punctuation:
            symbols += 1

    result[i] = result[i].replace("\n", "")
    output.write(f"Line {i + 1}: {result[i]} ({letters})({symbols})\n")
