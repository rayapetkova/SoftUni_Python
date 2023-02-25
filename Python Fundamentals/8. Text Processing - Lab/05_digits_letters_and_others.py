text = input()

digits = ''
letters = ''
symbols = ''

for element in text:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        letters += element
    else:
        symbols += element

print(digits)
print(letters)
print(symbols)