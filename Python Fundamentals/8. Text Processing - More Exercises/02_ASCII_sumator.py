first_symbol, second_symbol,  text = ord(input()), ord(input()), input()
total = 0

for element in text:
    if first_symbol < ord(element) < second_symbol:
        total += ord(element)

print(total)




#2
#
# first_symbol, second_symbol,  text = ord(input()), ord(input()), input()
# print(sum([ord(element) for element in text if first_symbol < ord(element) < second_symbol]))
