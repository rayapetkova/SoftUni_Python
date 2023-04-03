import re

text = input()

tags_pattern = r"<([^<>]*)>"

found_tags = re.finditer(tags_pattern, text)
for tag in found_tags:
    if tag[1] != "title" and tag[1] != "/title" and tag[1] != "body" and tag[1] != "/body":
        text = text.replace(tag[1], "", 1)


text = text.replace("\\n", " ").replace("<>", " ").replace("</>", " ")

title_pattern = r"<title>(.+)<\/title>"
body_pattern = r"<body>(.+)<\/body>"

final = []
found_title = re.finditer(title_pattern, text)
found_body = re.finditer(body_pattern, text)

for title in found_title:
    final.append(title[1])
for body in found_body:
    final.append(body[1])

print(f"Title: {' '.join(final[0].split())}\nContent: {' '.join(final[1].split())}")