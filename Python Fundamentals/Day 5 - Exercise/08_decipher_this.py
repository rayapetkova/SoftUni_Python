text = input().split()

number = []
for i in text:
    number = []
    num_to_letter = ""
    letter = ""
    counter = 0
    new_word = ""
    for letter in i:
        if letter.isnumeric():
            number.append(letter)
            counter += 1
            int_lst = [num for num in number]
            needed_num = int("".join(int_lst))
            num_to_letter = chr(needed_num)
        else:
            word = num_to_letter + i[counter:len(i)]
            if len(word) > 2:
                middle = word[2:-1]
                print(word[0] + word[-1] + middle + word[1], end=" ")
            else:
                print(word, end=" ")
            break
