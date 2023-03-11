import re

text = input()
pattern = r"www\.[a-zA-Z0-9\-]+\.[\.a-z]+"
final = []

while text:
    valid_links = re.findall(pattern, text)
    for link in valid_links:
        print(link)
    text = input()
