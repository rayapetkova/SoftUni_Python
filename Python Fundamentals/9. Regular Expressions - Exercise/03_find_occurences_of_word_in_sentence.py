import re

text, word = input().lower(), input().lower()

final = re.findall(rf"\b({word})+\b", text)   # rf means that the regular expression can receive a variable

print(len(final))