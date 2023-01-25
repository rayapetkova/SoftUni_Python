word = input()
reversed_word = ""

for index in range(len(word) -1, -1, -1):
    letter = word[index]
    reversed_word = reversed_word + letter

print(reversed_word)