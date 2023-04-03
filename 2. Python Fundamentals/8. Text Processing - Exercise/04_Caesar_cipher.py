text = input()
new = ""

for el in text:
    ascii_value = ord(el) + 3
    new += chr(ascii_value)

print(new)




#2
#
# text = input()
# new = []
#
# new += [chr(ord(el) + 3) for el in text]
#
# print(*new, sep="")