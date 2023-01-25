first_word = input()
second_word = input()
new_word = ""

for i in range(len(first_word)):
    if first_word[i] == second_word[i]:
        continue
    new_word = second_word[:(i + 1)] + first_word[(i + 1):]
    if first_word == second_word:
        break
    print(new_word)