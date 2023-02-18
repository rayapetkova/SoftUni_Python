vowels = ['a', 'o', 'u', 'e', 'i']


def func(text):
    output = [i for i in text if i not in vowels]
    return "".join(output)


current_text = input()
print(func(current_text))