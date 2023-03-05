import re
names = input()

valid_names = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)
print(*valid_names, sep=" ")




#2
#
# import re
# names = input()
#
# valid_names = re.finditer(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)
#
# for name in valid_names:
#     print(name.group(), end=" ")
