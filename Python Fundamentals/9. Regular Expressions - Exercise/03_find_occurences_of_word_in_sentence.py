import re

text, word = input().lower(), input().lower()

final = re.findall(r"\b({})+\b".format(word), text)

print(len(final))