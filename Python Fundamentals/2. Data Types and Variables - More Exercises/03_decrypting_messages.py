key = int(input())
n = int(input())
word = ""

for i in range(1, n + 1):
    letter = input()
    letter_in_num = ord(letter)
    expected_letter = chr(letter_in_num + key)
    word += expected_letter

print(word)